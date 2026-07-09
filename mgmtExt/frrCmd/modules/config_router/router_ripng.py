import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='aggregate-address', invoke_without_command=True)
@click.argument('aggregate_network', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ripng_aggregateaddress(aggregate_network, aggregateaddress_='aggregate-address'):
    """Set aggregate RIPng route announcement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_aggregateaddress.name
    data_gen['AGGREGATE_NETWORK'] = aggregate_network
    
    if 'RIPNG_NODE|aggregate-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|aggregate-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|aggregate-address']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|aggregate-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|aggregate-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'aggregate-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_aggregateaddress.command('./	<cr>')
def frr_config_router_ripng_aggregateaddress_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='allow-ecmp', invoke_without_command=True)
def frr_config_router_ripng_allowecmp(allowecmp_='allow-ecmp'):
    """Allow Equal Cost MultiPath"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_allowecmp.name
    
    if 'RIPNG_NODE|allow-ecmp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|allow-ecmp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|allow-ecmp']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|allow-ecmp'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|allow-ecmp'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'allow-ecmp')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_allowecmp.command('./	<cr>')
def frr_config_router_ripng_allowecmp_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='default-information',)
def frr_config_router_ripng_defaultinformation(defaultinformation_='default-information'):
    """Default route information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_defaultinformation.name
    
    if 'RIPNG_NODE|default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_ripng_defaultinformation_originate(originate_='originate'):
    """Distribute default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_defaultinformation_originate.name
    data_gen['originate'] = originate_='originate'
    
    if 'RIPNG_NODE|default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_defaultinformation_originate.command('./	<cr>')
def frr_config_router_ripng_defaultinformation_originate_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='default-metric', invoke_without_command=True)
@click.argument('default_metric', metavar='(1-16)', required=True, type=FRR_TYPE((1, 16)))
def frr_config_router_ripng_defaultmetric(default_metric, defaultmetric_='default-metric'):
    """Set a metric of redistribute routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_defaultmetric.name
    data_gen['DEFAULT_METRIC'] = default_metric
    
    if 'RIPNG_NODE|default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_defaultmetric.command('./	<cr>')
def frr_config_router_ripng_defaultmetric_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_config_router_ripng_end(end_='end'):
    """End current mode and change to enable mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_end.name
    
    if 'RIPNG_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|end'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|end'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'end')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_end.command('./	<cr>')
def frr_config_router_ripng_end_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_config_router_ripng_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_exit.name
    
    if 'RIPNG_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|exit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|exit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'exit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_exit.command('./	<cr>')
def frr_config_router_ripng_exit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_config_router_ripng_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_find.name
    
    if 'RIPNG_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_config_router_ripng_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'RIPNG_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_find_fromsearchpattern.command('./	<cr>')
def frr_config_router_ripng_find_fromsearchpattern_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ipv6',)
def frr_config_router_ripng_ipv6():
    """IPv6"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_ripng_ipv6.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_ripng_ipv6_distributelist(ipv6_distributelist_='ipv6_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_ipv6_distributelist.name
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['ACCESSLIST6_NAME']),)
def frr_config_router_ripng_ipv6_distributelist_accesslistname():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_ipv6_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_ipv6_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ripng_ipv6_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_ipv6_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_ipv6_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_ripng_ipv6_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_ripng_ipv6_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_ripng_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_ripng_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ripng_ipv6_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_ipv6_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_ipv6_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ripng_ipv6_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_ipv6_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_ipv6_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_ripng_ipv6_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_ripng_ipv6_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_ipv6_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_ipv6_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_ipv6_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_ripng_ipv6_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_config_router_ripng_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_list.name
    
    if 'RIPNG_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_list.command('./	<cr>')
def frr_config_router_ripng_list_cr():
    pass


@frr_config_router_ripng_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_config_router_ripng_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'RIPNG_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_list_permutations.command('./	<cr>')
def frr_config_router_ripng_list_permutations_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='network',)
def frr_config_router_ripng_network(network_='network'):
    """RIPng enable on specified interface or network."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_network.name
    
    if 'RIPNG_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_network_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_network_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_network_interfacename.command('./	<cr>')
def frr_config_router_ripng_network_interfacename_cr():
    pass


