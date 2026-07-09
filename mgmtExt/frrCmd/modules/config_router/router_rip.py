import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='allow-ecmp', invoke_without_command=True)
def frr_config_router_rip_allowecmp(allowecmp_='allow-ecmp'):
    """Allow Equal Cost MultiPath"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_allowecmp.name
    
    if 'RIP_NODE|allow-ecmp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|allow-ecmp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|allow-ecmp']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|allow-ecmp'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|allow-ecmp'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'allow-ecmp')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_allowecmp.command('./	<cr>')
def frr_config_router_rip_allowecmp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='default-information',)
def frr_config_router_rip_defaultinformation(defaultinformation_='default-information'):
    """Control distribution of default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_defaultinformation.name
    
    if 'RIP_NODE|default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_rip_defaultinformation_originate(originate_='originate'):
    """Distribute a default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_defaultinformation_originate.name
    data_gen['originate'] = originate_='originate'
    
    if 'RIP_NODE|default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_defaultinformation_originate.command('./	<cr>')
def frr_config_router_rip_defaultinformation_originate_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='default-metric', invoke_without_command=True)
@click.argument('default_metric', metavar='(1-16)', required=True, type=FRR_TYPE((1, 16)))
def frr_config_router_rip_defaultmetric(default_metric, defaultmetric_='default-metric'):
    """Set a metric of redistribute routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_defaultmetric.name
    data_gen['DEFAULT_METRIC'] = default_metric
    
    if 'RIP_NODE|default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_defaultmetric.command('./	<cr>')
def frr_config_router_rip_defaultmetric_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='distance', invoke_without_command=True)
@click.argument('distance_value', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_rip_distance(distance_value, distance_='distance'):
    """Administrative distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_distance.name
    data_gen['DISTANCE_VALUE'] = distance_value
    
    if 'RIP_NODE|distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_distance.command('./	<cr>')
def frr_config_router_rip_distance_cr():
    pass


@frr_config_router_rip_distance.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D/M']), invoke_without_command=True)
def frr_config_router_rip_distance_ipprefix():
    """IP source prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_distance_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_distance_ipprefix.command('./	<cr>')
def frr_config_router_rip_distance_ipprefix_cr():
    pass


@frr_config_router_rip_distance_ipprefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_distance_ipprefix_accesslistname():
    """Access list name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_distance_ipprefix_accesslistname.name
    data_gen['ACCESS_LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_distance_ipprefix_accesslistname.command('./	<cr>')
def frr_config_router_rip_distance_ipprefix_accesslistname_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_rip_distributelist(distributelist_='distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_distributelist.name
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['ACCESSLIST4_NAME']),)
def frr_config_router_rip_distributelist_accesslistname():
    """4"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
def frr_config_router_rip_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_rip_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_rip_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_rip_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_rip_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST4_NAME', required=True, type=FRR_TYPE('ACCESSLIST4_NAME'))
def frr_config_router_rip_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
def frr_config_router_rip_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_rip_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_rip_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_rip_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_config_router_rip_end(end_='end'):
    """End current mode and change to enable mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_end.name
    
    if 'RIP_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|end'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|end'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'end')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_end.command('./	<cr>')
def frr_config_router_rip_end_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_config_router_rip_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_exit.name
    
    if 'RIP_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|exit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|exit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'exit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_exit.command('./	<cr>')
def frr_config_router_rip_exit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_config_router_rip_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_find.name
    
    if 'RIP_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_config_router_rip_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'RIP_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_find_fromsearchpattern.command('./	<cr>')
def frr_config_router_rip_find_fromsearchpattern_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_config_router_rip_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_list.name
    
    if 'RIP_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_list.command('./	<cr>')
def frr_config_router_rip_list_cr():
    pass


@frr_config_router_rip_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_config_router_rip_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'RIP_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_list_permutations.command('./	<cr>')
def frr_config_router_rip_list_permutations_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_rip_neighbor(neighbor_address, neighbor_='neighbor'):
    """Specify a neighbor router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_neighbor.name
    data_gen['NEIGHBOR_ADDRESS'] = neighbor_address
    
    if 'RIP_NODE|neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|neighbor'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|neighbor'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'neighbor')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_neighbor.command('./	<cr>')
def frr_config_router_rip_neighbor_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='network',)
def frr_config_router_rip_network(network_='network'):
    """Enable routing on an IP network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_network.name
    
    if 'RIP_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_network_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_network_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_network_interfacename.command('./	<cr>')
def frr_config_router_rip_network_interfacename_cr():
    pass


@frr_config_router_rip_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D/M']), invoke_without_command=True)
def frr_config_router_rip_network_ipprefix():
    """IP prefix <network>/<length>, e.g., 35.0.0.0/8"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_network_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_network_ipprefix.command('./	<cr>')
def frr_config_router_rip_network_ipprefix_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_config_router_rip_no(no_='no'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no.name
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='allow-ecmp', invoke_without_command=True)
def frr_config_router_rip_no_allowecmp(allowecmp_='allow-ecmp'):
    """Allow Equal Cost MultiPath"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_allowecmp.name
    data_gen['allow-ecmp'] = allowecmp_='allow-ecmp'
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_allowecmp.command('./	<cr>')
def frr_config_router_rip_no_allowecmp_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='default-information',)
def frr_config_router_rip_no_defaultinformation(no_defaultinformation_='no_default-information'):
    """Control distribution of default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_defaultinformation.name
    
    if 'RIP_NODE|no_default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_rip_no_defaultinformation_originate(originate_='originate'):
    """Distribute a default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_defaultinformation_originate.name
    data_gen['originate'] = originate_='originate'
    
    if 'RIP_NODE|no_default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_defaultinformation_originate.command('./	<cr>')
def frr_config_router_rip_no_defaultinformation_originate_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='default-metric', invoke_without_command=True)
def frr_config_router_rip_no_defaultmetric(no_defaultmetric_='no_default-metric'):
    """Set a metric of redistribute routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_defaultmetric.name
    
    if 'RIP_NODE|no_default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_defaultmetric.command('./	<cr>')
def frr_config_router_rip_no_defaultmetric_cr():
    pass


