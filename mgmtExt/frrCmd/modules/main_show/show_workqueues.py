import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(3, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_workqueues_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_workqueues_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_work-queues' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_work-queues'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_work-queues']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_work-queues'][key] = val
    
    # set VIEW_NODE -> show_work-queues table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_work-queues'
    pass


@frr_show_workqueues_daemonslist.command('./	<cr>')
def frr_show_workqueues_daemonslist_cr():
    pass

