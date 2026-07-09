import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='debug',)
def frr_no_debug(no_debug_='no_debug'):
    """Debugging functions"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug.name
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='all',)
def frr_no_debug_all():
    """Disable all VNC debugging"""
    global COMMON_DATA_MAP
    
    pass


@frr_no_debug_all.group(cls=FRR_AbbreviationGroup, name='bgp',)
def frr_no_debug_all_bgp(no_debug_all_bgp_='no_debug_all_bgp'):
    """BGP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_all_bgp.name
    
    if 'VIEW_NODE|no_debug_all_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_all_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_all_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_all_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_all_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_all_bgp'
    pass


@frr_no_debug_all_bgp.group(cls=FRR_AbbreviationGroup, name='vnc', invoke_without_command=True)
def frr_no_debug_all_bgp_vnc(vnc_='vnc'):
    """VNC information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_all_bgp_vnc.name
    data_gen['vnc'] = vnc_='vnc'
    
    if 'VIEW_NODE|no_debug_all_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_all_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_all_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_all_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_all_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_all_bgp'
    pass


@frr_no_debug_all_bgp_vnc.command('./	<cr>')
def frr_no_debug_all_bgp_vnc_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='babel',)
def frr_no_debug_babel(babel_='babel'):
    """Babel information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_babel.name
    data_gen['babel'] = babel_='babel'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_babel.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['common', 'kernel', 'filter', 'timeout', 'interface', 'route', 'all']), invoke_without_command=True)
def frr_no_debug_babel_babelloggingmessagetype():
    """Common messages (default)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_babel_babelloggingmessagetype.name
    data_gen['BABEL_LOGGING_MESSAGE_TYPE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_babel_babelloggingmessagetype.command('./	<cr>')
def frr_no_debug_babel_babelloggingmessagetype_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='bfd',)
def frr_no_debug_bfd(no_debug_bfd_='no_debug_bfd'):
    """Bidirection Forwarding Detection"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bfd.name
    
    if 'VIEW_NODE|no_debug_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd'][key] = val
    
    # set VIEW_NODE -> no_debug_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bfd'
    pass


@frr_no_debug_bfd.group(cls=FRR_AbbreviationGroup, name='distributed', invoke_without_command=True)
def frr_no_debug_bfd_distributed(distributed_='distributed'):
    """BFD data plane (distributed BFD) debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bfd_distributed.name
    data_gen['distributed'] = distributed_='distributed'
    
    if 'VIEW_NODE|no_debug_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd'][key] = val
    
    # set VIEW_NODE -> no_debug_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bfd'
    pass


@frr_no_debug_bfd_distributed.command('./	<cr>')
def frr_no_debug_bfd_distributed_cr():
    pass


@frr_no_debug_bfd.group(cls=FRR_AbbreviationGroup, name='network', invoke_without_command=True)
def frr_no_debug_bfd_network(network_='network'):
    """Network layer debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bfd_network.name
    data_gen['network'] = network_='network'
    
    if 'VIEW_NODE|no_debug_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd'][key] = val
    
    # set VIEW_NODE -> no_debug_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bfd'
    pass


@frr_no_debug_bfd_network.command('./	<cr>')
def frr_no_debug_bfd_network_cr():
    pass


@frr_no_debug_bfd.group(cls=FRR_AbbreviationGroup, name='peer', invoke_without_command=True)
def frr_no_debug_bfd_peer(peer_='peer'):
    """Peer events debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bfd_peer.name
    data_gen['peer'] = peer_='peer'
    
    if 'VIEW_NODE|no_debug_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd'][key] = val
    
    # set VIEW_NODE -> no_debug_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bfd'
    pass


@frr_no_debug_bfd_peer.command('./	<cr>')
def frr_no_debug_bfd_peer_cr():
    pass


@frr_no_debug_bfd.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_bfd_zebra(zebra_='zebra'):
    """Zebra events debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bfd_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'VIEW_NODE|no_debug_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bfd'][key] = val
    
    # set VIEW_NODE -> no_debug_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bfd'
    pass


@frr_no_debug_bfd_zebra.command('./	<cr>')
def frr_no_debug_bfd_zebra_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='bgp', invoke_without_command=True)
def frr_no_debug_bgp(no_debug_bgp_='no_debug_bgp'):
    """BGP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp.name
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp.command('./	<cr>')
def frr_no_debug_bgp_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='as4', invoke_without_command=True)
def frr_no_debug_bgp_as4(no_debug_bgp_as4_='no_debug_bgp_as4'):
    """BGP AS4 actions"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_as4.name
    
    if 'VIEW_NODE|no_debug_bgp_as4' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_as4'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_as4']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_as4'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_as4 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_as4'
    pass


@frr_no_debug_bgp_as4.command('./	<cr>')
def frr_no_debug_bgp_as4_cr():
    pass


@frr_no_debug_bgp_as4.group(cls=FRR_AbbreviationGroup, name='segment', invoke_without_command=True)
def frr_no_debug_bgp_as4_segment(segment_='segment'):
    """BGP AS4 aspath segment handling"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_as4_segment.name
    data_gen['segment'] = segment_='segment'
    
    if 'VIEW_NODE|no_debug_bgp_as4' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_as4'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_as4']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_as4'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_as4 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_as4'
    pass


@frr_no_debug_bgp_as4_segment.command('./	<cr>')
def frr_no_debug_bgp_as4_segment_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='bestpath', invoke_without_command=True)
def frr_no_debug_bgp_bestpath(no_debug_bgp_bestpath_='no_debug_bgp_bestpath'):
    """BGP bestpath"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_bestpath.name
    
    if 'VIEW_NODE|no_debug_bgp_bestpath' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_bestpath'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_bestpath']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_bestpath'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_bestpath table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_bestpath'
    pass


@frr_no_debug_bgp_bestpath.command('./	<cr>')
def frr_no_debug_bgp_bestpath_cr():
    pass


@frr_no_debug_bgp_bestpath.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_no_debug_bgp_bestpath_ipprefix():
    """IPv4 prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_bestpath_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_bestpath' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_bestpath'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_bestpath']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_bestpath'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_bestpath table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_bestpath'
    pass


@frr_no_debug_bgp_bestpath_ipprefix.command('./	<cr>')
def frr_no_debug_bgp_bestpath_ipprefix_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='bfd', invoke_without_command=True)
def frr_no_debug_bgp_bfd(bfd_='bfd'):
    """Bidirection Forwarding Detection"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_bfd.name
    data_gen['bfd'] = bfd_='bfd'
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_bfd.command('./	<cr>')
def frr_no_debug_bgp_bfd_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='conditional-advertisement', invoke_without_command=True)
def frr_no_debug_bgp_conditionaladvertisement(conditionaladvertisement_='conditional-advertisement'):
    """BGP conditional advertisement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_conditionaladvertisement.name
    data_gen['conditional-advertisement'] = conditionaladvertisement_='conditional-advertisement'
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_conditionaladvertisement.command('./	<cr>')
def frr_no_debug_bgp_conditionaladvertisement_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='evpn',)
def frr_no_debug_bgp_evpn(no_debug_bgp_evpn_='no_debug_bgp_evpn'):
    """EVPN"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_evpn.name
    
    if 'VIEW_NODE|no_debug_bgp_evpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_evpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_evpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_evpn'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_evpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_evpn'
    pass


@frr_no_debug_bgp_evpn.group(cls=FRR_AbbreviationGroup, name='mh',)
def frr_no_debug_bgp_evpn_mh(mh_='mh'):
    """Multihoming"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_evpn_mh.name
    data_gen['mh'] = mh_='mh'
    
    if 'VIEW_NODE|no_debug_bgp_evpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_evpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_evpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_evpn'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_evpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_evpn'
    pass


@frr_no_debug_bgp_evpn_mh.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['es', 'route']), invoke_without_command=True)
def frr_no_debug_bgp_evpn_mh_mhchoicecase():
    """Ethernet Segment debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_evpn_mh_mhchoicecase.name
    data_gen['MH_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_evpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_evpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_evpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_evpn'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_evpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_evpn'
    pass


@frr_no_debug_bgp_evpn_mh_mhchoicecase.command('./	<cr>')
def frr_no_debug_bgp_evpn_mh_mhchoicecase_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='flowspec', invoke_without_command=True)
def frr_no_debug_bgp_flowspec(flowspec_='flowspec'):
    """BGP allow flowspec debugging entries"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_flowspec.name
    data_gen['flowspec'] = flowspec_='flowspec'
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_flowspec.command('./	<cr>')
def frr_no_debug_bgp_flowspec_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='graceful-restart', invoke_without_command=True)
def frr_no_debug_bgp_gracefulrestart(gracefulrestart_='graceful-restart'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_gracefulrestart.name
    data_gen['graceful-restart'] = gracefulrestart_='graceful-restart'
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_gracefulrestart.command('./	<cr>')
def frr_no_debug_bgp_gracefulrestart_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='keepalives', invoke_without_command=True)
def frr_no_debug_bgp_keepalives(no_debug_bgp_keepalives_='no_debug_bgp_keepalives'):
    """BGP keepalives"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_keepalives.name
    
    if 'VIEW_NODE|no_debug_bgp_keepalives' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_keepalives'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_keepalives']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_keepalives'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_keepalives table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_keepalives'
    pass


@frr_no_debug_bgp_keepalives.command('./	<cr>')
def frr_no_debug_bgp_keepalives_cr():
    pass


@frr_no_debug_bgp_keepalives.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D', 'X:X::X:X', 'WORD']), invoke_without_command=True)
def frr_no_debug_bgp_keepalives_ipaddress():
    """BGP neighbor IP address to debug"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_keepalives_ipaddress.name
    data_gen['IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_keepalives' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_keepalives'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_keepalives']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_keepalives'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_keepalives table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_keepalives'
    pass


@frr_no_debug_bgp_keepalives_ipaddress.command('./	<cr>')
def frr_no_debug_bgp_keepalives_ipaddress_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='labelpool', invoke_without_command=True)
def frr_no_debug_bgp_labelpool(labelpool_='labelpool'):
    """label pool"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_labelpool.name
    data_gen['labelpool'] = labelpool_='labelpool'
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_labelpool.command('./	<cr>')
def frr_no_debug_bgp_labelpool_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='neighbor-events', invoke_without_command=True)
def frr_no_debug_bgp_neighborevents(no_debug_bgp_neighborevents_='no_debug_bgp_neighbor-events'):
    """Neighbor Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_neighborevents.name
    
    if 'VIEW_NODE|no_debug_bgp_neighbor-events' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_neighbor-events'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_neighbor-events']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_neighbor-events'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_neighbor-events table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_neighbor-events'
    pass


@frr_no_debug_bgp_neighborevents.command('./	<cr>')
def frr_no_debug_bgp_neighborevents_cr():
    pass


@frr_no_debug_bgp_neighborevents.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D', 'X:X::X:X', 'WORD']), invoke_without_command=True)
def frr_no_debug_bgp_neighborevents_ipaddress():
    """BGP neighbor IP address to debug"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_neighborevents_ipaddress.name
    data_gen['IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_neighbor-events' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_neighbor-events'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_neighbor-events']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_neighbor-events'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_neighbor-events table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_neighbor-events'
    pass


@frr_no_debug_bgp_neighborevents_ipaddress.command('./	<cr>')
def frr_no_debug_bgp_neighborevents_ipaddress_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='nht', invoke_without_command=True)
def frr_no_debug_bgp_nht(nht_='nht'):
    """BGP nexthop tracking events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_nht.name
    data_gen['nht'] = nht_='nht'
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_nht.command('./	<cr>')
def frr_no_debug_bgp_nht_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='pbr', invoke_without_command=True)
def frr_no_debug_bgp_pbr(no_debug_bgp_pbr_='no_debug_bgp_pbr'):
    """BGP policy based routing"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_pbr.name
    
    if 'VIEW_NODE|no_debug_bgp_pbr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_pbr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_pbr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_pbr'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_pbr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_pbr'
    pass


@frr_no_debug_bgp_pbr.command('./	<cr>')
def frr_no_debug_bgp_pbr_cr():
    pass


@frr_no_debug_bgp_pbr.group(cls=FRR_AbbreviationGroup, name='error', invoke_without_command=True)
def frr_no_debug_bgp_pbr_error(error_='error'):
    """BGP PBR Error"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_pbr_error.name
    data_gen['error'] = error_='error'
    
    if 'VIEW_NODE|no_debug_bgp_pbr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_pbr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_pbr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_pbr'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_pbr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_pbr'
    pass


@frr_no_debug_bgp_pbr_error.command('./	<cr>')
def frr_no_debug_bgp_pbr_error_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='update-groups', invoke_without_command=True)
def frr_no_debug_bgp_updategroups(updategroups_='update-groups'):
    """BGP update-groups"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updategroups.name
    data_gen['update-groups'] = updategroups_='update-groups'
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_updategroups.command('./	<cr>')
def frr_no_debug_bgp_updategroups_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='updates', invoke_without_command=True)
def frr_no_debug_bgp_updates(no_debug_bgp_updates_='no_debug_bgp_updates'):
    """BGP updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates.name
    
    if 'VIEW_NODE|no_debug_bgp_updates' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates'
    pass


@frr_no_debug_bgp_updates.command('./	<cr>')
def frr_no_debug_bgp_updates_cr():
    pass


@frr_no_debug_bgp_updates.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['in', 'out']), invoke_without_command=True)
def frr_no_debug_bgp_updates_inoutbound():
    """Inbound updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_inoutbound.name
    data_gen['IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_updates' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates'
    pass


@frr_no_debug_bgp_updates_inoutbound.command('./	<cr>')
def frr_no_debug_bgp_updates_inoutbound_cr():
    pass


@frr_no_debug_bgp_updates_inoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D', 'X:X::X:X', 'WORD']), invoke_without_command=True)
def frr_no_debug_bgp_updates_inoutbound_ipaddress():
    """BGP neighbor IP address to debug"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_inoutbound_ipaddress.name
    data_gen['IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_updates' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates'
    pass


@frr_no_debug_bgp_updates_inoutbound_ipaddress.command('./	<cr>')
def frr_no_debug_bgp_updates_inoutbound_ipaddress_cr():
    pass


@frr_no_debug_bgp_updates.group(cls=FRR_AbbreviationGroup, name='prefix',)
def frr_no_debug_bgp_updates_prefix(no_debug_bgp_updates_prefix_='no_debug_bgp_updates_prefix'):
    """Specify a prefix to debug"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix.name
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix'
    pass


@frr_no_debug_bgp_updates_prefix.group(cls=FRR_AbbreviationGroup, name='l2vpn', invoke_without_command=True)
def frr_no_debug_bgp_updates_prefix_l2vpn():
    """Layer 2 Virtual Private Network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_l2vpn.name
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix_l2vpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix_l2vpn'
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn.command('./	<cr>')
def frr_no_debug_bgp_updates_prefix_l2vpn_cr():
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn.group(cls=FRR_AbbreviationGroup, name='evpn', invoke_without_command=True)
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn():
    """Ethernet Virtual Private Network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_l2vpn_evpn.name
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix_l2vpn_evpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix_l2vpn_evpn'
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn.command('./	<cr>')
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_cr():
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn.group(cls=FRR_AbbreviationGroup, name='type', invoke_without_command=True)
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type(no_debug_bgp_updates_prefix_l2vpn_evpn_type_='no_debug_bgp_updates_prefix_l2vpn_evpn_type'):
    """Specify Route type"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type.name
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix_l2vpn_evpn_type table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix_l2vpn_evpn_type'
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type.command('./	<cr>')
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_cr():
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['macip', '2']),)
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase():
    """8"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix_l2vpn_evpn_type table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix_l2vpn_evpn_type'
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase.group(cls=FRR_AbbreviationGroup, name='ip',)
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip(ip_='ip'):
    """IP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip.name
    data_gen['ip'] = ip_='ip'
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix_l2vpn_evpn_type table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix_l2vpn_evpn_type'
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip_ipipaddress():
    """IPv4 address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip_ipipaddress.name
    data_gen['IP_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix_l2vpn_evpn_type table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix_l2vpn_evpn_type'
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip_ipipaddress.command('./	<cr>')
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip_ipipaddress_cr():
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip_ipipprefix():
    """IPv4 prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip_ipipprefix.name
    data_gen['IP_IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix_l2vpn_evpn_type table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix_l2vpn_evpn_type'
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip_ipipprefix.command('./	<cr>')
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_ip_ipipprefix_cr():
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase.group(cls=FRR_AbbreviationGroup, name='mac', invoke_without_command=True)
@click.argument('mac_address', metavar='X:X:X:X:X:X', required=True, type=FRR_TYPE('X:X:X:X:X:X'))
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac(mac_address, mac_='mac'):
    """MAC address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac.name
    data_gen['mac'] = mac_='mac'
    data_gen['MAC_ADDRESS'] = mac_address
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix_l2vpn_evpn_type table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix_l2vpn_evpn_type'
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac.command('./	<cr>')
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac_cr():
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac.group(cls=FRR_AbbreviationGroup, name='ip',)
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac_ip(ip_='ip'):
    """IP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac_ip.name
    data_gen['ip'] = ip_='ip'
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix_l2vpn_evpn_type table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix_l2vpn_evpn_type'
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac_ip.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(12, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac_ip_ipipaddress():
    """IPv4 address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac_ip_ipipaddress.name
    data_gen['IP_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix_l2vpn_evpn_type'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix_l2vpn_evpn_type table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix_l2vpn_evpn_type'
    pass


@frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac_ip_ipipaddress.command('./	<cr>')
def frr_no_debug_bgp_updates_prefix_l2vpn_evpn_type_choicecase_mac_ip_ipipaddress_cr():
    pass


@frr_no_debug_bgp_updates_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_no_debug_bgp_updates_prefix_prefixipprefix():
    """IPv4 prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_updates_prefix_prefixipprefix.name
    data_gen['PREFIX_IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_updates_prefix' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_updates_prefix'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_updates_prefix table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_updates_prefix'
    pass


@frr_no_debug_bgp_updates_prefix_prefixipprefix.command('./	<cr>')
def frr_no_debug_bgp_updates_prefix_prefixipprefix_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='vnc',)
def frr_no_debug_bgp_vnc(vnc_='vnc'):
    """VNC information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_vnc.name
    data_gen['vnc'] = vnc_='vnc'
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_vnc.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['rfapi-query', 'import-bi-attach', 'import-del-remote', 'verbose']), invoke_without_command=True)
def frr_no_debug_bgp_vnc_vncrfapidebugoptions():
    """rfapi query handling"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_vnc_vncrfapidebugoptions.name
    data_gen['VNC_RFAPI_DEBUG_OPTIONS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_vnc_vncrfapidebugoptions.command('./	<cr>')
def frr_no_debug_bgp_vnc_vncrfapidebugoptions_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='vpn',)
def frr_no_debug_bgp_vpn(vpn_='vpn'):
    """VPN routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_vpn.name
    data_gen['vpn'] = vpn_='vpn'
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_vpn.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['leak-from-vrf', 'leak-to-vrf', 'rmap-event', 'label']), invoke_without_command=True)
def frr_no_debug_bgp_vpn_vpnvrfleakeventlabel():
    """leaked from vrf to vpn"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_vpn_vpnvrfleakeventlabel.name
    data_gen['VPN_VRF_LEAK_EVENT_LABEL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp'
    pass


@frr_no_debug_bgp_vpn_vpnvrfleakeventlabel.command('./	<cr>')
def frr_no_debug_bgp_vpn_vpnvrfleakeventlabel_cr():
    pass


@frr_no_debug_bgp.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_bgp_zebra(no_debug_bgp_zebra_='no_debug_bgp_zebra'):
    """BGP Zebra messages"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_zebra.name
    
    if 'VIEW_NODE|no_debug_bgp_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_zebra'
    pass


