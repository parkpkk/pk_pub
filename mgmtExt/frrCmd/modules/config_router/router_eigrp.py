import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_eigrp_distributelist(distributelist_='distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_distributelist.name
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['ACCESSLIST_NAME']),)
def frr_config_router_eigrp_distributelist_accesslistname():
    """4"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
def frr_config_router_eigrp_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_eigrp_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_eigrp_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['WORD']), invoke_without_command=True)
def frr_config_router_eigrp_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_eigrp_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_eigrp_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST_NAME', required=True, type=FRR_TYPE('ACCESSLIST_NAME'))
def frr_config_router_eigrp_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
def frr_config_router_eigrp_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_eigrp_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_eigrp_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['WORD']), invoke_without_command=True)
def frr_config_router_eigrp_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_eigrp_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='eigrp',)
def frr_config_router_eigrp_eigrp(eigrp_='eigrp'):
    """P information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_eigrp.name
    
    if 'EIGRP_NODE|eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|eigrp'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|eigrp'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'eigrp')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_eigrp.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
@click.argument('eigrp_routerid_in_ip', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_eigrp_eigrp_routerid(eigrp_routerid_in_ip, routerid_='router-id'):
    """Router ID for this EIGRP process"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_eigrp_routerid.name
    data_gen['router-id'] = routerid_='router-id'
    data_gen['EIGRP_ROUTER-ID_IN_IP'] = eigrp_routerid_in_ip
    
    if 'EIGRP_NODE|eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|eigrp'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|eigrp'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'eigrp')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_eigrp_routerid.command('./	<cr>')
def frr_config_router_eigrp_eigrp_routerid_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_config_router_eigrp_end(end_='end'):
    """End current mode and change to enable mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_end.name
    
    if 'EIGRP_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|end'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|end'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'end')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_end.command('./	<cr>')
def frr_config_router_eigrp_end_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_config_router_eigrp_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_exit.name
    
    if 'EIGRP_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|exit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|exit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'exit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_exit.command('./	<cr>')
def frr_config_router_eigrp_exit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_config_router_eigrp_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_find.name
    
    if 'EIGRP_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_config_router_eigrp_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'EIGRP_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_find_fromsearchpattern.command('./	<cr>')
def frr_config_router_eigrp_find_fromsearchpattern_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_config_router_eigrp_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_list.name
    
    if 'EIGRP_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_list.command('./	<cr>')
def frr_config_router_eigrp_list_cr():
    pass


@frr_config_router_eigrp_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_config_router_eigrp_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'EIGRP_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_list_permutations.command('./	<cr>')
def frr_config_router_eigrp_list_permutations_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='maximum-paths', invoke_without_command=True)
@click.argument('number_of_paths', metavar='(1-32)', required=True, type=FRR_TYPE((1, 32)))
def frr_config_router_eigrp_maximumpaths(number_of_paths, maximumpaths_='maximum-paths'):
    """Forward packets over multiple paths"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_maximumpaths.name
    data_gen['NUMBER_OF_PATHS'] = number_of_paths
    
    if 'EIGRP_NODE|maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_maximumpaths.command('./	<cr>')
def frr_config_router_eigrp_maximumpaths_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='metric',)
def frr_config_router_eigrp_metric(metric_='metric'):
    """Modify metrics and parameters for advertisement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_metric.name
    
    if 'EIGRP_NODE|metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|metric']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_metric.group(cls=FRR_AbbreviationGroup, name='weights',)
