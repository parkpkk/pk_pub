import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'VIEW_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|list'][key] = val
    
    # set VIEW_NODE -> list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'list'
    pass


@frr_list_permutations.command('./	<cr>')
def frr_list_permutations_cr():
    pass

