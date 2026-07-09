import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='database', invoke_without_command=True)
def frr_show_isis_database(show_isis_database_='show_isis_database'):
    """Link state database"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_database.name
    
    if 'VIEW_NODE|show_isis_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database'][key] = val
    
    # set VIEW_NODE -> show_isis_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_database'
    pass


@frr_show_isis_database.command('./	<cr>')
def frr_show_isis_database_cr():
    pass


@frr_show_isis_database.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_database_detail(show_isis_database_detail_='show_isis_database_detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_database_detail.name
    
    if 'VIEW_NODE|show_isis_database_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail'][key] = val
    
    # set VIEW_NODE -> show_isis_database_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_database_detail'
    pass


@frr_show_isis_database_detail.command('./	<cr>')
def frr_show_isis_database_detail_cr():
    pass


@frr_show_isis_database_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_database_detail_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_database_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_database_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail'][key] = val
    
    # set VIEW_NODE -> show_isis_database_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_database_detail'
    pass


@frr_show_isis_database_detail_json.command('./	<cr>')
def frr_show_isis_database_detail_json_cr():
    pass


@frr_show_isis_database_detail.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD']), invoke_without_command=True)
def frr_show_isis_database_detail_lspid():
    """LSP ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_database_detail_lspid.name
    data_gen['LSP_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_database_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail'][key] = val
    
    # set VIEW_NODE -> show_isis_database_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_database_detail'
    pass


@frr_show_isis_database_detail_lspid.command('./	<cr>')
def frr_show_isis_database_detail_lspid_cr():
    pass


@frr_show_isis_database_detail_lspid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_database_detail_lspid_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_database_detail_lspid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_database_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database_detail'][key] = val
    
    # set VIEW_NODE -> show_isis_database_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_database_detail'
    pass


@frr_show_isis_database_detail_lspid_json.command('./	<cr>')
def frr_show_isis_database_detail_lspid_json_cr():
    pass


@frr_show_isis_database.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_database_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_database_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database'][key] = val
    
    # set VIEW_NODE -> show_isis_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_database'
    pass


@frr_show_isis_database_json.command('./	<cr>')
def frr_show_isis_database_json_cr():
    pass


@frr_show_isis_database.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['WORD']), invoke_without_command=True)
def frr_show_isis_database_lspid():
    """LSP ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_database_lspid.name
    data_gen['LSP_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database'][key] = val
    
    # set VIEW_NODE -> show_isis_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_database'
    pass


@frr_show_isis_database_lspid.command('./	<cr>')
def frr_show_isis_database_lspid_cr():
    pass


@frr_show_isis_database_lspid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_database_lspid_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_database_lspid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_database'][key] = val
    
    # set VIEW_NODE -> show_isis_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_database'
    pass


@frr_show_isis_database_lspid_json.command('./	<cr>')
def frr_show_isis_database_lspid_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='fast-reroute', invoke_without_command=True)
def frr_show_isis_fastreroute():
    """IS-IS FRR information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_fastreroute.name
    
    if 'VIEW_NODE|show_isis_fast-reroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_fast-reroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_fast-reroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_fast-reroute'][key] = val
    
    # set VIEW_NODE -> show_isis_fast-reroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_fast-reroute'
    pass


@frr_show_isis_fastreroute.command('./	<cr>')
def frr_show_isis_fastreroute_cr():
    pass


@frr_show_isis_fastreroute.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_isis_fastreroute_summary(show_isis_fastreroute_summary_='show_isis_fast-reroute_summary'):
    """FRR summary"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_fastreroute_summary.name
    
    if 'VIEW_NODE|show_isis_fast-reroute_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_fast-reroute_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_fast-reroute_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_fast-reroute_summary'][key] = val
    
    # set VIEW_NODE -> show_isis_fast-reroute_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_fast-reroute_summary'
    pass


@frr_show_isis_fastreroute_summary.command('./	<cr>')
def frr_show_isis_fastreroute_summary_cr():
    pass


@frr_show_isis_fastreroute_summary.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['level-1', 'level-2']), invoke_without_command=True)
def frr_show_isis_fastreroute_summary_isislevel():
    """level-1 routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_fastreroute_summary_isislevel.name
    data_gen['ISIS_LEVEL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_fast-reroute_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_fast-reroute_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_fast-reroute_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_fast-reroute_summary'][key] = val
    
    # set VIEW_NODE -> show_isis_fast-reroute_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_fast-reroute_summary'
    pass


