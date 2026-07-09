import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='brief', invoke_without_command=True)
def frr_show_interface_brief(show_interface_brief_='show_interface_brief'):
    """Interface status and configuration summary"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_brief.name
    
    if 'VIEW_NODE|show_interface_brief' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_brief'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_brief']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_brief'][key] = val
    
    # set VIEW_NODE -> show_interface_brief table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_brief'
    pass


@frr_show_interface_brief.command('./	<cr>')
def frr_show_interface_brief_cr():
    pass


@frr_show_interface_brief.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_interface_brief_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_brief_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_interface_brief' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_brief'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_brief']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_brief'][key] = val
    
    # set VIEW_NODE -> show_interface_brief table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_brief'
    pass


@frr_show_interface_brief_json.command('./	<cr>')
def frr_show_interface_brief_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='description',)
def frr_show_interface_description():
    """Interface description"""
    global COMMON_DATA_MAP
    
    pass


@frr_show_interface_description.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_interface_description_vrf(show_interface_description_vrf_='show_interface_description_vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_description_vrf.name
    
    if 'VIEW_NODE|show_interface_description_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_description_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_description_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_description_vrf'][key] = val
    
    # set VIEW_NODE -> show_interface_description_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_description_vrf'
    pass


@frr_show_interface_description_vrf.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_interface_description_vrf_all(all_='all'):
    """All VRFs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_description_vrf_all.name
    data_gen['all'] = all_='all'
    
    if 'VIEW_NODE|show_interface_description_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_description_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_description_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_description_vrf'][key] = val
    
    # set VIEW_NODE -> show_interface_description_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_description_vrf'
    pass


@frr_show_interface_description_vrf_all.command('./	<cr>')
def frr_show_interface_description_vrf_all_cr():
    pass


@frr_show_interface_description_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['NAME']), invoke_without_command=True)
def frr_show_interface_description_vrf_thevrfname():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_description_vrf_thevrfname.name
    data_gen['THE_VRF_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_interface_description_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_description_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_description_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_description_vrf'][key] = val
    
    # set VIEW_NODE -> show_interface_description_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_description_vrf'
    pass


@frr_show_interface_description_vrf_thevrfname.command('./	<cr>')
def frr_show_interface_description_vrf_thevrfname_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(3, ['IFNAME']), invoke_without_command=True)
def frr_show_interface_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface'][key] = val
    
    # set VIEW_NODE -> show_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface'
    pass


@frr_show_interface_interfacename.command('./	<cr>')
def frr_show_interface_interfacename_cr():
    pass


@frr_show_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_interface_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface'][key] = val
    
    # set VIEW_NODE -> show_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface'
    pass


@frr_show_interface_interfacename_json.command('./	<cr>')
def frr_show_interface_interfacename_json_cr():
    pass


@frr_show_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_interface_interfacename_nexthopgroup(nexthopgroup_='nexthop-group'):
    """Show Nexthop Groups"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_interfacename_nexthopgroup.name
    data_gen['nexthop-group'] = nexthopgroup_='nexthop-group'
    
    if 'VIEW_NODE|show_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface'][key] = val
    
    # set VIEW_NODE -> show_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface'
    pass


@frr_show_interface_interfacename_nexthopgroup.command('./	<cr>')
def frr_show_interface_interfacename_nexthopgroup_cr():
    pass


@frr_show_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_interface_interfacename_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_interfacename_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface'][key] = val
    
    # set VIEW_NODE -> show_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface'
    pass


@frr_show_interface_interfacename_vrf.command('./	<cr>')
def frr_show_interface_interfacename_vrf_cr():
    pass


@frr_show_interface_interfacename_vrf.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_interface_interfacename_vrf_all(vrf_all_='vrf_all'):
    """All VRFs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_interfacename_vrf_all.name
    data_gen['vrf_all'] = vrf_all_='vrf_all'
    
    if 'VIEW_NODE|show_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface'][key] = val
    
    # set VIEW_NODE -> show_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface'
    pass


@frr_show_interface_interfacename_vrf_all.command('./	<cr>')
def frr_show_interface_interfacename_vrf_all_cr():
    pass


@frr_show_interface_interfacename_vrf_all.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_interface_interfacename_vrf_all_json(vrf_all_json_='vrf_all_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_interfacename_vrf_all_json.name
    data_gen['vrf_all_json'] = vrf_all_json_='vrf_all_json'
    
    if 'VIEW_NODE|show_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface'][key] = val
    
    # set VIEW_NODE -> show_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface'
    pass