@frr_config_router_rip_no_defaultmetric.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, [(1, 16)]), invoke_without_command=True)
def frr_config_router_rip_no_defaultmetric_defaultmetric():
    """Default metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_defaultmetric_defaultmetric.name
    data_gen['DEFAULT_METRIC'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_defaultmetric_defaultmetric.command('./	<cr>')
def frr_config_router_rip_no_defaultmetric_defaultmetric_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='distance', invoke_without_command=True)
def frr_config_router_rip_no_distance(no_distance_='no_distance'):
    """Administrative distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distance.name
    
    if 'RIP_NODE|no_distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distance.command('./	<cr>')
def frr_config_router_rip_no_distance_cr():
    pass


@frr_config_router_rip_no_distance.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, [(1, 255)]), invoke_without_command=True)
def frr_config_router_rip_no_distance_distancevalue():
    """Distance value"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distance_distancevalue.name
    data_gen['DISTANCE_VALUE'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distance_distancevalue.command('./	<cr>')
def frr_config_router_rip_no_distance_distancevalue_cr():
    pass


@frr_config_router_rip_no_distance_distancevalue.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D/M']), invoke_without_command=True)
def frr_config_router_rip_no_distance_distancevalue_ipprefix():
    """IP source prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distance_distancevalue_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distance_distancevalue_ipprefix.command('./	<cr>')
def frr_config_router_rip_no_distance_distancevalue_ipprefix_cr():
    pass


@frr_config_router_rip_no_distance_distancevalue_ipprefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_no_distance_distancevalue_ipprefix_accesslistname():
    """Access list name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distance_distancevalue_ipprefix_accesslistname.name
    data_gen['ACCESS_LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distance_distancevalue_ipprefix_accesslistname.command('./	<cr>')
def frr_config_router_rip_no_distance_distancevalue_ipprefix_accesslistname_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_rip_no_distributelist(no_distributelist_='no_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distributelist.name
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['ACCESSLIST4_NAME']),)
def frr_config_router_rip_no_distributelist_accesslistname():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_rip_no_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_rip_no_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_rip_no_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_rip_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_rip_no_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST4_NAME', required=True, type=FRR_TYPE('ACCESSLIST4_NAME'))
def frr_config_router_rip_no_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_rip_no_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_rip_no_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_rip_no_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_no_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_rip_no_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_rip_no_neighbor(neighbor_address, neighbor_='neighbor'):
    """Specify a neighbor router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    data_gen['NEIGHBOR_ADDRESS'] = neighbor_address
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_neighbor.command('./	<cr>')
def frr_config_router_rip_no_neighbor_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='network',)
def frr_config_router_rip_no_network(no_network_='no_network'):
    """Enable routing on an IP network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_network.name
    
    if 'RIP_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_no_network_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_network_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_network_interfacename.command('./	<cr>')
def frr_config_router_rip_no_network_interfacename_cr():
    pass


@frr_config_router_rip_no_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D/M']), invoke_without_command=True)
def frr_config_router_rip_no_network_ipprefix():
    """IP prefix <network>/<length>, e.g., 35.0.0.0/8"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_network_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_network_ipprefix.command('./	<cr>')
def frr_config_router_rip_no_network_ipprefix_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='offset-list',)
@click.argument('accesslist_name', metavar='ACCESSLIST4_NAME', required=True, type=FRR_TYPE('ACCESSLIST4_NAME'))
def frr_config_router_rip_no_offsetlist(accesslist_name, offsetlist_='offset-list'):
    """Modify RIP metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_offsetlist.name
    data_gen['offset-list'] = offsetlist_='offset-list'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_offsetlist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_rip_no_offsetlist_offsetlistinoutbound(metric_value):
    """For incoming updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_offsetlist_offsetlistinoutbound.name
    data_gen['OFFSET-LIST_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_offsetlist_offsetlistinoutbound.command('./	<cr>')
def frr_config_router_rip_no_offsetlist_offsetlistinoutbound_cr():
    pass


@frr_config_router_rip_no_offsetlist_offsetlistinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['IFNAME']), invoke_without_command=True)
def frr_config_router_rip_no_offsetlist_offsetlistinoutbound_interfacetomatch():
    """Interface to match"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_offsetlist_offsetlistinoutbound_interfacetomatch.name
    data_gen['INTERFACE_TO_MATCH'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_offsetlist_offsetlistinoutbound_interfacetomatch.command('./	<cr>')
def frr_config_router_rip_no_offsetlist_offsetlistinoutbound_interfacetomatch_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_config_router_rip_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_output.name
    
    if 'RIP_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_output.command('./	<cr>')
def frr_config_router_rip_no_output_cr():
    pass


@frr_config_router_rip_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_config_router_rip_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_output_file.name
    
    if 'RIP_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_output_file.command('./	<cr>')
def frr_config_router_rip_no_output_file_cr():
    pass


@frr_config_router_rip_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['FILE']), invoke_without_command=True)
def frr_config_router_rip_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_config_router_rip_no_output_file_pathtodumpoutput_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='passive-interface',)
def frr_config_router_rip_no_passiveinterface(no_passiveinterface_='no_passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_passiveinterface.name
    
    if 'RIP_NODE|no_passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_passiveinterface.group(cls=FRR_AbbreviationGroup, name='default', invoke_without_command=True)
def frr_config_router_rip_no_passiveinterface_default(default_='default'):
    """default for all interfaces"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_passiveinterface_default.name
    data_gen['default'] = default_='default'
    
    if 'RIP_NODE|no_passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_passiveinterface_default.command('./	<cr>')
def frr_config_router_rip_no_passiveinterface_default_cr():
    pass


