import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(2, ['file', 'memory']), invoke_without_command=True)
def frr_write_configwritetarget():
    """Write to configuration file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_write_configwritetarget.name
    data_gen['CONFIG_WRITE_TARGET'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|write' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|write'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|write']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|write'][key] = val
    
    # set VIEW_NODE -> write table
    COMMON_DATA_MAP['VIEW_NODE'] = 'write'
    pass


@frr_write_configwritetarget.command('./	<cr>')
def frr_write_configwritetarget_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='integrated', invoke_without_command=True)
def frr_write_integrated(integrated_='integrated'):
    """Write integrated all-daemon frr.conf file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_write_integrated.name
    data_gen['integrated'] = integrated_='integrated'
    
    if 'VIEW_NODE|write' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|write'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|write']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|write'][key] = val
    
    # set VIEW_NODE -> write table
    COMMON_DATA_MAP['VIEW_NODE'] = 'write'
    pass


@frr_write_integrated.command('./	<cr>')
def frr_write_integrated_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(2, ['memory', 'file']), invoke_without_command=True)
def frr_write_storagetype():
    """Write configuration to the file (same as write file)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_write_storagetype.name
    data_gen['STORAGE_TYPE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|write' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|write'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|write']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|write'][key] = val
    
    # set VIEW_NODE -> write table
    COMMON_DATA_MAP['VIEW_NODE'] = 'write'
    pass


@frr_write_storagetype.command('./	<cr>')
def frr_write_storagetype_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='terminal', invoke_without_command=True)
def frr_write_terminal(write_terminal_='write_terminal'):
    """Write to terminal"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_write_terminal.name
    
    if 'VIEW_NODE|write_terminal' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|write_terminal'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|write_terminal']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|write_terminal'][key] = val
    
    # set VIEW_NODE -> write_terminal table
    COMMON_DATA_MAP['VIEW_NODE'] = 'write_terminal'
    pass


@frr_write_terminal.command('./	<cr>')
def frr_write_terminal_cr():
    pass


@frr_write_terminal.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(3, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_write_terminal_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_write_terminal_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|write_terminal' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|write_terminal'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|write_terminal']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|write_terminal'][key] = val
    
    # set VIEW_NODE -> write_terminal table
    COMMON_DATA_MAP['VIEW_NODE'] = 'write_terminal'
    pass


@frr_write_terminal_daemonslist.command('./	<cr>')
def frr_write_terminal_daemonslist_cr():
    pass


@frr_write_terminal_daemonslist.group(cls=FRR_AbbreviationGroup, name='no-header', invoke_without_command=True)
def frr_write_terminal_daemonslist_noheader(noheader_='no-header'):
    """Skip Building configuration... header"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_write_terminal_daemonslist_noheader.name
    data_gen['no-header'] = noheader_='no-header'
    
    if 'VIEW_NODE|write_terminal' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|write_terminal'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|write_terminal']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|write_terminal'][key] = val
    
    # set VIEW_NODE -> write_terminal table
    COMMON_DATA_MAP['VIEW_NODE'] = 'write_terminal'
    pass


@frr_write_terminal_daemonslist_noheader.command('./	<cr>')
def frr_write_terminal_daemonslist_noheader_cr():
    pass


@frr_write_terminal.group(cls=FRR_AbbreviationGroup, name='no-header', invoke_without_command=True)
def frr_write_terminal_noheader(noheader_='no-header'):
    """Skip Building configuration... header"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_write_terminal_noheader.name
    data_gen['no-header'] = noheader_='no-header'
    
    if 'VIEW_NODE|write_terminal' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|write_terminal'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|write_terminal']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|write_terminal'][key] = val
    
    # set VIEW_NODE -> write_terminal table
    COMMON_DATA_MAP['VIEW_NODE'] = 'write_terminal'
    pass


@frr_write_terminal_noheader.command('./	<cr>')
def frr_write_terminal_noheader_cr():
    pass