@frr_no_debug_bgp_zebra.command('./	<cr>')
def frr_no_debug_bgp_zebra_cr():
    pass


@frr_no_debug_bgp_zebra.group(cls=FRR_AbbreviationGroup, name='prefix',)
def frr_no_debug_bgp_zebra_prefix(prefix_='prefix'):
    """Specify a prefix to debug"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_zebra_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    
    if 'VIEW_NODE|no_debug_bgp_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_zebra'
    pass


@frr_no_debug_bgp_zebra_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_no_debug_bgp_zebra_prefix_prefixipprefix():
    """IPv4 prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_bgp_zebra_prefix_prefixipprefix.name
    data_gen['PREFIX_IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_bgp_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_bgp_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_bgp_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_bgp_zebra'
    pass


@frr_no_debug_bgp_zebra_prefix_prefixipprefix.command('./	<cr>')
def frr_no_debug_bgp_zebra_prefix_prefixipprefix_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='eigrp',)
def frr_no_debug_eigrp(no_debug_eigrp_='no_debug_eigrp'):
    """P information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp.name
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp.group(cls=FRR_AbbreviationGroup, name='packets',)
def frr_no_debug_eigrp_packets(packets_='packets'):
    """EIGRP packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp_packets.name
    data_gen['packets'] = packets_='packets'
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp_packets.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['siaquery', 'siareply', 'ack', 'hello', 'probe', 'query', 'reply', 'request', 'retry', 'stub', 'terse', 'update', 'all']), invoke_without_command=True)
def frr_no_debug_eigrp_packets_packetseigrppackettype():
    """EIGRP SIA-Query packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp_packets_packetseigrppackettype.name
    data_gen['PACKETS_EIGRP_PACKET_TYPE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype.command('./	<cr>')
def frr_no_debug_eigrp_packets_packetseigrppackettype_cr():
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_eigrp_packets_packetseigrppackettype_detail(detail_='detail'):
    """Detailed Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp_packets_packetseigrppackettype_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype_detail.command('./	<cr>')
def frr_no_debug_eigrp_packets_packetseigrppackettype_detail_cr():
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype.group(cls=FRR_AbbreviationGroup, name='receive', invoke_without_command=True)
def frr_no_debug_eigrp_packets_packetseigrppackettype_receive(receive_='receive'):
    """Receive Packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp_packets_packetseigrppackettype_receive.name
    data_gen['receive'] = receive_='receive'
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype_receive.command('./	<cr>')
def frr_no_debug_eigrp_packets_packetseigrppackettype_receive_cr():
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype_receive.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_eigrp_packets_packetseigrppackettype_receive_detail(receive_detail_='receive_detail'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp_packets_packetseigrppackettype_receive_detail.name
    data_gen['receive_detail'] = receive_detail_='receive_detail'
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype_receive_detail.command('./	<cr>')
def frr_no_debug_eigrp_packets_packetseigrppackettype_receive_detail_cr():
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype.group(cls=FRR_AbbreviationGroup, name='send', invoke_without_command=True)
def frr_no_debug_eigrp_packets_packetseigrppackettype_send(send_='send'):
    """Send Packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp_packets_packetseigrppackettype_send.name
    data_gen['send'] = send_='send'
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype_send.command('./	<cr>')
def frr_no_debug_eigrp_packets_packetseigrppackettype_send_cr():
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype_send.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_eigrp_packets_packetseigrppackettype_send_detail(send_detail_='send_detail'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp_packets_packetseigrppackettype_send_detail.name
    data_gen['send_detail'] = send_detail_='send_detail'
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp_packets_packetseigrppackettype_send_detail.command('./	<cr>')
def frr_no_debug_eigrp_packets_packetseigrppackettype_send_detail_cr():
    pass


@frr_no_debug_eigrp.group(cls=FRR_AbbreviationGroup, name='transmit',)
def frr_no_debug_eigrp_transmit(transmit_='transmit'):
    """EIGRP transmission events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp_transmit.name
    data_gen['transmit'] = transmit_='transmit'
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp_transmit.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['send', 'recv', 'all']), invoke_without_command=True)
def frr_no_debug_eigrp_transmit_transmiteigrppacketevent():
    """packet sent"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp_transmit_transmiteigrppacketevent.name
    data_gen['TRANSMIT_EIGRP_PACKET_EVENT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp_transmit_transmiteigrppacketevent.command('./	<cr>')
def frr_no_debug_eigrp_transmit_transmiteigrppacketevent_cr():
    pass


@frr_no_debug_eigrp_transmit_transmiteigrppacketevent.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_eigrp_transmit_transmiteigrppacketevent_detail(detail_='detail'):
    """Detailed Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_eigrp_transmit_transmiteigrppacketevent_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_eigrp'][key] = val
    
    # set VIEW_NODE -> no_debug_eigrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_eigrp'
    pass


@frr_no_debug_eigrp_transmit_transmiteigrppacketevent_detail.command('./	<cr>')
def frr_no_debug_eigrp_transmit_transmiteigrppacketevent_detail_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='igmp', invoke_without_command=True)
def frr_no_debug_igmp(no_debug_igmp_='no_debug_igmp'):
    """IGMP protocol activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_igmp.name
    
    if 'VIEW_NODE|no_debug_igmp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp'][key] = val
    
    # set VIEW_NODE -> no_debug_igmp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_igmp'
    pass


@frr_no_debug_igmp.command('./	<cr>')
def frr_no_debug_igmp_cr():
    pass


@frr_no_debug_igmp.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_igmp_events(events_='events'):
    """IGMP protocol events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_igmp_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_igmp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp'][key] = val
    
    # set VIEW_NODE -> no_debug_igmp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_igmp'
    pass


@frr_no_debug_igmp_events.command('./	<cr>')
def frr_no_debug_igmp_events_cr():
    pass


@frr_no_debug_igmp.group(cls=FRR_AbbreviationGroup, name='packets', invoke_without_command=True)
def frr_no_debug_igmp_packets(packets_='packets'):
    """IGMP protocol packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_igmp_packets.name
    data_gen['packets'] = packets_='packets'
    
    if 'VIEW_NODE|no_debug_igmp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp'][key] = val
    
    # set VIEW_NODE -> no_debug_igmp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_igmp'
    pass


@frr_no_debug_igmp_packets.command('./	<cr>')
def frr_no_debug_igmp_packets_cr():
    pass


@frr_no_debug_igmp.group(cls=FRR_AbbreviationGroup, name='trace', invoke_without_command=True)
def frr_no_debug_igmp_trace(no_debug_igmp_trace_='no_debug_igmp_trace'):
    """IGMP internal daemon activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_igmp_trace.name
    
    if 'VIEW_NODE|no_debug_igmp_trace' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp_trace'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp_trace']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp_trace'][key] = val
    
    # set VIEW_NODE -> no_debug_igmp_trace table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_igmp_trace'
    pass


@frr_no_debug_igmp_trace.command('./	<cr>')
def frr_no_debug_igmp_trace_cr():
    pass


@frr_no_debug_igmp_trace.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_igmp_trace_detail(detail_='detail'):
    """detailed"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_igmp_trace_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_igmp_trace' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp_trace'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp_trace']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_igmp_trace'][key] = val
    
    # set VIEW_NODE -> no_debug_igmp_trace table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_igmp_trace'
    pass


@frr_no_debug_igmp_trace_detail.command('./	<cr>')
def frr_no_debug_igmp_trace_detail_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='isis',)
def frr_no_debug_isis(no_debug_isis_='no_debug_isis'):
    """OpenFabric routing protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis.name
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='adj-packets', invoke_without_command=True)
def frr_no_debug_isis_adjpackets(adjpackets_='adj-packets'):
    """IS-IS Adjacency related packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_adjpackets.name
    data_gen['adj-packets'] = adjpackets_='adj-packets'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_adjpackets.command('./	<cr>')
def frr_no_debug_isis_adjpackets_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='bfd', invoke_without_command=True)
def frr_no_debug_isis_bfd(bfd_='bfd'):
    """PROTO_NAME interaction with BFD"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_bfd.name
    data_gen['bfd'] = bfd_='bfd'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_bfd.command('./	<cr>')
def frr_no_debug_isis_bfd_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_isis_events(events_='events'):
    """IS-IS Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_events.command('./	<cr>')
def frr_no_debug_isis_events_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='flooding', invoke_without_command=True)
def frr_no_debug_isis_flooding(flooding_='flooding'):
    """Flooding algorithm"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_flooding.name
    data_gen['flooding'] = flooding_='flooding'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_flooding.command('./	<cr>')
def frr_no_debug_isis_flooding_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='ldp-sync', invoke_without_command=True)
def frr_no_debug_isis_ldpsync(ldpsync_='ldp-sync'):
    """PROTO_NAME interaction with LDP-Sync"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_ldpsync.name
    data_gen['ldp-sync'] = ldpsync_='ldp-sync'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_ldpsync.command('./	<cr>')
def frr_no_debug_isis_ldpsync_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='lfa', invoke_without_command=True)
def frr_no_debug_isis_lfa(lfa_='lfa'):
    """IS-IS LFA Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_lfa.name
    data_gen['lfa'] = lfa_='lfa'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_lfa.command('./	<cr>')
def frr_no_debug_isis_lfa_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='lsp-gen', invoke_without_command=True)
def frr_no_debug_isis_lspgen(lspgen_='lsp-gen'):
    """IS-IS generation of own LSPs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_lspgen.name
    data_gen['lsp-gen'] = lspgen_='lsp-gen'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_lspgen.command('./	<cr>')
def frr_no_debug_isis_lspgen_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='lsp-sched', invoke_without_command=True)
def frr_no_debug_isis_lspsched(lspsched_='lsp-sched'):
    """IS-IS scheduling of LSP generation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_lspsched.name
    data_gen['lsp-sched'] = lspsched_='lsp-sched'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_lspsched.command('./	<cr>')
def frr_no_debug_isis_lspsched_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='packet-dump', invoke_without_command=True)
def frr_no_debug_isis_packetdump(packetdump_='packet-dump'):
    """IS-IS packet dump"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_packetdump.name
    data_gen['packet-dump'] = packetdump_='packet-dump'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_packetdump.command('./	<cr>')
def frr_no_debug_isis_packetdump_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='route-events', invoke_without_command=True)
def frr_no_debug_isis_routeevents(routeevents_='route-events'):
    """IS-IS Route related events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_routeevents.name
    data_gen['route-events'] = routeevents_='route-events'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_routeevents.command('./	<cr>')
def frr_no_debug_isis_routeevents_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='snp-packets', invoke_without_command=True)
def frr_no_debug_isis_snppackets(snppackets_='snp-packets'):
    """IS-IS CSNP/PSNP packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_snppackets.name
    data_gen['snp-packets'] = snppackets_='snp-packets'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_snppackets.command('./	<cr>')
def frr_no_debug_isis_snppackets_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='spf-events', invoke_without_command=True)
def frr_no_debug_isis_spfevents(spfevents_='spf-events'):
    """IS-IS Shortest Path First Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_spfevents.name
    data_gen['spf-events'] = spfevents_='spf-events'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_spfevents.command('./	<cr>')
def frr_no_debug_isis_spfevents_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='sr-events', invoke_without_command=True)
def frr_no_debug_isis_srevents(srevents_='sr-events'):
    """IS-IS Segment Routing Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_srevents.name
    data_gen['sr-events'] = srevents_='sr-events'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_srevents.command('./	<cr>')
def frr_no_debug_isis_srevents_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='te-events', invoke_without_command=True)
def frr_no_debug_isis_teevents(teevents_='te-events'):
    """IS-IS Traffic Engineering Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_teevents.name
    data_gen['te-events'] = teevents_='te-events'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_teevents.command('./	<cr>')
def frr_no_debug_isis_teevents_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='tx-queue', invoke_without_command=True)
def frr_no_debug_isis_txqueue(txqueue_='tx-queue'):
    """IS-IS TX queues"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_txqueue.name
    data_gen['tx-queue'] = txqueue_='tx-queue'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_txqueue.command('./	<cr>')
def frr_no_debug_isis_txqueue_cr():
    pass


@frr_no_debug_isis.group(cls=FRR_AbbreviationGroup, name='update-packets', invoke_without_command=True)
def frr_no_debug_isis_updatepackets(updatepackets_='update-packets'):
    """IS-IS Update related packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_isis_updatepackets.name
    data_gen['update-packets'] = updatepackets_='update-packets'
    
    if 'VIEW_NODE|no_debug_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_isis'][key] = val
    
    # set VIEW_NODE -> no_debug_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_isis'
    pass


@frr_no_debug_isis_updatepackets.command('./	<cr>')
def frr_no_debug_isis_updatepackets_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='memstats-at-exit', invoke_without_command=True)
def frr_no_debug_memstatsatexit(memstatsatexit_='memstats-at-exit'):
    """Print memory type statistics at exit"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_memstatsatexit.name
    data_gen['memstats-at-exit'] = memstatsatexit_='memstats-at-exit'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_memstatsatexit.command('./	<cr>')
def frr_no_debug_memstatsatexit_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='mld', invoke_without_command=True)
def frr_no_debug_mld(no_debug_mld_='no_debug_mld'):
    """MLD protocol activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mld.name
    
    if 'VIEW_NODE|no_debug_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mld'][key] = val
    
    # set VIEW_NODE -> no_debug_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mld'
    pass


@frr_no_debug_mld.command('./	<cr>')
def frr_no_debug_mld_cr():
    pass


@frr_no_debug_mld.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_mld_events(events_='events'):
    """MLD protocol events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mld_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mld'][key] = val
    
    # set VIEW_NODE -> no_debug_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mld'
    pass


@frr_no_debug_mld_events.command('./	<cr>')
def frr_no_debug_mld_events_cr():
    pass


@frr_no_debug_mld.group(cls=FRR_AbbreviationGroup, name='packets', invoke_without_command=True)
def frr_no_debug_mld_packets(packets_='packets'):
    """MLD protocol packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mld_packets.name
    data_gen['packets'] = packets_='packets'
    
    if 'VIEW_NODE|no_debug_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mld'][key] = val
    
    # set VIEW_NODE -> no_debug_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mld'
    pass


@frr_no_debug_mld_packets.command('./	<cr>')
def frr_no_debug_mld_packets_cr():
    pass


@frr_no_debug_mld.group(cls=FRR_AbbreviationGroup, name='trace', invoke_without_command=True)
def frr_no_debug_mld_trace(no_debug_mld_trace_='no_debug_mld_trace'):
    """MLD internal daemon activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mld_trace.name
    
    if 'VIEW_NODE|no_debug_mld_trace' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mld_trace'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mld_trace']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mld_trace'][key] = val
    
    # set VIEW_NODE -> no_debug_mld_trace table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mld_trace'
    pass


@frr_no_debug_mld_trace.command('./	<cr>')
def frr_no_debug_mld_trace_cr():
    pass


@frr_no_debug_mld_trace.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_mld_trace_detail(detail_='detail'):
    """detailed"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mld_trace_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_mld_trace' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mld_trace'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mld_trace']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mld_trace'][key] = val
    
    # set VIEW_NODE -> no_debug_mld_trace table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mld_trace'
    pass


@frr_no_debug_mld_trace_detail.command('./	<cr>')
def frr_no_debug_mld_trace_detail_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='mpls',)
def frr_no_debug_mpls():
    """MPLS information"""
    global COMMON_DATA_MAP
    
    pass


@frr_no_debug_mpls.group(cls=FRR_AbbreviationGroup, name='ldp',)
def frr_no_debug_mpls_ldp(no_debug_mpls_ldp_='no_debug_mpls_ldp'):
    """Label Distribution Protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mpls_ldp.name
    
    if 'VIEW_NODE|no_debug_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> no_debug_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mpls_ldp'
    pass


@frr_no_debug_mpls_ldp.group(cls=FRR_AbbreviationGroup, name='discovery',)
def frr_no_debug_mpls_ldp_discovery(no_debug_mpls_ldp_discovery_='no_debug_mpls_ldp_discovery'):
    """Discovery messages"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mpls_ldp_discovery.name
    
    if 'VIEW_NODE|no_debug_mpls_ldp_discovery' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_discovery'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_discovery']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_discovery'][key] = val
    
    # set VIEW_NODE -> no_debug_mpls_ldp_discovery table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mpls_ldp_discovery'
    pass


@frr_no_debug_mpls_ldp_discovery.group(cls=FRR_AbbreviationGroup, name='hello',)
def frr_no_debug_mpls_ldp_discovery_hello(hello_='hello'):
    """Discovery hello message"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mpls_ldp_discovery_hello.name
    data_gen['hello'] = hello_='hello'
    
    if 'VIEW_NODE|no_debug_mpls_ldp_discovery' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_discovery'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_discovery']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_discovery'][key] = val
    
    # set VIEW_NODE -> no_debug_mpls_ldp_discovery table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mpls_ldp_discovery'
    pass