@frr_config_router_rip_no_passiveinterface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['IFNAME']), invoke_without_command=True)
def frr_config_router_rip_no_passiveinterface_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_passiveinterface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_passiveinterface_interfacename.command('./	<cr>')
def frr_config_router_rip_no_passiveinterface_interfacename_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ripd', metavar='FRR_REDIST_STR_RIPD', required=True, type=FRR_TYPE('FRR_REDIST_STR_RIPD'))
def frr_config_router_rip_no_redistribute(frr_redist_help_str_ripd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_redistribute.name
    data_gen['redistribute'] = redistribute_='redistribute'
    data_gen['FRR_REDIST_HELP_STR_RIPD'] = frr_redist_help_str_ripd
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_redistribute.command('./	<cr>')
def frr_config_router_rip_no_redistribute_cr():
    pass


@frr_config_router_rip_no_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_rip_no_redistribute_metric(metric_value, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_redistribute_metric.command('./	<cr>')
def frr_config_router_rip_no_redistribute_metric_cr():
    pass


@frr_config_router_rip_no_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_rip_no_redistribute_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_redistribute_routemap.command('./	<cr>')
def frr_config_router_rip_no_redistribute_routemap_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
@click.argument('ip_prefix', metavar='A.B.C.D/M', required=True, type=FRR_TYPE('A.B.C.D/M'))
def frr_config_router_rip_no_route(ip_prefix, route_='route'):
    """RIP static route configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_route.name
    data_gen['route'] = route_='route'
    data_gen['IP_PREFIX'] = ip_prefix
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_route.command('./	<cr>')
def frr_config_router_rip_no_route_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='route-map',)
@click.argument('route_map_name', metavar='ROUTEMAP_NAME', required=True, type=FRR_TYPE('ROUTEMAP_NAME'))
def frr_config_router_rip_no_routemap(route_map_name, routemap_='route-map'):
    """Route map unset"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['ROUTE_MAP_NAME'] = route_map_name
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_routemap.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
@click.argument('route_map_interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_rip_no_routemap_routemapinoutbound(route_map_interface_name):
    """Route map for input filtering"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_routemap_routemapinoutbound.name
    data_gen['ROUTE-MAP_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['ROUTE_MAP_INTERFACE_NAME'] = route_map_interface_name
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_routemap_routemapinoutbound.command('./	<cr>')
def frr_config_router_rip_no_routemap_routemapinoutbound_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='timers', invoke_without_command=True)
def frr_config_router_rip_no_timers():
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_timers.name
    
    if 'RIP_NODE|no_timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_timers.command('./	<cr>')
def frr_config_router_rip_no_timers_cr():
    pass


@frr_config_router_rip_no_timers.group(cls=FRR_AbbreviationGroup, name='basic', invoke_without_command=True)
def frr_config_router_rip_no_timers_basic(no_timers_basic_='no_timers_basic'):
    """Basic routing protocol update timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_timers_basic.name
    
    if 'RIP_NODE|no_timers_basic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_timers_basic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_timers_basic']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_timers_basic'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_timers_basic'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_basic')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_timers_basic.command('./	<cr>')
def frr_config_router_rip_no_timers_basic_cr():
    pass


@frr_config_router_rip_no_timers_basic.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(5, 2147483647)]), invoke_without_command=True)
@click.argument('routing_information_timeout_timer', metavar='(5-2147483647)', required=True, type=FRR_TYPE((5, 2147483647)))
@click.argument('garbage_collection_timer_default', metavar='(5-2147483647)', required=True, type=FRR_TYPE((5, 2147483647)))
def frr_config_router_rip_no_timers_basic_routingtableupdatetimer(routing_information_timeout_timer, garbage_collection_timer_default):
    """Routing table update timer value in second. Default is 30."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_timers_basic_routingtableupdatetimer.name
    data_gen['ROUTING_TABLE_UPDATE_TIMER'] = FRR_CLI_ARGS[name]
    data_gen['ROUTING_INFORMATION_TIMEOUT_TIMER'] = routing_information_timeout_timer
    data_gen['GARBAGE_COLLECTION_TIMER_DEFAULT'] = garbage_collection_timer_default
    
    if 'RIP_NODE|no_timers_basic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_timers_basic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_timers_basic']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_timers_basic'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_timers_basic'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_basic')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_timers_basic_routingtableupdatetimer.command('./	<cr>')
def frr_config_router_rip_no_timers_basic_routingtableupdatetimer_cr():
    pass


@frr_config_router_rip_no.group(cls=FRR_AbbreviationGroup, name='version', invoke_without_command=True)
def frr_config_router_rip_no_version(no_version_='no_version'):
    """Set routing protocol version"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_version.name
    
    if 'RIP_NODE|no_version' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_version'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_version']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_version'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_version'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_version')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_version.command('./	<cr>')
def frr_config_router_rip_no_version_cr():
    pass