@frr_show_isis_fastreroute_summary_isislevel.command('./	<cr>')
def frr_show_isis_fastreroute_summary_isislevel_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='hostname', invoke_without_command=True)
def frr_show_isis_hostname(hostname_='hostname'):
    """IS-IS Dynamic hostname mapping"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_hostname.name
    data_gen['hostname'] = hostname_='hostname'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_hostname.command('./	<cr>')
def frr_show_isis_hostname_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_isis_interface(show_isis_interface_='show_isis_interface'):
    """IS-IS interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_interface.name
    
    if 'VIEW_NODE|show_isis_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface'][key] = val
    
    # set VIEW_NODE -> show_isis_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_interface'
    pass


@frr_show_isis_interface.command('./	<cr>')
def frr_show_isis_interface_cr():
    pass


@frr_show_isis_interface.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_interface_detail(show_isis_interface_detail_='show_isis_interface_detail'):
    """show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_interface_detail.name
    
    if 'VIEW_NODE|show_isis_interface_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_interface_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface_detail'][key] = val
    
    # set VIEW_NODE -> show_isis_interface_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_interface_detail'
    pass


@frr_show_isis_interface_detail.command('./	<cr>')
def frr_show_isis_interface_detail_cr():
    pass


@frr_show_isis_interface_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_interface_detail_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_interface_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_interface_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_interface_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface_detail'][key] = val
    
    # set VIEW_NODE -> show_isis_interface_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_interface_detail'
    pass


@frr_show_isis_interface_detail_json.command('./	<cr>')
def frr_show_isis_interface_detail_json_cr():
    pass


@frr_show_isis_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['WORD']), invoke_without_command=True)
def frr_show_isis_interface_isisinterfacename():
    """IS-IS interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_interface_isisinterfacename.name
    data_gen['IS-IS_INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface'][key] = val
    
    # set VIEW_NODE -> show_isis_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_interface'
    pass


@frr_show_isis_interface_isisinterfacename.command('./	<cr>')
def frr_show_isis_interface_isisinterfacename_cr():
    pass


@frr_show_isis_interface_isisinterfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_interface_isisinterfacename_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_interface_isisinterfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface'][key] = val
    
    # set VIEW_NODE -> show_isis_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_interface'
    pass


@frr_show_isis_interface_isisinterfacename_json.command('./	<cr>')
def frr_show_isis_interface_isisinterfacename_json_cr():
    pass


@frr_show_isis_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_interface_json(json_='json'):
    """IS-IS interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_interface'][key] = val
    
    # set VIEW_NODE -> show_isis_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_interface'
    pass


@frr_show_isis_interface_json.command('./	<cr>')
def frr_show_isis_interface_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='mpls', invoke_without_command=True)
def frr_show_isis_mpls():
    """MPLS information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mpls.name
    
    if 'VIEW_NODE|show_isis_mpls' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls'
    pass


@frr_show_isis_mpls.command('./	<cr>')
def frr_show_isis_mpls_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='mpls-te',)
def frr_show_isis_mplste(show_isis_mplste_='show_isis_mpls-te'):
    """MPLS-TE specific commands"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste.name
    
    if 'VIEW_NODE|show_isis_mpls-te' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te'
    pass


@frr_show_isis_mplste.group(cls=FRR_AbbreviationGroup, name='database', invoke_without_command=True)
def frr_show_isis_mplste_database(show_isis_mplste_database_='show_isis_mpls-te_database'):
    """MPLS-TE database"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database.name
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database.command('./	<cr>')
def frr_show_isis_mplste_database_cr():
    pass


@frr_show_isis_mplste_database.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_mplste_database_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database_detail.command('./	<cr>')
def frr_show_isis_mplste_database_detail_cr():
    pass


