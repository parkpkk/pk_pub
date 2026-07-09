import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='babel',)
def frr_config_router_babel_babel(babel_='babel'):
    """Babel commands"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_babel.name
    
    if 'BABEL_NODE|babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|babel']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|babel'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|babel'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'babel')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_babel.group(cls=FRR_AbbreviationGroup, name='diversity', invoke_without_command=True)
def frr_config_router_babel_babel_diversity(diversity_='diversity'):
    """Enable diversity-aware routing."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_babel_diversity.name
    data_gen['diversity'] = diversity_='diversity'
    
    if 'BABEL_NODE|babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|babel']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|babel'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|babel'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'babel')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_babel_diversity.command('./	<cr>')
def frr_config_router_babel_babel_diversity_cr():
    pass


@frr_config_router_babel_babel.group(cls=FRR_AbbreviationGroup, name='diversity-factor', invoke_without_command=True)
@click.argument('factor_in_units_of', metavar='(1-256)', required=True, type=FRR_TYPE((1, 256)))
def frr_config_router_babel_babel_diversityfactor(factor_in_units_of, diversityfactor_='diversity-factor'):
    """Set the diversity factor."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_babel_diversityfactor.name
    data_gen['diversity-factor'] = diversityfactor_='diversity-factor'
    data_gen['FACTOR_IN_UNITS_OF'] = factor_in_units_of
    
    if 'BABEL_NODE|babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|babel']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|babel'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|babel'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'babel')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_babel_diversityfactor.command('./	<cr>')
def frr_config_router_babel_babel_diversityfactor_cr():
    pass


@frr_config_router_babel_babel.group(cls=FRR_AbbreviationGroup, name='resend-delay', invoke_without_command=True)
@click.argument('milliseconds', metavar='(20-655340)', required=True, type=FRR_TYPE((20, 655340)))
def frr_config_router_babel_babel_resenddelay(milliseconds, resenddelay_='resend-delay'):
    """Time before resending a message"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_babel_resenddelay.name
    data_gen['resend-delay'] = resenddelay_='resend-delay'
    data_gen['MILLISECONDS'] = milliseconds
    
    if 'BABEL_NODE|babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|babel']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|babel'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|babel'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'babel')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_babel_resenddelay.command('./	<cr>')
def frr_config_router_babel_babel_resenddelay_cr():
    pass


@frr_config_router_babel_babel.group(cls=FRR_AbbreviationGroup, name='smoothing-half-life', invoke_without_command=True)
@click.argument('seconds', metavar='(0-65534)', required=True, type=FRR_TYPE((0, 65534)))
def frr_config_router_babel_babel_smoothinghalflife(seconds, smoothinghalflife_='smoothing-half-life'):
    """Smoothing half-life"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_babel_smoothinghalflife.name
    data_gen['smoothing-half-life'] = smoothinghalflife_='smoothing-half-life'
    data_gen['SECONDS'] = seconds
    
    if 'BABEL_NODE|babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|babel']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|babel'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|babel'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'babel')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_babel_smoothinghalflife.command('./	<cr>')
def frr_config_router_babel_babel_smoothinghalflife_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_babel_distributelist(distributelist_='distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_distributelist.name
    
    if 'BABEL_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['ACCESSLIST4_NAME']),)
def frr_config_router_babel_distributelist_accesslistname():
    """4"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
def frr_config_router_babel_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_babel_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_babel_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['WORD']), invoke_without_command=True)
def frr_config_router_babel_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_babel_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_babel_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST4_NAME', required=True, type=FRR_TYPE('ACCESSLIST4_NAME'))
def frr_config_router_babel_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'BABEL_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
def frr_config_router_babel_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_babel_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_babel_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['WORD']), invoke_without_command=True)
def frr_config_router_babel_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_babel_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_config_router_babel_end(end_='end'):
    """End current mode and change to enable mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_end.name
    
    if 'BABEL_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|end'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|end'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'end')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_end.command('./	<cr>')
def frr_config_router_babel_end_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_config_router_babel_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_exit.name
    
    if 'BABEL_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|exit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|exit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'exit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_exit.command('./	<cr>')
def frr_config_router_babel_exit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_config_router_babel_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_find.name
    
    if 'BABEL_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_config_router_babel_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'BABEL_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_find_fromsearchpattern.command('./	<cr>')
def frr_config_router_babel_find_fromsearchpattern_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ipv6',)
def frr_config_router_babel_ipv6():
    """IPv6"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_babel_ipv6.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_babel_ipv6_distributelist(ipv6_distributelist_='ipv6_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_ipv6_distributelist.name
    
    if 'BABEL_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['ACCESSLIST6_NAME']),)