@frr_config_router_rip_no_version.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, [(1, 2)]), invoke_without_command=True)
def frr_config_router_rip_no_version_version():
    """version"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_no_version_version.name
    data_gen['VERSION'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_version' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_version'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_version']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_version'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_version'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_version')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_no_version_version.command('./	<cr>')
def frr_config_router_rip_no_version_version_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='offset-list',)
@click.argument('accesslist_name', metavar='ACCESSLIST4_NAME', required=True, type=FRR_TYPE('ACCESSLIST4_NAME'))
def frr_config_router_rip_offsetlist(accesslist_name, offsetlist_='offset-list'):
    """Modify RIP metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_offsetlist.name
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIP_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_offsetlist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['in', 'out']), invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_rip_offsetlist_offsetlistinoutbound(metric_value):
    """For incoming updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_offsetlist_offsetlistinoutbound.name
    data_gen['OFFSET-LIST_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIP_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_offsetlist_offsetlistinoutbound.command('./	<cr>')
def frr_config_router_rip_offsetlist_offsetlistinoutbound_cr():
    pass


@frr_config_router_rip_offsetlist_offsetlistinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['IFNAME']), invoke_without_command=True)
def frr_config_router_rip_offsetlist_offsetlistinoutbound_interfacetomatch():
    """Interface to match"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_offsetlist_offsetlistinoutbound_interfacetomatch.name
    data_gen['INTERFACE_TO_MATCH'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_offsetlist_offsetlistinoutbound_interfacetomatch.command('./	<cr>')
def frr_config_router_rip_offsetlist_offsetlistinoutbound_interfacetomatch_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_config_router_rip_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_output.name
    
    if 'RIP_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_config_router_rip_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'RIP_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_output_file.command('./	<cr>')
def frr_config_router_rip_output_file_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='passive-interface',)
def frr_config_router_rip_passiveinterface(passiveinterface_='passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_passiveinterface.name
    
    if 'RIP_NODE|passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_passiveinterface.group(cls=FRR_AbbreviationGroup, name='default', invoke_without_command=True)
def frr_config_router_rip_passiveinterface_default(default_='default'):
    """default for all interfaces"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_passiveinterface_default.name
    data_gen['default'] = default_='default'
    
    if 'RIP_NODE|passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_passiveinterface_default.command('./	<cr>')
def frr_config_router_rip_passiveinterface_default_cr():
    pass


@frr_config_router_rip_passiveinterface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['IFNAME']), invoke_without_command=True)
def frr_config_router_rip_passiveinterface_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_passiveinterface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_passiveinterface_interfacename.command('./	<cr>')
def frr_config_router_rip_passiveinterface_interfacename_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_config_router_rip_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_quit.name
    
    if 'RIP_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|quit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|quit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'quit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_quit.command('./	<cr>')
def frr_config_router_rip_quit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ripd', metavar='FRR_REDIST_STR_RIPD', required=True, type=FRR_TYPE('FRR_REDIST_STR_RIPD'))
def frr_config_router_rip_redistribute(frr_redist_help_str_ripd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_redistribute.name
    data_gen['FRR_REDIST_HELP_STR_RIPD'] = frr_redist_help_str_ripd
    
    if 'RIP_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_redistribute.command('./	<cr>')
def frr_config_router_rip_redistribute_cr():
    pass


@frr_config_router_rip_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_rip_redistribute_metric(metric_value, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIP_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_redistribute_metric.command('./	<cr>')
def frr_config_router_rip_redistribute_metric_cr():
    pass


@frr_config_router_rip_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_rip_redistribute_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'RIP_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_redistribute_routemap.command('./	<cr>')
def frr_config_router_rip_redistribute_routemap_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
@click.argument('ip_prefix', metavar='A.B.C.D/M', required=True, type=FRR_TYPE('A.B.C.D/M'))
def frr_config_router_rip_route(ip_prefix, route_='route'):
    """RIP static route configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_route.name
    data_gen['IP_PREFIX'] = ip_prefix
    
    if 'RIP_NODE|route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|route']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|route'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|route'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'route')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_route.command('./	<cr>')
def frr_config_router_rip_route_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='route-map',)
@click.argument('route_map_name', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_rip_routemap(route_map_name, routemap_='route-map'):
    """Route map set"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_routemap.name
    data_gen['ROUTE_MAP_NAME'] = route_map_name
    
    if 'RIP_NODE|route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|route-map']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|route-map'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|route-map'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'route-map')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_routemap.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['in', 'out']), invoke_without_command=True)
@click.argument('route_map_interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_rip_routemap_routemapinoutbound(route_map_interface_name):
    """Route map set for input filtering"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_routemap_routemapinoutbound.name
    data_gen['ROUTE-MAP_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['ROUTE_MAP_INTERFACE_NAME'] = route_map_interface_name
    
    if 'RIP_NODE|route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|route-map']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|route-map'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|route-map'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'route-map')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_routemap_routemapinoutbound.command('./	<cr>')
def frr_config_router_rip_routemap_routemapinoutbound_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='timers',)
def frr_config_router_rip_timers(timers_='timers'):
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_timers.name
    
    if 'RIP_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_timers.group(cls=FRR_AbbreviationGroup, name='basic', invoke_without_command=True)
@click.argument('routing_table_update_timer', metavar='(5-2147483647)', required=True, type=FRR_TYPE((5, 2147483647)))
@click.argument('routing_information_timeout_timer', metavar='(5-2147483647)', required=True, type=FRR_TYPE((5, 2147483647)))
@click.argument('garbage_collection_timer_default', metavar='(5-2147483647)', required=True, type=FRR_TYPE((5, 2147483647)))
def frr_config_router_rip_timers_basic(garbage_collection_timer_default, routing_table_update_timer, routing_information_timeout_timer, basic_='basic'):
    """Basic routing protocol update timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_timers_basic.name
    data_gen['basic'] = basic_='basic'
    data_gen['ROUTING_TABLE_UPDATE_TIMER'] = routing_table_update_timer
    data_gen['ROUTING_INFORMATION_TIMEOUT_TIMER'] = routing_information_timeout_timer
    data_gen['GARBAGE_COLLECTION_TIMER_DEFAULT'] = garbage_collection_timer_default
    
    if 'RIP_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_timers_basic.command('./	<cr>')
def frr_config_router_rip_timers_basic_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='version', invoke_without_command=True)
@click.argument('version', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_rip_version(version, version_='version'):
    """Set routing protocol version"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_version.name
    data_gen['VERSION'] = version
    
    if 'RIP_NODE|version' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|version'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|version']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|version'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|version'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'version')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_version.command('./	<cr>')
