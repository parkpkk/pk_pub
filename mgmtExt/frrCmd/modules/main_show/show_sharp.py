import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='cspf',)
def frr_show_sharp_cspf(show_sharp_cspf_='show_sharp_cspf'):
    """Constraint Shortest Path First path computation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_cspf.name
    
    if 'VIEW_NODE|show_sharp_cspf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'][key] = val
    
    # set VIEW_NODE -> show_sharp_cspf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_cspf'
    pass


@frr_show_sharp_cspf.group(cls=FRR_AbbreviationGroup, name='source',)
def frr_show_sharp_cspf_source(source_='source'):
    """Source of the path"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_cspf_source.name
    data_gen['source'] = source_='source'
    
    if 'VIEW_NODE|show_sharp_cspf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'][key] = val
    
    # set VIEW_NODE -> show_sharp_cspf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_cspf'
    pass


@frr_show_sharp_cspf_source.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D', 'X:X::X:X']),)
def frr_show_sharp_cspf_source_sourceipaddress():
    """4"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_cspf_source_sourceipaddress.name
    data_gen['SOURCE_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_sharp_cspf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'][key] = val
    
    # set VIEW_NODE -> show_sharp_cspf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_cspf'
    pass


@frr_show_sharp_cspf_source_sourceipaddress.group(cls=FRR_AbbreviationGroup, name='destination',)
def frr_show_sharp_cspf_source_sourceipaddress_destination(destination_='destination'):
    """Destination of the path"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_cspf_source_sourceipaddress_destination.name
    data_gen['destination'] = destination_='destination'
    
    if 'VIEW_NODE|show_sharp_cspf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'][key] = val
    
    # set VIEW_NODE -> show_sharp_cspf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_cspf'
    pass


@frr_show_sharp_cspf_source_sourceipaddress_destination.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D', 'X:X::X:X']),)
def frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress.name
    data_gen['DESTINATION_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_sharp_cspf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'][key] = val
    
    # set VIEW_NODE -> show_sharp_cspf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_cspf'
    pass


@frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['metric', 'te-metric', 'delay']), invoke_without_command=True)
@click.argument('value_of_maximum_cost', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress_destinationipaddresschoicecase(value_of_maximum_cost):
    """Maximum Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress_destinationipaddresschoicecase.name
    data_gen['DESTINATION-IP-ADDRESS_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    data_gen['VALUE_OF_MAXIMUM_COST'] = value_of_maximum_cost
    
    if 'VIEW_NODE|show_sharp_cspf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'][key] = val
    
    # set VIEW_NODE -> show_sharp_cspf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_cspf'
    pass


@frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress_destinationipaddresschoicecase.command('./	<cr>')
def frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress_destinationipaddresschoicecase_cr():
    pass


@frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress_destinationipaddresschoicecase.group(cls=FRR_AbbreviationGroup, name='rsv-bw', invoke_without_command=True)
@click.argument('class_of_service_or', metavar='(0-7)', required=True, type=FRR_TYPE((0, 7)))
@click.argument('bytessecond', metavar='BANDWIDTH', required=True, type=FRR_TYPE('BANDWIDTH'))
def frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress_destinationipaddresschoicecase_rsvbw(bytessecond, class_of_service_or, rsvbw_='rsv-bw'):
    """Reserved Bandwidth of this path"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress_destinationipaddresschoicecase_rsvbw.name
    data_gen['rsv-bw'] = rsvbw_='rsv-bw'
    data_gen['CLASS_OF_SERVICE_OR'] = class_of_service_or
    data_gen['BYTESSECOND'] = bytessecond
    
    if 'VIEW_NODE|show_sharp_cspf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_cspf'][key] = val
    
    # set VIEW_NODE -> show_sharp_cspf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_cspf'
    pass


@frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress_destinationipaddresschoicecase_rsvbw.command('./	<cr>')
def frr_show_sharp_cspf_source_sourceipaddress_destination_destinationipaddress_destinationipaddresschoicecase_rsvbw_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='segment-routing', invoke_without_command=True)
def frr_show_sharp_segmentrouting():
    """Segment-Routing"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_segmentrouting.name
    
    if 'VIEW_NODE|show_sharp_segment-routing' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_segment-routing'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_segment-routing']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_segment-routing'][key] = val
    
    # set VIEW_NODE -> show_sharp_segment-routing table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_segment-routing'
    pass


@frr_show_sharp_segmentrouting.command('./	<cr>')
def frr_show_sharp_segmentrouting_cr():
    pass


@frr_show_sharp_segmentrouting.group(cls=FRR_AbbreviationGroup, name='srv6', invoke_without_command=True)
def frr_show_sharp_segmentrouting_srv6(show_sharp_segmentrouting_srv6_='show_sharp_segment-routing_srv6'):
    """Segment-Routing IPv6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_segmentrouting_srv6.name
    
    if 'VIEW_NODE|show_sharp_segment-routing_srv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_segment-routing_srv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_segment-routing_srv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_segment-routing_srv6'][key] = val
    
    # set VIEW_NODE -> show_sharp_segment-routing_srv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_segment-routing_srv6'
    pass


@frr_show_sharp_segmentrouting_srv6.command('./	<cr>')
def frr_show_sharp_segmentrouting_srv6_cr():
    pass


@frr_show_sharp_segmentrouting_srv6.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_sharp_segmentrouting_srv6_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_segmentrouting_srv6_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_sharp_segment-routing_srv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_segment-routing_srv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_segment-routing_srv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_segment-routing_srv6'][key] = val
    
    # set VIEW_NODE -> show_sharp_segment-routing_srv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_segment-routing_srv6'
    pass


@frr_show_sharp_segmentrouting_srv6_json.command('./	<cr>')
def frr_show_sharp_segmentrouting_srv6_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ted', invoke_without_command=True)
def frr_show_sharp_ted(show_sharp_ted_='show_sharp_ted'):
    """Traffic Engineering Database"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted.name
    
    if 'VIEW_NODE|show_sharp_ted' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted'
    pass


@frr_show_sharp_ted.command('./	<cr>')
def frr_show_sharp_ted_cr():
    pass


@frr_show_sharp_ted.group(cls=FRR_AbbreviationGroup, name='edge', invoke_without_command=True)
def frr_show_sharp_ted_edge(show_sharp_ted_edge_='show_sharp_ted_edge'):
    """MPLS-TE Edge"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_edge.name
    
    if 'VIEW_NODE|show_sharp_ted_edge' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_edge table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_edge'
    pass


@frr_show_sharp_ted_edge.command('./	<cr>')
def frr_show_sharp_ted_edge_cr():
    pass


@frr_show_sharp_ted_edge.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_sharp_ted_edge_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_edge_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_sharp_ted_edge' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_edge table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_edge'
    pass


@frr_show_sharp_ted_edge_json.command('./	<cr>')
def frr_show_sharp_ted_edge_json_cr():
    pass


@frr_show_sharp_ted_edge.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D']), invoke_without_command=True)
def frr_show_sharp_ted_edge_mplsteedgeidv4():
    """MPLS-TE Edge ID (as an IP address)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_edge_mplsteedgeidv4.name
    data_gen['MPLS-TE_EDGE_ID_V4'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_sharp_ted_edge' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_edge table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_edge'
    pass


@frr_show_sharp_ted_edge_mplsteedgeidv4.command('./	<cr>')
def frr_show_sharp_ted_edge_mplsteedgeidv4_cr():
    pass


@frr_show_sharp_ted_edge_mplsteedgeidv4.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_sharp_ted_edge_mplsteedgeidv4_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_edge_mplsteedgeidv4_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_sharp_ted_edge' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_edge table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_edge'
    pass


@frr_show_sharp_ted_edge_mplsteedgeidv4_json.command('./	<cr>')
def frr_show_sharp_ted_edge_mplsteedgeidv4_json_cr():
    pass


@frr_show_sharp_ted_edge_mplsteedgeidv4.group(cls=FRR_AbbreviationGroup, name='verbose', invoke_without_command=True)
def frr_show_sharp_ted_edge_mplsteedgeidv4_verbose(verbose_='verbose'):
    """Verbose output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_edge_mplsteedgeidv4_verbose.name
    data_gen['verbose'] = verbose_='verbose'
    
    if 'VIEW_NODE|show_sharp_ted_edge' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_edge table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_edge'
    pass


