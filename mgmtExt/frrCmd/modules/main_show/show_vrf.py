import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(3, ['NAME', 'all']),)
def frr_show_vrf_choicecase():
    """2"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrf_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrf'][key] = val
    
    # set VIEW_NODE -> show_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrf'
    pass


@frr_show_vrf_choicecase.group(cls=FRR_AbbreviationGroup, name='vni', invoke_without_command=True)
def frr_show_vrf_choicecase_vni(vni_='vni'):
    """VNI"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrf_choicecase_vni.name
    data_gen['vni'] = vni_='vni'
    
    if 'VIEW_NODE|show_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrf'][key] = val
    
    # set VIEW_NODE -> show_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrf'
    pass


@frr_show_vrf_choicecase_vni.command('./	<cr>')
def frr_show_vrf_choicecase_vni_cr():
    pass


@frr_show_vrf_choicecase_vni.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_vrf_choicecase_vni_json(vni_json_='vni_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrf_choicecase_vni_json.name
    data_gen['vni_json'] = vni_json_='vni_json'
    
    if 'VIEW_NODE|show_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrf'][key] = val
    
    # set VIEW_NODE -> show_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrf'
    pass


@frr_show_vrf_choicecase_vni_json.command('./	<cr>')
def frr_show_vrf_choicecase_vni_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vni', invoke_without_command=True)
def frr_show_vrf_vni(show_vrf_vni_='show_vrf_vni'):
    """VNI"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrf_vni.name
    
    if 'VIEW_NODE|show_vrf_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrf_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrf_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrf_vni'][key] = val
    
    # set VIEW_NODE -> show_vrf_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrf_vni'
    pass


@frr_show_vrf_vni.command('./	<cr>')
def frr_show_vrf_vni_cr():
    pass


@frr_show_vrf_vni.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_vrf_vni_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vrf_vni_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_vrf_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vrf_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vrf_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vrf_vni'][key] = val
    
    # set VIEW_NODE -> show_vrf_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vrf_vni'
    pass


@frr_show_vrf_vni_json.command('./	<cr>')
def frr_show_vrf_vni_json_cr():
    pass