@frr_show_interface_interfacename_vrf_all_json.command('./	<cr>')
def frr_show_interface_interfacename_vrf_all_json_cr():
    pass


@frr_show_interface_interfacename_vrf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_interface_interfacename_vrf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_interfacename_vrf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface'][key] = val
    
    # set VIEW_NODE -> show_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface'
    pass


@frr_show_interface_interfacename_vrf_json.command('./	<cr>')
def frr_show_interface_interfacename_vrf_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface'][key] = val
    
    # set VIEW_NODE -> show_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface'
    pass


@frr_show_interface_json.command('./	<cr>')
def frr_show_interface_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_interface_nexthopgroup(nexthopgroup_='nexthop-group'):
    """Show Nexthop Groups"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_nexthopgroup.name
    data_gen['nexthop-group'] = nexthopgroup_='nexthop-group'
    
    if 'VIEW_NODE|show_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface'][key] = val
    
    # set VIEW_NODE -> show_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface'
    pass


@frr_show_interface_nexthopgroup.command('./	<cr>')
def frr_show_interface_nexthopgroup_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_interface_vrf(the_vrf_name, show_interface_vrf_='show_interface_vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_vrf.name
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_interface_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf'][key] = val
    
    # set VIEW_NODE -> show_interface_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_vrf'
    pass


@frr_show_interface_vrf.command('./	<cr>')
def frr_show_interface_vrf_cr():
    pass


@frr_show_interface_vrf.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_interface_vrf_all(show_interface_vrf_all_='show_interface_vrf_all'):
    """All VRFs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_vrf_all.name
    
    if 'VIEW_NODE|show_interface_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_interface_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_vrf_all'
    pass


@frr_show_interface_vrf_all.command('./	<cr>')
def frr_show_interface_vrf_all_cr():
    pass


@frr_show_interface_vrf_all.group(cls=FRR_AbbreviationGroup, name='brief', invoke_without_command=True)
def frr_show_interface_vrf_all_brief(show_interface_vrf_all_brief_='show_interface_vrf_all_brief'):
    """Interface status and configuration summary"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_vrf_all_brief.name
    
    if 'VIEW_NODE|show_interface_vrf_all_brief' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all_brief'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all_brief']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all_brief'][key] = val
    
    # set VIEW_NODE -> show_interface_vrf_all_brief table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_vrf_all_brief'
    pass


@frr_show_interface_vrf_all_brief.command('./	<cr>')
def frr_show_interface_vrf_all_brief_cr():
    pass


@frr_show_interface_vrf_all_brief.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_interface_vrf_all_brief_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_vrf_all_brief_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_interface_vrf_all_brief' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all_brief'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all_brief']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all_brief'][key] = val
    
    # set VIEW_NODE -> show_interface_vrf_all_brief table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_vrf_all_brief'
    pass


@frr_show_interface_vrf_all_brief_json.command('./	<cr>')
def frr_show_interface_vrf_all_brief_json_cr():
    pass


@frr_show_interface_vrf_all.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_interface_vrf_all_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_vrf_all_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_interface_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_interface_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_vrf_all'
    pass


@frr_show_interface_vrf_all_json.command('./	<cr>')
def frr_show_interface_vrf_all_json_cr():
    pass


@frr_show_interface_vrf.group(cls=FRR_AbbreviationGroup, name='brief', invoke_without_command=True)
def frr_show_interface_vrf_brief(brief_='brief'):
    """Interface status and configuration summary"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_vrf_brief.name
    data_gen['brief'] = brief_='brief'
    
    if 'VIEW_NODE|show_interface_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf'][key] = val
    
    # set VIEW_NODE -> show_interface_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_vrf'
    pass


@frr_show_interface_vrf_brief.command('./	<cr>')
def frr_show_interface_vrf_brief_cr():
    pass


@frr_show_interface_vrf_brief.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_interface_vrf_brief_json(brief_json_='brief_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_vrf_brief_json.name
    data_gen['brief_json'] = brief_json_='brief_json'
    
    if 'VIEW_NODE|show_interface_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf'][key] = val
    
    # set VIEW_NODE -> show_interface_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_vrf'
    pass


@frr_show_interface_vrf_brief_json.command('./	<cr>')
def frr_show_interface_vrf_brief_json_cr():
    pass


@frr_show_interface_vrf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_interface_vrf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_interface_vrf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_interface_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_interface_vrf'][key] = val
    
    # set VIEW_NODE -> show_interface_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_interface_vrf'
    pass


@frr_show_interface_vrf_json.command('./	<cr>')
def frr_show_interface_vrf_json_cr():
    pass