@frr_show_isis_mplste_database.group(cls=FRR_AbbreviationGroup, name='edge',)
def frr_show_isis_mplste_database_edge(edge_='edge'):
    """MPLS-TE Edge"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_edge.name
    data_gen['edge'] = edge_='edge'
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database_edge.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_isis_mplste_database_edge_edgeipaddress():
    """MPLS-TE Edge ID (as an IPv4 address)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_edge_edgeipaddress.name
    data_gen['EDGE_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database_edge_edgeipaddress.command('./	<cr>')
def frr_show_isis_mplste_database_edge_edgeipaddress_cr():
    pass


@frr_show_isis_mplste_database_edge_edgeipaddress.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_mplste_database_edge_edgeipaddress_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_edge_edgeipaddress_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database_edge_edgeipaddress_detail.command('./	<cr>')
def frr_show_isis_mplste_database_edge_edgeipaddress_detail_cr():
    pass


@frr_show_isis_mplste_database_edge_edgeipaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_mplste_database_edge_edgeipaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_edge_edgeipaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database_edge_edgeipaddress_json.command('./	<cr>')
def frr_show_isis_mplste_database_edge_edgeipaddress_json_cr():
    pass


@frr_show_isis_mplste_database.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_mplste_database_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database_json.command('./	<cr>')
def frr_show_isis_mplste_database_json_cr():
    pass


@frr_show_isis_mplste_database.group(cls=FRR_AbbreviationGroup, name='subnet',)
def frr_show_isis_mplste_database_subnet(subnet_='subnet'):
    """MPLS-TE Subnet"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_subnet.name
    data_gen['subnet'] = subnet_='subnet'
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database_subnet.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_isis_mplste_database_subnet_subnetipprefix():
    """MPLS-TE Subnet ID (as an IPv4 prefix)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_subnet_subnetipprefix.name
    data_gen['SUBNET_IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database_subnet_subnetipprefix.command('./	<cr>')
def frr_show_isis_mplste_database_subnet_subnetipprefix_cr():
    pass


@frr_show_isis_mplste_database_subnet_subnetipprefix.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_mplste_database_subnet_subnetipprefix_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_subnet_subnetipprefix_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database_subnet_subnetipprefix_detail.command('./	<cr>')
def frr_show_isis_mplste_database_subnet_subnetipprefix_detail_cr():
    pass


@frr_show_isis_mplste_database_subnet_subnetipprefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_mplste_database_subnet_subnetipprefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_subnet_subnetipprefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_mpls-te_database' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database'
    pass


@frr_show_isis_mplste_database_subnet_subnetipprefix_json.command('./	<cr>')
def frr_show_isis_mplste_database_subnet_subnetipprefix_json_cr():
    pass


@frr_show_isis_mplste_database.group(cls=FRR_AbbreviationGroup, name='vertex', invoke_without_command=True)
def frr_show_isis_mplste_database_vertex(show_isis_mplste_database_vertex_='show_isis_mpls-te_database_vertex'):
    """MPLS-TE Vertex"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_vertex.name
    
    if 'VIEW_NODE|show_isis_mpls-te_database_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database_vertex'
    pass


@frr_show_isis_mplste_database_vertex.command('./	<cr>')
def frr_show_isis_mplste_database_vertex_cr():
    pass


@frr_show_isis_mplste_database_vertex.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_mplste_database_vertex_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_vertex_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_isis_mpls-te_database_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database_vertex'
    pass


@frr_show_isis_mplste_database_vertex_detail.command('./	<cr>')
def frr_show_isis_mplste_database_vertex_detail_cr():
    pass


@frr_show_isis_mplste_database_vertex.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_mplste_database_vertex_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_vertex_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_mpls-te_database_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database_vertex'
    pass


@frr_show_isis_mplste_database_vertex_json.command('./	<cr>')
def frr_show_isis_mplste_database_vertex_json_cr():
    pass


@frr_show_isis_mplste_database_vertex.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_show_isis_mplste_database_vertex_mplstevertexid():
    """MPLS-TE Vertex ID (as an ISO ID, hostname or self)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_vertex_mplstevertexid.name
    data_gen['MPLS-TE_VERTEX_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_mpls-te_database_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database_vertex'
    pass


@frr_show_isis_mplste_database_vertex_mplstevertexid.command('./	<cr>')
def frr_show_isis_mplste_database_vertex_mplstevertexid_cr():
    pass


@frr_show_isis_mplste_database_vertex_mplstevertexid.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_mplste_database_vertex_mplstevertexid_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_vertex_mplstevertexid_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_isis_mpls-te_database_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database_vertex'
    pass


@frr_show_isis_mplste_database_vertex_mplstevertexid_detail.command('./	<cr>')
def frr_show_isis_mplste_database_vertex_mplstevertexid_detail_cr():
    pass


@frr_show_isis_mplste_database_vertex_mplstevertexid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_mplste_database_vertex_mplstevertexid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_database_vertex_mplstevertexid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_mpls-te_database_vertex' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_database_vertex'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_database_vertex table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_database_vertex'
    pass


@frr_show_isis_mplste_database_vertex_mplstevertexid_json.command('./	<cr>')
def frr_show_isis_mplste_database_vertex_mplstevertexid_json_cr():
    pass


@frr_show_isis_mplste.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_isis_mplste_interface(show_isis_mplste_interface_='show_isis_mpls-te_interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_interface.name
    
    if 'VIEW_NODE|show_isis_mpls-te_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_interface'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_interface'
    pass


@frr_show_isis_mplste_interface.command('./	<cr>')
def frr_show_isis_mplste_interface_cr():
    pass


@frr_show_isis_mplste_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['INTERFACE']), invoke_without_command=True)
def frr_show_isis_mplste_interface_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_interface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_mpls-te_interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_interface']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te_interface'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te_interface table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te_interface'
    pass


@frr_show_isis_mplste_interface_interfacename.command('./	<cr>')
def frr_show_isis_mplste_interface_interfacename_cr():
    pass


@frr_show_isis_mplste.group(cls=FRR_AbbreviationGroup, name='router', invoke_without_command=True)
def frr_show_isis_mplste_router(router_='router'):
    """Router information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mplste_router.name
    data_gen['router'] = router_='router'
    
    if 'VIEW_NODE|show_isis_mpls-te' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls-te'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls-te table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls-te'
    pass


@frr_show_isis_mplste_router.command('./	<cr>')
def frr_show_isis_mplste_router_cr():
    pass


@frr_show_isis_mpls.group(cls=FRR_AbbreviationGroup, name='ldp-sync', invoke_without_command=True)
def frr_show_isis_mpls_ldpsync(show_isis_mpls_ldpsync_='show_isis_mpls_ldp-sync'):
    """LDP-IGP Sync information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mpls_ldpsync.name
    
    if 'VIEW_NODE|show_isis_mpls_ldp-sync' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls_ldp-sync'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls_ldp-sync']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls_ldp-sync'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls_ldp-sync table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls_ldp-sync'
    pass


@frr_show_isis_mpls_ldpsync.command('./	<cr>')
def frr_show_isis_mpls_ldpsync_cr():
    pass


@frr_show_isis_mpls_ldpsync.group(cls=FRR_AbbreviationGroup, name='interface',)
def frr_show_isis_mpls_ldpsync_interface(interface_='interface'):
    """Interface information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mpls_ldpsync_interface.name
    data_gen['interface'] = interface_='interface'
    
    if 'VIEW_NODE|show_isis_mpls_ldp-sync' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls_ldp-sync'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls_ldp-sync']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls_ldp-sync'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls_ldp-sync table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls_ldp-sync'
    pass


@frr_show_isis_mpls_ldpsync_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['INTERFACE', 'all']), invoke_without_command=True)
def frr_show_isis_mpls_ldpsync_interface_interfacechoicecase():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_mpls_ldpsync_interface_interfacechoicecase.name
    data_gen['INTERFACE_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_mpls_ldp-sync' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls_ldp-sync'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls_ldp-sync']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_mpls_ldp-sync'][key] = val
    
    # set VIEW_NODE -> show_isis_mpls_ldp-sync table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_mpls_ldp-sync'
    pass


@frr_show_isis_mpls_ldpsync_interface_interfacechoicecase.command('./	<cr>')
def frr_show_isis_mpls_ldpsync_interface_interfacechoicecase_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
def frr_show_isis_neighbor(show_isis_neighbor_='show_isis_neighbor'):
    """IS-IS neighbor adjacencies"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_neighbor.name
    
    if 'VIEW_NODE|show_isis_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor'][key] = val
    
    # set VIEW_NODE -> show_isis_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_neighbor'
    pass


