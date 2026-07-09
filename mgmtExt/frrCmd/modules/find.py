import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(2, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'VIEW_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|find'][key] = val
    
    # set VIEW_NODE -> find table
    COMMON_DATA_MAP['VIEW_NODE'] = 'find'
    pass


@frr_find_fromsearchpattern.command('./	<cr>')
def frr_find_fromsearchpattern_cr():
    pass

