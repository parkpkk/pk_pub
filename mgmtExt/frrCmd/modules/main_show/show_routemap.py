import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_routemap_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_routemap_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_route-map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_route-map'][key] = val
    
    # set VIEW_NODE -> show_route-map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_route-map'
    pass


@frr_show_routemap_json.command('./	<cr>')
def frr_show_routemap_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(3, ['WORD']), invoke_without_command=True)
def frr_show_routemap_routemapname():
    """route-map name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_routemap_routemapname.name
    data_gen['ROUTE-MAP_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_route-map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_route-map'][key] = val
    
    # set VIEW_NODE -> show_route-map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_route-map'
    pass


@frr_show_routemap_routemapname.command('./	<cr>')
def frr_show_routemap_routemapname_cr():
    pass


@frr_show_routemap_routemapname.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_routemap_routemapname_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_routemap_routemapname_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_route-map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_route-map'][key] = val
    
    # set VIEW_NODE -> show_route-map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_route-map'
    pass


@frr_show_routemap_routemapname_json.command('./	<cr>')
def frr_show_routemap_routemapname_json_cr():
    pass


@frr_show_routemap_routemapname.group(cls=FRR_AbbreviationGroup, name='prefix-table', invoke_without_command=True)
def frr_show_routemap_routemapname_prefixtable(prefixtable_='prefix-table'):
    """internal prefix-table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_routemap_routemapname_prefixtable.name
    data_gen['prefix-table'] = prefixtable_='prefix-table'
    
    if 'VIEW_NODE|show_route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_route-map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_route-map'][key] = val
    
    # set VIEW_NODE -> show_route-map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_route-map'
    pass


@frr_show_routemap_routemapname_prefixtable.command('./	<cr>')
def frr_show_routemap_routemapname_prefixtable_cr():
    pass

