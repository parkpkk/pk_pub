import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='babel',)
def frr_show_babel(show_babel_='show_babel'):
    """Babel information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_babel.name
    
    if 'VIEW_NODE|show_babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_babel']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_babel'][key] = val
    
    # set VIEW_NODE -> show_babel table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_babel'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='bfd',)
def frr_show_bfd(show_bfd_='show_bfd'):
    """BFD monitoring"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bfd.name
    
    if 'VIEW_NODE|show_bfd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bfd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bfd'][key] = val
    
    # set VIEW_NODE -> show_bfd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bfd'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='bgp', invoke_without_command=True)
def frr_show_bgp(show_bgp_='show_bgp'):
    """BGP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bgp.name
    
    if 'VIEW_NODE|show_bgp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_bgp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_bgp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_bgp'][key] = val
    
    # set VIEW_NODE -> show_bgp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_bgp'
    pass


@frr_show_bgp.command('./	<cr>')
def frr_show_bgp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='bmp', invoke_without_command=True)
def frr_show_bmp(bmp_='bmp'):
    """BGP Monitoring Protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_bmp.name
    data_gen['bmp'] = bmp_='bmp'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_bmp.command('./	<cr>')
def frr_show_bmp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='cli',)
def frr_show_cli(show_cli_='show_cli'):
    """CLI reflection"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_cli.name
    
    if 'VIEW_NODE|show_cli' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_cli'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_cli']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_cli'][key] = val
    
    # set VIEW_NODE -> show_cli table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_cli'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='commandtree', invoke_without_command=True)
def frr_show_commandtree(show_commandtree_='show_commandtree'):
    """Show command tree"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_commandtree.name
    
    if 'VIEW_NODE|show_commandtree' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_commandtree'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_commandtree']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_commandtree'][key] = val
    
    # set VIEW_NODE -> show_commandtree table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_commandtree'
    pass


@frr_show_commandtree.command('./	<cr>')
def frr_show_commandtree_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='configuration', invoke_without_command=True)
def frr_show_configuration():
    """Configuration information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration.name
    
    if 'VIEW_NODE|show_configuration' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration'][key] = val
    
    # set VIEW_NODE -> show_configuration table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration'
    pass


@frr_show_configuration.command('./	<cr>')
def frr_show_configuration_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='daemons', invoke_without_command=True)
def frr_show_daemons(daemons_='daemons'):
    """Show list of running daemons"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_daemons.name
    data_gen['daemons'] = daemons_='daemons'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_daemons.command('./	<cr>')
def frr_show_daemons_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='debugging', invoke_without_command=True)
def frr_show_debugging(show_debugging_='show_debugging'):
    """Debugging functions"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_debugging.name
    
    if 'VIEW_NODE|show_debugging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_debugging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_debugging'][key] = val
    
    # set VIEW_NODE -> show_debugging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_debugging'
    pass


@frr_show_debugging.command('./	<cr>')
def frr_show_debugging_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='dmvpn', invoke_without_command=True)
def frr_show_dmvpn(show_dmvpn_='show_dmvpn'):
    """DMVPN information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_dmvpn.name
    
    if 'VIEW_NODE|show_dmvpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_dmvpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_dmvpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_dmvpn'][key] = val
    
    # set VIEW_NODE -> show_dmvpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_dmvpn'
    pass


@frr_show_dmvpn.command('./	<cr>')
def frr_show_dmvpn_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='error',)
def frr_show_error(error_='error'):
    """Information on errors"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_error.name
    data_gen['error'] = error_='error'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='evpn', invoke_without_command=True)
def frr_show_evpn(show_evpn_='show_evpn'):
    """EVPN"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn.name
    
    if 'VIEW_NODE|show_evpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn'][key] = val
    
    # set VIEW_NODE -> show_evpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn'
    pass


@frr_show_evpn.command('./	<cr>')
def frr_show_evpn_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='fpm', invoke_without_command=True)
def frr_show_fpm():
    """Forwarding Plane Manager configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_fpm.name
    
    if 'VIEW_NODE|show_fpm' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_fpm'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_fpm']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_fpm'][key] = val
    
    # set VIEW_NODE -> show_fpm table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_fpm'
    pass


@frr_show_fpm.command('./	<cr>')
def frr_show_fpm_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='frr', invoke_without_command=True)
def frr_show_frr(frr_='frr'):
    """FRR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_frr.name
    data_gen['frr'] = frr_='frr'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_frr.command('./	<cr>')
def frr_show_frr_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='history', invoke_without_command=True)
def frr_show_history(history_='history'):
    """Display the session command history"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_history.name
    data_gen['history'] = history_='history'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_history.command('./	<cr>')
def frr_show_history_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_interface(show_interface_='show_interface'):
    """Interface status and configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface.name
    
    if 'VIEW_NODE|show_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface'][key] = val
    
    # set VIEW_NODE -> show_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface'
    pass


