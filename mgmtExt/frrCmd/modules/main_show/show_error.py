import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(3, [(1, 4294967296), 'all']), invoke_without_command=True)
def frr_show_error_errorchoicecase():
    """Error code to get info about"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_error_errorchoicecase.name
    data_gen['ERROR_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_error_errorchoicecase.command('./	<cr>')
def frr_show_error_errorchoicecase_cr():
    pass


@frr_show_error_errorchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_error_errorchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_error_errorchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_error_errorchoicecase_json.command('./	<cr>')
def frr_show_error_errorchoicecase_json_cr():
    pass