@frr_no_debug_mpls_ldp_discovery_hello.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['recv', 'sent']), invoke_without_command=True)
def frr_no_debug_mpls_ldp_discovery_hello_hellocommunicationmode():
    """Received messages"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mpls_ldp_discovery_hello_hellocommunicationmode.name
    data_gen['HELLO_COMMUNICATION_MODE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_mpls_ldp_discovery' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_discovery'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_discovery']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_discovery'][key] = val
    
    # set VIEW_NODE -> no_debug_mpls_ldp_discovery table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mpls_ldp_discovery'
    pass


@frr_no_debug_mpls_ldp_discovery_hello_hellocommunicationmode.command('./	<cr>')
def frr_no_debug_mpls_ldp_discovery_hello_hellocommunicationmode_cr():
    pass


@frr_no_debug_mpls_ldp.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['errors', 'event', 'labels', 'sync', 'zebra']), invoke_without_command=True)
def frr_no_debug_mpls_ldp_ldpchoicecase():
    """Errors"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mpls_ldp_ldpchoicecase.name
    data_gen['LDP_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> no_debug_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mpls_ldp'
    pass


@frr_no_debug_mpls_ldp_ldpchoicecase.command('./	<cr>')
def frr_no_debug_mpls_ldp_ldpchoicecase_cr():
    pass


@frr_no_debug_mpls_ldp.group(cls=FRR_AbbreviationGroup, name='messages', invoke_without_command=True)
def frr_no_debug_mpls_ldp_messages():
    """Messages"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mpls_ldp_messages.name
    
    if 'VIEW_NODE|no_debug_mpls_ldp_messages' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages'][key] = val
    
    # set VIEW_NODE -> no_debug_mpls_ldp_messages table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mpls_ldp_messages'
    pass


@frr_no_debug_mpls_ldp_messages.command('./	<cr>')
def frr_no_debug_mpls_ldp_messages_cr():
    pass


@frr_no_debug_mpls_ldp_messages.group(cls=FRR_AbbreviationGroup, name='recv', invoke_without_command=True)
def frr_no_debug_mpls_ldp_messages_recv(no_debug_mpls_ldp_messages_recv_='no_debug_mpls_ldp_messages_recv'):
    """Received messages, excluding periodic Keep Alives"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mpls_ldp_messages_recv.name
    
    if 'VIEW_NODE|no_debug_mpls_ldp_messages_recv' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_recv'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_recv']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_recv'][key] = val
    
    # set VIEW_NODE -> no_debug_mpls_ldp_messages_recv table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mpls_ldp_messages_recv'
    pass


@frr_no_debug_mpls_ldp_messages_recv.command('./	<cr>')
def frr_no_debug_mpls_ldp_messages_recv_cr():
    pass


@frr_no_debug_mpls_ldp_messages_recv.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_no_debug_mpls_ldp_messages_recv_all(all_='all'):
    """Received messages, including periodic Keep Alives"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mpls_ldp_messages_recv_all.name
    data_gen['all'] = all_='all'
    
    if 'VIEW_NODE|no_debug_mpls_ldp_messages_recv' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_recv'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_recv']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_recv'][key] = val
    
    # set VIEW_NODE -> no_debug_mpls_ldp_messages_recv table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mpls_ldp_messages_recv'
    pass


@frr_no_debug_mpls_ldp_messages_recv_all.command('./	<cr>')
def frr_no_debug_mpls_ldp_messages_recv_all_cr():
    pass


@frr_no_debug_mpls_ldp_messages.group(cls=FRR_AbbreviationGroup, name='sent', invoke_without_command=True)
def frr_no_debug_mpls_ldp_messages_sent(no_debug_mpls_ldp_messages_sent_='no_debug_mpls_ldp_messages_sent'):
    """Sent messages, excluding periodic Keep Alives"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mpls_ldp_messages_sent.name
    
    if 'VIEW_NODE|no_debug_mpls_ldp_messages_sent' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_sent'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_sent']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_sent'][key] = val
    
    # set VIEW_NODE -> no_debug_mpls_ldp_messages_sent table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mpls_ldp_messages_sent'
    pass


@frr_no_debug_mpls_ldp_messages_sent.command('./	<cr>')
def frr_no_debug_mpls_ldp_messages_sent_cr():
    pass


@frr_no_debug_mpls_ldp_messages_sent.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_no_debug_mpls_ldp_messages_sent_all(all_='all'):
    """Sent messages, including periodic Keep Alives"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mpls_ldp_messages_sent_all.name
    data_gen['all'] = all_='all'
    
    if 'VIEW_NODE|no_debug_mpls_ldp_messages_sent' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_sent'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_sent']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mpls_ldp_messages_sent'][key] = val
    
    # set VIEW_NODE -> no_debug_mpls_ldp_messages_sent table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mpls_ldp_messages_sent'
    pass


@frr_no_debug_mpls_ldp_messages_sent_all.command('./	<cr>')
def frr_no_debug_mpls_ldp_messages_sent_all_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='mroute', invoke_without_command=True)
def frr_no_debug_mroute(no_debug_mroute_='no_debug_mroute'):
    """PIM interaction with kernel MFC cache"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mroute.name
    
    if 'VIEW_NODE|no_debug_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute'][key] = val
    
    # set VIEW_NODE -> no_debug_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mroute'
    pass


@frr_no_debug_mroute.command('./	<cr>')
def frr_no_debug_mroute_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='mroute6', invoke_without_command=True)
def frr_no_debug_mroute6(no_debug_mroute6_='no_debug_mroute6'):
    """PIMv6 interaction with kernel MFC cache"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mroute6.name
    
    if 'VIEW_NODE|no_debug_mroute6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute6'][key] = val
    
    # set VIEW_NODE -> no_debug_mroute6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mroute6'
    pass


@frr_no_debug_mroute6.command('./	<cr>')
def frr_no_debug_mroute6_cr():
    pass


@frr_no_debug_mroute6.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_mroute6_detail(detail_='detail'):
    """detailed"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mroute6_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_mroute6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute6'][key] = val
    
    # set VIEW_NODE -> no_debug_mroute6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mroute6'
    pass


@frr_no_debug_mroute6_detail.command('./	<cr>')
def frr_no_debug_mroute6_detail_cr():
    pass


@frr_no_debug_mroute.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_mroute_detail(detail_='detail'):
    """detailed"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mroute_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_mroute'][key] = val
    
    # set VIEW_NODE -> no_debug_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_mroute'
    pass


@frr_no_debug_mroute_detail.command('./	<cr>')
def frr_no_debug_mroute_detail_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='msdp', invoke_without_command=True)
def frr_no_debug_msdp(no_debug_msdp_='no_debug_msdp'):
    """MSDP protocol activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_msdp.name
    
    if 'VIEW_NODE|no_debug_msdp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_msdp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_msdp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_msdp'][key] = val
    
    # set VIEW_NODE -> no_debug_msdp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_msdp'
    pass


@frr_no_debug_msdp.command('./	<cr>')
def frr_no_debug_msdp_cr():
    pass


@frr_no_debug_msdp.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_msdp_events(events_='events'):
    """MSDP protocol events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_msdp_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_msdp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_msdp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_msdp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_msdp'][key] = val
    
    # set VIEW_NODE -> no_debug_msdp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_msdp'
    pass


@frr_no_debug_msdp_events.command('./	<cr>')
def frr_no_debug_msdp_events_cr():
    pass


@frr_no_debug_msdp.group(cls=FRR_AbbreviationGroup, name='packets', invoke_without_command=True)
def frr_no_debug_msdp_packets(packets_='packets'):
    """MSDP protocol packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_msdp_packets.name
    data_gen['packets'] = packets_='packets'
    
    if 'VIEW_NODE|no_debug_msdp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_msdp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_msdp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_msdp'][key] = val
    
    # set VIEW_NODE -> no_debug_msdp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_msdp'
    pass


@frr_no_debug_msdp_packets.command('./	<cr>')
def frr_no_debug_msdp_packets_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='mtrace', invoke_without_command=True)
def frr_no_debug_mtrace(mtrace_='mtrace'):
    """Mtrace protocol activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_mtrace.name
    data_gen['mtrace'] = mtrace_='mtrace'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_mtrace.command('./	<cr>')
def frr_no_debug_mtrace_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='nhrp',)
def frr_no_debug_nhrp(nhrp_='nhrp'):
    """NHRP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_nhrp.name
    data_gen['nhrp'] = nhrp_='nhrp'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_nhrp.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['all', 'common', 'event', 'interface', 'kernel', 'route', 'vici']), invoke_without_command=True)
def frr_no_debug_nhrp_nhrplogcategory():
    """All messages"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_nhrp_nhrplogcategory.name
    data_gen['NHRP_LOG_CATEGORY'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_nhrp_nhrplogcategory.command('./	<cr>')
def frr_no_debug_nhrp_nhrplogcategory_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='northbound', invoke_without_command=True)
def frr_no_debug_northbound(no_debug_northbound_='no_debug_northbound'):
    """Northbound debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound.name
    
    if 'VIEW_NODE|no_debug_northbound' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound'
    pass


@frr_no_debug_northbound.command('./	<cr>')
def frr_no_debug_northbound_cr():
    pass


@frr_no_debug_northbound.group(cls=FRR_AbbreviationGroup, name='callbacks', invoke_without_command=True)
def frr_no_debug_northbound_callbacks(no_debug_northbound_callbacks_='no_debug_northbound_callbacks'):
    """Callbacks"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound_callbacks.name
    
    if 'VIEW_NODE|no_debug_northbound_callbacks' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound_callbacks table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound_callbacks'
    pass


@frr_no_debug_northbound_callbacks.command('./	<cr>')
def frr_no_debug_northbound_callbacks_cr():
    pass


@frr_no_debug_northbound_callbacks.group(cls=FRR_AbbreviationGroup, name='configuration', invoke_without_command=True)
def frr_no_debug_northbound_callbacks_configuration(configuration_='configuration'):
    """Configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound_callbacks_configuration.name
    data_gen['configuration'] = configuration_='configuration'
    
    if 'VIEW_NODE|no_debug_northbound_callbacks' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound_callbacks table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound_callbacks'
    pass


@frr_no_debug_northbound_callbacks_configuration.command('./	<cr>')
def frr_no_debug_northbound_callbacks_configuration_cr():
    pass


@frr_no_debug_northbound_callbacks.group(cls=FRR_AbbreviationGroup, name='rpc', invoke_without_command=True)
def frr_no_debug_northbound_callbacks_rpc(rpc_='rpc'):
    """RPC"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound_callbacks_rpc.name
    data_gen['rpc'] = rpc_='rpc'
    
    if 'VIEW_NODE|no_debug_northbound_callbacks' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound_callbacks table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound_callbacks'
    pass


@frr_no_debug_northbound_callbacks_rpc.command('./	<cr>')
def frr_no_debug_northbound_callbacks_rpc_cr():
    pass


@frr_no_debug_northbound_callbacks.group(cls=FRR_AbbreviationGroup, name='state', invoke_without_command=True)
def frr_no_debug_northbound_callbacks_state(state_='state'):
    """State"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound_callbacks_state.name
    data_gen['state'] = state_='state'
    
    if 'VIEW_NODE|no_debug_northbound_callbacks' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_callbacks'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound_callbacks table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound_callbacks'
    pass


@frr_no_debug_northbound_callbacks_state.command('./	<cr>')
def frr_no_debug_northbound_callbacks_state_cr():
    pass


@frr_no_debug_northbound.group(cls=FRR_AbbreviationGroup, name='client',)
def frr_no_debug_northbound_client(no_debug_northbound_client_='no_debug_northbound_client'):
    """Northbound client"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound_client.name
    
    if 'VIEW_NODE|no_debug_northbound_client' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_client'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_client']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_client'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound_client table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound_client'
    pass


@frr_no_debug_northbound_client.group(cls=FRR_AbbreviationGroup, name='confd', invoke_without_command=True)
def frr_no_debug_northbound_client_confd(confd_='confd'):
    """ConfD"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound_client_confd.name
    data_gen['confd'] = confd_='confd'
    
    if 'VIEW_NODE|no_debug_northbound_client' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_client'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_client']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_client'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound_client table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound_client'
    pass


@frr_no_debug_northbound_client_confd.command('./	<cr>')
def frr_no_debug_northbound_client_confd_cr():
    pass


@frr_no_debug_northbound_client.group(cls=FRR_AbbreviationGroup, name='sysrepo', invoke_without_command=True)
def frr_no_debug_northbound_client_sysrepo(sysrepo_='sysrepo'):
    """Sysrepo"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound_client_sysrepo.name
    data_gen['sysrepo'] = sysrepo_='sysrepo'
    
    if 'VIEW_NODE|no_debug_northbound_client' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_client'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_client']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound_client'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound_client table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound_client'
    pass


@frr_no_debug_northbound_client_sysrepo.command('./	<cr>')
def frr_no_debug_northbound_client_sysrepo_cr():
    pass


@frr_no_debug_northbound.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_northbound_events(events_='events'):
    """Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_northbound' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound'
    pass


@frr_no_debug_northbound_events.command('./	<cr>')
def frr_no_debug_northbound_events_cr():
    pass


@frr_no_debug_northbound.group(cls=FRR_AbbreviationGroup, name='libyang', invoke_without_command=True)
def frr_no_debug_northbound_libyang(libyang_='libyang'):
    """libyang debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound_libyang.name
    data_gen['libyang'] = libyang_='libyang'
    
    if 'VIEW_NODE|no_debug_northbound' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound'
    pass


@frr_no_debug_northbound_libyang.command('./	<cr>')
def frr_no_debug_northbound_libyang_cr():
    pass


@frr_no_debug_northbound.group(cls=FRR_AbbreviationGroup, name='notifications', invoke_without_command=True)
def frr_no_debug_northbound_notifications(notifications_='notifications'):
    """Notifications"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_northbound_notifications.name
    data_gen['notifications'] = notifications_='notifications'
    
    if 'VIEW_NODE|no_debug_northbound' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_northbound'][key] = val
    
    # set VIEW_NODE -> no_debug_northbound table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_northbound'
    pass


@frr_no_debug_northbound_notifications.command('./	<cr>')
def frr_no_debug_northbound_notifications_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='openfabric',)
def frr_no_debug_openfabric(no_debug_openfabric_='no_debug_openfabric'):
    """OpenFabric routing protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric.name
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='adj-packets', invoke_without_command=True)
def frr_no_debug_openfabric_adjpackets(adjpackets_='adj-packets'):
    """IS-IS Adjacency related packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_adjpackets.name
    data_gen['adj-packets'] = adjpackets_='adj-packets'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_adjpackets.command('./	<cr>')
def frr_no_debug_openfabric_adjpackets_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='bfd', invoke_without_command=True)
def frr_no_debug_openfabric_bfd(bfd_='bfd'):
    """PROTO_NAME interaction with BFD"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_bfd.name
    data_gen['bfd'] = bfd_='bfd'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_bfd.command('./	<cr>')
def frr_no_debug_openfabric_bfd_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_openfabric_events(events_='events'):
    """IS-IS Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_events.command('./	<cr>')
def frr_no_debug_openfabric_events_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='flooding', invoke_without_command=True)
def frr_no_debug_openfabric_flooding(flooding_='flooding'):
    """Flooding algorithm"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_flooding.name
    data_gen['flooding'] = flooding_='flooding'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_flooding.command('./	<cr>')
def frr_no_debug_openfabric_flooding_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='ldp-sync', invoke_without_command=True)
def frr_no_debug_openfabric_ldpsync(ldpsync_='ldp-sync'):
    """PROTO_NAME interaction with LDP-Sync"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_ldpsync.name
    data_gen['ldp-sync'] = ldpsync_='ldp-sync'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_ldpsync.command('./	<cr>')
def frr_no_debug_openfabric_ldpsync_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='lfa', invoke_without_command=True)
def frr_no_debug_openfabric_lfa(lfa_='lfa'):
    """IS-IS LFA Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_lfa.name
    data_gen['lfa'] = lfa_='lfa'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_lfa.command('./	<cr>')
def frr_no_debug_openfabric_lfa_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='lsp-gen', invoke_without_command=True)
def frr_no_debug_openfabric_lspgen(lspgen_='lsp-gen'):
    """IS-IS generation of own LSPs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_lspgen.name
    data_gen['lsp-gen'] = lspgen_='lsp-gen'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_lspgen.command('./	<cr>')
def frr_no_debug_openfabric_lspgen_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='lsp-sched', invoke_without_command=True)
def frr_no_debug_openfabric_lspsched(lspsched_='lsp-sched'):
    """IS-IS scheduling of LSP generation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_lspsched.name
    data_gen['lsp-sched'] = lspsched_='lsp-sched'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_lspsched.command('./	<cr>')
def frr_no_debug_openfabric_lspsched_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='packet-dump', invoke_without_command=True)
def frr_no_debug_openfabric_packetdump(packetdump_='packet-dump'):
    """IS-IS packet dump"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_packetdump.name
    data_gen['packet-dump'] = packetdump_='packet-dump'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_packetdump.command('./	<cr>')
def frr_no_debug_openfabric_packetdump_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='route-events', invoke_without_command=True)
def frr_no_debug_openfabric_routeevents(routeevents_='route-events'):
    """IS-IS Route related events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_routeevents.name
    data_gen['route-events'] = routeevents_='route-events'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_routeevents.command('./	<cr>')
def frr_no_debug_openfabric_routeevents_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='snp-packets', invoke_without_command=True)
def frr_no_debug_openfabric_snppackets(snppackets_='snp-packets'):
    """IS-IS CSNP/PSNP packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_snppackets.name
    data_gen['snp-packets'] = snppackets_='snp-packets'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_snppackets.command('./	<cr>')
def frr_no_debug_openfabric_snppackets_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='spf-events', invoke_without_command=True)
def frr_no_debug_openfabric_spfevents(spfevents_='spf-events'):
    """IS-IS Shortest Path First Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_spfevents.name
    data_gen['spf-events'] = spfevents_='spf-events'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_spfevents.command('./	<cr>')
def frr_no_debug_openfabric_spfevents_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='sr-events', invoke_without_command=True)
def frr_no_debug_openfabric_srevents(srevents_='sr-events'):
    """IS-IS Segment Routing Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_srevents.name
    data_gen['sr-events'] = srevents_='sr-events'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_srevents.command('./	<cr>')
def frr_no_debug_openfabric_srevents_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='te-events', invoke_without_command=True)
def frr_no_debug_openfabric_teevents(teevents_='te-events'):
    """IS-IS Traffic Engineering Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_teevents.name
    data_gen['te-events'] = teevents_='te-events'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_teevents.command('./	<cr>')
def frr_no_debug_openfabric_teevents_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='tx-queue', invoke_without_command=True)
def frr_no_debug_openfabric_txqueue(txqueue_='tx-queue'):
    """IS-IS TX queues"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_txqueue.name
    data_gen['tx-queue'] = txqueue_='tx-queue'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_txqueue.command('./	<cr>')
