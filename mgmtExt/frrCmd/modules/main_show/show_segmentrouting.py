import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='srv6', invoke_without_command=True)
def frr_show_segmentrouting_srv6():
    """Segment Routing SRv6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_segmentrouting_srv6.name
    
    if 'VIEW_NODE|show_segment-routing_srv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6'][key] = val
    
    # set VIEW_NODE -> show_segment-routing_srv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_segment-routing_srv6'
    pass


@frr_show_segmentrouting_srv6.command('./	<cr>')
def frr_show_segmentrouting_srv6_cr():
    pass


@frr_show_segmentrouting_srv6.group(cls=FRR_AbbreviationGroup, name='locator', invoke_without_command=True)
def frr_show_segmentrouting_srv6_locator(show_segmentrouting_srv6_locator_='show_segment-routing_srv6_locator'):
    """Locator Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_segmentrouting_srv6_locator.name
    
    if 'VIEW_NODE|show_segment-routing_srv6_locator' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator'][key] = val
    
    # set VIEW_NODE -> show_segment-routing_srv6_locator table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_segment-routing_srv6_locator'
    pass


@frr_show_segmentrouting_srv6_locator.command('./	<cr>')
def frr_show_segmentrouting_srv6_locator_cr():
    pass


@frr_show_segmentrouting_srv6_locator.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_segmentrouting_srv6_locator_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_segmentrouting_srv6_locator_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_segment-routing_srv6_locator' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator'][key] = val
    
    # set VIEW_NODE -> show_segment-routing_srv6_locator table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_segment-routing_srv6_locator'
    pass


@frr_show_segmentrouting_srv6_locator_json.command('./	<cr>')
def frr_show_segmentrouting_srv6_locator_json_cr():
    pass


@frr_show_segmentrouting_srv6_locator.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['NAME']),)
def frr_show_segmentrouting_srv6_locator_locatorname():
    """4"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_segmentrouting_srv6_locator_locatorname.name
    data_gen['LOCATOR_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_segment-routing_srv6_locator' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator'][key] = val
    
    # set VIEW_NODE -> show_segment-routing_srv6_locator table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_segment-routing_srv6_locator'
    pass


@frr_show_segmentrouting_srv6_locator_locatorname.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_segmentrouting_srv6_locator_locatorname_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_segmentrouting_srv6_locator_locatorname_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_segment-routing_srv6_locator' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator'][key] = val
    
    # set VIEW_NODE -> show_segment-routing_srv6_locator table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_segment-routing_srv6_locator'
    pass


@frr_show_segmentrouting_srv6_locator_locatorname_detail.command('./	<cr>')
def frr_show_segmentrouting_srv6_locator_locatorname_detail_cr():
    pass


@frr_show_segmentrouting_srv6_locator_locatorname_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_segmentrouting_srv6_locator_locatorname_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_segmentrouting_srv6_locator_locatorname_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_segment-routing_srv6_locator' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_segment-routing_srv6_locator'][key] = val
    
    # set VIEW_NODE -> show_segment-routing_srv6_locator table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_segment-routing_srv6_locator'
    pass


@frr_show_segmentrouting_srv6_locator_locatorname_detail_json.command('./	<cr>')
def frr_show_segmentrouting_srv6_locator_locatorname_detail_json_cr():
    pass

