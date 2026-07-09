import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='ip', invoke_without_command=True)
@click.argument('ping_destination_address_or', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_ping_ip(ping_destination_address_or, ip_='ip'):
    """IP echo"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_ping_ip.name
    data_gen['ip'] = ip_='ip'
    data_gen['PING_DESTINATION_ADDRESS_OR'] = ping_destination_address_or
    
    if 'VIEW_NODE|ping' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|ping'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|ping']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|ping'][key] = val
    
    # set VIEW_NODE -> ping table
    COMMON_DATA_MAP['VIEW_NODE'] = 'ping'
    pass


@frr_ping_ip.command('./	<cr>')
def frr_ping_ip_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ipv6', invoke_without_command=True)
@click.argument('ping_destination_address_or', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_ping_ipv6(ping_destination_address_or, ipv6_='ipv6'):
    """IPv6 echo"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_ping_ipv6.name
    data_gen['ipv6'] = ipv6_='ipv6'
    data_gen['PING_DESTINATION_ADDRESS_OR'] = ping_destination_address_or
    
    if 'VIEW_NODE|ping' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|ping'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|ping']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|ping'][key] = val
    
    # set VIEW_NODE -> ping table
    COMMON_DATA_MAP['VIEW_NODE'] = 'ping'
    pass


@frr_ping_ipv6.command('./	<cr>')
def frr_ping_ipv6_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(2, ['WORD']), invoke_without_command=True)
def frr_ping_pingdestinationaddressor():
    """Ping destination address or hostname"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_ping_pingdestinationaddressor.name
    data_gen['PING_DESTINATION_ADDRESS_OR'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|ping' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|ping'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|ping']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|ping'][key] = val
    
    # set VIEW_NODE -> ping table
    COMMON_DATA_MAP['VIEW_NODE'] = 'ping'
    pass


@frr_ping_pingdestinationaddressor.command('./	<cr>')
def frr_ping_pingdestinationaddressor_cr():
    pass

