# FRR/SONiC Command Tester

This tool tests and compares the execution of BGP configuration commands between a standard FRR `vtysh` instance and FRR running on a SONiC device. It connects to a target node via SSH, runs a series of predefined commands, and generates a report detailing the results.

---

## 1. Setup and Configuration

First, create a file named `config.yml` in the same directory as the scripts. Copy the contents below into that file and edit the values to match your environment.

```yaml
# ===================================================
# SSH Connection Details
# ===================================================
# Enter the connection info for your target device.
connection:
  host: "192.168.122.5"
  port: "22"
  user: "admin"
  # ⚠️ IMPORTANT: Replace with your actual password.
  password: "YourPaSsWoRd" 
  timeout: 3

# ===================================================
# Test Modules (Nodes)
# ===================================================
# Uncomment a module to enable it for testing.
# Comment out a module with '#' to disable it.
# In this example, only 'bgp' tests will run.
nodes:
  - VIEW_NODE
  - CONFIG_NODE
  # - BGP_NODE
  # - BGP_VNC_NVE_GROUP_NODE
  # - BGP_VNC_L2_GROUP_NODE
  # - BGP_VNC_DEFAULTS_NODE
  # - BGP_SRV6_NODE
  # - BFD_NODE
  # - BFD_PEER_NODE
  # - BMP_NODE
  # - BGP_VPNV6_NODE
  # - BGP_VPNV4_NODE
  # - BGP_EVPN_NODE
  # - BGP_IPV6M_NODE
  # - BGP_IPV6L_NODE
  # - BGP_FLOWSPECV6_NODE
  # - BGP_IPV6_NODE
  # - LDP_NODE
  # - BGP_IPV4M_NODE
  # - BGP_IPV4L_NODE
  # - BGP_FLOWSPECV4_NODE
  # - BGP_IPV4_NODE
  # - LDP_IPV4_NODE
  # - SEGMENT_ROUTING_NODE
  # - SR_TRAFFIC_ENG_NODE
  # - PCEP_NODE
  # - SRV6_NODE
  # - VRF_NODE
  # - RPKI_NODE
  # - RIPNG_NODE
  - RIP_NODE
  # - OSPF6_NODE
  - OSPF_NODE
  # - OPENFABRIC_NODE
  - ISIS_NODE
  # - EIGRP_NODE
  # - BABEL_NODE
  # - RMAP_NODE
  # - PW_NODE
  # - PBRMAP_NODE
  # - NH_GROUP_NODE
  # - VTY_NODE
  # - LDP_L2VPN_NODE
  # - KEYCHAIN_NODE
  # - INTERFACE_NODE
  # - BGP_EVPN_VNI_NODE
  # - KEYCHAIN_KEY_NODE
  # - LDP_IPV4_IFACE_NODE
  # - LDP_PSEUDOWIRE_NODE
  # - SRV6_LOCS_NODE
  # - LINK_PARAMS_NODE
  # - SR_POLICY_NODE
  # - SR_SEGMENT_LIST_NODE

# ===================================================
# Regex Placeholders
# ===================================================
# Define variables to be substituted into test commands.
# This makes tests reusable and easy to adapt.
# For example, 'INTERFACE' in a command will be 
# replaced with 'eth99'.
regexps:
  A.B.C.D/M: "1.1.1.1/32"
  A.B.C.D: "1.1.1.2"
  X:X::X:X/M: "2001:db8::1/128"
  X:X::X:X: "2001:db8::1"
  INTERFACE: "eth99"
  IFNAME: "eth88"
  
2. Install Prerequisites
Before running the test for the first time, execute the frrCmdTester_prerequisite.sh script to install the necessary Python packages.

You may need to make the script executable first:

$chmod +x frrCmdTester_prerequisite.sh

Then run the script:

$bash frrCmdTester_prerequisite.sh

3. Run the Test
Once your config.yml is saved and the prerequisites are installed, execute the main script from your terminal:

$python3 ssh_exec.py

OR

$run.sh

4. Understand the Results
The test results are saved to a .rst file named after the test module and timestamp (e.g., frrCmdTester_bgp_20250812_110248.rst).

Individual Command Log
The report shows a side-by-side execution for each command:

-----------
[#1062/1062][FRR]     vtysh -c 'configure terminal' -c 'router bgp 2694015005 view all' -c 'vnc nve-group NAME' -c 'exit-vnc' --> success
[#1062/1062][SONIC]   frr config router bgp 2694015005 view all  vnc nve-group NAME  exit-vnc --> success
[#1062/1062][compare] SAME
-----------
[FRR]: The command run on a standard FRR vtysh shell and its result.

[SONIC]: The equivalent command for the SONiC host's CLI and its result.

[compare]: The final status. SAME means both environments behaved as expected.

Final Summary
A summary at the end of the file gives a high-level overview:

End time 2025-08-12 09:53:21	duration 0:40:51.762284
Total clis: 1062
FRR success: 1062(rate: 100%)
FRR fail: 0
SONIC success: 1042(rate: 98%)
SONIC fail: 20