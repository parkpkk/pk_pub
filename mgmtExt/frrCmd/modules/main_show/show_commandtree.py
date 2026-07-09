import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_show_commandtree_permutations(permutations_='permutations'):
    """Permutations that we are interested in"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_commandtree_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'VIEW_NODE|show_commandtree' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_commandtree'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_commandtree']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_commandtree'][key] = val
    
    # set VIEW_NODE -> show_commandtree table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_commandtree'
    pass


@frr_show_commandtree_permutations.command('./	<cr>')
def frr_show_commandtree_permutations_cr():
    pass