@frr_show_isis_neighbor.command('./	<cr>')
def frr_show_isis_neighbor_cr():
    pass


@frr_show_isis_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_neighbor_detail(show_isis_neighbor_detail_='show_isis_neighbor_detail'):
    """show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_neighbor_detail.name
    
    if 'VIEW_NODE|show_isis_neighbor_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor_detail'][key] = val
    
    # set VIEW_NODE -> show_isis_neighbor_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_neighbor_detail'
    pass


@frr_show_isis_neighbor_detail.command('./	<cr>')
def frr_show_isis_neighbor_detail_cr():
    pass


@frr_show_isis_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_neighbor_detail_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_neighbor_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_neighbor_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor_detail'][key] = val
    
    # set VIEW_NODE -> show_isis_neighbor_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_neighbor_detail'
    pass


@frr_show_isis_neighbor_detail_json.command('./	<cr>')
def frr_show_isis_neighbor_detail_json_cr():
    pass


@frr_show_isis_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_neighbor_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor'][key] = val
    
    # set VIEW_NODE -> show_isis_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_neighbor'
    pass


@frr_show_isis_neighbor_json.command('./	<cr>')
def frr_show_isis_neighbor_json_cr():
    pass


@frr_show_isis_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['WORD']), invoke_without_command=True)
def frr_show_isis_neighbor_systemid():
    """System id"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_neighbor_systemid.name
    data_gen['SYSTEM_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor'][key] = val
    
    # set VIEW_NODE -> show_isis_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_neighbor'
    pass