@click.argument('cost_value', metavar='(0-255)', required=True, type=FRR_TYPE((0, 255)))
def frr_config_router_eigrp_metric_weights(cost_value, weights_='weights'):
    """Modify metric coefficients"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_metric_weights.name
    data_gen['weights'] = weights_='weights'
    data_gen['COST_VALUE'] = cost_value
    
    if 'EIGRP_NODE|metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|metric']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_metric_weights.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(0, 255)]), invoke_without_command=True)
def frr_config_router_eigrp_metric_weights_costvalue():
    """K6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_metric_weights_costvalue.name
    data_gen['COST_VALUE'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|metric']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_metric_weights_costvalue.command('./	<cr>')
def frr_config_router_eigrp_metric_weights_costvalue_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_eigrp_neighbor(neighbor_address, neighbor_='neighbor'):
    """Specify a neighbor router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_neighbor.name
    data_gen['NEIGHBOR_ADDRESS'] = neighbor_address
    
    if 'EIGRP_NODE|neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|neighbor'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|neighbor'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'neighbor')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_neighbor.command('./	<cr>')
def frr_config_router_eigrp_neighbor_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='network', invoke_without_command=True)
@click.argument('ip_prefix', metavar='A.B.C.D/M', required=True, type=FRR_TYPE('A.B.C.D/M'))
def frr_config_router_eigrp_network(ip_prefix, network_='network'):
    """Enable routing on an IP network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_network.name
    data_gen['IP_PREFIX'] = ip_prefix
    
    if 'EIGRP_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_network.command('./	<cr>')
def frr_config_router_eigrp_network_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_config_router_eigrp_no(no_='no'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no.name
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_eigrp_no_distributelist(no_distributelist_='no_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_distributelist.name
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['ACCESSLIST_NAME']),)
def frr_config_router_eigrp_no_distributelist_accesslistname():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_eigrp_no_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_eigrp_no_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_eigrp_no_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_eigrp_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_eigrp_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_eigrp_no_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST_NAME', required=True, type=FRR_TYPE('ACCESSLIST_NAME'))
def frr_config_router_eigrp_no_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_eigrp_no_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_eigrp_no_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_eigrp_no_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_eigrp_no_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_eigrp_no_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='eigrp', invoke_without_command=True)
def frr_config_router_eigrp_no_eigrp():
    """P information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_eigrp.name
    
    if 'EIGRP_NODE|no_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_eigrp')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_eigrp.command('./	<cr>')
def frr_config_router_eigrp_no_eigrp_cr():
    pass


@frr_config_router_eigrp_no_eigrp.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
def frr_config_router_eigrp_no_eigrp_routerid(no_eigrp_routerid_='no_eigrp_router-id'):
    """Router ID for this EIGRP process"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_eigrp_routerid.name
    
    if 'EIGRP_NODE|no_eigrp_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_eigrp_router-id')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_eigrp_routerid.command('./	<cr>')
def frr_config_router_eigrp_no_eigrp_routerid_cr():
    pass


@frr_config_router_eigrp_no_eigrp_routerid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D']), invoke_without_command=True)
def frr_config_router_eigrp_no_eigrp_routerid_eigrprouteridinip():
    """EIGRP Router-ID in IP address format"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_eigrp_routerid_eigrprouteridinip.name
    data_gen['EIGRP_ROUTER-ID_IN_IP'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_eigrp_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_eigrp_router-id')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_eigrp_routerid_eigrprouteridinip.command('./	<cr>')
def frr_config_router_eigrp_no_eigrp_routerid_eigrprouteridinip_cr():
    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='maximum-paths', invoke_without_command=True)
def frr_config_router_eigrp_no_maximumpaths(no_maximumpaths_='no_maximum-paths'):
    """Forward packets over multiple paths"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_maximumpaths.name
    
    if 'EIGRP_NODE|no_maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_maximumpaths.command('./	<cr>')
def frr_config_router_eigrp_no_maximumpaths_cr():
    pass


@frr_config_router_eigrp_no_maximumpaths.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, [(1, 32)]), invoke_without_command=True)
def frr_config_router_eigrp_no_maximumpaths_numberofpaths():
    """Number of paths"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_maximumpaths_numberofpaths.name
    data_gen['NUMBER_OF_PATHS'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_maximumpaths_numberofpaths.command('./	<cr>')
def frr_config_router_eigrp_no_maximumpaths_numberofpaths_cr():
    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
def frr_config_router_eigrp_no_metric():
    """Modify metrics and parameters for advertisement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_metric.name
    
    if 'EIGRP_NODE|no_metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_metric']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_metric.command('./	<cr>')
def frr_config_router_eigrp_no_metric_cr():
    pass


@frr_config_router_eigrp_no_metric.group(cls=FRR_AbbreviationGroup, name='weights', invoke_without_command=True)
def frr_config_router_eigrp_no_metric_weights(no_metric_weights_='no_metric_weights'):
    """Modify metric coefficients"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_metric_weights.name
    
    if 'EIGRP_NODE|no_metric_weights' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_metric_weights')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_metric_weights.command('./	<cr>')
def frr_config_router_eigrp_no_metric_weights_cr():
    pass


@frr_config_router_eigrp_no_metric_weights.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(0, 255)]),)
def frr_config_router_eigrp_no_metric_weights_costvalue():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_metric_weights_costvalue.name
    data_gen['COST_VALUE'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_metric_weights' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_metric_weights')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_eigrp_no_neighbor(neighbor_address, neighbor_='neighbor'):
    """Specify a neighbor router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    data_gen['NEIGHBOR_ADDRESS'] = neighbor_address
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_neighbor.command('./	<cr>')
def frr_config_router_eigrp_no_neighbor_cr():
    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='network', invoke_without_command=True)