@frr_config_router_ripng_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['X:X::X:X/M']), invoke_without_command=True)
def frr_config_router_ripng_network_ipv6network():
    """IPv6 network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_network_ipv6network.name
    data_gen['IPV6_NETWORK'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_network_ipv6network.command('./	<cr>')
def frr_config_router_ripng_network_ipv6network_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_config_router_ripng_no(no_='no'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no.name
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='aggregate-address', invoke_without_command=True)
@click.argument('aggregate_network', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ripng_no_aggregateaddress(aggregate_network, aggregateaddress_='aggregate-address'):
    """Set aggregate RIPng route announcement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_aggregateaddress.name
    data_gen['aggregate-address'] = aggregateaddress_='aggregate-address'
    data_gen['AGGREGATE_NETWORK'] = aggregate_network
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_aggregateaddress.command('./	<cr>')
def frr_config_router_ripng_no_aggregateaddress_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='allow-ecmp', invoke_without_command=True)
def frr_config_router_ripng_no_allowecmp(allowecmp_='allow-ecmp'):
    """Allow Equal Cost MultiPath"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_allowecmp.name
    data_gen['allow-ecmp'] = allowecmp_='allow-ecmp'
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_allowecmp.command('./	<cr>')
def frr_config_router_ripng_no_allowecmp_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='default-information',)
def frr_config_router_ripng_no_defaultinformation(no_defaultinformation_='no_default-information'):
    """Default route information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_defaultinformation.name
    
    if 'RIPNG_NODE|no_default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_ripng_no_defaultinformation_originate(originate_='originate'):
    """Distribute default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_defaultinformation_originate.name
    data_gen['originate'] = originate_='originate'
    
    if 'RIPNG_NODE|no_default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_defaultinformation_originate.command('./	<cr>')
def frr_config_router_ripng_no_defaultinformation_originate_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='default-metric', invoke_without_command=True)
def frr_config_router_ripng_no_defaultmetric(no_defaultmetric_='no_default-metric'):
    """Set a metric of redistribute routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_defaultmetric.name
    
    if 'RIPNG_NODE|no_default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_defaultmetric.command('./	<cr>')
def frr_config_router_ripng_no_defaultmetric_cr():
    pass


@frr_config_router_ripng_no_defaultmetric.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, [(1, 16)]), invoke_without_command=True)
def frr_config_router_ripng_no_defaultmetric_defaultmetric():
    """Default metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_defaultmetric_defaultmetric.name
    data_gen['DEFAULT_METRIC'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_defaultmetric_defaultmetric.command('./	<cr>')
def frr_config_router_ripng_no_defaultmetric_defaultmetric_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='ipv6',)
def frr_config_router_ripng_no_ipv6():
    """IPv6"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_ripng_no_ipv6.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_ripng_no_ipv6_distributelist(no_ipv6_distributelist_='no_ipv6_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_ipv6_distributelist.name
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['ACCESSLIST6_NAME']),)
def frr_config_router_ripng_no_ipv6_distributelist_accesslistname():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_ipv6_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_ipv6_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ripng_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_ripng_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_ripng_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_ripng_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_ripng_no_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ripng_no_ipv6_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_ipv6_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_ipv6_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ripng_no_ipv6_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_ipv6_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_ipv6_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_ripng_no_ipv6_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_ripng_no_ipv6_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_ripng_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='network',)
def frr_config_router_ripng_no_network(no_network_='no_network'):
    """RIPng enable on specified interface or network."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_network.name
    
    if 'RIPNG_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_no_network_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_network_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_network_interfacename.command('./	<cr>')
def frr_config_router_ripng_no_network_interfacename_cr():
    pass


@frr_config_router_ripng_no_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['X:X::X:X/M']), invoke_without_command=True)
def frr_config_router_ripng_no_network_ipv6network():
    """IPv6 network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_network_ipv6network.name
    data_gen['IPV6_NETWORK'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_network_ipv6network.command('./	<cr>')
def frr_config_router_ripng_no_network_ipv6network_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='offset-list',)
@click.argument('accesslist_name', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ripng_no_offsetlist(accesslist_name, offsetlist_='offset-list'):
    """Modify RIPng metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_offsetlist.name
    data_gen['offset-list'] = offsetlist_='offset-list'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_offsetlist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_ripng_no_offsetlist_offsetlistinoutbound(metric_value):
    """For incoming updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_offsetlist_offsetlistinoutbound.name
    data_gen['OFFSET-LIST_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_offsetlist_offsetlistinoutbound.command('./	<cr>')
def frr_config_router_ripng_no_offsetlist_offsetlistinoutbound_cr():
    pass


@frr_config_router_ripng_no_offsetlist_offsetlistinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['IFNAME']), invoke_without_command=True)
def frr_config_router_ripng_no_offsetlist_offsetlistinoutbound_interfacetomatch():
    """Interface to match"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_offsetlist_offsetlistinoutbound_interfacetomatch.name
    data_gen['INTERFACE_TO_MATCH'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_offsetlist_offsetlistinoutbound_interfacetomatch.command('./	<cr>')
def frr_config_router_ripng_no_offsetlist_offsetlistinoutbound_interfacetomatch_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_config_router_ripng_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_output.name
    
    if 'RIPNG_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_output.command('./	<cr>')
def frr_config_router_ripng_no_output_cr():
    pass


@frr_config_router_ripng_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_config_router_ripng_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_output_file.name
    
    if 'RIPNG_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_output_file.command('./	<cr>')
def frr_config_router_ripng_no_output_file_cr():
    pass


@frr_config_router_ripng_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['FILE']), invoke_without_command=True)
def frr_config_router_ripng_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_config_router_ripng_no_output_file_pathtodumpoutput_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='passive-interface', invoke_without_command=True)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_ripng_no_passiveinterface(interface_name, passiveinterface_='passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_passiveinterface.name
    data_gen['passive-interface'] = passiveinterface_='passive-interface'
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_passiveinterface.command('./	<cr>')
def frr_config_router_ripng_no_passiveinterface_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ripngd', metavar='FRR_REDIST_STR_RIPNGD', required=True, type=FRR_TYPE('FRR_REDIST_STR_RIPNGD'))
def frr_config_router_ripng_no_redistribute(frr_redist_help_str_ripngd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_redistribute.name
    data_gen['redistribute'] = redistribute_='redistribute'
    data_gen['FRR_REDIST_HELP_STR_RIPNGD'] = frr_redist_help_str_ripngd
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_redistribute.command('./	<cr>')
def frr_config_router_ripng_no_redistribute_cr():
    pass


@frr_config_router_ripng_no_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_ripng_no_redistribute_metric(metric_value, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_redistribute_metric.command('./	<cr>')
def frr_config_router_ripng_no_redistribute_metric_cr():
    pass


@frr_config_router_ripng_no_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ripng_no_redistribute_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_redistribute_routemap.command('./	<cr>')
def frr_config_router_ripng_no_redistribute_routemap_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
@click.argument('set_static_ripng_route', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ripng_no_route(set_static_ripng_route, route_='route'):
    """Static route setup"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_route.name
    data_gen['route'] = route_='route'
    data_gen['SET_STATIC_RIPNG_ROUTE'] = set_static_ripng_route
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_route.command('./	<cr>')
def frr_config_router_ripng_no_route_cr():
    pass