@frr_show_isis_neighbor_systemid.command('./	<cr>')
def frr_show_isis_neighbor_systemid_cr():
    pass


@frr_show_isis_neighbor_systemid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_neighbor_systemid_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_neighbor_systemid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_neighbor'][key] = val
    
    # set VIEW_NODE -> show_isis_neighbor table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_neighbor'
    pass


@frr_show_isis_neighbor_systemid_json.command('./	<cr>')
def frr_show_isis_neighbor_systemid_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
def frr_show_isis_route(show_isis_route_='show_isis_route'):
    """IS-IS routing table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_route.name
    
    if 'VIEW_NODE|show_isis_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_route'][key] = val
    
    # set VIEW_NODE -> show_isis_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_route'
    pass


@frr_show_isis_route.command('./	<cr>')
def frr_show_isis_route_cr():
    pass


@frr_show_isis_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['prefix-sid', 'backup']), invoke_without_command=True)
def frr_show_isis_route_choicecase():
    """Show Prefix-SID information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_route_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_route'][key] = val
    
    # set VIEW_NODE -> show_isis_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_route'
    pass


@frr_show_isis_route_choicecase.command('./	<cr>')
def frr_show_isis_route_choicecase_cr():
    pass


@frr_show_isis_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['level-1', 'level-2']), invoke_without_command=True)
def frr_show_isis_route_isislevel():
    """level-1 routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_route_isislevel.name
    data_gen['ISIS_LEVEL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_route'][key] = val
    
    # set VIEW_NODE -> show_isis_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_route'
    pass


@frr_show_isis_route_isislevel.command('./	<cr>')
def frr_show_isis_route_isislevel_cr():
    pass


@frr_show_isis_route_isislevel.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['prefix-sid', 'backup']), invoke_without_command=True)
def frr_show_isis_route_isislevel_choicecase():
    """Show Prefix-SID information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_route_isislevel_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_route']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_route'][key] = val
    
    # set VIEW_NODE -> show_isis_route table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_route'
    pass