def frr_no_debug_openfabric_txqueue_cr():
    pass


@frr_no_debug_openfabric.group(cls=FRR_AbbreviationGroup, name='update-packets', invoke_without_command=True)
def frr_no_debug_openfabric_updatepackets(updatepackets_='update-packets'):
    """IS-IS Update related packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_openfabric_updatepackets.name
    data_gen['update-packets'] = updatepackets_='update-packets'
    
    if 'VIEW_NODE|no_debug_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_openfabric'][key] = val
    
    # set VIEW_NODE -> no_debug_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_openfabric'
    pass


@frr_no_debug_openfabric_updatepackets.command('./	<cr>')
def frr_no_debug_openfabric_updatepackets_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='ospf', invoke_without_command=True)
def frr_no_debug_ospf(no_debug_ospf_='no_debug_ospf'):
    """OSPF information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf.name
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf.command('./	<cr>')
def frr_no_debug_ospf_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='ospf6', invoke_without_command=True)
def frr_no_debug_ospf6(no_debug_ospf6_='no_debug_ospf6'):
    """Open Shortest Path First (OSPF) for IPv6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6.name
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6.command('./	<cr>')
def frr_no_debug_ospf6_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='abr', invoke_without_command=True)
def frr_no_debug_ospf6_abr(abr_='abr'):
    """Debug OSPFv3 ABR function"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_abr.name
    data_gen['abr'] = abr_='abr'
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_abr.command('./	<cr>')
def frr_no_debug_ospf6_abr_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='asbr', invoke_without_command=True)
def frr_no_debug_ospf6_asbr(asbr_='asbr'):
    """Debug OSPFv3 ASBR function"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_asbr.name
    data_gen['asbr'] = asbr_='asbr'
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_asbr.command('./	<cr>')
def frr_no_debug_ospf6_asbr_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='authentication', invoke_without_command=True)
def frr_no_debug_ospf6_authentication(no_debug_ospf6_authentication_='no_debug_ospf6_authentication'):
    """debug OSPF6 authentication"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_authentication.name
    
    if 'VIEW_NODE|no_debug_ospf6_authentication' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_authentication'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_authentication']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_authentication'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_authentication table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_authentication'
    pass


@frr_no_debug_ospf6_authentication.command('./	<cr>')
def frr_no_debug_ospf6_authentication_cr():
    pass


@frr_no_debug_ospf6_authentication.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['tx', 'rx']), invoke_without_command=True)
def frr_no_debug_ospf6_authentication_choicecase():
    """debug authentication tx"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_authentication_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf6_authentication' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_authentication'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_authentication']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_authentication'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_authentication table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_authentication'
    pass


@frr_no_debug_ospf6_authentication_choicecase.command('./	<cr>')
def frr_no_debug_ospf6_authentication_choicecase_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='border-routers', invoke_without_command=True)
def frr_no_debug_ospf6_borderrouters():
    """Debug border router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_borderrouters.name
    
    if 'VIEW_NODE|no_debug_ospf6_border-routers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_border-routers table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_border-routers'
    pass


@frr_no_debug_ospf6_borderrouters.command('./	<cr>')
def frr_no_debug_ospf6_borderrouters_cr():
    pass


@frr_no_debug_ospf6_borderrouters.group(cls=FRR_AbbreviationGroup, name='area-id', invoke_without_command=True)
def frr_no_debug_ospf6_borderrouters_areaid(no_debug_ospf6_borderrouters_areaid_='no_debug_ospf6_border-routers_area-id'):
    """Debug border routers in specific Area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_borderrouters_areaid.name
    
    if 'VIEW_NODE|no_debug_ospf6_border-routers_area-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_area-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_area-id']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_area-id'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_border-routers_area-id table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_border-routers_area-id'
    pass


@frr_no_debug_ospf6_borderrouters_areaid.command('./	<cr>')
def frr_no_debug_ospf6_borderrouters_areaid_cr():
    pass


@frr_no_debug_ospf6_borderrouters_areaid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D']), invoke_without_command=True)
def frr_no_debug_ospf6_borderrouters_areaid_specifyareaid():
    """Specify Area-ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_borderrouters_areaid_specifyareaid.name
    data_gen['SPECIFY_AREA-ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf6_border-routers_area-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_area-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_area-id']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_area-id'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_border-routers_area-id table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_border-routers_area-id'
    pass


@frr_no_debug_ospf6_borderrouters_areaid_specifyareaid.command('./	<cr>')
def frr_no_debug_ospf6_borderrouters_areaid_specifyareaid_cr():
    pass


@frr_no_debug_ospf6_borderrouters.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
def frr_no_debug_ospf6_borderrouters_routerid(no_debug_ospf6_borderrouters_routerid_='no_debug_ospf6_border-routers_router-id'):
    """Debug specific border router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_borderrouters_routerid.name
    
    if 'VIEW_NODE|no_debug_ospf6_border-routers_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_router-id'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_border-routers_router-id table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_border-routers_router-id'
    pass


@frr_no_debug_ospf6_borderrouters_routerid.command('./	<cr>')
def frr_no_debug_ospf6_borderrouters_routerid_cr():
    pass


@frr_no_debug_ospf6_borderrouters_routerid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D']), invoke_without_command=True)
def frr_no_debug_ospf6_borderrouters_routerid_specifyborderrouterrouterid():
    """Specify border-router's router-id"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_borderrouters_routerid_specifyborderrouterrouterid.name
    data_gen['SPECIFY_BORDER-ROUTER_ROUTER-ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf6_border-routers_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_border-routers_router-id'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_border-routers_router-id table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_border-routers_router-id'
    pass


@frr_no_debug_ospf6_borderrouters_routerid_specifyborderrouterrouterid.command('./	<cr>')
def frr_no_debug_ospf6_borderrouters_routerid_specifyborderrouterrouterid_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='flooding', invoke_without_command=True)
def frr_no_debug_ospf6_flooding(flooding_='flooding'):
    """Debug OSPFv3 flooding function"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_flooding.name
    data_gen['flooding'] = flooding_='flooding'
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_flooding.command('./	<cr>')
def frr_no_debug_ospf6_flooding_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='graceful-restart', invoke_without_command=True)
def frr_no_debug_ospf6_gracefulrestart(gracefulrestart_='graceful-restart'):
    """Graceful restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_gracefulrestart.name
    data_gen['graceful-restart'] = gracefulrestart_='graceful-restart'
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_gracefulrestart.command('./	<cr>')
def frr_no_debug_ospf6_gracefulrestart_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_no_debug_ospf6_interface(interface_='interface'):
    """Debug OSPFv3 Interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_interface.name
    data_gen['interface'] = interface_='interface'
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_interface.command('./	<cr>')
def frr_no_debug_ospf6_interface_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='lsa',)
def frr_no_debug_ospf6_lsa(no_debug_ospf6_lsa_='no_debug_ospf6_lsa'):
    """Debug Link State Advertisements (LSAs)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_lsa.name
    
    if 'VIEW_NODE|no_debug_ospf6_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_lsa table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_lsa'
    pass


@frr_no_debug_ospf6_lsa.group(cls=FRR_AbbreviationGroup, name='aggregation', invoke_without_command=True)
def frr_no_debug_ospf6_lsa_aggregation(aggregation_='aggregation'):
    """External LSA Aggregation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_lsa_aggregation.name
    data_gen['aggregation'] = aggregation_='aggregation'
    
    if 'VIEW_NODE|no_debug_ospf6_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_lsa table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_lsa'
    pass


@frr_no_debug_ospf6_lsa_aggregation.command('./	<cr>')
def frr_no_debug_ospf6_lsa_aggregation_cr():
    pass


@frr_no_debug_ospf6_lsa.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_no_debug_ospf6_lsa_all(all_='all'):
    """Display for all types of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_lsa_all.name
    data_gen['all'] = all_='all'
    
    if 'VIEW_NODE|no_debug_ospf6_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_lsa table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_lsa'
    pass


@frr_no_debug_ospf6_lsa_all.command('./	<cr>')
def frr_no_debug_ospf6_lsa_all_cr():
    pass


@frr_no_debug_ospf6_lsa.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['router', 'network', 'inter-prefix', 'inter-router', 'as-external', 'nssa', 'link', 'intra-prefix', 'unknown']), invoke_without_command=True)
def frr_no_debug_ospf6_lsa_lsatypes():
    """Display Router LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_lsa_lsatypes.name
    data_gen['LSA_TYPES'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf6_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_lsa table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_lsa'
    pass


@frr_no_debug_ospf6_lsa_lsatypes.command('./	<cr>')
def frr_no_debug_ospf6_lsa_lsatypes_cr():
    pass


@frr_no_debug_ospf6_lsa_lsatypes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['originate', 'examine', 'flooding']), invoke_without_command=True)
def frr_no_debug_ospf6_lsa_lsatypes_lsaactions():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_lsa_lsatypes_lsaactions.name
    data_gen['LSA_ACTIONS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf6_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_lsa'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_lsa table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_lsa'
    pass


@frr_no_debug_ospf6_lsa_lsatypes_lsaactions.command('./	<cr>')
def frr_no_debug_ospf6_lsa_lsatypes_lsaactions_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='message',)
def frr_no_debug_ospf6_message(message_='message'):
    """Debug OSPFv3 message"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_message.name
    data_gen['message'] = message_='message'
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_message.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['unknown', 'hello', 'dbdesc', 'lsreq', 'lsupdate', 'lsack', 'all']), invoke_without_command=True)
def frr_no_debug_ospf6_message_messageospfdebugpackettype():
    """Debug Unknown message"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_message_messageospfdebugpackettype.name
    data_gen['MESSAGE_OSPF_DEBUG_PACKET_TYPE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_message_messageospfdebugpackettype.command('./	<cr>')
def frr_no_debug_ospf6_message_messageospfdebugpackettype_cr():
    pass


@frr_no_debug_ospf6_message_messageospfdebugpackettype.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['send', 'recv', 'send-hdr', 'recv-hdr']), invoke_without_command=True)
def frr_no_debug_ospf6_message_messageospfdebugpackettype_debugpacketdirection():
    """Debug only sending message, entire pkt"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_message_messageospfdebugpackettype_debugpacketdirection.name
    data_gen['DEBUG_PACKET_DIRECTION'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_message_messageospfdebugpackettype_debugpacketdirection.command('./	<cr>')
def frr_no_debug_ospf6_message_messageospfdebugpackettype_debugpacketdirection_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
def frr_no_debug_ospf6_neighbor(no_debug_ospf6_neighbor_='no_debug_ospf6_neighbor'):
    """Debug OSPFv3 Neighbor"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_neighbor.name
    
    if 'VIEW_NODE|no_debug_ospf6_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_neighbor'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_neighbor'
    pass


@frr_no_debug_ospf6_neighbor.command('./	<cr>')
def frr_no_debug_ospf6_neighbor_cr():
    pass


@frr_no_debug_ospf6_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['state', 'event']), invoke_without_command=True)
def frr_no_debug_ospf6_neighbor_choicecase():
    """Debug OSPFv3 Neighbor State Change"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_neighbor_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf6_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_neighbor'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_neighbor'
    pass


@frr_no_debug_ospf6_neighbor_choicecase.command('./	<cr>')
def frr_no_debug_ospf6_neighbor_choicecase_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='nssa', invoke_without_command=True)
def frr_no_debug_ospf6_nssa(nssa_='nssa'):
    """Debug OSPFv3 NSSA function"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_nssa.name
    data_gen['nssa'] = nssa_='nssa'
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_nssa.command('./	<cr>')
def frr_no_debug_ospf6_nssa_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='route',)
def frr_no_debug_ospf6_route(route_='route'):
    """Debug routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_route.name
    data_gen['route'] = route_='route'
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['all', 'table', 'intra-area', 'inter-area', 'memory']), invoke_without_command=True)
def frr_no_debug_ospf6_route_routechoicecase():
    """Debug for all types of route calculation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_route_routechoicecase.name
    data_gen['ROUTE_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6'
    pass


@frr_no_debug_ospf6_route_routechoicecase.command('./	<cr>')
def frr_no_debug_ospf6_route_routechoicecase_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='spf',)
def frr_no_debug_ospf6_spf(no_debug_ospf6_spf_='no_debug_ospf6_spf'):
    """Quit Debugging SPF Calculation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_spf.name
    
    if 'VIEW_NODE|no_debug_ospf6_spf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_spf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_spf'
    pass


@frr_no_debug_ospf6_spf.group(cls=FRR_AbbreviationGroup, name='database', invoke_without_command=True)
def frr_no_debug_ospf6_spf_database(database_='database'):
    """Quit Logging number of LSAs at SPF Calculation time"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_spf_database.name
    data_gen['database'] = database_='database'
    
    if 'VIEW_NODE|no_debug_ospf6_spf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_spf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_spf'
    pass


@frr_no_debug_ospf6_spf_database.command('./	<cr>')
def frr_no_debug_ospf6_spf_database_cr():
    pass


@frr_no_debug_ospf6_spf.group(cls=FRR_AbbreviationGroup, name='process', invoke_without_command=True)
def frr_no_debug_ospf6_spf_process(process_='process'):
    """Quit Debugging Detailed SPF Process"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_spf_process.name
    data_gen['process'] = process_='process'
    
    if 'VIEW_NODE|no_debug_ospf6_spf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_spf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_spf'
    pass


@frr_no_debug_ospf6_spf_process.command('./	<cr>')
def frr_no_debug_ospf6_spf_process_cr():
    pass


@frr_no_debug_ospf6_spf.group(cls=FRR_AbbreviationGroup, name='time', invoke_without_command=True)
def frr_no_debug_ospf6_spf_time(time_='time'):
    """Quit Measuring time taken by SPF Calculation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_spf_time.name
    data_gen['time'] = time_='time'
    
    if 'VIEW_NODE|no_debug_ospf6_spf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_spf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_spf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_spf'
    pass


@frr_no_debug_ospf6_spf_time.command('./	<cr>')
def frr_no_debug_ospf6_spf_time_cr():
    pass


@frr_no_debug_ospf6.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_ospf6_zebra(no_debug_ospf6_zebra_='no_debug_ospf6_zebra'):
    """Debug connection between zebra"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_zebra.name
    
    if 'VIEW_NODE|no_debug_ospf6_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_zebra'
    pass


@frr_no_debug_ospf6_zebra.command('./	<cr>')
def frr_no_debug_ospf6_zebra_cr():
    pass


@frr_no_debug_ospf6_zebra.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['send', 'recv']), invoke_without_command=True)
def frr_no_debug_ospf6_zebra_choicecase():
    """Debug Sending zebra"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf6_zebra_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf6_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf6_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf6_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf6_zebra'
    pass


@frr_no_debug_ospf6_zebra_choicecase.command('./	<cr>')
def frr_no_debug_ospf6_zebra_choicecase_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='bfd', invoke_without_command=True)
def frr_no_debug_ospf_bfd(bfd_='bfd'):
    """Bidirection Forwarding Detection"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_bfd.name
    data_gen['bfd'] = bfd_='bfd'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_bfd.command('./	<cr>')
def frr_no_debug_ospf_bfd_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='client-api', invoke_without_command=True)
def frr_no_debug_ospf_clientapi(clientapi_='client-api'):
    """OSPF client API information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_clientapi.name
    data_gen['client-api'] = clientapi_='client-api'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_clientapi.command('./	<cr>')
def frr_no_debug_ospf_clientapi_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='default-information', invoke_without_command=True)
def frr_no_debug_ospf_defaultinformation(defaultinformation_='default-information'):
    """OSPF default information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_defaultinformation.name
    data_gen['default-information'] = defaultinformation_='default-information'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_defaultinformation.command('./	<cr>')
def frr_no_debug_ospf_defaultinformation_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='event', invoke_without_command=True)
def frr_no_debug_ospf_event(event_='event'):
    """OSPF event information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_event.name
    data_gen['event'] = event_='event'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_event.command('./	<cr>')
def frr_no_debug_ospf_event_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='graceful-restart', invoke_without_command=True)
def frr_no_debug_ospf_gracefulrestart(gracefulrestart_='graceful-restart'):
    """OSPF Graceful Restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_gracefulrestart.name
    data_gen['graceful-restart'] = gracefulrestart_='graceful-restart'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_gracefulrestart.command('./	<cr>')
def frr_no_debug_ospf_gracefulrestart_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, [(1, 65535)]),)
def frr_no_debug_ospf_instanceid():
    """3"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid.name
    data_gen['INSTANCE_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='bfd', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_bfd(bfd_='bfd'):
    """Bidirection Forwarding Detection"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_bfd.name
    data_gen['bfd'] = bfd_='bfd'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_bfd.command('./	<cr>')
def frr_no_debug_ospf_instanceid_bfd_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='client-api', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_clientapi(clientapi_='client-api'):
    """OSPF client API information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_clientapi.name
    data_gen['client-api'] = clientapi_='client-api'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_clientapi.command('./	<cr>')
def frr_no_debug_ospf_instanceid_clientapi_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='default-information', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_defaultinformation(defaultinformation_='default-information'):
    """OSPF default information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_defaultinformation.name
    data_gen['default-information'] = defaultinformation_='default-information'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_defaultinformation.command('./	<cr>')
def frr_no_debug_ospf_instanceid_defaultinformation_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='event', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_event(event_='event'):
    """OSPF event information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_event.name
    data_gen['event'] = event_='event'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_event.command('./	<cr>')
def frr_no_debug_ospf_instanceid_event_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='graceful-restart', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_gracefulrestart(gracefulrestart_='graceful-restart'):
    """OSPF Graceful Restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_gracefulrestart.name
    data_gen['graceful-restart'] = gracefulrestart_='graceful-restart'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_gracefulrestart.command('./	<cr>')