@click.argument('ip_prefix', metavar='A.B.C.D/M', required=True, type=FRR_TYPE('A.B.C.D/M'))
def frr_config_router_eigrp_no_network(ip_prefix, network_='network'):
    """Enable routing on an IP network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_network.name
    data_gen['network'] = network_='network'
    data_gen['IP_PREFIX'] = ip_prefix
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_network.command('./	<cr>')
def frr_config_router_eigrp_no_network_cr():
    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_config_router_eigrp_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_output.name
    
    if 'EIGRP_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_output.command('./	<cr>')
def frr_config_router_eigrp_no_output_cr():
    pass


@frr_config_router_eigrp_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_config_router_eigrp_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_output_file.name
    
    if 'EIGRP_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_output_file.command('./	<cr>')
def frr_config_router_eigrp_no_output_file_cr():
    pass


@frr_config_router_eigrp_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['FILE']), invoke_without_command=True)
def frr_config_router_eigrp_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_config_router_eigrp_no_output_file_pathtodumpoutput_cr():
    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='passive-interface', invoke_without_command=True)
@click.argument('interface_to_suppress_on', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_eigrp_no_passiveinterface(interface_to_suppress_on, passiveinterface_='passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_passiveinterface.name
    data_gen['passive-interface'] = passiveinterface_='passive-interface'
    data_gen['INTERFACE_TO_SUPPRESS_ON'] = interface_to_suppress_on
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_passiveinterface.command('./	<cr>')
def frr_config_router_eigrp_no_passiveinterface_cr():
    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_eigrpd', metavar='FRR_REDIST_STR_EIGRPD', required=True, type=FRR_TYPE('FRR_REDIST_STR_EIGRPD'))
def frr_config_router_eigrp_no_redistribute(frr_redist_help_str_eigrpd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_redistribute.name
    data_gen['redistribute'] = redistribute_='redistribute'
    data_gen['FRR_REDIST_HELP_STR_EIGRPD'] = frr_redist_help_str_eigrpd
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_redistribute.command('./	<cr>')
def frr_config_router_eigrp_no_redistribute_cr():
    pass


@frr_config_router_eigrp_no_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('bandwidth_metric_in_kbits', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
@click.argument('eigrp_delay_metric_in', metavar='(0-4294967295)', required=True, type=FRR_TYPE((0, 4294967295)))
@click.argument('cost_value', metavar='(0-255)', required=True, type=FRR_TYPE((0, 255)))
@click.argument('eigrp_effective_bandwidth_metric', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
@click.argument('eigrp_mtu_of_the', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
def frr_config_router_eigrp_no_redistribute_metric(eigrp_mtu_of_the, bandwidth_metric_in_kbits, eigrp_delay_metric_in, cost_value, eigrp_effective_bandwidth_metric, metric_='metric'):
    """Metric for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['BANDWIDTH_METRIC_IN_KBITS'] = bandwidth_metric_in_kbits
    data_gen['EIGRP_DELAY_METRIC_IN'] = eigrp_delay_metric_in
    data_gen['COST_VALUE'] = cost_value
    data_gen['EIGRP_EFFECTIVE_BANDWIDTH_METRIC'] = eigrp_effective_bandwidth_metric
    data_gen['EIGRP_MTU_OF_THE'] = eigrp_mtu_of_the
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_redistribute_metric.command('./	<cr>')
def frr_config_router_eigrp_no_redistribute_metric_cr():
    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='timers', invoke_without_command=True)
def frr_config_router_eigrp_no_timers():
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_timers.name
    
    if 'EIGRP_NODE|no_timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_timers']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_timers.command('./	<cr>')
def frr_config_router_eigrp_no_timers_cr():
    pass


@frr_config_router_eigrp_no_timers.group(cls=FRR_AbbreviationGroup, name='active-time', invoke_without_command=True)
def frr_config_router_eigrp_no_timers_activetime(no_timers_activetime_='no_timers_active-time'):
    """Time limit for active state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_timers_activetime.name
    
    if 'EIGRP_NODE|no_timers_active-time' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_active-time')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_timers_activetime.command('./	<cr>')
def frr_config_router_eigrp_no_timers_activetime_cr():
    pass


@frr_config_router_eigrp_no_timers_activetime.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 65535), 'disabled']), invoke_without_command=True)
def frr_config_router_eigrp_no_timers_activetime_choicecase():
    """Active state time limit in seconds"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_timers_activetime_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_timers_active-time' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_active-time')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_timers_activetime_choicecase.command('./	<cr>')
def frr_config_router_eigrp_no_timers_activetime_choicecase_cr():
    pass