@frr_show_isis_route_isislevel_choicecase.command('./	<cr>')
def frr_show_isis_route_isislevel_choicecase_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='segment-routing',)
def frr_show_isis_segmentrouting(show_isis_segmentrouting_='show_isis_segment-routing'):
    """Segment-Routing"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_segmentrouting.name
    
    if 'VIEW_NODE|show_isis_segment-routing' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_segment-routing'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_segment-routing']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_segment-routing'][key] = val
    
    # set VIEW_NODE -> show_isis_segment-routing table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_segment-routing'
    pass


@frr_show_isis_segmentrouting.group(cls=FRR_AbbreviationGroup, name='node', invoke_without_command=True)
def frr_show_isis_segmentrouting_node(node_='node'):
    """Segment-Routing node"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_segmentrouting_node.name
    data_gen['node'] = node_='node'
    
    if 'VIEW_NODE|show_isis_segment-routing' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_segment-routing'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_segment-routing']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_segment-routing'][key] = val
    
    # set VIEW_NODE -> show_isis_segment-routing table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_segment-routing'
    pass


@frr_show_isis_segmentrouting_node.command('./	<cr>')
def frr_show_isis_segmentrouting_node_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='spf-delay-ietf', invoke_without_command=True)
def frr_show_isis_spfdelayietf(spfdelayietf_='spf-delay-ietf'):
    """SPF delay IETF information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_spfdelayietf.name
    data_gen['spf-delay-ietf'] = spfdelayietf_='spf-delay-ietf'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_spfdelayietf.command('./	<cr>')
def frr_show_isis_spfdelayietf_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_isis_summary(show_isis_summary_='show_isis_summary'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_summary.name
    
    if 'VIEW_NODE|show_isis_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_summary'][key] = val
    
    # set VIEW_NODE -> show_isis_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_summary'
    pass


@frr_show_isis_summary.command('./	<cr>')
def frr_show_isis_summary_cr():
    pass


@frr_show_isis_summary.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_summary_json(json_='json'):
    """summary"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_summary_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis_summary' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_summary'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_summary']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_summary'][key] = val
    
    # set VIEW_NODE -> show_isis_summary table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_summary'
    pass


@frr_show_isis_summary_json.command('./	<cr>')
def frr_show_isis_summary_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='topology', invoke_without_command=True)
def frr_show_isis_topology(show_isis_topology_='show_isis_topology'):
    """IS-IS paths to Intermediate Systems"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_topology.name
    
    if 'VIEW_NODE|show_isis_topology' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_topology'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_topology']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_topology'][key] = val
    
    # set VIEW_NODE -> show_isis_topology table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_topology'
    pass


@frr_show_isis_topology.command('./	<cr>')
def frr_show_isis_topology_cr():
    pass


@frr_show_isis_topology.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['level-1', 'level-2']), invoke_without_command=True)
def frr_show_isis_topology_isislevel():
    """Paths to all level-1 routers in the area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_topology_isislevel.name
    data_gen['ISIS_LEVEL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis_topology' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis_topology'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis_topology']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis_topology'][key] = val
    
    # set VIEW_NODE -> show_isis_topology table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis_topology'
    pass