def frr_no_debug_ospf_instanceid_gracefulrestart_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='ism', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_ism(ism_='ism'):
    """OSPF Interface State Machine"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_ism.name
    data_gen['ism'] = ism_='ism'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_ism.command('./	<cr>')
def frr_no_debug_ospf_instanceid_ism_cr():
    pass


@frr_no_debug_ospf_instanceid_ism.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['status', 'events', 'timers']), invoke_without_command=True)
def frr_no_debug_ospf_instanceid_ism_nsmstatuseventtimer():
    """ISM Status Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_ism_nsmstatuseventtimer.name
    data_gen['NSM_STATUS_EVENT_TIMER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_ism_nsmstatuseventtimer.command('./	<cr>')
def frr_no_debug_ospf_instanceid_ism_nsmstatuseventtimer_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='ldp-sync', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_ldpsync(ldpsync_='ldp-sync'):
    """OSPF LDP-Sync information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_ldpsync.name
    data_gen['ldp-sync'] = ldpsync_='ldp-sync'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_ldpsync.command('./	<cr>')
def frr_no_debug_ospf_instanceid_ldpsync_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='lsa', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_lsa(lsa_='lsa'):
    """OSPF Link State Advertisement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_lsa.name
    data_gen['lsa'] = lsa_='lsa'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_lsa.command('./	<cr>')
def frr_no_debug_ospf_instanceid_lsa_cr():
    pass


@frr_no_debug_ospf_instanceid_lsa.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['generate', 'flooding', 'install', 'refresh', 'aggregate']), invoke_without_command=True)
def frr_no_debug_ospf_instanceid_lsa_lsaoperationtype():
    """LSA Generation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_lsa_lsaoperationtype.name
    data_gen['LSA_OPERATION_TYPE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_lsa_lsaoperationtype.command('./	<cr>')
def frr_no_debug_ospf_instanceid_lsa_lsaoperationtype_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='nsm', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_nsm(nsm_='nsm'):
    """OSPF Neighbor State Machine"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_nsm.name
    data_gen['nsm'] = nsm_='nsm'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_nsm.command('./	<cr>')
def frr_no_debug_ospf_instanceid_nsm_cr():
    pass


@frr_no_debug_ospf_instanceid_nsm.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['status', 'events', 'timers']), invoke_without_command=True)
def frr_no_debug_ospf_instanceid_nsm_nsmstatuseventtimer():
    """NSM Status Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_nsm_nsmstatuseventtimer.name
    data_gen['NSM_STATUS_EVENT_TIMER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_nsm_nsmstatuseventtimer.command('./	<cr>')
def frr_no_debug_ospf_instanceid_nsm_nsmstatuseventtimer_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='nssa', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_nssa(nssa_='nssa'):
    """OSPF nssa information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_nssa.name
    data_gen['nssa'] = nssa_='nssa'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_nssa.command('./	<cr>')
def frr_no_debug_ospf_instanceid_nssa_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='packet',)
def frr_no_debug_ospf_instanceid_packet(packet_='packet'):
    """OSPF packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_packet.name
    data_gen['packet'] = packet_='packet'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_packet.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['hello', 'dd', 'ls-request', 'ls-update', 'ls-ack', 'all']), invoke_without_command=True)
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype():
    """OSPF Hello"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_packet_packetospfpackettype.name
    data_gen['PACKET_OSPF_PACKET_TYPE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype.command('./	<cr>')
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_cr():
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_detail(detail_='detail'):
    """Detail Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_packet_packetospfpackettype_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype_detail.command('./	<cr>')
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_detail_cr():
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype.group(cls=FRR_AbbreviationGroup, name='recv', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_recv(recv_='recv'):
    """Packet received"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_packet_packetospfpackettype_recv.name
    data_gen['recv'] = recv_='recv'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype_recv.command('./	<cr>')
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_recv_cr():
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype_recv.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_recv_detail(recv_detail_='recv_detail'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_packet_packetospfpackettype_recv_detail.name
    data_gen['recv_detail'] = recv_detail_='recv_detail'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype_recv_detail.command('./	<cr>')
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_recv_detail_cr():
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype.group(cls=FRR_AbbreviationGroup, name='send', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_send(send_='send'):
    """Packet sent"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_packet_packetospfpackettype_send.name
    data_gen['send'] = send_='send'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype_send.command('./	<cr>')
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_send_cr():
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype_send.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_send_detail(send_detail_='send_detail'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_packet_packetospfpackettype_send_detail.name
    data_gen['send_detail'] = send_detail_='send_detail'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_packet_packetospfpackettype_send_detail.command('./	<cr>')
def frr_no_debug_ospf_instanceid_packet_packetospfpackettype_send_detail_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='sr', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_sr(sr_='sr'):
    """OSPF-SR information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_sr.name
    data_gen['sr'] = sr_='sr'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_sr.command('./	<cr>')
def frr_no_debug_ospf_instanceid_sr_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='te', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_te(te_='te'):
    """OSPF-TE information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_te.name
    data_gen['te'] = te_='te'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_te.command('./	<cr>')
def frr_no_debug_ospf_instanceid_te_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='ti-lfa', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_tilfa(tilfa_='ti-lfa'):
    """OSPF-SR TI-LFA information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_tilfa.name
    data_gen['ti-lfa'] = tilfa_='ti-lfa'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_tilfa.command('./	<cr>')
def frr_no_debug_ospf_instanceid_tilfa_cr():
    pass


@frr_no_debug_ospf_instanceid.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_ospf_instanceid_zebra(zebra_='zebra'):
    """Zebra information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_zebra.command('./	<cr>')
def frr_no_debug_ospf_instanceid_zebra_cr():
    pass


@frr_no_debug_ospf_instanceid_zebra.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['interface', 'redistribute']), invoke_without_command=True)
def frr_no_debug_ospf_instanceid_zebra_zebrainterfaceredistribute():
    """Zebra interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_instanceid_zebra_zebrainterfaceredistribute.name
    data_gen['ZEBRA_INTERFACE_REDISTRIBUTE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_instanceid_zebra_zebrainterfaceredistribute.command('./	<cr>')
def frr_no_debug_ospf_instanceid_zebra_zebrainterfaceredistribute_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='ism', invoke_without_command=True)
def frr_no_debug_ospf_ism(no_debug_ospf_ism_='no_debug_ospf_ism'):
    """OSPF Interface State Machine"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_ism.name
    
    if 'VIEW_NODE|no_debug_ospf_ism' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_ism'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_ism']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_ism'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf_ism table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf_ism'
    pass


@frr_no_debug_ospf_ism.command('./	<cr>')
def frr_no_debug_ospf_ism_cr():
    pass


@frr_no_debug_ospf_ism.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['status', 'events', 'timers']), invoke_without_command=True)
def frr_no_debug_ospf_ism_nsmstatuseventtimer():
    """ISM Status Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_ism_nsmstatuseventtimer.name
    data_gen['NSM_STATUS_EVENT_TIMER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf_ism' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_ism'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_ism']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_ism'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf_ism table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf_ism'
    pass


@frr_no_debug_ospf_ism_nsmstatuseventtimer.command('./	<cr>')
def frr_no_debug_ospf_ism_nsmstatuseventtimer_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='ldp-sync', invoke_without_command=True)
def frr_no_debug_ospf_ldpsync(ldpsync_='ldp-sync'):
    """OSPF LDP-Sync information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_ldpsync.name
    data_gen['ldp-sync'] = ldpsync_='ldp-sync'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_ldpsync.command('./	<cr>')
def frr_no_debug_ospf_ldpsync_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='lsa', invoke_without_command=True)
def frr_no_debug_ospf_lsa(no_debug_ospf_lsa_='no_debug_ospf_lsa'):
    """OSPF Link State Advertisement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_lsa.name
    
    if 'VIEW_NODE|no_debug_ospf_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_lsa'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf_lsa table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf_lsa'
    pass


@frr_no_debug_ospf_lsa.command('./	<cr>')
def frr_no_debug_ospf_lsa_cr():
    pass


@frr_no_debug_ospf_lsa.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['generate', 'flooding', 'install', 'refresh', 'aggregate']), invoke_without_command=True)
def frr_no_debug_ospf_lsa_lsaoperationtype():
    """LSA Generation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_lsa_lsaoperationtype.name
    data_gen['LSA_OPERATION_TYPE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_lsa'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf_lsa table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf_lsa'
    pass


@frr_no_debug_ospf_lsa_lsaoperationtype.command('./	<cr>')
def frr_no_debug_ospf_lsa_lsaoperationtype_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='nsm', invoke_without_command=True)
def frr_no_debug_ospf_nsm(no_debug_ospf_nsm_='no_debug_ospf_nsm'):
    """OSPF Neighbor State Machine"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_nsm.name
    
    if 'VIEW_NODE|no_debug_ospf_nsm' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_nsm'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_nsm']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_nsm'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf_nsm table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf_nsm'
    pass


@frr_no_debug_ospf_nsm.command('./	<cr>')
def frr_no_debug_ospf_nsm_cr():
    pass


@frr_no_debug_ospf_nsm.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['status', 'events', 'timers']), invoke_without_command=True)
def frr_no_debug_ospf_nsm_nsmstatuseventtimer():
    """NSM Status Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_nsm_nsmstatuseventtimer.name
    data_gen['NSM_STATUS_EVENT_TIMER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf_nsm' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_nsm'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_nsm']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_nsm'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf_nsm table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf_nsm'
    pass


@frr_no_debug_ospf_nsm_nsmstatuseventtimer.command('./	<cr>')
def frr_no_debug_ospf_nsm_nsmstatuseventtimer_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='nssa', invoke_without_command=True)
def frr_no_debug_ospf_nssa(nssa_='nssa'):
    """OSPF nssa information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_nssa.name
    data_gen['nssa'] = nssa_='nssa'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_nssa.command('./	<cr>')
def frr_no_debug_ospf_nssa_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='packet',)
def frr_no_debug_ospf_packet(packet_='packet'):
    """OSPF packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_packet.name
    data_gen['packet'] = packet_='packet'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_packet.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['hello', 'dd', 'ls-request', 'ls-update', 'ls-ack', 'all']), invoke_without_command=True)
def frr_no_debug_ospf_packet_packetospfpackettype():
    """OSPF Hello"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_packet_packetospfpackettype.name
    data_gen['PACKET_OSPF_PACKET_TYPE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_packet_packetospfpackettype.command('./	<cr>')
def frr_no_debug_ospf_packet_packetospfpackettype_cr():
    pass


@frr_no_debug_ospf_packet_packetospfpackettype.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_ospf_packet_packetospfpackettype_detail(detail_='detail'):
    """Detail Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_packet_packetospfpackettype_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_packet_packetospfpackettype_detail.command('./	<cr>')
def frr_no_debug_ospf_packet_packetospfpackettype_detail_cr():
    pass


@frr_no_debug_ospf_packet_packetospfpackettype.group(cls=FRR_AbbreviationGroup, name='recv', invoke_without_command=True)
def frr_no_debug_ospf_packet_packetospfpackettype_recv(recv_='recv'):
    """Packet received"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_packet_packetospfpackettype_recv.name
    data_gen['recv'] = recv_='recv'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_packet_packetospfpackettype_recv.command('./	<cr>')
def frr_no_debug_ospf_packet_packetospfpackettype_recv_cr():
    pass


@frr_no_debug_ospf_packet_packetospfpackettype_recv.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_ospf_packet_packetospfpackettype_recv_detail(recv_detail_='recv_detail'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_packet_packetospfpackettype_recv_detail.name
    data_gen['recv_detail'] = recv_detail_='recv_detail'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_packet_packetospfpackettype_recv_detail.command('./	<cr>')
def frr_no_debug_ospf_packet_packetospfpackettype_recv_detail_cr():
    pass


@frr_no_debug_ospf_packet_packetospfpackettype.group(cls=FRR_AbbreviationGroup, name='send', invoke_without_command=True)
def frr_no_debug_ospf_packet_packetospfpackettype_send(send_='send'):
    """Packet sent"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_packet_packetospfpackettype_send.name
    data_gen['send'] = send_='send'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_packet_packetospfpackettype_send.command('./	<cr>')
def frr_no_debug_ospf_packet_packetospfpackettype_send_cr():
    pass


@frr_no_debug_ospf_packet_packetospfpackettype_send.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_ospf_packet_packetospfpackettype_send_detail(send_detail_='send_detail'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_packet_packetospfpackettype_send_detail.name
    data_gen['send_detail'] = send_detail_='send_detail'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_packet_packetospfpackettype_send_detail.command('./	<cr>')
def frr_no_debug_ospf_packet_packetospfpackettype_send_detail_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='sr', invoke_without_command=True)
def frr_no_debug_ospf_sr(sr_='sr'):
    """OSPF-SR information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_sr.name
    data_gen['sr'] = sr_='sr'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_sr.command('./	<cr>')
def frr_no_debug_ospf_sr_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='te', invoke_without_command=True)
def frr_no_debug_ospf_te(te_='te'):
    """OSPF-TE information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_te.name
    data_gen['te'] = te_='te'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_te.command('./	<cr>')
def frr_no_debug_ospf_te_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='ti-lfa', invoke_without_command=True)
def frr_no_debug_ospf_tilfa(tilfa_='ti-lfa'):
    """OSPF-SR TI-LFA information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_tilfa.name
    data_gen['ti-lfa'] = tilfa_='ti-lfa'
    
    if 'VIEW_NODE|no_debug_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf'
    pass


@frr_no_debug_ospf_tilfa.command('./	<cr>')
def frr_no_debug_ospf_tilfa_cr():
    pass


@frr_no_debug_ospf.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_ospf_zebra(no_debug_ospf_zebra_='no_debug_ospf_zebra'):
    """Zebra information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_zebra.name
    
    if 'VIEW_NODE|no_debug_ospf_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf_zebra'
    pass


@frr_no_debug_ospf_zebra.command('./	<cr>')
def frr_no_debug_ospf_zebra_cr():
    pass


@frr_no_debug_ospf_zebra.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['interface', 'redistribute']), invoke_without_command=True)
def frr_no_debug_ospf_zebra_zebrainterfaceredistribute():
    """Zebra interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ospf_zebra_zebrainterfaceredistribute.name
    data_gen['ZEBRA_INTERFACE_REDISTRIBUTE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ospf_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ospf_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_ospf_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ospf_zebra'
    pass


@frr_no_debug_ospf_zebra_zebrainterfaceredistribute.command('./	<cr>')
def frr_no_debug_ospf_zebra_zebrainterfaceredistribute_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='pathd',)
def frr_no_debug_pathd(no_debug_pathd_='no_debug_pathd'):
    """path debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd.name
    
    if 'VIEW_NODE|no_debug_pathd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd'
    pass


@frr_no_debug_pathd.group(cls=FRR_AbbreviationGroup, name='mpls-te', invoke_without_command=True)
def frr_no_debug_pathd_mplste(mplste_='mpls-te'):
    """ted debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_mplste.name
    data_gen['mpls-te'] = mplste_='mpls-te'
    
    if 'VIEW_NODE|no_debug_pathd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd'
    pass


@frr_no_debug_pathd_mplste.command('./	<cr>')
def frr_no_debug_pathd_mplste_cr():
    pass


@frr_no_debug_pathd.group(cls=FRR_AbbreviationGroup, name='pcep', invoke_without_command=True)
def frr_no_debug_pathd_pcep(no_debug_pathd_pcep_='no_debug_pathd_pcep'):
    """pcep module debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep.name
    
    if 'VIEW_NODE|no_debug_pathd_pcep' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep'
    pass


@frr_no_debug_pathd_pcep.command('./	<cr>')
def frr_no_debug_pathd_pcep_cr():
    pass


@frr_no_debug_pathd_pcep.group(cls=FRR_AbbreviationGroup, name='basic', invoke_without_command=True)
def frr_no_debug_pathd_pcep_basic(no_debug_pathd_pcep_basic_='no_debug_pathd_pcep_basic'):
    """module basic debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_basic.name
    
    if 'VIEW_NODE|no_debug_pathd_pcep_basic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_basic table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_basic'
    pass


@frr_no_debug_pathd_pcep_basic.command('./	<cr>')
def frr_no_debug_pathd_pcep_basic_cr():
    pass


@frr_no_debug_pathd_pcep_basic.group(cls=FRR_AbbreviationGroup, name='message', invoke_without_command=True)
def frr_no_debug_pathd_pcep_basic_message(no_debug_pathd_pcep_basic_message_='no_debug_pathd_pcep_basic_message'):
    """pcep message debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_basic_message.name
    
    if 'VIEW_NODE|no_debug_pathd_pcep_basic_message' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_message'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_message']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_message'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_basic_message table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_basic_message'
    pass


@frr_no_debug_pathd_pcep_basic_message.command('./	<cr>')
def frr_no_debug_pathd_pcep_basic_message_cr():
    pass


@frr_no_debug_pathd_pcep_basic_message.group(cls=FRR_AbbreviationGroup, name='pceplib', invoke_without_command=True)
def frr_no_debug_pathd_pcep_basic_message_pceplib(pceplib_='pceplib'):
    """pceplib debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_basic_message_pceplib.name
    data_gen['pceplib'] = pceplib_='pceplib'
    
    if 'VIEW_NODE|no_debug_pathd_pcep_basic_message' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_message'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_message']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_message'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_basic_message table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_basic_message'
    pass


@frr_no_debug_pathd_pcep_basic_message_pceplib.command('./	<cr>')
def frr_no_debug_pathd_pcep_basic_message_pceplib_cr():
    pass


@frr_no_debug_pathd_pcep_basic.group(cls=FRR_AbbreviationGroup, name='path', invoke_without_command=True)
def frr_no_debug_pathd_pcep_basic_path(no_debug_pathd_pcep_basic_path_='no_debug_pathd_pcep_basic_path'):
    """path structures debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_basic_path.name
    
    if 'VIEW_NODE|no_debug_pathd_pcep_basic_path' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_basic_path table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_basic_path'
    pass


@frr_no_debug_pathd_pcep_basic_path.command('./	<cr>')
def frr_no_debug_pathd_pcep_basic_path_cr():
    pass


@frr_no_debug_pathd_pcep_basic_path.group(cls=FRR_AbbreviationGroup, name='message', invoke_without_command=True)
def frr_no_debug_pathd_pcep_basic_path_message(no_debug_pathd_pcep_basic_path_message_='no_debug_pathd_pcep_basic_path_message'):
    """pcep message debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_basic_path_message.name
    
    if 'VIEW_NODE|no_debug_pathd_pcep_basic_path_message' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path_message'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path_message']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path_message'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_basic_path_message table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_basic_path_message'
    pass


@frr_no_debug_pathd_pcep_basic_path_message.command('./	<cr>')
def frr_no_debug_pathd_pcep_basic_path_message_cr():
    pass


