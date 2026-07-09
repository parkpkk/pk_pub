import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='fec', invoke_without_command=True)
def frr_show_mpls_fec(show_mpls_fec_='show_mpls_fec'):
    """MPLS FEC table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_fec.name
    
    if 'VIEW_NODE|show_mpls_fec' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_fec'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_fec']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_fec'][key] = val
    
    # set VIEW_NODE -> show_mpls_fec table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_fec'
    pass


@frr_show_mpls_fec.command('./	<cr>')
def frr_show_mpls_fec_cr():
    pass


@frr_show_mpls_fec.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_mpls_fec_ipprefix():
    """FEC to display information about"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_fec_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_mpls_fec' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_fec'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_fec']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_fec'][key] = val
    
    # set VIEW_NODE -> show_mpls_fec table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_fec'
    pass


@frr_show_mpls_fec_ipprefix.command('./	<cr>')
def frr_show_mpls_fec_ipprefix_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ldp',)
def frr_show_mpls_ldp(show_mpls_ldp_='show_mpls_ldp'):
    """Label Distribution Protocol"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp.name
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp.group(cls=FRR_AbbreviationGroup, name='binding', invoke_without_command=True)
def frr_show_mpls_ldp_binding(show_mpls_ldp_binding_='show_mpls_ldp_binding'):
    """Label Information Base (LIB) information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding.name
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding.command('./	<cr>')
def frr_show_mpls_ldp_binding_cr():
    pass