def frr_config_router_rip_version_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_config_router_rip_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'CONFIG_NODE|router_rip' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['CONFIG_NODE|router_rip'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['CONFIG_NODE|router_rip']:
            key = key.upper()
        COMMON_DATA_MAP['CONFIG_NODE|router_rip'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['CONFIG_NODE|router_rip'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'router_rip')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'CONFIG_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['CONFIG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf.command('./	<cr>')
def frr_config_router_rip_vrf_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='allow-ecmp', invoke_without_command=True)
def frr_config_router_rip_vrf_allowecmp(allowecmp_='allow-ecmp'):
    """Allow Equal Cost MultiPath"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_allowecmp.name
    
    if 'RIP_NODE|allow-ecmp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|allow-ecmp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|allow-ecmp']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|allow-ecmp'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|allow-ecmp'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'allow-ecmp')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_allowecmp.command('./	<cr>')
def frr_config_router_rip_vrf_allowecmp_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='default-information',)
def frr_config_router_rip_vrf_defaultinformation(defaultinformation_='default-information'):
    """Control distribution of default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_defaultinformation.name
    
    if 'RIP_NODE|default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_rip_vrf_defaultinformation_originate(originate_='originate'):
    """Distribute a default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_defaultinformation_originate.name
    data_gen['originate'] = originate_='originate'
    
    if 'RIP_NODE|default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_defaultinformation_originate.command('./	<cr>')
def frr_config_router_rip_vrf_defaultinformation_originate_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='default-metric', invoke_without_command=True)
@click.argument('default_metric', metavar='(1-16)', required=True, type=FRR_TYPE((1, 16)))
def frr_config_router_rip_vrf_defaultmetric(default_metric, defaultmetric_='default-metric'):
    """Set a metric of redistribute routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_defaultmetric.name
    data_gen['DEFAULT_METRIC'] = default_metric
    
    if 'RIP_NODE|default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_defaultmetric.command('./	<cr>')
def frr_config_router_rip_vrf_defaultmetric_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='distance', invoke_without_command=True)
@click.argument('distance_value', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_rip_vrf_distance(distance_value, distance_='distance'):
    """Administrative distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_distance.name
    data_gen['DISTANCE_VALUE'] = distance_value
    
    if 'RIP_NODE|distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_distance.command('./	<cr>')
def frr_config_router_rip_vrf_distance_cr():
    pass


@frr_config_router_rip_vrf_distance.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D/M']), invoke_without_command=True)
def frr_config_router_rip_vrf_distance_ipprefix():
    """IP source prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_distance_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_distance_ipprefix.command('./	<cr>')
def frr_config_router_rip_vrf_distance_ipprefix_cr():
    pass


@frr_config_router_rip_vrf_distance_ipprefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_vrf_distance_ipprefix_accesslistname():
    """Access list name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_distance_ipprefix_accesslistname.name
    data_gen['ACCESS_LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_distance_ipprefix_accesslistname.command('./	<cr>')
def frr_config_router_rip_vrf_distance_ipprefix_accesslistname_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_rip_vrf_distributelist(distributelist_='distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_distributelist.name
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['ACCESSLIST4_NAME']),)
def frr_config_router_rip_vrf_distributelist_accesslistname():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_rip_vrf_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_rip_vrf_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_rip_vrf_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_vrf_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_rip_vrf_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_rip_vrf_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST4_NAME', required=True, type=FRR_TYPE('ACCESSLIST4_NAME'))
def frr_config_router_rip_vrf_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_rip_vrf_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_rip_vrf_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_rip_vrf_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_vrf_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_rip_vrf_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_config_router_rip_vrf_end(end_='end'):
    """End current mode and change to enable mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_end.name
    
    if 'RIP_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|end'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|end'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'end')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_end.command('./	<cr>')
def frr_config_router_rip_vrf_end_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_config_router_rip_vrf_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_exit.name
    
    if 'RIP_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|exit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|exit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'exit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_exit.command('./	<cr>')
def frr_config_router_rip_vrf_exit_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_config_router_rip_vrf_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_find.name
    
    if 'RIP_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_config_router_rip_vrf_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'RIP_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_find_fromsearchpattern.command('./	<cr>')
def frr_config_router_rip_vrf_find_fromsearchpattern_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_config_router_rip_vrf_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_list.name
    
    if 'RIP_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_list.command('./	<cr>')
def frr_config_router_rip_vrf_list_cr():
    pass


@frr_config_router_rip_vrf_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_config_router_rip_vrf_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'RIP_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_list_permutations.command('./	<cr>')
def frr_config_router_rip_vrf_list_permutations_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_rip_vrf_neighbor(neighbor_address, neighbor_='neighbor'):
    """Specify a neighbor router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_neighbor.name
    data_gen['NEIGHBOR_ADDRESS'] = neighbor_address
    
    if 'RIP_NODE|neighbor' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|neighbor'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|neighbor']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|neighbor'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|neighbor'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'neighbor')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_neighbor.command('./	<cr>')
def frr_config_router_rip_vrf_neighbor_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='network',)
def frr_config_router_rip_vrf_network(network_='network'):
    """Enable routing on an IP network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_network.name
    
    if 'RIP_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_vrf_network_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_network_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_network_interfacename.command('./	<cr>')
def frr_config_router_rip_vrf_network_interfacename_cr():
    pass


@frr_config_router_rip_vrf_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D/M']), invoke_without_command=True)
def frr_config_router_rip_vrf_network_ipprefix():
    """IP prefix <network>/<length>, e.g., 35.0.0.0/8"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_network_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_network_ipprefix.command('./	<cr>')
def frr_config_router_rip_vrf_network_ipprefix_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_config_router_rip_vrf_no(no_='no'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no.name
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='allow-ecmp', invoke_without_command=True)
def frr_config_router_rip_vrf_no_allowecmp(allowecmp_='allow-ecmp'):
    """Allow Equal Cost MultiPath"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_allowecmp.name
    data_gen['allow-ecmp'] = allowecmp_='allow-ecmp'
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_allowecmp.command('./	<cr>')
def frr_config_router_rip_vrf_no_allowecmp_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='default-information',)
def frr_config_router_rip_vrf_no_defaultinformation(no_defaultinformation_='no_default-information'):
    """Control distribution of default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_defaultinformation.name
    
    if 'RIP_NODE|no_default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_rip_vrf_no_defaultinformation_originate(originate_='originate'):
    """Distribute a default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_defaultinformation_originate.name
    data_gen['originate'] = originate_='originate'
    
    if 'RIP_NODE|no_default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_defaultinformation_originate.command('./	<cr>')
