import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='exclusive', invoke_without_command=True)
def frr_configure_exclusive(exclusive_='exclusive'):
    """Configure exclusively from this terminal"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_configure_exclusive.name
    data_gen['exclusive'] = exclusive_='exclusive'
    
    if 'VIEW_NODE|configure' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|configure'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|configure']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|configure'][key] = val
    
    # set VIEW_NODE -> configure table
    COMMON_DATA_MAP['VIEW_NODE'] = 'configure'
    pass


@frr_configure_exclusive.command('./	<cr>')
def frr_configure_exclusive_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='private', invoke_without_command=True)
def frr_configure_private(private_='private'):
    """Configure using a private candidate configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_configure_private.name
    data_gen['private'] = private_='private'
    
    if 'VIEW_NODE|configure' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|configure'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|configure']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|configure'][key] = val
    
    # set VIEW_NODE -> configure table
    COMMON_DATA_MAP['VIEW_NODE'] = 'configure'
    pass


@frr_configure_private.command('./	<cr>')
def frr_configure_private_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='terminal', invoke_without_command=True)
def frr_configure_terminal(terminal_='terminal'):
    """Configuration terminal"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_configure_terminal.name
    data_gen['terminal'] = terminal_='terminal'
    
    if 'VIEW_NODE|configure' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|configure'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|configure']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|configure'][key] = val
    
    # set VIEW_NODE -> configure table
    COMMON_DATA_MAP['VIEW_NODE'] = 'configure'
    pass


@frr_configure_terminal.command('./	<cr>')
def frr_configure_terminal_cr():
    pass