@frr_config_router_ripng_no.group(cls=FRR_AbbreviationGroup, name='timers', invoke_without_command=True)
def frr_config_router_ripng_no_timers():
    """RIPng timers setup"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_timers.name
    
    if 'RIPNG_NODE|no_timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_timers.command('./	<cr>')
def frr_config_router_ripng_no_timers_cr():
    pass


@frr_config_router_ripng_no_timers.group(cls=FRR_AbbreviationGroup, name='basic', invoke_without_command=True)
def frr_config_router_ripng_no_timers_basic(no_timers_basic_='no_timers_basic'):
    """Basic timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_timers_basic.name
    
    if 'RIPNG_NODE|no_timers_basic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_basic')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_timers_basic.command('./	<cr>')
def frr_config_router_ripng_no_timers_basic_cr():
    pass


@frr_config_router_ripng_no_timers_basic.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 65535)]), invoke_without_command=True)
@click.argument('routing_information_timeout_timer', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
@click.argument('garbage_collection_timer_default', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
def frr_config_router_ripng_no_timers_basic_routingtableupdatetimer(routing_information_timeout_timer, garbage_collection_timer_default):
    """Routing table update timer value in second. Default is 30."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_no_timers_basic_routingtableupdatetimer.name
    data_gen['ROUTING_TABLE_UPDATE_TIMER'] = FRR_CLI_ARGS[name]
    data_gen['ROUTING_INFORMATION_TIMEOUT_TIMER'] = routing_information_timeout_timer
    data_gen['GARBAGE_COLLECTION_TIMER_DEFAULT'] = garbage_collection_timer_default
    
    if 'RIPNG_NODE|no_timers_basic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_basic')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_no_timers_basic_routingtableupdatetimer.command('./	<cr>')
def frr_config_router_ripng_no_timers_basic_routingtableupdatetimer_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='offset-list',)
@click.argument('accesslist_name', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ripng_offsetlist(accesslist_name, offsetlist_='offset-list'):
    """Modify RIPng metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_offsetlist.name
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIPNG_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_offsetlist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['in', 'out']), invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_ripng_offsetlist_offsetlistinoutbound(metric_value):
    """For incoming updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_offsetlist_offsetlistinoutbound.name
    data_gen['OFFSET-LIST_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIPNG_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_offsetlist_offsetlistinoutbound.command('./	<cr>')
def frr_config_router_ripng_offsetlist_offsetlistinoutbound_cr():
    pass


@frr_config_router_ripng_offsetlist_offsetlistinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['IFNAME']), invoke_without_command=True)
def frr_config_router_ripng_offsetlist_offsetlistinoutbound_interfacetomatch():
    """Interface to match"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_offsetlist_offsetlistinoutbound_interfacetomatch.name
    data_gen['INTERFACE_TO_MATCH'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_offsetlist_offsetlistinoutbound_interfacetomatch.command('./	<cr>')
def frr_config_router_ripng_offsetlist_offsetlistinoutbound_interfacetomatch_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_config_router_ripng_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_output.name
    
    if 'RIPNG_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_config_router_ripng_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'RIPNG_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_output_file.command('./	<cr>')
def frr_config_router_ripng_output_file_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='passive-interface', invoke_without_command=True)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_ripng_passiveinterface(interface_name, passiveinterface_='passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_passiveinterface.name
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'RIPNG_NODE|passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_passiveinterface.command('./	<cr>')
def frr_config_router_ripng_passiveinterface_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_config_router_ripng_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_quit.name
    
    if 'RIPNG_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|quit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|quit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'quit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_quit.command('./	<cr>')
def frr_config_router_ripng_quit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ripngd', metavar='FRR_REDIST_STR_RIPNGD', required=True, type=FRR_TYPE('FRR_REDIST_STR_RIPNGD'))
def frr_config_router_ripng_redistribute(frr_redist_help_str_ripngd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_redistribute.name
    data_gen['FRR_REDIST_HELP_STR_RIPNGD'] = frr_redist_help_str_ripngd
    
    if 'RIPNG_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_redistribute.command('./	<cr>')
def frr_config_router_ripng_redistribute_cr():
    pass


@frr_config_router_ripng_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_ripng_redistribute_metric(metric_value, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIPNG_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_redistribute_metric.command('./	<cr>')
def frr_config_router_ripng_redistribute_metric_cr():
    pass


@frr_config_router_ripng_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ripng_redistribute_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'RIPNG_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_redistribute_routemap.command('./	<cr>')
def frr_config_router_ripng_redistribute_routemap_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
@click.argument('set_static_ripng_route', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ripng_route(set_static_ripng_route, route_='route'):
    """Static route setup"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_route.name
    data_gen['SET_STATIC_RIPNG_ROUTE'] = set_static_ripng_route
    
    if 'RIPNG_NODE|route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|route']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|route'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|route'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'route')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_route.command('./	<cr>')
def frr_config_router_ripng_route_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='timers',)
def frr_config_router_ripng_timers(timers_='timers'):
    """RIPng timers setup"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_timers.name
    
    if 'RIPNG_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_timers.group(cls=FRR_AbbreviationGroup, name='basic', invoke_without_command=True)
@click.argument('routing_table_update_timer', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
@click.argument('routing_information_timeout_timer', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
@click.argument('garbage_collection_timer_default', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
def frr_config_router_ripng_timers_basic(garbage_collection_timer_default, routing_table_update_timer, routing_information_timeout_timer, basic_='basic'):
    """Basic timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_timers_basic.name
    data_gen['basic'] = basic_='basic'
    data_gen['ROUTING_TABLE_UPDATE_TIMER'] = routing_table_update_timer
    data_gen['ROUTING_INFORMATION_TIMEOUT_TIMER'] = routing_information_timeout_timer
    data_gen['GARBAGE_COLLECTION_TIMER_DEFAULT'] = garbage_collection_timer_default
    
    if 'RIPNG_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_timers_basic.command('./	<cr>')
def frr_config_router_ripng_timers_basic_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_config_router_ripng_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'CONFIG_NODE|router_ripng' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['CONFIG_NODE|router_ripng'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['CONFIG_NODE|router_ripng']:
            key = key.upper()
        COMMON_DATA_MAP['CONFIG_NODE|router_ripng'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['CONFIG_NODE|router_ripng'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'router_ripng')
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


@frr_config_router_ripng_vrf.command('./	<cr>')
def frr_config_router_ripng_vrf_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='aggregate-address', invoke_without_command=True)
@click.argument('aggregate_network', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ripng_vrf_aggregateaddress(aggregate_network, aggregateaddress_='aggregate-address'):
    """Set aggregate RIPng route announcement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_aggregateaddress.name
    data_gen['AGGREGATE_NETWORK'] = aggregate_network
    
    if 'RIPNG_NODE|aggregate-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|aggregate-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|aggregate-address']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|aggregate-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|aggregate-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'aggregate-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_aggregateaddress.command('./	<cr>')
def frr_config_router_ripng_vrf_aggregateaddress_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='allow-ecmp', invoke_without_command=True)
def frr_config_router_ripng_vrf_allowecmp(allowecmp_='allow-ecmp'):
    """Allow Equal Cost MultiPath"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_allowecmp.name
    
    if 'RIPNG_NODE|allow-ecmp' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|allow-ecmp'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|allow-ecmp']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|allow-ecmp'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|allow-ecmp'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'allow-ecmp')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_allowecmp.command('./	<cr>')
def frr_config_router_ripng_vrf_allowecmp_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='default-information',)
def frr_config_router_ripng_vrf_defaultinformation(defaultinformation_='default-information'):
    """Default route information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_defaultinformation.name
    
    if 'RIPNG_NODE|default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_ripng_vrf_defaultinformation_originate(originate_='originate'):
    """Distribute default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_defaultinformation_originate.name
    data_gen['originate'] = originate_='originate'
    
    if 'RIPNG_NODE|default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_defaultinformation_originate.command('./	<cr>')
def frr_config_router_ripng_vrf_defaultinformation_originate_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='default-metric', invoke_without_command=True)
@click.argument('default_metric', metavar='(1-16)', required=True, type=FRR_TYPE((1, 16)))
def frr_config_router_ripng_vrf_defaultmetric(default_metric, defaultmetric_='default-metric'):
    """Set a metric of redistribute routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_defaultmetric.name
    data_gen['DEFAULT_METRIC'] = default_metric
    
    if 'RIPNG_NODE|default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_defaultmetric.command('./	<cr>')
def frr_config_router_ripng_vrf_defaultmetric_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_config_router_ripng_vrf_end(end_='end'):
    """End current mode and change to enable mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_end.name
    
    if 'RIPNG_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|end'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|end'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'end')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_end.command('./	<cr>')
def frr_config_router_ripng_vrf_end_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_config_router_ripng_vrf_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_exit.name
    
    if 'RIPNG_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|exit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|exit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'exit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_exit.command('./	<cr>')
def frr_config_router_ripng_vrf_exit_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_config_router_ripng_vrf_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_find.name
    
    if 'RIPNG_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_config_router_ripng_vrf_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'RIPNG_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_find_fromsearchpattern.command('./	<cr>')
def frr_config_router_ripng_vrf_find_fromsearchpattern_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='ipv6',)
def frr_config_router_ripng_vrf_ipv6():
    """IPv6"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_ripng_vrf_ipv6.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_ripng_vrf_ipv6_distributelist(ipv6_distributelist_='ipv6_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_ipv6_distributelist.name
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['ACCESSLIST6_NAME']),)
def frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_ripng_vrf_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_ripng_vrf_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ripng_vrf_ipv6_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_ipv6_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_ipv6_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ripng_vrf_ipv6_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_ipv6_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_ipv6_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_ripng_vrf_ipv6_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_ripng_vrf_ipv6_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_vrf_ipv6_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_ipv6_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_ipv6_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_ripng_vrf_ipv6_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_config_router_ripng_vrf_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_list.name
    
    if 'RIPNG_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_list.command('./	<cr>')
def frr_config_router_ripng_vrf_list_cr():
    pass


@frr_config_router_ripng_vrf_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_config_router_ripng_vrf_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'RIPNG_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_list_permutations.command('./	<cr>')
def frr_config_router_ripng_vrf_list_permutations_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='network',)
def frr_config_router_ripng_vrf_network(network_='network'):
    """RIPng enable on specified interface or network."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_network.name
    
    if 'RIPNG_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_vrf_network_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_network_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_network_interfacename.command('./	<cr>')
def frr_config_router_ripng_vrf_network_interfacename_cr():
    pass


@frr_config_router_ripng_vrf_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['X:X::X:X/M']), invoke_without_command=True)
def frr_config_router_ripng_vrf_network_ipv6network():
    """IPv6 network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_network_ipv6network.name
    data_gen['IPV6_NETWORK'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_network_ipv6network.command('./	<cr>')
def frr_config_router_ripng_vrf_network_ipv6network_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_config_router_ripng_vrf_no(no_='no'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no.name
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='aggregate-address', invoke_without_command=True)
@click.argument('aggregate_network', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ripng_vrf_no_aggregateaddress(aggregate_network, aggregateaddress_='aggregate-address'):
    """Set aggregate RIPng route announcement"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_aggregateaddress.name
    data_gen['aggregate-address'] = aggregateaddress_='aggregate-address'
    data_gen['AGGREGATE_NETWORK'] = aggregate_network
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_aggregateaddress.command('./	<cr>')
def frr_config_router_ripng_vrf_no_aggregateaddress_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='allow-ecmp', invoke_without_command=True)
def frr_config_router_ripng_vrf_no_allowecmp(allowecmp_='allow-ecmp'):
    """Allow Equal Cost MultiPath"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_allowecmp.name
    data_gen['allow-ecmp'] = allowecmp_='allow-ecmp'
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_allowecmp.command('./	<cr>')
def frr_config_router_ripng_vrf_no_allowecmp_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='default-information',)
def frr_config_router_ripng_vrf_no_defaultinformation(no_defaultinformation_='no_default-information'):
    """Default route information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_defaultinformation.name
    
    if 'RIPNG_NODE|no_default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_ripng_vrf_no_defaultinformation_originate(originate_='originate'):
    """Distribute default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_defaultinformation_originate.name
    data_gen['originate'] = originate_='originate'
    
    if 'RIPNG_NODE|no_default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_default-information']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_defaultinformation_originate.command('./	<cr>')
def frr_config_router_ripng_vrf_no_defaultinformation_originate_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='default-metric', invoke_without_command=True)
def frr_config_router_ripng_vrf_no_defaultmetric(no_defaultmetric_='no_default-metric'):
    """Set a metric of redistribute routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_defaultmetric.name
    
    if 'RIPNG_NODE|no_default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_defaultmetric.command('./	<cr>')
def frr_config_router_ripng_vrf_no_defaultmetric_cr():
    pass


@frr_config_router_ripng_vrf_no_defaultmetric.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 16)]), invoke_without_command=True)
def frr_config_router_ripng_vrf_no_defaultmetric_defaultmetric():
    """Default metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_defaultmetric_defaultmetric.name
    data_gen['DEFAULT_METRIC'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_default-metric' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_default-metric']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_default-metric'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-metric')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_defaultmetric_defaultmetric.command('./	<cr>')
def frr_config_router_ripng_vrf_no_defaultmetric_defaultmetric_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='ipv6',)
def frr_config_router_ripng_vrf_no_ipv6():
    """IPv6"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_ripng_vrf_no_ipv6.group(cls=FRR_AbbreviationGroup, name='distribute-list',)
def frr_config_router_ripng_vrf_no_ipv6_distributelist(no_ipv6_distributelist_='no_ipv6_distribute-list'):
    """Filter networks in routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_ipv6_distributelist.name
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['ACCESSLIST6_NAME']),)
def frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname():
    """7"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname.name
    data_gen['ACCESS-LIST_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound.name
    data_gen['ACCESS-LIST-NAME_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound.command('./	<cr>')
def frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_cr():
    pass


@frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename.command('./	<cr>')
def frr_config_router_ripng_vrf_no_ipv6_distributelist_accesslistname_accesslistnameinoutbound_interfacename_cr():
    pass


@frr_config_router_ripng_vrf_no_ipv6_distributelist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('accesslist_name', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix(accesslist_name, prefix_='prefix'):
    """Specify a prefix"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix.name
    data_gen['prefix'] = prefix_='prefix'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix_prefixinoutbound():
    """Filter incoming routing updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix_prefixinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_ipv6_distribute-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_ipv6_distribute-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ipv6_distribute-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename.command('./	<cr>')
def frr_config_router_ripng_vrf_no_ipv6_distributelist_prefix_prefixinoutbound_interfacename_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='network',)
def frr_config_router_ripng_vrf_no_network(no_network_='no_network'):
    """RIPng enable on specified interface or network."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_network.name
    
    if 'RIPNG_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['WORD']), invoke_without_command=True)