def frr_config_router_rip_vrf_no_defaultinformation_originate_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='default-metric', invoke_without_command=True)
def frr_config_router_rip_vrf_no_defaultmetric(no_defaultmetric_='no_default-metric'):
    """Set a metric of redistribute routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_defaultmetric.name
    
    if 'RIP_NODE|no_default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_defaultmetric.command('./	<cr>')
def frr_config_router_rip_vrf_no_defaultmetric_cr():
    pass


@frr_config_router_rip_vrf_no_defaultmetric.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 16)]), invoke_without_command=True)
def frr_config_router_rip_vrf_no_defaultmetric_defaultmetric():
    """Default metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_defaultmetric_defaultmetric.name
    data_gen['DEFAULT_METRIC'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_defaultmetric_defaultmetric.command('./	<cr>')
def frr_config_router_rip_vrf_no_defaultmetric_defaultmetric_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='distance', invoke_without_command=True)
def frr_config_router_rip_vrf_no_distance(no_distance_='no_distance'):
    """Administrative distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distance.name
    
    if 'RIP_NODE|no_distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distance.command('./	<cr>')
def frr_config_router_rip_vrf_no_distance_cr():
    pass


@frr_config_router_rip_vrf_no_distance.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 255)]), invoke_without_command=True)
def frr_config_router_rip_vrf_no_distance_distancevalue():
    """Distance value"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distance_distancevalue.name
    data_gen['DISTANCE_VALUE'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distance_distancevalue.command('./	<cr>')
def frr_config_router_rip_vrf_no_distance_distancevalue_cr():
    pass


@frr_config_router_rip_vrf_no_distance_distancevalue.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['A.B.C.D/M']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_distance_distancevalue_ipprefix():
    """IP source prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distance_distancevalue_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distance_distancevalue_ipprefix.command('./	<cr>')
def frr_config_router_rip_vrf_no_distance_distancevalue_ipprefix_cr():
    pass


@frr_config_router_rip_vrf_no_distance_distancevalue_ipprefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_distance_distancevalue_ipprefix_accesslistname():
    """Access list name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distance_distancevalue_ipprefix_accesslistname.name
    data_gen['ACCESS_LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distance']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distance_distancevalue_ipprefix_accesslistname.command('./	<cr>')
def frr_config_router_rip_vrf_no_distance_distancevalue_ipprefix_accesslistname_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_rip_vrf_no_distributelist(no_distributelist_='no_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distributelist.name
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['ACCESSLIST4_NAME']),)
def frr_config_router_rip_vrf_no_distributelist_accesslistname():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_rip_vrf_no_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_rip_vrf_no_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_rip_vrf_no_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_rip_vrf_no_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST4_NAME', required=True, type=FRR_TYPE('ACCESSLIST4_NAME'))
def frr_config_router_rip_vrf_no_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_rip_vrf_no_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_rip_vrf_no_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_rip_vrf_no_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='neighbor', invoke_without_command=True)
@click.argument('neighbor_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_rip_vrf_no_neighbor(neighbor_address, neighbor_='neighbor'):
    """Specify a neighbor router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_neighbor.name
    data_gen['neighbor'] = neighbor_='neighbor'
    data_gen['NEIGHBOR_ADDRESS'] = neighbor_address
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_neighbor.command('./	<cr>')
def frr_config_router_rip_vrf_no_neighbor_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='network',)
def frr_config_router_rip_vrf_no_network(no_network_='no_network'):
    """Enable routing on an IP network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_network.name
    
    if 'RIP_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['WORD']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_network_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_network_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_network_interfacename.command('./	<cr>')
def frr_config_router_rip_vrf_no_network_interfacename_cr():
    pass


@frr_config_router_rip_vrf_no_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D/M']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_network_ipprefix():
    """IP prefix <network>/<length>, e.g., 35.0.0.0/8"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_network_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_network_ipprefix.command('./	<cr>')
def frr_config_router_rip_vrf_no_network_ipprefix_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='offset-list',)
@click.argument('accesslist_name', metavar='ACCESSLIST4_NAME', required=True, type=FRR_TYPE('ACCESSLIST4_NAME'))
def frr_config_router_rip_vrf_no_offsetlist(accesslist_name, offsetlist_='offset-list'):
    """Modify RIP metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_offsetlist.name
    data_gen['offset-list'] = offsetlist_='offset-list'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_offsetlist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_rip_vrf_no_offsetlist_offsetlistinoutbound(metric_value):
    """For incoming updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_offsetlist_offsetlistinoutbound.name
    data_gen['OFFSET-LIST_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_offsetlist_offsetlistinoutbound.command('./	<cr>')
def frr_config_router_rip_vrf_no_offsetlist_offsetlistinoutbound_cr():
    pass


@frr_config_router_rip_vrf_no_offsetlist_offsetlistinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['IFNAME']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_offsetlist_offsetlistinoutbound_interfacetomatch():
    """Interface to match"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_offsetlist_offsetlistinoutbound_interfacetomatch.name
    data_gen['INTERFACE_TO_MATCH'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_offsetlist_offsetlistinoutbound_interfacetomatch.command('./	<cr>')
def frr_config_router_rip_vrf_no_offsetlist_offsetlistinoutbound_interfacetomatch_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_config_router_rip_vrf_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_output.name
    
    if 'RIP_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_output.command('./	<cr>')
def frr_config_router_rip_vrf_no_output_cr():
    pass


@frr_config_router_rip_vrf_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_config_router_rip_vrf_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_output_file.name
    
    if 'RIP_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_output_file.command('./	<cr>')
def frr_config_router_rip_vrf_no_output_file_cr():
    pass


@frr_config_router_rip_vrf_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['FILE']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_config_router_rip_vrf_no_output_file_pathtodumpoutput_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='passive-interface',)
def frr_config_router_rip_vrf_no_passiveinterface(no_passiveinterface_='no_passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_passiveinterface.name
    
    if 'RIP_NODE|no_passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_passiveinterface.group(cls=FRR_AbbreviationGroup, name='default', invoke_without_command=True)
def frr_config_router_rip_vrf_no_passiveinterface_default(default_='default'):
    """default for all interfaces"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_passiveinterface_default.name
    data_gen['default'] = default_='default'
    
    if 'RIP_NODE|no_passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_passiveinterface_default.command('./	<cr>')
def frr_config_router_rip_vrf_no_passiveinterface_default_cr():
    pass


@frr_config_router_rip_vrf_no_passiveinterface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['IFNAME']), invoke_without_command=True)
def frr_config_router_rip_vrf_no_passiveinterface_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_passiveinterface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_passiveinterface_interfacename.command('./	<cr>')
def frr_config_router_rip_vrf_no_passiveinterface_interfacename_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ripd', metavar='FRR_REDIST_STR_RIPD', required=True, type=FRR_TYPE('FRR_REDIST_STR_RIPD'))
def frr_config_router_rip_vrf_no_redistribute(frr_redist_help_str_ripd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_redistribute.name
    data_gen['redistribute'] = redistribute_='redistribute'
    data_gen['FRR_REDIST_HELP_STR_RIPD'] = frr_redist_help_str_ripd
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_redistribute.command('./	<cr>')
def frr_config_router_rip_vrf_no_redistribute_cr():
    pass


@frr_config_router_rip_vrf_no_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_rip_vrf_no_redistribute_metric(metric_value, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_redistribute_metric.command('./	<cr>')
def frr_config_router_rip_vrf_no_redistribute_metric_cr():
    pass


@frr_config_router_rip_vrf_no_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_rip_vrf_no_redistribute_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_redistribute_routemap.command('./	<cr>')
def frr_config_router_rip_vrf_no_redistribute_routemap_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
@click.argument('ip_prefix', metavar='A.B.C.D/M', required=True, type=FRR_TYPE('A.B.C.D/M'))
def frr_config_router_rip_vrf_no_route(ip_prefix, route_='route'):
    """RIP static route configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_route.name
    data_gen['route'] = route_='route'
    data_gen['IP_PREFIX'] = ip_prefix
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_route.command('./	<cr>')
def frr_config_router_rip_vrf_no_route_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='route-map',)
@click.argument('route_map_name', metavar='ROUTEMAP_NAME', required=True, type=FRR_TYPE('ROUTEMAP_NAME'))
def frr_config_router_rip_vrf_no_routemap(route_map_name, routemap_='route-map'):
    """Route map unset"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['ROUTE_MAP_NAME'] = route_map_name
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_routemap.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
@click.argument('route_map_interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_rip_vrf_no_routemap_routemapinoutbound(route_map_interface_name):
    """Route map for input filtering"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_routemap_routemapinoutbound.name
    data_gen['ROUTE-MAP_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['ROUTE_MAP_INTERFACE_NAME'] = route_map_interface_name
    
    if 'RIP_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_routemap_routemapinoutbound.command('./	<cr>')
def frr_config_router_rip_vrf_no_routemap_routemapinoutbound_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='timers', invoke_without_command=True)
def frr_config_router_rip_vrf_no_timers():
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_timers.name
    
    if 'RIP_NODE|no_timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_timers.command('./	<cr>')
def frr_config_router_rip_vrf_no_timers_cr():
    pass


@frr_config_router_rip_vrf_no_timers.group(cls=FRR_AbbreviationGroup, name='basic', invoke_without_command=True)
def frr_config_router_rip_vrf_no_timers_basic(no_timers_basic_='no_timers_basic'):
    """Basic routing protocol update timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_timers_basic.name
    
    if 'RIP_NODE|no_timers_basic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_timers_basic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_timers_basic']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_timers_basic'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_timers_basic'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_basic')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_timers_basic.command('./	<cr>')
def frr_config_router_rip_vrf_no_timers_basic_cr():
    pass


@frr_config_router_rip_vrf_no_timers_basic.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(5, 2147483647)]), invoke_without_command=True)
@click.argument('routing_information_timeout_timer', metavar='(5-2147483647)', required=True, type=FRR_TYPE((5, 2147483647)))
@click.argument('garbage_collection_timer_default', metavar='(5-2147483647)', required=True, type=FRR_TYPE((5, 2147483647)))
def frr_config_router_rip_vrf_no_timers_basic_routingtableupdatetimer(routing_information_timeout_timer, garbage_collection_timer_default):
    """Routing table update timer value in second. Default is 30."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_timers_basic_routingtableupdatetimer.name
    data_gen['ROUTING_TABLE_UPDATE_TIMER'] = FRR_CLI_ARGS[name]
    data_gen['ROUTING_INFORMATION_TIMEOUT_TIMER'] = routing_information_timeout_timer
    data_gen['GARBAGE_COLLECTION_TIMER_DEFAULT'] = garbage_collection_timer_default
    
    if 'RIP_NODE|no_timers_basic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_timers_basic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_timers_basic']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_timers_basic'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_timers_basic'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_basic')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_timers_basic_routingtableupdatetimer.command('./	<cr>')
