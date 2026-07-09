import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(2, ['WORD']), invoke_without_command=True)
def frr_mtrace_multicasttraceroutefor():
    """Multicast trace route for multicast group address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_mtrace_multicasttraceroutefor.name
    data_gen['MULTICAST_TRACE_ROUTE_FOR'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|mtrace' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|mtrace'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|mtrace']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|mtrace'][key] = val
    
    # set VIEW_NODE -> mtrace table
    COMMON_DATA_MAP['VIEW_NODE'] = 'mtrace'
    pass


@frr_mtrace_multicasttraceroutefor.command('./	<cr>')
def frr_mtrace_multicasttraceroutefor_cr():
    pass

