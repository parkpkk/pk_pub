import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='as-number', invoke_without_command=True)
@click.argument('as_number', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_rpki_asnumber(as_number, asnumber_='as-number'):
    """Lookup by ASN in prefix table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_asnumber.name
    data_gen['as-number'] = asnumber_='as-number'
    data_gen['AS_NUMBER'] = as_number
    
    if 'VIEW_NODE|show_rpki' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'][key] = val
    
    # set VIEW_NODE -> show_rpki table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki'
    pass


@frr_show_rpki_asnumber.command('./	<cr>')
def frr_show_rpki_asnumber_cr():
    pass


@frr_show_rpki_asnumber.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_rpki_asnumber_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_asnumber_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_rpki' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'][key] = val
    
    # set VIEW_NODE -> show_rpki table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki'
    pass


@frr_show_rpki_asnumber_json.command('./	<cr>')
def frr_show_rpki_asnumber_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='cache-connection', invoke_without_command=True)
def frr_show_rpki_cacheconnection(show_rpki_cacheconnection_='show_rpki_cache-connection'):
    """Show to which RPKI Cache Servers we have a connection"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_cacheconnection.name
    
    if 'VIEW_NODE|show_rpki_cache-connection' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-connection'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-connection']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-connection'][key] = val
    
    # set VIEW_NODE -> show_rpki_cache-connection table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki_cache-connection'
    pass


@frr_show_rpki_cacheconnection.command('./	<cr>')
def frr_show_rpki_cacheconnection_cr():
    pass


@frr_show_rpki_cacheconnection.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_rpki_cacheconnection_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_cacheconnection_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_rpki_cache-connection' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-connection'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-connection']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-connection'][key] = val
    
    # set VIEW_NODE -> show_rpki_cache-connection table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki_cache-connection'
    pass


@frr_show_rpki_cacheconnection_json.command('./	<cr>')
def frr_show_rpki_cacheconnection_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='cache-server', invoke_without_command=True)
def frr_show_rpki_cacheserver(show_rpki_cacheserver_='show_rpki_cache-server'):
    """Show configured cache server"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_cacheserver.name
    
    if 'VIEW_NODE|show_rpki_cache-server' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-server'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-server']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-server'][key] = val
    
    # set VIEW_NODE -> show_rpki_cache-server table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki_cache-server'
    pass


@frr_show_rpki_cacheserver.command('./	<cr>')
def frr_show_rpki_cacheserver_cr():
    pass


@frr_show_rpki_cacheserver.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_rpki_cacheserver_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_cacheserver_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_rpki_cache-server' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-server'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-server']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_cache-server'][key] = val
    
    # set VIEW_NODE -> show_rpki_cache-server table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki_cache-server'
    pass


@frr_show_rpki_cacheserver_json.command('./	<cr>')
def frr_show_rpki_cacheserver_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='prefix',)
def frr_show_rpki_prefix(prefix_='prefix'):
    """Lookup IP prefix and optionally ASN in prefix table"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    
    if 'VIEW_NODE|show_rpki' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'][key] = val
    
    # set VIEW_NODE -> show_rpki table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki'
    pass


@click.group(cls=FRR_AbbreviationGroup, name='prefix-table', invoke_without_command=True)
def frr_show_rpki_prefixtable(show_rpki_prefixtable_='show_rpki_prefix-table'):
    """Show validated prefixes which were received from RPKI Cache"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_prefixtable.name
    
    if 'VIEW_NODE|show_rpki_prefix-table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_prefix-table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki_prefix-table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_prefix-table'][key] = val
    
    # set VIEW_NODE -> show_rpki_prefix-table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki_prefix-table'
    pass


@frr_show_rpki_prefixtable.command('./	<cr>')
def frr_show_rpki_prefixtable_cr():
    pass


@frr_show_rpki_prefixtable.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_rpki_prefixtable_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_prefixtable_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_rpki_prefix-table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_prefix-table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki_prefix-table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki_prefix-table'][key] = val
    
    # set VIEW_NODE -> show_rpki_prefix-table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki_prefix-table'
    pass


@frr_show_rpki_prefixtable_json.command('./	<cr>')
def frr_show_rpki_prefixtable_json_cr():
    pass


@frr_show_rpki_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D/M', 'X:X::X:X/M']), invoke_without_command=True)
def frr_show_rpki_prefix_prefixipprefix():
    """IPv4 prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_prefix_prefixipprefix.name
    data_gen['PREFIX_IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_rpki' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'][key] = val
    
    # set VIEW_NODE -> show_rpki table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki'
    pass


@frr_show_rpki_prefix_prefixipprefix.command('./	<cr>')
def frr_show_rpki_prefix_prefixipprefix_cr():
    pass


@frr_show_rpki_prefix_prefixipprefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, [(1, 4294967295)]), invoke_without_command=True)
def frr_show_rpki_prefix_prefixipprefix_asnumber():
    """AS Number"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_prefix_prefixipprefix_asnumber.name
    data_gen['AS_NUMBER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_rpki' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'][key] = val
    
    # set VIEW_NODE -> show_rpki table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki'
    pass


@frr_show_rpki_prefix_prefixipprefix_asnumber.command('./	<cr>')
def frr_show_rpki_prefix_prefixipprefix_asnumber_cr():
    pass


@frr_show_rpki_prefix_prefixipprefix_asnumber.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_rpki_prefix_prefixipprefix_asnumber_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_prefix_prefixipprefix_asnumber_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_rpki' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'][key] = val
    
    # set VIEW_NODE -> show_rpki table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki'
    pass


@frr_show_rpki_prefix_prefixipprefix_asnumber_json.command('./	<cr>')
def frr_show_rpki_prefix_prefixipprefix_asnumber_json_cr():
    pass


@frr_show_rpki_prefix_prefixipprefix.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_rpki_prefix_prefixipprefix_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_rpki_prefix_prefixipprefix_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_rpki' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_rpki']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_rpki'][key] = val
    
    # set VIEW_NODE -> show_rpki table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_rpki'
    pass


@frr_show_rpki_prefix_prefixipprefix_json.command('./	<cr>')
def frr_show_rpki_prefix_prefixipprefix_json_cr():
    pass

