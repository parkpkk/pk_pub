import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='distributed', invoke_without_command=True)
def frr_show_bfd_distributed(distributed_='distributed'):
    """Show BFD data plane (distributed BFD) statistics"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_distributed.name
    data_gen['distributed'] = distributed_='distributed'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_distributed.command('./	<cr>')
def frr_show_bfd_distributed_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='peer', invoke_without_command=True)
def frr_show_bfd_peer(show_bfd_peer_='show_bfd_peer'):
    """BFD peers status"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer.name
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer.command('./	<cr>')
def frr_show_bfd_peer_cr():
    pass


@frr_show_bfd_peer.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_peer_counters(show_bfd_peer_counters_='show_bfd_peer_counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_counters.name
    
    if 'VIEW_NODE|show_bfd_peer_counters' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer_counters'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer_counters']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer_counters'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer_counters table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer_counters'
    pass


@frr_show_bfd_peer_counters.command('./	<cr>')
def frr_show_bfd_peer_counters_cr():
    pass


@frr_show_bfd_peer_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_counters_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_counters_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd_peer_counters' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer_counters'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer_counters']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer_counters'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer_counters table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer_counters'
    pass


@frr_show_bfd_peer_counters_json.command('./	<cr>')
def frr_show_bfd_peer_counters_json_cr():
    pass


@frr_show_bfd_peer.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_bfd_peer_ipaddress():
    """IPv4 peer address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress.name
    data_gen['IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_cr():
    pass


@frr_show_bfd_peer_ipaddress.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_counters(counters_='counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_counters.name
    data_gen['counters'] = counters_='counters'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_counters.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_counters_cr():
    pass


@frr_show_bfd_peer_ipaddress_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_counters_json(counters_json_='counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_counters_json.name
    data_gen['counters_json'] = counters_json_='counters_json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_counters_json.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_counters_json_cr():
    pass


@frr_show_bfd_peer_ipaddress.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
@click.argument('configure_local_interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_show_bfd_peer_ipaddress_interface(configure_local_interface_name, interface_='interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_interface.name
    data_gen['interface'] = interface_='interface'
    data_gen['CONFIGURE_LOCAL_INTERFACE_NAME'] = configure_local_interface_name
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_interface.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_interface_cr():
    pass


@frr_show_bfd_peer_ipaddress_interface.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_interface_counters(counters_='counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_interface_counters.name
    data_gen['counters'] = counters_='counters'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_interface_counters.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_interface_counters_cr():
    pass


@frr_show_bfd_peer_ipaddress_interface_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_interface_counters_json(counters_json_='counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_interface_counters_json.name
    data_gen['counters_json'] = counters_json_='counters_json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_interface_counters_json.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_interface_counters_json_cr():
    pass


@frr_show_bfd_peer_ipaddress_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_interface_json.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_interface_json_cr():
    pass


@frr_show_bfd_peer_ipaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_json.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_json_cr():
    pass


@frr_show_bfd_peer_ipaddress.group(cls=FRR_AbbreviationGroup, name='local-address',)
def frr_show_bfd_peer_ipaddress_localaddress(localaddress_='local-address'):
    """Configure local address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_localaddress.name
    data_gen['local-address'] = localaddress_='local-address'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_localaddress.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress():
    """IPv4 local address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress.name
    data_gen['LOCAL-ADDRESS_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_cr():
    pass


@frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_counters(counters_='counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_counters.name
    data_gen['counters'] = counters_='counters'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_counters.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_counters_cr():
    pass


@frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_counters_json(counters_json_='counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_counters_json.name
    data_gen['counters_json'] = counters_json_='counters_json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_counters_json.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_counters_json_cr():
    pass


@frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_json.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_localaddress_localaddressipaddress_json_cr():
    pass


@frr_show_bfd_peer_ipaddress.group(cls=FRR_AbbreviationGroup, name='multihop', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_multihop(multihop_='multihop'):
    """Configure multihop"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_multihop.name
    data_gen['multihop'] = multihop_='multihop'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_multihop.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_multihop_cr():
    pass