def frr_config_router_babel_ipv6_distributelist_accesslistname():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_ipv6_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_ipv6_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_babel_ipv6_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_ipv6_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_ipv6_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_babel_ipv6_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_babel_ipv6_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_babel_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_babel_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_babel_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_babel_ipv6_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_ipv6_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'BABEL_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_ipv6_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_babel_ipv6_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_ipv6_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_ipv6_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_babel_ipv6_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_babel_ipv6_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_babel_ipv6_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_ipv6_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_ipv6_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_babel_ipv6_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_config_router_babel_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_list.name
    
    if 'BABEL_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_list.command('./	<cr>')
def frr_config_router_babel_list_cr():
    pass


@frr_config_router_babel_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_config_router_babel_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'BABEL_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_list_permutations.command('./	<cr>')
def frr_config_router_babel_list_permutations_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='network', invoke_without_command=True)
@click.argument('interface_or_address', metavar='IF_OR_ADDR', required=True, type=FRR_TYPE('IF_OR_ADDR'))
def frr_config_router_babel_network(interface_or_address, network_='network'):
    """Enable Babel protocol on specified interface or network."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_network.name
    data_gen['INTERFACE_OR_ADDRESS'] = interface_or_address
    
    if 'BABEL_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_network.command('./	<cr>')
def frr_config_router_babel_network_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_config_router_babel_no(no_='no'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no.name
    
    if 'BABEL_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no.group(cls=FRR_AbbreviationGroup, name='babel',)
def frr_config_router_babel_no_babel(no_babel_='no_babel'):
    """Babel commands"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_babel.name
    
    if 'BABEL_NODE|no_babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_babel']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_babel'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_babel'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_babel')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_babel.group(cls=FRR_AbbreviationGroup, name='diversity', invoke_without_command=True)
def frr_config_router_babel_no_babel_diversity(diversity_='diversity'):
    """Disable diversity-aware routing."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_babel_diversity.name
    data_gen['diversity'] = diversity_='diversity'
    
    if 'BABEL_NODE|no_babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_babel']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_babel'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_babel'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_babel')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_babel_diversity.command('./	<cr>')
def frr_config_router_babel_no_babel_diversity_cr():
    pass


@frr_config_router_babel_no_babel.group(cls=FRR_AbbreviationGroup, name='diversity-factor', invoke_without_command=True)
@click.argument('factor_in_units_of', metavar='(1-256)', required=True, type=FRR_TYPE((1, 256)))
def frr_config_router_babel_no_babel_diversityfactor(factor_in_units_of, diversityfactor_='diversity-factor'):
    """Set the diversity factor."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_babel_diversityfactor.name
    data_gen['diversity-factor'] = diversityfactor_='diversity-factor'
    data_gen['FACTOR_IN_UNITS_OF'] = factor_in_units_of
    
    if 'BABEL_NODE|no_babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_babel']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_babel'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_babel'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_babel')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_babel_diversityfactor.command('./	<cr>')
def frr_config_router_babel_no_babel_diversityfactor_cr():
    pass