@frr_show_interface.command('./	<cr>')
def frr_show_interface_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ip',)
def frr_show_ip(show_ip_='show_ip'):
    """IP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ip.name
    
    if 'VIEW_NODE|show_ip' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ip'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ip']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ip'][key] = val
    
    # set VIEW_NODE -> show_ip table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ip'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ipv6',)
def frr_show_ipv6(show_ipv6_='show_ipv6'):
    """IPv6 information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6.name
    
    if 'VIEW_NODE|show_ipv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6'][key] = val
    
    # set VIEW_NODE -> show_ipv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='isis',)
def frr_show_isis(show_isis_='show_isis'):
    """OpenFabric routing protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis.name
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_json(show_json_='show_json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_json.name
    
    if 'VIEW_NODE|show_json' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_json'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_json']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_json'][key] = val
    
    # set VIEW_NODE -> show_json table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_json'
    pass


@frr_show_json.command('./	<cr>')
def frr_show_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='l2vpn', invoke_without_command=True)
def frr_show_l2vpn():
    """Show information about Layer2 VPN"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn.name
    
    if 'VIEW_NODE|show_l2vpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn'][key] = val
    
    # set VIEW_NODE -> show_l2vpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn'
    pass


@frr_show_l2vpn.command('./	<cr>')
def frr_show_l2vpn_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='logging', invoke_without_command=True)
def frr_show_logging(show_logging_='show_logging'):
    """Show current logging configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_logging.name
    
    if 'VIEW_NODE|show_logging' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_logging'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_logging']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_logging'][key] = val
    
    # set VIEW_NODE -> show_logging table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_logging'
    pass


@frr_show_logging.command('./	<cr>')
def frr_show_logging_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='mac', invoke_without_command=True)
def frr_show_mac():
    """mac access lists"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mac.name
    
    if 'VIEW_NODE|show_mac' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mac'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mac']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mac'][key] = val
    
    # set VIEW_NODE -> show_mac table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mac'
    pass


@frr_show_mac.command('./	<cr>')
def frr_show_mac_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='memory', invoke_without_command=True)
def frr_show_memory(show_memory_='show_memory'):
    """Memory statistics"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_memory.name
    
    if 'VIEW_NODE|show_memory' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_memory'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_memory']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_memory'][key] = val
    
    # set VIEW_NODE -> show_memory table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_memory'
    pass


@frr_show_memory.command('./	<cr>')
def frr_show_memory_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='modules', invoke_without_command=True)
def frr_show_modules(modules_='modules'):
    """Loaded modules"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_modules.name
    data_gen['modules'] = modules_='modules'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_modules.command('./	<cr>')
def frr_show_modules_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='motd', invoke_without_command=True)
def frr_show_motd(motd_='motd'):
    """Show motd"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_motd.name
    data_gen['motd'] = motd_='motd'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_motd.command('./	<cr>')
def frr_show_motd_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='mpls',)
def frr_show_mpls(show_mpls_='show_mpls'):
    """MPLS information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls.name
    
    if 'VIEW_NODE|show_mpls' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls'][key] = val
    
    # set VIEW_NODE -> show_mpls table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_nexthopgroup():
    """Show Nexthop Groups"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup.name
    
    if 'VIEW_NODE|show_nexthop-group' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group'
    pass


@frr_show_nexthopgroup.command('./	<cr>')
def frr_show_nexthopgroup_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='openfabric',)
def frr_show_openfabric(show_openfabric_='show_openfabric'):
    """OpenFabric routing protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_openfabric.name
    
    if 'VIEW_NODE|show_openfabric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_openfabric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_openfabric']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_openfabric'][key] = val
    
    # set VIEW_NODE -> show_openfabric table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_openfabric'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='pathd',)
def frr_show_pathd():
    """pathd daemon"""
    global COMMON_DATA_MAP
    
    pass


@click.group(cls=FRR_AbbreviationGroup, name='pbr', invoke_without_command=True)
def frr_show_pbr(show_pbr_='show_pbr'):
    """Policy-Based Routing"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr.name
    
    if 'VIEW_NODE|show_pbr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr'][key] = val
    
    # set VIEW_NODE -> show_pbr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr'
    pass


@frr_show_pbr.command('./	<cr>')
def frr_show_pbr_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
def frr_show_routemap(show_routemap_='show_route-map'):
    """route-map information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_routemap.name
    
    if 'VIEW_NODE|show_route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_route-map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_route-map'][key] = val
    
    # set VIEW_NODE -> show_route-map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_route-map'
    pass


@frr_show_routemap.command('./	<cr>')
def frr_show_routemap_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='route-map-unused', invoke_without_command=True)
def frr_show_routemapunused(routemapunused_='route-map-unused'):
    """unused route-map information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_routemapunused.name
    data_gen['route-map-unused'] = routemapunused_='route-map-unused'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_routemapunused.command('./	<cr>')
def frr_show_routemapunused_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
def frr_show_routerid(show_routerid_='show_router-id'):
    """Show the configured router-id"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_routerid.name
    
    if 'VIEW_NODE|show_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_router-id'][key] = val
    
    # set VIEW_NODE -> show_router-id table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_router-id'
    pass