def frr_config_router_ripng_vrf_no_network_interfacename():
    """Interface name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_network_interfacename.name
    data_gen['INTERFACE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_network_interfacename.command('./	<cr>')
def frr_config_router_ripng_vrf_no_network_interfacename_cr():
    pass


@frr_config_router_ripng_vrf_no_network.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['X:X::X:X/M']), invoke_without_command=True)
def frr_config_router_ripng_vrf_no_network_ipv6network():
    """IPv6 network"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_network_ipv6network.name
    data_gen['IPV6_NETWORK'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_network' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_network'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_network']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_network'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_network'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_network')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_network_ipv6network.command('./	<cr>')
def frr_config_router_ripng_vrf_no_network_ipv6network_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='offset-list',)
@click.argument('accesslist_name', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ripng_vrf_no_offsetlist(accesslist_name, offsetlist_='offset-list'):
    """Modify RIPng metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_offsetlist.name
    data_gen['offset-list'] = offsetlist_='offset-list'
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_offsetlist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['in', 'out']), invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_ripng_vrf_no_offsetlist_offsetlistinoutbound(metric_value):
    """For incoming updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_offsetlist_offsetlistinoutbound.name
    data_gen['OFFSET-LIST_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_offsetlist_offsetlistinoutbound.command('./	<cr>')
def frr_config_router_ripng_vrf_no_offsetlist_offsetlistinoutbound_cr():
    pass


@frr_config_router_ripng_vrf_no_offsetlist_offsetlistinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['IFNAME']), invoke_without_command=True)
def frr_config_router_ripng_vrf_no_offsetlist_offsetlistinoutbound_interfacetomatch():
    """Interface to match"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_offsetlist_offsetlistinoutbound_interfacetomatch.name
    data_gen['INTERFACE_TO_MATCH'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_offsetlist_offsetlistinoutbound_interfacetomatch.command('./	<cr>')
def frr_config_router_ripng_vrf_no_offsetlist_offsetlistinoutbound_interfacetomatch_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_config_router_ripng_vrf_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_output.name
    
    if 'RIPNG_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_output.command('./	<cr>')
def frr_config_router_ripng_vrf_no_output_cr():
    pass


@frr_config_router_ripng_vrf_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_config_router_ripng_vrf_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_output_file.name
    
    if 'RIPNG_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_output_file.command('./	<cr>')
def frr_config_router_ripng_vrf_no_output_file_cr():
    pass


@frr_config_router_ripng_vrf_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['FILE']), invoke_without_command=True)
def frr_config_router_ripng_vrf_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_config_router_ripng_vrf_no_output_file_pathtodumpoutput_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='passive-interface', invoke_without_command=True)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_ripng_vrf_no_passiveinterface(interface_name, passiveinterface_='passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_passiveinterface.name
    data_gen['passive-interface'] = passiveinterface_='passive-interface'
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_passiveinterface.command('./	<cr>')
def frr_config_router_ripng_vrf_no_passiveinterface_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ripngd', metavar='FRR_REDIST_STR_RIPNGD', required=True, type=FRR_TYPE('FRR_REDIST_STR_RIPNGD'))
def frr_config_router_ripng_vrf_no_redistribute(frr_redist_help_str_ripngd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_redistribute.name
    data_gen['redistribute'] = redistribute_='redistribute'
    data_gen['FRR_REDIST_HELP_STR_RIPNGD'] = frr_redist_help_str_ripngd
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_redistribute.command('./	<cr>')
def frr_config_router_ripng_vrf_no_redistribute_cr():
    pass


@frr_config_router_ripng_vrf_no_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_ripng_vrf_no_redistribute_metric(metric_value, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_redistribute_metric.command('./	<cr>')
def frr_config_router_ripng_vrf_no_redistribute_metric_cr():
    pass


@frr_config_router_ripng_vrf_no_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ripng_vrf_no_redistribute_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_redistribute_routemap.command('./	<cr>')
def frr_config_router_ripng_vrf_no_redistribute_routemap_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
@click.argument('set_static_ripng_route', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ripng_vrf_no_route(set_static_ripng_route, route_='route'):
    """Static route setup"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_route.name
    data_gen['route'] = route_='route'
    data_gen['SET_STATIC_RIPNG_ROUTE'] = set_static_ripng_route
    
    if 'RIPNG_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_route.command('./	<cr>')