@frr_show_isis_topology_isislevel.command('./	<cr>')
def frr_show_isis_topology_isislevel_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrf',)
def frr_show_isis_vrf(vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['NAME', 'all']),)
def frr_show_isis_vrf_vrfchoicecase():
    """3"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase.name
    data_gen['VRF_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='database', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_database(database_='database'):
    """Link state database"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_database.name
    data_gen['database'] = database_='database'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_database.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_database_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_database_detail(database_detail_='database_detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_database_detail.name
    data_gen['database_detail'] = database_detail_='database_detail'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_database_detail.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_database_detail_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_database_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_database_detail_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_database_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_database_detail_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_database_detail_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_database_detail.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['WORD']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_database_detail_lspid():
    """LSP ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_database_detail_lspid.name
    data_gen['LSP_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_database_detail_lspid.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_database_detail_lspid_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_database_detail_lspid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_database_detail_lspid_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_database_detail_lspid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_database_detail_lspid_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_database_detail_lspid_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_database_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_database_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_database_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_database_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_database.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_database_lspid():
    """LSP ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_database_lspid.name
    data_gen['LSP_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_database_lspid.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_database_lspid_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_database_lspid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_database_lspid_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_database_lspid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_database_lspid_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_database_lspid_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='fast-reroute', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_fastreroute():
    """IS-IS FRR information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_fastreroute.name
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_fastreroute.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_fastreroute_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_fastreroute.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_fastreroute_summary(fastreroute_summary_='fast-reroute_summary'):
    """FRR summary"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_fastreroute_summary.name
    data_gen['fast-reroute_summary'] = fastreroute_summary_='fast-reroute_summary'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_fastreroute_summary.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_fastreroute_summary_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_fastreroute_summary.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['level-1', 'level-2']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_fastreroute_summary_isislevel():
    """level-1 routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_fastreroute_summary_isislevel.name
    data_gen['ISIS_LEVEL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_fastreroute_summary_isislevel.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_fastreroute_summary_isislevel_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='hostname', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_hostname(hostname_='hostname'):
    """IS-IS Dynamic hostname mapping"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_hostname.name
    data_gen['hostname'] = hostname_='hostname'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_hostname.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_hostname_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_interface(interface_='interface'):
    """IS-IS interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_interface.name
    data_gen['interface'] = interface_='interface'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_interface.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_interface_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_interface.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_interface_detail(interface_detail_='interface_detail'):
    """show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_interface_detail.name
    data_gen['interface_detail'] = interface_detail_='interface_detail'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_interface_detail.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_interface_detail_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_interface_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_interface_detail_json(interface_detail_json_='interface_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_interface_detail_json.name
    data_gen['interface_detail_json'] = interface_detail_json_='interface_detail_json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_interface_detail_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_interface_detail_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_interface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_interface_isisinterfacename():
    """IS-IS interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_interface_isisinterfacename.name
    data_gen['IS-IS_INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_interface_isisinterfacename.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_interface_isisinterfacename_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_interface_isisinterfacename.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_interface_isisinterfacename_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_interface_isisinterfacename_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_interface_isisinterfacename_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_interface_isisinterfacename_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)

def frr_show_isis_vrf_vrfchoicecase_interface_json(json_='json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_interface_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_interface_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='mpls-te', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste():
    """Router information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste.name
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste.group(cls=FRR_AbbreviationGroup, name='database', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database(mplste_database_='mpls-te_database'):
    """MPLS-TE database"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database.name
    data_gen['mpls-te_database'] = mplste_database_='mpls-te_database'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_detail(mplste_database_detail_='mpls-te_database_detail'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_detail.name
    data_gen['mpls-te_database_detail'] = mplste_database_detail_='mpls-te_database_detail'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_detail.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_detail_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database.group(cls=FRR_AbbreviationGroup, name='edge',)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_edge(mplste_database_edge_='mpls-te_database_edge'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_edge.name
    data_gen['mpls-te_database_edge'] = mplste_database_edge_='mpls-te_database_edge'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_edge.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress():
    """MPLS-TE Edge ID (as an IPv4 address)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress.name
    data_gen['EDGE_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress_detail.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress_detail_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_edge_edgeipaddress_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_json(mplste_database_json_='mpls-te_database_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_json.name
    data_gen['mpls-te_database_json'] = mplste_database_json_='mpls-te_database_json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database.group(cls=FRR_AbbreviationGroup, name='subnet',)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet(mplste_database_subnet_='mpls-te_database_subnet'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet.name
    data_gen['mpls-te_database_subnet'] = mplste_database_subnet_='mpls-te_database_subnet'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix():
    """MPLS-TE Subnet ID (as an IPv4 prefix)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix.name
    data_gen['SUBNET_IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix_detail.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix_detail_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_subnet_subnetipprefix_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database.group(cls=FRR_AbbreviationGroup, name='vertex', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex(mplste_database_vertex_='mpls-te_database_vertex'):
    """MPLS-TE Vertex"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex.name
    data_gen['mpls-te_database_vertex'] = mplste_database_vertex_='mpls-te_database_vertex'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_detail.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_detail_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['WORD']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid():
    """MPLS-TE Vertex ID (as an ISO ID, hostname or self)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid.name
    data_gen['MPLS-TE_VERTEX_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid_detail.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid_detail_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_database_vertex_mplstevertexid_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste.group(cls=FRR_AbbreviationGroup, name='router', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_mplste_router(mplste_router_='mpls-te_router'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_mplste_router.name
    data_gen['mpls-te_router'] = mplste_router_='mpls-te_router'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_mplste_router.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_mplste_router_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_neighbor(neighbor_='neighbor'):
    """IS-IS neighbor adjacencies"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_neighbor_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_neighbor_detail(neighbor_detail_='neighbor_detail'):
    """show detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_neighbor_detail.name
    data_gen['neighbor_detail'] = neighbor_detail_='neighbor_detail'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor_detail.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_neighbor_detail_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_neighbor_detail_json(neighbor_detail_json_='neighbor_detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_neighbor_detail_json.name
    data_gen['neighbor_detail_json'] = neighbor_detail_json_='neighbor_detail_json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor_detail_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_neighbor_detail_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)

def frr_show_isis_vrf_vrfchoicecase_neighbor_json(json_='json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_neighbor_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_neighbor_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_neighbor_systemid():
    """System id"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_neighbor_systemid.name
    data_gen['SYSTEM_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor_systemid.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_neighbor_systemid_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor_systemid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_neighbor_systemid_json(json_='json'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_neighbor_systemid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_neighbor_systemid_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_neighbor_systemid_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_route(route_='route'):
    """IS-IS routing table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_route.name
    data_gen['route'] = route_='route'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_route.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_route_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['prefix-sid', 'backup']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_route_choicecase():
    """Show Prefix-SID information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_route_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_route_choicecase.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_route_choicecase_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_route.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['level-1', 'level-2']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_route_isislevel():
    """level-1 routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_route_isislevel.name
    data_gen['ISIS_LEVEL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_route_isislevel.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_route_isislevel_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_route_isislevel.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['prefix-sid', 'backup']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_route_isislevel_choicecase():
    """Show Prefix-SID information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_route_isislevel_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_route_isislevel_choicecase.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_route_isislevel_choicecase_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='spf-delay-ietf', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_spfdelayietf(spfdelayietf_='spf-delay-ietf'):
    """SPF delay IETF information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_spfdelayietf.name
    data_gen['spf-delay-ietf'] = spfdelayietf_='spf-delay-ietf'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_spfdelayietf.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_spfdelayietf_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_summary(summary_='summary'):
    """json output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_summary.name
    data_gen['summary'] = summary_='summary'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_summary.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_summary_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_summary.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_summary_json(summary_json_='summary_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_summary_json.name
    data_gen['summary_json'] = summary_json_='summary_json'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_summary_json.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_summary_json_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase.group(cls=FRR_AbbreviationGroup, name='topology', invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_topology(topology_='topology'):
    """IS-IS paths to Intermediate Systems"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_topology.name
    data_gen['topology'] = topology_='topology'
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_topology.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_topology_cr():
    pass


@frr_show_isis_vrf_vrfchoicecase_topology.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['level-1', 'level-2']), invoke_without_command=True)
def frr_show_isis_vrf_vrfchoicecase_topology_isislevel():
    """Paths to all level-1 routers in the area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_isis_vrf_vrfchoicecase_topology_isislevel.name
    data_gen['ISIS_LEVEL'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_isis' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_isis'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_isis']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_isis'][key] = val
    
    # set VIEW_NODE -> show_isis table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_isis'
    pass


@frr_show_isis_vrf_vrfchoicecase_topology_isislevel.command('./	<cr>')
def frr_show_isis_vrf_vrfchoicecase_topology_isislevel_cr():
    pass

