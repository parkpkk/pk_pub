import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='cpu', invoke_without_command=True)
def frr_show_thread_cpu(show_thread_cpu_='show_thread_cpu'):
    """Thread CPU usage"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_thread_cpu.name
    
    if 'VIEW_NODE|show_thread_cpu' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_thread_cpu'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_thread_cpu']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_thread_cpu'][key] = val
    
    # set VIEW_NODE -> show_thread_cpu table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_thread_cpu'
    pass


@frr_show_thread_cpu.command('./	<cr>')
def frr_show_thread_cpu_cr():
    pass


@frr_show_thread_cpu.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['FILTER']), invoke_without_command=True)
def frr_show_thread_cpu_displayfilter():
    """Display filter (rwtex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_thread_cpu_displayfilter.name
    data_gen['DISPLAY_FILTER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_thread_cpu' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_thread_cpu'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_thread_cpu']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_thread_cpu'][key] = val
    
    # set VIEW_NODE -> show_thread_cpu table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_thread_cpu'
    pass


@frr_show_thread_cpu_displayfilter.command('./	<cr>')
def frr_show_thread_cpu_displayfilter_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='poll', invoke_without_command=True)
def frr_show_thread_poll(poll_='poll'):
    """Show poll FD's and information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_thread_poll.name
    data_gen['poll'] = poll_='poll'
    
    if 'VIEW_NODE|show_thread' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_thread'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_thread']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_thread'][key] = val
    
    # set VIEW_NODE -> show_thread table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_thread'
    pass


@frr_show_thread_poll.command('./	<cr>')
def frr_show_thread_poll_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='timers', invoke_without_command=True)
def frr_show_thread_timers(timers_='timers'):
    """Show all timers and how long they have in the system"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_thread_timers.name
    data_gen['timers'] = timers_='timers'
    
    if 'VIEW_NODE|show_thread' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_thread'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_thread']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_thread'][key] = val
    
    # set VIEW_NODE -> show_thread table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_thread'
    pass


@frr_show_thread_timers.command('./	<cr>')
def frr_show_thread_timers_cr():
    pass

