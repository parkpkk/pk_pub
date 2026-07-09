import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
@click.argument('only_show_vrrp_instances', metavar='INTERFACE', required=True, type=FRR_TYPE('INTERFACE'))
def frr_show_vrrp_interface(only_show_vrrp_instances, interface_='interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_interface.name
    data_gen['interface'] = interface_='interface'
    data_gen['ONLY_SHOW_VRRP_INSTANCES'] = only_show_vrrp_instances
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_interface.command('./	<cr>')
def frr_show_vrrp_interface_cr():
    pass


@frr_show_vrrp_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_vrrp_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_interface_json.command('./	<cr>')
def frr_show_vrrp_interface_json_cr():
    pass


@frr_show_vrrp_interface.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_vrrp_interface_summary(summary_='summary'):
    """Summarize all VRRP instances"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_interface_summary.name
    data_gen['summary'] = summary_='summary'
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_interface_summary.command('./	<cr>')
def frr_show_vrrp_interface_summary_cr():
    pass


@frr_show_vrrp_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, [(1, 255)]), invoke_without_command=True)
def frr_show_vrrp_interface_virtualrouterid():
    """Virtual Router ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_interface_virtualrouterid.name
    data_gen['VIRTUAL_ROUTER_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_interface_virtualrouterid.command('./	<cr>')
def frr_show_vrrp_interface_virtualrouterid_cr():
    pass


@frr_show_vrrp_interface_virtualrouterid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_vrrp_interface_virtualrouterid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_interface_virtualrouterid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_interface_virtualrouterid_json.command('./	<cr>')
def frr_show_vrrp_interface_virtualrouterid_json_cr():
    pass


@frr_show_vrrp_interface_virtualrouterid.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_vrrp_interface_virtualrouterid_summary(summary_='summary'):
    """Summarize all VRRP instances"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_interface_virtualrouterid_summary.name
    data_gen['summary'] = summary_='summary'
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_interface_virtualrouterid_summary.command('./	<cr>')
def frr_show_vrrp_interface_virtualrouterid_summary_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_vrrp_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_json.command('./	<cr>')
def frr_show_vrrp_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_vrrp_summary(summary_='summary'):
    """Summarize all VRRP instances"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_summary.name
    data_gen['summary'] = summary_='summary'
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_summary.command('./	<cr>')
def frr_show_vrrp_summary_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(3, [(1, 255)]), invoke_without_command=True)
def frr_show_vrrp_virtualrouterid():
    """Virtual Router ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_virtualrouterid.name
    data_gen['VIRTUAL_ROUTER_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_virtualrouterid.command('./	<cr>')
def frr_show_vrrp_virtualrouterid_cr():
    pass


@frr_show_vrrp_virtualrouterid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_vrrp_virtualrouterid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_virtualrouterid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_virtualrouterid_json.command('./	<cr>')
def frr_show_vrrp_virtualrouterid_json_cr():
    pass


@frr_show_vrrp_virtualrouterid.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_vrrp_virtualrouterid_summary(summary_='summary'):
    """Summarize all VRRP instances"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp_virtualrouterid_summary.name
    data_gen['summary'] = summary_='summary'
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp_virtualrouterid_summary.command('./	<cr>')
def frr_show_vrrp_virtualrouterid_summary_cr():
    pass