def frr_config_router_rip_vrf_no_timers_basic_routingtableupdatetimer_cr():
    pass


@frr_config_router_rip_vrf_no.group(cls=FRR_AbbreviationGroup, name='version', invoke_without_command=True)
def frr_config_router_rip_vrf_no_version(no_version_='no_version'):
    """Set routing protocol version"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_version.name
    
    if 'RIP_NODE|no_version' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_version'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_version']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_version'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_version'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_version')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_version.command('./	<cr>')
def frr_config_router_rip_vrf_no_version_cr():
    pass


@frr_config_router_rip_vrf_no_version.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 2)]), invoke_without_command=True)
def frr_config_router_rip_vrf_no_version_version():
    """version"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_no_version_version.name
    data_gen['VERSION'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|no_version' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|no_version'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|no_version']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|no_version'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|no_version'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_version')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_no_version_version.command('./	<cr>')
def frr_config_router_rip_vrf_no_version_version_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='offset-list',)
@click.argument('accesslist_name', metavar='ACCESSLIST4_NAME', required=True, type=FRR_TYPE('ACCESSLIST4_NAME'))
def frr_config_router_rip_vrf_offsetlist(accesslist_name, offsetlist_='offset-list'):
    """Modify RIP metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_offsetlist.name
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIP_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_offsetlist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_rip_vrf_offsetlist_offsetlistinoutbound(metric_value):
    """For incoming updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_offsetlist_offsetlistinoutbound.name
    data_gen['OFFSET-LIST_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIP_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_offsetlist_offsetlistinoutbound.command('./	<cr>')
def frr_config_router_rip_vrf_offsetlist_offsetlistinoutbound_cr():
    pass


@frr_config_router_rip_vrf_offsetlist_offsetlistinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['IFNAME']), invoke_without_command=True)
def frr_config_router_rip_vrf_offsetlist_offsetlistinoutbound_interfacetomatch():
    """Interface to match"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_offsetlist_offsetlistinoutbound_interfacetomatch.name
    data_gen['INTERFACE_TO_MATCH'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_offsetlist_offsetlistinoutbound_interfacetomatch.command('./	<cr>')
def frr_config_router_rip_vrf_offsetlist_offsetlistinoutbound_interfacetomatch_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_config_router_rip_vrf_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_output.name
    
    if 'RIP_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_config_router_rip_vrf_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'RIP_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_output_file.command('./	<cr>')
def frr_config_router_rip_vrf_output_file_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='passive-interface',)
def frr_config_router_rip_vrf_passiveinterface(passiveinterface_='passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_passiveinterface.name
    
    if 'RIP_NODE|passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_passiveinterface.group(cls=FRR_AbbreviationGroup, name='default', invoke_without_command=True)
def frr_config_router_rip_vrf_passiveinterface_default(default_='default'):
    """default for all interfaces"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_passiveinterface_default.name
    data_gen['default'] = default_='default'
    
    if 'RIP_NODE|passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_passiveinterface_default.command('./	<cr>')
