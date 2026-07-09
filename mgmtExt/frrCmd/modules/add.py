import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='vnc',)
def frr_add_vnc(add_vnc_='add_vnc'):
    """VNC Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc.name
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc.group(cls=FRR_AbbreviationGroup, name='mac',)
@click.argument('mac_address', metavar='X:X:X:X:X:X', required=True, type=FRR_TYPE('X:X:X:X:X:X'))
def frr_add_vnc_mac(mac_address, mac_='mac'):
    """Add/modify mac address information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac.name
    data_gen['mac'] = mac_='mac'
    data_gen['MAC_ADDRESS'] = mac_address
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac.group(cls=FRR_AbbreviationGroup, name='virtual-network-identifier',)
@click.argument('virtual_network_identifier', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_add_vnc_mac_virtualnetworkidentifier(virtual_network_identifier, virtualnetworkidentifier_='virtual-network-identifier'):
    """Virtual Network Identifier follows"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier.name
    data_gen['virtual-network-identifier'] = virtualnetworkidentifier_='virtual-network-identifier'
    data_gen['VIRTUAL_NETWORK_IDENTIFIER'] = virtual_network_identifier
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier.group(cls=FRR_AbbreviationGroup, name='vn',)
def frr_add_vnc_mac_virtualnetworkidentifier_vn(vn_='vn'):
    """VN address of NVE"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn.name
    data_gen['vn'] = vn_='vn'
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', 'X:X::X:X']),)
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress.name
    data_gen['VN_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress.group(cls=FRR_AbbreviationGroup, name='un',)
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un(un_='un'):
    """UN address of NVE"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un.name
    data_gen['un'] = un_='un'
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress():
    """UN IPv4 interface address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress.name
    data_gen['UN_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress.command('./	<cr>')
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_cr():
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('cost_value', metavar='(0-255)', required=True, type=FRR_TYPE((0, 255)))
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_cost(cost_value, cost_='cost'):
    """Administrative cost [default: 255]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['COST_VALUE'] = cost_value
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_cost.command('./	<cr>')
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_cost_cr():
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_cost.group(cls=FRR_AbbreviationGroup, name='lifetime', invoke_without_command=True)
@click.argument('lifetime_value_in_seconds', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_cost_lifetime(lifetime_value_in_seconds, lifetime_='lifetime'):
    """Registration lifetime [default: infinite]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_cost_lifetime.name
    data_gen['lifetime'] = lifetime_='lifetime'
    data_gen['LIFETIME_VALUE_IN_SECONDS'] = lifetime_value_in_seconds
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_cost_lifetime.command('./	<cr>')
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_cost_lifetime_cr():
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress.group(cls=FRR_AbbreviationGroup, name='lifetime', invoke_without_command=True)
@click.argument('lifetime_value_in_seconds', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_lifetime(lifetime_value_in_seconds, lifetime_='lifetime'):
    """Registration lifetime [default: infinite]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_lifetime.name
    data_gen['lifetime'] = lifetime_='lifetime'
    data_gen['LIFETIME_VALUE_IN_SECONDS'] = lifetime_value_in_seconds
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_lifetime.command('./	<cr>')
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_lifetime_cr():
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress.group(cls=FRR_AbbreviationGroup, name='prefix',)
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix(prefix_='prefix'):
    """Add/modify prefix related information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix():
    """IPv4 prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix.name
    data_gen['PREFIX_IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix.command('./	<cr>')
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_cr():
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('cost_value', metavar='(0-255)', required=True, type=FRR_TYPE((0, 255)))
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_cost(cost_value, cost_='cost'):
    """Administrative cost [default: 255]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['COST_VALUE'] = cost_value
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_cost.command('./	<cr>')
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_cost_cr():
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_cost.group(cls=FRR_AbbreviationGroup, name='lifetime', invoke_without_command=True)
@click.argument('lifetime_value_in_seconds', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_cost_lifetime(lifetime_value_in_seconds, lifetime_='lifetime'):
    """Registration lifetime [default: infinite]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_cost_lifetime.name
    data_gen['lifetime'] = lifetime_='lifetime'
    data_gen['LIFETIME_VALUE_IN_SECONDS'] = lifetime_value_in_seconds
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_cost_lifetime.command('./	<cr>')
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_cost_lifetime_cr():
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix.group(cls=FRR_AbbreviationGroup, name='lifetime', invoke_without_command=True)
@click.argument('lifetime_value_in_seconds', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_lifetime(lifetime_value_in_seconds, lifetime_='lifetime'):
    """Registration lifetime [default: infinite]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_lifetime.name
    data_gen['lifetime'] = lifetime_='lifetime'
    data_gen['LIFETIME_VALUE_IN_SECONDS'] = lifetime_value_in_seconds
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_lifetime.command('./	<cr>')
def frr_add_vnc_mac_virtualnetworkidentifier_vn_vnipaddress_un_unipaddress_prefix_prefixipprefix_lifetime_cr():
    pass


@frr_add_vnc.group(cls=FRR_AbbreviationGroup, name='prefix',)
def frr_add_vnc_prefix(prefix_='prefix'):
    """Add/modify prefix related information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D/M', 'X:X::X:X/M']),)
def frr_add_vnc_prefix_prefixipprefix():
    """3"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix.name
    data_gen['PREFIX_IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix.group(cls=FRR_AbbreviationGroup, name='vn',)
def frr_add_vnc_prefix_prefixipprefix_vn(vn_='vn'):
    """VN address of NVE"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn.name
    data_gen['vn'] = vn_='vn'
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', 'X:X::X:X']),)
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress.name
    data_gen['VN_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress.group(cls=FRR_AbbreviationGroup, name='un',)
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un(un_='un'):
    """UN address of NVE"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un.name
    data_gen['un'] = un_='un'
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress():
    """UN IPv4 interface address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress.name
    data_gen['UN_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress.command('./	<cr>')
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cr():
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('cost_value', metavar='(0-255)', required=True, type=FRR_TYPE((0, 255)))
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost(cost_value, cost_='cost'):
    """Administrative cost [default: 255]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['COST_VALUE'] = cost_value
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost.command('./	<cr>')
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_cr():
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['LNH_OPTIONS']), invoke_without_command=True)
@click.argument('to_localnexthop', metavar='LNH_OPTIONS', required=True, type=FRR_TYPE('LNH_OPTIONS'))
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_fromlocalnexthop(to_localnexthop):
    """[local-next-hop (A.B.C.D|X:X::X:X)] [local-cost <0-255>]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_fromlocalnexthop.name
    data_gen['FROM_LOCAL-NEXT-HOP'] = FRR_CLI_ARGS[name]
    data_gen['TO_LOCAL-NEXT-HOP'] = to_localnexthop
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_fromlocalnexthop.command('./	<cr>')
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_fromlocalnexthop_cr():
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost.group(cls=FRR_AbbreviationGroup, name='lifetime', invoke_without_command=True)
@click.argument('lifetime_value_in_seconds', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_lifetime(lifetime_value_in_seconds, lifetime_='lifetime'):
    """Registration lifetime [default: infinite]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_lifetime.name
    data_gen['lifetime'] = lifetime_='lifetime'
    data_gen['LIFETIME_VALUE_IN_SECONDS'] = lifetime_value_in_seconds
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_lifetime.command('./	<cr>')
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_lifetime_cr():
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_lifetime.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(12, ['LNH_OPTIONS']), invoke_without_command=True)
@click.argument('to_localnexthop', metavar='LNH_OPTIONS', required=True, type=FRR_TYPE('LNH_OPTIONS'))
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_lifetime_fromlocalnexthop(to_localnexthop):
    """[local-next-hop (A.B.C.D|X:X::X:X)] [local-cost <0-255>]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_lifetime_fromlocalnexthop.name
    data_gen['FROM_LOCAL-NEXT-HOP'] = FRR_CLI_ARGS[name]
    data_gen['TO_LOCAL-NEXT-HOP'] = to_localnexthop
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_lifetime_fromlocalnexthop.command('./	<cr>')
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_cost_lifetime_fromlocalnexthop_cr():
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['LNH_OPTIONS']), invoke_without_command=True)
@click.argument('to_localnexthop', metavar='LNH_OPTIONS', required=True, type=FRR_TYPE('LNH_OPTIONS'))
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_fromlocalnexthop(to_localnexthop):
    """[local-next-hop (A.B.C.D|X:X::X:X)] [local-cost <0-255>]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_fromlocalnexthop.name
    data_gen['FROM_LOCAL-NEXT-HOP'] = FRR_CLI_ARGS[name]
    data_gen['TO_LOCAL-NEXT-HOP'] = to_localnexthop
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_fromlocalnexthop.command('./	<cr>')
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_fromlocalnexthop_cr():
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress.group(cls=FRR_AbbreviationGroup, name='lifetime', invoke_without_command=True)
@click.argument('lifetime_value_in_seconds', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime(lifetime_value_in_seconds, lifetime_='lifetime'):
    """Registration lifetime [default: infinite]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime.name
    data_gen['lifetime'] = lifetime_='lifetime'
    data_gen['LIFETIME_VALUE_IN_SECONDS'] = lifetime_value_in_seconds
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime.command('./	<cr>')
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_cr():
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('cost_value', metavar='(0-255)', required=True, type=FRR_TYPE((0, 255)))
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_cost(cost_value, cost_='cost'):
    """Administrative cost [default: 255]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['COST_VALUE'] = cost_value
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_cost.command('./	<cr>')
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_cost_cr():
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_cost.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(12, ['LNH_OPTIONS']), invoke_without_command=True)
@click.argument('to_localnexthop', metavar='LNH_OPTIONS', required=True, type=FRR_TYPE('LNH_OPTIONS'))
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_cost_fromlocalnexthop(to_localnexthop):
    """[local-next-hop (A.B.C.D|X:X::X:X)] [local-cost <0-255>]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_cost_fromlocalnexthop.name
    data_gen['FROM_LOCAL-NEXT-HOP'] = FRR_CLI_ARGS[name]
    data_gen['TO_LOCAL-NEXT-HOP'] = to_localnexthop
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_cost_fromlocalnexthop.command('./	<cr>')
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_cost_fromlocalnexthop_cr():
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['LNH_OPTIONS']), invoke_without_command=True)
@click.argument('to_localnexthop', metavar='LNH_OPTIONS', required=True, type=FRR_TYPE('LNH_OPTIONS'))
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_fromlocalnexthop(to_localnexthop):
    """[local-next-hop (A.B.C.D|X:X::X:X)] [local-cost <0-255>]"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_fromlocalnexthop.name
    data_gen['FROM_LOCAL-NEXT-HOP'] = FRR_CLI_ARGS[name]
    data_gen['TO_LOCAL-NEXT-HOP'] = to_localnexthop
    
    if 'VIEW_NODE|add_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add_vnc'][key] = val
    
    # set VIEW_NODE -> add_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add_vnc'
    pass


@frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_fromlocalnexthop.command('./	<cr>')
def frr_add_vnc_prefix_prefixipprefix_vn_vnipaddress_un_unipaddress_lifetime_fromlocalnexthop_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrf',)
@click.argument('vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_add_vrf(vrf_name, vrf_='vrf'):
    """To a VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['VRF_NAME'] = vrf_name
    
    if 'VIEW_NODE|add' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add'][key] = val
    
    # set VIEW_NODE -> add table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add'
    pass


@frr_add_vrf.group(cls=FRR_AbbreviationGroup, name='prefix',)
def frr_add_vrf_prefix(prefix_='prefix'):
    """Add/modify prefix related information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vrf_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    
    if 'VIEW_NODE|add' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add'][key] = val
    
    # set VIEW_NODE -> add table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add'
    pass


@frr_add_vrf_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_add_vrf_prefix_prefixipprefix():
    """IPv4 prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vrf_prefix_prefixipprefix.name
    data_gen['PREFIX_IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|add' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add'][key] = val
    
    # set VIEW_NODE -> add table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add'
    pass


@frr_add_vrf_prefix_prefixipprefix.command('./	<cr>')
def frr_add_vrf_prefix_prefixipprefix_cr():
    pass


@frr_add_vrf_prefix_prefixipprefix.group(cls=FRR_AbbreviationGroup, name='label', invoke_without_command=True)
@click.argument('label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_add_vrf_prefix_prefixipprefix_label(label_value, label_='label'):
    """Override configured VRF label"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vrf_prefix_prefixipprefix_label.name
    data_gen['label'] = label_='label'
    data_gen['LABEL_VALUE'] = label_value
    
    if 'VIEW_NODE|add' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add'][key] = val
    
    # set VIEW_NODE -> add table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add'
    pass


@frr_add_vrf_prefix_prefixipprefix_label.command('./	<cr>')
def frr_add_vrf_prefix_prefixipprefix_label_cr():
    pass


@frr_add_vrf_prefix_prefixipprefix.group(cls=FRR_AbbreviationGroup, name='preference', invoke_without_command=True)
@click.argument('local_preference', metavar='(0-4294967295)', required=True, type=FRR_TYPE((0, 4294967295)))
def frr_add_vrf_prefix_prefixipprefix_preference(local_preference, preference_='preference'):
    """Set advertised local preference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vrf_prefix_prefixipprefix_preference.name
    data_gen['preference'] = preference_='preference'
    data_gen['LOCAL_PREFERENCE'] = local_preference
    
    if 'VIEW_NODE|add' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add'][key] = val
    
    # set VIEW_NODE -> add table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add'
    pass


@frr_add_vrf_prefix_prefixipprefix_preference.command('./	<cr>')
def frr_add_vrf_prefix_prefixipprefix_preference_cr():
    pass


@frr_add_vrf_prefix_prefixipprefix.group(cls=FRR_AbbreviationGroup, name='rd', invoke_without_command=True)
@click.argument('bgp_identifier', metavar='ASN:NN_OR_IP-ADDRESS', required=True, type=FRR_TYPE('ASN:NN_OR_IP-ADDRESS'))
def frr_add_vrf_prefix_prefixipprefix_rd(bgp_identifier, rd_='rd'):
    """Override configured VRF Route Distinguisher"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add_vrf_prefix_prefixipprefix_rd.name
    data_gen['rd'] = rd_='rd'
    data_gen['BGP_IDENTIFIER'] = bgp_identifier
    
    if 'VIEW_NODE|add' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add'][key] = val
    
    # set VIEW_NODE -> add table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add'
    pass


@frr_add_vrf_prefix_prefixipprefix_rd.command('./	<cr>')
def frr_add_vrf_prefix_prefixipprefix_rd_cr():
    pass

