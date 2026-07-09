import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_pbr_interface(show_pbr_interface_='show_pbr_interface'):
    """PBR Interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_interface.name
    
    if 'VIEW_NODE|show_pbr_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface'][key] = val
    
    # set VIEW_NODE -> show_pbr_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_interface'
    pass


@frr_show_pbr_interface.command('./	<cr>')
def frr_show_pbr_interface_cr():
    pass


@frr_show_pbr_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_pbr_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_pbr_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface'][key] = val
    
    # set VIEW_NODE -> show_pbr_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_interface'
    pass


@frr_show_pbr_interface_json.command('./	<cr>')
def frr_show_pbr_interface_json_cr():
    pass


@frr_show_pbr_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['NAME']), invoke_without_command=True)
def frr_show_pbr_interface_pbrinterfacename():
    """PBR Interface Name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_interface_pbrinterfacename.name
    data_gen['PBR_INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_pbr_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface'][key] = val
    
    # set VIEW_NODE -> show_pbr_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_interface'
    pass


@frr_show_pbr_interface_pbrinterfacename.command('./	<cr>')
def frr_show_pbr_interface_pbrinterfacename_cr():
    pass


@frr_show_pbr_interface_pbrinterfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_pbr_interface_pbrinterfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_interface_pbrinterfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_pbr_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_interface'][key] = val
    
    # set VIEW_NODE -> show_pbr_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_interface'
    pass


@frr_show_pbr_interface_pbrinterfacename_json.command('./	<cr>')
def frr_show_pbr_interface_pbrinterfacename_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ipset', invoke_without_command=True)
def frr_show_pbr_ipset(show_pbr_ipset_='show_pbr_ipset'):
    """IPset Context information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_ipset.name
    
    if 'VIEW_NODE|show_pbr_ipset' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_ipset'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_ipset']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_ipset'][key] = val
    
    # set VIEW_NODE -> show_pbr_ipset table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_ipset'
    pass


@frr_show_pbr_ipset.command('./	<cr>')
def frr_show_pbr_ipset_cr():
    pass


@frr_show_pbr_ipset.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['WORD']), invoke_without_command=True)
def frr_show_pbr_ipset_ipsetnameinformation():
    """IPset Name information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_ipset_ipsetnameinformation.name
    data_gen['IPSET_NAME_INFORMATION'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_pbr_ipset' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_ipset'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_ipset']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_ipset'][key] = val
    
    # set VIEW_NODE -> show_pbr_ipset table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_ipset'
    pass


@frr_show_pbr_ipset_ipsetnameinformation.command('./	<cr>')
def frr_show_pbr_ipset_ipsetnameinformation_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='iptable', invoke_without_command=True)
def frr_show_pbr_iptable(show_pbr_iptable_='show_pbr_iptable'):
    """IPtable Context information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_iptable.name
    
    if 'VIEW_NODE|show_pbr_iptable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_iptable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_iptable']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_iptable'][key] = val
    
    # set VIEW_NODE -> show_pbr_iptable table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_iptable'
    pass


@frr_show_pbr_iptable.command('./	<cr>')
def frr_show_pbr_iptable_cr():
    pass


@frr_show_pbr_iptable.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['WORD']), invoke_without_command=True)
def frr_show_pbr_iptable_iptablenameinformation():
    """IPtable Name information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_iptable_iptablenameinformation.name
    data_gen['IPTABLE_NAME_INFORMATION'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_pbr_iptable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_iptable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_iptable']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_iptable'][key] = val
    
    # set VIEW_NODE -> show_pbr_iptable table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_iptable'
    pass