@frr_show_bfd_peer_ipaddress_multihop.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_multihop_counters(multihop_counters_='multihop_counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_multihop_counters.name
    data_gen['multihop_counters'] = multihop_counters_='multihop_counters'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_multihop_counters.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_multihop_counters_cr():
    pass


@frr_show_bfd_peer_ipaddress_multihop_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_multihop_counters_json(multihop_counters_json_='multihop_counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_multihop_counters_json.name
    data_gen['multihop_counters_json'] = multihop_counters_json_='multihop_counters_json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_multihop_counters_json.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_multihop_counters_json_cr():
    pass


@frr_show_bfd_peer_ipaddress_multihop.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_ipaddress_multihop_json(multihop_json_='multihop_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_ipaddress_multihop_json.name
    data_gen['multihop_json'] = multihop_json_='multihop_json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_ipaddress_multihop_json.command('./	<cr>')
def frr_show_bfd_peer_ipaddress_multihop_json_cr():
    pass


@frr_show_bfd_peer.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_json.command('./	<cr>')
def frr_show_bfd_peer_json_cr():
    pass


@frr_show_bfd_peer.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['WORD']), invoke_without_command=True)
def frr_show_bfd_peer_peerlabel():
    """Peer label"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_peerlabel.name
    data_gen['PEER_LABEL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_peerlabel.command('./	<cr>')
def frr_show_bfd_peer_peerlabel_cr():
    pass


@frr_show_bfd_peer_peerlabel.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_peer_peerlabel_counters(counters_='counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_peerlabel_counters.name
    data_gen['counters'] = counters_='counters'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_peerlabel_counters.command('./	<cr>')
def frr_show_bfd_peer_peerlabel_counters_cr():
    pass


@frr_show_bfd_peer_peerlabel_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_peerlabel_counters_json(counters_json_='counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_peerlabel_counters_json.name
    data_gen['counters_json'] = counters_json_='counters_json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_peerlabel_counters_json.command('./	<cr>')
def frr_show_bfd_peer_peerlabel_counters_json_cr():
    pass


@frr_show_bfd_peer_peerlabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peer_peerlabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peer_peerlabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd_peer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peer'][key] = val
    
    # set VIEW_NODE -> show_bfd_peer table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peer'
    pass


@frr_show_bfd_peer_peerlabel_json.command('./	<cr>')
def frr_show_bfd_peer_peerlabel_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='peers', invoke_without_command=True)
def frr_show_bfd_peers(show_bfd_peers_='show_bfd_peers'):
    """BFD peers status"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peers.name
    
    if 'VIEW_NODE|show_bfd_peers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers'][key] = val
    
    # set VIEW_NODE -> show_bfd_peers table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peers'
    pass


@frr_show_bfd_peers.command('./	<cr>')
def frr_show_bfd_peers_cr():
    pass


@frr_show_bfd_peers.group(cls=FRR_AbbreviationGroup, name='brief', invoke_without_command=True)
def frr_show_bfd_peers_brief(show_bfd_peers_brief_='show_bfd_peers_brief'):
    """Show BFD peer information in tabular form"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peers_brief.name
    
    if 'VIEW_NODE|show_bfd_peers_brief' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_brief'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_brief']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_brief'][key] = val
    
    # set VIEW_NODE -> show_bfd_peers_brief table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peers_brief'
    pass


@frr_show_bfd_peers_brief.command('./	<cr>')
def frr_show_bfd_peers_brief_cr():
    pass


@frr_show_bfd_peers_brief.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peers_brief_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peers_brief_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd_peers_brief' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_brief'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_brief']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_brief'][key] = val
    
    # set VIEW_NODE -> show_bfd_peers_brief table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peers_brief'
    pass


@frr_show_bfd_peers_brief_json.command('./	<cr>')
def frr_show_bfd_peers_brief_json_cr():
    pass


@frr_show_bfd_peers.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_peers_counters(show_bfd_peers_counters_='show_bfd_peers_counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peers_counters.name
    
    if 'VIEW_NODE|show_bfd_peers_counters' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_counters'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_counters']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_counters'][key] = val
    
    # set VIEW_NODE -> show_bfd_peers_counters table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peers_counters'
    pass


@frr_show_bfd_peers_counters.command('./	<cr>')
def frr_show_bfd_peers_counters_cr():
    pass


@frr_show_bfd_peers_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peers_counters_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peers_counters_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd_peers_counters' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_counters'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_counters']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers_counters'][key] = val
    
    # set VIEW_NODE -> show_bfd_peers_counters table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peers_counters'
    pass


@frr_show_bfd_peers_counters_json.command('./	<cr>')
def frr_show_bfd_peers_counters_json_cr():
    pass


@frr_show_bfd_peers.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_peers_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_peers_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd_peers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_peers'][key] = val
    
    # set VIEW_NODE -> show_bfd_peers table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_peers'
    pass


@frr_show_bfd_peers_json.command('./	<cr>')
def frr_show_bfd_peers_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='static', invoke_without_command=True)
def frr_show_bfd_static():
    """Static route daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_static.name
    
    if 'VIEW_NODE|show_bfd_static' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_static'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_static']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_static'][key] = val
    
    # set VIEW_NODE -> show_bfd_static table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_static'
    pass


