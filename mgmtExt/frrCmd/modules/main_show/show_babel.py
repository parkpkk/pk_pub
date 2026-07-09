import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_babel_interface(show_babel_interface_='show_babel_interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_babel_interface.name
    
    if 'VIEW_NODE|show_babel_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_babel_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_babel_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_babel_interface'][key] = val
    
    # set VIEW_NODE -> show_babel_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_babel_interface'
    pass


@frr_show_babel_interface.command('./	<cr>')
def frr_show_babel_interface_cr():
    pass


@frr_show_babel_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['IFNAME']), invoke_without_command=True)
def frr_show_babel_interface_interface():
    """Interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_babel_interface_interface.name
    data_gen['INTERFACE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_babel_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_babel_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_babel_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_babel_interface'][key] = val
    
    # set VIEW_NODE -> show_babel_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_babel_interface'
    pass


@frr_show_babel_interface_interface.command('./	<cr>')
def frr_show_babel_interface_interface_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
def frr_show_babel_neighbor(show_babel_neighbor_='show_babel_neighbor'):
    """Print neighbors"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_babel_neighbor.name
    
    if 'VIEW_NODE|show_babel_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_babel_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_babel_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_babel_neighbor'][key] = val
    
    # set VIEW_NODE -> show_babel_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_babel_neighbor'
    pass


@frr_show_babel_neighbor.command('./	<cr>')
def frr_show_babel_neighbor_cr():
    pass


@frr_show_babel_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['IFNAME']), invoke_without_command=True)
def frr_show_babel_neighbor_interface():
    """Interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_babel_neighbor_interface.name
    data_gen['INTERFACE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_babel_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_babel_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_babel_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_babel_neighbor'][key] = val
    
    # set VIEW_NODE -> show_babel_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_babel_neighbor'
    pass


@frr_show_babel_neighbor_interface.command('./	<cr>')
def frr_show_babel_neighbor_interface_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='parameters', invoke_without_command=True)
def frr_show_babel_parameters(parameters_='parameters'):
    """Configuration information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_babel_parameters.name
    data_gen['parameters'] = parameters_='parameters'
    
    if 'VIEW_NODE|show_babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_babel']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_babel'][key] = val
    
    # set VIEW_NODE -> show_babel table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_babel'
    pass


@frr_show_babel_parameters.command('./	<cr>')
def frr_show_babel_parameters_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
def frr_show_babel_route(show_babel_route_='show_babel_route'):
    """Babel internal routing table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_babel_route.name
    
    if 'VIEW_NODE|show_babel_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_babel_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_babel_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_babel_route'][key] = val
    
    # set VIEW_NODE -> show_babel_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_babel_route'
    pass


@frr_show_babel_route.command('./	<cr>')
def frr_show_babel_route_cr():
    pass


@frr_show_babel_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_babel_route_ipprefix():
    """IPv4 prefix <network>/<length>"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_babel_route_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_babel_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_babel_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_babel_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_babel_route'][key] = val
    
    # set VIEW_NODE -> show_babel_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_babel_route'
    pass


@frr_show_babel_route_ipprefix.command('./	<cr>')
def frr_show_babel_route_ipprefix_cr():
    pass


@frr_show_babel_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D']), invoke_without_command=True)
def frr_show_babel_route_ipv4address():
    """IPv4 address <network>/<length>"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_babel_route_ipv4address.name
    data_gen['IPV4_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_babel_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_babel_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_babel_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_babel_route'][key] = val
    
    # set VIEW_NODE -> show_babel_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_babel_route'
    pass


@frr_show_babel_route_ipv4address.command('./	<cr>')
def frr_show_babel_route_ipv4address_cr():
    pass


@frr_show_babel_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['X:X::X:X']), invoke_without_command=True)
def frr_show_babel_route_ipv6address():
    """IPv6 address <network>/<length>"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_babel_route_ipv6address.name
    data_gen['IPV6_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_babel_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_babel_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_babel_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_babel_route'][key] = val
    
    # set VIEW_NODE -> show_babel_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_babel_route'
    pass


@frr_show_babel_route_ipv6address.command('./	<cr>')
def frr_show_babel_route_ipv6address_cr():
    pass