@frr_config_router_babel_no_babel.group(cls=FRR_AbbreviationGroup, name='resend-delay', invoke_without_command=True)
@click.argument('milliseconds', metavar='(20-655340)', required=True, type=FRR_TYPE((20, 655340)))
def frr_config_router_babel_no_babel_resenddelay(milliseconds, resenddelay_='resend-delay'):
    """Time before resending a message"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_babel_resenddelay.name
    data_gen['resend-delay'] = resenddelay_='resend-delay'
    data_gen['MILLISECONDS'] = milliseconds
    
    if 'BABEL_NODE|no_babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_babel']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_babel'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_babel'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_babel')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_babel_resenddelay.command('./	<cr>')
def frr_config_router_babel_no_babel_resenddelay_cr():
    pass


@frr_config_router_babel_no_babel.group(cls=FRR_AbbreviationGroup, name='smoothing-half-life', invoke_without_command=True)
@click.argument('seconds', metavar='(0-65534)', required=True, type=FRR_TYPE((0, 65534)))
def frr_config_router_babel_no_babel_smoothinghalflife(seconds, smoothinghalflife_='smoothing-half-life'):
    """Smoothing half-life"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_babel_smoothinghalflife.name
    data_gen['smoothing-half-life'] = smoothinghalflife_='smoothing-half-life'
    data_gen['SECONDS'] = seconds
    
    if 'BABEL_NODE|no_babel' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_babel'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_babel']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_babel'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_babel'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_babel')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_babel_smoothinghalflife.command('./	<cr>')
def frr_config_router_babel_no_babel_smoothinghalflife_cr():
    pass


@frr_config_router_babel_no.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_babel_no_distributelist(no_distributelist_='no_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_distributelist.name
    
    if 'BABEL_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['ACCESSLIST4_NAME']),)
def frr_config_router_babel_no_distributelist_accesslistname():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_babel_no_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_babel_no_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_babel_no_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_babel_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_babel_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_babel_no_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST4_NAME', required=True, type=FRR_TYPE('ACCESSLIST4_NAME'))
def frr_config_router_babel_no_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'BABEL_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_babel_no_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_babel_no_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_babel_no_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_babel_no_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_babel_no_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_babel_no.group(cls=FRR_AbbreviationGroup, name='ipv6',)
def frr_config_router_babel_no_ipv6():
    """IPv6"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_babel_no_ipv6.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_babel_no_ipv6_distributelist(no_ipv6_distributelist_='no_ipv6_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_ipv6_distributelist.name
    
    if 'BABEL_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['ACCESSLIST6_NAME']),)
def frr_config_router_babel_no_ipv6_distributelist_accesslistname():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_ipv6_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_ipv6_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_babel_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_babel_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_babel_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_babel_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_babel_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_babel_no_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_babel_no_ipv6_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_ipv6_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'BABEL_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_ipv6_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_babel_no_ipv6_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_ipv6_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_ipv6_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_babel_no_ipv6_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_babel_no_ipv6_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_babel_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_babel_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_babel_no.group(cls=FRR_AbbreviationGroup, name='network', invoke_without_command=True)
@click.argument('interface_or_address', metavar='IF_OR_ADDR', required=True, type=FRR_TYPE('IF_OR_ADDR'))
def frr_config_router_babel_no_network(interface_or_address, network_='network'):
    """Disable Babel protocol on specified interface or network."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_network.name
    data_gen['network'] = network_='network'
    data_gen['INTERFACE_OR_ADDRESS'] = interface_or_address
    
    if 'BABEL_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_network.command('./	<cr>')
def frr_config_router_babel_no_network_cr():
    pass


@frr_config_router_babel_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_config_router_babel_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_output.name
    
    if 'BABEL_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_output.command('./	<cr>')
def frr_config_router_babel_no_output_cr():
    pass


@frr_config_router_babel_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_config_router_babel_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_output_file.name
    
    if 'BABEL_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_output_file.command('./	<cr>')
def frr_config_router_babel_no_output_file_cr():
    pass


@frr_config_router_babel_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['FILE']), invoke_without_command=True)
def frr_config_router_babel_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'BABEL_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_config_router_babel_no_output_file_pathtodumpoutput_cr():
    pass


