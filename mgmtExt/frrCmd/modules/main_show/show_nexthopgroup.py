import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='rib', invoke_without_command=True)
def frr_show_nexthopgroup_rib(show_nexthopgroup_rib_='show_nexthop-group_rib'):
    """RIB information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib.name
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib.command('./	<cr>')
def frr_show_nexthopgroup_rib_cr():
    pass


@frr_show_nexthopgroup_rib.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['kernel', 'zebra', 'bgp', 'sharp']), invoke_without_command=True)
def frr_show_nexthopgroup_rib_choicecase():
    """Kernel (not installed via the zebra RIB)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_choicecase.command('./	<cr>')
def frr_show_nexthopgroup_rib_choicecase_cr():
    pass


@frr_show_nexthopgroup_rib_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_nexthopgroup_rib_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_choicecase_json.command('./	<cr>')
def frr_show_nexthopgroup_rib_choicecase_json_cr():
    pass


@frr_show_nexthopgroup_rib_choicecase.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_nexthopgroup_rib_choicecase_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_choicecase_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_choicecase_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['NAME', 'all']), invoke_without_command=True)
def frr_show_nexthopgroup_rib_choicecase_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_choicecase_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_choicecase_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_nexthopgroup_rib_choicecase_vrf_vrfchoicecase_cr():
    pass


@frr_show_nexthopgroup_rib_choicecase_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_nexthopgroup_rib_choicecase_vrf_vrfchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_choicecase_vrf_vrfchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_choicecase_vrf_vrfchoicecase_json.command('./	<cr>')
def frr_show_nexthopgroup_rib_choicecase_vrf_vrfchoicecase_json_cr():
    pass


@frr_show_nexthopgroup_rib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_nexthopgroup_rib_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_json.command('./	<cr>')
def frr_show_nexthopgroup_rib_json_cr():
    pass


@frr_show_nexthopgroup_rib.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, [(0, 4294967295)]), invoke_without_command=True)
def frr_show_nexthopgroup_rib_nexthopgroupid():
    """Nexthop Group ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_nexthopgroupid.name
    data_gen['NEXTHOP_GROUP_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_nexthopgroupid.command('./	<cr>')
def frr_show_nexthopgroup_rib_nexthopgroupid_cr():
    pass


@frr_show_nexthopgroup_rib_nexthopgroupid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_nexthopgroup_rib_nexthopgroupid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_nexthopgroupid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_nexthopgroupid_json.command('./	<cr>')
def frr_show_nexthopgroup_rib_nexthopgroupid_json_cr():
    pass


@frr_show_nexthopgroup_rib.group(cls=FRR_AbbreviationGroup, name='singleton',)
def frr_show_nexthopgroup_rib_singleton(singleton_='singleton'):
    """Show Singleton Nexthop-Groups"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton.name
    data_gen['singleton'] = singleton_='singleton'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['ip', 'ipv6']), invoke_without_command=True)
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward():
    """IP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton_singletonlabelforward.name
    data_gen['SINGLETON_LABEL_FORWARD'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward.command('./	<cr>')
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_cr():
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['kernel', 'zebra', 'bgp', 'sharp']), invoke_without_command=True)
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase():
    """Kernel (not installed via the zebra RIB)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase.command('./	<cr>')
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_cr():
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_json.command('./	<cr>')
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_json_cr():
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['NAME', 'all']), invoke_without_command=True)
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf_vrfchoicecase_cr():
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf_vrfchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf_vrfchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf_vrfchoicecase_json.command('./	<cr>')
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_choicecase_vrf_vrfchoicecase_json_cr():
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton_singletonlabelforward_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_json.command('./	<cr>')
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_json_cr():
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['NAME', 'all']), invoke_without_command=True)
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf_vrfchoicecase_cr():
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf_vrfchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf_vrfchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf_vrfchoicecase_json.command('./	<cr>')
def frr_show_nexthopgroup_rib_singleton_singletonlabelforward_vrf_vrfchoicecase_json_cr():
    pass


@frr_show_nexthopgroup_rib.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_nexthopgroup_rib_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['NAME', 'all']), invoke_without_command=True)
def frr_show_nexthopgroup_rib_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_nexthopgroup_rib_vrf_vrfchoicecase_cr():
    pass


@frr_show_nexthopgroup_rib_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_nexthopgroup_rib_vrf_vrfchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_nexthopgroup_rib_vrf_vrfchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_nexthop-group_rib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_nexthop-group_rib'][key] = val
    
    # set VIEW_NODE -> show_nexthop-group_rib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_nexthop-group_rib'
    pass


@frr_show_nexthopgroup_rib_vrf_vrfchoicecase_json.command('./	<cr>')
def frr_show_nexthopgroup_rib_vrf_vrfchoicecase_json_cr():
    pass