def frr_config_router_ripng_vrf_no_route_cr():
    pass


@frr_config_router_ripng_vrf_no.group(cls=FRR_AbbreviationGroup, name='timers', invoke_without_command=True)
def frr_config_router_ripng_vrf_no_timers():
    """RIPng timers setup"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_timers.name
    
    if 'RIPNG_NODE|no_timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_timers.command('./	<cr>')
def frr_config_router_ripng_vrf_no_timers_cr():
    pass


@frr_config_router_ripng_vrf_no_timers.group(cls=FRR_AbbreviationGroup, name='basic', invoke_without_command=True)
def frr_config_router_ripng_vrf_no_timers_basic(no_timers_basic_='no_timers_basic'):
    """Basic timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_timers_basic.name
    
    if 'RIPNG_NODE|no_timers_basic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_basic')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_timers_basic.command('./	<cr>')
def frr_config_router_ripng_vrf_no_timers_basic_cr():
    pass


@frr_config_router_ripng_vrf_no_timers_basic.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(1, 65535)]), invoke_without_command=True)
@click.argument('routing_information_timeout_timer', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
@click.argument('garbage_collection_timer_default', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
def frr_config_router_ripng_vrf_no_timers_basic_routingtableupdatetimer(routing_information_timeout_timer, garbage_collection_timer_default):
    """Routing table update timer value in second. Default is 30."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_no_timers_basic_routingtableupdatetimer.name
    data_gen['ROUTING_TABLE_UPDATE_TIMER'] = FRR_CLI_ARGS[name]
    data_gen['ROUTING_INFORMATION_TIMEOUT_TIMER'] = routing_information_timeout_timer
    data_gen['GARBAGE_COLLECTION_TIMER_DEFAULT'] = garbage_collection_timer_default
    
    if 'RIPNG_NODE|no_timers_basic' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|no_timers_basic'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_basic')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_no_timers_basic_routingtableupdatetimer.command('./	<cr>')
def frr_config_router_ripng_vrf_no_timers_basic_routingtableupdatetimer_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='offset-list',)
@click.argument('accesslist_name', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ripng_vrf_offsetlist(accesslist_name, offsetlist_='offset-list'):
    """Modify RIPng metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_offsetlist.name
    data_gen['ACCESS-LIST_NAME'] = accesslist_name
    
    if 'RIPNG_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_offsetlist.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['in', 'out']), invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_ripng_vrf_offsetlist_offsetlistinoutbound(metric_value):
    """For incoming updates"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_offsetlist_offsetlistinoutbound.name
    data_gen['OFFSET-LIST_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIPNG_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_offsetlist_offsetlistinoutbound.command('./	<cr>')
def frr_config_router_ripng_vrf_offsetlist_offsetlistinoutbound_cr():
    pass


@frr_config_router_ripng_vrf_offsetlist_offsetlistinoutbound.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['IFNAME']), invoke_without_command=True)
def frr_config_router_ripng_vrf_offsetlist_offsetlistinoutbound_interfacetomatch():
    """Interface to match"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_offsetlist_offsetlistinoutbound_interfacetomatch.name
    data_gen['INTERFACE_TO_MATCH'] = FRR_CLI_ARGS[name]
    
    if 'RIPNG_NODE|offset-list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|offset-list']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|offset-list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|offset-list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'offset-list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_offsetlist_offsetlistinoutbound_interfacetomatch.command('./	<cr>')
def frr_config_router_ripng_vrf_offsetlist_offsetlistinoutbound_interfacetomatch_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_config_router_ripng_vrf_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_output.name
    
    if 'RIPNG_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_config_router_ripng_vrf_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'RIPNG_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_output_file.command('./	<cr>')
def frr_config_router_ripng_vrf_output_file_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='passive-interface', invoke_without_command=True)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_ripng_vrf_passiveinterface(interface_name, passiveinterface_='passive-interface'):
    """Suppress routing updates on an interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_passiveinterface.name
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'RIPNG_NODE|passive-interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|passive-interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|passive-interface']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|passive-interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|passive-interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'passive-interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_passiveinterface.command('./	<cr>')
def frr_config_router_ripng_vrf_passiveinterface_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_config_router_ripng_vrf_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_quit.name
    
    if 'RIPNG_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|quit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|quit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'quit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_quit.command('./	<cr>')
def frr_config_router_ripng_vrf_quit_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ripngd', metavar='FRR_REDIST_STR_RIPNGD', required=True, type=FRR_TYPE('FRR_REDIST_STR_RIPNGD'))
def frr_config_router_ripng_vrf_redistribute(frr_redist_help_str_ripngd, redistribute_='redistribute'):
    """REDIST_STR"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_redistribute.name
    data_gen['FRR_REDIST_HELP_STR_RIPNGD'] = frr_redist_help_str_ripngd
    
    if 'RIPNG_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_redistribute.command('./	<cr>')