@frr_config_router_babel_no.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
def frr_config_router_babel_no_redistribute(no_redistribute_='no_redistribute'):
    """Redistribute"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_redistribute.name
    
    if 'BABEL_NODE|no_redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_redistribute.command('./	<cr>')
def frr_config_router_babel_no_redistribute_cr():
    pass


@frr_config_router_babel_no_redistribute.group(cls=FRR_AbbreviationGroup, name='ipv4', invoke_without_command=True)
@click.argument('frr_ip_redist_help_str_babeld', metavar='FRR_IP_REDIST_STR_BABELD', required=True, type=FRR_TYPE('FRR_IP_REDIST_STR_BABELD'))
def frr_config_router_babel_no_redistribute_ipv4(frr_ip_redist_help_str_babeld, ipv4_='ipv4'):
    """Redistribute IPv4 routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_redistribute_ipv4.name
    data_gen['ipv4'] = ipv4_='ipv4'
    data_gen['FRR_IP_REDIST_HELP_STR_BABELD'] = frr_ip_redist_help_str_babeld
    
    if 'BABEL_NODE|no_redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_redistribute_ipv4.command('./	<cr>')
def frr_config_router_babel_no_redistribute_ipv4_cr():
    pass


@frr_config_router_babel_no_redistribute.group(cls=FRR_AbbreviationGroup, name='ipv6', invoke_without_command=True)
@click.argument('frr_ip6_redist_help_str_babeld', metavar='FRR_IP6_REDIST_STR_BABELD', required=True, type=FRR_TYPE('FRR_IP6_REDIST_STR_BABELD'))
def frr_config_router_babel_no_redistribute_ipv6(frr_ip6_redist_help_str_babeld, ipv6_='ipv6'):
    """Redistribute IPv6 routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_no_redistribute_ipv6.name
    data_gen['ipv6'] = ipv6_='ipv6'
    data_gen['FRR_IP6_REDIST_HELP_STR_BABELD'] = frr_ip6_redist_help_str_babeld
    
    if 'BABEL_NODE|no_redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|no_redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|no_redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|no_redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|no_redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_no_redistribute_ipv6.command('./	<cr>')
def frr_config_router_babel_no_redistribute_ipv6_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_config_router_babel_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_output.name
    
    if 'BABEL_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_config_router_babel_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'BABEL_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_output_file.command('./	<cr>')
def frr_config_router_babel_output_file_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_config_router_babel_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_quit.name
    
    if 'BABEL_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|quit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|quit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'quit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_quit.command('./	<cr>')
def frr_config_router_babel_quit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
def frr_config_router_babel_redistribute(redistribute_='redistribute'):
    """Redistribute"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_redistribute.name
    
    if 'BABEL_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_redistribute.command('./	<cr>')
def frr_config_router_babel_redistribute_cr():
    pass


@frr_config_router_babel_redistribute.group(cls=FRR_AbbreviationGroup, name='ipv4', invoke_without_command=True)
@click.argument('frr_ip_redist_help_str_babeld', metavar='FRR_IP_REDIST_STR_BABELD', required=True, type=FRR_TYPE('FRR_IP_REDIST_STR_BABELD'))
def frr_config_router_babel_redistribute_ipv4(frr_ip_redist_help_str_babeld, ipv4_='ipv4'):
    """Redistribute IPv4 routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_redistribute_ipv4.name
    data_gen['ipv4'] = ipv4_='ipv4'
    data_gen['FRR_IP_REDIST_HELP_STR_BABELD'] = frr_ip_redist_help_str_babeld
    
    if 'BABEL_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_redistribute_ipv4.command('./	<cr>')
def frr_config_router_babel_redistribute_ipv4_cr():
    pass


@frr_config_router_babel_redistribute.group(cls=FRR_AbbreviationGroup, name='ipv6', invoke_without_command=True)
@click.argument('frr_ip6_redist_help_str_babeld', metavar='FRR_IP6_REDIST_STR_BABELD', required=True, type=FRR_TYPE('FRR_IP6_REDIST_STR_BABELD'))
def frr_config_router_babel_redistribute_ipv6(frr_ip6_redist_help_str_babeld, ipv6_='ipv6'):
    """Redistribute IPv6 routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_babel_redistribute_ipv6.name
    data_gen['ipv6'] = ipv6_='ipv6'
    data_gen['FRR_IP6_REDIST_HELP_STR_BABELD'] = frr_ip6_redist_help_str_babeld
    
    if 'BABEL_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['BABEL_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['BABEL_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['BABEL_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['BABEL_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'BABEL_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['BABEL_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_babel_redistribute_ipv6.command('./	<cr>')
def frr_config_router_babel_redistribute_ipv6_cr():
    pass