@frr_show_bfd_static.command('./	<cr>')
def frr_show_bfd_static_cr():
    pass


@frr_show_bfd_static.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
def frr_show_bfd_static_route(show_bfd_static_route_='show_bfd_static_route'):
    """Routing Table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_static_route.name
    
    if 'VIEW_NODE|show_bfd_static_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_static_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_static_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_static_route'][key] = val
    
    # set VIEW_NODE -> show_bfd_static_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_static_route'
    pass


@frr_show_bfd_static_route.command('./	<cr>')
def frr_show_bfd_static_route_cr():
    pass


@frr_show_bfd_static_route.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_static_route_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_static_route_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd_static_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_static_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd_static_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd_static_route'][key] = val
    
    # set VIEW_NODE -> show_bfd_static_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd_static_route'
    pass


@frr_show_bfd_static_route_json.command('./	<cr>')
def frr_show_bfd_static_route_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrf',)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_bfd_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf.group(cls=FRR_AbbreviationGroup, name='peer', invoke_without_command=True)
def frr_show_bfd_vrf_peer(peer_='peer'):
    """BFD peers status"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer.name
    data_gen['peer'] = peer_='peer'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer.command('./	<cr>')
def frr_show_bfd_vrf_peer_cr():
    pass


@frr_show_bfd_vrf_peer.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_vrf_peer_counters(peer_counters_='peer_counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_counters.name
    data_gen['peer_counters'] = peer_counters_='peer_counters'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_counters.command('./	<cr>')
def frr_show_bfd_vrf_peer_counters_cr():
    pass


@frr_show_bfd_vrf_peer_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_counters_json(peer_counters_json_='peer_counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_counters_json.name
    data_gen['peer_counters_json'] = peer_counters_json_='peer_counters_json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_counters_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_counters_json_cr():
    pass


@frr_show_bfd_vrf_peer.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress():
    """IPv4 peer address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress.name
    data_gen['IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_counters(counters_='counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_counters.name
    data_gen['counters'] = counters_='counters'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_counters.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_counters_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_counters_json(counters_json_='counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_counters_json.name
    data_gen['counters_json'] = counters_json_='counters_json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_counters_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_counters_json_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
@click.argument('configure_local_interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_show_bfd_vrf_peer_ipaddress_interface(configure_local_interface_name, interface_='interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_interface.name
    data_gen['interface'] = interface_='interface'
    data_gen['CONFIGURE_LOCAL_INTERFACE_NAME'] = configure_local_interface_name
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_interface.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_interface_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress_interface.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_interface_counters(counters_='counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_interface_counters.name
    data_gen['counters'] = counters_='counters'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_interface_counters.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_interface_counters_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress_interface_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_interface_counters_json(counters_json_='counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_interface_counters_json.name
    data_gen['counters_json'] = counters_json_='counters_json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_interface_counters_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_interface_counters_json_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_interface_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_interface_json_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_json_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress.group(cls=FRR_AbbreviationGroup, name='local-address',)
def frr_show_bfd_vrf_peer_ipaddress_localaddress(localaddress_='local-address'):
    """Configure local address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_localaddress.name
    data_gen['local-address'] = localaddress_='local-address'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_localaddress.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress():
    """IPv4 local address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress.name
    data_gen['LOCAL-ADDRESS_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_counters(counters_='counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_counters.name
    data_gen['counters'] = counters_='counters'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_counters.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_counters_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_counters_json(counters_json_='counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_counters_json.name
    data_gen['counters_json'] = counters_json_='counters_json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_counters_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_counters_json_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_localaddress_localaddressipaddress_json_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress.group(cls=FRR_AbbreviationGroup, name='multihop', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_multihop(multihop_='multihop'):
    """Configure multihop"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_multihop.name
    data_gen['multihop'] = multihop_='multihop'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_multihop.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_multihop_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress_multihop.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_multihop_counters(multihop_counters_='multihop_counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_multihop_counters.name
    data_gen['multihop_counters'] = multihop_counters_='multihop_counters'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_multihop_counters.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_multihop_counters_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress_multihop_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_multihop_counters_json(multihop_counters_json_='multihop_counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_multihop_counters_json.name
    data_gen['multihop_counters_json'] = multihop_counters_json_='multihop_counters_json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_multihop_counters_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_multihop_counters_json_cr():
    pass


@frr_show_bfd_vrf_peer_ipaddress_multihop.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_ipaddress_multihop_json(multihop_json_='multihop_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_ipaddress_multihop_json.name
    data_gen['multihop_json'] = multihop_json_='multihop_json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_ipaddress_multihop_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_ipaddress_multihop_json_cr():
    pass


@frr_show_bfd_vrf_peer.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_json_cr():
    pass


@frr_show_bfd_vrf_peer.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD']), invoke_without_command=True)
def frr_show_bfd_vrf_peer_peerlabel():
    """Peer label"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_peerlabel.name
    data_gen['PEER_LABEL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_peerlabel.command('./	<cr>')
def frr_show_bfd_vrf_peer_peerlabel_cr():
    pass


@frr_show_bfd_vrf_peer_peerlabel.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_vrf_peer_peerlabel_counters(counters_='counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_peerlabel_counters.name
    data_gen['counters'] = counters_='counters'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_peerlabel_counters.command('./	<cr>')
def frr_show_bfd_vrf_peer_peerlabel_counters_cr():
    pass


@frr_show_bfd_vrf_peer_peerlabel_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_peerlabel_counters_json(counters_json_='counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_peerlabel_counters_json.name
    data_gen['counters_json'] = counters_json_='counters_json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_peerlabel_counters_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_peerlabel_counters_json_cr():
    pass


@frr_show_bfd_vrf_peer_peerlabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peer_peerlabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peer_peerlabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peer_peerlabel_json.command('./	<cr>')
def frr_show_bfd_vrf_peer_peerlabel_json_cr():
    pass


@frr_show_bfd_vrf.group(cls=FRR_AbbreviationGroup, name='peers', invoke_without_command=True)
def frr_show_bfd_vrf_peers(peers_='peers'):
    """BFD peers status"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peers.name
    data_gen['peers'] = peers_='peers'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peers.command('./	<cr>')
def frr_show_bfd_vrf_peers_cr():
    pass


@frr_show_bfd_vrf_peers.group(cls=FRR_AbbreviationGroup, name='brief', invoke_without_command=True)
def frr_show_bfd_vrf_peers_brief(peers_brief_='peers_brief'):
    """Show BFD peer information in tabular form"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peers_brief.name
    data_gen['peers_brief'] = peers_brief_='peers_brief'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peers_brief.command('./	<cr>')
def frr_show_bfd_vrf_peers_brief_cr():
    pass


@frr_show_bfd_vrf_peers_brief.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peers_brief_json(peers_brief_json_='peers_brief_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peers_brief_json.name
    data_gen['peers_brief_json'] = peers_brief_json_='peers_brief_json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peers_brief_json.command('./	<cr>')
def frr_show_bfd_vrf_peers_brief_json_cr():
    pass


@frr_show_bfd_vrf_peers.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_bfd_vrf_peers_counters(peers_counters_='peers_counters'):
    """Show BFD peer counters information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peers_counters.name
    data_gen['peers_counters'] = peers_counters_='peers_counters'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peers_counters.command('./	<cr>')
def frr_show_bfd_vrf_peers_counters_cr():
    pass


@frr_show_bfd_vrf_peers_counters.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peers_counters_json(peers_counters_json_='peers_counters_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peers_counters_json.name
    data_gen['peers_counters_json'] = peers_counters_json_='peers_counters_json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peers_counters_json.command('./	<cr>')
def frr_show_bfd_vrf_peers_counters_json_cr():
    pass


@frr_show_bfd_vrf_peers.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_bfd_vrf_peers_json(peers_json_='peers_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd_vrf_peers_json.name
    data_gen['peers_json'] = peers_json_='peers_json'
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@frr_show_bfd_vrf_peers_json.command('./	<cr>')
def frr_show_bfd_vrf_peers_json_cr():
    pass

