import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(2, ['FILENAME']),)
def frr_copy_configurationfiletoread():
    """1"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_copy_configurationfiletoread.name
    data_gen['CONFIGURATION_FILE_TO_READ'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|copy' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|copy'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|copy']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|copy'][key] = val
    
    # set VIEW_NODE -> copy table
    COMMON_DATA_MAP['VIEW_NODE'] = 'copy'
    pass


@frr_copy_configurationfiletoread.group(cls=FRR_AbbreviationGroup, name='running-config', invoke_without_command=True)
def frr_copy_configurationfiletoread_runningconfig(runningconfig_='running-config'):
    """Apply to current configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_copy_configurationfiletoread_runningconfig.name
    data_gen['running-config'] = runningconfig_='running-config'
    
    if 'VIEW_NODE|copy' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|copy'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|copy']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|copy'][key] = val
    
    # set VIEW_NODE -> copy table
    COMMON_DATA_MAP['VIEW_NODE'] = 'copy'
    pass


@frr_copy_configurationfiletoread_runningconfig.command('./	<cr>')
def frr_copy_configurationfiletoread_runningconfig_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='running-config',)
def frr_copy_runningconfig(copy_runningconfig_='copy_running-config'):
    """Copy running config to..."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_copy_runningconfig.name
    
    if 'VIEW_NODE|copy_running-config' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|copy_running-config'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|copy_running-config']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|copy_running-config'][key] = val
    
    # set VIEW_NODE -> copy_running-config table
    COMMON_DATA_MAP['VIEW_NODE'] = 'copy_running-config'
    pass


@frr_copy_runningconfig.group(cls=FRR_AbbreviationGroup, name='startup-config', invoke_without_command=True)
def frr_copy_runningconfig_startupconfig(startupconfig_='startup-config'):
    """Copy running config to startup config (same as write file/memory)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_copy_runningconfig_startupconfig.name
    data_gen['startup-config'] = startupconfig_='startup-config'
    
    if 'VIEW_NODE|copy_running-config' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|copy_running-config'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|copy_running-config']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|copy_running-config'][key] = val
    
    # set VIEW_NODE -> copy_running-config table
    COMMON_DATA_MAP['VIEW_NODE'] = 'copy_running-config'
    pass


@frr_copy_runningconfig_startupconfig.command('./	<cr>')
def frr_copy_runningconfig_startupconfig_cr():
    pass