@frr_no_debug_pathd_pcep_basic_path_message.group(cls=FRR_AbbreviationGroup, name='pceplib', invoke_without_command=True)
def frr_no_debug_pathd_pcep_basic_path_message_pceplib(pceplib_='pceplib'):
    """pceplib debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_basic_path_message_pceplib.name
    data_gen['pceplib'] = pceplib_='pceplib'
    
    if 'VIEW_NODE|no_debug_pathd_pcep_basic_path_message' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path_message'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path_message']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path_message'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_basic_path_message table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_basic_path_message'
    pass


@frr_no_debug_pathd_pcep_basic_path_message_pceplib.command('./	<cr>')
def frr_no_debug_pathd_pcep_basic_path_message_pceplib_cr():
    pass


@frr_no_debug_pathd_pcep_basic_path.group(cls=FRR_AbbreviationGroup, name='pceplib', invoke_without_command=True)
def frr_no_debug_pathd_pcep_basic_path_pceplib(pceplib_='pceplib'):
    """pceplib debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_basic_path_pceplib.name
    data_gen['pceplib'] = pceplib_='pceplib'
    
    if 'VIEW_NODE|no_debug_pathd_pcep_basic_path' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic_path'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_basic_path table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_basic_path'
    pass


@frr_no_debug_pathd_pcep_basic_path_pceplib.command('./	<cr>')
def frr_no_debug_pathd_pcep_basic_path_pceplib_cr():
    pass


@frr_no_debug_pathd_pcep_basic.group(cls=FRR_AbbreviationGroup, name='pceplib', invoke_without_command=True)
def frr_no_debug_pathd_pcep_basic_pceplib(pceplib_='pceplib'):
    """pceplib debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_basic_pceplib.name
    data_gen['pceplib'] = pceplib_='pceplib'
    
    if 'VIEW_NODE|no_debug_pathd_pcep_basic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_basic'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_basic table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_basic'
    pass


@frr_no_debug_pathd_pcep_basic_pceplib.command('./	<cr>')
def frr_no_debug_pathd_pcep_basic_pceplib_cr():
    pass


@frr_no_debug_pathd_pcep.group(cls=FRR_AbbreviationGroup, name='message', invoke_without_command=True)
def frr_no_debug_pathd_pcep_message(no_debug_pathd_pcep_message_='no_debug_pathd_pcep_message'):
    """pcep message debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_message.name
    
    if 'VIEW_NODE|no_debug_pathd_pcep_message' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_message'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_message']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_message'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_message table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_message'
    pass


@frr_no_debug_pathd_pcep_message.command('./	<cr>')
def frr_no_debug_pathd_pcep_message_cr():
    pass


@frr_no_debug_pathd_pcep_message.group(cls=FRR_AbbreviationGroup, name='pceplib', invoke_without_command=True)
def frr_no_debug_pathd_pcep_message_pceplib(pceplib_='pceplib'):
    """pceplib debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_message_pceplib.name
    data_gen['pceplib'] = pceplib_='pceplib'
    
    if 'VIEW_NODE|no_debug_pathd_pcep_message' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_message'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_message']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_message'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_message table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_message'
    pass


@frr_no_debug_pathd_pcep_message_pceplib.command('./	<cr>')
def frr_no_debug_pathd_pcep_message_pceplib_cr():
    pass


@frr_no_debug_pathd_pcep.group(cls=FRR_AbbreviationGroup, name='path', invoke_without_command=True)
def frr_no_debug_pathd_pcep_path(no_debug_pathd_pcep_path_='no_debug_pathd_pcep_path'):
    """path structures debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_path.name
    
    if 'VIEW_NODE|no_debug_pathd_pcep_path' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_path table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_path'
    pass


@frr_no_debug_pathd_pcep_path.command('./	<cr>')
def frr_no_debug_pathd_pcep_path_cr():
    pass


@frr_no_debug_pathd_pcep_path.group(cls=FRR_AbbreviationGroup, name='message', invoke_without_command=True)
def frr_no_debug_pathd_pcep_path_message(no_debug_pathd_pcep_path_message_='no_debug_pathd_pcep_path_message'):
    """pcep message debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_path_message.name
    
    if 'VIEW_NODE|no_debug_pathd_pcep_path_message' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path_message'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path_message']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path_message'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_path_message table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_path_message'
    pass


@frr_no_debug_pathd_pcep_path_message.command('./	<cr>')
def frr_no_debug_pathd_pcep_path_message_cr():
    pass


@frr_no_debug_pathd_pcep_path_message.group(cls=FRR_AbbreviationGroup, name='pceplib', invoke_without_command=True)
def frr_no_debug_pathd_pcep_path_message_pceplib(pceplib_='pceplib'):
    """pceplib debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_path_message_pceplib.name
    data_gen['pceplib'] = pceplib_='pceplib'
    
    if 'VIEW_NODE|no_debug_pathd_pcep_path_message' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path_message'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path_message']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path_message'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_path_message table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_path_message'
    pass


@frr_no_debug_pathd_pcep_path_message_pceplib.command('./	<cr>')
def frr_no_debug_pathd_pcep_path_message_pceplib_cr():
    pass


@frr_no_debug_pathd_pcep_path.group(cls=FRR_AbbreviationGroup, name='pceplib', invoke_without_command=True)
def frr_no_debug_pathd_pcep_path_pceplib(pceplib_='pceplib'):
    """pceplib debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_path_pceplib.name
    data_gen['pceplib'] = pceplib_='pceplib'
    
    if 'VIEW_NODE|no_debug_pathd_pcep_path' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep_path'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep_path table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep_path'
    pass


@frr_no_debug_pathd_pcep_path_pceplib.command('./	<cr>')
def frr_no_debug_pathd_pcep_path_pceplib_cr():
    pass


@frr_no_debug_pathd_pcep.group(cls=FRR_AbbreviationGroup, name='pceplib', invoke_without_command=True)
def frr_no_debug_pathd_pcep_pceplib(pceplib_='pceplib'):
    """pceplib debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_pcep_pceplib.name
    data_gen['pceplib'] = pceplib_='pceplib'
    
    if 'VIEW_NODE|no_debug_pathd_pcep' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd_pcep'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd_pcep table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd_pcep'
    pass


@frr_no_debug_pathd_pcep_pceplib.command('./	<cr>')
def frr_no_debug_pathd_pcep_pceplib_cr():
    pass


@frr_no_debug_pathd.group(cls=FRR_AbbreviationGroup, name='policy', invoke_without_command=True)
def frr_no_debug_pathd_policy(policy_='policy'):
    """policy debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pathd_policy.name
    data_gen['policy'] = policy_='policy'
    
    if 'VIEW_NODE|no_debug_pathd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pathd'][key] = val
    
    # set VIEW_NODE -> no_debug_pathd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pathd'
    pass


@frr_no_debug_pathd_policy.command('./	<cr>')
def frr_no_debug_pathd_policy_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='pbr', invoke_without_command=True)
def frr_no_debug_pbr(no_debug_pbr_='no_debug_pbr'):
    """Policy Based Routing"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pbr.name
    
    if 'VIEW_NODE|no_debug_pbr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr'][key] = val
    
    # set VIEW_NODE -> no_debug_pbr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pbr'
    pass


@frr_no_debug_pbr.command('./	<cr>')
def frr_no_debug_pbr_cr():
    pass


@frr_no_debug_pbr.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_pbr_events(events_='events'):
    """Events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pbr_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_pbr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr'][key] = val
    
    # set VIEW_NODE -> no_debug_pbr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pbr'
    pass


@frr_no_debug_pbr_events.command('./	<cr>')
def frr_no_debug_pbr_events_cr():
    pass


@frr_no_debug_pbr.group(cls=FRR_AbbreviationGroup, name='map', invoke_without_command=True)
def frr_no_debug_pbr_map(map_='map'):
    """Policy maps"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pbr_map.name
    data_gen['map'] = map_='map'
    
    if 'VIEW_NODE|no_debug_pbr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr'][key] = val
    
    # set VIEW_NODE -> no_debug_pbr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pbr'
    pass


@frr_no_debug_pbr_map.command('./	<cr>')
def frr_no_debug_pbr_map_cr():
    pass


@frr_no_debug_pbr.group(cls=FRR_AbbreviationGroup, name='nht', invoke_without_command=True)
def frr_no_debug_pbr_nht(nht_='nht'):
    """Nexthop tracking"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pbr_nht.name
    data_gen['nht'] = nht_='nht'
    
    if 'VIEW_NODE|no_debug_pbr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr'][key] = val
    
    # set VIEW_NODE -> no_debug_pbr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pbr'
    pass


@frr_no_debug_pbr_nht.command('./	<cr>')
def frr_no_debug_pbr_nht_cr():
    pass


@frr_no_debug_pbr.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_pbr_zebra(zebra_='zebra'):
    """PBRD <-> Zebra communications"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pbr_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'VIEW_NODE|no_debug_pbr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pbr'][key] = val
    
    # set VIEW_NODE -> no_debug_pbr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pbr'
    pass


@frr_no_debug_pbr_zebra.command('./	<cr>')
def frr_no_debug_pbr_zebra_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='pim', invoke_without_command=True)
def frr_no_debug_pim(no_debug_pim_='no_debug_pim'):
    """PIM protocol activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim.name
    
    if 'VIEW_NODE|no_debug_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'][key] = val
    
    # set VIEW_NODE -> no_debug_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim'
    pass


@frr_no_debug_pim.command('./	<cr>')
def frr_no_debug_pim_cr():
    pass


@frr_no_debug_pim.group(cls=FRR_AbbreviationGroup, name='bsm', invoke_without_command=True)
def frr_no_debug_pim_bsm(bsm_='bsm'):
    """BSR message processing activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_bsm.name
    data_gen['bsm'] = bsm_='bsm'
    
    if 'VIEW_NODE|no_debug_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'][key] = val
    
    # set VIEW_NODE -> no_debug_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim'
    pass


@frr_no_debug_pim_bsm.command('./	<cr>')
def frr_no_debug_pim_bsm_cr():
    pass


@frr_no_debug_pim.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_pim_events(events_='events'):
    """PIM protocol events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'][key] = val
    
    # set VIEW_NODE -> no_debug_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim'
    pass


@frr_no_debug_pim_events.command('./	<cr>')
def frr_no_debug_pim_events_cr():
    pass


@frr_no_debug_pim.group(cls=FRR_AbbreviationGroup, name='mlag', invoke_without_command=True)
def frr_no_debug_pim_mlag(mlag_='mlag'):
    """PIM Mlag activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_mlag.name
    data_gen['mlag'] = mlag_='mlag'
    
    if 'VIEW_NODE|no_debug_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'][key] = val
    
    # set VIEW_NODE -> no_debug_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim'
    pass


@frr_no_debug_pim_mlag.command('./	<cr>')
def frr_no_debug_pim_mlag_cr():
    pass


@frr_no_debug_pim.group(cls=FRR_AbbreviationGroup, name='nht', invoke_without_command=True)
def frr_no_debug_pim_nht(no_debug_pim_nht_='no_debug_pim_nht'):
    """Nexthop Tracking"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_nht.name
    
    if 'VIEW_NODE|no_debug_pim_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_nht'][key] = val
    
    # set VIEW_NODE -> no_debug_pim_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim_nht'
    pass


@frr_no_debug_pim_nht.command('./	<cr>')
def frr_no_debug_pim_nht_cr():
    pass


@frr_no_debug_pim_nht.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_pim_nht_detail(detail_='detail'):
    """Detailed Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_nht_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_pim_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_nht'][key] = val
    
    # set VIEW_NODE -> no_debug_pim_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim_nht'
    pass


@frr_no_debug_pim_nht_detail.command('./	<cr>')
def frr_no_debug_pim_nht_detail_cr():
    pass


@frr_no_debug_pim_nht.group(cls=FRR_AbbreviationGroup, name='rp', invoke_without_command=True)
def frr_no_debug_pim_nht_rp(rp_='rp'):
    """RP Nexthop Tracking"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_nht_rp.name
    data_gen['rp'] = rp_='rp'
    
    if 'VIEW_NODE|no_debug_pim_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_nht'][key] = val
    
    # set VIEW_NODE -> no_debug_pim_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim_nht'
    pass


@frr_no_debug_pim_nht_rp.command('./	<cr>')
def frr_no_debug_pim_nht_rp_cr():
    pass


@frr_no_debug_pim.group(cls=FRR_AbbreviationGroup, name='packet-dump',)
def frr_no_debug_pim_packetdump(no_debug_pim_packetdump_='no_debug_pim_packet-dump'):
    """PIM packet dump"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_packetdump.name
    
    if 'VIEW_NODE|no_debug_pim_packet-dump' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packet-dump'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packet-dump']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packet-dump'][key] = val
    
    # set VIEW_NODE -> no_debug_pim_packet-dump table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim_packet-dump'
    pass


@frr_no_debug_pim_packetdump.group(cls=FRR_AbbreviationGroup, name='receive', invoke_without_command=True)
def frr_no_debug_pim_packetdump_receive(receive_='receive'):
    """Dump received packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_packetdump_receive.name
    data_gen['receive'] = receive_='receive'
    
    if 'VIEW_NODE|no_debug_pim_packet-dump' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packet-dump'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packet-dump']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packet-dump'][key] = val
    
    # set VIEW_NODE -> no_debug_pim_packet-dump table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim_packet-dump'
    pass


@frr_no_debug_pim_packetdump_receive.command('./	<cr>')
def frr_no_debug_pim_packetdump_receive_cr():
    pass


@frr_no_debug_pim_packetdump.group(cls=FRR_AbbreviationGroup, name='send', invoke_without_command=True)
def frr_no_debug_pim_packetdump_send(send_='send'):
    """Dump sent packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_packetdump_send.name
    data_gen['send'] = send_='send'
    
    if 'VIEW_NODE|no_debug_pim_packet-dump' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packet-dump'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packet-dump']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packet-dump'][key] = val
    
    # set VIEW_NODE -> no_debug_pim_packet-dump table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim_packet-dump'
    pass


@frr_no_debug_pim_packetdump_send.command('./	<cr>')
def frr_no_debug_pim_packetdump_send_cr():
    pass


@frr_no_debug_pim.group(cls=FRR_AbbreviationGroup, name='packets', invoke_without_command=True)
def frr_no_debug_pim_packets(no_debug_pim_packets_='no_debug_pim_packets'):
    """PIM protocol packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_packets.name
    
    if 'VIEW_NODE|no_debug_pim_packets' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packets'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packets']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packets'][key] = val
    
    # set VIEW_NODE -> no_debug_pim_packets table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim_packets'
    pass


@frr_no_debug_pim_packets.command('./	<cr>')
def frr_no_debug_pim_packets_cr():
    pass


@frr_no_debug_pim_packets.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['hello', 'joins', 'register']), invoke_without_command=True)
def frr_no_debug_pim_packets_choicecase():
    """PIM Hello protocol packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_packets_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_pim_packets' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packets'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packets']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_packets'][key] = val
    
    # set VIEW_NODE -> no_debug_pim_packets table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim_packets'
    pass


@frr_no_debug_pim_packets_choicecase.command('./	<cr>')
def frr_no_debug_pim_packets_choicecase_cr():
    pass


@frr_no_debug_pim.group(cls=FRR_AbbreviationGroup, name='static', invoke_without_command=True)
def frr_no_debug_pim_static(static_='static'):
    """PIM Static Multicast Route activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_static.name
    data_gen['static'] = static_='static'
    
    if 'VIEW_NODE|no_debug_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'][key] = val
    
    # set VIEW_NODE -> no_debug_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim'
    pass


@frr_no_debug_pim_static.command('./	<cr>')
def frr_no_debug_pim_static_cr():
    pass


@frr_no_debug_pim.group(cls=FRR_AbbreviationGroup, name='trace', invoke_without_command=True)
def frr_no_debug_pim_trace(no_debug_pim_trace_='no_debug_pim_trace'):
    """PIM internal daemon activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_trace.name
    
    if 'VIEW_NODE|no_debug_pim_trace' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_trace'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_trace']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_trace'][key] = val
    
    # set VIEW_NODE -> no_debug_pim_trace table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim_trace'
    pass


@frr_no_debug_pim_trace.command('./	<cr>')
def frr_no_debug_pim_trace_cr():
    pass


@frr_no_debug_pim_trace.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_pim_trace_detail(detail_='detail'):
    """Detailed Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_trace_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_pim_trace' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_trace'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_trace']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim_trace'][key] = val
    
    # set VIEW_NODE -> no_debug_pim_trace table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim_trace'
    pass


@frr_no_debug_pim_trace_detail.command('./	<cr>')
def frr_no_debug_pim_trace_detail_cr():
    pass


@frr_no_debug_pim.group(cls=FRR_AbbreviationGroup, name='vxlan', invoke_without_command=True)
def frr_no_debug_pim_vxlan(vxlan_='vxlan'):
    """PIM VxLAN events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_vxlan.name
    data_gen['vxlan'] = vxlan_='vxlan'
    
    if 'VIEW_NODE|no_debug_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'][key] = val
    
    # set VIEW_NODE -> no_debug_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim'
    pass


@frr_no_debug_pim_vxlan.command('./	<cr>')
def frr_no_debug_pim_vxlan_cr():
    pass


@frr_no_debug_pim.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_pim_zebra(zebra_='zebra'):
    """ZEBRA protocol activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pim_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'VIEW_NODE|no_debug_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pim'][key] = val
    
    # set VIEW_NODE -> no_debug_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pim'
    pass


@frr_no_debug_pim_zebra.command('./	<cr>')
def frr_no_debug_pim_zebra_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='pimv6', invoke_without_command=True)
def frr_no_debug_pimv6(no_debug_pimv6_='no_debug_pimv6'):
    """PIMv6 protocol activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6.name
    
    if 'VIEW_NODE|no_debug_pimv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6'
    pass


@frr_no_debug_pimv6.command('./	<cr>')
def frr_no_debug_pimv6_cr():
    pass


@frr_no_debug_pimv6.group(cls=FRR_AbbreviationGroup, name='bsm', invoke_without_command=True)
def frr_no_debug_pimv6_bsm(bsm_='bsm'):
    """BSR message processing activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_bsm.name
    data_gen['bsm'] = bsm_='bsm'
    
    if 'VIEW_NODE|no_debug_pimv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6'
    pass


@frr_no_debug_pimv6_bsm.command('./	<cr>')
def frr_no_debug_pimv6_bsm_cr():
    pass


@frr_no_debug_pimv6.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_pimv6_events(events_='events'):
    """PIMv6 protocol events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_pimv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6'
    pass


@frr_no_debug_pimv6_events.command('./	<cr>')
def frr_no_debug_pimv6_events_cr():
    pass


@frr_no_debug_pimv6.group(cls=FRR_AbbreviationGroup, name='nht', invoke_without_command=True)
def frr_no_debug_pimv6_nht(no_debug_pimv6_nht_='no_debug_pimv6_nht'):
    """Nexthop Tracking"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_nht.name
    
    if 'VIEW_NODE|no_debug_pimv6_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_nht'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6_nht'
    pass


@frr_no_debug_pimv6_nht.command('./	<cr>')
def frr_no_debug_pimv6_nht_cr():
    pass


@frr_no_debug_pimv6_nht.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_pimv6_nht_detail(detail_='detail'):
    """Detailed Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_nht_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_pimv6_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_nht'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6_nht'
    pass


