import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='babel', invoke_without_command=True)
def frr_show_debugging_babel(babel_='babel'):
    """Babel"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_babel.name
    data_gen['babel'] = babel_='babel'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_babel.command('./	<cr>')
def frr_show_debugging_babel_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='bfd', invoke_without_command=True)
def frr_show_debugging_bfd(bfd_='bfd'):
    """BFD daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_bfd.name
    data_gen['bfd'] = bfd_='bfd'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_bfd.command('./	<cr>')
def frr_show_debugging_bfd_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='bgp', invoke_without_command=True)
def frr_show_debugging_bgp(show_debugging_bgp_='show_debugging_bgp'):
    """BGP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_bgp.name
    
    if 'VIEW_NODE|show_debugging_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_bgp'][key] = val
    
    # set VIEW_NODE -> show_debugging_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging_bgp'
    pass


@frr_show_debugging_bgp.command('./	<cr>')
def frr_show_debugging_bgp_cr():
    pass


@frr_show_debugging_bgp.group(cls=FRR_AbbreviationGroup, name='vnc', invoke_without_command=True)
def frr_show_debugging_bgp_vnc(vnc_='vnc'):
    """VNC information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_bgp_vnc.name
    data_gen['vnc'] = vnc_='vnc'
    
    if 'VIEW_NODE|show_debugging_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_bgp'][key] = val
    
    # set VIEW_NODE -> show_debugging_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging_bgp'
    pass


@frr_show_debugging_bgp_vnc.command('./	<cr>')
def frr_show_debugging_bgp_vnc_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='eigrp', invoke_without_command=True)
def frr_show_debugging_eigrp(eigrp_='eigrp'):
    """P information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_eigrp.name
    data_gen['eigrp'] = eigrp_='eigrp'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_eigrp.command('./	<cr>')
def frr_show_debugging_eigrp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='hashtable', invoke_without_command=True)
def frr_show_debugging_hashtable(show_debugging_hashtable_='show_debugging_hashtable'):
    """Statistics about hash tables"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_hashtable.name
    
    if 'VIEW_NODE|show_debugging_hashtable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_hashtable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging_hashtable']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_hashtable'][key] = val
    
    # set VIEW_NODE -> show_debugging_hashtable table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging_hashtable'
    pass


@frr_show_debugging_hashtable.command('./	<cr>')
def frr_show_debugging_hashtable_cr():
    pass


@frr_show_debugging_hashtable.group(cls=FRR_AbbreviationGroup, name='statistics', invoke_without_command=True)
def frr_show_debugging_hashtable_statistics(statistics_='statistics'):
    """Statistics about hash tables"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_hashtable_statistics.name
    data_gen['statistics'] = statistics_='statistics'
    
    if 'VIEW_NODE|show_debugging_hashtable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_hashtable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging_hashtable']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_hashtable'][key] = val
    
    # set VIEW_NODE -> show_debugging_hashtable table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging_hashtable'
    pass


@frr_show_debugging_hashtable_statistics.command('./	<cr>')
def frr_show_debugging_hashtable_statistics_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='isis', invoke_without_command=True)
def frr_show_debugging_isis(isis_='isis'):
    """OpenFabric routing protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_isis.name
    data_gen['isis'] = isis_='isis'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_isis.command('./	<cr>')
def frr_show_debugging_isis_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='mpls',)
def frr_show_debugging_mpls(show_debugging_mpls_='show_debugging_mpls'):
    """MPLS information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_mpls.name
    
    if 'VIEW_NODE|show_debugging_mpls' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_mpls'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging_mpls']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_mpls'][key] = val
    
    # set VIEW_NODE -> show_debugging_mpls table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging_mpls'
    pass


@frr_show_debugging_mpls.group(cls=FRR_AbbreviationGroup, name='ldp', invoke_without_command=True)
def frr_show_debugging_mpls_ldp(ldp_='ldp'):
    """Label Distribution Protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_mpls_ldp.name
    data_gen['ldp'] = ldp_='ldp'
    
    if 'VIEW_NODE|show_debugging_mpls' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_mpls'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging_mpls']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_mpls'][key] = val
    
    # set VIEW_NODE -> show_debugging_mpls table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging_mpls'
    pass


@frr_show_debugging_mpls_ldp.command('./	<cr>')
def frr_show_debugging_mpls_ldp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='nhrp', invoke_without_command=True)
def frr_show_debugging_nhrp(nhrp_='nhrp'):
    """NHRP configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_nhrp.name
    data_gen['nhrp'] = nhrp_='nhrp'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_nhrp.command('./	<cr>')
def frr_show_debugging_nhrp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='openfabric', invoke_without_command=True)
def frr_show_debugging_openfabric(openfabric_='openfabric'):
    """OpenFabric routing protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_openfabric.name
    data_gen['openfabric'] = openfabric_='openfabric'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_openfabric.command('./	<cr>')
