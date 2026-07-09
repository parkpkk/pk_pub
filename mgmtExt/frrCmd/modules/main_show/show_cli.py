import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='graph', invoke_without_command=True)
def frr_show_cli_graph(graph_='graph'):
    """Dump current command space as DOT graph"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_cli_graph.name
    data_gen['graph'] = graph_='graph'
    
    if 'VIEW_NODE|show_cli' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_cli'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_cli']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_cli'][key] = val
    
    # set VIEW_NODE -> show_cli table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_cli'
    pass


@frr_show_cli_graph.command('./	<cr>')
def frr_show_cli_graph_cr():
    pass

