import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='prepare',)
def frr_gracefulrestart_prepare():
    """Prepare upcoming graceful restart"""
    global COMMON_DATA_MAP
    
    pass


@frr_gracefulrestart_prepare.group(cls=FRR_AbbreviationGroup, name='ip',)
def frr_gracefulrestart_prepare_ip(gracefulrestart_prepare_ip_='graceful-restart_prepare_ip'):
    """IP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_gracefulrestart_prepare_ip.name
    
    if 'VIEW_NODE|graceful-restart_prepare_ip' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ip'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ip']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ip'][key] = val
    
    # set VIEW_NODE -> graceful-restart_prepare_ip table
    COMMON_DATA_MAP['VIEW_NODE'] = 'graceful-restart_prepare_ip'
    pass


@frr_gracefulrestart_prepare_ip.group(cls=FRR_AbbreviationGroup, name='ospf', invoke_without_command=True)
def frr_gracefulrestart_prepare_ip_ospf(ospf_='ospf'):
    """Prepare to restart the OSPF process"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_gracefulrestart_prepare_ip_ospf.name
    data_gen['ospf'] = ospf_='ospf'
    
    if 'VIEW_NODE|graceful-restart_prepare_ip' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ip'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ip']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ip'][key] = val
    
    # set VIEW_NODE -> graceful-restart_prepare_ip table
    COMMON_DATA_MAP['VIEW_NODE'] = 'graceful-restart_prepare_ip'
    pass


@frr_gracefulrestart_prepare_ip_ospf.command('./	<cr>')
def frr_gracefulrestart_prepare_ip_ospf_cr():
    pass


@frr_gracefulrestart_prepare.group(cls=FRR_AbbreviationGroup, name='ipv6',)
def frr_gracefulrestart_prepare_ipv6(gracefulrestart_prepare_ipv6_='graceful-restart_prepare_ipv6'):
    """IPv6 information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_gracefulrestart_prepare_ipv6.name
    
    if 'VIEW_NODE|graceful-restart_prepare_ipv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ipv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ipv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ipv6'][key] = val
    
    # set VIEW_NODE -> graceful-restart_prepare_ipv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'graceful-restart_prepare_ipv6'
    pass


@frr_gracefulrestart_prepare_ipv6.group(cls=FRR_AbbreviationGroup, name='ospf', invoke_without_command=True)
def frr_gracefulrestart_prepare_ipv6_ospf(ospf_='ospf'):
    """Prepare to restart the OSPFv3 process"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_gracefulrestart_prepare_ipv6_ospf.name
    data_gen['ospf'] = ospf_='ospf'
    
    if 'VIEW_NODE|graceful-restart_prepare_ipv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ipv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ipv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|graceful-restart_prepare_ipv6'][key] = val
    
    # set VIEW_NODE -> graceful-restart_prepare_ipv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'graceful-restart_prepare_ipv6'
    pass


@frr_gracefulrestart_prepare_ipv6_ospf.command('./	<cr>')
def frr_gracefulrestart_prepare_ipv6_ospf_cr():
    pass