@frr_config_router_eigrp_no.group(cls=FRR_AbbreviationGroup, name='variance', invoke_without_command=True)
def frr_config_router_eigrp_no_variance(no_variance_='no_variance'):
    """Control load balancing variance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_variance.name
    
    if 'EIGRP_NODE|no_variance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_variance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_variance']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_variance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_variance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_variance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_variance.command('./	<cr>')
def frr_config_router_eigrp_no_variance_cr():
    pass


@frr_config_router_eigrp_no_variance.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, [(1, 128)]), invoke_without_command=True)
def frr_config_router_eigrp_no_variance_metricvariancemultiplier():
    """Metric variance multiplier"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_no_variance_metricvariancemultiplier.name
    data_gen['METRIC_VARIANCE_MULTIPLIER'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_variance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_variance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_variance']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_variance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_variance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_variance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_no_variance_metricvariancemultiplier.command('./	<cr>')
def frr_config_router_eigrp_no_variance_metricvariancemultiplier_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_config_router_eigrp_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_output.name
    
    if 'EIGRP_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_config_router_eigrp_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'EIGRP_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_output_file.command('./	<cr>')
def frr_config_router_eigrp_output_file_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='passive-interface', invoke_without_command=True)
@click.argument('interface_to_suppress_on', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_eigrp_passiveinterface(interface_to_suppress_on, passiveinterface_='passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_passiveinterface.name
    data_gen['INTERFACE_TO_SUPPRESS_ON'] = interface_to_suppress_on
    
    if 'EIGRP_NODE|passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_passiveinterface.command('./	<cr>')
def frr_config_router_eigrp_passiveinterface_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_config_router_eigrp_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_quit.name
    
    if 'EIGRP_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|quit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|quit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'quit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_quit.command('./	<cr>')
def frr_config_router_eigrp_quit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_eigrpd', metavar='FRR_REDIST_STR_EIGRPD', required=True, type=FRR_TYPE('FRR_REDIST_STR_EIGRPD'))
def frr_config_router_eigrp_redistribute(frr_redist_help_str_eigrpd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_redistribute.name
    data_gen['FRR_REDIST_HELP_STR_EIGRPD'] = frr_redist_help_str_eigrpd
    
    if 'EIGRP_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_redistribute.command('./	<cr>')
def frr_config_router_eigrp_redistribute_cr():
    pass


@frr_config_router_eigrp_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('bandwidth_metric_in_kbits', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
@click.argument('eigrp_delay_metric_in', metavar='(0-4294967295)', required=True, type=FRR_TYPE((0, 4294967295)))
@click.argument('cost_value', metavar='(0-255)', required=True, type=FRR_TYPE((0, 255)))
@click.argument('eigrp_effective_bandwidth_metric', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
@click.argument('eigrp_mtu_of_the', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
def frr_config_router_eigrp_redistribute_metric(eigrp_mtu_of_the, bandwidth_metric_in_kbits, eigrp_delay_metric_in, cost_value, eigrp_effective_bandwidth_metric, metric_='metric'):
    """Metric for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['BANDWIDTH_METRIC_IN_KBITS'] = bandwidth_metric_in_kbits
    data_gen['EIGRP_DELAY_METRIC_IN'] = eigrp_delay_metric_in
    data_gen['COST_VALUE'] = cost_value
    data_gen['EIGRP_EFFECTIVE_BANDWIDTH_METRIC'] = eigrp_effective_bandwidth_metric
    data_gen['EIGRP_MTU_OF_THE'] = eigrp_mtu_of_the
    
    if 'EIGRP_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_redistribute_metric.command('./	<cr>')
def frr_config_router_eigrp_redistribute_metric_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='timers',)
def frr_config_router_eigrp_timers(timers_='timers'):
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_timers.name
    
    if 'EIGRP_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_timers.group(cls=FRR_AbbreviationGroup, name='active-time',)
def frr_config_router_eigrp_timers_activetime(activetime_='active-time'):
    """Time limit for active state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_timers_activetime.name
    data_gen['active-time'] = activetime_='active-time'
    
    if 'EIGRP_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_timers_activetime.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, [(1, 65535), 'disabled']), invoke_without_command=True)
def frr_config_router_eigrp_timers_activetime_activetimechoicecase():
    """Active state time limit in seconds"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_timers_activetime_activetimechoicecase.name
    data_gen['ACTIVE-TIME_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_timers_activetime_activetimechoicecase.command('./	<cr>')
def frr_config_router_eigrp_timers_activetime_activetimechoicecase_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='variance', invoke_without_command=True)
@click.argument('metric_variance_multiplier', metavar='(1-128)', required=True, type=FRR_TYPE((1, 128)))
def frr_config_router_eigrp_variance(metric_variance_multiplier, variance_='variance'):
    """Control load balancing variance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_variance.name
    data_gen['METRIC_VARIANCE_MULTIPLIER'] = metric_variance_multiplier
    
    if 'EIGRP_NODE|variance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|variance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|variance']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|variance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|variance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'variance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_variance.command('./	<cr>')
def frr_config_router_eigrp_variance_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_config_router_eigrp_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'CONFIG_NODE|router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['CONFIG_NODE|router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['CONFIG_NODE|router']:
            key = key.upper()
        COMMON_DATA_MAP['CONFIG_NODE|router'][key] = val
    
    # set CONFIG_NODE -> router table
    COMMON_DATA_MAP['CONFIG_NODE'] = 'router'
    pass


@frr_config_router_eigrp_vrf.command('./	<cr>')
def frr_config_router_eigrp_vrf_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_eigrp_vrf_distributelist(distributelist_='distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_distributelist.name
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['ACCESSLIST_NAME']),)
def frr_config_router_eigrp_vrf_distributelist_accesslistname():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_eigrp_vrf_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_eigrp_vrf_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_eigrp_vrf_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_eigrp_vrf_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST_NAME', required=True, type=FRR_TYPE('ACCESSLIST_NAME'))
def frr_config_router_eigrp_vrf_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_eigrp_vrf_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_eigrp_vrf_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_eigrp_vrf_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='eigrp',)
def frr_config_router_eigrp_vrf_eigrp(eigrp_='eigrp'):
    """P information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_eigrp.name
    
    if 'EIGRP_NODE|eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|eigrp'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|eigrp'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'eigrp')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_eigrp.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
@click.argument('eigrp_routerid_in_ip', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_eigrp_vrf_eigrp_routerid(eigrp_routerid_in_ip, routerid_='router-id'):
    """Router ID for this EIGRP process"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_eigrp_routerid.name
    data_gen['router-id'] = routerid_='router-id'
    data_gen['EIGRP_ROUTER-ID_IN_IP'] = eigrp_routerid_in_ip
    
    if 'EIGRP_NODE|eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|eigrp'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|eigrp'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'eigrp')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_eigrp_routerid.command('./	<cr>')
def frr_config_router_eigrp_vrf_eigrp_routerid_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_config_router_eigrp_vrf_end(end_='end'):
    """End current mode and change to enable mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_end.name
    
    if 'EIGRP_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|end'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|end'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'end')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_end.command('./	<cr>')
def frr_config_router_eigrp_vrf_end_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_config_router_eigrp_vrf_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_exit.name
    
    if 'EIGRP_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|exit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|exit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'exit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_exit.command('./	<cr>')
def frr_config_router_eigrp_vrf_exit_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_config_router_eigrp_vrf_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_find.name
    
    if 'EIGRP_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_config_router_eigrp_vrf_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'EIGRP_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_find_fromsearchpattern.command('./	<cr>')
def frr_config_router_eigrp_vrf_find_fromsearchpattern_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_config_router_eigrp_vrf_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_list.name
    
    if 'EIGRP_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_list.command('./	<cr>')
def frr_config_router_eigrp_vrf_list_cr():
    pass


@frr_config_router_eigrp_vrf_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_config_router_eigrp_vrf_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'EIGRP_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_list_permutations.command('./	<cr>')
def frr_config_router_eigrp_vrf_list_permutations_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='maximum-paths', invoke_without_command=True)
@click.argument('number_of_paths', metavar='(1-32)', required=True, type=FRR_TYPE((1, 32)))
def frr_config_router_eigrp_vrf_maximumpaths(number_of_paths, maximumpaths_='maximum-paths'):
    """Forward packets over multiple paths"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_maximumpaths.name
    data_gen['NUMBER_OF_PATHS'] = number_of_paths
    
    if 'EIGRP_NODE|maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_maximumpaths.command('./	<cr>')
def frr_config_router_eigrp_vrf_maximumpaths_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='metric',)
def frr_config_router_eigrp_vrf_metric(metric_='metric'):
    """Modify metrics and parameters for advertisement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_metric.name
    
    if 'EIGRP_NODE|metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|metric']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_metric.group(cls=FRR_AbbreviationGroup, name='weights',)
@click.argument('cost_value', metavar='(0-255)', required=True, type=FRR_TYPE((0, 255)))
def frr_config_router_eigrp_vrf_metric_weights(cost_value, weights_='weights'):
    """Modify metric coefficients"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_metric_weights.name
    data_gen['weights'] = weights_='weights'
    data_gen['COST_VALUE'] = cost_value
    
    if 'EIGRP_NODE|metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|metric']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_metric_weights.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(0, 255)]), invoke_without_command=True)