@frr_show_sharp_ted_edge_mplsteedgeidv4_verbose.command('./	<cr>')
def frr_show_sharp_ted_edge_mplsteedgeidv4_verbose_cr():
    pass


@frr_show_sharp_ted_edge.group(cls=FRR_AbbreviationGroup, name='verbose', invoke_without_command=True)
def frr_show_sharp_ted_edge_verbose(verbose_='verbose'):
    """Verbose output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_edge_verbose.name
    data_gen['verbose'] = verbose_='verbose'
    
    if 'VIEW_NODE|show_sharp_ted_edge' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_edge'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_edge table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_edge'
    pass


@frr_show_sharp_ted_edge_verbose.command('./	<cr>')
def frr_show_sharp_ted_edge_verbose_cr():
    pass


@frr_show_sharp_ted.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_sharp_ted_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_sharp_ted' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted'
    pass


@frr_show_sharp_ted_json.command('./	<cr>')
def frr_show_sharp_ted_json_cr():
    pass


@frr_show_sharp_ted.group(cls=FRR_AbbreviationGroup, name='subnet', invoke_without_command=True)
def frr_show_sharp_ted_subnet(show_sharp_ted_subnet_='show_sharp_ted_subnet'):
    """MPLS-TE Subnet"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_subnet.name
    
    if 'VIEW_NODE|show_sharp_ted_subnet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_subnet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_subnet'
    pass


@frr_show_sharp_ted_subnet.command('./	<cr>')
def frr_show_sharp_ted_subnet_cr():
    pass


@frr_show_sharp_ted_subnet.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D/M']), invoke_without_command=True)
def frr_show_sharp_ted_subnet_ipprefix():
    """MPLS-TE Subnet ID (as an IP prefix)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_subnet_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_sharp_ted_subnet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_subnet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_subnet'
    pass


@frr_show_sharp_ted_subnet_ipprefix.command('./	<cr>')
def frr_show_sharp_ted_subnet_ipprefix_cr():
    pass


@frr_show_sharp_ted_subnet_ipprefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_sharp_ted_subnet_ipprefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_subnet_ipprefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_sharp_ted_subnet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_subnet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_subnet'
    pass


@frr_show_sharp_ted_subnet_ipprefix_json.command('./	<cr>')
def frr_show_sharp_ted_subnet_ipprefix_json_cr():
    pass


@frr_show_sharp_ted_subnet_ipprefix.group(cls=FRR_AbbreviationGroup, name='verbose', invoke_without_command=True)
def frr_show_sharp_ted_subnet_ipprefix_verbose(verbose_='verbose'):
    """Verbose output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_subnet_ipprefix_verbose.name
    data_gen['verbose'] = verbose_='verbose'
    
    if 'VIEW_NODE|show_sharp_ted_subnet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_subnet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_subnet'
    pass


@frr_show_sharp_ted_subnet_ipprefix_verbose.command('./	<cr>')
def frr_show_sharp_ted_subnet_ipprefix_verbose_cr():
    pass


@frr_show_sharp_ted_subnet.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_sharp_ted_subnet_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_subnet_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_sharp_ted_subnet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_subnet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_subnet'
    pass


@frr_show_sharp_ted_subnet_json.command('./	<cr>')
def frr_show_sharp_ted_subnet_json_cr():
    pass


