import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='filter-text', invoke_without_command=True)
def frr_show_logging_filtertext(filtertext_='filter-text'):
    """Filter Logs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_logging_filtertext.name
    data_gen['filter-text'] = filtertext_='filter-text'
    
    if 'VIEW_NODE|show_logging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_logging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_logging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_logging'][key] = val
    
    # set VIEW_NODE -> show_logging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_logging'
    pass


@frr_show_logging_filtertext.command('./	<cr>')
def frr_show_logging_filtertext_cr():
    pass