def frr_config_router_eigrp_vrf_metric_weights_costvalue():
    """K6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_metric_weights_costvalue.name
    data_gen['COST_VALUE'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|metric']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_metric_weights_costvalue.command('./	<cr>')
def frr_config_router_eigrp_vrf_metric_weights_costvalue_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_eigrp_vrf_neighbor(neighbor_address, neighbor_='neighbor'):
    """Specify a neighbor router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_neighbor.name
    data_gen['NEIGHBOR_ADDRESS'] = neighbor_address
    
    if 'EIGRP_NODE|neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|neighbor'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|neighbor'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'neighbor')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_neighbor.command('./	<cr>')
def frr_config_router_eigrp_vrf_neighbor_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='network', invoke_without_command=True)
@click.argument('ip_prefix', metavar='A.B.C.D/M', required=True, type=FRR_TYPE('A.B.C.D/M'))
def frr_config_router_eigrp_vrf_network(ip_prefix, network_='network'):
    """Enable routing on an IP network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_network.name
    data_gen['IP_PREFIX'] = ip_prefix
    
    if 'EIGRP_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_network.command('./	<cr>')
def frr_config_router_eigrp_vrf_network_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_config_router_eigrp_vrf_no(no_='no'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no.name
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_eigrp_vrf_no_distributelist(no_distributelist_='no_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_distributelist.name
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['ACCESSLIST_NAME']),)
def frr_config_router_eigrp_vrf_no_distributelist_accesslistname():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_eigrp_vrf_no_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_eigrp_vrf_no_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST_NAME', required=True, type=FRR_TYPE('ACCESSLIST_NAME'))
def frr_config_router_eigrp_vrf_no_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_eigrp_vrf_no_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='eigrp', invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_eigrp():
    """P information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_eigrp.name
    
    if 'EIGRP_NODE|no_eigrp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_eigrp')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_eigrp.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_eigrp_cr():
    pass


