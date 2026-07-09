import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='ignore', invoke_without_command=True)
@click.argument('the_daemon_to_ignore', metavar='DAEMON', required=True, type=FRR_TYPE('DAEMON'))
def frr_watchfrr_ignore(the_daemon_to_ignore, ignore_='ignore'):
    """Ignore a specified daemon when it does not respond to echo request"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_watchfrr_ignore.name
    data_gen['ignore'] = ignore_='ignore'
    data_gen['THE_DAEMON_TO_IGNORE'] = the_daemon_to_ignore
    
    if 'VIEW_NODE|watchfrr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|watchfrr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|watchfrr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|watchfrr'][key] = val
    
    # set VIEW_NODE -> watchfrr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'watchfrr'
    pass


@frr_watchfrr_ignore.command('./	<cr>')
def frr_watchfrr_ignore_cr():
    pass

