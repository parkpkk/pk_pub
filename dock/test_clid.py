#!/usr/bin/env python3
import os
import sys
import time
from swsscommon import swsscommon
from sonic_py_common import daemon_base

SYSLOG_IDENTIFIER = "test_clid"
TEST_TABLE_NAME = "TEST_NEW_CLI"

class TestCliDaemon(daemon_base.DaemonBase):
    REDIS_TIMEOUT_MS = 100
    SELECT_TIMEOUT_MS = 100

    def __init__(self, log_identifier):
        super(TestCliDaemon, self).__init__(log_identifier)
                                    
        # 1. Initialize database connectors for SONiC core infrastructure
        self.config_db = swsscommon.DBConnector("CONFIG_DB", self.REDIS_TIMEOUT_MS, False)
        self.state_db = swsscommon.DBConnector("STATE_DB", self.REDIS_TIMEOUT_MS, False)

        # 2. Define the runtime status table inside STATE_DB (DB 6)
        self.test_state_table = swsscommon.Table(self.state_db, 'TEST_STATE')

    def process_test_event(self, key, op, fvp):
        """Callback function invoked when a configuration event occurs in TEST_NEW_CLI table from CONFIG_DB"""
        self.log_notice(f"Intercepted configuration event: Key={key}, Op={op}")
        self.log_notice(f"[TEST DAEMON] Key: {key}, Op: {op}, Data: {fvp}")
        print(f"[TEST DAEMON] Key: {key}, Op: {op}, Data: {fvp}")
        # Handle deletion event (DEL command from CLI)

        if op == "DEL":
            # Remove the corresponding state tracking entry from STATE_DB
            self.test_state_table._del(key)
            self.log_notice(f"Removed runtime state tracking for {key} from STATE_DB")

            return

        # Deserialize the FieldValuePairs (fvp) data into a dynamic map
        current_data = {}
        for k, v in fvp:
            current_data[k] = v

        # Extract parsed attributes for processing
        ip_prefix = current_data.get('IP_PREFIX', 'unknown')
        ifname = current_data.get('IFNAME', 'unknown')

        # 3. Construct new FieldValuePairs mapping to be pushed into STATE_DB
        state_pairs = [
                ("IP_PREFIX", ip_prefix),
                ("IFNAME", ifname),
                ("run_status", "executed"), # Mark the interface execution state as active/executed
                ("last_updated", time.strftime("%Y-%m-%d %H:%M:%S"))
        ]

        fvs = swsscommon.FieldValuePairs(state_pairs)

        # 4. Synchronize the execution state state directly to STATE_DB
        print(key)
        print(fvs)
        self.log_notice(key)
        self.log_notice(fvs)
        self.test_state_table.set(key, fvs)
        self.log_notice(f"Successfully synchronized 'executed' status for {key} to STATE_DB")

    def run(self):
        self.log_info("Initializing test_clid daemon execution flow...")

        if not os.geteuid() == 0:
                self.log_error("Root privileges required to run this system service daemon")
                sys.exit(1)

        # 5. Setup the core SWSS asynchronous select loop notification engine
        sel = swsscommon.Select()

        # Subscribe a state table listener to intercept data from CONFIG_DB
        sst_test_cli_confdb = swsscommon.SubscriberStateTable(self.config_db, TEST_TABLE_NAME)
        sel.addSelectable(sst_test_cli_confdb)
        self.log_info("CONFIG_DB event monitoring mechanism successfully established")
        print("[TEST DAEMON] Listening for inbound configuration commands from CLI...")

        # 6. Infinite poll engine loop (aligned with ptpcfgd system design architecture)
        while True:
            (state, selectableObj) = sel.select(self.SELECT_TIMEOUT_MS)

            if state == swsscommon.Select.OBJECT:
                fd = selectableObj.getFd()

                # Check if the triggered file descriptor matches our registered table channel
                if fd == sst_test_cli_confdb.getFd():
                    (key, op, fvp) = sst_test_cli_confdb.pop()

                    # Process the inbound database transaction and execute state updates
                    self.process_test_event(key, op, fvp)

def main():
    daemon = TestCliDaemon(SYSLOG_IDENTIFIER)
    daemon.run()

if __name__ == "__main__":
    main()