@frr_show_mpls_ldp_binding.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_detail(show_mpls_ldp_binding_detail_='show_mpls_ldp_binding_detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_detail.name
    
    if 'VIEW_NODE|show_mpls_ldp_binding_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding_detail'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding_detail'
    pass


@frr_show_mpls_ldp_binding_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_detail_cr():
    pass


@frr_show_mpls_ldp_binding_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding_detail'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding_detail'
    pass


@frr_show_mpls_ldp_binding_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix():
    """Destination prefix (IPv4)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_detail_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='local-label', invoke_without_command=True)
@click.argument('locally_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_binding_ipprefix_locallabel(locally_assigned_label_value, locallabel_='local-label'):
    """Match locally assigned label values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_locallabel.name
    data_gen['local-label'] = locallabel_='local-label'
    data_gen['LOCALLY_ASSIGNED_LABEL_VALUE'] = locally_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_locallabel.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_locallabel_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_locallabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_locallabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_locallabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_locallabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_locallabel_detail_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_locallabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_locallabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_locallabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_locallabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_locallabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_locallabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_locallabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_locallabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_locallabel_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_locallabel_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='longer-prefixes', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes(longerprefixes_='longer-prefixes'):
    """Include longer matches"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes.name
    data_gen['longer-prefixes'] = longerprefixes_='longer-prefixes'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_detail(longerprefixes_detail_='longer-prefixes_detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_detail.name
    data_gen['longer-prefixes_detail'] = longerprefixes_detail_='longer-prefixes_detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_detail_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_detail_json(longerprefixes_detail_json_='longer-prefixes_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_detail_json.name
    data_gen['longer-prefixes_detail_json'] = longerprefixes_detail_json_='longer-prefixes_detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_json(longerprefixes_json_='longer-prefixes_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_json.name
    data_gen['longer-prefixes_json'] = longerprefixes_json_='longer-prefixes_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name='local-label', invoke_without_command=True)
@click.argument('locally_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel(locally_assigned_label_value, longerprefixes_locallabel_='longer-prefixes_local-label'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel.name
    data_gen['longer-prefixes_local-label'] = longerprefixes_locallabel_='longer-prefixes_local-label'
    data_gen['LOCALLY_ASSIGNED_LABEL_VALUE'] = locally_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_detail_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_locallabel_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_lsrid', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor(neighbor_lsrid, longerprefixes_neighbor_='longer-prefixes_neighbor'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor.name
    data_gen['longer-prefixes_neighbor'] = longerprefixes_neighbor_='longer-prefixes_neighbor'
    data_gen['NEIGHBOR_LSR-ID'] = neighbor_lsrid
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_detail_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_neighbor_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name='remote-label', invoke_without_command=True)
@click.argument('remotely_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel(remotely_assigned_label_value, longerprefixes_remotelabel_='longer-prefixes_remote-label'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel.name
    data_gen['longer-prefixes_remote-label'] = longerprefixes_remotelabel_='longer-prefixes_remote-label'
    data_gen['REMOTELY_ASSIGNED_LABEL_VALUE'] = remotely_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_detail_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_longerprefixes_remotelabel_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_lsrid', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_mpls_ldp_binding_ipprefix_neighbor(neighbor_lsrid, neighbor_='neighbor'):
    """Display labels from LDP neighbor"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    data_gen['NEIGHBOR_LSR-ID'] = neighbor_lsrid
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_neighbor.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_neighbor_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_neighbor_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_neighbor_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_neighbor_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_neighbor_detail_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_neighbor_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_neighbor_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_neighbor_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_neighbor_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_neighbor_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_neighbor_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='remote-label', invoke_without_command=True)
@click.argument('remotely_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_binding_ipprefix_remotelabel(remotely_assigned_label_value, remotelabel_='remote-label'):
    """Match remotely assigned label values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_remotelabel.name
    data_gen['remote-label'] = remotelabel_='remote-label'
    data_gen['REMOTELY_ASSIGNED_LABEL_VALUE'] = remotely_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_remotelabel.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_remotelabel_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_remotelabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_remotelabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_remotelabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_remotelabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_remotelabel_detail_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_remotelabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_remotelabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_remotelabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_remotelabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_remotelabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_ipprefix_remotelabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_ipprefix_remotelabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_ipprefix_remotelabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_ipprefix_remotelabel_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_ipprefix_remotelabel_json_cr():
    pass


@frr_show_mpls_ldp_binding.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_json_cr():
    pass


@frr_show_mpls_ldp_binding.group(cls=FRR_AbbreviationGroup, name='local-label', invoke_without_command=True)
@click.argument('locally_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_binding_locallabel(locally_assigned_label_value, locallabel_='local-label'):
    """Match locally assigned label values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_locallabel.name
    data_gen['local-label'] = locallabel_='local-label'
    data_gen['LOCALLY_ASSIGNED_LABEL_VALUE'] = locally_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_locallabel.command('./	<cr>')
def frr_show_mpls_ldp_binding_locallabel_cr():
    pass


@frr_show_mpls_ldp_binding_locallabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_locallabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_locallabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_locallabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_locallabel_detail_cr():
    pass


@frr_show_mpls_ldp_binding_locallabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_locallabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_locallabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_locallabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_locallabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_locallabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_locallabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_locallabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_locallabel_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_locallabel_json_cr():
    pass


@frr_show_mpls_ldp_binding.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_lsrid', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_mpls_ldp_binding_neighbor(neighbor_lsrid, neighbor_='neighbor'):
    """Display labels from LDP neighbor"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    data_gen['NEIGHBOR_LSR-ID'] = neighbor_lsrid
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_neighbor.command('./	<cr>')
def frr_show_mpls_ldp_binding_neighbor_cr():
    pass


@frr_show_mpls_ldp_binding_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_neighbor_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_neighbor_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_neighbor_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_neighbor_detail_cr():
    pass


@frr_show_mpls_ldp_binding_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_neighbor_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_neighbor_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_neighbor_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_neighbor_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_neighbor_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_neighbor_json_cr():
    pass


@frr_show_mpls_ldp_binding.group(cls=FRR_AbbreviationGroup, name='remote-label', invoke_without_command=True)
@click.argument('remotely_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_binding_remotelabel(remotely_assigned_label_value, remotelabel_='remote-label'):
    """Match remotely assigned label values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_remotelabel.name
    data_gen['remote-label'] = remotelabel_='remote-label'
    data_gen['REMOTELY_ASSIGNED_LABEL_VALUE'] = remotely_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_remotelabel.command('./	<cr>')
def frr_show_mpls_ldp_binding_remotelabel_cr():
    pass


@frr_show_mpls_ldp_binding_remotelabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_binding_remotelabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_remotelabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_remotelabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_binding_remotelabel_detail_cr():
    pass


@frr_show_mpls_ldp_binding_remotelabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_remotelabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_remotelabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_remotelabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_remotelabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_binding_remotelabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_binding_remotelabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_binding_remotelabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_binding'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_binding'
    pass


@frr_show_mpls_ldp_binding_remotelabel_json.command('./	<cr>')
def frr_show_mpls_ldp_binding_remotelabel_json_cr():
    pass


@frr_show_mpls_ldp.group(cls=FRR_AbbreviationGroup, name='capabilities', invoke_without_command=True)
def frr_show_mpls_ldp_capabilities(show_mpls_ldp_capabilities_='show_mpls_ldp_capabilities'):
    """Display LDP Capabilities information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_capabilities.name
    
    if 'VIEW_NODE|show_mpls_ldp_capabilities' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_capabilities'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_capabilities']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_capabilities'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_capabilities table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_capabilities'
    pass


@frr_show_mpls_ldp_capabilities.command('./	<cr>')
def frr_show_mpls_ldp_capabilities_cr():
    pass


@frr_show_mpls_ldp_capabilities.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_capabilities_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_capabilities_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_capabilities' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_capabilities'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_capabilities']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_capabilities'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_capabilities table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_capabilities'
    pass


@frr_show_mpls_ldp_capabilities_json.command('./	<cr>')
def frr_show_mpls_ldp_capabilities_json_cr():
    pass


@frr_show_mpls_ldp.group(cls=FRR_AbbreviationGroup, name='discovery', invoke_without_command=True)
def frr_show_mpls_ldp_discovery(show_mpls_ldp_discovery_='show_mpls_ldp_discovery'):
    """Discovery Hello Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_discovery.name
    
    if 'VIEW_NODE|show_mpls_ldp_discovery' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_discovery table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_discovery'
    pass


@frr_show_mpls_ldp_discovery.command('./	<cr>')
def frr_show_mpls_ldp_discovery_cr():
    pass


@frr_show_mpls_ldp_discovery.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_discovery_detail(show_mpls_ldp_discovery_detail_='show_mpls_ldp_discovery_detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_discovery_detail.name
    
    if 'VIEW_NODE|show_mpls_ldp_discovery_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery_detail'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_discovery_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_discovery_detail'
    pass


@frr_show_mpls_ldp_discovery_detail.command('./	<cr>')
def frr_show_mpls_ldp_discovery_detail_cr():
    pass


@frr_show_mpls_ldp_discovery_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_discovery_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_discovery_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_discovery_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery_detail'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_discovery_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_discovery_detail'
    pass


@frr_show_mpls_ldp_discovery_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_discovery_detail_json_cr():
    pass


@frr_show_mpls_ldp_discovery.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_discovery_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_discovery_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_discovery' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_discovery'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_discovery table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_discovery'
    pass


@frr_show_mpls_ldp_discovery_json.command('./	<cr>')
def frr_show_mpls_ldp_discovery_json_cr():
    pass


@frr_show_mpls_ldp.group(cls=FRR_AbbreviationGroup, name='igp-sync', invoke_without_command=True)
def frr_show_mpls_ldp_igpsync(show_mpls_ldp_igpsync_='show_mpls_ldp_igp-sync'):
    """LDP-IGP Sync information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_igpsync.name
    
    if 'VIEW_NODE|show_mpls_ldp_igp-sync' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_igp-sync'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_igp-sync']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_igp-sync'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_igp-sync table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_igp-sync'
    pass


@frr_show_mpls_ldp_igpsync.command('./	<cr>')
def frr_show_mpls_ldp_igpsync_cr():
    pass


@frr_show_mpls_ldp_igpsync.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_igpsync_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_igpsync_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_igp-sync' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_igp-sync'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_igp-sync']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_igp-sync'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_igp-sync table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_igp-sync'
    pass


@frr_show_mpls_ldp_igpsync_json.command('./	<cr>')
def frr_show_mpls_ldp_igpsync_json_cr():
    pass


@frr_show_mpls_ldp.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_mpls_ldp_interface(show_mpls_ldp_interface_='show_mpls_ldp_interface'):
    """interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_interface.name
    
    if 'VIEW_NODE|show_mpls_ldp_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_interface'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_interface'
    pass


@frr_show_mpls_ldp_interface.command('./	<cr>')
def frr_show_mpls_ldp_interface_cr():
    pass


@frr_show_mpls_ldp_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_interface'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_interface'
    pass


@frr_show_mpls_ldp_interface_json.command('./	<cr>')
def frr_show_mpls_ldp_interface_json_cr():
    pass


@frr_show_mpls_ldp.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['ipv4', 'ipv6']),)
def frr_show_mpls_ldp_ldpredistributeip():
    """3"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip.name
    data_gen['LDP_REDISTRIBUTE_IP'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip.group(cls=FRR_AbbreviationGroup, name='binding', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding(binding_='binding'):
    """Label Information Base (LIB) information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding.name
    data_gen['binding'] = binding_='binding'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_detail(binding_detail_='binding_detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_detail.name
    data_gen['binding_detail'] = binding_detail_='binding_detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_detail_json(binding_detail_json_='binding_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_detail_json.name
    data_gen['binding_detail_json'] = binding_detail_json_='binding_detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix():
    """Destination prefix (IPv4)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='local-label', invoke_without_command=True)
@click.argument('locally_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel(locally_assigned_label_value, locallabel_='local-label'):
    """Match locally assigned label values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel.name
    data_gen['local-label'] = locallabel_='local-label'
    data_gen['LOCALLY_ASSIGNED_LABEL_VALUE'] = locally_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_locallabel_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='longer-prefixes', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes(longerprefixes_='longer-prefixes'):
    """Include longer matches"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes.name
    data_gen['longer-prefixes'] = longerprefixes_='longer-prefixes'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_detail(longerprefixes_detail_='longer-prefixes_detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_detail.name
    data_gen['longer-prefixes_detail'] = longerprefixes_detail_='longer-prefixes_detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_detail_json(longerprefixes_detail_json_='longer-prefixes_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_detail_json.name
    data_gen['longer-prefixes_detail_json'] = longerprefixes_detail_json_='longer-prefixes_detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_json(longerprefixes_json_='longer-prefixes_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_json.name
    data_gen['longer-prefixes_json'] = longerprefixes_json_='longer-prefixes_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name='local-label', invoke_without_command=True)
@click.argument('locally_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel(locally_assigned_label_value, longerprefixes_locallabel_='longer-prefixes_local-label'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel.name
    data_gen['longer-prefixes_local-label'] = longerprefixes_locallabel_='longer-prefixes_local-label'
    data_gen['LOCALLY_ASSIGNED_LABEL_VALUE'] = locally_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_locallabel_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_lsrid', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor(neighbor_lsrid, longerprefixes_neighbor_='longer-prefixes_neighbor'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor.name
    data_gen['longer-prefixes_neighbor'] = longerprefixes_neighbor_='longer-prefixes_neighbor'
    data_gen['NEIGHBOR_LSR-ID'] = neighbor_lsrid
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_neighbor_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes.group(cls=FRR_AbbreviationGroup, name='remote-label', invoke_without_command=True)
@click.argument('remotely_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel(remotely_assigned_label_value, longerprefixes_remotelabel_='longer-prefixes_remote-label'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel.name
    data_gen['longer-prefixes_remote-label'] = longerprefixes_remotelabel_='longer-prefixes_remote-label'
    data_gen['REMOTELY_ASSIGNED_LABEL_VALUE'] = remotely_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_longerprefixes_remotelabel_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_lsrid', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor(neighbor_lsrid, neighbor_='neighbor'):
    """Display labels from LDP neighbor"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    data_gen['NEIGHBOR_LSR-ID'] = neighbor_lsrid
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_neighbor_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix.group(cls=FRR_AbbreviationGroup, name='remote-label', invoke_without_command=True)
@click.argument('remotely_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel(remotely_assigned_label_value, remotelabel_='remote-label'):
    """Match remotely assigned label values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel.name
    data_gen['remote-label'] = remotelabel_='remote-label'
    data_gen['REMOTELY_ASSIGNED_LABEL_VALUE'] = remotely_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_ipprefix_remotelabel_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding.group(cls=FRR_AbbreviationGroup, name='local-label', invoke_without_command=True)
@click.argument('locally_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_ldpredistributeip_binding_locallabel(locally_assigned_label_value, locallabel_='local-label'):
    """Match locally assigned label values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_locallabel.name
    data_gen['local-label'] = locallabel_='local-label'
    data_gen['LOCALLY_ASSIGNED_LABEL_VALUE'] = locally_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_locallabel.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_locallabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_locallabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_locallabel_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_lsrid', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_mpls_ldp_ldpredistributeip_binding_neighbor(neighbor_lsrid, neighbor_='neighbor'):
    """Display labels from LDP neighbor"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    data_gen['NEIGHBOR_LSR-ID'] = neighbor_lsrid
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_neighbor.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_neighbor_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding.group(cls=FRR_AbbreviationGroup, name='remote-label', invoke_without_command=True)
@click.argument('remotely_assigned_label_value', metavar='(0-1048575)', required=True, type=FRR_TYPE((0, 1048575)))
def frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel(remotely_assigned_label_value, remotelabel_='remote-label'):
    """Match remotely assigned label values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel.name
    data_gen['remote-label'] = remotelabel_='remote-label'
    data_gen['REMOTELY_ASSIGNED_LABEL_VALUE'] = remotely_assigned_label_value
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_binding_remotelabel_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip.group(cls=FRR_AbbreviationGroup, name='discovery', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_discovery(discovery_='discovery'):
    """Discovery Hello Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_discovery.name
    data_gen['discovery'] = discovery_='discovery'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_discovery.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_discovery_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_discovery.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_discovery_detail(discovery_detail_='discovery_detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_discovery_detail.name
    data_gen['discovery_detail'] = discovery_detail_='discovery_detail'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_discovery_detail.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_discovery_detail_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_discovery_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_discovery_detail_json(discovery_detail_json_='discovery_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_discovery_detail_json.name
    data_gen['discovery_detail_json'] = discovery_detail_json_='discovery_detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_discovery_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_discovery_detail_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_discovery.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_discovery_json(discovery_json_='discovery_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_discovery_json.name
    data_gen['discovery_json'] = discovery_json_='discovery_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_discovery_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_discovery_json_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_interface(interface_='interface'):
    """interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_interface.name
    data_gen['interface'] = interface_='interface'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_interface.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_interface_cr():
    pass


@frr_show_mpls_ldp_ldpredistributeip_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_ldpredistributeip_interface_json(interface_json_='interface_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_ldpredistributeip_interface_json.name
    data_gen['interface_json'] = interface_json_='interface_json'
    
    if 'VIEW_NODE|show_mpls_ldp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp'
    pass


@frr_show_mpls_ldp_ldpredistributeip_interface_json.command('./	<cr>')
def frr_show_mpls_ldp_ldpredistributeip_interface_json_cr():
    pass


@frr_show_mpls_ldp.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor(show_mpls_ldp_neighbor_='show_mpls_ldp_neighbor'):
    """Neighbor information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor.name
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor'
    pass


@frr_show_mpls_ldp_neighbor.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_cr():
    pass


@frr_show_mpls_ldp_neighbor.group(cls=FRR_AbbreviationGroup, name='capabilities', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_capabilities(show_mpls_ldp_neighbor_capabilities_='show_mpls_ldp_neighbor_capabilities'):
    """Display neighbor capability information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_capabilities.name
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor_capabilities' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_capabilities'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_capabilities']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_capabilities'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor_capabilities table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor_capabilities'
    pass


@frr_show_mpls_ldp_neighbor_capabilities.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_capabilities_cr():
    pass


@frr_show_mpls_ldp_neighbor_capabilities.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_capabilities_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_capabilities_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor_capabilities' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_capabilities'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_capabilities']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_capabilities'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor_capabilities table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor_capabilities'
    pass


@frr_show_mpls_ldp_neighbor_capabilities_json.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_capabilities_json_cr():
    pass


@frr_show_mpls_ldp_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_detail(show_mpls_ldp_neighbor_detail_='show_mpls_ldp_neighbor_detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_detail.name
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_detail'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor_detail'
    pass


@frr_show_mpls_ldp_neighbor_detail.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_detail_cr():
    pass


@frr_show_mpls_ldp_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor_detail'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor_detail'
    pass


@frr_show_mpls_ldp_neighbor_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_detail_json_cr():
    pass


@frr_show_mpls_ldp_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor'
    pass


@frr_show_mpls_ldp_neighbor_json.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_json_cr():
    pass


@frr_show_mpls_ldp_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D']), invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_neighborlsrid():
    """Neighbor LSR-ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_neighborlsrid.name
    data_gen['NEIGHBOR_LSR-ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor'
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_neighborlsrid_cr():
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid.group(cls=FRR_AbbreviationGroup, name='capabilities', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_neighborlsrid_capabilities(capabilities_='capabilities'):
    """Display neighbor capability information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_neighborlsrid_capabilities.name
    data_gen['capabilities'] = capabilities_='capabilities'
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor'
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid_capabilities.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_neighborlsrid_capabilities_cr():
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid_capabilities.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_neighborlsrid_capabilities_json(capabilities_json_='capabilities_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_neighborlsrid_capabilities_json.name
    data_gen['capabilities_json'] = capabilities_json_='capabilities_json'
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor'
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid_capabilities_json.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_neighborlsrid_capabilities_json_cr():
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_neighborlsrid_detail(detail_='detail'):
    """Show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_neighborlsrid_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor'
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid_detail.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_neighborlsrid_detail_cr():
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_neighborlsrid_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_neighborlsrid_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor'
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid_detail_json.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_neighborlsrid_detail_json_cr():
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_ldp_neighbor_neighborlsrid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_ldp_neighbor_neighborlsrid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_ldp_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_ldp_neighbor'][key] = val
    
    # set VIEW_NODE -> show_mpls_ldp_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_ldp_neighbor'
    pass


@frr_show_mpls_ldp_neighbor_neighborlsrid_json.command('./	<cr>')
def frr_show_mpls_ldp_neighbor_neighborlsrid_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='pseudowires', invoke_without_command=True)
def frr_show_mpls_pseudowires():
    """Pseudowires"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_pseudowires.name
    
    if 'VIEW_NODE|show_mpls_pseudowires' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_pseudowires'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_pseudowires']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_pseudowires'][key] = val
    
    # set VIEW_NODE -> show_mpls_pseudowires table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_pseudowires'
    pass


@frr_show_mpls_pseudowires.command('./	<cr>')
def frr_show_mpls_pseudowires_cr():
    pass


@frr_show_mpls_pseudowires.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_mpls_pseudowires_detail(show_mpls_pseudowires_detail_='show_mpls_pseudowires_detail'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_pseudowires_detail.name
    
    if 'VIEW_NODE|show_mpls_pseudowires_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_pseudowires_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_pseudowires_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_pseudowires_detail'][key] = val
    
    # set VIEW_NODE -> show_mpls_pseudowires_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_pseudowires_detail'
    pass


@frr_show_mpls_pseudowires_detail.command('./	<cr>')
def frr_show_mpls_pseudowires_detail_cr():
    pass


@frr_show_mpls_pseudowires_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_pseudowires_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_pseudowires_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_pseudowires_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_pseudowires_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_pseudowires_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_pseudowires_detail'][key] = val
    
    # set VIEW_NODE -> show_mpls_pseudowires_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_pseudowires_detail'
    pass


@frr_show_mpls_pseudowires_detail_json.command('./	<cr>')
def frr_show_mpls_pseudowires_detail_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='status', invoke_without_command=True)
def frr_show_mpls_status(status_='status'):
    """MPLS status"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_status.name
    data_gen['status'] = status_='status'
    
    if 'VIEW_NODE|show_mpls' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls'][key] = val
    
    # set VIEW_NODE -> show_mpls table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls'
    pass


@frr_show_mpls_status.command('./	<cr>')
def frr_show_mpls_status_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='table', invoke_without_command=True)
def frr_show_mpls_table(show_mpls_table_='show_mpls_table'):
    """MPLS table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_table.name
    
    if 'VIEW_NODE|show_mpls_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_table'][key] = val
    
    # set VIEW_NODE -> show_mpls_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_table'
    pass


@frr_show_mpls_table.command('./	<cr>')
def frr_show_mpls_table_cr():
    pass


@frr_show_mpls_table.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_table_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_table_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_table'][key] = val
    
    # set VIEW_NODE -> show_mpls_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_table'
    pass


@frr_show_mpls_table_json.command('./	<cr>')
def frr_show_mpls_table_json_cr():
    pass


@frr_show_mpls_table.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, [(16, 1048575)]), invoke_without_command=True)
def frr_show_mpls_table_lsptodisplayinformation():
    """LSP to display information about"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_table_lsptodisplayinformation.name
    data_gen['LSP_TO_DISPLAY_INFORMATION'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_mpls_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_table'][key] = val
    
    # set VIEW_NODE -> show_mpls_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_table'
    pass


@frr_show_mpls_table_lsptodisplayinformation.command('./	<cr>')
def frr_show_mpls_table_lsptodisplayinformation_cr():
    pass


@frr_show_mpls_table_lsptodisplayinformation.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_mpls_table_lsptodisplayinformation_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_mpls_table_lsptodisplayinformation_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_mpls_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_mpls_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_mpls_table'][key] = val
    
    # set VIEW_NODE -> show_mpls_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_mpls_table'
    pass


@frr_show_mpls_table_lsptodisplayinformation_json.command('./	<cr>')
def frr_show_mpls_table_lsptodisplayinformation_json_cr():
    pass