@frr_show_pbr_iptable_iptablenameinformation.command('./	<cr>')
def frr_show_pbr_iptable_iptablenameinformation_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='map', invoke_without_command=True)
def frr_show_pbr_map(show_pbr_map_='show_pbr_map'):
    """PBR Map"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_map.name
    
    if 'VIEW_NODE|show_pbr_map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'][key] = val
    
    # set VIEW_NODE -> show_pbr_map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_map'
    pass


@frr_show_pbr_map.command('./	<cr>')
def frr_show_pbr_map_cr():
    pass


@frr_show_pbr_map.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_pbr_map_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_map_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_pbr_map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'][key] = val
    
    # set VIEW_NODE -> show_pbr_map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_map'
    pass


@frr_show_pbr_map_detail.command('./	<cr>')
def frr_show_pbr_map_detail_cr():
    pass


@frr_show_pbr_map.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_pbr_map_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_map_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_pbr_map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'][key] = val
    
    # set VIEW_NODE -> show_pbr_map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_map'
    pass


@frr_show_pbr_map_json.command('./	<cr>')
def frr_show_pbr_map_json_cr():
    pass


@frr_show_pbr_map.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['NAME']), invoke_without_command=True)
def frr_show_pbr_map_pbrmapname():
    """PBR Map Name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_map_pbrmapname.name
    data_gen['PBR_MAP_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_pbr_map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'][key] = val
    
    # set VIEW_NODE -> show_pbr_map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_map'
    pass


@frr_show_pbr_map_pbrmapname.command('./	<cr>')
def frr_show_pbr_map_pbrmapname_cr():
    pass


@frr_show_pbr_map_pbrmapname.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_pbr_map_pbrmapname_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_map_pbrmapname_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_pbr_map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'][key] = val
    
    # set VIEW_NODE -> show_pbr_map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_map'
    pass


@frr_show_pbr_map_pbrmapname_detail.command('./	<cr>')
def frr_show_pbr_map_pbrmapname_detail_cr():
    pass


@frr_show_pbr_map_pbrmapname.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_pbr_map_pbrmapname_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_map_pbrmapname_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_pbr_map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_map'][key] = val
    
    # set VIEW_NODE -> show_pbr_map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_map'
    pass


@frr_show_pbr_map_pbrmapname_json.command('./	<cr>')
def frr_show_pbr_map_pbrmapname_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='nexthop-groups', invoke_without_command=True)
def frr_show_pbr_nexthopgroups(show_pbr_nexthopgroups_='show_pbr_nexthop-groups'):
    """Nexthop Groups"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_nexthopgroups.name
    
    if 'VIEW_NODE|show_pbr_nexthop-groups' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups'][key] = val
    
    # set VIEW_NODE -> show_pbr_nexthop-groups table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_nexthop-groups'
    pass


@frr_show_pbr_nexthopgroups.command('./	<cr>')
def frr_show_pbr_nexthopgroups_cr():
    pass


@frr_show_pbr_nexthopgroups.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_pbr_nexthopgroups_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_nexthopgroups_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_pbr_nexthop-groups' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups'][key] = val
    
    # set VIEW_NODE -> show_pbr_nexthop-groups table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_nexthop-groups'
    pass


@frr_show_pbr_nexthopgroups_json.command('./	<cr>')
def frr_show_pbr_nexthopgroups_json_cr():
    pass


@frr_show_pbr_nexthopgroups.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['WORD']), invoke_without_command=True)
def frr_show_pbr_nexthopgroups_optionalnameofthe():
    """Optional Name of the nexthop group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_nexthopgroups_optionalnameofthe.name
    data_gen['OPTIONAL_NAME_OF_THE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_pbr_nexthop-groups' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups'][key] = val
    
    # set VIEW_NODE -> show_pbr_nexthop-groups table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_nexthop-groups'
    pass


@frr_show_pbr_nexthopgroups_optionalnameofthe.command('./	<cr>')
def frr_show_pbr_nexthopgroups_optionalnameofthe_cr():
    pass


@frr_show_pbr_nexthopgroups_optionalnameofthe.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_pbr_nexthopgroups_optionalnameofthe_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_nexthopgroups_optionalnameofthe_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_pbr_nexthop-groups' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr_nexthop-groups'][key] = val
    
    # set VIEW_NODE -> show_pbr_nexthop-groups table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr_nexthop-groups'
    pass


@frr_show_pbr_nexthopgroups_optionalnameofthe_json.command('./	<cr>')
def frr_show_pbr_nexthopgroups_optionalnameofthe_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='rule', invoke_without_command=True)
def frr_show_pbr_rule(rule_='rule'):
    """Rule"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_pbr_rule.name
    data_gen['rule'] = rule_='rule'
    
    if 'VIEW_NODE|show_pbr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_pbr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_pbr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_pbr'][key] = val
    
    # set VIEW_NODE -> show_pbr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_pbr'
    pass


@frr_show_pbr_rule.command('./	<cr>')
def frr_show_pbr_rule_cr():
    pass

