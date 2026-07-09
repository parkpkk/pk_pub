import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='ip', invoke_without_command=True)
@click.argument('trace_route_to_destination', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_traceroute_ip(trace_route_to_destination, ip_='ip'):
    """IP trace"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_traceroute_ip.name
    data_gen['ip'] = ip_='ip'
    data_gen['TRACE_ROUTE_TO_DESTINATION'] = trace_route_to_destination
    
    if 'VIEW_NODE|traceroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|traceroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|traceroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|traceroute'][key] = val
    
    # set VIEW_NODE -> traceroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'traceroute'
    pass


@frr_traceroute_ip.command('./	<cr>')
def frr_traceroute_ip_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ipv6', invoke_without_command=True)
@click.argument('trace_route_to_destination', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_traceroute_ipv6(trace_route_to_destination, ipv6_='ipv6'):
    """IPv6 trace"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_traceroute_ipv6.name
    data_gen['ipv6'] = ipv6_='ipv6'
    data_gen['TRACE_ROUTE_TO_DESTINATION'] = trace_route_to_destination
    
    if 'VIEW_NODE|traceroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|traceroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|traceroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|traceroute'][key] = val
    
    # set VIEW_NODE -> traceroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'traceroute'
    pass


@frr_traceroute_ipv6.command('./	<cr>')
def frr_traceroute_ipv6_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(2, ['WORD']), invoke_without_command=True)
def frr_traceroute_traceroutetodestination():
    """Trace route to destination address or hostname"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_traceroute_traceroutetodestination.name
    data_gen['TRACE_ROUTE_TO_DESTINATION'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|traceroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|traceroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|traceroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|traceroute'][key] = val
    
    # set VIEW_NODE -> traceroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'traceroute'
    pass


@frr_traceroute_traceroutetodestination.command('./	<cr>')
def frr_traceroute_traceroutetodestination_cr():
    pass

