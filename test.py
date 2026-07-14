import click
import ipaddress

import utilities_common.cli as clicommon
from .validated_config_db_connector import ValidatedConfigDBConnector

@click.group(cls=clicommon.AbbreviationGroup, name='test')
@click.argument('ipv4prefix', metavar='A.B.C.D/M', required=True, type=str)
@clicommon.pass_db
def test(db, ipv4prefix):
    """test-related 1st configuration tasks""" # help
    config_db = ValidatedConfigDBConnector(db.cfgdb)
    config_db.set_entry('TEST_NEW_CLI', 'test', {'IP_PREFIX': ipv4prefix})

    pass

@test.command('with')
@click.argument('ifname', metavar='INTERFACE', required=True, type=str)
@clicommon.pass_db
def test1(db, ifname):
    """test-related 2nd configuration tasks""" # help
    config_db = ValidatedConfigDBConnector(db.cfgdb)
    config_db.mod_entry('TEST_NEW_CLI','test', {'with': 'with'})
    config_db.mod_entry('TEST_NEW_CLI','test', {'IFNAME': ifname})
