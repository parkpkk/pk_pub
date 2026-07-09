import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='length',)
def frr_terminal_length(terminal_length_='terminal_length'):
    """Set number of lines on a screen"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_terminal_length.name
    
    if 'VIEW_NODE|terminal_length' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|terminal_length'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|terminal_length']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|terminal_length'][key] = val
    
    # set VIEW_NODE -> terminal_length table
    COMMON_DATA_MAP['VIEW_NODE'] = 'terminal_length'
    pass


@frr_terminal_length.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(3, [(0, 512)]), invoke_without_command=True)
def frr_terminal_length_numberoflineson():
    """Number of lines on screen (0 for no pausing)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_terminal_length_numberoflineson.name
    data_gen['NUMBER_OF_LINES_ON'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|terminal_length' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|terminal_length'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|terminal_length']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|terminal_length'][key] = val
    
    # set VIEW_NODE -> terminal_length table
    COMMON_DATA_MAP['VIEW_NODE'] = 'terminal_length'
    pass


@frr_terminal_length_numberoflineson.command('./	<cr>')
def frr_terminal_length_numberoflineson_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='monitor', invoke_without_command=True)
def frr_terminal_monitor(terminal_monitor_='terminal_monitor'):
    """Receive log messages to active VTY session"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_terminal_monitor.name
    
    if 'VIEW_NODE|terminal_monitor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|terminal_monitor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|terminal_monitor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|terminal_monitor'][key] = val
    
    # set VIEW_NODE -> terminal_monitor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'terminal_monitor'
    pass


@frr_terminal_monitor.command('./	<cr>')
def frr_terminal_monitor_cr():
    pass


@frr_terminal_monitor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(3, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_terminal_monitor_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_terminal_monitor_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|terminal_monitor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|terminal_monitor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|terminal_monitor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|terminal_monitor'][key] = val
    
    # set VIEW_NODE -> terminal_monitor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'terminal_monitor'
    pass


@frr_terminal_monitor_daemonslist.command('./	<cr>')
def frr_terminal_monitor_daemonslist_cr():
    pass


@frr_terminal_monitor.group(cls=FRR_AbbreviationGroup, name='detach', invoke_without_command=True)
def frr_terminal_monitor_detach(detach_='detach'):
    """Keep logging feed open independent of VTY session"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_terminal_monitor_detach.name
    data_gen['detach'] = detach_='detach'
    
    if 'VIEW_NODE|terminal_monitor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|terminal_monitor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|terminal_monitor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|terminal_monitor'][key] = val
    
    # set VIEW_NODE -> terminal_monitor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'terminal_monitor'
    pass


@frr_terminal_monitor_detach.command('./	<cr>')
def frr_terminal_monitor_detach_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_terminal_no(terminal_no_='terminal_no'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_terminal_no.name
    
    if 'VIEW_NODE|terminal_no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|terminal_no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|terminal_no']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|terminal_no'][key] = val
    
    # set VIEW_NODE -> terminal_no table
    COMMON_DATA_MAP['VIEW_NODE'] = 'terminal_no'
    pass


@frr_terminal_no.group(cls=FRR_AbbreviationGroup, name='length', invoke_without_command=True)
def frr_terminal_no_length(length_='length'):
    """Set number of lines on a screen"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_terminal_no_length.name
    data_gen['length'] = length_='length'
    
    if 'VIEW_NODE|terminal_no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|terminal_no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|terminal_no']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|terminal_no'][key] = val
    
    # set VIEW_NODE -> terminal_no table
    COMMON_DATA_MAP['VIEW_NODE'] = 'terminal_no'
    pass


@frr_terminal_no_length.command('./	<cr>')
def frr_terminal_no_length_cr():
    pass


@frr_terminal_no.group(cls=FRR_AbbreviationGroup, name='monitor', invoke_without_command=True)
def frr_terminal_no_monitor(monitor_='monitor'):
    """Copy debug output to the current terminal line"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_terminal_no_monitor.name
    data_gen['monitor'] = monitor_='monitor'
    
    if 'VIEW_NODE|terminal_no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|terminal_no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|terminal_no']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|terminal_no'][key] = val
    
    # set VIEW_NODE -> terminal_no table
    COMMON_DATA_MAP['VIEW_NODE'] = 'terminal_no'
    pass


@frr_terminal_no_monitor.command('./	<cr>')
def frr_terminal_no_monitor_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='paginate', invoke_without_command=True)
def frr_terminal_paginate(paginate_='paginate'):
    """Use pager for output scrolling"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_terminal_paginate.name
    data_gen['paginate'] = paginate_='paginate'
    
    if 'VIEW_NODE|terminal' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|terminal'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|terminal']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|terminal'][key] = val
    
    # set VIEW_NODE -> terminal table
    COMMON_DATA_MAP['VIEW_NODE'] = 'terminal'
    pass


@frr_terminal_paginate.command('./	<cr>')
def frr_terminal_paginate_cr():
    pass