@frr_no_debug_pimv6_nht_detail.command('./	<cr>')
def frr_no_debug_pimv6_nht_detail_cr():
    pass


@frr_no_debug_pimv6.group(cls=FRR_AbbreviationGroup, name='packet-dump',)
def frr_no_debug_pimv6_packetdump(no_debug_pimv6_packetdump_='no_debug_pimv6_packet-dump'):
    """PIMv6 packet dump"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_packetdump.name
    
    if 'VIEW_NODE|no_debug_pimv6_packet-dump' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packet-dump'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packet-dump']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packet-dump'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6_packet-dump table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6_packet-dump'
    pass


@frr_no_debug_pimv6_packetdump.group(cls=FRR_AbbreviationGroup, name='receive', invoke_without_command=True)
def frr_no_debug_pimv6_packetdump_receive(receive_='receive'):
    """Dump received packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_packetdump_receive.name
    data_gen['receive'] = receive_='receive'
    
    if 'VIEW_NODE|no_debug_pimv6_packet-dump' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packet-dump'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packet-dump']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packet-dump'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6_packet-dump table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6_packet-dump'
    pass


@frr_no_debug_pimv6_packetdump_receive.command('./	<cr>')
def frr_no_debug_pimv6_packetdump_receive_cr():
    pass


@frr_no_debug_pimv6_packetdump.group(cls=FRR_AbbreviationGroup, name='send', invoke_without_command=True)
def frr_no_debug_pimv6_packetdump_send(send_='send'):
    """Dump sent packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_packetdump_send.name
    data_gen['send'] = send_='send'
    
    if 'VIEW_NODE|no_debug_pimv6_packet-dump' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packet-dump'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packet-dump']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packet-dump'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6_packet-dump table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6_packet-dump'
    pass


@frr_no_debug_pimv6_packetdump_send.command('./	<cr>')
def frr_no_debug_pimv6_packetdump_send_cr():
    pass


@frr_no_debug_pimv6.group(cls=FRR_AbbreviationGroup, name='packets', invoke_without_command=True)
def frr_no_debug_pimv6_packets(no_debug_pimv6_packets_='no_debug_pimv6_packets'):
    """PIMv6 protocol packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_packets.name
    
    if 'VIEW_NODE|no_debug_pimv6_packets' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packets'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packets']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packets'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6_packets table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6_packets'
    pass


@frr_no_debug_pimv6_packets.command('./	<cr>')
def frr_no_debug_pimv6_packets_cr():
    pass


@frr_no_debug_pimv6_packets.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['hello', 'joins', 'register']), invoke_without_command=True)
def frr_no_debug_pimv6_packets_choicecase():
    """PIMv6 Hello protocol packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_packets_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_pimv6_packets' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packets'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packets']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_packets'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6_packets table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6_packets'
    pass


@frr_no_debug_pimv6_packets_choicecase.command('./	<cr>')
def frr_no_debug_pimv6_packets_choicecase_cr():
    pass


@frr_no_debug_pimv6.group(cls=FRR_AbbreviationGroup, name='trace', invoke_without_command=True)
def frr_no_debug_pimv6_trace(no_debug_pimv6_trace_='no_debug_pimv6_trace'):
    """PIMv6 internal daemon activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_trace.name
    
    if 'VIEW_NODE|no_debug_pimv6_trace' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_trace'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_trace']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_trace'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6_trace table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6_trace'
    pass


@frr_no_debug_pimv6_trace.command('./	<cr>')
def frr_no_debug_pimv6_trace_cr():
    pass


@frr_no_debug_pimv6_trace.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_pimv6_trace_detail(detail_='detail'):
    """Detailed Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_trace_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_pimv6_trace' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_trace'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_trace']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6_trace'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6_trace table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6_trace'
    pass


@frr_no_debug_pimv6_trace_detail.command('./	<cr>')
def frr_no_debug_pimv6_trace_detail_cr():
    pass


@frr_no_debug_pimv6.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_pimv6_zebra(zebra_='zebra'):
    """ZEBRA protocol activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_pimv6_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'VIEW_NODE|no_debug_pimv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_pimv6'][key] = val
    
    # set VIEW_NODE -> no_debug_pimv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_pimv6'
    pass


@frr_no_debug_pimv6_zebra.command('./	<cr>')
def frr_no_debug_pimv6_zebra_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='resolver', invoke_without_command=True)
def frr_no_debug_resolver(resolver_='resolver'):
    """Debug DNS resolver actions"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_resolver.name
    data_gen['resolver'] = resolver_='resolver'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_resolver.command('./	<cr>')
def frr_no_debug_resolver_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='rip',)
def frr_no_debug_rip(no_debug_rip_='no_debug_rip'):
    """RIP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_rip.name
    
    if 'VIEW_NODE|no_debug_rip' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_rip'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_rip']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_rip'][key] = val
    
    # set VIEW_NODE -> no_debug_rip table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_rip'
    pass


@frr_no_debug_rip.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_rip_events(events_='events'):
    """RIP events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_rip_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_rip' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_rip'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_rip']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_rip'][key] = val
    
    # set VIEW_NODE -> no_debug_rip table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_rip'
    pass


@frr_no_debug_rip_events.command('./	<cr>')
def frr_no_debug_rip_events_cr():
    pass


@frr_no_debug_rip.group(cls=FRR_AbbreviationGroup, name='packet', invoke_without_command=True)
def frr_no_debug_rip_packet(no_debug_rip_packet_='no_debug_rip_packet'):
    """RIP packet"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_rip_packet.name
    
    if 'VIEW_NODE|no_debug_rip_packet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_rip_packet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_rip_packet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_rip_packet'][key] = val
    
    # set VIEW_NODE -> no_debug_rip_packet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_rip_packet'
    pass


@frr_no_debug_rip_packet.command('./	<cr>')
def frr_no_debug_rip_packet_cr():
    pass


@frr_no_debug_rip_packet.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['recv', 'send']), invoke_without_command=True)
def frr_no_debug_rip_packet_choicecase():
    """RIP option set for receive packet"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_rip_packet_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_rip_packet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_rip_packet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_rip_packet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_rip_packet'][key] = val
    
    # set VIEW_NODE -> no_debug_rip_packet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_rip_packet'
    pass


@frr_no_debug_rip_packet_choicecase.command('./	<cr>')
def frr_no_debug_rip_packet_choicecase_cr():
    pass


@frr_no_debug_rip.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_rip_zebra(zebra_='zebra'):
    """RIP and ZEBRA communication"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_rip_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'VIEW_NODE|no_debug_rip' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_rip'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_rip']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_rip'][key] = val
    
    # set VIEW_NODE -> no_debug_rip table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_rip'
    pass


@frr_no_debug_rip_zebra.command('./	<cr>')
def frr_no_debug_rip_zebra_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='ripng',)
def frr_no_debug_ripng(no_debug_ripng_='no_debug_ripng'):
    """RIPng configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ripng.name
    
    if 'VIEW_NODE|no_debug_ripng' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng'][key] = val
    
    # set VIEW_NODE -> no_debug_ripng table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ripng'
    pass


@frr_no_debug_ripng.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_ripng_events(events_='events'):
    """Debug option set for ripng events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ripng_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_ripng' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng'][key] = val
    
    # set VIEW_NODE -> no_debug_ripng table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ripng'
    pass


@frr_no_debug_ripng_events.command('./	<cr>')
def frr_no_debug_ripng_events_cr():
    pass


@frr_no_debug_ripng.group(cls=FRR_AbbreviationGroup, name='packet', invoke_without_command=True)
def frr_no_debug_ripng_packet(no_debug_ripng_packet_='no_debug_ripng_packet'):
    """Debug option set for ripng packet"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ripng_packet.name
    
    if 'VIEW_NODE|no_debug_ripng_packet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng_packet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng_packet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng_packet'][key] = val
    
    # set VIEW_NODE -> no_debug_ripng_packet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ripng_packet'
    pass


@frr_no_debug_ripng_packet.command('./	<cr>')
def frr_no_debug_ripng_packet_cr():
    pass


@frr_no_debug_ripng_packet.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['recv', 'send']), invoke_without_command=True)
def frr_no_debug_ripng_packet_choicecase():
    """Debug option set for receive packet"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ripng_packet_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_ripng_packet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng_packet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng_packet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng_packet'][key] = val
    
    # set VIEW_NODE -> no_debug_ripng_packet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ripng_packet'
    pass


@frr_no_debug_ripng_packet_choicecase.command('./	<cr>')
def frr_no_debug_ripng_packet_choicecase_cr():
    pass


@frr_no_debug_ripng.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_ripng_zebra(zebra_='zebra'):
    """Debug option set for ripng and zebra communication"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ripng_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'VIEW_NODE|no_debug_ripng' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_ripng'][key] = val
    
    # set VIEW_NODE -> no_debug_ripng table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_ripng'
    pass


@frr_no_debug_ripng_zebra.command('./	<cr>')
def frr_no_debug_ripng_zebra_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
def frr_no_debug_routemap(routemap_='route-map'):
    """Debug option set for route-maps"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_routemap.command('./	<cr>')
def frr_no_debug_routemap_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='rpki', invoke_without_command=True)
def frr_no_debug_rpki(rpki_='rpki'):
    """Disable debugging for rpki"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_rpki.name
    data_gen['rpki'] = rpki_='rpki'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_rpki.command('./	<cr>')
def frr_no_debug_rpki_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='spf-delay-ietf', invoke_without_command=True)
def frr_no_debug_spfdelayietf(spfdelayietf_='spf-delay-ietf'):
    """SPF Back-off Debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_spfdelayietf.name
    data_gen['spf-delay-ietf'] = spfdelayietf_='spf-delay-ietf'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_spfdelayietf.command('./	<cr>')
def frr_no_debug_spfdelayietf_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='ssmpingd', invoke_without_command=True)
def frr_no_debug_ssmpingd(ssmpingd_='ssmpingd'):
    """ssmpingd activity"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_ssmpingd.name
    data_gen['ssmpingd'] = ssmpingd_='ssmpingd'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_ssmpingd.command('./	<cr>')
def frr_no_debug_ssmpingd_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='static', invoke_without_command=True)
def frr_no_debug_static(no_debug_static_='no_debug_static'):
    """Static route daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_static.name
    
    if 'VIEW_NODE|no_debug_static' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_static'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_static']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_static'][key] = val
    
    # set VIEW_NODE -> no_debug_static table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_static'
    pass


@frr_no_debug_static.command('./	<cr>')
def frr_no_debug_static_cr():
    pass


@frr_no_debug_static.group(cls=FRR_AbbreviationGroup, name='bfd', invoke_without_command=True)
def frr_no_debug_static_bfd(bfd_='bfd'):
    """Debug bfd"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_static_bfd.name
    data_gen['bfd'] = bfd_='bfd'
    
    if 'VIEW_NODE|no_debug_static' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_static'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_static']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_static'][key] = val
    
    # set VIEW_NODE -> no_debug_static table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_static'
    pass


@frr_no_debug_static_bfd.command('./	<cr>')
def frr_no_debug_static_bfd_cr():
    pass


@frr_no_debug_static.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_static_events(events_='events'):
    """Debug events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_static_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_static' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_static'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_static']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_static'][key] = val
    
    # set VIEW_NODE -> no_debug_static table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_static'
    pass


@frr_no_debug_static_events.command('./	<cr>')
def frr_no_debug_static_events_cr():
    pass


@frr_no_debug_static.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
def frr_no_debug_static_route(route_='route'):
    """Debug route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_static_route.name
    data_gen['route'] = route_='route'
    
    if 'VIEW_NODE|no_debug_static' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_static'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_static']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_static'][key] = val
    
    # set VIEW_NODE -> no_debug_static table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_static'
    pass


@frr_no_debug_static_route.command('./	<cr>')
def frr_no_debug_static_route_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='unique-id',)
@click.argument('log_message_unique_id', metavar='UID', required=True, type=FRR_TYPE('UID'))
def frr_no_debug_uniqueid(log_message_unique_id, uniqueid_='unique-id'):
    """Options per individual log message, by unique ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_uniqueid.name
    data_gen['unique-id'] = uniqueid_='unique-id'
    data_gen['LOG_MESSAGE_UNIQUE_ID'] = log_message_unique_id
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_uniqueid.group(cls=FRR_AbbreviationGroup, name='backtrace', invoke_without_command=True)
def frr_no_debug_uniqueid_backtrace(backtrace_='backtrace'):
    """Add backtrace to log when message is printed"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_uniqueid_backtrace.name
    data_gen['backtrace'] = backtrace_='backtrace'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_uniqueid_backtrace.command('./	<cr>')
def frr_no_debug_uniqueid_backtrace_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
def frr_no_debug_vrf(vrf_='vrf'):
    """VRF Debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|no_debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug'][key] = val
    
    # set VIEW_NODE -> no_debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug'
    pass


@frr_no_debug_vrf.command('./	<cr>')
def frr_no_debug_vrf_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='vrrp', invoke_without_command=True)
def frr_no_debug_vrrp(no_debug_vrrp_='no_debug_vrrp'):
    """Virtual Router Redundancy Protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_vrrp.name
    
    if 'VIEW_NODE|no_debug_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'][key] = val
    
    # set VIEW_NODE -> no_debug_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_vrrp'
    pass


@frr_no_debug_vrrp.command('./	<cr>')
def frr_no_debug_vrrp_cr():
    pass


@frr_no_debug_vrrp.group(cls=FRR_AbbreviationGroup, name='arp', invoke_without_command=True)
def frr_no_debug_vrrp_arp(arp_='arp'):
    """Debug ARP"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_vrrp_arp.name
    data_gen['arp'] = arp_='arp'
    
    if 'VIEW_NODE|no_debug_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'][key] = val
    
    # set VIEW_NODE -> no_debug_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_vrrp'
    pass


@frr_no_debug_vrrp_arp.command('./	<cr>')
def frr_no_debug_vrrp_arp_cr():
    pass


@frr_no_debug_vrrp.group(cls=FRR_AbbreviationGroup, name='autoconfigure', invoke_without_command=True)
def frr_no_debug_vrrp_autoconfigure(autoconfigure_='autoconfigure'):
    """Debug autoconfiguration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_vrrp_autoconfigure.name
    data_gen['autoconfigure'] = autoconfigure_='autoconfigure'
    
    if 'VIEW_NODE|no_debug_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'][key] = val
    
    # set VIEW_NODE -> no_debug_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_vrrp'
    pass


@frr_no_debug_vrrp_autoconfigure.command('./	<cr>')
def frr_no_debug_vrrp_autoconfigure_cr():
    pass


@frr_no_debug_vrrp.group(cls=FRR_AbbreviationGroup, name='ndisc', invoke_without_command=True)
def frr_no_debug_vrrp_ndisc(ndisc_='ndisc'):
    """Debug Neighbor Discovery"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_vrrp_ndisc.name
    data_gen['ndisc'] = ndisc_='ndisc'
    
    if 'VIEW_NODE|no_debug_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'][key] = val
    
    # set VIEW_NODE -> no_debug_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_vrrp'
    pass


@frr_no_debug_vrrp_ndisc.command('./	<cr>')
def frr_no_debug_vrrp_ndisc_cr():
    pass


@frr_no_debug_vrrp.group(cls=FRR_AbbreviationGroup, name='packets', invoke_without_command=True)
def frr_no_debug_vrrp_packets(packets_='packets'):
    """Debug sent and received packets"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_vrrp_packets.name
    data_gen['packets'] = packets_='packets'
    
    if 'VIEW_NODE|no_debug_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'][key] = val
    
    # set VIEW_NODE -> no_debug_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_vrrp'
    pass


@frr_no_debug_vrrp_packets.command('./	<cr>')
def frr_no_debug_vrrp_packets_cr():
    pass


@frr_no_debug_vrrp.group(cls=FRR_AbbreviationGroup, name='protocol', invoke_without_command=True)
def frr_no_debug_vrrp_protocol(protocol_='protocol'):
    """Debug protocol state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_vrrp_protocol.name
    data_gen['protocol'] = protocol_='protocol'
    
    if 'VIEW_NODE|no_debug_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'][key] = val
    
    # set VIEW_NODE -> no_debug_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_vrrp'
    pass


@frr_no_debug_vrrp_protocol.command('./	<cr>')
def frr_no_debug_vrrp_protocol_cr():
    pass


@frr_no_debug_vrrp.group(cls=FRR_AbbreviationGroup, name='sockets', invoke_without_command=True)
def frr_no_debug_vrrp_sockets(sockets_='sockets'):
    """Debug socket creation and configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_vrrp_sockets.name
    data_gen['sockets'] = sockets_='sockets'
    
    if 'VIEW_NODE|no_debug_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'][key] = val
    
    # set VIEW_NODE -> no_debug_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_vrrp'
    pass


@frr_no_debug_vrrp_sockets.command('./	<cr>')
def frr_no_debug_vrrp_sockets_cr():
    pass


@frr_no_debug_vrrp.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_no_debug_vrrp_zebra(zebra_='zebra'):
    """Debug Zebra events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_vrrp_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'VIEW_NODE|no_debug_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_vrrp'][key] = val
    
    # set VIEW_NODE -> no_debug_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_vrrp'
    pass


@frr_no_debug_vrrp_zebra.command('./	<cr>')
def frr_no_debug_vrrp_zebra_cr():
    pass


@frr_no_debug.group(cls=FRR_AbbreviationGroup, name='zebra',)
def frr_no_debug_zebra(no_debug_zebra_='no_debug_zebra'):
    """Zebra configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra.name
    
    if 'VIEW_NODE|no_debug_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra'
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='dplane', invoke_without_command=True)
def frr_no_debug_zebra_dplane():
    """Debug zebra dataplane events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_dplane.name
    
    if 'VIEW_NODE|no_debug_zebra_dplane' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_dplane'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_dplane']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_dplane'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_dplane table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_dplane'
    pass


@frr_no_debug_zebra_dplane.command('./	<cr>')
def frr_no_debug_zebra_dplane_cr():
    pass


