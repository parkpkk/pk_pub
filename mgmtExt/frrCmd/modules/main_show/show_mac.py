import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='access-list', invoke_without_command=True)
def frr_show_mac_accesslist(show_mac_accesslist_='show_mac_access-list'):
    """List mac access lists"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mac_accesslist.name
    
    if 'VIEW_NODE|show_mac_access-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mac_access-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mac_access-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mac_access-list'][key] = val
    
    # set VIEW_NODE -> show_mac_access-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mac_access-list'
    pass


@frr_show_mac_accesslist.command('./	<cr>')
def frr_show_mac_accesslist_cr():
    pass


@frr_show_mac_accesslist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['ACCESSLIST_MAC_NAME']), invoke_without_command=True)
def frr_show_mac_accesslist_macaddress():
    """mac address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mac_accesslist_macaddress.name
    data_gen['MAC_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_mac_access-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mac_access-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mac_access-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mac_access-list'][key] = val
    
    # set VIEW_NODE -> show_mac_access-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mac_access-list'
    pass


@frr_show_mac_accesslist_macaddress.command('./	<cr>')
def frr_show_mac_accesslist_macaddress_cr():
    pass

