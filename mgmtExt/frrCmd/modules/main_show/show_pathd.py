import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='ted',)
def frr_show_pathd_ted(show_pathd_ted_='show_pathd_ted'):
    """traffic eng"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pathd_ted.name
    
    if 'VIEW_NODE|show_pathd_ted' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pathd_ted'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pathd_ted']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pathd_ted'][key] = val
    
    # set VIEW_NODE -> show_pathd_ted table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pathd_ted'
    pass


@frr_show_pathd_ted.group(cls=FRR_AbbreviationGroup, name='database',)
def frr_show_pathd_ted_database(database_='database'):
    """database"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pathd_ted_database.name
    data_gen['database'] = database_='database'
    
    if 'VIEW_NODE|show_pathd_ted' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pathd_ted'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pathd_ted']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pathd_ted'][key] = val
    
    # set VIEW_NODE -> show_pathd_ted table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pathd_ted'
    pass


@frr_show_pathd_ted_database.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['verbose', 'json']), invoke_without_command=True)
def frr_show_pathd_ted_database_databasechoicecase():
    """verbose output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pathd_ted_database_databasechoicecase.name
    data_gen['DATABASE_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_pathd_ted' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pathd_ted'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pathd_ted']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pathd_ted'][key] = val
    
    # set VIEW_NODE -> show_pathd_ted table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pathd_ted'
    pass


@frr_show_pathd_ted_database_databasechoicecase.command('./	<cr>')
def frr_show_pathd_ted_database_databasechoicecase_cr():
    pass