@frr_config_router_eigrp_vrf_no_eigrp.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_eigrp_routerid(no_eigrp_routerid_='no_eigrp_router-id'):
    """Router ID for this EIGRP process"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_eigrp_routerid.name
    
    if 'EIGRP_NODE|no_eigrp_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_eigrp_router-id')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_eigrp_routerid.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_eigrp_routerid_cr():
    pass


@frr_config_router_eigrp_vrf_no_eigrp_routerid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_eigrp_routerid_eigrprouteridinip():
    """EIGRP Router-ID in IP address format"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_eigrp_routerid_eigrprouteridinip.name
    data_gen['EIGRP_ROUTER-ID_IN_IP'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_eigrp_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_eigrp_router-id'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_eigrp_router-id')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_eigrp_routerid_eigrprouteridinip.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_eigrp_routerid_eigrprouteridinip_cr():
    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='maximum-paths', invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_maximumpaths(no_maximumpaths_='no_maximum-paths'):
    """Forward packets over multiple paths"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_maximumpaths.name
    
    if 'EIGRP_NODE|no_maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_maximumpaths.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_maximumpaths_cr():
    pass


@frr_config_router_eigrp_vrf_no_maximumpaths.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 32)]), invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_maximumpaths_numberofpaths():
    """Number of paths"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_maximumpaths_numberofpaths.name
    data_gen['NUMBER_OF_PATHS'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_maximumpaths_numberofpaths.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_maximumpaths_numberofpaths_cr():
    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_metric():
    """Modify metrics and parameters for advertisement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_metric.name
    
    if 'EIGRP_NODE|no_metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_metric']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_metric.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_metric_cr():
    pass


@frr_config_router_eigrp_vrf_no_metric.group(cls=FRR_AbbreviationGroup, name='weights', invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_metric_weights(no_metric_weights_='no_metric_weights'):
    """Modify metric coefficients"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_metric_weights.name
    
    if 'EIGRP_NODE|no_metric_weights' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_metric_weights')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_metric_weights.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_metric_weights_cr():
    pass


@frr_config_router_eigrp_vrf_no_metric_weights.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(0, 255)]),)
def frr_config_router_eigrp_vrf_no_metric_weights_costvalue():
    """7"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_metric_weights_costvalue.name
    data_gen['COST_VALUE'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_metric_weights' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_metric_weights'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_metric_weights')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_eigrp_vrf_no_neighbor(neighbor_address, neighbor_='neighbor'):
    """Specify a neighbor router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    data_gen['NEIGHBOR_ADDRESS'] = neighbor_address
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_neighbor.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_neighbor_cr():
    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='network', invoke_without_command=True)