def frr_config_router_ripng_vrf_redistribute_cr():
    pass


@frr_config_router_ripng_vrf_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('metric_value', metavar='(0-16)', required=True, type=FRR_TYPE((0, 16)))
def frr_config_router_ripng_vrf_redistribute_metric(metric_value, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['METRIC_VALUE'] = metric_value
    
    if 'RIPNG_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_redistribute_metric.command('./	<cr>')
def frr_config_router_ripng_vrf_redistribute_metric_cr():
    pass


@frr_config_router_ripng_vrf_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ripng_vrf_redistribute_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'RIPNG_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_redistribute_routemap.command('./	<cr>')
def frr_config_router_ripng_vrf_redistribute_routemap_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='route', invoke_without_command=True)
@click.argument('set_static_ripng_route', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ripng_vrf_route(set_static_ripng_route, route_='route'):
    """Static route setup"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_route.name
    data_gen['SET_STATIC_RIPNG_ROUTE'] = set_static_ripng_route
    
    if 'RIPNG_NODE|route' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|route'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|route']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|route'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|route'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'route')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_route.command('./	<cr>')
def frr_config_router_ripng_vrf_route_cr():
    pass


@frr_config_router_ripng_vrf.group(cls=FRR_AbbreviationGroup, name='timers',)
def frr_config_router_ripng_vrf_timers(timers_='timers'):
    """RIPng timers setup"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_timers.name
    
    if 'RIPNG_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_timers.group(cls=FRR_AbbreviationGroup, name='basic', invoke_without_command=True)
@click.argument('routing_table_update_timer', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
@click.argument('routing_information_timeout_timer', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
@click.argument('garbage_collection_timer_default', metavar='(1-65535)', required=True, type=FRR_TYPE((1, 65535)))
def frr_config_router_ripng_vrf_timers_basic(garbage_collection_timer_default, routing_table_update_timer, routing_information_timeout_timer, basic_='basic'):
    """Basic timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ripng_vrf_timers_basic.name
    data_gen['basic'] = basic_='basic'
    data_gen['ROUTING_TABLE_UPDATE_TIMER'] = routing_table_update_timer
    data_gen['ROUTING_INFORMATION_TIMEOUT_TIMER'] = routing_information_timeout_timer
    data_gen['GARBAGE_COLLECTION_TIMER_DEFAULT'] = garbage_collection_timer_default
    
    if 'RIPNG_NODE|timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['RIPNG_NODE|timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['RIPNG_NODE|timers']:
            key = key.upper()
        COMMON_DATA_MAP['RIPNG_NODE|timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['RIPNG_NODE|timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'RIPNG_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['RIPNG_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ripng_vrf_timers_basic.command('./	<cr>')
def frr_config_router_ripng_vrf_timers_basic_cr():
    pass