@frr_show_routerid.command('./	<cr>')
def frr_show_routerid_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='rpki',)
def frr_show_rpki(show_rpki_='show_rpki'):
    """Control rpki specific settings"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki.name
    
    if 'VIEW_NODE|show_rpki' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'][key] = val
    
    # set VIEW_NODE -> show_rpki table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='running-config', invoke_without_command=True)
def frr_show_runningconfig(show_runningconfig_='show_running-config'):
    """Current operating configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_runningconfig.name
    
    if 'VIEW_NODE|show_running-config' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_running-config'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_running-config']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_running-config'][key] = val
    
    # set VIEW_NODE -> show_running-config table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_running-config'
    pass


@frr_show_runningconfig.command('./	<cr>')
def frr_show_runningconfig_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='segment-routing', invoke_without_command=True)
def frr_show_segmentrouting():
    """Segment Routing"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_segmentrouting.name
    
    if 'VIEW_NODE|show_segment-routing' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_segment-routing']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing'][key] = val
    
    # set VIEW_NODE -> show_segment-routing table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_segment-routing'
    pass


@frr_show_segmentrouting.command('./	<cr>')
def frr_show_segmentrouting_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='sharp', invoke_without_command=True)
def frr_show_sharp():
    """Sharp Routing Protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp.name
    
    if 'VIEW_NODE|show_sharp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp'][key] = val
    
    # set VIEW_NODE -> show_sharp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp'
    pass


@frr_show_sharp.command('./	<cr>')
def frr_show_sharp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='sr-te', invoke_without_command=True)
def frr_show_srte():
    """SR-TE info"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte.name
    
    if 'VIEW_NODE|show_sr-te' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te'][key] = val
    
    # set VIEW_NODE -> show_sr-te table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te'
    pass


@frr_show_srte.command('./	<cr>')
def frr_show_srte_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='startup-config', invoke_without_command=True)
def frr_show_startupconfig(startupconfig_='startup-config'):
    """Contents of startup configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_startupconfig.name
    data_gen['startup-config'] = startupconfig_='startup-config'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_startupconfig.command('./	<cr>')
def frr_show_startupconfig_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='thread',)
def frr_show_thread(show_thread_='show_thread'):
    """Thread information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_thread.name
    
    if 'VIEW_NODE|show_thread' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_thread'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_thread']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_thread'][key] = val
    
    # set VIEW_NODE -> show_thread table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_thread'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='version', invoke_without_command=True)
def frr_show_version(version_='version'):
    """Displays zebra version"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_version.name
    data_gen['version'] = version_='version'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_version.command('./	<cr>')
def frr_show_version_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vnc',)
def frr_show_vnc(show_vnc_='show_vnc'):
    """VNC information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc.name
    
    if 'VIEW_NODE|show_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc'][key] = val
    
    # set VIEW_NODE -> show_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
def frr_show_vrf(show_vrf_='show_vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrf.name
    
    if 'VIEW_NODE|show_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrf'][key] = val
    
    # set VIEW_NODE -> show_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrf'
    pass


@frr_show_vrf.command('./	<cr>')
def frr_show_vrf_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrrp', invoke_without_command=True)
def frr_show_vrrp(show_vrrp_='show_vrrp'):
    """Virtual Router Redundancy Protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrrp.name
    
    if 'VIEW_NODE|show_vrrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrrp'][key] = val
    
    # set VIEW_NODE -> show_vrrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrrp'
    pass


@frr_show_vrrp.command('./	<cr>')
def frr_show_vrrp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='watchfrr', invoke_without_command=True)
def frr_show_watchfrr(watchfrr_='watchfrr'):
    """watchfrr information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_watchfrr.name
    data_gen['watchfrr'] = watchfrr_='watchfrr'
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr_show_watchfrr.command('./	<cr>')
def frr_show_watchfrr_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='work-queues', invoke_without_command=True)
def frr_show_workqueues(show_workqueues_='show_work-queues'):
    """Work Queue information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_workqueues.name
    
    if 'VIEW_NODE|show_work-queues' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_work-queues'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_work-queues']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_work-queues'][key] = val
    
    # set VIEW_NODE -> show_work-queues table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_work-queues'
    pass


@frr_show_workqueues.command('./	<cr>')
def frr_show_workqueues_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='yang',)
def frr_show_yang(show_yang_='show_yang'):
    """YANG information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang.name
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_show_zebra(show_zebra_='show_zebra'):
    """Zebra information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra.name
    
    if 'VIEW_NODE|show_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra'][key] = val
    
    # set VIEW_NODE -> show_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra'
    pass


@frr_show_zebra.command('./	<cr>')
def frr_show_zebra_cr():
    pass