@click.argument('ip_prefix', metavar='A.B.C.D/M', required=True, type=FRR_TYPE('A.B.C.D/M'))
def frr_config_router_eigrp_vrf_no_network(ip_prefix, network_='network'):
    """Enable routing on an IP network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_network.name
    data_gen['network'] = network_='network'
    data_gen['IP_PREFIX'] = ip_prefix
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_network.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_network_cr():
    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_output.name
    
    if 'EIGRP_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_output.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_output_cr():
    pass


@frr_config_router_eigrp_vrf_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_output_file.name
    
    if 'EIGRP_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_output_file.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_output_file_cr():
    pass


@frr_config_router_eigrp_vrf_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['FILE']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_output_file_pathtodumpoutput_cr():
    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='passive-interface', invoke_without_command=True)
@click.argument('interface_to_suppress_on', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_eigrp_vrf_no_passiveinterface(interface_to_suppress_on, passiveinterface_='passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_passiveinterface.name
    data_gen['passive-interface'] = passiveinterface_='passive-interface'
    data_gen['INTERFACE_TO_SUPPRESS_ON'] = interface_to_suppress_on
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_passiveinterface.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_passiveinterface_cr():
    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_eigrpd', metavar='FRR_REDIST_STR_EIGRPD', required=True, type=FRR_TYPE('FRR_REDIST_STR_EIGRPD'))
def frr_config_router_eigrp_vrf_no_redistribute(frr_redist_help_str_eigrpd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_redistribute.name
    data_gen['redistribute'] = redistribute_='redistribute'
    data_gen['FRR_REDIST_HELP_STR_EIGRPD'] = frr_redist_help_str_eigrpd
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_redistribute.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_redistribute_cr():
    pass


@frr_config_router_eigrp_vrf_no_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('bandwidth_metric_in_kbits', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
@click.argument('eigrp_delay_metric_in', metavar='(0-4294967295)', required=True, type=FRR_TYPE((0, 4294967295)))
@click.argument('cost_value', metavar='(0-255)', required=True, type=FRR_TYPE((0, 255)))
@click.argument('eigrp_effective_bandwidth_metric', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
@click.argument('eigrp_mtu_of_the', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
def frr_config_router_eigrp_vrf_no_redistribute_metric(eigrp_mtu_of_the, bandwidth_metric_in_kbits, eigrp_delay_metric_in, cost_value, eigrp_effective_bandwidth_metric, metric_='metric'):
    """Metric for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['BANDWIDTH_METRIC_IN_KBITS'] = bandwidth_metric_in_kbits
    data_gen['EIGRP_DELAY_METRIC_IN'] = eigrp_delay_metric_in
    data_gen['COST_VALUE'] = cost_value
    data_gen['EIGRP_EFFECTIVE_BANDWIDTH_METRIC'] = eigrp_effective_bandwidth_metric
    data_gen['EIGRP_MTU_OF_THE'] = eigrp_mtu_of_the
    
    if 'EIGRP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_redistribute_metric.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_redistribute_metric_cr():
    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='timers', invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_timers():
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_timers.name
    
    if 'EIGRP_NODE|no_timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_timers']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_timers.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_timers_cr():
    pass


