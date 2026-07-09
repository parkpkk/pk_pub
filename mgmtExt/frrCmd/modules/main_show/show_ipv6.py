import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='access-list', invoke_without_command=True)
def frr_show_ipv6_accesslist(show_ipv6_accesslist_='show_ipv6_access-list'):
    """List IPv6 access lists"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_accesslist.name
    
    if 'VIEW_NODE|show_ipv6_access-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_access-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_access-list'
    pass


@frr_show_ipv6_accesslist.command('./	<cr>')
def frr_show_ipv6_accesslist_cr():
    pass


@frr_show_ipv6_accesslist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['ACCESSLIST6_NAME']), invoke_without_command=True)
def frr_show_ipv6_accesslist_ipv6accesslistname():
    """IPv6 access-list name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_accesslist_ipv6accesslistname.name
    data_gen['IPV6_ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_access-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_access-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_access-list'
    pass


@frr_show_ipv6_accesslist_ipv6accesslistname.command('./	<cr>')
def frr_show_ipv6_accesslist_ipv6accesslistname_cr():
    pass


@frr_show_ipv6_accesslist_ipv6accesslistname.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_accesslist_ipv6accesslistname_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_accesslist_ipv6accesslistname_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_access-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_access-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_access-list'
    pass


@frr_show_ipv6_accesslist_ipv6accesslistname_json.command('./	<cr>')
def frr_show_ipv6_accesslist_ipv6accesslistname_json_cr():
    pass


@frr_show_ipv6_accesslist.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_accesslist_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_accesslist_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_access-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_access-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_access-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_access-list'
    pass


@frr_show_ipv6_accesslist_json.command('./	<cr>')
def frr_show_ipv6_accesslist_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='fib', invoke_without_command=True)
def frr_show_ipv6_fib(show_ipv6_fib_='show_ipv6_fib'):
    """IPv6 forwarding table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib.name
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib.command('./	<cr>')
def frr_show_ipv6_fib_cr():
    pass


@frr_show_ipv6_fib.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_choicecase():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_choicecase.command('./	<cr>')
def frr_show_ipv6_fib_choicecase_cr():
    pass


@frr_show_ipv6_fib_choicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_choicecase_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_choicecase_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_choicecase_format.command('./	<cr>')
def frr_show_ipv6_fib_choicecase_format_cr():
    pass


@frr_show_ipv6_fib.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_format.command('./	<cr>')
def frr_show_ipv6_fib_format_cr():
    pass


@frr_show_ipv6_fib.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_fib_ipv6address():
    """IPv6 Address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_ipv6address.name
    data_gen['IPV6_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_ipv6address.command('./	<cr>')
def frr_show_ipv6_fib_ipv6address_cr():
    pass


@frr_show_ipv6_fib_ipv6address.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_fib_ipv6address_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_ipv6address_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_ipv6address_json.command('./	<cr>')
def frr_show_ipv6_fib_ipv6address_json_cr():
    pass


@frr_show_ipv6_fib_ipv6address_json.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_ipv6_fib_ipv6address_json_nexthopgroup(json_nexthopgroup_='json_nexthop-group'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_ipv6address_json_nexthopgroup.name
    data_gen['json_nexthop-group'] = json_nexthopgroup_='json_nexthop-group'
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_ipv6address_json_nexthopgroup.command('./	<cr>')
def frr_show_ipv6_fib_ipv6address_json_nexthopgroup_cr():
    pass


@frr_show_ipv6_fib_ipv6address.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_ipv6_fib_ipv6address_nexthopgroup(nexthopgroup_='nexthop-group'):
    """Nexthop Group Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_ipv6address_nexthopgroup.name
    data_gen['nexthop-group'] = nexthopgroup_='nexthop-group'
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_ipv6address_nexthopgroup.command('./	<cr>')
def frr_show_ipv6_fib_ipv6address_nexthopgroup_cr():
    pass


@frr_show_ipv6_fib.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['X:X::X:X/M']),)
def frr_show_ipv6_fib_ipv6prefix():
    """3"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_ipv6prefix.name
    data_gen['IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_ipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer-prefixes', invoke_without_command=True)
def frr_show_ipv6_fib_ipv6prefix_longerprefixes(longerprefixes_='longer-prefixes'):
    """Show route matching the specified Network/Mask pair only"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_ipv6prefix_longerprefixes.name
    data_gen['longer-prefixes'] = longerprefixes_='longer-prefixes'
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_ipv6prefix_longerprefixes.command('./	<cr>')
def frr_show_ipv6_fib_ipv6prefix_longerprefixes_cr():
    pass


@frr_show_ipv6_fib_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_ipv6prefix_longerprefixes_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_ipv6prefix_longerprefixes_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_ipv6prefix_longerprefixes_format.command('./	<cr>')
def frr_show_ipv6_fib_ipv6prefix_longerprefixes_format_cr():
    pass


@frr_show_ipv6_fib_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_ipv6prefix_longerprefixes_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_ipv6prefix_longerprefixes_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_ipv6prefix_longerprefixes_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_ipv6prefix_longerprefixes_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_ipv6prefix_longerprefixes_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_ipv6prefix_longerprefixes_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_ipv6prefix_longerprefixes_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_ipv6prefix_longerprefixes_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_ipv6prefix_longerprefixes_frrip6redist_format_cr():
    pass


@frr_show_ipv6_fib.group(cls=FRR_AbbreviationGroup, name='table', invoke_without_command=True)
def frr_show_ipv6_fib_table(show_ipv6_fib_table_='show_ipv6_fib_table'):
    """Table to display"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table.name
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table.command('./	<cr>')
def frr_show_ipv6_fib_table_cr():
    pass


@frr_show_ipv6_fib_table.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, [(1, 4294967295), 'all']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase():
    """The table number to display"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_cr():
    pass


@frr_show_ipv6_fib_table_choicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_frrip6redist_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X/M']),)
def frr_show_ipv6_fib_table_choicecase_ipv6prefix():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_ipv6prefix.name
    data_gen['IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_ipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer-prefixes', invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes(longerprefixes_='longer-prefixes'):
    """Show route matching the specified Network/Mask pair only"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes.name
    data_gen['longer-prefixes'] = longerprefixes_='longer-prefixes'
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_ipv6prefix_longerprefixes_frrip6redist_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_fib_table_choicecase_tag(tag_value, tag_='tag'):
    """Show only routes with tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['TAG_VALUE'] = tag_value
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_tag.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_tag_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_tag_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_tag_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_tag_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_tag_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_tag_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_tag_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_tag_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_tag_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_tag_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_tag_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_tag_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_tag_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_tag_frrip6redist_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_ipv6_fib_table_choicecase_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['NAME', 'all']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_frrip6redist_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['X:X::X:X/M']),)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix():
    """8"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix.name
    data_gen['IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer-prefixes', invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes(longerprefixes_='longer-prefixes'):
    """Show route matching the specified Network/Mask pair only"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes.name
    data_gen['longer-prefixes'] = longerprefixes_='longer-prefixes'
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(12, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag(tag_value, tag_='tag'):
    """Show only routes with tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['TAG_VALUE'] = tag_value
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_format_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist_format_cr():
    pass


@frr_show_ipv6_fib_table.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_table_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_table_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib_table'
    pass


@frr_show_ipv6_fib_table_format.command('./	<cr>')
def frr_show_ipv6_fib_table_format_cr():
    pass


@frr_show_ipv6_fib.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_fib_tag(tag_value, tag_='tag'):
    """Show only routes with tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['TAG_VALUE'] = tag_value
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_tag.command('./	<cr>')
def frr_show_ipv6_fib_tag_cr():
    pass


@frr_show_ipv6_fib_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_tag_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_tag_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_tag_format.command('./	<cr>')
def frr_show_ipv6_fib_tag_format_cr():
    pass


@frr_show_ipv6_fib_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_tag_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_tag_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_tag_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_tag_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_tag_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_tag_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_tag_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_tag_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_tag_frrip6redist_format_cr():
    pass


@frr_show_ipv6_fib.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_ipv6_fib_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['NAME', 'all']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_format.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_format_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_frrip6redist_format_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address():
    """IPv6 Address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address.name
    data_gen['IPV6_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_json.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_json_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_json.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_json_nexthopgroup(json_nexthopgroup_='json_nexthop-group'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_json_nexthopgroup.name
    data_gen['json_nexthop-group'] = json_nexthopgroup_='json_nexthop-group'
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_json_nexthopgroup.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_json_nexthopgroup_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_nexthopgroup(nexthopgroup_='nexthop-group'):
    """Nexthop Group Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_nexthopgroup.name
    data_gen['nexthop-group'] = nexthopgroup_='nexthop-group'
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_nexthopgroup.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6address_nexthopgroup_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X/M']),)
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix.name
    data_gen['IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer-prefixes', invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes(longerprefixes_='longer-prefixes'):
    """Show route matching the specified Network/Mask pair only"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes.name
    data_gen['longer-prefixes'] = longerprefixes_='longer-prefixes'
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_fib_vrf_vrfchoicecase_tag(tag_value, tag_='tag'):
    """Show only routes with tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['TAG_VALUE'] = tag_value
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_tag.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_tag_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_tag_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_tag_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_tag_format.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_tag_format_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_tag_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_tag_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_tag_frrip6redist.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_tag_frrip6redist_cr():
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_tag_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_fib_vrf_vrfchoicecase_tag_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_fib_vrf_vrfchoicecase_tag_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_fib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_fib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_fib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_fib'
    pass


@frr_show_ipv6_fib_vrf_vrfchoicecase_tag_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_fib_vrf_vrfchoicecase_tag_frrip6redist_format_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='forwarding', invoke_without_command=True)
def frr_show_ipv6_forwarding(forwarding_='forwarding'):
    """Forwarding status"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_forwarding.name
    data_gen['forwarding'] = forwarding_='forwarding'
    
    if 'VIEW_NODE|show_ipv6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6'][key] = val
    
    # set VIEW_NODE -> show_ipv6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6'
    pass


@frr_show_ipv6_forwarding.command('./	<cr>')
def frr_show_ipv6_forwarding_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='import-check', invoke_without_command=True)
def frr_show_ipv6_importcheck(show_ipv6_importcheck_='show_ipv6_import-check'):
    """IP import check tracking table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck.name
    
    if 'VIEW_NODE|show_ipv6_import-check' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check'
    pass


@frr_show_ipv6_importcheck.command('./	<cr>')
def frr_show_ipv6_importcheck_cr():
    pass


@frr_show_ipv6_importcheck.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_importcheck_ipaddress():
    """IPv4 Address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_ipaddress.name
    data_gen['IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_import-check' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check'
    pass


@frr_show_ipv6_importcheck_ipaddress.command('./	<cr>')
def frr_show_ipv6_importcheck_ipaddress_cr():
    pass


@frr_show_ipv6_importcheck_ipaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_importcheck_ipaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_ipaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_import-check' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check'
    pass


@frr_show_ipv6_importcheck_ipaddress_json.command('./	<cr>')
def frr_show_ipv6_importcheck_ipaddress_json_cr():
    pass


@frr_show_ipv6_importcheck_ipaddress.group(cls=FRR_AbbreviationGroup, name='mrib', invoke_without_command=True)
def frr_show_ipv6_importcheck_ipaddress_mrib(mrib_='mrib'):
    """Show Multicast (MRIB) NHT state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_ipaddress_mrib.name
    data_gen['mrib'] = mrib_='mrib'
    
    if 'VIEW_NODE|show_ipv6_import-check' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check'
    pass


@frr_show_ipv6_importcheck_ipaddress_mrib.command('./	<cr>')
def frr_show_ipv6_importcheck_ipaddress_mrib_cr():
    pass


@frr_show_ipv6_importcheck_ipaddress_mrib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_importcheck_ipaddress_mrib_json(mrib_json_='mrib_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_ipaddress_mrib_json.name
    data_gen['mrib_json'] = mrib_json_='mrib_json'
    
    if 'VIEW_NODE|show_ipv6_import-check' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check'
    pass


@frr_show_ipv6_importcheck_ipaddress_mrib_json.command('./	<cr>')
def frr_show_ipv6_importcheck_ipaddress_mrib_json_cr():
    pass


@frr_show_ipv6_importcheck.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_importcheck_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_import-check' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check'
    pass


@frr_show_ipv6_importcheck_json.command('./	<cr>')
def frr_show_ipv6_importcheck_json_cr():
    pass


@frr_show_ipv6_importcheck.group(cls=FRR_AbbreviationGroup, name='mrib', invoke_without_command=True)
def frr_show_ipv6_importcheck_mrib(show_ipv6_importcheck_mrib_='show_ipv6_import-check_mrib'):
    """Show Multicast (MRIB) NHT state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_mrib.name
    
    if 'VIEW_NODE|show_ipv6_import-check_mrib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_mrib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_mrib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_mrib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_mrib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_mrib'
    pass


@frr_show_ipv6_importcheck_mrib.command('./	<cr>')
def frr_show_ipv6_importcheck_mrib_cr():
    pass


@frr_show_ipv6_importcheck_mrib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_importcheck_mrib_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_mrib_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_import-check_mrib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_mrib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_mrib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_mrib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_mrib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_mrib'
    pass


@frr_show_ipv6_importcheck_mrib_json.command('./	<cr>')
def frr_show_ipv6_importcheck_mrib_json_cr():
    pass


@frr_show_ipv6_importcheck.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_ipv6_importcheck_vrf(the_vrf_name, show_ipv6_importcheck_vrf_='show_ipv6_import-check_vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf.name
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf'
    pass


@frr_show_ipv6_importcheck_vrf.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_cr():
    pass


@frr_show_ipv6_importcheck_vrf.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_all(show_ipv6_importcheck_vrf_all_='show_ipv6_import-check_vrf_all'):
    """All VRFs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_all.name
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf_all'
    pass


@frr_show_ipv6_importcheck_vrf_all.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_all_cr():
    pass


@frr_show_ipv6_importcheck_vrf_all.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_all_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_all_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf_all'
    pass


@frr_show_ipv6_importcheck_vrf_all_json.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_all_json_cr():
    pass


@frr_show_ipv6_importcheck_vrf_all.group(cls=FRR_AbbreviationGroup, name='mrib', invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_all_mrib(show_ipv6_importcheck_vrf_all_mrib_='show_ipv6_import-check_vrf_all_mrib'):
    """Show Multicast (MRIB) NHT state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_all_mrib.name
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf_all_mrib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all_mrib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all_mrib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all_mrib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf_all_mrib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf_all_mrib'
    pass


@frr_show_ipv6_importcheck_vrf_all_mrib.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_all_mrib_cr():
    pass


@frr_show_ipv6_importcheck_vrf_all_mrib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_all_mrib_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_all_mrib_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf_all_mrib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all_mrib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all_mrib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf_all_mrib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf_all_mrib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf_all_mrib'
    pass


@frr_show_ipv6_importcheck_vrf_all_mrib_json.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_all_mrib_json_cr():
    pass


@frr_show_ipv6_importcheck_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_ipaddress():
    """IPv4 Address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_ipaddress.name
    data_gen['IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf'
    pass


@frr_show_ipv6_importcheck_vrf_ipaddress.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_ipaddress_cr():
    pass


@frr_show_ipv6_importcheck_vrf_ipaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_ipaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_ipaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf'
    pass


@frr_show_ipv6_importcheck_vrf_ipaddress_json.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_ipaddress_json_cr():
    pass


@frr_show_ipv6_importcheck_vrf_ipaddress.group(cls=FRR_AbbreviationGroup, name='mrib', invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_ipaddress_mrib(mrib_='mrib'):
    """Show Multicast (MRIB) NHT state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_ipaddress_mrib.name
    data_gen['mrib'] = mrib_='mrib'
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf'
    pass


@frr_show_ipv6_importcheck_vrf_ipaddress_mrib.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_ipaddress_mrib_cr():
    pass


@frr_show_ipv6_importcheck_vrf_ipaddress_mrib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_ipaddress_mrib_json(mrib_json_='mrib_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_ipaddress_mrib_json.name
    data_gen['mrib_json'] = mrib_json_='mrib_json'
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf'
    pass


@frr_show_ipv6_importcheck_vrf_ipaddress_mrib_json.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_ipaddress_mrib_json_cr():
    pass


@frr_show_ipv6_importcheck_vrf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf'
    pass


@frr_show_ipv6_importcheck_vrf_json.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_json_cr():
    pass


@frr_show_ipv6_importcheck_vrf.group(cls=FRR_AbbreviationGroup, name='mrib', invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_mrib(mrib_='mrib'):
    """Show Multicast (MRIB) NHT state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_mrib.name
    data_gen['mrib'] = mrib_='mrib'
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf'
    pass


@frr_show_ipv6_importcheck_vrf_mrib.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_mrib_cr():
    pass


@frr_show_ipv6_importcheck_vrf_mrib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_importcheck_vrf_mrib_json(mrib_json_='mrib_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_importcheck_vrf_mrib_json.name
    data_gen['mrib_json'] = mrib_json_='mrib_json'
    
    if 'VIEW_NODE|show_ipv6_import-check_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_import-check_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_import-check_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_import-check_vrf'
    pass


@frr_show_ipv6_importcheck_vrf_mrib_json.command('./	<cr>')
def frr_show_ipv6_importcheck_vrf_mrib_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='mld',)
def frr_show_ipv6_mld(show_ipv6_mld_='show_ipv6_mld'):
    """MLD information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld.name
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld.group(cls=FRR_AbbreviationGroup, name='groups', invoke_without_command=True)
def frr_show_ipv6_mld_groups(show_ipv6_mld_groups_='show_ipv6_mld_groups'):
    """MLD groups information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_groups.name
    
    if 'VIEW_NODE|show_ipv6_mld_groups' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_groups'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_groups']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_groups'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_groups table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_groups'
    pass


@frr_show_ipv6_mld_groups.command('./	<cr>')
def frr_show_ipv6_mld_groups_cr():
    pass


@frr_show_ipv6_mld_groups.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_groups_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_groups_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_groups' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_groups'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_groups']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_groups'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_groups table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_groups'
    pass


@frr_show_ipv6_mld_groups_json.command('./	<cr>')
def frr_show_ipv6_mld_groups_json_cr():
    pass


@frr_show_ipv6_mld.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_ipv6_mld_interface(show_ipv6_mld_interface_='show_ipv6_mld_interface'):
    """MLD interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_interface.name
    
    if 'VIEW_NODE|show_ipv6_mld_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_interface'
    pass


@frr_show_ipv6_mld_interface.command('./	<cr>')
def frr_show_ipv6_mld_interface_cr():
    pass


@frr_show_ipv6_mld_interface.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_mld_interface_detail(show_ipv6_mld_interface_detail_='show_ipv6_mld_interface_detail'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_interface_detail.name
    
    if 'VIEW_NODE|show_ipv6_mld_interface_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_interface_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_interface_detail'
    pass


@frr_show_ipv6_mld_interface_detail.command('./	<cr>')
def frr_show_ipv6_mld_interface_detail_cr():
    pass


@frr_show_ipv6_mld_interface_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_interface_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_interface_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_interface_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_interface_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_interface_detail'
    pass


@frr_show_ipv6_mld_interface_detail_json.command('./	<cr>')
def frr_show_ipv6_mld_interface_detail_json_cr():
    pass


@frr_show_ipv6_mld_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['IFNAME']), invoke_without_command=True)
def frr_show_ipv6_mld_interface_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_interface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_mld_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_interface'
    pass


@frr_show_ipv6_mld_interface_interfacename.command('./	<cr>')
def frr_show_ipv6_mld_interface_interfacename_cr():
    pass


@frr_show_ipv6_mld_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_interface_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_interface_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_interface'
    pass


@frr_show_ipv6_mld_interface_interfacename_json.command('./	<cr>')
def frr_show_ipv6_mld_interface_interfacename_json_cr():
    pass


@frr_show_ipv6_mld_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_interface'
    pass


@frr_show_ipv6_mld_interface_json.command('./	<cr>')
def frr_show_ipv6_mld_interface_json_cr():
    pass


@frr_show_ipv6_mld.group(cls=FRR_AbbreviationGroup, name='joins', invoke_without_command=True)
def frr_show_ipv6_mld_joins(show_ipv6_mld_joins_='show_ipv6_mld_joins'):
    """MLD joined groups & sources"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_joins.name
    
    if 'VIEW_NODE|show_ipv6_mld_joins' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_joins table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_joins'
    pass


@frr_show_ipv6_mld_joins.command('./	<cr>')
def frr_show_ipv6_mld_joins_cr():
    pass


@frr_show_ipv6_mld_joins.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_mld_joins_detail(show_ipv6_mld_joins_detail_='show_ipv6_mld_joins_detail'):
    """Show details, including tracked receivers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_joins_detail.name
    
    if 'VIEW_NODE|show_ipv6_mld_joins_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_joins_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_joins_detail'
    pass


@frr_show_ipv6_mld_joins_detail.command('./	<cr>')
def frr_show_ipv6_mld_joins_detail_cr():
    pass


@frr_show_ipv6_mld_joins_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_joins_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_joins_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_joins_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_joins_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_joins_detail'
    pass


@frr_show_ipv6_mld_joins_detail_json.command('./	<cr>')
def frr_show_ipv6_mld_joins_detail_json_cr():
    pass


@frr_show_ipv6_mld_joins.group(cls=FRR_AbbreviationGroup, name='groups', invoke_without_command=True)
@click.argument('show_groups_covered_by', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_show_ipv6_mld_joins_groups(show_groups_covered_by, groups_='groups'):
    """Limit output to group range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_joins_groups.name
    data_gen['groups'] = groups_='groups'
    data_gen['SHOW_GROUPS_COVERED_BY'] = show_groups_covered_by
    
    if 'VIEW_NODE|show_ipv6_mld_joins' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_joins table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_joins'
    pass


@frr_show_ipv6_mld_joins_groups.command('./	<cr>')
def frr_show_ipv6_mld_joins_groups_cr():
    pass


@frr_show_ipv6_mld_joins_groups.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_joins_groups_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_joins_groups_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_joins' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_joins table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_joins'
    pass


@frr_show_ipv6_mld_joins_groups_json.command('./	<cr>')
def frr_show_ipv6_mld_joins_groups_json_cr():
    pass


@frr_show_ipv6_mld_joins.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_show_ipv6_mld_joins_interface(interface_name, interface_='interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_joins_interface.name
    data_gen['interface'] = interface_='interface'
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'VIEW_NODE|show_ipv6_mld_joins' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_joins table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_joins'
    pass


@frr_show_ipv6_mld_joins_interface.command('./	<cr>')
def frr_show_ipv6_mld_joins_interface_cr():
    pass


@frr_show_ipv6_mld_joins_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_joins_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_joins_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_joins' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_joins table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_joins'
    pass


@frr_show_ipv6_mld_joins_interface_json.command('./	<cr>')
def frr_show_ipv6_mld_joins_interface_json_cr():
    pass


@frr_show_ipv6_mld_joins.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_joins_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_joins_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_joins' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_joins table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_joins'
    pass


@frr_show_ipv6_mld_joins_json.command('./	<cr>')
def frr_show_ipv6_mld_joins_json_cr():
    pass


@frr_show_ipv6_mld_joins.group(cls=FRR_AbbreviationGroup, name='sources', invoke_without_command=True)
@click.argument('show_sources_covered_by', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_show_ipv6_mld_joins_sources(show_sources_covered_by, sources_='sources'):
    """Limit output to source range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_joins_sources.name
    data_gen['sources'] = sources_='sources'
    data_gen['SHOW_SOURCES_COVERED_BY'] = show_sources_covered_by
    
    if 'VIEW_NODE|show_ipv6_mld_joins' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_joins table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_joins'
    pass


@frr_show_ipv6_mld_joins_sources.command('./	<cr>')
def frr_show_ipv6_mld_joins_sources_cr():
    pass


@frr_show_ipv6_mld_joins_sources.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_joins_sources_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_joins_sources_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_joins' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_joins'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_joins table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_joins'
    pass


@frr_show_ipv6_mld_joins_sources_json.command('./	<cr>')
def frr_show_ipv6_mld_joins_sources_json_cr():
    pass


@frr_show_ipv6_mld.group(cls=FRR_AbbreviationGroup, name='statistics', invoke_without_command=True)
def frr_show_ipv6_mld_statistics(show_ipv6_mld_statistics_='show_ipv6_mld_statistics'):
    """MLD statistics"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_statistics.name
    
    if 'VIEW_NODE|show_ipv6_mld_statistics' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_statistics table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_statistics'
    pass


@frr_show_ipv6_mld_statistics.command('./	<cr>')
def frr_show_ipv6_mld_statistics_cr():
    pass


@frr_show_ipv6_mld_statistics.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_show_ipv6_mld_statistics_interface(interface_name, interface_='interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_statistics_interface.name
    data_gen['interface'] = interface_='interface'
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'VIEW_NODE|show_ipv6_mld_statistics' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_statistics table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_statistics'
    pass


@frr_show_ipv6_mld_statistics_interface.command('./	<cr>')
def frr_show_ipv6_mld_statistics_interface_cr():
    pass


@frr_show_ipv6_mld_statistics_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_statistics_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_statistics_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_statistics' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_statistics table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_statistics'
    pass


@frr_show_ipv6_mld_statistics_interface_json.command('./	<cr>')
def frr_show_ipv6_mld_statistics_interface_json_cr():
    pass


@frr_show_ipv6_mld_statistics.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_statistics_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_statistics_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld_statistics' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld_statistics'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld_statistics table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld_statistics'
    pass


@frr_show_ipv6_mld_statistics_json.command('./	<cr>')
def frr_show_ipv6_mld_statistics_json_cr():
    pass


@frr_show_ipv6_mld.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_ipv6_mld_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['VRF', 'all']),)
def frr_show_ipv6_mld_vrf_vrfchoicecase():
    """4"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='groups', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_groups(groups_='groups'):
    """MLD groups information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_groups.name
    data_gen['groups'] = groups_='groups'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_groups.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_groups_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_groups.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_groups_json(groups_json_='groups_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_groups_json.name
    data_gen['groups_json'] = groups_json_='groups_json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_groups_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_groups_json_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface(interface_='interface'):
    """MLD interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_interface.name
    data_gen['interface'] = interface_='interface'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_detail(interface_detail_='interface_detail'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_interface_detail.name
    data_gen['interface_detail'] = interface_detail_='interface_detail'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface_detail.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_detail_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_detail_json(interface_detail_json_='interface_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_interface_detail_json.name
    data_gen['interface_detail_json'] = interface_detail_json_='interface_detail_json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface_detail_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_detail_json_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['IFNAME']), invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_interface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface_interfacename.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_interfacename_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_interface_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface_interfacename_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_interfacename_json_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_interface_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_interface_json_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='joins', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins(joins_='joins'):
    """MLD joined groups & sources"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_joins.name
    data_gen['joins'] = joins_='joins'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_detail(joins_detail_='joins_detail'):
    """Show details, including tracked receivers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_joins_detail.name
    data_gen['joins_detail'] = joins_detail_='joins_detail'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_detail.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_detail_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_detail_json(joins_detail_json_='joins_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_joins_detail_json.name
    data_gen['joins_detail_json'] = joins_detail_json_='joins_detail_json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_detail_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_detail_json_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins.group(cls=FRR_AbbreviationGroup, name='groups', invoke_without_command=True)
@click.argument('show_groups_covered_by', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_groups(show_groups_covered_by, joins_groups_='joins_groups'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_joins_groups.name
    data_gen['joins_groups'] = joins_groups_='joins_groups'
    data_gen['SHOW_GROUPS_COVERED_BY'] = show_groups_covered_by
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_groups.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_groups_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_groups.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_groups_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_joins_groups_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_groups_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_groups_json_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_interface(interface_name, joins_interface_='joins_interface'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_joins_interface.name
    data_gen['joins_interface'] = joins_interface_='joins_interface'
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_interface.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_interface_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_joins_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_interface_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_interface_json_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_json(joins_json_='joins_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_joins_json.name
    data_gen['joins_json'] = joins_json_='joins_json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_json_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins.group(cls=FRR_AbbreviationGroup, name='sources', invoke_without_command=True)
@click.argument('show_sources_covered_by', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_sources(show_sources_covered_by, joins_sources_='joins_sources'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_joins_sources.name
    data_gen['joins_sources'] = joins_sources_='joins_sources'
    data_gen['SHOW_SOURCES_COVERED_BY'] = show_sources_covered_by
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_sources.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_sources_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_sources.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_sources_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_joins_sources_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_joins_sources_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_joins_sources_json_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='statistics', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_statistics(statistics_='statistics'):
    """MLD statistics"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_statistics.name
    data_gen['statistics'] = statistics_='statistics'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_statistics.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_statistics.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_interface(interface_name, statistics_interface_='statistics_interface'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_interface.name
    data_gen['statistics_interface'] = statistics_interface_='statistics_interface'
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_interface.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_interface_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_interface_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_interface_json_cr():
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_statistics.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_json(statistics_json_='statistics_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_json.name
    data_gen['statistics_json'] = statistics_json_='statistics_json'
    
    if 'VIEW_NODE|show_ipv6_mld' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mld'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mld table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mld'
    pass


@frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_json.command('./	<cr>')
def frr_show_ipv6_mld_vrf_vrfchoicecase_statistics_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='mroute', invoke_without_command=True)
def frr_show_ipv6_mroute(show_ipv6_mroute_='show_ipv6_mroute'):
    """IP multicast routing table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute.name
    
    if 'VIEW_NODE|show_ipv6_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute'
    pass


@frr_show_ipv6_mroute.command('./	<cr>')
def frr_show_ipv6_mroute_cr():
    pass


@frr_show_ipv6_mroute.group(cls=FRR_AbbreviationGroup, name='count', invoke_without_command=True)
def frr_show_ipv6_mroute_count(show_ipv6_mroute_count_='show_ipv6_mroute_count'):
    """Route and packet count data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_count.name
    
    if 'VIEW_NODE|show_ipv6_mroute_count' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_count'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_count']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_count'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_count table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_count'
    pass


@frr_show_ipv6_mroute_count.command('./	<cr>')
def frr_show_ipv6_mroute_count_cr():
    pass


@frr_show_ipv6_mroute_count.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_count_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_count_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute_count' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_count'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_count']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_count'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_count table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_count'
    pass


@frr_show_ipv6_mroute_count_json.command('./	<cr>')
def frr_show_ipv6_mroute_count_json_cr():
    pass


@frr_show_ipv6_mroute.group(cls=FRR_AbbreviationGroup, name='fill', invoke_without_command=True)
def frr_show_ipv6_mroute_fill(show_ipv6_mroute_fill_='show_ipv6_mroute_fill'):
    """Fill in Assumed data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_fill.name
    
    if 'VIEW_NODE|show_ipv6_mroute_fill' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_fill'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_fill']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_fill'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_fill table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_fill'
    pass


@frr_show_ipv6_mroute_fill.command('./	<cr>')
def frr_show_ipv6_mroute_fill_cr():
    pass


@frr_show_ipv6_mroute_fill.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_fill_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_fill_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute_fill' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_fill'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_fill']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_fill'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_fill table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_fill'
    pass


@frr_show_ipv6_mroute_fill_json.command('./	<cr>')
def frr_show_ipv6_mroute_fill_json_cr():
    pass


@frr_show_ipv6_mroute.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute'
    pass


@frr_show_ipv6_mroute_json.command('./	<cr>')
def frr_show_ipv6_mroute_json_cr():
    pass


@frr_show_ipv6_mroute.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_ipv6_mroute_summary(show_ipv6_mroute_summary_='show_ipv6_mroute_summary'):
    """Summary of all mroutes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_summary.name
    
    if 'VIEW_NODE|show_ipv6_mroute_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_summary'
    pass


@frr_show_ipv6_mroute_summary.command('./	<cr>')
def frr_show_ipv6_mroute_summary_cr():
    pass


@frr_show_ipv6_mroute_summary.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_summary_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_summary_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_summary'
    pass


@frr_show_ipv6_mroute_summary_json.command('./	<cr>')
def frr_show_ipv6_mroute_summary_json_cr():
    pass


@frr_show_ipv6_mroute.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_mroute_thesourceorgroup():
    """The Source or Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_thesourceorgroup.name
    data_gen['THE_SOURCE_OR_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute'
    pass


@frr_show_ipv6_mroute_thesourceorgroup.command('./	<cr>')
def frr_show_ipv6_mroute_thesourceorgroup_cr():
    pass


@frr_show_ipv6_mroute_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name='fill', invoke_without_command=True)
def frr_show_ipv6_mroute_thesourceorgroup_fill(fill_='fill'):
    """Fill in Assumed data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_thesourceorgroup_fill.name
    data_gen['fill'] = fill_='fill'
    
    if 'VIEW_NODE|show_ipv6_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute'
    pass


@frr_show_ipv6_mroute_thesourceorgroup_fill.command('./	<cr>')
def frr_show_ipv6_mroute_thesourceorgroup_fill_cr():
    pass


@frr_show_ipv6_mroute_thesourceorgroup_fill.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_thesourceorgroup_fill_json(fill_json_='fill_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_thesourceorgroup_fill_json.name
    data_gen['fill_json'] = fill_json_='fill_json'
    
    if 'VIEW_NODE|show_ipv6_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute'
    pass


@frr_show_ipv6_mroute_thesourceorgroup_fill_json.command('./	<cr>')
def frr_show_ipv6_mroute_thesourceorgroup_fill_json_cr():
    pass


@frr_show_ipv6_mroute_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_thesourceorgroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_thesourceorgroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute'
    pass


@frr_show_ipv6_mroute_thesourceorgroup_json.command('./	<cr>')
def frr_show_ipv6_mroute_thesourceorgroup_json_cr():
    pass


@frr_show_ipv6_mroute_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_mroute_thesourceorgroup_thegroup():
    """The Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_thesourceorgroup_thegroup.name
    data_gen['THE_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute'
    pass


@frr_show_ipv6_mroute_thesourceorgroup_thegroup.command('./	<cr>')
def frr_show_ipv6_mroute_thesourceorgroup_thegroup_cr():
    pass


@frr_show_ipv6_mroute_thesourceorgroup_thegroup.group(cls=FRR_AbbreviationGroup, name='fill', invoke_without_command=True)
def frr_show_ipv6_mroute_thesourceorgroup_thegroup_fill(fill_='fill'):
    """Fill in Assumed data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_thesourceorgroup_thegroup_fill.name
    data_gen['fill'] = fill_='fill'
    
    if 'VIEW_NODE|show_ipv6_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute'
    pass


@frr_show_ipv6_mroute_thesourceorgroup_thegroup_fill.command('./	<cr>')
def frr_show_ipv6_mroute_thesourceorgroup_thegroup_fill_cr():
    pass


@frr_show_ipv6_mroute_thesourceorgroup_thegroup_fill.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_thesourceorgroup_thegroup_fill_json(fill_json_='fill_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_thesourceorgroup_thegroup_fill_json.name
    data_gen['fill_json'] = fill_json_='fill_json'
    
    if 'VIEW_NODE|show_ipv6_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute'
    pass


@frr_show_ipv6_mroute_thesourceorgroup_thegroup_fill_json.command('./	<cr>')
def frr_show_ipv6_mroute_thesourceorgroup_thegroup_fill_json_cr():
    pass


@frr_show_ipv6_mroute_thesourceorgroup_thegroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_thesourceorgroup_thegroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_thesourceorgroup_thegroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute'
    pass


@frr_show_ipv6_mroute_thesourceorgroup_thegroup_json.command('./	<cr>')
def frr_show_ipv6_mroute_thesourceorgroup_thegroup_json_cr():
    pass


@frr_show_ipv6_mroute.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_ipv6_mroute_vrf(the_vrf_name, show_ipv6_mroute_vrf_='show_ipv6_mroute_vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf.name
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_cr():
    pass


@frr_show_ipv6_mroute_vrf.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_all(show_ipv6_mroute_vrf_all_='show_ipv6_mroute_vrf_all'):
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_all.name
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf_all'
    pass


@frr_show_ipv6_mroute_vrf_all.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_all_cr():
    pass


@frr_show_ipv6_mroute_vrf_all.group(cls=FRR_AbbreviationGroup, name='count', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_all_count(show_ipv6_mroute_vrf_all_count_='show_ipv6_mroute_vrf_all_count'):
    """Route and packet count data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_all_count.name
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf_all_count' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_count'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_count']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_count'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf_all_count table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf_all_count'
    pass


@frr_show_ipv6_mroute_vrf_all_count.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_all_count_cr():
    pass


@frr_show_ipv6_mroute_vrf_all_count.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_all_count_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_all_count_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf_all_count' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_count'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_count']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_count'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf_all_count table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf_all_count'
    pass


@frr_show_ipv6_mroute_vrf_all_count_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_all_count_json_cr():
    pass


@frr_show_ipv6_mroute_vrf_all.group(cls=FRR_AbbreviationGroup, name='fill', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_all_fill(show_ipv6_mroute_vrf_all_fill_='show_ipv6_mroute_vrf_all_fill'):
    """Fill in Assumed data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_all_fill.name
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf_all_fill' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_fill'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_fill']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_fill'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf_all_fill table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf_all_fill'
    pass


@frr_show_ipv6_mroute_vrf_all_fill.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_all_fill_cr():
    pass


@frr_show_ipv6_mroute_vrf_all_fill.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_all_fill_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_all_fill_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf_all_fill' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_fill'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_fill']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_fill'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf_all_fill table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf_all_fill'
    pass


@frr_show_ipv6_mroute_vrf_all_fill_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_all_fill_json_cr():
    pass


@frr_show_ipv6_mroute_vrf_all.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_all_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_all_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf_all'
    pass


@frr_show_ipv6_mroute_vrf_all_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_all_json_cr():
    pass


@frr_show_ipv6_mroute_vrf_all.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_all_summary(show_ipv6_mroute_vrf_all_summary_='show_ipv6_mroute_vrf_all_summary'):
    """Summary of all mroutes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_all_summary.name
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf_all_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf_all_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf_all_summary'
    pass


@frr_show_ipv6_mroute_vrf_all_summary.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_all_summary_cr():
    pass


@frr_show_ipv6_mroute_vrf_all_summary.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_all_summary_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_all_summary_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf_all_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf_all_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf_all_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf_all_summary'
    pass


@frr_show_ipv6_mroute_vrf_all_summary_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_all_summary_json_cr():
    pass


@frr_show_ipv6_mroute_vrf.group(cls=FRR_AbbreviationGroup, name='count', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_count(count_='count'):
    """Route and packet count data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_count.name
    data_gen['count'] = count_='count'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_count.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_count_cr():
    pass


@frr_show_ipv6_mroute_vrf_count.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_count_json(count_json_='count_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_count_json.name
    data_gen['count_json'] = count_json_='count_json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_count_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_count_json_cr():
    pass


@frr_show_ipv6_mroute_vrf.group(cls=FRR_AbbreviationGroup, name='fill', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_fill(fill_='fill'):
    """Fill in Assumed data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_fill.name
    data_gen['fill'] = fill_='fill'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_fill.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_fill_cr():
    pass


@frr_show_ipv6_mroute_vrf_fill.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_fill_json(fill_json_='fill_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_fill_json.name
    data_gen['fill_json'] = fill_json_='fill_json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_fill_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_fill_json_cr():
    pass


@frr_show_ipv6_mroute_vrf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_json_cr():
    pass


@frr_show_ipv6_mroute_vrf.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_summary(summary_='summary'):
    """Summary of all mroutes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_summary.name
    data_gen['summary'] = summary_='summary'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_summary.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_summary_cr():
    pass


@frr_show_ipv6_mroute_vrf_summary.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_summary_json(summary_json_='summary_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_summary_json.name
    data_gen['summary_json'] = summary_json_='summary_json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_summary_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_summary_json_cr():
    pass


@frr_show_ipv6_mroute_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_thesourceorgroup():
    """The Source or Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_thesourceorgroup.name
    data_gen['THE_SOURCE_OR_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_thesourceorgroup_cr():
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name='fill', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_thesourceorgroup_fill(fill_='fill'):
    """Fill in Assumed data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_thesourceorgroup_fill.name
    data_gen['fill'] = fill_='fill'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_fill.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_thesourceorgroup_fill_cr():
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_fill.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_thesourceorgroup_fill_json(fill_json_='fill_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_thesourceorgroup_fill_json.name
    data_gen['fill_json'] = fill_json_='fill_json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_fill_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_thesourceorgroup_fill_json_cr():
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_thesourceorgroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_thesourceorgroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_thesourceorgroup_json_cr():
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup():
    """The Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup.name
    data_gen['THE_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_cr():
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup.group(cls=FRR_AbbreviationGroup, name='fill', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_fill(fill_='fill'):
    """Fill in Assumed data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_fill.name
    data_gen['fill'] = fill_='fill'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_fill.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_fill_cr():
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_fill.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_fill_json(fill_json_='fill_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_fill_json.name
    data_gen['fill_json'] = fill_json_='fill_json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_fill_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_fill_json_cr():
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_mroute_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_mroute_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_mroute_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_mroute_vrf'
    pass


@frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_json.command('./	<cr>')
def frr_show_ipv6_mroute_vrf_thesourceorgroup_thegroup_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='multicast',)
def frr_show_ipv6_multicast():
    """Multicast global information"""
    global COMMON_DATA_MAP
    
    pass


@frr_show_ipv6_multicast.group(cls=FRR_AbbreviationGroup, name='count', invoke_without_command=True)
def frr_show_ipv6_multicast_count(show_ipv6_multicast_count_='show_ipv6_multicast_count'):
    """Data packet count"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_multicast_count.name
    
    if 'VIEW_NODE|show_ipv6_multicast_count' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count'][key] = val
    
    # set VIEW_NODE -> show_ipv6_multicast_count table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_multicast_count'
    pass


@frr_show_ipv6_multicast_count.command('./	<cr>')
def frr_show_ipv6_multicast_count_cr():
    pass


@frr_show_ipv6_multicast_count.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_multicast_count_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_multicast_count_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_multicast_count' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count'][key] = val
    
    # set VIEW_NODE -> show_ipv6_multicast_count table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_multicast_count'
    pass


@frr_show_ipv6_multicast_count_json.command('./	<cr>')
def frr_show_ipv6_multicast_count_json_cr():
    pass


@frr_show_ipv6_multicast_count.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_ipv6_multicast_count_vrf(the_vrf_name, show_ipv6_multicast_count_vrf_='show_ipv6_multicast_count_vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_multicast_count_vrf.name
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_multicast_count_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_multicast_count_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_multicast_count_vrf'
    pass


@frr_show_ipv6_multicast_count_vrf.command('./	<cr>')
def frr_show_ipv6_multicast_count_vrf_cr():
    pass


@frr_show_ipv6_multicast_count_vrf.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_ipv6_multicast_count_vrf_all(show_ipv6_multicast_count_vrf_all_='show_ipv6_multicast_count_vrf_all'):
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_multicast_count_vrf_all.name
    
    if 'VIEW_NODE|show_ipv6_multicast_count_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_ipv6_multicast_count_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_multicast_count_vrf_all'
    pass


@frr_show_ipv6_multicast_count_vrf_all.command('./	<cr>')
def frr_show_ipv6_multicast_count_vrf_all_cr():
    pass


@frr_show_ipv6_multicast_count_vrf_all.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_multicast_count_vrf_all_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_multicast_count_vrf_all_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_multicast_count_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_ipv6_multicast_count_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_multicast_count_vrf_all'
    pass


@frr_show_ipv6_multicast_count_vrf_all_json.command('./	<cr>')
def frr_show_ipv6_multicast_count_vrf_all_json_cr():
    pass


@frr_show_ipv6_multicast_count_vrf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_multicast_count_vrf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_multicast_count_vrf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_multicast_count_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_count_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_multicast_count_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_multicast_count_vrf'
    pass


@frr_show_ipv6_multicast_count_vrf_json.command('./	<cr>')
def frr_show_ipv6_multicast_count_vrf_json_cr():
    pass


@frr_show_ipv6_multicast.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_ipv6_multicast_vrf(show_ipv6_multicast_vrf_='show_ipv6_multicast_vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_multicast_vrf.name
    
    if 'VIEW_NODE|show_ipv6_multicast_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_multicast_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_multicast_vrf'
    pass


@frr_show_ipv6_multicast_vrf.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_ipv6_multicast_vrf_all(all_='all'):
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_multicast_vrf_all.name
    data_gen['all'] = all_='all'
    
    if 'VIEW_NODE|show_ipv6_multicast_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_multicast_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_multicast_vrf'
    pass


@frr_show_ipv6_multicast_vrf_all.command('./	<cr>')
def frr_show_ipv6_multicast_vrf_all_cr():
    pass


@frr_show_ipv6_multicast_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['NAME']), invoke_without_command=True)
def frr_show_ipv6_multicast_vrf_thevrfname():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_multicast_vrf_thevrfname.name
    data_gen['THE_VRF_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_multicast_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_multicast_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_multicast_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_multicast_vrf'
    pass


@frr_show_ipv6_multicast_vrf_thevrfname.command('./	<cr>')
def frr_show_ipv6_multicast_vrf_thevrfname_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='nd', invoke_without_command=True)
def frr_show_ipv6_nd():
    """Neighbor discovery"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nd.name
    
    if 'VIEW_NODE|show_ipv6_nd' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nd table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nd'
    pass


@frr_show_ipv6_nd.command('./	<cr>')
def frr_show_ipv6_nd_cr():
    pass


@frr_show_ipv6_nd.group(cls=FRR_AbbreviationGroup, name='ra-interfaces', invoke_without_command=True)
def frr_show_ipv6_nd_rainterfaces(show_ipv6_nd_rainterfaces_='show_ipv6_nd_ra-interfaces'):
    """Route Advertisement Interfaces"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nd_rainterfaces.name
    
    if 'VIEW_NODE|show_ipv6_nd_ra-interfaces' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd_ra-interfaces'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd_ra-interfaces']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd_ra-interfaces'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nd_ra-interfaces table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nd_ra-interfaces'
    pass


@frr_show_ipv6_nd_rainterfaces.command('./	<cr>')
def frr_show_ipv6_nd_rainterfaces_cr():
    pass


@frr_show_ipv6_nd_rainterfaces.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_ipv6_nd_rainterfaces_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nd_rainterfaces_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_ipv6_nd_ra-interfaces' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd_ra-interfaces'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd_ra-interfaces']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd_ra-interfaces'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nd_ra-interfaces table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nd_ra-interfaces'
    pass


@frr_show_ipv6_nd_rainterfaces_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['NAME', 'all']), invoke_without_command=True)
def frr_show_ipv6_nd_rainterfaces_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nd_rainterfaces_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_nd_ra-interfaces' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd_ra-interfaces'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd_ra-interfaces']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nd_ra-interfaces'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nd_ra-interfaces table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nd_ra-interfaces'
    pass


@frr_show_ipv6_nd_rainterfaces_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_ipv6_nd_rainterfaces_vrf_vrfchoicecase_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='nhrp', invoke_without_command=True)
def frr_show_ipv6_nhrp(show_ipv6_nhrp_='show_ipv6_nhrp'):
    """NHRP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nhrp.name
    
    if 'VIEW_NODE|show_ipv6_nhrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nhrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nhrp'
    pass


@frr_show_ipv6_nhrp.command('./	<cr>')
def frr_show_ipv6_nhrp_cr():
    pass


@frr_show_ipv6_nhrp.group(cls=FRR_AbbreviationGroup, name='cache', invoke_without_command=True)
def frr_show_ipv6_nhrp_cache(show_ipv6_nhrp_cache_='show_ipv6_nhrp_cache'):
    """Forwarding cache information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nhrp_cache.name
    
    if 'VIEW_NODE|show_ipv6_nhrp_cache' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_cache'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_cache']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_cache'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nhrp_cache table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nhrp_cache'
    pass


@frr_show_ipv6_nhrp_cache.command('./	<cr>')
def frr_show_ipv6_nhrp_cache_cr():
    pass


@frr_show_ipv6_nhrp_cache.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nhrp_cache_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nhrp_cache_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nhrp_cache' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_cache'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_cache']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_cache'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nhrp_cache table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nhrp_cache'
    pass


@frr_show_ipv6_nhrp_cache_json.command('./	<cr>')
def frr_show_ipv6_nhrp_cache_json_cr():
    pass


@frr_show_ipv6_nhrp.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nhrp_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nhrp_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nhrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nhrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nhrp'
    pass


@frr_show_ipv6_nhrp_json.command('./	<cr>')
def frr_show_ipv6_nhrp_json_cr():
    pass


@frr_show_ipv6_nhrp.group(cls=FRR_AbbreviationGroup, name='nhs', invoke_without_command=True)
def frr_show_ipv6_nhrp_nhs(show_ipv6_nhrp_nhs_='show_ipv6_nhrp_nhs'):
    """Next hop server information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nhrp_nhs.name
    
    if 'VIEW_NODE|show_ipv6_nhrp_nhs' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_nhs'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_nhs']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_nhs'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nhrp_nhs table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nhrp_nhs'
    pass


@frr_show_ipv6_nhrp_nhs.command('./	<cr>')
def frr_show_ipv6_nhrp_nhs_cr():
    pass


@frr_show_ipv6_nhrp_nhs.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nhrp_nhs_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nhrp_nhs_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nhrp_nhs' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_nhs'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_nhs']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_nhs'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nhrp_nhs table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nhrp_nhs'
    pass


@frr_show_ipv6_nhrp_nhs_json.command('./	<cr>')
def frr_show_ipv6_nhrp_nhs_json_cr():
    pass


@frr_show_ipv6_nhrp.group(cls=FRR_AbbreviationGroup, name='opennhrp', invoke_without_command=True)
def frr_show_ipv6_nhrp_opennhrp(show_ipv6_nhrp_opennhrp_='show_ipv6_nhrp_opennhrp'):
    """opennhrpctl style cache dump"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nhrp_opennhrp.name
    
    if 'VIEW_NODE|show_ipv6_nhrp_opennhrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_opennhrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_opennhrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_opennhrp'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nhrp_opennhrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nhrp_opennhrp'
    pass


@frr_show_ipv6_nhrp_opennhrp.command('./	<cr>')
def frr_show_ipv6_nhrp_opennhrp_cr():
    pass


@frr_show_ipv6_nhrp_opennhrp.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nhrp_opennhrp_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nhrp_opennhrp_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nhrp_opennhrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_opennhrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_opennhrp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_opennhrp'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nhrp_opennhrp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nhrp_opennhrp'
    pass


@frr_show_ipv6_nhrp_opennhrp_json.command('./	<cr>')
def frr_show_ipv6_nhrp_opennhrp_json_cr():
    pass


@frr_show_ipv6_nhrp.group(cls=FRR_AbbreviationGroup, name='shortcut', invoke_without_command=True)
def frr_show_ipv6_nhrp_shortcut(show_ipv6_nhrp_shortcut_='show_ipv6_nhrp_shortcut'):
    """Shortcut information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nhrp_shortcut.name
    
    if 'VIEW_NODE|show_ipv6_nhrp_shortcut' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_shortcut'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_shortcut']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_shortcut'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nhrp_shortcut table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nhrp_shortcut'
    pass


@frr_show_ipv6_nhrp_shortcut.command('./	<cr>')
def frr_show_ipv6_nhrp_shortcut_cr():
    pass


@frr_show_ipv6_nhrp_shortcut.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nhrp_shortcut_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nhrp_shortcut_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nhrp_shortcut' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_shortcut'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_shortcut']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nhrp_shortcut'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nhrp_shortcut table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nhrp_shortcut'
    pass


@frr_show_ipv6_nhrp_shortcut_json.command('./	<cr>')
def frr_show_ipv6_nhrp_shortcut_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='nht', invoke_without_command=True)
def frr_show_ipv6_nht(show_ipv6_nht_='show_ipv6_nht'):
    """IPv6 nexthop tracking table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht.name
    
    if 'VIEW_NODE|show_ipv6_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht'
    pass


@frr_show_ipv6_nht.command('./	<cr>')
def frr_show_ipv6_nht_cr():
    pass


@frr_show_ipv6_nht.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_nht_ipaddress():
    """IPv4 Address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_ipaddress.name
    data_gen['IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht'
    pass


@frr_show_ipv6_nht_ipaddress.command('./	<cr>')
def frr_show_ipv6_nht_ipaddress_cr():
    pass


@frr_show_ipv6_nht_ipaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_ipaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_ipaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht'
    pass


@frr_show_ipv6_nht_ipaddress_json.command('./	<cr>')
def frr_show_ipv6_nht_ipaddress_json_cr():
    pass


@frr_show_ipv6_nht_ipaddress.group(cls=FRR_AbbreviationGroup, name='mrib', invoke_without_command=True)
def frr_show_ipv6_nht_ipaddress_mrib(mrib_='mrib'):
    """Show Multicast (MRIB) NHT state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_ipaddress_mrib.name
    data_gen['mrib'] = mrib_='mrib'
    
    if 'VIEW_NODE|show_ipv6_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht'
    pass


@frr_show_ipv6_nht_ipaddress_mrib.command('./	<cr>')
def frr_show_ipv6_nht_ipaddress_mrib_cr():
    pass


@frr_show_ipv6_nht_ipaddress_mrib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_ipaddress_mrib_json(mrib_json_='mrib_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_ipaddress_mrib_json.name
    data_gen['mrib_json'] = mrib_json_='mrib_json'
    
    if 'VIEW_NODE|show_ipv6_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht'
    pass


@frr_show_ipv6_nht_ipaddress_mrib_json.command('./	<cr>')
def frr_show_ipv6_nht_ipaddress_mrib_json_cr():
    pass


@frr_show_ipv6_nht.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nht' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht'
    pass


@frr_show_ipv6_nht_json.command('./	<cr>')
def frr_show_ipv6_nht_json_cr():
    pass


@frr_show_ipv6_nht.group(cls=FRR_AbbreviationGroup, name='mrib', invoke_without_command=True)
def frr_show_ipv6_nht_mrib(show_ipv6_nht_mrib_='show_ipv6_nht_mrib'):
    """Show Multicast (MRIB) NHT state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_mrib.name
    
    if 'VIEW_NODE|show_ipv6_nht_mrib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_mrib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_mrib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_mrib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_mrib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_mrib'
    pass


@frr_show_ipv6_nht_mrib.command('./	<cr>')
def frr_show_ipv6_nht_mrib_cr():
    pass


@frr_show_ipv6_nht_mrib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_mrib_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_mrib_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nht_mrib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_mrib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_mrib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_mrib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_mrib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_mrib'
    pass


@frr_show_ipv6_nht_mrib_json.command('./	<cr>')
def frr_show_ipv6_nht_mrib_json_cr():
    pass


@frr_show_ipv6_nht.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
def frr_show_ipv6_nht_routemap(show_ipv6_nht_routemap_='show_ipv6_nht_route-map'):
    """IPv6 Next Hop tracking filtering status"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_routemap.name
    
    if 'VIEW_NODE|show_ipv6_nht_route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_route-map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_route-map'
    pass


@frr_show_ipv6_nht_routemap.command('./	<cr>')
def frr_show_ipv6_nht_routemap_cr():
    pass


@frr_show_ipv6_nht_routemap.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_routemap_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_routemap_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nht_route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_route-map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_route-map'
    pass


@frr_show_ipv6_nht_routemap_json.command('./	<cr>')
def frr_show_ipv6_nht_routemap_json_cr():
    pass


@frr_show_ipv6_nht_routemap.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_ipv6_nht_routemap_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_routemap_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_ipv6_nht_route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_route-map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_route-map'
    pass


@frr_show_ipv6_nht_routemap_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['NAME', 'all']), invoke_without_command=True)
def frr_show_ipv6_nht_routemap_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_routemap_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_nht_route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_route-map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_route-map'
    pass


@frr_show_ipv6_nht_routemap_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_ipv6_nht_routemap_vrf_vrfchoicecase_cr():
    pass


@frr_show_ipv6_nht_routemap_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_routemap_vrf_vrfchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_routemap_vrf_vrfchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nht_route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_route-map'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_route-map table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_route-map'
    pass


@frr_show_ipv6_nht_routemap_vrf_vrfchoicecase_json.command('./	<cr>')
def frr_show_ipv6_nht_routemap_vrf_vrfchoicecase_json_cr():
    pass


@frr_show_ipv6_nht.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_ipv6_nht_vrf(the_vrf_name, show_ipv6_nht_vrf_='show_ipv6_nht_vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf.name
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_nht_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf'
    pass


@frr_show_ipv6_nht_vrf.command('./	<cr>')
def frr_show_ipv6_nht_vrf_cr():
    pass


@frr_show_ipv6_nht_vrf.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_ipv6_nht_vrf_all(show_ipv6_nht_vrf_all_='show_ipv6_nht_vrf_all'):
    """All VRFs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_all.name
    
    if 'VIEW_NODE|show_ipv6_nht_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf_all'
    pass


@frr_show_ipv6_nht_vrf_all.command('./	<cr>')
def frr_show_ipv6_nht_vrf_all_cr():
    pass


@frr_show_ipv6_nht_vrf_all.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_vrf_all_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_all_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nht_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf_all'
    pass


@frr_show_ipv6_nht_vrf_all_json.command('./	<cr>')
def frr_show_ipv6_nht_vrf_all_json_cr():
    pass


@frr_show_ipv6_nht_vrf_all.group(cls=FRR_AbbreviationGroup, name='mrib', invoke_without_command=True)
def frr_show_ipv6_nht_vrf_all_mrib(show_ipv6_nht_vrf_all_mrib_='show_ipv6_nht_vrf_all_mrib'):
    """Show Multicast (MRIB) NHT state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_all_mrib.name
    
    if 'VIEW_NODE|show_ipv6_nht_vrf_all_mrib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all_mrib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all_mrib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all_mrib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf_all_mrib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf_all_mrib'
    pass


@frr_show_ipv6_nht_vrf_all_mrib.command('./	<cr>')
def frr_show_ipv6_nht_vrf_all_mrib_cr():
    pass


@frr_show_ipv6_nht_vrf_all_mrib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_vrf_all_mrib_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_all_mrib_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nht_vrf_all_mrib' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all_mrib'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all_mrib']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf_all_mrib'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf_all_mrib table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf_all_mrib'
    pass


@frr_show_ipv6_nht_vrf_all_mrib_json.command('./	<cr>')
def frr_show_ipv6_nht_vrf_all_mrib_json_cr():
    pass


@frr_show_ipv6_nht_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_nht_vrf_ipaddress():
    """IPv4 Address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_ipaddress.name
    data_gen['IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_nht_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf'
    pass


@frr_show_ipv6_nht_vrf_ipaddress.command('./	<cr>')
def frr_show_ipv6_nht_vrf_ipaddress_cr():
    pass


@frr_show_ipv6_nht_vrf_ipaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_vrf_ipaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_ipaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nht_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf'
    pass


@frr_show_ipv6_nht_vrf_ipaddress_json.command('./	<cr>')
def frr_show_ipv6_nht_vrf_ipaddress_json_cr():
    pass


@frr_show_ipv6_nht_vrf_ipaddress.group(cls=FRR_AbbreviationGroup, name='mrib', invoke_without_command=True)
def frr_show_ipv6_nht_vrf_ipaddress_mrib(mrib_='mrib'):
    """Show Multicast (MRIB) NHT state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_ipaddress_mrib.name
    data_gen['mrib'] = mrib_='mrib'
    
    if 'VIEW_NODE|show_ipv6_nht_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf'
    pass


@frr_show_ipv6_nht_vrf_ipaddress_mrib.command('./	<cr>')
def frr_show_ipv6_nht_vrf_ipaddress_mrib_cr():
    pass


@frr_show_ipv6_nht_vrf_ipaddress_mrib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_vrf_ipaddress_mrib_json(mrib_json_='mrib_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_ipaddress_mrib_json.name
    data_gen['mrib_json'] = mrib_json_='mrib_json'
    
    if 'VIEW_NODE|show_ipv6_nht_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf'
    pass


@frr_show_ipv6_nht_vrf_ipaddress_mrib_json.command('./	<cr>')
def frr_show_ipv6_nht_vrf_ipaddress_mrib_json_cr():
    pass


@frr_show_ipv6_nht_vrf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_vrf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_nht_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf'
    pass


@frr_show_ipv6_nht_vrf_json.command('./	<cr>')
def frr_show_ipv6_nht_vrf_json_cr():
    pass


@frr_show_ipv6_nht_vrf.group(cls=FRR_AbbreviationGroup, name='mrib', invoke_without_command=True)
def frr_show_ipv6_nht_vrf_mrib(mrib_='mrib'):
    """Show Multicast (MRIB) NHT state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_mrib.name
    data_gen['mrib'] = mrib_='mrib'
    
    if 'VIEW_NODE|show_ipv6_nht_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf'
    pass


@frr_show_ipv6_nht_vrf_mrib.command('./	<cr>')
def frr_show_ipv6_nht_vrf_mrib_cr():
    pass


@frr_show_ipv6_nht_vrf_mrib.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_nht_vrf_mrib_json(mrib_json_='mrib_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_nht_vrf_mrib_json.name
    data_gen['mrib_json'] = mrib_json_='mrib_json'
    
    if 'VIEW_NODE|show_ipv6_nht_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_nht_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_nht_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_nht_vrf'
    pass


@frr_show_ipv6_nht_vrf_mrib_json.command('./	<cr>')
def frr_show_ipv6_nht_vrf_mrib_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ospf6', invoke_without_command=True)
def frr_show_ipv6_ospf6(show_ipv6_ospf6_='show_ipv6_ospf6'):
    """Open Shortest Path First (OSPF) for IPv6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6.name
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6.command('./	<cr>')
def frr_show_ipv6_ospf6_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='area',)
@click.argument('area_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_area(area_id, area_='area'):
    """Area information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_area.name
    data_gen['area'] = area_='area'
    data_gen['AREA_ID'] = area_id
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_area.group(cls=FRR_AbbreviationGroup, name='spf', invoke_without_command=True)
def frr_show_ipv6_ospf6_area_spf():
    """Show SPF tree"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_area_spf.name
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_area_spf.command('./	<cr>')
def frr_show_ipv6_ospf6_area_spf_cr():
    pass


@frr_show_ipv6_ospf6_area_spf.group(cls=FRR_AbbreviationGroup, name='tree', invoke_without_command=True)
def frr_show_ipv6_ospf6_area_spf_tree(spf_tree_='spf_tree'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_area_spf_tree.name
    data_gen['spf_tree'] = spf_tree_='spf_tree'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_area_spf_tree.command('./	<cr>')
def frr_show_ipv6_ospf6_area_spf_tree_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='border-routers', invoke_without_command=True)
def frr_show_ipv6_ospf6_borderrouters(show_ipv6_ospf6_borderrouters_='show_ipv6_ospf6_border-routers'):
    """Display routing table for ABR and ASBR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_borderrouters.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_border-routers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_border-routers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_border-routers']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_border-routers'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_border-routers table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_border-routers'
    pass


@frr_show_ipv6_ospf6_borderrouters.command('./	<cr>')
def frr_show_ipv6_ospf6_borderrouters_cr():
    pass


@frr_show_ipv6_ospf6_borderrouters.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D', 'detail']), invoke_without_command=True)
def frr_show_ipv6_ospf6_borderrouters_choicecase():
    """Router ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_borderrouters_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_border-routers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_border-routers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_border-routers']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_border-routers'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_border-routers table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_border-routers'
    pass


@frr_show_ipv6_ospf6_borderrouters_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_borderrouters_choicecase_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='database', invoke_without_command=True)
def frr_show_ipv6_ospf6_database(show_ipv6_ospf6_database_='show_ipv6_ospf6_database'):
    """Display Link state database"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database.command('./	<cr>')
def frr_show_ipv6_ospf6_database_cr():
    pass


@frr_show_ipv6_ospf6_database.group(cls=FRR_AbbreviationGroup, name='adv-router',)
def frr_show_ipv6_ospf6_database_advrouter(show_ipv6_ospf6_database_advrouter_='show_ipv6_ospf6_database_adv-router'):
    """Search by Advertising Router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_advrouter.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_adv-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_adv-router table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_adv-router'
    pass


@frr_show_ipv6_ospf6_database_advrouter.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['*']),)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_advrouter_anylinkstateid(specify_advertising_router_as):
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_advrouter_anylinkstateid.name
    data_gen['ANY_LINK_STATE_ID'] = FRR_CLI_ARGS[name]
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_adv-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_adv-router table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_adv-router'
    pass


@frr_show_ipv6_ospf6_database_advrouter_anylinkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_advrouter_anylinkstateid_anylinkstateidchoicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_advrouter_anylinkstateid_anylinkstateidchoicecase.name
    data_gen['ANY-LINK-STATE-ID_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_adv-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_adv-router table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_adv-router'
    pass


@frr_show_ipv6_ospf6_database_advrouter_anylinkstateid_anylinkstateidchoicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_advrouter_anylinkstateid_anylinkstateidchoicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_advrouter_anylinkstateid_anylinkstateidchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_advrouter_anylinkstateid_anylinkstateidchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_advrouter_anylinkstateid_anylinkstateidchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_adv-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_adv-router table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_adv-router'
    pass


@frr_show_ipv6_ospf6_database_advrouter_anylinkstateid_anylinkstateidchoicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_advrouter_anylinkstateid_anylinkstateidchoicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_advrouter.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D']),)
def frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras.name
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_adv-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_adv-router table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_adv-router'
    pass


@frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras.group(cls=FRR_AbbreviationGroup, name='linkstate-id', invoke_without_command=True)
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid(specify_link_state_id, linkstateid_='linkstate-id'):
    """Search by Link state ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid.name
    data_gen['linkstate-id'] = linkstateid_='linkstate-id'
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_adv-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_adv-router table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_adv-router'
    pass


@frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_cr():
    pass


@frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_adv-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_adv-router table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_adv-router'
    pass


@frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_adv-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_adv-router table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_adv-router'
    pass


@frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_adv-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_adv-router'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_adv-router table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_adv-router'
    pass


@frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_advrouter_specifyadvertisingrouteras_linkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_database.group(cls=FRR_AbbreviationGroup, name='aggr',)
def frr_show_ipv6_ospf6_database_aggr(show_ipv6_ospf6_database_aggr_='show_ipv6_ospf6_database_aggr'):
    """Aggregated Router LSA"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_aggr.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_aggr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_aggr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_aggr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_aggr'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_aggr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_aggr'
    pass


@frr_show_ipv6_ospf6_database_aggr.group(cls=FRR_AbbreviationGroup, name='adv-router', invoke_without_command=True)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_aggr_advrouter(specify_advertising_router_as, advrouter_='adv-router'):
    """Search by Advertising Router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_aggr_advrouter.name
    data_gen['adv-router'] = advrouter_='adv-router'
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_aggr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_aggr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_aggr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_aggr'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_aggr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_aggr'
    pass


@frr_show_ipv6_ospf6_database_aggr_advrouter.command('./	<cr>')
def frr_show_ipv6_ospf6_database_aggr_advrouter_cr():
    pass


@frr_show_ipv6_ospf6_database.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['*']),)
def frr_show_ipv6_ospf6_database_anylinkstatetype():
    """4"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_anylinkstatetype.name
    data_gen['ANY_LINK_STATE_TYPE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['*']),)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid(specify_advertising_router_as):
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid.name
    data_gen['ANY_LINK_STATE_ID'] = FRR_CLI_ARGS[name]
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase.name
    data_gen['ANY-LINK-STATE-ID_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D']), invoke_without_command=True)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid(specify_advertising_router_as):
    """Specify Link state ID as IPv4 address notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid.name
    data_gen['SPECIFY_LINK_STATE_ID'] = FRR_CLI_ARGS[name]
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_cr():
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_anylinkstatetype_specifylinkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_database.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_json_cr():
    pass


@frr_show_ipv6_ospf6_database.group(cls=FRR_AbbreviationGroup, name='linkstate-id', invoke_without_command=True)
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_linkstateid(specify_link_state_id, linkstateid_='linkstate-id'):
    """Search by Link state ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_linkstateid.name
    data_gen['linkstate-id'] = linkstateid_='linkstate-id'
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_linkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_database_linkstateid_cr():
    pass


@frr_show_ipv6_ospf6_database_linkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_linkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_linkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_linkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_linkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_linkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_linkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_linkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_linkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_linkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_linkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_linkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_linkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_linkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_linkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_database.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['router', 'network', 'inter-prefix', 'inter-router', 'as-external', 'group-membership', 'type-7', 'link', 'intra-prefix']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord():
    """Display Router LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord.name
    data_gen['LSA_RECORD'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord.group(cls=FRR_AbbreviationGroup, name='adv-router', invoke_without_command=True)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_lsarecord_advrouter(specify_advertising_router_as, advrouter_='adv-router'):
    """Search by Advertising Router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_advrouter.name
    data_gen['adv-router'] = advrouter_='adv-router'
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_advrouter_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_advrouter_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_advrouter_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter.group(cls=FRR_AbbreviationGroup, name='linkstate-id', invoke_without_command=True)
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid(specify_link_state_id, linkstateid_='linkstate-id'):
    """Search by Link state ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid.name
    data_gen['linkstate-id'] = linkstateid_='linkstate-id'
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_choicecase():
    """Dump LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_advrouter_linkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['*']), invoke_without_command=True)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid(specify_advertising_router_as):
    """Any Link state ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid.name
    data_gen['ANY_LINK_STATE_ID'] = FRR_CLI_ARGS[name]
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_anylinkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord.group(cls=FRR_AbbreviationGroup, name='linkstate-id', invoke_without_command=True)
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_lsarecord_linkstateid(specify_link_state_id, linkstateid_='linkstate-id'):
    """Search by Link state ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_linkstateid.name
    data_gen['linkstate-id'] = linkstateid_='linkstate-id'
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_linkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_linkstateid_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_linkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_linkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_linkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_linkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_linkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_linkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_linkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_linkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_linkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_linkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_linkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_linkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_linkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_linkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_linkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord.group(cls=FRR_AbbreviationGroup, name='self-originated', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated(selforiginated_='self-originated'):
    """Display Self-originated LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_selforiginated.name
    data_gen['self-originated'] = selforiginated_='self-originated'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_selforiginated_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_selforiginated_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_selforiginated_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated.group(cls=FRR_AbbreviationGroup, name='linkstate-id', invoke_without_command=True)
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid(specify_link_state_id, linkstateid_='linkstate-id'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid.name
    data_gen['linkstate-id'] = linkstateid_='linkstate-id'
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_selforiginated_linkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D']),)
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid.name
    data_gen['SPECIFY_LINK_STATE_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid.group(cls=FRR_AbbreviationGroup, name='self-originated', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated(selforiginated_='self-originated'):
    """Display Self-originated LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated.name
    data_gen['self-originated'] = selforiginated_='self-originated'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_selforiginated_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras():
    """Specify Advertising Router as IPv4 address notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras.name
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase():
    """Dump LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database'
    pass


@frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_json_cr():
    pass


@frr_show_ipv6_ospf6_database.group(cls=FRR_AbbreviationGroup, name='self-originated', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_selforiginated(show_ipv6_ospf6_database_selforiginated_='show_ipv6_ospf6_database_self-originated'):
    """Display Self-originated LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_selforiginated.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_self-originated' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_self-originated table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_self-originated'
    pass


@frr_show_ipv6_ospf6_database_selforiginated.command('./	<cr>')
def frr_show_ipv6_ospf6_database_selforiginated_cr():
    pass


@frr_show_ipv6_ospf6_database_selforiginated.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_database_selforiginated_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_selforiginated_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_self-originated' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_self-originated table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_self-originated'
    pass


@frr_show_ipv6_ospf6_database_selforiginated_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_database_selforiginated_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_database_selforiginated_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_selforiginated_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_selforiginated_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_self-originated' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_self-originated table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_self-originated'
    pass


@frr_show_ipv6_ospf6_database_selforiginated_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_selforiginated_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_database_selforiginated.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_database_selforiginated_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_database_selforiginated_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_database_self-originated' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_database_self-originated'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_database_self-originated table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_database_self-originated'
    pass


@frr_show_ipv6_ospf6_database_selforiginated_json.command('./	<cr>')
def frr_show_ipv6_ospf6_database_selforiginated_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='graceful-restart', invoke_without_command=True)
def frr_show_ipv6_ospf6_gracefulrestart():
    """ospf6 graceful restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_gracefulrestart.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_graceful-restart' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_graceful-restart table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_graceful-restart'
    pass


@frr_show_ipv6_ospf6_gracefulrestart.command('./	<cr>')
def frr_show_ipv6_ospf6_gracefulrestart_cr():
    pass


@frr_show_ipv6_ospf6_gracefulrestart.group(cls=FRR_AbbreviationGroup, name='helper', invoke_without_command=True)
def frr_show_ipv6_ospf6_gracefulrestart_helper(show_ipv6_ospf6_gracefulrestart_helper_='show_ipv6_ospf6_graceful-restart_helper'):
    """helper details in the router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_gracefulrestart_helper.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_graceful-restart_helper table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_graceful-restart_helper'
    pass


@frr_show_ipv6_ospf6_gracefulrestart_helper.command('./	<cr>')
def frr_show_ipv6_ospf6_gracefulrestart_helper_cr():
    pass


@frr_show_ipv6_ospf6_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_gracefulrestart_helper_detail(show_ipv6_ospf6_gracefulrestart_helper_detail_='show_ipv6_ospf6_graceful-restart_helper_detail'):
    """detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_gracefulrestart_helper_detail.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_graceful-restart_helper_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_graceful-restart_helper_detail'
    pass


@frr_show_ipv6_ospf6_gracefulrestart_helper_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_gracefulrestart_helper_detail_cr():
    pass


@frr_show_ipv6_ospf6_gracefulrestart_helper_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_gracefulrestart_helper_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_gracefulrestart_helper_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_graceful-restart_helper_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_graceful-restart_helper_detail'
    pass


@frr_show_ipv6_ospf6_gracefulrestart_helper_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_gracefulrestart_helper_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_gracefulrestart_helper_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_gracefulrestart_helper_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_graceful-restart_helper'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_graceful-restart_helper table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_graceful-restart_helper'
    pass


@frr_show_ipv6_ospf6_gracefulrestart_helper_json.command('./	<cr>')
def frr_show_ipv6_ospf6_gracefulrestart_helper_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface(show_ipv6_ospf6_interface_='show_ipv6_ospf6_interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_cr():
    pass


@frr_show_ipv6_ospf6_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['IFNAME']), invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_interfacename():
    """Interface name(e.g. ep0)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_interfacename.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_interfacename_cr():
    pass


@frr_show_ipv6_ospf6_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_interfacename_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_interfacename_json_cr():
    pass


@frr_show_ipv6_ospf6_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='prefix', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_interfacename_prefix(prefix_='prefix'):
    """Display connected prefixes to advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_interfacename_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_interfacename_prefix_cr():
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase():
    """Display the route bestmatches the address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['match', 'detail']), invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_routeprefixmatchdetail():
    """Display the route matches the prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_routeprefixmatchdetail.name
    data_gen['ROUTE_PREFIX_MATCH_DETAIL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_routeprefixmatchdetail.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_routeprefixmatchdetail_cr():
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_routeprefixmatchdetail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_routeprefixmatchdetail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_routeprefixmatchdetail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_routeprefixmatchdetail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_interfacename_prefix_choicecase_routeprefixmatchdetail_json_cr():
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_interfacename_prefix_detail(prefix_detail_='prefix_detail'):
    """Display details of the prefixes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_interfacename_prefix_detail.name
    data_gen['prefix_detail'] = prefix_detail_='prefix_detail'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_interfacename_prefix_detail_cr():
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_interfacename_prefix_detail_json(prefix_detail_json_='prefix_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_interfacename_prefix_detail_json.name
    data_gen['prefix_detail_json'] = prefix_detail_json_='prefix_detail_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_interfacename_prefix_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_interfacename_prefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_interfacename_prefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_interfacename_prefix_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_interfacename_prefix_json_cr():
    pass


@frr_show_ipv6_ospf6_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface'
    pass


@frr_show_ipv6_ospf6_interface_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_json_cr():
    pass


@frr_show_ipv6_ospf6_interface.group(cls=FRR_AbbreviationGroup, name='prefix', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_prefix(show_ipv6_ospf6_interface_prefix_='show_ipv6_ospf6_interface_prefix'):
    """Display connected prefixes to advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_prefix.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_prefix' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_prefix table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_prefix'
    pass


@frr_show_ipv6_ospf6_interface_prefix.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_prefix_cr():
    pass


@frr_show_ipv6_ospf6_interface_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['X:X::X:X', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_prefix_choicecase():
    """Display the route bestmatches the address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_prefix_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_prefix' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_prefix table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_prefix'
    pass


@frr_show_ipv6_ospf6_interface_prefix_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_prefix_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_interface_prefix_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_prefix_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_prefix_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_prefix' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_prefix table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_prefix'
    pass


@frr_show_ipv6_ospf6_interface_prefix_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_prefix_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_interface_prefix_choicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['match', 'detail']), invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_prefix_choicecase_routeprefixmatchdetail():
    """Display the route matches the prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_prefix_choicecase_routeprefixmatchdetail.name
    data_gen['ROUTE_PREFIX_MATCH_DETAIL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_prefix' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_prefix table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_prefix'
    pass


@frr_show_ipv6_ospf6_interface_prefix_choicecase_routeprefixmatchdetail.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_prefix_choicecase_routeprefixmatchdetail_cr():
    pass


@frr_show_ipv6_ospf6_interface_prefix_choicecase_routeprefixmatchdetail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_prefix_choicecase_routeprefixmatchdetail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_prefix_choicecase_routeprefixmatchdetail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_prefix' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_prefix table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_prefix'
    pass


@frr_show_ipv6_ospf6_interface_prefix_choicecase_routeprefixmatchdetail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_prefix_choicecase_routeprefixmatchdetail_json_cr():
    pass


@frr_show_ipv6_ospf6_interface_prefix.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_prefix_detail(show_ipv6_ospf6_interface_prefix_detail_='show_ipv6_ospf6_interface_prefix_detail'):
    """Display details of the prefixes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_prefix_detail.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_prefix_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_prefix_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_prefix_detail'
    pass


@frr_show_ipv6_ospf6_interface_prefix_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_prefix_detail_cr():
    pass


@frr_show_ipv6_ospf6_interface_prefix_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_prefix_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_prefix_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_prefix_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_prefix_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_prefix_detail'
    pass


@frr_show_ipv6_ospf6_interface_prefix_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_prefix_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_interface_prefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_prefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_prefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_prefix' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_prefix'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_prefix table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_prefix'
    pass


@frr_show_ipv6_ospf6_interface_prefix_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_prefix_json_cr():
    pass


@frr_show_ipv6_ospf6_interface.group(cls=FRR_AbbreviationGroup, name='traffic', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_traffic(show_ipv6_ospf6_interface_traffic_='show_ipv6_ospf6_interface_traffic'):
    """Protocol Packet counters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_traffic.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_traffic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_traffic table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_traffic'
    pass


@frr_show_ipv6_ospf6_interface_traffic.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_traffic_cr():
    pass


@frr_show_ipv6_ospf6_interface_traffic.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['IFNAME']), invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_traffic_interfacename():
    """Interface name(e.g. ep0)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_traffic_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_traffic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_traffic table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_traffic'
    pass


@frr_show_ipv6_ospf6_interface_traffic_interfacename.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_traffic_interfacename_cr():
    pass


@frr_show_ipv6_ospf6_interface_traffic_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_traffic_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_traffic_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_traffic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_traffic table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_traffic'
    pass


@frr_show_ipv6_ospf6_interface_traffic_interfacename_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_traffic_interfacename_json_cr():
    pass


@frr_show_ipv6_ospf6_interface_traffic.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_interface_traffic_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_interface_traffic_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_interface_traffic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_interface_traffic'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_interface_traffic table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_interface_traffic'
    pass


@frr_show_ipv6_ospf6_interface_traffic_json.command('./	<cr>')
def frr_show_ipv6_ospf6_interface_traffic_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_json.command('./	<cr>')
def frr_show_ipv6_ospf6_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='linkstate', invoke_without_command=True)
def frr_show_ipv6_ospf6_linkstate(show_ipv6_ospf6_linkstate_='show_ipv6_ospf6_linkstate'):
    """Display linkstate routing table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_linkstate.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_linkstate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_linkstate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_linkstate'
    pass


@frr_show_ipv6_ospf6_linkstate.command('./	<cr>')
def frr_show_ipv6_ospf6_linkstate_cr():
    pass


@frr_show_ipv6_ospf6_linkstate.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_linkstate_detail(detail_='detail'):
    """Display detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_linkstate_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_ipv6_ospf6_linkstate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_linkstate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_linkstate'
    pass


@frr_show_ipv6_ospf6_linkstate_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_linkstate_detail_cr():
    pass


@frr_show_ipv6_ospf6_linkstate.group(cls=FRR_AbbreviationGroup, name='network', invoke_without_command=True)
@click.argument('specify_router_id_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_linkstate_network(specify_link_state_id, specify_router_id_as, network_='network'):
    """Display Network Entry"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_linkstate_network.name
    data_gen['network'] = network_='network'
    data_gen['SPECIFY_ROUTER_ID_AS'] = specify_router_id_as
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6_linkstate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_linkstate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_linkstate'
    pass


@frr_show_ipv6_ospf6_linkstate_network.command('./	<cr>')
def frr_show_ipv6_ospf6_linkstate_network_cr():
    pass


@frr_show_ipv6_ospf6_linkstate.group(cls=FRR_AbbreviationGroup, name='router', invoke_without_command=True)
@click.argument('specify_router_id_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_linkstate_router(specify_router_id_as, router_='router'):
    """Display Router Entry"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_linkstate_router.name
    data_gen['router'] = router_='router'
    data_gen['SPECIFY_ROUTER_ID_AS'] = specify_router_id_as
    
    if 'VIEW_NODE|show_ipv6_ospf6_linkstate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_linkstate'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_linkstate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_linkstate'
    pass


@frr_show_ipv6_ospf6_linkstate_router.command('./	<cr>')
def frr_show_ipv6_ospf6_linkstate_router_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
def frr_show_ipv6_ospf6_neighbor(show_ipv6_ospf6_neighbor_='show_ipv6_ospf6_neighbor'):
    """Neighbor list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_neighbor.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_neighbor'
    pass


@frr_show_ipv6_ospf6_neighbor.command('./	<cr>')
def frr_show_ipv6_ospf6_neighbor_cr():
    pass


@frr_show_ipv6_ospf6_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['detail', 'drchoice']), invoke_without_command=True)
def frr_show_ipv6_ospf6_neighbor_choicecase():
    """Display details"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_neighbor_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_neighbor'
    pass


@frr_show_ipv6_ospf6_neighbor_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_neighbor_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_neighbor_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_neighbor_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_neighbor_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_neighbor'
    pass


@frr_show_ipv6_ospf6_neighbor_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_neighbor_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_neighbor'
    pass


@frr_show_ipv6_ospf6_neighbor_json.command('./	<cr>')
def frr_show_ipv6_ospf6_neighbor_json_cr():
    pass


@frr_show_ipv6_ospf6_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D']), invoke_without_command=True)
def frr_show_ipv6_ospf6_neighbor_specifyrouteridasipv4():
    """Specify Router-ID as IPv4 address notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_neighbor_specifyrouteridasipv4.name
    data_gen['SPECIFY_ROUTER-ID_AS_IPV4'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_neighbor'
    pass


@frr_show_ipv6_ospf6_neighbor_specifyrouteridasipv4.command('./	<cr>')
def frr_show_ipv6_ospf6_neighbor_specifyrouteridasipv4_cr():
    pass


@frr_show_ipv6_ospf6_neighbor_specifyrouteridasipv4.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_neighbor_specifyrouteridasipv4_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_neighbor_specifyrouteridasipv4_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_neighbor'
    pass


@frr_show_ipv6_ospf6_neighbor_specifyrouteridasipv4_json.command('./	<cr>')
def frr_show_ipv6_ospf6_neighbor_specifyrouteridasipv4_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
def frr_show_ipv6_ospf6_redistribute(show_ipv6_ospf6_redistribute_='show_ipv6_ospf6_redistribute'):
    """redistributing External information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_redistribute.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_redistribute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_redistribute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_redistribute'
    pass


@frr_show_ipv6_ospf6_redistribute.command('./	<cr>')
def frr_show_ipv6_ospf6_redistribute_cr():
    pass


@frr_show_ipv6_ospf6_redistribute.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_redistribute_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_redistribute_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_redistribute'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_redistribute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_redistribute'
    pass


@frr_show_ipv6_ospf6_redistribute_json.command('./	<cr>')
def frr_show_ipv6_ospf6_redistribute_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
def frr_show_ipv6_ospf6_route(show_ipv6_ospf6_route_='show_ipv6_ospf6_route'):
    """Routing Table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route.command('./	<cr>')
def frr_show_ipv6_ospf6_route_cr():
    pass


@frr_show_ipv6_ospf6_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['X:X::X:X', 'detail', 'summary']), invoke_without_command=True)
def frr_show_ipv6_ospf6_route_choicecase():
    """Specify IPv6 address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_route_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_route_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_route_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_route_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_route.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_route_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_json.command('./	<cr>')
def frr_show_ipv6_ospf6_route_json_cr():
    pass


@frr_show_ipv6_ospf6_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['intra-area', 'inter-area', 'external-1', 'external-2']),)
def frr_show_ipv6_ospf6_route_routetypefilter():
    """4"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_routetypefilter.name
    data_gen['ROUTE_TYPE_FILTER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_routetypefilter.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_route_routetypefilter_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_routetypefilter_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_routetypefilter_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_route_routetypefilter_detail_cr():
    pass


@frr_show_ipv6_ospf6_route_routetypefilter_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_route_routetypefilter_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_routetypefilter_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_routetypefilter_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_route_routetypefilter_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['X:X::X:X/M']),)
def frr_show_ipv6_ospf6_route_specifyipv6prefix():
    """4"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_specifyipv6prefix.name
    data_gen['SPECIFY_IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer', invoke_without_command=True)
def frr_show_ipv6_ospf6_route_specifyipv6prefix_longer(longer_='longer'):
    """Display routes longer than the specified route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_specifyipv6prefix_longer.name
    data_gen['longer'] = longer_='longer'
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix_longer.command('./	<cr>')
def frr_show_ipv6_ospf6_route_specifyipv6prefix_longer_cr():
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix_longer.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_route_specifyipv6prefix_longer_json(longer_json_='longer_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_specifyipv6prefix_longer_json.name
    data_gen['longer_json'] = longer_json_='longer_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix_longer_json.command('./	<cr>')
def frr_show_ipv6_ospf6_route_specifyipv6prefix_longer_json_cr():
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix.group(cls=FRR_AbbreviationGroup, name='match', invoke_without_command=True)
def frr_show_ipv6_ospf6_route_specifyipv6prefix_match(match_='match'):
    """Display routes which match the specified route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_specifyipv6prefix_match.name
    data_gen['match'] = match_='match'
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix_match.command('./	<cr>')
def frr_show_ipv6_ospf6_route_specifyipv6prefix_match_cr():
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix_match.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_route_specifyipv6prefix_match_detail(match_detail_='match_detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_specifyipv6prefix_match_detail.name
    data_gen['match_detail'] = match_detail_='match_detail'
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix_match_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_route_specifyipv6prefix_match_detail_cr():
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix_match_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_route_specifyipv6prefix_match_detail_json(match_detail_json_='match_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_specifyipv6prefix_match_detail_json.name
    data_gen['match_detail_json'] = match_detail_json_='match_detail_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix_match_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_route_specifyipv6prefix_match_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix_match.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_route_specifyipv6prefix_match_json(match_json_='match_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_route_specifyipv6prefix_match_json.name
    data_gen['match_json'] = match_json_='match_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_route'
    pass


@frr_show_ipv6_ospf6_route_specifyipv6prefix_match_json.command('./	<cr>')
def frr_show_ipv6_ospf6_route_specifyipv6prefix_match_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='simulate',)
def frr_show_ipv6_ospf6_simulate(show_ipv6_ospf6_simulate_='show_ipv6_ospf6_simulate'):
    """Shortest Path First calculation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_simulate.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_simulate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_simulate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_simulate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_simulate'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_simulate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_simulate'
    pass


@frr_show_ipv6_ospf6_simulate.group(cls=FRR_AbbreviationGroup, name='spf-tree',)
@click.argument('specify_root_routerid_to', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_simulate_spftree(specify_root_routerid_to, spftree_='spf-tree'):
    """Show SPF tree"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_simulate_spftree.name
    data_gen['spf-tree'] = spftree_='spf-tree'
    data_gen['SPECIFY_ROOT_ROUTER-ID_TO'] = specify_root_routerid_to
    
    if 'VIEW_NODE|show_ipv6_ospf6_simulate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_simulate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_simulate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_simulate'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_simulate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_simulate'
    pass


@frr_show_ipv6_ospf6_simulate_spftree.group(cls=FRR_AbbreviationGroup, name='area', invoke_without_command=True)
@click.argument('area_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_simulate_spftree_area(area_id, area_='area'):
    """OSPF6 area parameters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_simulate_spftree_area.name
    data_gen['area'] = area_='area'
    data_gen['AREA_ID'] = area_id
    
    if 'VIEW_NODE|show_ipv6_ospf6_simulate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_simulate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_simulate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_simulate'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_simulate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_simulate'
    pass


@frr_show_ipv6_ospf6_simulate_spftree_area.command('./	<cr>')
def frr_show_ipv6_ospf6_simulate_spftree_area_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='spf', invoke_without_command=True)
def frr_show_ipv6_ospf6_spf():
    """Shortest Path First calculation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_spf.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_spf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_spf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_spf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_spf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_spf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_spf'
    pass


@frr_show_ipv6_ospf6_spf.command('./	<cr>')
def frr_show_ipv6_ospf6_spf_cr():
    pass


@frr_show_ipv6_ospf6_spf.group(cls=FRR_AbbreviationGroup, name='tree', invoke_without_command=True)
def frr_show_ipv6_ospf6_spf_tree(show_ipv6_ospf6_spf_tree_='show_ipv6_ospf6_spf_tree'):
    """Show SPF tree"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_spf_tree.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_spf_tree' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_spf_tree'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_spf_tree']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_spf_tree'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_spf_tree table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_spf_tree'
    pass


@frr_show_ipv6_ospf6_spf_tree.command('./	<cr>')
def frr_show_ipv6_ospf6_spf_tree_cr():
    pass


@frr_show_ipv6_ospf6_spf_tree.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_spf_tree_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_spf_tree_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_spf_tree' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_spf_tree'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_spf_tree']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_spf_tree'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_spf_tree table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_spf_tree'
    pass


@frr_show_ipv6_ospf6_spf_tree_json.command('./	<cr>')
def frr_show_ipv6_ospf6_spf_tree_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='summary-address', invoke_without_command=True)
def frr_show_ipv6_ospf6_summaryaddress(show_ipv6_ospf6_summaryaddress_='show_ipv6_ospf6_summary-address'):
    """Show external summary addresses"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_summaryaddress.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_summary-address table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_summary-address'
    pass


@frr_show_ipv6_ospf6_summaryaddress.command('./	<cr>')
def frr_show_ipv6_ospf6_summaryaddress_cr():
    pass


@frr_show_ipv6_ospf6_summaryaddress.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_summaryaddress_detail(show_ipv6_ospf6_summaryaddress_detail_='show_ipv6_ospf6_summary-address_detail'):
    """detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_summaryaddress_detail.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_summary-address_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_summary-address_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_summary-address_detail'
    pass


@frr_show_ipv6_ospf6_summaryaddress_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_summaryaddress_detail_cr():
    pass


@frr_show_ipv6_ospf6_summaryaddress_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_summaryaddress_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_summaryaddress_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_summary-address_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_summary-address_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_summary-address_detail'
    pass


@frr_show_ipv6_ospf6_summaryaddress_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_summaryaddress_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_summaryaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_summaryaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_summaryaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_summary-address'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_summary-address table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_summary-address'
    pass


@frr_show_ipv6_ospf6_summaryaddress_json.command('./	<cr>')
def frr_show_ipv6_ospf6_summaryaddress_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_ipv6_ospf6_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['NAME', 'all']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='area',)
@click.argument('area_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_area(area_id, area_='area'):
    """Area information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_area.name
    data_gen['area'] = area_='area'
    data_gen['AREA_ID'] = area_id
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_area.group(cls=FRR_AbbreviationGroup, name='spf', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_area_spf():
    """Show SPF tree"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_area_spf.name
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_area_spf.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_area_spf_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_area_spf.group(cls=FRR_AbbreviationGroup, name='tree', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_area_spf_tree(spf_tree_='spf_tree'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_area_spf_tree.name
    data_gen['spf_tree'] = spf_tree_='spf_tree'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_area_spf_tree.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_area_spf_tree_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='border-routers', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_borderrouters(borderrouters_='border-routers'):
    """Display routing table for ABR and ASBR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_borderrouters.name
    data_gen['border-routers'] = borderrouters_='border-routers'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_borderrouters.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_borderrouters_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_borderrouters.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D', 'detail']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_borderrouters_choicecase():
    """Router ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_borderrouters_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_borderrouters_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_borderrouters_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='database', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database(database_='database'):
    """Display Link state database"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database.name
    data_gen['database'] = database_='database'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name='adv-router',)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter(specify_advertising_router_as, advrouter_='adv-router'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter.name
    data_gen['adv-router'] = advrouter_='adv-router'
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter.group(cls=FRR_AbbreviationGroup, name='linkstate-id', invoke_without_command=True)
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid(specify_link_state_id, linkstateid_='linkstate-id'):
    """Search by Link state ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid.name
    data_gen['linkstate-id'] = linkstateid_='linkstate-id'
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_advrouter_linkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name='aggr',)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_aggr():
    """"""
    global COMMON_DATA_MAP
    
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_aggr.group(cls=FRR_AbbreviationGroup, name='adv-router', invoke_without_command=True)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_aggr_advrouter(specify_advertising_router_as, database_aggr_advrouter_='database_aggr_adv-router'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_aggr_advrouter.name
    data_gen['database_aggr_adv-router'] = database_aggr_advrouter_='database_aggr_adv-router'
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_aggr_advrouter.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_aggr_advrouter_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['*']),)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype.name
    data_gen['ANY_LINK_STATE_TYPE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['*']),)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid(specify_advertising_router_as):
    """8"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid.name
    data_gen['ANY_LINK_STATE_ID'] = FRR_CLI_ARGS[name]
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase.name
    data_gen['ANY-LINK-STATE-ID_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_anylinkstateid_anylinkstateidchoicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['A.B.C.D']), invoke_without_command=True)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid(specify_advertising_router_as):
    """Specify Link state ID as IPv4 address notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid.name
    data_gen['SPECIFY_LINK_STATE_ID'] = FRR_CLI_ARGS[name]
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_anylinkstatetype_specifylinkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name='linkstate-id', invoke_without_command=True)
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid(specify_link_state_id, linkstateid_='linkstate-id'):
    """Search by Link state ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid.name
    data_gen['linkstate-id'] = linkstateid_='linkstate-id'
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_linkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['router', 'network', 'inter-prefix', 'inter-router', 'as-external', 'group-membership', 'type-7', 'link', 'intra-prefix']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord():
    """Display Router LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord.name
    data_gen['LSA_RECORD'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord.group(cls=FRR_AbbreviationGroup, name='adv-router', invoke_without_command=True)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter(specify_advertising_router_as, advrouter_='adv-router'):
    """Search by Advertising Router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter.name
    data_gen['adv-router'] = advrouter_='adv-router'
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter.group(cls=FRR_AbbreviationGroup, name='linkstate-id', invoke_without_command=True)
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid(specify_link_state_id, linkstateid_='linkstate-id'):
    """Search by Link state ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid.name
    data_gen['linkstate-id'] = linkstateid_='linkstate-id'
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_choicecase():
    """Dump LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_advrouter_linkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['*']), invoke_without_command=True)
@click.argument('specify_advertising_router_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid(specify_advertising_router_as):
    """Any Link state ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid.name
    data_gen['ANY_LINK_STATE_ID'] = FRR_CLI_ARGS[name]
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = specify_advertising_router_as
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_anylinkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord.group(cls=FRR_AbbreviationGroup, name='linkstate-id', invoke_without_command=True)
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid(specify_link_state_id, linkstateid_='linkstate-id'):
    """Search by Link state ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid.name
    data_gen['linkstate-id'] = linkstateid_='linkstate-id'
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_linkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord.group(cls=FRR_AbbreviationGroup, name='self-originated', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated(selforiginated_='self-originated'):
    """Display Self-originated LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated.name
    data_gen['self-originated'] = selforiginated_='self-originated'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated.group(cls=FRR_AbbreviationGroup, name='linkstate-id', invoke_without_command=True)
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid(specify_link_state_id, linkstateid_='linkstate-id'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid.name
    data_gen['linkstate-id'] = linkstateid_='linkstate-id'
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_selforiginated_linkstateid_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['A.B.C.D']),)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid():
    """8"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid.name
    data_gen['SPECIFY_LINK_STATE_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid.group(cls=FRR_AbbreviationGroup, name='self-originated', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated(selforiginated_='self-originated'):
    """Display Self-originated LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated.name
    data_gen['self-originated'] = selforiginated_='self-originated'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_selforiginated_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['A.B.C.D']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras():
    """Specify Advertising Router as IPv4 address notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras.name
    data_gen['SPECIFY_ADVERTISING_ROUTER_AS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase():
    """Dump LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_lsarecord_specifylinkstateid_specifyadvertisingrouteras_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name='self-originated', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated(database_selforiginated_='database_self-originated'):
    """Display Self-originated LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated.name
    data_gen['database_self-originated'] = database_selforiginated_='database_self-originated'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['detail', 'dump', 'internal']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_choicecase():
    """Display details of LSAs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_database_selforiginated_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface(interface_='interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface.name
    data_gen['interface'] = interface_='interface'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['IFNAME']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename():
    """Interface name(e.g. ep0)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='prefix', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix(prefix_='prefix'):
    """Display connected prefixes to advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_detail(prefix_detail_='prefix_detail'):
    """Display details of the prefixes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_detail.name
    data_gen['prefix_detail'] = prefix_detail_='prefix_detail'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_detail_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_detail_json(prefix_detail_json_='prefix_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_detail_json.name
    data_gen['prefix_detail_json'] = prefix_detail_json_='prefix_detail_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['X:X::X:X', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase():
    """Display the route bestmatches the address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase.name
    data_gen['SECOND_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['match', 'detail']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_routeprefixmatchdetail():
    """Display the route matches the prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_routeprefixmatchdetail.name
    data_gen['ROUTE_PREFIX_MATCH_DETAIL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_routeprefixmatchdetail.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_routeprefixmatchdetail_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_routeprefixmatchdetail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_routeprefixmatchdetail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_routeprefixmatchdetail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_routeprefixmatchdetail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_interfacename_prefix_secondchoicecase_routeprefixmatchdetail_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface.group(cls=FRR_AbbreviationGroup, name='prefix', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix(interface_prefix_='interface_prefix'):
    """Display connected prefixes to advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix.name
    data_gen['interface_prefix'] = interface_prefix_='interface_prefix'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_detail(interface_prefix_detail_='interface_prefix_detail'):
    """Display details of the prefixes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_detail.name
    data_gen['interface_prefix_detail'] = interface_prefix_detail_='interface_prefix_detail'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_detail_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_detail_json(interface_prefix_detail_json_='interface_prefix_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_detail_json.name
    data_gen['interface_prefix_detail_json'] = interface_prefix_detail_json_='interface_prefix_detail_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['X:X::X:X', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase():
    """Display the route bestmatches the address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase.name
    data_gen['SECOND_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['match', 'detail']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_routeprefixmatchdetail():
    """Display the route matches the prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_routeprefixmatchdetail.name
    data_gen['ROUTE_PREFIX_MATCH_DETAIL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_routeprefixmatchdetail.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_routeprefixmatchdetail_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_routeprefixmatchdetail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_routeprefixmatchdetail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_routeprefixmatchdetail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_routeprefixmatchdetail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_prefix_secondchoicecase_routeprefixmatchdetail_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface.group(cls=FRR_AbbreviationGroup, name='traffic', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic(interface_traffic_='interface_traffic'):
    """Protocol Packet counters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic.name
    data_gen['interface_traffic'] = interface_traffic_='interface_traffic'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['IFNAME']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_interfacename():
    """Interface name(e.g. ep0)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_interfacename.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_interfacename_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_interfacename_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_interfacename_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_interface_traffic_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='linkstate', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate(linkstate_='linkstate'):
    """Display linkstate routing table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate.name
    data_gen['linkstate'] = linkstate_='linkstate'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_detail(linkstate_detail_='linkstate_detail'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_detail.name
    data_gen['linkstate_detail'] = linkstate_detail_='linkstate_detail'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_detail_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate.group(cls=FRR_AbbreviationGroup, name='network', invoke_without_command=True)
@click.argument('specify_router_id_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
@click.argument('specify_link_state_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_network(specify_link_state_id, specify_router_id_as, linkstate_network_='linkstate_network'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_network.name
    data_gen['linkstate_network'] = linkstate_network_='linkstate_network'
    data_gen['SPECIFY_ROUTER_ID_AS'] = specify_router_id_as
    data_gen['SPECIFY_LINK_STATE_ID'] = specify_link_state_id
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_network.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_network_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate.group(cls=FRR_AbbreviationGroup, name='router', invoke_without_command=True)
@click.argument('specify_router_id_as', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_router(specify_router_id_as, linkstate_router_='linkstate_router'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_router.name
    data_gen['linkstate_router'] = linkstate_router_='linkstate_router'
    data_gen['SPECIFY_ROUTER_ID_AS'] = specify_router_id_as
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_router.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_linkstate_router_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor(neighbor_='neighbor'):
    """Neighbor list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['detail', 'drchoice']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_choicecase():
    """Display details"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_specifyrouteridasipv4():
    """Specify Router-ID as IPv4 address notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_specifyrouteridasipv4.name
    data_gen['SPECIFY_ROUTER-ID_AS_IPV4'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_specifyrouteridasipv4.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_specifyrouteridasipv4_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_specifyrouteridasipv4.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_specifyrouteridasipv4_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_specifyrouteridasipv4_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_specifyrouteridasipv4_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_neighbor_specifyrouteridasipv4_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_redistribute(redistribute_='redistribute'):
    """redistributing External information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_redistribute.name
    data_gen['redistribute'] = redistribute_='redistribute'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_redistribute.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_redistribute_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_redistribute.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_redistribute_json(redistribute_json_='redistribute_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_redistribute_json.name
    data_gen['redistribute_json'] = redistribute_json_='redistribute_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_redistribute_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_redistribute_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route(route_='route'):
    """Routing Table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route.name
    data_gen['route'] = route_='route'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X', 'detail', 'summary']), invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_choicecase():
    """Specify IPv6 address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_choicecase.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_choicecase_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_choicecase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_choicecase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_choicecase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_choicecase_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_choicecase_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)

def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_json(json_='json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['intra-area', 'inter-area', 'external-1', 'external-2']),)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter.name
    data_gen['ROUTE_TYPE_FILTER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter_detail_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_routetypefilter_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X/M']),)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix.name
    data_gen['SPECIFY_IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_longer(longer_='longer'):
    """Display routes longer than the specified route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_longer.name
    data_gen['longer'] = longer_='longer'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_longer.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_longer_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_longer.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_longer_json(longer_json_='longer_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_longer_json.name
    data_gen['longer_json'] = longer_json_='longer_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_longer_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_longer_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix.group(cls=FRR_AbbreviationGroup, name='match', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match(match_='match'):
    """Display routes which match the specified route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match.name
    data_gen['match'] = match_='match'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_detail(match_detail_='match_detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_detail.name
    data_gen['match_detail'] = match_detail_='match_detail'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_detail_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_detail_json(match_detail_json_='match_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_detail_json.name
    data_gen['match_detail_json'] = match_detail_json_='match_detail_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_json(match_json_='match_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_json.name
    data_gen['match_json'] = match_json_='match_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_route_specifyipv6prefix_match_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='simulate',)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_simulate():
    """Show SPF tree"""
    global COMMON_DATA_MAP
    
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_simulate.group(cls=FRR_AbbreviationGroup, name='spf-tree',)
@click.argument('specify_root_routerid_to', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_simulate_spftree(specify_root_routerid_to, simulate_spftree_='simulate_spf-tree'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_simulate_spftree.name
    data_gen['simulate_spf-tree'] = simulate_spftree_='simulate_spf-tree'
    data_gen['SPECIFY_ROOT_ROUTER-ID_TO'] = specify_root_routerid_to
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_simulate_spftree.group(cls=FRR_AbbreviationGroup, name='area', invoke_without_command=True)
@click.argument('area_id', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_simulate_spftree_area(area_id, area_='area'):
    """OSPF6 area parameters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_simulate_spftree_area.name
    data_gen['area'] = area_='area'
    data_gen['AREA_ID'] = area_id
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_simulate_spftree_area.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_simulate_spftree_area_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='spf', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf():
    """Shortest Path First calculation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf.name
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf.group(cls=FRR_AbbreviationGroup, name='tree', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf_tree(spf_tree_='spf_tree'):
    """Show SPF tree"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf_tree.name
    data_gen['spf_tree'] = spf_tree_='spf_tree'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf_tree.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf_tree_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf_tree.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf_tree_json(spf_tree_json_='spf_tree_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf_tree_json.name
    data_gen['spf_tree_json'] = spf_tree_json_='spf_tree_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf_tree_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_spf_tree_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='summary-address', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress(summaryaddress_='summary-address'):
    """Show external summary addresses"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress.name
    data_gen['summary-address'] = summaryaddress_='summary-address'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_detail(summaryaddress_detail_='summary-address_detail'):
    """detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_detail.name
    data_gen['summary-address_detail'] = summaryaddress_detail_='summary-address_detail'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_detail.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_detail_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_detail_json(summaryaddress_detail_json_='summary-address_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_detail_json.name
    data_gen['summary-address_detail_json'] = summaryaddress_detail_json_='summary-address_detail_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_detail_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_detail_json_cr():
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_json(summaryaddress_json_='summary-address_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_json.name
    data_gen['summary-address_json'] = summaryaddress_json_='summary-address_json'
    
    if 'VIEW_NODE|show_ipv6_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6 table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6'
    pass


@frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrf_vrfchoicecase_summaryaddress_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='vrfs', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrfs(show_ipv6_ospf6_vrfs_='show_ipv6_ospf6_vrfs'):
    """Show OSPF6 VRFs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrfs.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_vrfs' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_vrfs'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_vrfs']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_vrfs'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_vrfs table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_vrfs'
    pass


@frr_show_ipv6_ospf6_vrfs.command('./	<cr>')
def frr_show_ipv6_ospf6_vrfs_cr():
    pass


@frr_show_ipv6_ospf6_vrfs.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_vrfs_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_vrfs_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_vrfs' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_vrfs'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_vrfs']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_vrfs'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_vrfs table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_vrfs'
    pass


@frr_show_ipv6_ospf6_vrfs_json.command('./	<cr>')
def frr_show_ipv6_ospf6_vrfs_json_cr():
    pass


@frr_show_ipv6_ospf6.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_show_ipv6_ospf6_zebra(show_ipv6_ospf6_zebra_='show_ipv6_ospf6_zebra'):
    """Zebra information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_zebra.name
    
    if 'VIEW_NODE|show_ipv6_ospf6_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_zebra'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_zebra'
    pass


@frr_show_ipv6_ospf6_zebra.command('./	<cr>')
def frr_show_ipv6_ospf6_zebra_cr():
    pass


@frr_show_ipv6_ospf6_zebra.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_ospf6_zebra_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ospf6_zebra_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_ospf6_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ospf6_zebra'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ospf6_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ospf6_zebra'
    pass


@frr_show_ipv6_ospf6_zebra_json.command('./	<cr>')
def frr_show_ipv6_ospf6_zebra_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='pim',)
def frr_show_ipv6_pim(show_ipv6_pim_='show_ipv6_pim'):
    """PIM information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim.name
    
    if 'VIEW_NODE|show_ipv6_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim'
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='bsm-database', invoke_without_command=True)
def frr_show_ipv6_pim_bsmdatabase(show_ipv6_pim_bsmdatabase_='show_ipv6_pim_bsm-database'):
    """PIM cached bsm packets information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsmdatabase.name
    
    if 'VIEW_NODE|show_ipv6_pim_bsm-database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsm-database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsm-database'
    pass


@frr_show_ipv6_pim_bsmdatabase.command('./	<cr>')
def frr_show_ipv6_pim_bsmdatabase_cr():
    pass


@frr_show_ipv6_pim_bsmdatabase.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_bsmdatabase_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsmdatabase_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_bsm-database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsm-database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsm-database'
    pass


@frr_show_ipv6_pim_bsmdatabase_json.command('./	<cr>')
def frr_show_ipv6_pim_bsmdatabase_json_cr():
    pass


@frr_show_ipv6_pim_bsmdatabase.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_ipv6_pim_bsmdatabase_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsmdatabase_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_pim_bsm-database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsm-database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsm-database'
    pass


@frr_show_ipv6_pim_bsmdatabase_vrf.command('./	<cr>')
def frr_show_ipv6_pim_bsmdatabase_vrf_cr():
    pass


@frr_show_ipv6_pim_bsmdatabase_vrf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_bsmdatabase_vrf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsmdatabase_vrf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_bsm-database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsm-database'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsm-database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsm-database'
    pass


@frr_show_ipv6_pim_bsmdatabase_vrf_json.command('./	<cr>')
def frr_show_ipv6_pim_bsmdatabase_vrf_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='bsr', invoke_without_command=True)
def frr_show_ipv6_pim_bsr(show_ipv6_pim_bsr_='show_ipv6_pim_bsr'):
    """boot-strap router information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsr.name
    
    if 'VIEW_NODE|show_ipv6_pim_bsr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsr'
    pass


@frr_show_ipv6_pim_bsr.command('./	<cr>')
def frr_show_ipv6_pim_bsr_cr():
    pass


@frr_show_ipv6_pim_bsr.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_bsr_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsr_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_bsr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsr'
    pass


@frr_show_ipv6_pim_bsr_json.command('./	<cr>')
def frr_show_ipv6_pim_bsr_json_cr():
    pass


@frr_show_ipv6_pim_bsr.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_ipv6_pim_bsr_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsr_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_pim_bsr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsr'
    pass


@frr_show_ipv6_pim_bsr_vrf.command('./	<cr>')
def frr_show_ipv6_pim_bsr_vrf_cr():
    pass


@frr_show_ipv6_pim_bsr_vrf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_bsr_vrf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsr_vrf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_bsr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsr'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsr'
    pass


@frr_show_ipv6_pim_bsr_vrf_json.command('./	<cr>')
def frr_show_ipv6_pim_bsr_vrf_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='bsrp-info', invoke_without_command=True)
def frr_show_ipv6_pim_bsrpinfo(show_ipv6_pim_bsrpinfo_='show_ipv6_pim_bsrp-info'):
    """PIM cached group-rp mappings information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsrpinfo.name
    
    if 'VIEW_NODE|show_ipv6_pim_bsrp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsrp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsrp-info'
    pass


@frr_show_ipv6_pim_bsrpinfo.command('./	<cr>')
def frr_show_ipv6_pim_bsrpinfo_cr():
    pass


@frr_show_ipv6_pim_bsrpinfo.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_bsrpinfo_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsrpinfo_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_bsrp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsrp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsrp-info'
    pass


@frr_show_ipv6_pim_bsrpinfo_json.command('./	<cr>')
def frr_show_ipv6_pim_bsrpinfo_json_cr():
    pass


@frr_show_ipv6_pim_bsrpinfo.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_ipv6_pim_bsrpinfo_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsrpinfo_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_pim_bsrp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsrp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsrp-info'
    pass


@frr_show_ipv6_pim_bsrpinfo_vrf.command('./	<cr>')
def frr_show_ipv6_pim_bsrpinfo_vrf_cr():
    pass


@frr_show_ipv6_pim_bsrpinfo_vrf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_bsrpinfo_vrf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_bsrpinfo_vrf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_bsrp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_bsrp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_bsrp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_bsrp-info'
    pass


@frr_show_ipv6_pim_bsrpinfo_vrf_json.command('./	<cr>')
def frr_show_ipv6_pim_bsrpinfo_vrf_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='channel', invoke_without_command=True)
def frr_show_ipv6_pim_channel(show_ipv6_pim_channel_='show_ipv6_pim_channel'):
    """PIM downstream channel info"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_channel.name
    
    if 'VIEW_NODE|show_ipv6_pim_channel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_channel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_channel']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_channel'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_channel table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_channel'
    pass


@frr_show_ipv6_pim_channel.command('./	<cr>')
def frr_show_ipv6_pim_channel_cr():
    pass


@frr_show_ipv6_pim_channel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_channel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_channel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_channel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_channel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_channel']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_channel'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_channel table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_channel'
    pass


@frr_show_ipv6_pim_channel_json.command('./	<cr>')
def frr_show_ipv6_pim_channel_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_ipv6_pim_interface(show_ipv6_pim_interface_='show_ipv6_pim_interface'):
    """PIM interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_interface.name
    
    if 'VIEW_NODE|show_ipv6_pim_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_interface'
    pass


@frr_show_ipv6_pim_interface.command('./	<cr>')
def frr_show_ipv6_pim_interface_cr():
    pass


@frr_show_ipv6_pim_interface.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_pim_interface_detail(show_ipv6_pim_interface_detail_='show_ipv6_pim_interface_detail'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_interface_detail.name
    
    if 'VIEW_NODE|show_ipv6_pim_interface_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_interface_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_interface_detail'
    pass


@frr_show_ipv6_pim_interface_detail.command('./	<cr>')
def frr_show_ipv6_pim_interface_detail_cr():
    pass


@frr_show_ipv6_pim_interface_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_interface_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_interface_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_interface_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_interface_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_interface_detail'
    pass


@frr_show_ipv6_pim_interface_detail_json.command('./	<cr>')
def frr_show_ipv6_pim_interface_detail_json_cr():
    pass


@frr_show_ipv6_pim_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_pim_interface_interfacename():
    """interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_interface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_interface'
    pass


@frr_show_ipv6_pim_interface_interfacename.command('./	<cr>')
def frr_show_ipv6_pim_interface_interfacename_cr():
    pass


@frr_show_ipv6_pim_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_interface_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_interface_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_interface'
    pass


@frr_show_ipv6_pim_interface_interfacename_json.command('./	<cr>')
def frr_show_ipv6_pim_interface_interfacename_json_cr():
    pass


@frr_show_ipv6_pim_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_interface'
    pass


@frr_show_ipv6_pim_interface_json.command('./	<cr>')
def frr_show_ipv6_pim_interface_json_cr():
    pass


@frr_show_ipv6_pim_interface.group(cls=FRR_AbbreviationGroup, name='traffic', invoke_without_command=True)
def frr_show_ipv6_pim_interface_traffic(show_ipv6_pim_interface_traffic_='show_ipv6_pim_interface_traffic'):
    """Protocol Packet counters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_interface_traffic.name
    
    if 'VIEW_NODE|show_ipv6_pim_interface_traffic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_interface_traffic table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_interface_traffic'
    pass


@frr_show_ipv6_pim_interface_traffic.command('./	<cr>')
def frr_show_ipv6_pim_interface_traffic_cr():
    pass


@frr_show_ipv6_pim_interface_traffic.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_pim_interface_traffic_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_interface_traffic_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_interface_traffic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_interface_traffic table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_interface_traffic'
    pass


@frr_show_ipv6_pim_interface_traffic_interfacename.command('./	<cr>')
def frr_show_ipv6_pim_interface_traffic_interfacename_cr():
    pass


@frr_show_ipv6_pim_interface_traffic_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_interface_traffic_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_interface_traffic_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_interface_traffic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_interface_traffic table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_interface_traffic'
    pass


@frr_show_ipv6_pim_interface_traffic_interfacename_json.command('./	<cr>')
def frr_show_ipv6_pim_interface_traffic_interfacename_json_cr():
    pass


@frr_show_ipv6_pim_interface_traffic.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_interface_traffic_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_interface_traffic_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_interface_traffic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_interface_traffic'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_interface_traffic table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_interface_traffic'
    pass


@frr_show_ipv6_pim_interface_traffic_json.command('./	<cr>')
def frr_show_ipv6_pim_interface_traffic_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='join', invoke_without_command=True)
def frr_show_ipv6_pim_join(show_ipv6_pim_join_='show_ipv6_pim_join'):
    """PIM interface join information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_join.name
    
    if 'VIEW_NODE|show_ipv6_pim_join' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_join table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_join'
    pass


@frr_show_ipv6_pim_join.command('./	<cr>')
def frr_show_ipv6_pim_join_cr():
    pass


@frr_show_ipv6_pim_join.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_join_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_join_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_join' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_join table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_join'
    pass


@frr_show_ipv6_pim_join_json.command('./	<cr>')
def frr_show_ipv6_pim_join_json_cr():
    pass


@frr_show_ipv6_pim_join.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_join_thesourceorgroup():
    """The Source or Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_join_thesourceorgroup.name
    data_gen['THE_SOURCE_OR_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_join' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_join table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_join'
    pass


@frr_show_ipv6_pim_join_thesourceorgroup.command('./	<cr>')
def frr_show_ipv6_pim_join_thesourceorgroup_cr():
    pass


@frr_show_ipv6_pim_join_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_join_thesourceorgroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_join_thesourceorgroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_join' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_join table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_join'
    pass


@frr_show_ipv6_pim_join_thesourceorgroup_json.command('./	<cr>')
def frr_show_ipv6_pim_join_thesourceorgroup_json_cr():
    pass


@frr_show_ipv6_pim_join_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_join_thesourceorgroup_thegroup():
    """The Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_join_thesourceorgroup_thegroup.name
    data_gen['THE_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_join' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_join table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_join'
    pass


@frr_show_ipv6_pim_join_thesourceorgroup_thegroup.command('./	<cr>')
def frr_show_ipv6_pim_join_thesourceorgroup_thegroup_cr():
    pass


@frr_show_ipv6_pim_join_thesourceorgroup_thegroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_join_thesourceorgroup_thegroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_join_thesourceorgroup_thegroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_join' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_join'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_join table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_join'
    pass


@frr_show_ipv6_pim_join_thesourceorgroup_thegroup_json.command('./	<cr>')
def frr_show_ipv6_pim_join_thesourceorgroup_thegroup_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='jp-agg', invoke_without_command=True)
def frr_show_ipv6_pim_jpagg(jpagg_='jp-agg'):
    """join prune aggregation list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_jpagg.name
    data_gen['jp-agg'] = jpagg_='jp-agg'
    
    if 'VIEW_NODE|show_ipv6_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim'
    pass


@frr_show_ipv6_pim_jpagg.command('./	<cr>')
def frr_show_ipv6_pim_jpagg_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='local-membership', invoke_without_command=True)
def frr_show_ipv6_pim_localmembership(show_ipv6_pim_localmembership_='show_ipv6_pim_local-membership'):
    """PIM interface local-membership"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_localmembership.name
    
    if 'VIEW_NODE|show_ipv6_pim_local-membership' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_local-membership'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_local-membership']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_local-membership'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_local-membership table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_local-membership'
    pass


@frr_show_ipv6_pim_localmembership.command('./	<cr>')
def frr_show_ipv6_pim_localmembership_cr():
    pass


@frr_show_ipv6_pim_localmembership.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_localmembership_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_localmembership_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_local-membership' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_local-membership'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_local-membership']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_local-membership'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_local-membership table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_local-membership'
    pass


@frr_show_ipv6_pim_localmembership_json.command('./	<cr>')
def frr_show_ipv6_pim_localmembership_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
def frr_show_ipv6_pim_neighbor(show_ipv6_pim_neighbor_='show_ipv6_pim_neighbor'):
    """PIM neighbor information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_neighbor.name
    
    if 'VIEW_NODE|show_ipv6_pim_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_neighbor'
    pass


@frr_show_ipv6_pim_neighbor.command('./	<cr>')
def frr_show_ipv6_pim_neighbor_cr():
    pass


@frr_show_ipv6_pim_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_pim_neighbor_detail(show_ipv6_pim_neighbor_detail_='show_ipv6_pim_neighbor_detail'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_neighbor_detail.name
    
    if 'VIEW_NODE|show_ipv6_pim_neighbor_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_neighbor_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_neighbor_detail'
    pass


@frr_show_ipv6_pim_neighbor_detail.command('./	<cr>')
def frr_show_ipv6_pim_neighbor_detail_cr():
    pass


@frr_show_ipv6_pim_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_neighbor_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_neighbor_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_neighbor_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_neighbor_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_neighbor_detail'
    pass


@frr_show_ipv6_pim_neighbor_detail_json.command('./	<cr>')
def frr_show_ipv6_pim_neighbor_detail_json_cr():
    pass


@frr_show_ipv6_pim_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_neighbor'
    pass


@frr_show_ipv6_pim_neighbor_json.command('./	<cr>')
def frr_show_ipv6_pim_neighbor_json_cr():
    pass


@frr_show_ipv6_pim_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_pim_neighbor_nameofinterfaceor():
    """Name of interface or neighbor"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_neighbor_nameofinterfaceor.name
    data_gen['NAME_OF_INTERFACE_OR'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_neighbor'
    pass


@frr_show_ipv6_pim_neighbor_nameofinterfaceor.command('./	<cr>')
def frr_show_ipv6_pim_neighbor_nameofinterfaceor_cr():
    pass


@frr_show_ipv6_pim_neighbor_nameofinterfaceor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_neighbor_nameofinterfaceor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_neighbor_nameofinterfaceor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_neighbor'
    pass


@frr_show_ipv6_pim_neighbor_nameofinterfaceor_json.command('./	<cr>')
def frr_show_ipv6_pim_neighbor_nameofinterfaceor_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='nexthop', invoke_without_command=True)
def frr_show_ipv6_pim_nexthop(show_ipv6_pim_nexthop_='show_ipv6_pim_nexthop'):
    """PIM cached nexthop rpf information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_nexthop.name
    
    if 'VIEW_NODE|show_ipv6_pim_nexthop' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_nexthop'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_nexthop']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_nexthop'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_nexthop table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_nexthop'
    pass


@frr_show_ipv6_pim_nexthop.command('./	<cr>')
def frr_show_ipv6_pim_nexthop_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='nexthop-lookup', invoke_without_command=True)
@click.argument('sourcerp_address', metavar='X:X::X:X', required=True, type=FRR_TYPE('X:X::X:X'))
@click.argument('multicast_group_address', metavar='X:X::X:X', required=True, type=FRR_TYPE('X:X::X:X'))
def frr_show_ipv6_pim_nexthoplookup(multicast_group_address, sourcerp_address, nexthoplookup_='nexthop-lookup'):
    """PIM cached nexthop rpf lookup"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_nexthoplookup.name
    data_gen['nexthop-lookup'] = nexthoplookup_='nexthop-lookup'
    data_gen['SOURCERP_ADDRESS'] = sourcerp_address
    data_gen['MULTICAST_GROUP_ADDRESS'] = multicast_group_address
    
    if 'VIEW_NODE|show_ipv6_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim'
    pass


@frr_show_ipv6_pim_nexthoplookup.command('./	<cr>')
def frr_show_ipv6_pim_nexthoplookup_cr():
    pass


@frr_show_ipv6_pim_nexthop.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_nexthop_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_nexthop_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_nexthop' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_nexthop'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_nexthop']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_nexthop'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_nexthop table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_nexthop'
    pass


@frr_show_ipv6_pim_nexthop_json.command('./	<cr>')
def frr_show_ipv6_pim_nexthop_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='rp-info', invoke_without_command=True)
def frr_show_ipv6_pim_rpinfo(show_ipv6_pim_rpinfo_='show_ipv6_pim_rp-info'):
    """PIM RP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_rpinfo.name
    
    if 'VIEW_NODE|show_ipv6_pim_rp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_rp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_rp-info'
    pass


@frr_show_ipv6_pim_rpinfo.command('./	<cr>')
def frr_show_ipv6_pim_rpinfo_cr():
    pass


@frr_show_ipv6_pim_rpinfo.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_rpinfo_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_rpinfo_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_rp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_rp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_rp-info'
    pass


@frr_show_ipv6_pim_rpinfo_json.command('./	<cr>')
def frr_show_ipv6_pim_rpinfo_json_cr():
    pass


@frr_show_ipv6_pim_rpinfo.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['X:X::X:X/M']), invoke_without_command=True)
def frr_show_ipv6_pim_rpinfo_multicastgrouprange():
    """Multicast Group range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_rpinfo_multicastgrouprange.name
    data_gen['MULTICAST_GROUP_RANGE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_rp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_rp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_rp-info'
    pass


@frr_show_ipv6_pim_rpinfo_multicastgrouprange.command('./	<cr>')
def frr_show_ipv6_pim_rpinfo_multicastgrouprange_cr():
    pass


@frr_show_ipv6_pim_rpinfo_multicastgrouprange.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_rpinfo_multicastgrouprange_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_rpinfo_multicastgrouprange_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_rp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_rp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_rp-info'
    pass


@frr_show_ipv6_pim_rpinfo_multicastgrouprange_json.command('./	<cr>')
def frr_show_ipv6_pim_rpinfo_multicastgrouprange_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='rpf', invoke_without_command=True)
def frr_show_ipv6_pim_rpf(show_ipv6_pim_rpf_='show_ipv6_pim_rpf'):
    """PIM cached source rpf information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_rpf.name
    
    if 'VIEW_NODE|show_ipv6_pim_rpf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rpf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rpf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rpf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_rpf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_rpf'
    pass


@frr_show_ipv6_pim_rpf.command('./	<cr>')
def frr_show_ipv6_pim_rpf_cr():
    pass


@frr_show_ipv6_pim_rpf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_rpf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_rpf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_rpf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rpf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rpf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_rpf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_rpf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_rpf'
    pass


@frr_show_ipv6_pim_rpf_json.command('./	<cr>')
def frr_show_ipv6_pim_rpf_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='secondary', invoke_without_command=True)
def frr_show_ipv6_pim_secondary(secondary_='secondary'):
    """PIM neighbor addresses"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_secondary.name
    data_gen['secondary'] = secondary_='secondary'
    
    if 'VIEW_NODE|show_ipv6_pim' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim'
    pass


@frr_show_ipv6_pim_secondary.command('./	<cr>')
def frr_show_ipv6_pim_secondary_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='state', invoke_without_command=True)
def frr_show_ipv6_pim_state(show_ipv6_pim_state_='show_ipv6_pim_state'):
    """PIM state information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_state.name
    
    if 'VIEW_NODE|show_ipv6_pim_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_state'
    pass


@frr_show_ipv6_pim_state.command('./	<cr>')
def frr_show_ipv6_pim_state_cr():
    pass


@frr_show_ipv6_pim_state.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_state_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_state_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_state'
    pass


@frr_show_ipv6_pim_state_json.command('./	<cr>')
def frr_show_ipv6_pim_state_json_cr():
    pass


@frr_show_ipv6_pim_state.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_state_unicastormulticastaddress():
    """Unicast or Multicast address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_state_unicastormulticastaddress.name
    data_gen['UNICAST_OR_MULTICAST_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_state'
    pass


@frr_show_ipv6_pim_state_unicastormulticastaddress.command('./	<cr>')
def frr_show_ipv6_pim_state_unicastormulticastaddress_cr():
    pass


@frr_show_ipv6_pim_state_unicastormulticastaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_state_unicastormulticastaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_state_unicastormulticastaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_state'
    pass


@frr_show_ipv6_pim_state_unicastormulticastaddress_json.command('./	<cr>')
def frr_show_ipv6_pim_state_unicastormulticastaddress_json_cr():
    pass


@frr_show_ipv6_pim_state_unicastormulticastaddress.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_state_unicastormulticastaddress_multicastaddress():
    """Multicast address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_state_unicastormulticastaddress_multicastaddress.name
    data_gen['MULTICAST_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_state'
    pass


@frr_show_ipv6_pim_state_unicastormulticastaddress_multicastaddress.command('./	<cr>')
def frr_show_ipv6_pim_state_unicastormulticastaddress_multicastaddress_cr():
    pass


@frr_show_ipv6_pim_state_unicastormulticastaddress_multicastaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_state_unicastormulticastaddress_multicastaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_state_unicastormulticastaddress_multicastaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_state'
    pass


@frr_show_ipv6_pim_state_unicastormulticastaddress_multicastaddress_json.command('./	<cr>')
def frr_show_ipv6_pim_state_unicastormulticastaddress_multicastaddress_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='statistics', invoke_without_command=True)
def frr_show_ipv6_pim_statistics(show_ipv6_pim_statistics_='show_ipv6_pim_statistics'):
    """PIM statistics"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_statistics.name
    
    if 'VIEW_NODE|show_ipv6_pim_statistics' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_statistics table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_statistics'
    pass


@frr_show_ipv6_pim_statistics.command('./	<cr>')
def frr_show_ipv6_pim_statistics_cr():
    pass


@frr_show_ipv6_pim_statistics.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
@click.argument('pim_interface', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_ipv6_pim_statistics_interface(pim_interface, interface_='interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_statistics_interface.name
    data_gen['interface'] = interface_='interface'
    data_gen['PIM_INTERFACE'] = pim_interface
    
    if 'VIEW_NODE|show_ipv6_pim_statistics' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_statistics table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_statistics'
    pass


@frr_show_ipv6_pim_statistics_interface.command('./	<cr>')
def frr_show_ipv6_pim_statistics_interface_cr():
    pass


@frr_show_ipv6_pim_statistics_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_statistics_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_statistics_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_statistics' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_statistics table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_statistics'
    pass


@frr_show_ipv6_pim_statistics_interface_json.command('./	<cr>')
def frr_show_ipv6_pim_statistics_interface_json_cr():
    pass


@frr_show_ipv6_pim_statistics.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_statistics_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_statistics_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_statistics' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_statistics'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_statistics table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_statistics'
    pass


@frr_show_ipv6_pim_statistics_json.command('./	<cr>')
def frr_show_ipv6_pim_statistics_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='upstream', invoke_without_command=True)
def frr_show_ipv6_pim_upstream(show_ipv6_pim_upstream_='show_ipv6_pim_upstream'):
    """PIM upstream information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_upstream.name
    
    if 'VIEW_NODE|show_ipv6_pim_upstream' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_upstream table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_upstream'
    pass


@frr_show_ipv6_pim_upstream.command('./	<cr>')
def frr_show_ipv6_pim_upstream_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='upstream-join-desired', invoke_without_command=True)
def frr_show_ipv6_pim_upstreamjoindesired(show_ipv6_pim_upstreamjoindesired_='show_ipv6_pim_upstream-join-desired'):
    """PIM upstream join-desired"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_upstreamjoindesired.name
    
    if 'VIEW_NODE|show_ipv6_pim_upstream-join-desired' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-join-desired'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-join-desired']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-join-desired'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_upstream-join-desired table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_upstream-join-desired'
    pass


@frr_show_ipv6_pim_upstreamjoindesired.command('./	<cr>')
def frr_show_ipv6_pim_upstreamjoindesired_cr():
    pass


@frr_show_ipv6_pim_upstreamjoindesired.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_upstreamjoindesired_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_upstreamjoindesired_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_upstream-join-desired' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-join-desired'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-join-desired']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-join-desired'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_upstream-join-desired table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_upstream-join-desired'
    pass


@frr_show_ipv6_pim_upstreamjoindesired_json.command('./	<cr>')
def frr_show_ipv6_pim_upstreamjoindesired_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='upstream-rpf', invoke_without_command=True)
def frr_show_ipv6_pim_upstreamrpf(show_ipv6_pim_upstreamrpf_='show_ipv6_pim_upstream-rpf'):
    """PIM upstream source rpf"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_upstreamrpf.name
    
    if 'VIEW_NODE|show_ipv6_pim_upstream-rpf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-rpf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-rpf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-rpf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_upstream-rpf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_upstream-rpf'
    pass


@frr_show_ipv6_pim_upstreamrpf.command('./	<cr>')
def frr_show_ipv6_pim_upstreamrpf_cr():
    pass


@frr_show_ipv6_pim_upstreamrpf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_upstreamrpf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_upstreamrpf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_upstream-rpf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-rpf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-rpf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream-rpf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_upstream-rpf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_upstream-rpf'
    pass


@frr_show_ipv6_pim_upstreamrpf_json.command('./	<cr>')
def frr_show_ipv6_pim_upstreamrpf_json_cr():
    pass


@frr_show_ipv6_pim_upstream.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_upstream_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_upstream_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_upstream' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_upstream table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_upstream'
    pass


@frr_show_ipv6_pim_upstream_json.command('./	<cr>')
def frr_show_ipv6_pim_upstream_json_cr():
    pass


@frr_show_ipv6_pim_upstream.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_upstream_thesourceorgroup():
    """The Source or Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_upstream_thesourceorgroup.name
    data_gen['THE_SOURCE_OR_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_upstream' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_upstream table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_upstream'
    pass


@frr_show_ipv6_pim_upstream_thesourceorgroup.command('./	<cr>')
def frr_show_ipv6_pim_upstream_thesourceorgroup_cr():
    pass


@frr_show_ipv6_pim_upstream_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_upstream_thesourceorgroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_upstream_thesourceorgroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_upstream' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_upstream table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_upstream'
    pass


@frr_show_ipv6_pim_upstream_thesourceorgroup_json.command('./	<cr>')
def frr_show_ipv6_pim_upstream_thesourceorgroup_json_cr():
    pass


@frr_show_ipv6_pim_upstream_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_upstream_thesourceorgroup_thegroup():
    """The Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_upstream_thesourceorgroup_thegroup.name
    data_gen['THE_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_upstream' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_upstream table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_upstream'
    pass


@frr_show_ipv6_pim_upstream_thesourceorgroup_thegroup.command('./	<cr>')
def frr_show_ipv6_pim_upstream_thesourceorgroup_thegroup_cr():
    pass


@frr_show_ipv6_pim_upstream_thesourceorgroup_thegroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_upstream_thesourceorgroup_thegroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_upstream_thesourceorgroup_thegroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_upstream' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_upstream'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_upstream table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_upstream'
    pass


@frr_show_ipv6_pim_upstream_thesourceorgroup_thegroup_json.command('./	<cr>')
def frr_show_ipv6_pim_upstream_thesourceorgroup_thegroup_json_cr():
    pass


@frr_show_ipv6_pim.group(cls=FRR_AbbreviationGroup, name='vrf',)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_ipv6_pim_vrf(the_vrf_name, show_ipv6_pim_vrf_='show_ipv6_pim_vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf.name
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all.name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all'
    pass


@frr_show_ipv6_pim_vrf_all.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_cr():
    pass


@frr_show_ipv6_pim_vrf_all.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_interface(show_ipv6_pim_vrf_all_interface_='show_ipv6_pim_vrf_all_interface'):
    """PIM interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_interface.name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_interface'
    pass


@frr_show_ipv6_pim_vrf_all_interface.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_interface_cr():
    pass


@frr_show_ipv6_pim_vrf_all_interface.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_interface_detail(show_ipv6_pim_vrf_all_interface_detail_='show_ipv6_pim_vrf_all_interface_detail'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_interface_detail.name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_interface_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_interface_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_interface_detail'
    pass


@frr_show_ipv6_pim_vrf_all_interface_detail.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_interface_detail_cr():
    pass


@frr_show_ipv6_pim_vrf_all_interface_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_interface_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_interface_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_interface_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_interface_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_interface_detail'
    pass


@frr_show_ipv6_pim_vrf_all_interface_detail_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_interface_detail_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_interface_interfacename():
    """interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_interface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_interface'
    pass


@frr_show_ipv6_pim_vrf_all_interface_interfacename.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_interface_interfacename_cr():
    pass


@frr_show_ipv6_pim_vrf_all_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_interface_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_interface_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_interface'
    pass


@frr_show_ipv6_pim_vrf_all_interface_interfacename_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_interface_interfacename_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_interface'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_interface'
    pass


@frr_show_ipv6_pim_vrf_all_interface_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_interface_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all.group(cls=FRR_AbbreviationGroup, name='join', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_join(show_ipv6_pim_vrf_all_join_='show_ipv6_pim_vrf_all_join'):
    """PIM interface join information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_join.name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_join' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_join'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_join']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_join'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_join table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_join'
    pass


@frr_show_ipv6_pim_vrf_all_join.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_join_cr():
    pass


@frr_show_ipv6_pim_vrf_all_join.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_join_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_join_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_join' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_join'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_join']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_join'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_join table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_join'
    pass


@frr_show_ipv6_pim_vrf_all_join_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_join_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_neighbor(show_ipv6_pim_vrf_all_neighbor_='show_ipv6_pim_vrf_all_neighbor'):
    """PIM neighbor information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_neighbor.name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_neighbor'
    pass


@frr_show_ipv6_pim_vrf_all_neighbor.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_neighbor_cr():
    pass


@frr_show_ipv6_pim_vrf_all_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_neighbor_detail(show_ipv6_pim_vrf_all_neighbor_detail_='show_ipv6_pim_vrf_all_neighbor_detail'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_neighbor_detail.name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_neighbor_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_neighbor_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_neighbor_detail'
    pass


@frr_show_ipv6_pim_vrf_all_neighbor_detail.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_neighbor_detail_cr():
    pass


@frr_show_ipv6_pim_vrf_all_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_neighbor_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_neighbor_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_neighbor_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_neighbor_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_neighbor_detail'
    pass


@frr_show_ipv6_pim_vrf_all_neighbor_detail_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_neighbor_detail_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_neighbor'
    pass


@frr_show_ipv6_pim_vrf_all_neighbor_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_neighbor_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_neighbor_nameofinterfaceor():
    """Name of interface or neighbor"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_neighbor_nameofinterfaceor.name
    data_gen['NAME_OF_INTERFACE_OR'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_neighbor'
    pass


@frr_show_ipv6_pim_vrf_all_neighbor_nameofinterfaceor.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_neighbor_nameofinterfaceor_cr():
    pass


@frr_show_ipv6_pim_vrf_all_neighbor_nameofinterfaceor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_neighbor_nameofinterfaceor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_neighbor_nameofinterfaceor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_neighbor'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_neighbor'
    pass


@frr_show_ipv6_pim_vrf_all_neighbor_nameofinterfaceor_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_neighbor_nameofinterfaceor_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all.group(cls=FRR_AbbreviationGroup, name='rp-info', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_rpinfo(show_ipv6_pim_vrf_all_rpinfo_='show_ipv6_pim_vrf_all_rp-info'):
    """PIM RP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_rpinfo.name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_rp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_rp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_rp-info'
    pass


@frr_show_ipv6_pim_vrf_all_rpinfo.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_rpinfo_cr():
    pass


@frr_show_ipv6_pim_vrf_all_rpinfo.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_rpinfo_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_rpinfo_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_rp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_rp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_rp-info'
    pass


@frr_show_ipv6_pim_vrf_all_rpinfo_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_rpinfo_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all_rpinfo.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X/M']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_rpinfo_multicastgrouprange():
    """Multicast Group range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_rpinfo_multicastgrouprange.name
    data_gen['MULTICAST_GROUP_RANGE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_rp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_rp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_rp-info'
    pass


@frr_show_ipv6_pim_vrf_all_rpinfo_multicastgrouprange.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_rpinfo_multicastgrouprange_cr():
    pass


@frr_show_ipv6_pim_vrf_all_rpinfo_multicastgrouprange.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_rpinfo_multicastgrouprange_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_rpinfo_multicastgrouprange_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_rp-info' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rp-info'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_rp-info table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_rp-info'
    pass


@frr_show_ipv6_pim_vrf_all_rpinfo_multicastgrouprange_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_rpinfo_multicastgrouprange_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all.group(cls=FRR_AbbreviationGroup, name='rpf', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_rpf(show_ipv6_pim_vrf_all_rpf_='show_ipv6_pim_vrf_all_rpf'):
    """PIM cached source rpf information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_rpf.name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_rpf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rpf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rpf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rpf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_rpf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_rpf'
    pass


@frr_show_ipv6_pim_vrf_all_rpf.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_rpf_cr():
    pass


@frr_show_ipv6_pim_vrf_all_rpf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_rpf_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_rpf_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_rpf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rpf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rpf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_rpf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_rpf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_rpf'
    pass


@frr_show_ipv6_pim_vrf_all_rpf_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_rpf_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all.group(cls=FRR_AbbreviationGroup, name='state', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_state(show_ipv6_pim_vrf_all_state_='show_ipv6_pim_vrf_all_state'):
    """PIM state information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_state.name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_state'
    pass


@frr_show_ipv6_pim_vrf_all_state.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_state_cr():
    pass


@frr_show_ipv6_pim_vrf_all_state.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_state_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_state_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_state'
    pass


@frr_show_ipv6_pim_vrf_all_state_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_state_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all_state.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress():
    """Unicast or Multicast address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress.name
    data_gen['UNICAST_OR_MULTICAST_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_state'
    pass


@frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_cr():
    pass


@frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_state'
    pass


@frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_multicastaddress():
    """Multicast address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_multicastaddress.name
    data_gen['MULTICAST_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_state'
    pass


@frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_multicastaddress.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_multicastaddress_cr():
    pass


@frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_multicastaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_multicastaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_multicastaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_state' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_state'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_state table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_state'
    pass


@frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_multicastaddress_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_state_unicastormulticastaddress_multicastaddress_json_cr():
    pass


@frr_show_ipv6_pim_vrf_all.group(cls=FRR_AbbreviationGroup, name='upstream', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_upstream(show_ipv6_pim_vrf_all_upstream_='show_ipv6_pim_vrf_all_upstream'):
    """PIM upstream information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_upstream.name
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_upstream' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_upstream'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_upstream']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_upstream'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_upstream table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_upstream'
    pass


@frr_show_ipv6_pim_vrf_all_upstream.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_upstream_cr():
    pass


@frr_show_ipv6_pim_vrf_all_upstream.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_all_upstream_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_all_upstream_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf_all_upstream' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_upstream'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_upstream']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf_all_upstream'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf_all_upstream table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf_all_upstream'
    pass


@frr_show_ipv6_pim_vrf_all_upstream_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_all_upstream_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='channel', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_channel(channel_='channel'):
    """PIM downstream channel info"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_channel.name
    data_gen['channel'] = channel_='channel'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_channel.command('./	<cr>')
def frr_show_ipv6_pim_vrf_channel_cr():
    pass


@frr_show_ipv6_pim_vrf_channel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_channel_json(channel_json_='channel_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_channel_json.name
    data_gen['channel_json'] = channel_json_='channel_json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_channel_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_channel_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_interface(interface_='interface'):
    """PIM interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_interface.name
    data_gen['interface'] = interface_='interface'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_interface.command('./	<cr>')
def frr_show_ipv6_pim_vrf_interface_cr():
    pass


@frr_show_ipv6_pim_vrf_interface.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_interface_detail(interface_detail_='interface_detail'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_interface_detail.name
    data_gen['interface_detail'] = interface_detail_='interface_detail'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_interface_detail.command('./	<cr>')
def frr_show_ipv6_pim_vrf_interface_detail_cr():
    pass


@frr_show_ipv6_pim_vrf_interface_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_interface_detail_json(interface_detail_json_='interface_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_interface_detail_json.name
    data_gen['interface_detail_json'] = interface_detail_json_='interface_detail_json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_interface_detail_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_interface_detail_json_cr():
    pass


@frr_show_ipv6_pim_vrf_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_interface_interfacename():
    """interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_interface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_interface_interfacename.command('./	<cr>')
def frr_show_ipv6_pim_vrf_interface_interfacename_cr():
    pass


@frr_show_ipv6_pim_vrf_interface_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_interface_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_interface_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_interface_interfacename_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_interface_interfacename_json_cr():
    pass


@frr_show_ipv6_pim_vrf_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_interface_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_interface_json_cr():
    pass


@frr_show_ipv6_pim_vrf_interface.group(cls=FRR_AbbreviationGroup, name='traffic', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_interface_traffic(interface_traffic_='interface_traffic'):
    """Protocol Packet counters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_interface_traffic.name
    data_gen['interface_traffic'] = interface_traffic_='interface_traffic'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_interface_traffic.command('./	<cr>')
def frr_show_ipv6_pim_vrf_interface_traffic_cr():
    pass


@frr_show_ipv6_pim_vrf_interface_traffic.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_interface_traffic_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_interface_traffic_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_interface_traffic_interfacename.command('./	<cr>')
def frr_show_ipv6_pim_vrf_interface_traffic_interfacename_cr():
    pass


@frr_show_ipv6_pim_vrf_interface_traffic_interfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_interface_traffic_interfacename_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_interface_traffic_interfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_interface_traffic_interfacename_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_interface_traffic_interfacename_json_cr():
    pass


@frr_show_ipv6_pim_vrf_interface_traffic.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_interface_traffic_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_interface_traffic_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_interface_traffic_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_interface_traffic_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='join', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_join(join_='join'):
    """PIM interface join information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_join.name
    data_gen['join'] = join_='join'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_join.command('./	<cr>')
def frr_show_ipv6_pim_vrf_join_cr():
    pass


@frr_show_ipv6_pim_vrf_join.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_join_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_join_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_join_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_join_json_cr():
    pass


@frr_show_ipv6_pim_vrf_join.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_join_thesourceorgroup():
    """The Source or Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_join_thesourceorgroup.name
    data_gen['THE_SOURCE_OR_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_join_thesourceorgroup.command('./	<cr>')
def frr_show_ipv6_pim_vrf_join_thesourceorgroup_cr():
    pass


@frr_show_ipv6_pim_vrf_join_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_join_thesourceorgroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_join_thesourceorgroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_join_thesourceorgroup_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_join_thesourceorgroup_json_cr():
    pass


@frr_show_ipv6_pim_vrf_join_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_join_thesourceorgroup_thegroup():
    """The Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_join_thesourceorgroup_thegroup.name
    data_gen['THE_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_join_thesourceorgroup_thegroup.command('./	<cr>')
def frr_show_ipv6_pim_vrf_join_thesourceorgroup_thegroup_cr():
    pass


@frr_show_ipv6_pim_vrf_join_thesourceorgroup_thegroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_join_thesourceorgroup_thegroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_join_thesourceorgroup_thegroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_join_thesourceorgroup_thegroup_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_join_thesourceorgroup_thegroup_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='jp-agg', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_jpagg(jpagg_='jp-agg'):
    """join prune aggregation list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_jpagg.name
    data_gen['jp-agg'] = jpagg_='jp-agg'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_jpagg.command('./	<cr>')
def frr_show_ipv6_pim_vrf_jpagg_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='local-membership', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_localmembership(localmembership_='local-membership'):
    """PIM interface local-membership"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_localmembership.name
    data_gen['local-membership'] = localmembership_='local-membership'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_localmembership.command('./	<cr>')
def frr_show_ipv6_pim_vrf_localmembership_cr():
    pass


@frr_show_ipv6_pim_vrf_localmembership.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_localmembership_json(localmembership_json_='local-membership_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_localmembership_json.name
    data_gen['local-membership_json'] = localmembership_json_='local-membership_json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_localmembership_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_localmembership_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_neighbor(neighbor_='neighbor'):
    """PIM neighbor information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_neighbor.command('./	<cr>')
def frr_show_ipv6_pim_vrf_neighbor_cr():
    pass


@frr_show_ipv6_pim_vrf_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_neighbor_detail(neighbor_detail_='neighbor_detail'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_neighbor_detail.name
    data_gen['neighbor_detail'] = neighbor_detail_='neighbor_detail'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_neighbor_detail.command('./	<cr>')
def frr_show_ipv6_pim_vrf_neighbor_detail_cr():
    pass


@frr_show_ipv6_pim_vrf_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_neighbor_detail_json(neighbor_detail_json_='neighbor_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_neighbor_detail_json.name
    data_gen['neighbor_detail_json'] = neighbor_detail_json_='neighbor_detail_json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_neighbor_detail_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_neighbor_detail_json_cr():
    pass


@frr_show_ipv6_pim_vrf_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_neighbor_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_neighbor_json_cr():
    pass


@frr_show_ipv6_pim_vrf_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_neighbor_nameofinterfaceor():
    """Name of interface or neighbor"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_neighbor_nameofinterfaceor.name
    data_gen['NAME_OF_INTERFACE_OR'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_neighbor_nameofinterfaceor.command('./	<cr>')
def frr_show_ipv6_pim_vrf_neighbor_nameofinterfaceor_cr():
    pass


@frr_show_ipv6_pim_vrf_neighbor_nameofinterfaceor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_neighbor_nameofinterfaceor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_neighbor_nameofinterfaceor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_neighbor_nameofinterfaceor_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_neighbor_nameofinterfaceor_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='nexthop', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_nexthop(nexthop_='nexthop'):
    """PIM cached nexthop rpf information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_nexthop.name
    data_gen['nexthop'] = nexthop_='nexthop'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_nexthop.command('./	<cr>')
def frr_show_ipv6_pim_vrf_nexthop_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='nexthop-lookup', invoke_without_command=True)
@click.argument('sourcerp_address', metavar='X:X::X:X', required=True, type=FRR_TYPE('X:X::X:X'))
@click.argument('multicast_group_address', metavar='X:X::X:X', required=True, type=FRR_TYPE('X:X::X:X'))
def frr_show_ipv6_pim_vrf_nexthoplookup(multicast_group_address, sourcerp_address, nexthoplookup_='nexthop-lookup'):
    """PIM cached nexthop rpf lookup"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_nexthoplookup.name
    data_gen['nexthop-lookup'] = nexthoplookup_='nexthop-lookup'
    data_gen['SOURCERP_ADDRESS'] = sourcerp_address
    data_gen['MULTICAST_GROUP_ADDRESS'] = multicast_group_address
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_nexthoplookup.command('./	<cr>')
def frr_show_ipv6_pim_vrf_nexthoplookup_cr():
    pass


@frr_show_ipv6_pim_vrf_nexthop.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_nexthop_json(nexthop_json_='nexthop_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_nexthop_json.name
    data_gen['nexthop_json'] = nexthop_json_='nexthop_json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_nexthop_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_nexthop_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='rp-info', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_rpinfo(rpinfo_='rp-info'):
    """PIM RP information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_rpinfo.name
    data_gen['rp-info'] = rpinfo_='rp-info'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_rpinfo.command('./	<cr>')
def frr_show_ipv6_pim_vrf_rpinfo_cr():
    pass


@frr_show_ipv6_pim_vrf_rpinfo.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_rpinfo_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_rpinfo_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_rpinfo_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_rpinfo_json_cr():
    pass


@frr_show_ipv6_pim_vrf_rpinfo.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['X:X::X:X/M']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_rpinfo_multicastgrouprange():
    """Multicast Group range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_rpinfo_multicastgrouprange.name
    data_gen['MULTICAST_GROUP_RANGE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_rpinfo_multicastgrouprange.command('./	<cr>')
def frr_show_ipv6_pim_vrf_rpinfo_multicastgrouprange_cr():
    pass


@frr_show_ipv6_pim_vrf_rpinfo_multicastgrouprange.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_rpinfo_multicastgrouprange_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_rpinfo_multicastgrouprange_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_rpinfo_multicastgrouprange_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_rpinfo_multicastgrouprange_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='rpf', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_rpf(rpf_='rpf'):
    """PIM cached source rpf information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_rpf.name
    data_gen['rpf'] = rpf_='rpf'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_rpf.command('./	<cr>')
def frr_show_ipv6_pim_vrf_rpf_cr():
    pass


@frr_show_ipv6_pim_vrf_rpf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_rpf_json(rpf_json_='rpf_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_rpf_json.name
    data_gen['rpf_json'] = rpf_json_='rpf_json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_rpf_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_rpf_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='secondary', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_secondary(secondary_='secondary'):
    """PIM neighbor addresses"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_secondary.name
    data_gen['secondary'] = secondary_='secondary'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_secondary.command('./	<cr>')
def frr_show_ipv6_pim_vrf_secondary_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='state', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_state(state_='state'):
    """PIM state information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_state.name
    data_gen['state'] = state_='state'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_state.command('./	<cr>')
def frr_show_ipv6_pim_vrf_state_cr():
    pass


@frr_show_ipv6_pim_vrf_state.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_state_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_state_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_state_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_state_json_cr():
    pass


@frr_show_ipv6_pim_vrf_state.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_state_unicastormulticastaddress():
    """Unicast or Multicast address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_state_unicastormulticastaddress.name
    data_gen['UNICAST_OR_MULTICAST_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_state_unicastormulticastaddress.command('./	<cr>')
def frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_cr():
    pass


@frr_show_ipv6_pim_vrf_state_unicastormulticastaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_json_cr():
    pass


@frr_show_ipv6_pim_vrf_state_unicastormulticastaddress.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_multicastaddress():
    """Multicast address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_multicastaddress.name
    data_gen['MULTICAST_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_multicastaddress.command('./	<cr>')
def frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_multicastaddress_cr():
    pass


@frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_multicastaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_multicastaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_multicastaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_multicastaddress_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_state_unicastormulticastaddress_multicastaddress_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='statistics', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_statistics(statistics_='statistics'):
    """PIM statistics"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_statistics.name
    data_gen['statistics'] = statistics_='statistics'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_statistics.command('./	<cr>')
def frr_show_ipv6_pim_vrf_statistics_cr():
    pass


@frr_show_ipv6_pim_vrf_statistics.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
@click.argument('pim_interface', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_ipv6_pim_vrf_statistics_interface(pim_interface, statistics_interface_='statistics_interface'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_statistics_interface.name
    data_gen['statistics_interface'] = statistics_interface_='statistics_interface'
    data_gen['PIM_INTERFACE'] = pim_interface
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_statistics_interface.command('./	<cr>')
def frr_show_ipv6_pim_vrf_statistics_interface_cr():
    pass


@frr_show_ipv6_pim_vrf_statistics_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_statistics_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_statistics_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_statistics_interface_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_statistics_interface_json_cr():
    pass


@frr_show_ipv6_pim_vrf_statistics.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_statistics_json(statistics_json_='statistics_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_statistics_json.name
    data_gen['statistics_json'] = statistics_json_='statistics_json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_statistics_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_statistics_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='upstream', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_upstream(upstream_='upstream'):
    """PIM upstream information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_upstream.name
    data_gen['upstream'] = upstream_='upstream'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_upstream.command('./	<cr>')
def frr_show_ipv6_pim_vrf_upstream_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='upstream-join-desired', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_upstreamjoindesired(upstreamjoindesired_='upstream-join-desired'):
    """PIM upstream join-desired"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_upstreamjoindesired.name
    data_gen['upstream-join-desired'] = upstreamjoindesired_='upstream-join-desired'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_upstreamjoindesired.command('./	<cr>')
def frr_show_ipv6_pim_vrf_upstreamjoindesired_cr():
    pass


@frr_show_ipv6_pim_vrf_upstreamjoindesired.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_upstreamjoindesired_json(upstreamjoindesired_json_='upstream-join-desired_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_upstreamjoindesired_json.name
    data_gen['upstream-join-desired_json'] = upstreamjoindesired_json_='upstream-join-desired_json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_upstreamjoindesired_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_upstreamjoindesired_json_cr():
    pass


@frr_show_ipv6_pim_vrf.group(cls=FRR_AbbreviationGroup, name='upstream-rpf', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_upstreamrpf(upstreamrpf_='upstream-rpf'):
    """PIM upstream source rpf"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_upstreamrpf.name
    data_gen['upstream-rpf'] = upstreamrpf_='upstream-rpf'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_upstreamrpf.command('./	<cr>')
def frr_show_ipv6_pim_vrf_upstreamrpf_cr():
    pass


@frr_show_ipv6_pim_vrf_upstreamrpf.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_upstreamrpf_json(upstreamrpf_json_='upstream-rpf_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_upstreamrpf_json.name
    data_gen['upstream-rpf_json'] = upstreamrpf_json_='upstream-rpf_json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_upstreamrpf_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_upstreamrpf_json_cr():
    pass


@frr_show_ipv6_pim_vrf_upstream.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_upstream_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_upstream_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_upstream_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_upstream_json_cr():
    pass


@frr_show_ipv6_pim_vrf_upstream.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_upstream_thesourceorgroup():
    """The Source or Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_upstream_thesourceorgroup.name
    data_gen['THE_SOURCE_OR_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_upstream_thesourceorgroup.command('./	<cr>')
def frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_cr():
    pass


@frr_show_ipv6_pim_vrf_upstream_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_json_cr():
    pass


@frr_show_ipv6_pim_vrf_upstream_thesourceorgroup.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_thegroup():
    """The Group"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_thegroup.name
    data_gen['THE_GROUP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_thegroup.command('./	<cr>')
def frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_thegroup_cr():
    pass


@frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_thegroup.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_thegroup_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_thegroup_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_pim_vrf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_pim_vrf'][key] = val
    
    # set VIEW_NODE -> show_ipv6_pim_vrf table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_pim_vrf'
    pass


@frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_thegroup_json.command('./	<cr>')
def frr_show_ipv6_pim_vrf_upstream_thesourceorgroup_thegroup_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='prefix-list', invoke_without_command=True)
def frr_show_ipv6_prefixlist(show_ipv6_prefixlist_='show_ipv6_prefix-list'):
    """Build a prefix list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist.name
    
    if 'VIEW_NODE|show_ipv6_prefix-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list'
    pass


@frr_show_ipv6_prefixlist.command('./	<cr>')
def frr_show_ipv6_prefixlist_cr():
    pass


@frr_show_ipv6_prefixlist.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_ipv6_prefixlist_detail(show_ipv6_prefixlist_detail_='show_ipv6_prefix-list_detail'):
    """Detail of prefix lists"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_detail.name
    
    if 'VIEW_NODE|show_ipv6_prefix-list_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list_detail'
    pass


@frr_show_ipv6_prefixlist_detail.command('./	<cr>')
def frr_show_ipv6_prefixlist_detail_cr():
    pass


@frr_show_ipv6_prefixlist_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_prefixlist_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_prefix-list_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list_detail'
    pass


@frr_show_ipv6_prefixlist_detail_json.command('./	<cr>')
def frr_show_ipv6_prefixlist_detail_json_cr():
    pass


@frr_show_ipv6_prefixlist_detail.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_prefixlist_detail_nameofaprefix():
    """Name of a prefix list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_detail_nameofaprefix.name
    data_gen['NAME_OF_A_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_prefix-list_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list_detail'
    pass


@frr_show_ipv6_prefixlist_detail_nameofaprefix.command('./	<cr>')
def frr_show_ipv6_prefixlist_detail_nameofaprefix_cr():
    pass


@frr_show_ipv6_prefixlist_detail_nameofaprefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_prefixlist_detail_nameofaprefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_detail_nameofaprefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_prefix-list_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_detail'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list_detail'
    pass


@frr_show_ipv6_prefixlist_detail_nameofaprefix_json.command('./	<cr>')
def frr_show_ipv6_prefixlist_detail_nameofaprefix_json_cr():
    pass


@frr_show_ipv6_prefixlist.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_prefixlist_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_prefix-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list'
    pass


@frr_show_ipv6_prefixlist_json.command('./	<cr>')
def frr_show_ipv6_prefixlist_json_cr():
    pass


@frr_show_ipv6_prefixlist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_prefixlist_nameofaprefix():
    """Name of a prefix list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_nameofaprefix.name
    data_gen['NAME_OF_A_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_prefix-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list'
    pass


@frr_show_ipv6_prefixlist_nameofaprefix.command('./	<cr>')
def frr_show_ipv6_prefixlist_nameofaprefix_cr():
    pass


@frr_show_ipv6_prefixlist_nameofaprefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['X:X::X:X/M']), invoke_without_command=True)
def frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix():
    """IPv6 prefix <network>/<length>, e.g., 3ffe::/16"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix.name
    data_gen['IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_prefix-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list'
    pass


@frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix.command('./	<cr>')
def frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix_cr():
    pass


@frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix.group(cls=FRR_AbbreviationGroup, name='first-match', invoke_without_command=True)
def frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix_firstmatch(firstmatch_='first-match'):
    """First matched prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix_firstmatch.name
    data_gen['first-match'] = firstmatch_='first-match'
    
    if 'VIEW_NODE|show_ipv6_prefix-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list'
    pass


@frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix_firstmatch.command('./	<cr>')
def frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix_firstmatch_cr():
    pass


@frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer', invoke_without_command=True)
def frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix_longer(longer_='longer'):
    """Lookup longer prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix_longer.name
    data_gen['longer'] = longer_='longer'
    
    if 'VIEW_NODE|show_ipv6_prefix-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list'
    pass


@frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix_longer.command('./	<cr>')
def frr_show_ipv6_prefixlist_nameofaprefix_ipv6prefix_longer_cr():
    pass


@frr_show_ipv6_prefixlist_nameofaprefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_prefixlist_nameofaprefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_nameofaprefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_prefix-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list'
    pass


@frr_show_ipv6_prefixlist_nameofaprefix_json.command('./	<cr>')
def frr_show_ipv6_prefixlist_nameofaprefix_json_cr():
    pass


@frr_show_ipv6_prefixlist_nameofaprefix.group(cls=FRR_AbbreviationGroup, name='seq', invoke_without_command=True)
@click.argument('sequence_number', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_prefixlist_nameofaprefix_seq(sequence_number, seq_='seq'):
    """sequence number of an entry"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_nameofaprefix_seq.name
    data_gen['seq'] = seq_='seq'
    data_gen['SEQUENCE_NUMBER'] = sequence_number
    
    if 'VIEW_NODE|show_ipv6_prefix-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list'
    pass


@frr_show_ipv6_prefixlist_nameofaprefix_seq.command('./	<cr>')
def frr_show_ipv6_prefixlist_nameofaprefix_seq_cr():
    pass


@frr_show_ipv6_prefixlist_nameofaprefix_seq.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_prefixlist_nameofaprefix_seq_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_nameofaprefix_seq_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_prefix-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list'
    pass


@frr_show_ipv6_prefixlist_nameofaprefix_seq_json.command('./	<cr>')
def frr_show_ipv6_prefixlist_nameofaprefix_seq_json_cr():
    pass


@frr_show_ipv6_prefixlist.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_ipv6_prefixlist_summary(show_ipv6_prefixlist_summary_='show_ipv6_prefix-list_summary'):
    """Summary of prefix lists"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_summary.name
    
    if 'VIEW_NODE|show_ipv6_prefix-list_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list_summary'
    pass


@frr_show_ipv6_prefixlist_summary.command('./	<cr>')
def frr_show_ipv6_prefixlist_summary_cr():
    pass


@frr_show_ipv6_prefixlist_summary.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_prefixlist_summary_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_summary_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_prefix-list_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list_summary'
    pass


@frr_show_ipv6_prefixlist_summary_json.command('./	<cr>')
def frr_show_ipv6_prefixlist_summary_json_cr():
    pass


@frr_show_ipv6_prefixlist_summary.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD']), invoke_without_command=True)
def frr_show_ipv6_prefixlist_summary_nameofaprefix():
    """Name of a prefix list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_summary_nameofaprefix.name
    data_gen['NAME_OF_A_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_prefix-list_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list_summary'
    pass


@frr_show_ipv6_prefixlist_summary_nameofaprefix.command('./	<cr>')
def frr_show_ipv6_prefixlist_summary_nameofaprefix_cr():
    pass


@frr_show_ipv6_prefixlist_summary_nameofaprefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_prefixlist_summary_nameofaprefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_prefixlist_summary_nameofaprefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_prefix-list_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_prefix-list_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_prefix-list_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_prefix-list_summary'
    pass


@frr_show_ipv6_prefixlist_summary_nameofaprefix_json.command('./	<cr>')
def frr_show_ipv6_prefixlist_summary_nameofaprefix_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='protocol', invoke_without_command=True)
def frr_show_ipv6_protocol(show_ipv6_protocol_='show_ipv6_protocol'):
    """IPv6 protocol filtering status"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_protocol.name
    
    if 'VIEW_NODE|show_ipv6_protocol' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_protocol'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_protocol']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_protocol'][key] = val
    
    # set VIEW_NODE -> show_ipv6_protocol table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_protocol'
    pass


@frr_show_ipv6_protocol.command('./	<cr>')
def frr_show_ipv6_protocol_cr():
    pass


@frr_show_ipv6_protocol.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_ipv6_protocol_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_protocol_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_ipv6_protocol' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_protocol'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_protocol']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_protocol'][key] = val
    
    # set VIEW_NODE -> show_ipv6_protocol table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_protocol'
    pass


@frr_show_ipv6_protocol_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['NAME', 'all']), invoke_without_command=True)
def frr_show_ipv6_protocol_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_protocol_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_protocol' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_protocol'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_protocol']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_protocol'][key] = val
    
    # set VIEW_NODE -> show_ipv6_protocol table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_protocol'
    pass


@frr_show_ipv6_protocol_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_ipv6_protocol_vrf_vrfchoicecase_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ripng', invoke_without_command=True)
def frr_show_ipv6_ripng(show_ipv6_ripng_='show_ipv6_ripng'):
    """Show RIPng routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ripng.name
    
    if 'VIEW_NODE|show_ipv6_ripng' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ripng table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ripng'
    pass


@frr_show_ipv6_ripng.command('./	<cr>')
def frr_show_ipv6_ripng_cr():
    pass


@frr_show_ipv6_ripng.group(cls=FRR_AbbreviationGroup, name='status', invoke_without_command=True)
def frr_show_ipv6_ripng_status(status_='status'):
    """IPv6 routing protocol process parameters and statistics"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ripng_status.name
    data_gen['status'] = status_='status'
    
    if 'VIEW_NODE|show_ipv6_ripng' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ripng table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ripng'
    pass


@frr_show_ipv6_ripng_status.command('./	<cr>')
def frr_show_ipv6_ripng_status_cr():
    pass


@frr_show_ipv6_ripng.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_ipv6_ripng_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ripng_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_ripng' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ripng table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ripng'
    pass


@frr_show_ipv6_ripng_vrf.command('./	<cr>')
def frr_show_ipv6_ripng_vrf_cr():
    pass


@frr_show_ipv6_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='status', invoke_without_command=True)
def frr_show_ipv6_ripng_vrf_status(status_='status'):
    """IPv6 routing protocol process parameters and statistics"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_ripng_vrf_status.name
    data_gen['status'] = status_='status'
    
    if 'VIEW_NODE|show_ipv6_ripng' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_ripng'][key] = val
    
    # set VIEW_NODE -> show_ipv6_ripng table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_ripng'
    pass


@frr_show_ipv6_ripng_vrf_status.command('./	<cr>')
def frr_show_ipv6_ripng_vrf_status_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
def frr_show_ipv6_route(show_ipv6_route_='show_ipv6_route'):
    """IP routing table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route.name
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route.command('./	<cr>')
def frr_show_ipv6_route_cr():
    pass


@frr_show_ipv6_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_choicecase():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_choicecase.command('./	<cr>')
def frr_show_ipv6_route_choicecase_cr():
    pass


@frr_show_ipv6_route_choicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_choicecase_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_choicecase_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_choicecase_format.command('./	<cr>')
def frr_show_ipv6_route_choicecase_format_cr():
    pass


@frr_show_ipv6_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_format.command('./	<cr>')
def frr_show_ipv6_route_format_cr():
    pass


@frr_show_ipv6_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_route_ipv6address():
    """IPv6 Address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_ipv6address.name
    data_gen['IPV6_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_ipv6address.command('./	<cr>')
def frr_show_ipv6_route_ipv6address_cr():
    pass


@frr_show_ipv6_route_ipv6address.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_route_ipv6address_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_ipv6address_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_ipv6address_json.command('./	<cr>')
def frr_show_ipv6_route_ipv6address_json_cr():
    pass


@frr_show_ipv6_route_ipv6address_json.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_ipv6_route_ipv6address_json_nexthopgroup(json_nexthopgroup_='json_nexthop-group'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_ipv6address_json_nexthopgroup.name
    data_gen['json_nexthop-group'] = json_nexthopgroup_='json_nexthop-group'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_ipv6address_json_nexthopgroup.command('./	<cr>')
def frr_show_ipv6_route_ipv6address_json_nexthopgroup_cr():
    pass


@frr_show_ipv6_route_ipv6address.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_ipv6_route_ipv6address_nexthopgroup(nexthopgroup_='nexthop-group'):
    """Nexthop Group Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_ipv6address_nexthopgroup.name
    data_gen['nexthop-group'] = nexthopgroup_='nexthop-group'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_ipv6address_nexthopgroup.command('./	<cr>')
def frr_show_ipv6_route_ipv6address_nexthopgroup_cr():
    pass


@frr_show_ipv6_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['X:X::X:X/M']),)
def frr_show_ipv6_route_ipv6prefix():
    """3"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_ipv6prefix.name
    data_gen['IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_ipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer-prefixes', invoke_without_command=True)
def frr_show_ipv6_route_ipv6prefix_longerprefixes(longerprefixes_='longer-prefixes'):
    """Show route matching the specified Network/Mask pair only"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_ipv6prefix_longerprefixes.name
    data_gen['longer-prefixes'] = longerprefixes_='longer-prefixes'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_ipv6prefix_longerprefixes.command('./	<cr>')
def frr_show_ipv6_route_ipv6prefix_longerprefixes_cr():
    pass


@frr_show_ipv6_route_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_ipv6prefix_longerprefixes_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_ipv6prefix_longerprefixes_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_ipv6prefix_longerprefixes_format.command('./	<cr>')
def frr_show_ipv6_route_ipv6prefix_longerprefixes_format_cr():
    pass


@frr_show_ipv6_route_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_ipv6prefix_longerprefixes_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_ipv6prefix_longerprefixes_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_ipv6prefix_longerprefixes_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_ipv6prefix_longerprefixes_frrip6redist_cr():
    pass


@frr_show_ipv6_route_ipv6prefix_longerprefixes_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_ipv6prefix_longerprefixes_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_ipv6prefix_longerprefixes_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_ipv6prefix_longerprefixes_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_ipv6prefix_longerprefixes_frrip6redist_format_cr():
    pass


@frr_show_ipv6_route.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_ipv6_route_summary(show_ipv6_route_summary_='show_ipv6_route_summary'):
    """Summary of all routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_summary.name
    
    if 'VIEW_NODE|show_ipv6_route_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_summary'
    pass


@frr_show_ipv6_route_summary.command('./	<cr>')
def frr_show_ipv6_route_summary_cr():
    pass


@frr_show_ipv6_route_summary.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_route_summary_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_summary_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_route_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_summary'
    pass


@frr_show_ipv6_route_summary_json.command('./	<cr>')
def frr_show_ipv6_route_summary_json_cr():
    pass


@frr_show_ipv6_route_summary.group(cls=FRR_AbbreviationGroup, name='prefix', invoke_without_command=True)
def frr_show_ipv6_route_summary_prefix(show_ipv6_route_summary_prefix_='show_ipv6_route_summary_prefix'):
    """Prefix routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_summary_prefix.name
    
    if 'VIEW_NODE|show_ipv6_route_summary_prefix' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary_prefix'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary_prefix']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary_prefix'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_summary_prefix table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_summary_prefix'
    pass


@frr_show_ipv6_route_summary_prefix.command('./	<cr>')
def frr_show_ipv6_route_summary_prefix_cr():
    pass


@frr_show_ipv6_route_summary_prefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_route_summary_prefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_summary_prefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_route_summary_prefix' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary_prefix'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary_prefix']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary_prefix'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_summary_prefix table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_summary_prefix'
    pass


@frr_show_ipv6_route_summary_prefix_json.command('./	<cr>')
def frr_show_ipv6_route_summary_prefix_json_cr():
    pass


@frr_show_ipv6_route_summary.group(cls=FRR_AbbreviationGroup, name='table', invoke_without_command=True)
@click.argument('the_table_number', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_route_summary_table(the_table_number, table_='table'):
    """Table to display summary for"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_summary_table.name
    data_gen['table'] = table_='table'
    data_gen['THE_TABLE_NUMBER'] = the_table_number
    
    if 'VIEW_NODE|show_ipv6_route_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_summary'
    pass


@frr_show_ipv6_route_summary_table.command('./	<cr>')
def frr_show_ipv6_route_summary_table_cr():
    pass


@frr_show_ipv6_route_summary_table.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_route_summary_table_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_summary_table_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_route_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_summary'
    pass


@frr_show_ipv6_route_summary_table_json.command('./	<cr>')
def frr_show_ipv6_route_summary_table_json_cr():
    pass


@frr_show_ipv6_route_summary_table.group(cls=FRR_AbbreviationGroup, name='prefix', invoke_without_command=True)
def frr_show_ipv6_route_summary_table_prefix(prefix_='prefix'):
    """Prefix routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_summary_table_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    
    if 'VIEW_NODE|show_ipv6_route_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_summary'
    pass


@frr_show_ipv6_route_summary_table_prefix.command('./	<cr>')
def frr_show_ipv6_route_summary_table_prefix_cr():
    pass


@frr_show_ipv6_route_summary_table_prefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_route_summary_table_prefix_json(prefix_json_='prefix_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_summary_table_prefix_json.name
    data_gen['prefix_json'] = prefix_json_='prefix_json'
    
    if 'VIEW_NODE|show_ipv6_route_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_summary'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_summary'
    pass


@frr_show_ipv6_route_summary_table_prefix_json.command('./	<cr>')
def frr_show_ipv6_route_summary_table_prefix_json_cr():
    pass


@frr_show_ipv6_route.group(cls=FRR_AbbreviationGroup, name='table', invoke_without_command=True)
def frr_show_ipv6_route_table(show_ipv6_route_table_='show_ipv6_route_table'):
    """Table to display"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table.name
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table.command('./	<cr>')
def frr_show_ipv6_route_table_cr():
    pass


@frr_show_ipv6_route_table.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, [(1, 4294967295), 'all']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase():
    """The table number to display"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_cr():
    pass


@frr_show_ipv6_route_table_choicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_frrip6redist_cr():
    pass


@frr_show_ipv6_route_table_choicecase_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_frrip6redist_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X/M']),)
def frr_show_ipv6_route_table_choicecase_ipv6prefix():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_ipv6prefix.name
    data_gen['IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_ipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer-prefixes', invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes(longerprefixes_='longer-prefixes'):
    """Show route matching the specified Network/Mask pair only"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes.name
    data_gen['longer-prefixes'] = longerprefixes_='longer-prefixes'
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_cr():
    pass


@frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_frrip6redist_cr():
    pass


@frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_ipv6prefix_longerprefixes_frrip6redist_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_route_table_choicecase_tag(tag_value, tag_='tag'):
    """Show only routes with tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['TAG_VALUE'] = tag_value
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_tag.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_tag_cr():
    pass


@frr_show_ipv6_route_table_choicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_tag_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_tag_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_tag_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_tag_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_tag_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_tag_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_tag_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_tag_frrip6redist_cr():
    pass


@frr_show_ipv6_route_table_choicecase_tag_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_tag_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_tag_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_tag_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_tag_frrip6redist_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_ipv6_route_table_choicecase_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['NAME', 'all']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_frrip6redist_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_frrip6redist_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['X:X::X:X/M']),)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix():
    """8"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix.name
    data_gen['IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer-prefixes', invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes(longerprefixes_='longer-prefixes'):
    """Show route matching the specified Network/Mask pair only"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes.name
    data_gen['longer-prefixes'] = longerprefixes_='longer-prefixes'
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(12, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag(tag_value, tag_='tag'):
    """Show only routes with tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['TAG_VALUE'] = tag_value
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_format_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist_cr():
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_table_choicecase_vrf_vrfchoicecase_tag_frrip6redist_format_cr():
    pass


@frr_show_ipv6_route_table.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_table_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_table_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route_table'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route_table'
    pass


@frr_show_ipv6_route_table_format.command('./	<cr>')
def frr_show_ipv6_route_table_format_cr():
    pass


@frr_show_ipv6_route.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_route_tag(tag_value, tag_='tag'):
    """Show only routes with tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['TAG_VALUE'] = tag_value
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_tag.command('./	<cr>')
def frr_show_ipv6_route_tag_cr():
    pass


@frr_show_ipv6_route_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_tag_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_tag_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_tag_format.command('./	<cr>')
def frr_show_ipv6_route_tag_format_cr():
    pass


@frr_show_ipv6_route_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_tag_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_tag_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_tag_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_tag_frrip6redist_cr():
    pass


@frr_show_ipv6_route_tag_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_tag_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_tag_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_tag_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_tag_frrip6redist_format_cr():
    pass


@frr_show_ipv6_route.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_ipv6_route_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['NAME', 'all']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase():
    """The VRF name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_format.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_format_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_frrip6redist_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_frrip6redist_format_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address():
    """IPv6 Address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address.name
    data_gen['IPV6_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_json.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_json_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_json.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_json_nexthopgroup(json_nexthopgroup_='json_nexthop-group'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_json_nexthopgroup.name
    data_gen['json_nexthop-group'] = json_nexthopgroup_='json_nexthop-group'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_json_nexthopgroup.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_json_nexthopgroup_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_nexthopgroup(nexthopgroup_='nexthop-group'):
    """Nexthop Group Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_nexthopgroup.name
    data_gen['nexthop-group'] = nexthopgroup_='nexthop-group'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_nexthopgroup.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6address_nexthopgroup_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X/M']),)
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix.name
    data_gen['IPV6_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix.group(cls=FRR_AbbreviationGroup, name='longer-prefixes', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes(longerprefixes_='longer-prefixes'):
    """Show route matching the specified Network/Mask pair only"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes.name
    data_gen['longer-prefixes'] = longerprefixes_='longer-prefixes'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_format_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_ipv6prefix_longerprefixes_frrip6redist_format_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_summary(summary_='summary'):
    """Summary of all routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_summary.name
    data_gen['summary'] = summary_='summary'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_json(summary_json_='summary_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_summary_json.name
    data_gen['summary_json'] = summary_json_='summary_json'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_json.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_json_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary.group(cls=FRR_AbbreviationGroup, name='prefix', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_prefix(summary_prefix_='summary_prefix'):
    """Prefix routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_summary_prefix.name
    data_gen['summary_prefix'] = summary_prefix_='summary_prefix'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_prefix.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_prefix_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_prefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_prefix_json(summary_prefix_json_='summary_prefix_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_summary_prefix_json.name
    data_gen['summary_prefix_json'] = summary_prefix_json_='summary_prefix_json'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_prefix_json.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_prefix_json_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary.group(cls=FRR_AbbreviationGroup, name='table', invoke_without_command=True)
@click.argument('the_table_number', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_table(the_table_number, summary_table_='summary_table'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_summary_table.name
    data_gen['summary_table'] = summary_table_='summary_table'
    data_gen['THE_TABLE_NUMBER'] = the_table_number
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_table.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_table.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_json.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_json_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_table.group(cls=FRR_AbbreviationGroup, name='prefix', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_prefix(prefix_='prefix'):
    """Prefix routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_prefix.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_prefix_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_prefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_prefix_json(prefix_json_='prefix_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_prefix_json.name
    data_gen['prefix_json'] = prefix_json_='prefix_json'
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_prefix_json.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_summary_table_prefix_json_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_ipv6_route_vrf_vrfchoicecase_tag(tag_value, tag_='tag'):
    """Show only routes with tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['TAG_VALUE'] = tag_value
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_tag.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_tag_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_tag_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_tag_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_tag_format.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_tag_format_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_tag.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['babel', 'bgp', 'connected', 'isis', 'kernel', 'nhrp', 'openfabric', 'ospf6', 'ripng', 'static', 'table', 'vnc']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_tag_frrip6redist():
    """Babel routing protocol (Babel)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_tag_frrip6redist.name
    data_gen['FRR_IP6_REDIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_tag_frrip6redist.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_tag_frrip6redist_cr():
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_tag_frrip6redist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['json', 'nexthop-group']), invoke_without_command=True)
def frr_show_ipv6_route_vrf_vrfchoicecase_tag_frrip6redist_format():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_route_vrf_vrfchoicecase_tag_frrip6redist_format.name
    data_gen['FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_ipv6_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_route'
    pass


@frr_show_ipv6_route_vrf_vrfchoicecase_tag_frrip6redist_format.command('./	<cr>')
def frr_show_ipv6_route_vrf_vrfchoicecase_tag_frrip6redist_format_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
def frr_show_ipv6_routerid(show_ipv6_routerid_='show_ipv6_router-id'):
    """Show the configured router-id"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_routerid.name
    
    if 'VIEW_NODE|show_ipv6_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_router-id'][key] = val
    
    # set VIEW_NODE -> show_ipv6_router-id table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_router-id'
    pass


@frr_show_ipv6_routerid.command('./	<cr>')
def frr_show_ipv6_routerid_cr():
    pass


@frr_show_ipv6_routerid.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_ipv6_routerid_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_routerid_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_router-id'][key] = val
    
    # set VIEW_NODE -> show_ipv6_router-id table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_router-id'
    pass


@frr_show_ipv6_routerid_vrf.command('./	<cr>')
def frr_show_ipv6_routerid_vrf_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_show_ipv6_zebra():
    """Zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_zebra.name
    
    if 'VIEW_NODE|show_ipv6_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra'][key] = val
    
    # set VIEW_NODE -> show_ipv6_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_zebra'
    pass


@frr_show_ipv6_zebra.command('./	<cr>')
def frr_show_ipv6_zebra_cr():
    pass


@frr_show_ipv6_zebra.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
def frr_show_ipv6_zebra_route():
    """Routing table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_zebra_route.name
    
    if 'VIEW_NODE|show_ipv6_zebra_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra_route'][key] = val
    
    # set VIEW_NODE -> show_ipv6_zebra_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_zebra_route'
    pass


@frr_show_ipv6_zebra_route.command('./	<cr>')
def frr_show_ipv6_zebra_route_cr():
    pass


@frr_show_ipv6_zebra_route.group(cls=FRR_AbbreviationGroup, name='dump', invoke_without_command=True)
def frr_show_ipv6_zebra_route_dump(show_ipv6_zebra_route_dump_='show_ipv6_zebra_route_dump'):
    """All information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_zebra_route_dump.name
    
    if 'VIEW_NODE|show_ipv6_zebra_route_dump' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra_route_dump'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra_route_dump']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra_route_dump'][key] = val
    
    # set VIEW_NODE -> show_ipv6_zebra_route_dump table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_zebra_route_dump'
    pass


@frr_show_ipv6_zebra_route_dump.command('./	<cr>')
def frr_show_ipv6_zebra_route_dump_cr():
    pass


@frr_show_ipv6_zebra_route_dump.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='VRFNAME', required=True, type=FRR_TYPE('VRFNAME'))
def frr_show_ipv6_zebra_route_dump_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_ipv6_zebra_route_dump_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_ipv6_zebra_route_dump' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra_route_dump'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra_route_dump']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_ipv6_zebra_route_dump'][key] = val
    
    # set VIEW_NODE -> show_ipv6_zebra_route_dump table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_ipv6_zebra_route_dump'
    pass


@frr_show_ipv6_zebra_route_dump_vrf.command('./	<cr>')
def frr_show_ipv6_zebra_route_dump_vrf_cr():
    pass