@frr_no_debug_zebra_dplane.group(cls=FRR_AbbreviationGroup, name='dpdk', invoke_without_command=True)
def frr_no_debug_zebra_dplane_dpdk(no_debug_zebra_dplane_dpdk_='no_debug_zebra_dplane_dpdk'):
    """Debug zebra DPDK offload events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_dplane_dpdk.name
    
    if 'VIEW_NODE|no_debug_zebra_dplane_dpdk' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_dplane_dpdk'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_dplane_dpdk']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_dplane_dpdk'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_dplane_dpdk table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_dplane_dpdk'
    pass


@frr_no_debug_zebra_dplane_dpdk.command('./	<cr>')
def frr_no_debug_zebra_dplane_dpdk_cr():
    pass


@frr_no_debug_zebra_dplane_dpdk.group(cls=FRR_AbbreviationGroup, name='detailed', invoke_without_command=True)
def frr_no_debug_zebra_dplane_dpdk_detailed(detailed_='detailed'):
    """Detailed debug information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_dplane_dpdk_detailed.name
    data_gen['detailed'] = detailed_='detailed'
    
    if 'VIEW_NODE|no_debug_zebra_dplane_dpdk' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_dplane_dpdk'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_dplane_dpdk']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_dplane_dpdk'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_dplane_dpdk table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_dplane_dpdk'
    pass


@frr_no_debug_zebra_dplane_dpdk_detailed.command('./	<cr>')
def frr_no_debug_zebra_dplane_dpdk_detailed_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='events', invoke_without_command=True)
def frr_no_debug_zebra_events(events_='events'):
    """Debug option set for zebra events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_events.name
    data_gen['events'] = events_='events'
    
    if 'VIEW_NODE|no_debug_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra'
    pass


@frr_no_debug_zebra_events.command('./	<cr>')
def frr_no_debug_zebra_events_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='evpn',)
def frr_no_debug_zebra_evpn(no_debug_zebra_evpn_='no_debug_zebra_evpn'):
    """EVPN"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_evpn.name
    
    if 'VIEW_NODE|no_debug_zebra_evpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_evpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_evpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_evpn'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_evpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_evpn'
    pass


@frr_no_debug_zebra_evpn.group(cls=FRR_AbbreviationGroup, name='mh',)
def frr_no_debug_zebra_evpn_mh(mh_='mh'):
    """Multihoming"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_evpn_mh.name
    data_gen['mh'] = mh_='mh'
    
    if 'VIEW_NODE|no_debug_zebra_evpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_evpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_evpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_evpn'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_evpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_evpn'
    pass


@frr_no_debug_zebra_evpn_mh.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['es', 'mac', 'neigh', 'nh']), invoke_without_command=True)
def frr_no_debug_zebra_evpn_mh_mhchoicecase():
    """Ethernet Segment Debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_evpn_mh_mhchoicecase.name
    data_gen['MH_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_zebra_evpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_evpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_evpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_evpn'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_evpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_evpn'
    pass


@frr_no_debug_zebra_evpn_mh_mhchoicecase.command('./	<cr>')
def frr_no_debug_zebra_evpn_mh_mhchoicecase_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='fpm', invoke_without_command=True)
def frr_no_debug_zebra_fpm(fpm_='fpm'):
    """Debug zebra FPM events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_fpm.name
    data_gen['fpm'] = fpm_='fpm'
    
    if 'VIEW_NODE|no_debug_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra'
    pass


@frr_no_debug_zebra_fpm.command('./	<cr>')
def frr_no_debug_zebra_fpm_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='kernel', invoke_without_command=True)
def frr_no_debug_zebra_kernel():
    """Debug option set for zebra between kernel interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_kernel.name
    
    if 'VIEW_NODE|no_debug_zebra_kernel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_kernel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_kernel']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_kernel'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_kernel table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_kernel'
    pass


@frr_no_debug_zebra_kernel.command('./	<cr>')
def frr_no_debug_zebra_kernel_cr():
    pass


@frr_no_debug_zebra_kernel.group(cls=FRR_AbbreviationGroup, name='msgdump', invoke_without_command=True)
def frr_no_debug_zebra_kernel_msgdump(no_debug_zebra_kernel_msgdump_='no_debug_zebra_kernel_msgdump'):
    """Dump raw netlink messages, sent and received"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_kernel_msgdump.name
    
    if 'VIEW_NODE|no_debug_zebra_kernel_msgdump' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_kernel_msgdump'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_kernel_msgdump']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_kernel_msgdump'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_kernel_msgdump table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_kernel_msgdump'
    pass


@frr_no_debug_zebra_kernel_msgdump.command('./	<cr>')
def frr_no_debug_zebra_kernel_msgdump_cr():
    pass


@frr_no_debug_zebra_kernel_msgdump.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['recv', 'send']), invoke_without_command=True)
def frr_no_debug_zebra_kernel_msgdump_choicecase():
    """Dump raw netlink messages received"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_kernel_msgdump_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_zebra_kernel_msgdump' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_kernel_msgdump'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_kernel_msgdump']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_kernel_msgdump'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_kernel_msgdump table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_kernel_msgdump'
    pass


@frr_no_debug_zebra_kernel_msgdump_choicecase.command('./	<cr>')
def frr_no_debug_zebra_kernel_msgdump_choicecase_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='mlag', invoke_without_command=True)
def frr_no_debug_zebra_mlag(mlag_='mlag'):
    """Debug option set for mlag events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_mlag.name
    data_gen['mlag'] = mlag_='mlag'
    
    if 'VIEW_NODE|no_debug_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra'
    pass


@frr_no_debug_zebra_mlag.command('./	<cr>')
def frr_no_debug_zebra_mlag_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='mpls', invoke_without_command=True)
def frr_no_debug_zebra_mpls(no_debug_zebra_mpls_='no_debug_zebra_mpls'):
    """Debug option set for zebra MPLS LSPs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_mpls.name
    
    if 'VIEW_NODE|no_debug_zebra_mpls' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_mpls'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_mpls']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_mpls'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_mpls table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_mpls'
    pass


@frr_no_debug_zebra_mpls.command('./	<cr>')
def frr_no_debug_zebra_mpls_cr():
    pass


@frr_no_debug_zebra_mpls.group(cls=FRR_AbbreviationGroup, name='detailed', invoke_without_command=True)
def frr_no_debug_zebra_mpls_detailed(detailed_='detailed'):
    """Debug option for zebra detailed info"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_mpls_detailed.name
    data_gen['detailed'] = detailed_='detailed'
    
    if 'VIEW_NODE|no_debug_zebra_mpls' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_mpls'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_mpls']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_mpls'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_mpls table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_mpls'
    pass


@frr_no_debug_zebra_mpls_detailed.command('./	<cr>')
def frr_no_debug_zebra_mpls_detailed_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='neigh', invoke_without_command=True)
def frr_no_debug_zebra_neigh(neigh_='neigh'):
    """Debug zebra neigh events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_neigh.name
    data_gen['neigh'] = neigh_='neigh'
    
    if 'VIEW_NODE|no_debug_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra'
    pass


@frr_no_debug_zebra_neigh.command('./	<cr>')
def frr_no_debug_zebra_neigh_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='nexthop', invoke_without_command=True)
def frr_no_debug_zebra_nexthop(no_debug_zebra_nexthop_='no_debug_zebra_nexthop'):
    """Debug zebra nexthop events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_nexthop.name
    
    if 'VIEW_NODE|no_debug_zebra_nexthop' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nexthop'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nexthop']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nexthop'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_nexthop table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_nexthop'
    pass


@frr_no_debug_zebra_nexthop.command('./	<cr>')
def frr_no_debug_zebra_nexthop_cr():
    pass


@frr_no_debug_zebra_nexthop.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_zebra_nexthop_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_nexthop_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_zebra_nexthop' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nexthop'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nexthop']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nexthop'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_nexthop table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_nexthop'
    pass


@frr_no_debug_zebra_nexthop_detail.command('./	<cr>')
def frr_no_debug_zebra_nexthop_detail_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='nht', invoke_without_command=True)
def frr_no_debug_zebra_nht(no_debug_zebra_nht_='no_debug_zebra_nht'):
    """Debug option set for zebra next hop tracking"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_nht.name
    
    if 'VIEW_NODE|no_debug_zebra_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nht'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_nht'
    pass


@frr_no_debug_zebra_nht.command('./	<cr>')
def frr_no_debug_zebra_nht_cr():
    pass


@frr_no_debug_zebra_nht.group(cls=FRR_AbbreviationGroup, name='detailed', invoke_without_command=True)
def frr_no_debug_zebra_nht_detailed(detailed_='detailed'):
    """Debug option set for detailed info"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_nht_detailed.name
    data_gen['detailed'] = detailed_='detailed'
    
    if 'VIEW_NODE|no_debug_zebra_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_nht'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_nht'
    pass


@frr_no_debug_zebra_nht_detailed.command('./	<cr>')
def frr_no_debug_zebra_nht_detailed_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='packet', invoke_without_command=True)
def frr_no_debug_zebra_packet(no_debug_zebra_packet_='no_debug_zebra_packet'):
    """Debug option set for zebra packet"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_packet.name
    
    if 'VIEW_NODE|no_debug_zebra_packet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_packet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_packet'
    pass


@frr_no_debug_zebra_packet.command('./	<cr>')
def frr_no_debug_zebra_packet_cr():
    pass


@frr_no_debug_zebra_packet.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['recv', 'send']), invoke_without_command=True)
def frr_no_debug_zebra_packet_choicecase():
    """Debug option set for receive packet"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_packet_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_debug_zebra_packet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_packet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_packet'
    pass


@frr_no_debug_zebra_packet_choicecase.command('./	<cr>')
def frr_no_debug_zebra_packet_choicecase_cr():
    pass


@frr_no_debug_zebra_packet_choicecase.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_zebra_packet_choicecase_detail(detail_='detail'):
    """Debug option set for detailed info"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_packet_choicecase_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_zebra_packet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_packet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_packet'
    pass


@frr_no_debug_zebra_packet_choicecase_detail.command('./	<cr>')
def frr_no_debug_zebra_packet_choicecase_detail_cr():
    pass


@frr_no_debug_zebra_packet.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_no_debug_zebra_packet_detail(detail_='detail'):
    """Debug option set for detailed info"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_packet_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|no_debug_zebra_packet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_packet'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_packet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_packet'
    pass


@frr_no_debug_zebra_packet_detail.command('./	<cr>')
def frr_no_debug_zebra_packet_detail_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='pbr', invoke_without_command=True)
def frr_no_debug_zebra_pbr(pbr_='pbr'):
    """Debug zebra pbr events"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_pbr.name
    data_gen['pbr'] = pbr_='pbr'
    
    if 'VIEW_NODE|no_debug_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra'
    pass


@frr_no_debug_zebra_pbr.command('./	<cr>')
def frr_no_debug_zebra_pbr_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='pseudowires', invoke_without_command=True)
def frr_no_debug_zebra_pseudowires(pseudowires_='pseudowires'):
    """Debug option set for zebra pseudowires"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_pseudowires.name
    data_gen['pseudowires'] = pseudowires_='pseudowires'
    
    if 'VIEW_NODE|no_debug_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra'
    pass


@frr_no_debug_zebra_pseudowires.command('./	<cr>')
def frr_no_debug_zebra_pseudowires_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='rib', invoke_without_command=True)
def frr_no_debug_zebra_rib(no_debug_zebra_rib_='no_debug_zebra_rib'):
    """Debug zebra RIB"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_rib.name
    
    if 'VIEW_NODE|no_debug_zebra_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_rib'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_rib'
    pass


@frr_no_debug_zebra_rib.command('./	<cr>')
def frr_no_debug_zebra_rib_cr():
    pass


@frr_no_debug_zebra_rib.group(cls=FRR_AbbreviationGroup, name='detailed', invoke_without_command=True)
def frr_no_debug_zebra_rib_detailed(detailed_='detailed'):
    """Detailed debugs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_rib_detailed.name
    data_gen['detailed'] = detailed_='detailed'
    
    if 'VIEW_NODE|no_debug_zebra_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra_rib'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra_rib'
    pass


@frr_no_debug_zebra_rib_detailed.command('./	<cr>')
def frr_no_debug_zebra_rib_detailed_cr():
    pass


@frr_no_debug_zebra.group(cls=FRR_AbbreviationGroup, name='vxlan', invoke_without_command=True)
def frr_no_debug_zebra_vxlan(vxlan_='vxlan'):
    """Debug option set for zebra VxLAN (EVPN)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_debug_zebra_vxlan.name
    data_gen['vxlan'] = vxlan_='vxlan'
    
    if 'VIEW_NODE|no_debug_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_debug_zebra'][key] = val
    
    # set VIEW_NODE -> no_debug_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_debug_zebra'
    pass


@frr_no_debug_zebra_vxlan.command('./	<cr>')
def frr_no_debug_zebra_vxlan_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_output.name
    
    if 'VIEW_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_output'][key] = val
    
    # set VIEW_NODE -> no_output table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_output'
    pass


@frr_no_output.command('./	<cr>')
def frr_no_output_cr():
    pass


@frr_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_output_file.name
    
    if 'VIEW_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_output_file'][key] = val
    
    # set VIEW_NODE -> no_output_file table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_output_file'
    pass


@frr_no_output_file.command('./	<cr>')
def frr_no_output_file_cr():
    pass


@frr_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['FILE']), invoke_without_command=True)
def frr_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_output_file'][key] = val
    
    # set VIEW_NODE -> no_output_file table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_output_file'
    pass


@frr_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_no_output_file_pathtodumpoutput_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='sharp',)
def frr_no_sharp(no_sharp_='no_sharp'):
    """Sharp Routing Protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_sharp.name
    
    if 'VIEW_NODE|no_sharp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_sharp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_sharp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_sharp'][key] = val
    
    # set VIEW_NODE -> no_sharp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_sharp'
    pass


@frr_no_sharp.group(cls=FRR_AbbreviationGroup, name='interface',)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_no_sharp_interface(interface_name, interface_='interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_sharp_interface.name
    data_gen['interface'] = interface_='interface'
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'VIEW_NODE|no_sharp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_sharp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_sharp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_sharp'][key] = val
    
    # set VIEW_NODE -> no_sharp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_sharp'
    pass


@frr_no_sharp_interface.group(cls=FRR_AbbreviationGroup, name='protodown', invoke_without_command=True)
def frr_no_sharp_interface_protodown(protodown_='protodown'):
    """Set interface protodown"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_sharp_interface_protodown.name
    data_gen['protodown'] = protodown_='protodown'
    
    if 'VIEW_NODE|no_sharp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_sharp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_sharp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_sharp'][key] = val
    
    # set VIEW_NODE -> no_sharp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_sharp'
    pass


@frr_no_sharp_interface_protodown.command('./	<cr>')
def frr_no_sharp_interface_protodown_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='terminal',)
def frr_no_terminal(no_terminal_='no_terminal'):
    """Set terminal line parameters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_terminal.name
    
    if 'VIEW_NODE|no_terminal' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_terminal'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_terminal']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_terminal'][key] = val
    
    # set VIEW_NODE -> no_terminal table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_terminal'
    pass


@frr_no_terminal.group(cls=FRR_AbbreviationGroup, name='length', invoke_without_command=True)
@click.argument('number_of_lines_on', metavar='(0-4294967295)', required=True, type=FRR_TYPE((0, 4294967295)))
def frr_no_terminal_length(number_of_lines_on, length_='length'):
    """Set number of lines on a screen"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_terminal_length.name
    data_gen['length'] = length_='length'
    data_gen['NUMBER_OF_LINES_ON'] = number_of_lines_on
    
    if 'VIEW_NODE|no_terminal' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_terminal'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_terminal']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_terminal'][key] = val
    
    # set VIEW_NODE -> no_terminal table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_terminal'
    pass


@frr_no_terminal_length.command('./	<cr>')
def frr_no_terminal_length_cr():
    pass


@frr_no_terminal.group(cls=FRR_AbbreviationGroup, name='monitor', invoke_without_command=True)
def frr_no_terminal_monitor(no_terminal_monitor_='no_terminal_monitor'):
    """Receive log messages to active VTY session"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_terminal_monitor.name
    
    if 'VIEW_NODE|no_terminal_monitor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_terminal_monitor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_terminal_monitor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_terminal_monitor'][key] = val
    
    # set VIEW_NODE -> no_terminal_monitor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_terminal_monitor'
    pass


@frr_no_terminal_monitor.command('./	<cr>')
def frr_no_terminal_monitor_cr():
    pass


@frr_no_terminal_monitor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_no_terminal_monitor_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_terminal_monitor_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|no_terminal_monitor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_terminal_monitor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_terminal_monitor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_terminal_monitor'][key] = val
    
    # set VIEW_NODE -> no_terminal_monitor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_terminal_monitor'
    pass


@frr_no_terminal_monitor_daemonslist.command('./	<cr>')
def frr_no_terminal_monitor_daemonslist_cr():
    pass


@frr_no_terminal.group(cls=FRR_AbbreviationGroup, name='paginate', invoke_without_command=True)
def frr_no_terminal_paginate(paginate_='paginate'):
    """Use pager for output scrolling"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_terminal_paginate.name
    data_gen['paginate'] = paginate_='paginate'
    
    if 'VIEW_NODE|no_terminal' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_terminal'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_terminal']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_terminal'][key] = val
    
    # set VIEW_NODE -> no_terminal table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_terminal'
    pass


@frr_no_terminal_paginate.command('./	<cr>')
def frr_no_terminal_paginate_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='watchfrr',)
def frr_no_watchfrr(no_watchfrr_='no_watchfrr'):
    """Watchfrr Specific sub-command"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_watchfrr.name
    
    if 'VIEW_NODE|no_watchfrr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_watchfrr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_watchfrr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_watchfrr'][key] = val
    
    # set VIEW_NODE -> no_watchfrr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_watchfrr'
    pass


@frr_no_watchfrr.group(cls=FRR_AbbreviationGroup, name='ignore', invoke_without_command=True)
@click.argument('the_daemon_to_ignore', metavar='DAEMON', required=True, type=FRR_TYPE('DAEMON'))
def frr_no_watchfrr_ignore(the_daemon_to_ignore, ignore_='ignore'):
    """Ignore a specified daemon when it does not respond to echo request"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_no_watchfrr_ignore.name
    data_gen['ignore'] = ignore_='ignore'
    data_gen['THE_DAEMON_TO_IGNORE'] = the_daemon_to_ignore
    
    if 'VIEW_NODE|no_watchfrr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|no_watchfrr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|no_watchfrr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|no_watchfrr'][key] = val
    
    # set VIEW_NODE -> no_watchfrr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'no_watchfrr'
    pass


@frr_no_watchfrr_ignore.command('./	<cr>')
def frr_no_watchfrr_ignore_cr():
    pass