@frr_show_sharp_ted_subnet.group(cls=FRR_AbbreviationGroup, name='verbose', invoke_without_command=True)
def frr_show_sharp_ted_subnet_verbose(verbose_='verbose'):
    """Verbose output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_subnet_verbose.name
    data_gen['verbose'] = verbose_='verbose'
    
    if 'VIEW_NODE|show_sharp_ted_subnet' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_subnet'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_subnet table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_subnet'
    pass


@frr_show_sharp_ted_subnet_verbose.command('./	<cr>')
def frr_show_sharp_ted_subnet_verbose_cr():
    pass


@frr_show_sharp_ted.group(cls=FRR_AbbreviationGroup, name='verbose', invoke_without_command=True)
def frr_show_sharp_ted_verbose(verbose_='verbose'):
    """Verbose output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_verbose.name
    data_gen['verbose'] = verbose_='verbose'
    
    if 'VIEW_NODE|show_sharp_ted' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted'
    pass


@frr_show_sharp_ted_verbose.command('./	<cr>')
def frr_show_sharp_ted_verbose_cr():
    pass


@frr_show_sharp_ted.group(cls=FRR_AbbreviationGroup, name='vertex', invoke_without_command=True)
def frr_show_sharp_ted_vertex(show_sharp_ted_vertex_='show_sharp_ted_vertex'):
    """MPLS-TE Vertex"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_vertex.name
    
    if 'VIEW_NODE|show_sharp_ted_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_vertex'
    pass


@frr_show_sharp_ted_vertex.command('./	<cr>')
def frr_show_sharp_ted_vertex_cr():
    pass


@frr_show_sharp_ted_vertex.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_sharp_ted_vertex_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_vertex_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_sharp_ted_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_vertex'
    pass


@frr_show_sharp_ted_vertex_json.command('./	<cr>')
def frr_show_sharp_ted_vertex_json_cr():
    pass


@frr_show_sharp_ted_vertex.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D']), invoke_without_command=True)
def frr_show_sharp_ted_vertex_mplsterouterid():
    """MPLS-TE router ID (as an IP address)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_vertex_mplsterouterid.name
    data_gen['MPLS-TE_ROUTER_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_sharp_ted_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_vertex'
    pass


@frr_show_sharp_ted_vertex_mplsterouterid.command('./	<cr>')
def frr_show_sharp_ted_vertex_mplsterouterid_cr():
    pass


@frr_show_sharp_ted_vertex_mplsterouterid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_sharp_ted_vertex_mplsterouterid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_vertex_mplsterouterid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_sharp_ted_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_vertex'
    pass


@frr_show_sharp_ted_vertex_mplsterouterid_json.command('./	<cr>')
def frr_show_sharp_ted_vertex_mplsterouterid_json_cr():
    pass


@frr_show_sharp_ted_vertex_mplsterouterid.group(cls=FRR_AbbreviationGroup, name='verbose', invoke_without_command=True)
def frr_show_sharp_ted_vertex_mplsterouterid_verbose(verbose_='verbose'):
    """Verbose output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_vertex_mplsterouterid_verbose.name
    data_gen['verbose'] = verbose_='verbose'
    
    if 'VIEW_NODE|show_sharp_ted_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_vertex'
    pass


@frr_show_sharp_ted_vertex_mplsterouterid_verbose.command('./	<cr>')
def frr_show_sharp_ted_vertex_mplsterouterid_verbose_cr():
    pass


@frr_show_sharp_ted_vertex.group(cls=FRR_AbbreviationGroup, name='verbose', invoke_without_command=True)
def frr_show_sharp_ted_vertex_verbose(verbose_='verbose'):
    """Verbose output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_sharp_ted_vertex_verbose.name
    data_gen['verbose'] = verbose_='verbose'
    
    if 'VIEW_NODE|show_sharp_ted_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sharp_ted_vertex'][key] = val
    
    # set VIEW_NODE -> show_sharp_ted_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sharp_ted_vertex'
    pass


@frr_show_sharp_ted_vertex_verbose.command('./	<cr>')
def frr_show_sharp_ted_vertex_verbose_cr():
    pass