def frr_config_router_rip_vrf_passiveinterface_default_cr():
    pass


@frr_config_router_rip_vrf_passiveinterface.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['IFNAME']), invoke_without_command=True)
def frr_config_router_rip_vrf_passiveinterface_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_passiveinterface_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIP_NODE|passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_passiveinterface_interfacename.command('./	<cr>')
def frr_config_router_rip_vrf_passiveinterface_interfacename_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_config_router_rip_vrf_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_quit.name
    
    if 'RIP_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|quit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|quit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'quit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_quit.command('./	<cr>')
def frr_config_router_rip_vrf_quit_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ripd', metavar='FRR_REDIST_STR_RIPD', required=True, type=FRR_TYPE('FRR_REDIST_STR_RIPD'))
def frr_config_router_rip_vrf_redistribute(frr_redist_help_str_ripd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_redistribute.name
    data_gen['FRR_REDIST_HELP_STR_RIPD'] = frr_redist_help_str_ripd
    
    if 'RIP_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_redistribute.command('./	<cr>')
def frr_config_router_rip_vrf_redistribute_cr():
    pass


@frr_config_router_rip_vrf_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_rip_vrf_redistribute_metric(metric_value, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIP_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_redistribute_metric.command('./	<cr>')
def frr_config_router_rip_vrf_redistribute_metric_cr():
    pass


@frr_config_router_rip_vrf_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_rip_vrf_redistribute_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'RIP_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_redistribute_routemap.command('./	<cr>')
def frr_config_router_rip_vrf_redistribute_routemap_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
@click.argument('ip_prefix', metavar='A.B.C.D/M', required=True, type=FRR_TYPE('A.B.C.D/M'))
def frr_config_router_rip_vrf_route(ip_prefix, route_='route'):
    """RIP static route configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_route.name
    data_gen['IP_PREFIX'] = ip_prefix
    
    if 'RIP_NODE|route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|route']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|route'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|route'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'route')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_route.command('./	<cr>')
def frr_config_router_rip_vrf_route_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='route-map',)
@click.argument('route_map_name', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_rip_vrf_routemap(route_map_name, routemap_='route-map'):
    """Route map set"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_routemap.name
    data_gen['ROUTE_MAP_NAME'] = route_map_name
    
    if 'RIP_NODE|route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|route-map']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|route-map'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|route-map'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'route-map')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_routemap.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
@click.argument('route_map_interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_rip_vrf_routemap_routemapinoutbound(route_map_interface_name):
    """Route map set for input filtering"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_routemap_routemapinoutbound.name
    data_gen['ROUTE-MAP_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['ROUTE_MAP_INTERFACE_NAME'] = route_map_interface_name
    
    if 'RIP_NODE|route-map' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|route-map'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|route-map']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|route-map'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|route-map'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'route-map')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_routemap_routemapinoutbound.command('./	<cr>')
def frr_config_router_rip_vrf_routemap_routemapinoutbound_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='timers',)
def frr_config_router_rip_vrf_timers(timers_='timers'):
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_timers.name
    
    if 'RIP_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_timers.group(cls=FRR_AbbreviationGroup, name='basic', invoke_without_command=True)
@click.argument('routing_table_update_timer', metavar='(5-2147483647)', required=True, type=FRR_TYPE((5, 2147483647)))
@click.argument('routing_information_timeout_timer', metavar='(5-2147483647)', required=True, type=FRR_TYPE((5, 2147483647)))
@click.argument('garbage_collection_timer_default', metavar='(5-2147483647)', required=True, type=FRR_TYPE((5, 2147483647)))
def frr_config_router_rip_vrf_timers_basic(garbage_collection_timer_default, routing_table_update_timer, routing_information_timeout_timer, basic_='basic'):
    """Basic routing protocol update timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_timers_basic.name
    data_gen['basic'] = basic_='basic'
    data_gen['ROUTING_TABLE_UPDATE_TIMER'] = routing_table_update_timer
    data_gen['ROUTING_INFORMATION_TIMEOUT_TIMER'] = routing_information_timeout_timer
    data_gen['GARBAGE_COLLECTION_TIMER_DEFAULT'] = garbage_collection_timer_default
    
    if 'RIP_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_timers_basic.command('./	<cr>')
def frr_config_router_rip_vrf_timers_basic_cr():
    pass


@frr_config_router_rip_vrf.group(cls=FRR_AbbreviationGroup, name='version', invoke_without_command=True)
@click.argument('version', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_rip_vrf_version(version, version_='version'):
    """Set routing protocol version"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_rip_vrf_version.name
    data_gen['VERSION'] = version
    
    if 'RIP_NODE|version' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIP_NODE|version'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIP_NODE|version']:
            key = key.upper()
        COMMON_DATA_MAP['RIP_NODE|version'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIP_NODE|version'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'version')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIP_NODE' not in BASE_NODE:
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
    
    COMMON_DATA_MAP['RIP_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_rip_vrf_version.command('./	<cr>')
def frr_config_router_rip_vrf_version_cr():
    pass