def frr_show_debugging_openfabric_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ospf', invoke_without_command=True)
def frr_show_debugging_ospf(show_debugging_ospf_='show_debugging_ospf'):
    """OSPF information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_ospf.name
    
    if 'VIEW_NODE|show_debugging_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_ospf'][key] = val
    
    # set VIEW_NODE -> show_debugging_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging_ospf'
    pass


@frr_show_debugging_ospf.command('./	<cr>')
def frr_show_debugging_ospf_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ospf6', invoke_without_command=True)
def frr_show_debugging_ospf6(ospf6_='ospf6'):
    """Open Shortest Path First (OSPF) for IPv6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_ospf6.name
    data_gen['ospf6'] = ospf6_='ospf6'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_ospf6.command('./	<cr>')
def frr_show_debugging_ospf6_cr():
    pass


@frr_show_debugging_ospf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, [(1, 65535)]), invoke_without_command=True)
def frr_show_debugging_ospf_instanceid():
    """Instance ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_ospf_instanceid.name
    data_gen['INSTANCE_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_debugging_ospf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_ospf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging_ospf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging_ospf'][key] = val
    
    # set VIEW_NODE -> show_debugging_ospf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging_ospf'
    pass


@frr_show_debugging_ospf_instanceid.command('./	<cr>')
def frr_show_debugging_ospf_instanceid_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='pathd', invoke_without_command=True)
def frr_show_debugging_pathd(pathd_='pathd'):
    """pathd module debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_pathd.name
    data_gen['pathd'] = pathd_='pathd'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_pathd.command('./	<cr>')
def frr_show_debugging_pathd_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='pathd-pcep', invoke_without_command=True)
def frr_show_debugging_pathdpcep(pathdpcep_='pathd-pcep'):
    """pathd pcep module debugging"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_pathdpcep.name
    data_gen['pathd-pcep'] = pathdpcep_='pathd-pcep'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_pathdpcep.command('./	<cr>')
def frr_show_debugging_pathdpcep_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='pbr', invoke_without_command=True)
def frr_show_debugging_pbr(pbr_='pbr'):
    """Policy Based Routing"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_pbr.name
    data_gen['pbr'] = pbr_='pbr'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_pbr.command('./	<cr>')
def frr_show_debugging_pbr_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='pim', invoke_without_command=True)
def frr_show_debugging_pim(pim_='pim'):
    """PIM information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_pim.name
    data_gen['pim'] = pim_='pim'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_pim.command('./	<cr>')
def frr_show_debugging_pim_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='pimv6', invoke_without_command=True)
def frr_show_debugging_pimv6(pimv6_='pimv6'):
    """PIMv6 Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_pimv6.name
    data_gen['pimv6'] = pimv6_='pimv6'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_pimv6.command('./	<cr>')
def frr_show_debugging_pimv6_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='rip', invoke_without_command=True)
def frr_show_debugging_rip(rip_='rip'):
    """RIP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_rip.name
    data_gen['rip'] = rip_='rip'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_rip.command('./	<cr>')
def frr_show_debugging_rip_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ripng', invoke_without_command=True)
def frr_show_debugging_ripng(ripng_='ripng'):
    """RIPng configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_ripng.name
    data_gen['ripng'] = ripng_='ripng'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_ripng.command('./	<cr>')
def frr_show_debugging_ripng_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='sharp', invoke_without_command=True)
def frr_show_debugging_sharp(sharp_='sharp'):
    """Sharp Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_sharp.name
    data_gen['sharp'] = sharp_='sharp'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_sharp.command('./	<cr>')
def frr_show_debugging_sharp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='static', invoke_without_command=True)
def frr_show_debugging_static(static_='static'):
    """Static Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_static.name
    data_gen['static'] = static_='static'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_static.command('./	<cr>')
def frr_show_debugging_static_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrrp', invoke_without_command=True)
def frr_show_debugging_vrrp(vrrp_='vrrp'):
    """VRRP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_vrrp.name
    data_gen['vrrp'] = vrrp_='vrrp'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_vrrp.command('./	<cr>')
def frr_show_debugging_vrrp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='watchfrr', invoke_without_command=True)
def frr_show_debugging_watchfrr(watchfrr_='watchfrr'):
    """watchfrr information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_watchfrr.name
    data_gen['watchfrr'] = watchfrr_='watchfrr'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_watchfrr.command('./	<cr>')
def frr_show_debugging_watchfrr_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_show_debugging_zebra(zebra_='zebra'):
    """Zebra configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging_zebra.command('./	<cr>')
def frr_show_debugging_zebra_cr():
    pass