@frr_config_router_eigrp_vrf_no_timers.group(cls=FRR_AbbreviationGroup, name='active-time', invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_timers_activetime(no_timers_activetime_='no_timers_active-time'):
    """Time limit for active state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_timers_activetime.name
    
    if 'EIGRP_NODE|no_timers_active-time' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_active-time')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_timers_activetime.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_timers_activetime_cr():
    pass


@frr_config_router_eigrp_vrf_no_timers_activetime.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(1, 65535), 'disabled']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_timers_activetime_choicecase():
    """Active state time limit in seconds"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_timers_activetime_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_timers_active-time' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_timers_active-time'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_active-time')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_timers_activetime_choicecase.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_timers_activetime_choicecase_cr():
    pass


@frr_config_router_eigrp_vrf_no.group(cls=FRR_AbbreviationGroup, name='variance', invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_variance(no_variance_='no_variance'):
    """Control load balancing variance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_variance.name
    
    if 'EIGRP_NODE|no_variance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_variance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_variance']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_variance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_variance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_variance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_variance.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_variance_cr():
    pass


@frr_config_router_eigrp_vrf_no_variance.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 128)]), invoke_without_command=True)
def frr_config_router_eigrp_vrf_no_variance_metricvariancemultiplier():
    """Metric variance multiplier"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_no_variance_metricvariancemultiplier.name
    data_gen['METRIC_VARIANCE_MULTIPLIER'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|no_variance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|no_variance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|no_variance']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|no_variance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|no_variance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_variance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_no_variance_metricvariancemultiplier.command('./	<cr>')
def frr_config_router_eigrp_vrf_no_variance_metricvariancemultiplier_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_config_router_eigrp_vrf_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_output.name
    
    if 'EIGRP_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_config_router_eigrp_vrf_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'EIGRP_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_output_file.command('./	<cr>')
def frr_config_router_eigrp_vrf_output_file_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='passive-interface', invoke_without_command=True)
@click.argument('interface_to_suppress_on', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_eigrp_vrf_passiveinterface(interface_to_suppress_on, passiveinterface_='passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_passiveinterface.name
    data_gen['INTERFACE_TO_SUPPRESS_ON'] = interface_to_suppress_on
    
    if 'EIGRP_NODE|passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_passiveinterface.command('./	<cr>')
def frr_config_router_eigrp_vrf_passiveinterface_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_config_router_eigrp_vrf_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_quit.name
    
    if 'EIGRP_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|quit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|quit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'quit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_quit.command('./	<cr>')
def frr_config_router_eigrp_vrf_quit_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_eigrpd', metavar='FRR_REDIST_STR_EIGRPD', required=True, type=FRR_TYPE('FRR_REDIST_STR_EIGRPD'))
def frr_config_router_eigrp_vrf_redistribute(frr_redist_help_str_eigrpd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_redistribute.name
    data_gen['FRR_REDIST_HELP_STR_EIGRPD'] = frr_redist_help_str_eigrpd
    
    if 'EIGRP_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_redistribute.command('./	<cr>')
def frr_config_router_eigrp_vrf_redistribute_cr():
    pass


@frr_config_router_eigrp_vrf_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('bandwidth_metric_in_kbits', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
@click.argument('eigrp_delay_metric_in', metavar='(0-4294967295)', required=True, type=FRR_TYPE((0, 4294967295)))
@click.argument('cost_value', metavar='(0-255)', required=True, type=FRR_TYPE((0, 255)))
@click.argument('eigrp_effective_bandwidth_metric', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
@click.argument('eigrp_mtu_of_the', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
def frr_config_router_eigrp_vrf_redistribute_metric(eigrp_mtu_of_the, bandwidth_metric_in_kbits, eigrp_delay_metric_in, cost_value, eigrp_effective_bandwidth_metric, metric_='metric'):
    """Metric for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['BANDWIDTH_METRIC_IN_KBITS'] = bandwidth_metric_in_kbits
    data_gen['EIGRP_DELAY_METRIC_IN'] = eigrp_delay_metric_in
    data_gen['COST_VALUE'] = cost_value
    data_gen['EIGRP_EFFECTIVE_BANDWIDTH_METRIC'] = eigrp_effective_bandwidth_metric
    data_gen['EIGRP_MTU_OF_THE'] = eigrp_mtu_of_the
    
    if 'EIGRP_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_redistribute_metric.command('./	<cr>')
def frr_config_router_eigrp_vrf_redistribute_metric_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='timers',)
def frr_config_router_eigrp_vrf_timers(timers_='timers'):
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_timers.name
    
    if 'EIGRP_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_timers.group(cls=FRR_AbbreviationGroup, name='active-time',)
def frr_config_router_eigrp_vrf_timers_activetime(activetime_='active-time'):
    """Time limit for active state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_timers_activetime.name
    data_gen['active-time'] = activetime_='active-time'
    
    if 'EIGRP_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_timers_activetime.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 65535), 'disabled']), invoke_without_command=True)
def frr_config_router_eigrp_vrf_timers_activetime_activetimechoicecase():
    """Active state time limit in seconds"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_timers_activetime_activetimechoicecase.name
    data_gen['ACTIVE-TIME_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'EIGRP_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_timers_activetime_activetimechoicecase.command('./	<cr>')
def frr_config_router_eigrp_vrf_timers_activetime_activetimechoicecase_cr():
    pass


@frr_config_router_eigrp_vrf.group(cls=FRR_AbbreviationGroup, name='variance', invoke_without_command=True)
@click.argument('metric_variance_multiplier', metavar='(1-128)', required=True, type=FRR_TYPE((1, 128)))
def frr_config_router_eigrp_vrf_variance(metric_variance_multiplier, variance_='variance'):
    """Control load balancing variance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_eigrp_vrf_variance.name
    data_gen['METRIC_VARIANCE_MULTIPLIER'] = metric_variance_multiplier
    
    if 'EIGRP_NODE|variance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['EIGRP_NODE|variance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['EIGRP_NODE|variance']:
            key = key.upper()
        COMMON_DATA_MAP['EIGRP_NODE|variance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['EIGRP_NODE|variance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'variance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'EIGRP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['EIGRP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_eigrp_vrf_variance.command('./	<cr>')
def frr_config_router_eigrp_vrf_variance_cr():
    pass

