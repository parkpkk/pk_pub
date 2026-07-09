import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='aggregation',)
def frr_config_router_ospf6_aggregation(aggregation_='aggregation'):
    """External route aggregation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_aggregation.name
    
    if 'OSPF6_NODE|aggregation' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|aggregation'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|aggregation']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|aggregation'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|aggregation'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'aggregation')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_aggregation.group(cls=FRR_AbbreviationGroup, name='timer', invoke_without_command=True)
@click.argument('timer_interval', metavar='(5-1800)', required=True, type=FRR_TYPE((5, 1800)))
def frr_config_router_ospf6_aggregation_timer(timer_interval, timer_='timer'):
    """Delay timer (in seconds)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_aggregation_timer.name
    data_gen['timer'] = timer_='timer'
    data_gen['TIMER_INTERVAL'] = timer_interval
    
    if 'OSPF6_NODE|aggregation' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|aggregation'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|aggregation']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|aggregation'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|aggregation'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'aggregation')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_aggregation_timer.command('./	<cr>')
def frr_config_router_ospf6_aggregation_timer_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='area',)
def frr_config_router_ospf6_area(area_='area'):
    """OSPF6 stub parameters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area.name
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D', (0, 4294967295)]),)
def frr_config_router_ospf6_area_areachoicecase():
    """4"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase.name
    data_gen['AREA_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='export-list', invoke_without_command=True)
@click.argument('name_of_the_accesslist', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ospf6_area_areachoicecase_exportlist(name_of_the_accesslist, exportlist_='export-list'):
    """Set the filter for networks announced to other areas"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_exportlist.name
    data_gen['export-list'] = exportlist_='export-list'
    data_gen['NAME_OF_THE_ACCESS-LIST'] = name_of_the_accesslist
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_exportlist.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_exportlist_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='filter-list',)
def frr_config_router_ospf6_area_areachoicecase_filterlist():
    """Filter prefixes between OSPF6 areas"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_ospf6_area_areachoicecase_filterlist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('name_of_an_ipv6', metavar='PREFIXLIST_NAME', required=True, type=FRR_TYPE('PREFIXLIST_NAME'))
def frr_config_router_ospf6_area_areachoicecase_filterlist_prefix(name_of_an_ipv6, filterlist_prefix_='filter-list_prefix'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_filterlist_prefix.name
    data_gen['filter-list_prefix'] = filterlist_prefix_='filter-list_prefix'
    data_gen['NAME_OF_AN_IPV6'] = name_of_an_ipv6
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_filterlist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ospf6_area_areachoicecase_filterlist_prefix_prefixinoutbound():
    """Filter networks sent to this area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_filterlist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_filterlist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_filterlist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='import-list', invoke_without_command=True)
@click.argument('name_of_the_accesslist', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ospf6_area_areachoicecase_importlist(name_of_the_accesslist, importlist_='import-list'):
    """Set the filter for networks from other areas announced to the specified one"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_importlist.name
    data_gen['import-list'] = importlist_='import-list'
    data_gen['NAME_OF_THE_ACCESS-LIST'] = name_of_the_accesslist
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_importlist.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_importlist_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='nssa', invoke_without_command=True)
def frr_config_router_ospf6_area_areachoicecase_nssa(nssa_='nssa'):
    """Configure OSPF6 area as nssa"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_nssa.name
    data_gen['nssa'] = nssa_='nssa'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_nssa.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_nssa_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='default-information-originate', invoke_without_command=True)
def frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate(nssa_defaultinformationoriginate_='nssa_default-information-originate'):
    """Originate Type 7 default into NSSA area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate.name
    data_gen['nssa_default-information-originate'] = nssa_defaultinformationoriginate_='nssa_default-information-originate'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospfv3_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate_metric(ospfv3_metric, nssa_defaultinformationoriginate_metric_='nssa_default-information-originate_metric'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate_metric.name
    data_gen['nssa_default-information-originate_metric'] = nssa_defaultinformationoriginate_metric_='nssa_default-information-originate_metric'
    data_gen['OSPFV3_METRIC'] = ospfv3_metric
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate_metric.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate_metric_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate_metrictype(set_ospfv3_external_type, nssa_defaultinformationoriginate_metrictype_='nssa_default-information-originate_metric-type'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate_metrictype.name
    data_gen['nssa_default-information-originate_metric-type'] = nssa_defaultinformationoriginate_metrictype_='nssa_default-information-originate_metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate_metrictype.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_nssa_defaultinformationoriginate_metrictype_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='no-summary', invoke_without_command=True)
def frr_config_router_ospf6_area_areachoicecase_nssa_nosummary(nssa_nosummary_='nssa_no-summary'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_nssa_nosummary.name
    data_gen['nssa_no-summary'] = nssa_nosummary_='nssa_no-summary'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_nosummary.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_nssa_nosummary_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='range', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_area_areachoicecase_nssa_range(specify_ipv6_prefix, nssa_range_='nssa_range'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_nssa_range.name
    data_gen['nssa_range'] = nssa_range_='nssa_range'
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_range.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_nssa_range_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_range.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_area_areachoicecase_nssa_range_cost(advertised_metric_for_this, cost_='cost'):
    """User specified metric for this range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_nssa_range_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_range_cost.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_nssa_range_cost_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_range.group(cls=FRR_AbbreviationGroup, name='not-advertise', invoke_without_command=True)
def frr_config_router_ospf6_area_areachoicecase_nssa_range_notadvertise(notadvertise_='not-advertise'):
    """Do not advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_nssa_range_notadvertise.name
    data_gen['not-advertise'] = notadvertise_='not-advertise'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_nssa_range_notadvertise.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_nssa_range_notadvertise_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='range', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_area_areachoicecase_range(specify_ipv6_prefix, range_='range'):
    """Configured address range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_range.name
    data_gen['range'] = range_='range'
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_range.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_range_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='advertise', invoke_without_command=True)
def frr_config_router_ospf6_area_areachoicecase_range_advertise(advertise_='advertise'):
    """Advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_range_advertise.name
    data_gen['advertise'] = advertise_='advertise'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_range_advertise.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_range_advertise_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_area_areachoicecase_range_cost(advertised_metric_for_this, cost_='cost'):
    """User specified metric for this range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_range_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_range_cost.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_range_cost_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='not-advertise', invoke_without_command=True)
def frr_config_router_ospf6_area_areachoicecase_range_notadvertise(notadvertise_='not-advertise'):
    """Do not advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_range_notadvertise.name
    data_gen['not-advertise'] = notadvertise_='not-advertise'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_range_notadvertise.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_range_notadvertise_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='stub', invoke_without_command=True)
def frr_config_router_ospf6_area_areachoicecase_stub(stub_='stub'):
    """Configure OSPF6 area as stub"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_stub.name
    data_gen['stub'] = stub_='stub'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_stub.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_stub_cr():
    pass


@frr_config_router_ospf6_area_areachoicecase_stub.group(cls=FRR_AbbreviationGroup, name='no-summary', invoke_without_command=True)
def frr_config_router_ospf6_area_areachoicecase_stub_nosummary(stub_nosummary_='stub_no-summary'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_area_areachoicecase_stub_nosummary.name
    data_gen['stub_no-summary'] = stub_nosummary_='stub_no-summary'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_area_areachoicecase_stub_nosummary.command('./	<cr>')
def frr_config_router_ospf6_area_areachoicecase_stub_nosummary_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='auto-cost',)
def frr_config_router_ospf6_autocost(autocost_='auto-cost'):
    """Calculate OSPF interface cost according to bandwidth"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_autocost.name
    
    if 'OSPF6_NODE|auto-cost' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|auto-cost'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|auto-cost']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|auto-cost'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|auto-cost'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'auto-cost')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_autocost.group(cls=FRR_AbbreviationGroup, name='reference-bandwidth', invoke_without_command=True)
@click.argument('the_reference_bandwidth_in', metavar='(1-4294967)', required=True, type=FRR_TYPE((1, 4294967)))
def frr_config_router_ospf6_autocost_referencebandwidth(the_reference_bandwidth_in, referencebandwidth_='reference-bandwidth'):
    """Use reference bandwidth method to assign OSPF cost"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_autocost_referencebandwidth.name
    data_gen['reference-bandwidth'] = referencebandwidth_='reference-bandwidth'
    data_gen['THE_REFERENCE_BANDWIDTH_IN'] = the_reference_bandwidth_in
    
    if 'OSPF6_NODE|auto-cost' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|auto-cost'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|auto-cost']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|auto-cost'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|auto-cost'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'auto-cost')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_autocost_referencebandwidth.command('./	<cr>')
def frr_config_router_ospf6_autocost_referencebandwidth_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='default-information', invoke_without_command=True)
def frr_config_router_ospf6_defaultinformation():
    """Control distribution of default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_defaultinformation.name
    
    if 'OSPF6_NODE|default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_defaultinformation.command('./	<cr>')
def frr_config_router_ospf6_defaultinformation_cr():
    pass


@frr_config_router_ospf6_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_ospf6_defaultinformation_originate(defaultinformation_originate_='default-information_originate'):
    """Distribute a default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_defaultinformation_originate.name
    
    if 'OSPF6_NODE|default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_defaultinformation_originate.command('./	<cr>')
def frr_config_router_ospf6_defaultinformation_originate_cr():
    pass


@frr_config_router_ospf6_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='always', invoke_without_command=True)
def frr_config_router_ospf6_defaultinformation_originate_always(always_='always'):
    """Always advertise default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_defaultinformation_originate_always.name
    data_gen['always'] = always_='always'
    
    if 'OSPF6_NODE|default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_defaultinformation_originate_always.command('./	<cr>')
def frr_config_router_ospf6_defaultinformation_originate_always_cr():
    pass


@frr_config_router_ospf6_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospfv3_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_defaultinformation_originate_metric(ospfv3_metric, metric_='metric'):
    """OSPFv3 default metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_defaultinformation_originate_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['OSPFV3_METRIC'] = ospfv3_metric
    
    if 'OSPF6_NODE|default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_defaultinformation_originate_metric.command('./	<cr>')
def frr_config_router_ospf6_defaultinformation_originate_metric_cr():
    pass


@frr_config_router_ospf6_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_defaultinformation_originate_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 metric type for default routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_defaultinformation_originate_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_defaultinformation_originate_metrictype.command('./	<cr>')
def frr_config_router_ospf6_defaultinformation_originate_metrictype_cr():
    pass


@frr_config_router_ospf6_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ospf6_defaultinformation_originate_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_defaultinformation_originate_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'OSPF6_NODE|default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_defaultinformation_originate_routemap.command('./	<cr>')
def frr_config_router_ospf6_defaultinformation_originate_routemap_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='distance', invoke_without_command=True)
@click.argument('ospf6_administrative_distance', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_ospf6_distance(ospf6_administrative_distance, distance_='distance'):
    """Administrative distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_distance.name
    data_gen['OSPF6_ADMINISTRATIVE_DISTANCE'] = ospf6_administrative_distance
    
    if 'OSPF6_NODE|distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|distance']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_distance.command('./	<cr>')
def frr_config_router_ospf6_distance_cr():
    pass


@frr_config_router_ospf6_distance.group(cls=FRR_AbbreviationGroup, name='ospf6', invoke_without_command=True)
def frr_config_router_ospf6_distance_ospf6(distance_ospf6_='distance_ospf6'):
    """OSPF6 administrative distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_distance_ospf6.name
    
    if 'OSPF6_NODE|distance_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_distance_ospf6.command('./	<cr>')
def frr_config_router_ospf6_distance_ospf6_cr():
    pass


@frr_config_router_ospf6_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='external', invoke_without_command=True)
@click.argument('distance_for_external_routes', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_ospf6_distance_ospf6_external(distance_for_external_routes, external_='external'):
    """External routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_distance_ospf6_external.name
    data_gen['external'] = external_='external'
    data_gen['DISTANCE_FOR_EXTERNAL_ROUTES'] = distance_for_external_routes
    
    if 'OSPF6_NODE|distance_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_distance_ospf6_external.command('./	<cr>')
def frr_config_router_ospf6_distance_ospf6_external_cr():
    pass


@frr_config_router_ospf6_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='inter-area', invoke_without_command=True)
@click.argument('distance_for_interarea_routes', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_ospf6_distance_ospf6_interarea(distance_for_interarea_routes, interarea_='inter-area'):
    """Inter-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_distance_ospf6_interarea.name
    data_gen['inter-area'] = interarea_='inter-area'
    data_gen['DISTANCE_FOR_INTER-AREA_ROUTES'] = distance_for_interarea_routes
    
    if 'OSPF6_NODE|distance_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_distance_ospf6_interarea.command('./	<cr>')
def frr_config_router_ospf6_distance_ospf6_interarea_cr():
    pass


@frr_config_router_ospf6_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='intra-area', invoke_without_command=True)
@click.argument('distance_for_intraarea_routes', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_ospf6_distance_ospf6_intraarea(distance_for_intraarea_routes, intraarea_='intra-area'):
    """Intra-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_distance_ospf6_intraarea.name
    data_gen['intra-area'] = intraarea_='intra-area'
    data_gen['DISTANCE_FOR_INTRA-AREA_ROUTES'] = distance_for_intraarea_routes
    
    if 'OSPF6_NODE|distance_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_distance_ospf6_intraarea.command('./	<cr>')
def frr_config_router_ospf6_distance_ospf6_intraarea_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_config_router_ospf6_end(end_='end'):
    """End current mode and change to enable mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_end.name
    
    if 'OSPF6_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|end'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|end'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'end')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_end.command('./	<cr>')
def frr_config_router_ospf6_end_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_config_router_ospf6_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_exit.name
    
    if 'OSPF6_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|exit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|exit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'exit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_exit.command('./	<cr>')
def frr_config_router_ospf6_exit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_config_router_ospf6_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_find.name
    
    if 'OSPF6_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_config_router_ospf6_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'OSPF6_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_find_fromsearchpattern.command('./	<cr>')
def frr_config_router_ospf6_find_fromsearchpattern_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='graceful-restart', invoke_without_command=True)
def frr_config_router_ospf6_gracefulrestart(gracefulrestart_='graceful-restart'):
    """ospf6 graceful restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_gracefulrestart.name
    
    if 'OSPF6_NODE|graceful-restart' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_gracefulrestart.command('./	<cr>')
def frr_config_router_ospf6_gracefulrestart_cr():
    pass


@frr_config_router_ospf6_gracefulrestart.group(cls=FRR_AbbreviationGroup, name='grace-period', invoke_without_command=True)
@click.argument('maximum_length_of_the', metavar='(1-1800)', required=True, type=FRR_TYPE((1, 1800)))
def frr_config_router_ospf6_gracefulrestart_graceperiod(maximum_length_of_the, graceperiod_='grace-period'):
    """Maximum length of the 'grace period'"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_gracefulrestart_graceperiod.name
    data_gen['grace-period'] = graceperiod_='grace-period'
    data_gen['MAXIMUM_LENGTH_OF_THE'] = maximum_length_of_the
    
    if 'OSPF6_NODE|graceful-restart' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_gracefulrestart_graceperiod.command('./	<cr>')
def frr_config_router_ospf6_gracefulrestart_graceperiod_cr():
    pass


@frr_config_router_ospf6_gracefulrestart.group(cls=FRR_AbbreviationGroup, name='helper',)
def frr_config_router_ospf6_gracefulrestart_helper(gracefulrestart_helper_='graceful-restart_helper'):
    """ospf6 GR Helper"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_gracefulrestart_helper.name
    
    if 'OSPF6_NODE|graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='enable', invoke_without_command=True)
def frr_config_router_ospf6_gracefulrestart_helper_enable(gracefulrestart_helper_enable_='graceful-restart_helper_enable'):
    """Enable Helper support"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_gracefulrestart_helper_enable.name
    
    if 'OSPF6_NODE|graceful-restart_helper_enable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper_enable')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_gracefulrestart_helper_enable.command('./	<cr>')
def frr_config_router_ospf6_gracefulrestart_helper_enable_cr():
    pass


@frr_config_router_ospf6_gracefulrestart_helper_enable.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D']), invoke_without_command=True)
def frr_config_router_ospf6_gracefulrestart_helper_enable_advertisementrouterid():
    """Advertisement Router-ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_gracefulrestart_helper_enable_advertisementrouterid.name
    data_gen['ADVERTISEMENT_ROUTER-ID'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|graceful-restart_helper_enable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper_enable')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_gracefulrestart_helper_enable_advertisementrouterid.command('./	<cr>')
def frr_config_router_ospf6_gracefulrestart_helper_enable_advertisementrouterid_cr():
    pass


@frr_config_router_ospf6_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='lsa-check-disable', invoke_without_command=True)
def frr_config_router_ospf6_gracefulrestart_helper_lsacheckdisable(lsacheckdisable_='lsa-check-disable'):
    """disable strict LSA check"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_gracefulrestart_helper_lsacheckdisable.name
    data_gen['lsa-check-disable'] = lsacheckdisable_='lsa-check-disable'
    
    if 'OSPF6_NODE|graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_gracefulrestart_helper_lsacheckdisable.command('./	<cr>')
def frr_config_router_ospf6_gracefulrestart_helper_lsacheckdisable_cr():
    pass


@frr_config_router_ospf6_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='planned-only', invoke_without_command=True)
def frr_config_router_ospf6_gracefulrestart_helper_plannedonly(plannedonly_='planned-only'):
    """supported only planned restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_gracefulrestart_helper_plannedonly.name
    data_gen['planned-only'] = plannedonly_='planned-only'
    
    if 'OSPF6_NODE|graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_gracefulrestart_helper_plannedonly.command('./	<cr>')
def frr_config_router_ospf6_gracefulrestart_helper_plannedonly_cr():
    pass


@frr_config_router_ospf6_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='supported-grace-time', invoke_without_command=True)
@click.argument('grace_interval', metavar='(10-1800)', required=True, type=FRR_TYPE((10, 1800)))
def frr_config_router_ospf6_gracefulrestart_helper_supportedgracetime(grace_interval, supportedgracetime_='supported-grace-time'):
    """supported grace timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_gracefulrestart_helper_supportedgracetime.name
    data_gen['supported-grace-time'] = supportedgracetime_='supported-grace-time'
    data_gen['GRACE_INTERVAL'] = grace_interval
    
    if 'OSPF6_NODE|graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_gracefulrestart_helper_supportedgracetime.command('./	<cr>')
def frr_config_router_ospf6_gracefulrestart_helper_supportedgracetime_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='interface',)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_ospf6_interface(interface_name, interface_='interface'):
    """Enable routing on an IPv6 interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_interface.name
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'OSPF6_NODE|interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|interface']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_interface.group(cls=FRR_AbbreviationGroup, name='area',)
def frr_config_router_ospf6_interface_area(area_='area'):
    """Specify the OSPF6 area ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_interface_area.name
    data_gen['area'] = area_='area'
    
    if 'OSPF6_NODE|interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|interface']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_interface_area.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', (0, 4294967295)]), invoke_without_command=True)
def frr_config_router_ospf6_interface_area_areachoicecase():
    """OSPF6 area ID in IPv4 address notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_interface_area_areachoicecase.name
    data_gen['AREA_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|interface']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_interface_area_areachoicecase.command('./	<cr>')
def frr_config_router_ospf6_interface_area_areachoicecase_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_config_router_ospf6_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_list.name
    
    if 'OSPF6_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_list.command('./	<cr>')
def frr_config_router_ospf6_list_cr():
    pass


@frr_config_router_ospf6_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_config_router_ospf6_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'OSPF6_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_list_permutations.command('./	<cr>')
def frr_config_router_ospf6_list_permutations_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='log-adjacency-changes', invoke_without_command=True)
def frr_config_router_ospf6_logadjacencychanges(logadjacencychanges_='log-adjacency-changes'):
    """Log changes in adjacency state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_logadjacencychanges.name
    
    if 'OSPF6_NODE|log-adjacency-changes' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'log-adjacency-changes')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_logadjacencychanges.command('./	<cr>')
def frr_config_router_ospf6_logadjacencychanges_cr():
    pass


@frr_config_router_ospf6_logadjacencychanges.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_config_router_ospf6_logadjacencychanges_detail(detail_='detail'):
    """Log all state changes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_logadjacencychanges_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'OSPF6_NODE|log-adjacency-changes' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'log-adjacency-changes')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_logadjacencychanges_detail.command('./	<cr>')
def frr_config_router_ospf6_logadjacencychanges_detail_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='maximum-paths', invoke_without_command=True)
@click.argument('number_of_paths', metavar='(1-256)', required=True, type=FRR_TYPE((1, 256)))
def frr_config_router_ospf6_maximumpaths(number_of_paths, maximumpaths_='maximum-paths'):
    """Max no of multiple paths for ECMP support"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_maximumpaths.name
    data_gen['NUMBER_OF_PATHS'] = number_of_paths
    
    if 'OSPF6_NODE|maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_maximumpaths.command('./	<cr>')
def frr_config_router_ospf6_maximumpaths_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_config_router_ospf6_no(no_='no'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no.name
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='aggregation', invoke_without_command=True)
def frr_config_router_ospf6_no_aggregation():
    """External route aggregation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_aggregation.name
    
    if 'OSPF6_NODE|no_aggregation' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_aggregation')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_aggregation.command('./	<cr>')
def frr_config_router_ospf6_no_aggregation_cr():
    pass


@frr_config_router_ospf6_no_aggregation.group(cls=FRR_AbbreviationGroup, name='timer', invoke_without_command=True)
def frr_config_router_ospf6_no_aggregation_timer(no_aggregation_timer_='no_aggregation_timer'):
    """Delay timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_aggregation_timer.name
    
    if 'OSPF6_NODE|no_aggregation_timer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_aggregation_timer')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_aggregation_timer.command('./	<cr>')
def frr_config_router_ospf6_no_aggregation_timer_cr():
    pass


@frr_config_router_ospf6_no_aggregation_timer.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(5, 1800)]), invoke_without_command=True)
def frr_config_router_ospf6_no_aggregation_timer_timerinterval():
    """Timer interval(in seconds)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_aggregation_timer_timerinterval.name
    data_gen['TIMER_INTERVAL'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_aggregation_timer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_aggregation_timer')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_aggregation_timer_timerinterval.command('./	<cr>')
def frr_config_router_ospf6_no_aggregation_timer_timerinterval_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='area',)
def frr_config_router_ospf6_no_area(area_='area'):
    """OSPF6 area parameters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area.name
    data_gen['area'] = area_='area'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', (0, 4294967295)]),)
def frr_config_router_ospf6_no_area_areachoicecase():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase.name
    data_gen['AREA_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='export-list', invoke_without_command=True)
@click.argument('name_of_the_accesslist', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ospf6_no_area_areachoicecase_exportlist(name_of_the_accesslist, exportlist_='export-list'):
    """Unset the filter for networks announced to other areas"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_exportlist.name
    data_gen['export-list'] = exportlist_='export-list'
    data_gen['NAME_OF_THE_ACCESS-LIST'] = name_of_the_accesslist
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_exportlist.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_exportlist_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='filter-list',)
def frr_config_router_ospf6_no_area_areachoicecase_filterlist():
    """Filter prefixes between OSPF6 areas"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_ospf6_no_area_areachoicecase_filterlist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('name_of_an_ipv6', metavar='PREFIXLIST_NAME', required=True, type=FRR_TYPE('PREFIXLIST_NAME'))
def frr_config_router_ospf6_no_area_areachoicecase_filterlist_prefix(name_of_an_ipv6, filterlist_prefix_='filter-list_prefix'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_filterlist_prefix.name
    data_gen['filter-list_prefix'] = filterlist_prefix_='filter-list_prefix'
    data_gen['NAME_OF_AN_IPV6'] = name_of_an_ipv6
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_filterlist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ospf6_no_area_areachoicecase_filterlist_prefix_prefixinoutbound():
    """Filter networks sent to this area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_filterlist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_filterlist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_filterlist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='import-list', invoke_without_command=True)
@click.argument('name_of_the_accesslist', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ospf6_no_area_areachoicecase_importlist(name_of_the_accesslist, importlist_='import-list'):
    """Unset the filter for networks announced to other areas"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_importlist.name
    data_gen['import-list'] = importlist_='import-list'
    data_gen['NAME_OF_THE_ACCESS-LIST'] = name_of_the_accesslist
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_importlist.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_importlist_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='nssa', invoke_without_command=True)
def frr_config_router_ospf6_no_area_areachoicecase_nssa(nssa_='nssa'):
    """Configure OSPF6 area as nssa"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_nssa.name
    data_gen['nssa'] = nssa_='nssa'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_nssa_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='default-information-originate', invoke_without_command=True)
def frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate(nssa_defaultinformationoriginate_='nssa_default-information-originate'):
    """Originate Type 7 default into NSSA area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate.name
    data_gen['nssa_default-information-originate'] = nssa_defaultinformationoriginate_='nssa_default-information-originate'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospfv3_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate_metric(ospfv3_metric, nssa_defaultinformationoriginate_metric_='nssa_default-information-originate_metric'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate_metric.name
    data_gen['nssa_default-information-originate_metric'] = nssa_defaultinformationoriginate_metric_='nssa_default-information-originate_metric'
    data_gen['OSPFV3_METRIC'] = ospfv3_metric
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate_metric.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate_metric_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate_metrictype(set_ospfv3_external_type, nssa_defaultinformationoriginate_metrictype_='nssa_default-information-originate_metric-type'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate_metrictype.name
    data_gen['nssa_default-information-originate_metric-type'] = nssa_defaultinformationoriginate_metrictype_='nssa_default-information-originate_metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate_metrictype.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_nssa_defaultinformationoriginate_metrictype_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='no-summary', invoke_without_command=True)
def frr_config_router_ospf6_no_area_areachoicecase_nssa_nosummary(nssa_nosummary_='nssa_no-summary'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_nssa_nosummary.name
    data_gen['nssa_no-summary'] = nssa_nosummary_='nssa_no-summary'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_nosummary.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_nssa_nosummary_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='range', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_no_area_areachoicecase_nssa_range(specify_ipv6_prefix, nssa_range_='nssa_range'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_nssa_range.name
    data_gen['nssa_range'] = nssa_range_='nssa_range'
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_range.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_nssa_range_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_range.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_no_area_areachoicecase_nssa_range_cost(advertised_metric_for_this, cost_='cost'):
    """User specified metric for this range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_nssa_range_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_range_cost.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_nssa_range_cost_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_range.group(cls=FRR_AbbreviationGroup, name='not-advertise', invoke_without_command=True)
def frr_config_router_ospf6_no_area_areachoicecase_nssa_range_notadvertise(notadvertise_='not-advertise'):
    """Do not advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_nssa_range_notadvertise.name
    data_gen['not-advertise'] = notadvertise_='not-advertise'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_nssa_range_notadvertise.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_nssa_range_notadvertise_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='range', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_no_area_areachoicecase_range(specify_ipv6_prefix, range_='range'):
    """Configured address range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_range.name
    data_gen['range'] = range_='range'
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_range.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_range_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='advertise', invoke_without_command=True)
def frr_config_router_ospf6_no_area_areachoicecase_range_advertise(advertise_='advertise'):
    """Advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_range_advertise.name
    data_gen['advertise'] = advertise_='advertise'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_range_advertise.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_range_advertise_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_no_area_areachoicecase_range_cost(advertised_metric_for_this, cost_='cost'):
    """User specified metric for this range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_range_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_range_cost.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_range_cost_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='not-advertise', invoke_without_command=True)
def frr_config_router_ospf6_no_area_areachoicecase_range_notadvertise(notadvertise_='not-advertise'):
    """Do not advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_range_notadvertise.name
    data_gen['not-advertise'] = notadvertise_='not-advertise'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_range_notadvertise.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_range_notadvertise_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='stub', invoke_without_command=True)
def frr_config_router_ospf6_no_area_areachoicecase_stub(stub_='stub'):
    """Configure OSPF6 area as stub"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_stub.name
    data_gen['stub'] = stub_='stub'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_stub.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_stub_cr():
    pass


@frr_config_router_ospf6_no_area_areachoicecase_stub.group(cls=FRR_AbbreviationGroup, name='no-summary', invoke_without_command=True)
def frr_config_router_ospf6_no_area_areachoicecase_stub_nosummary(stub_nosummary_='stub_no-summary'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_area_areachoicecase_stub_nosummary.name
    data_gen['stub_no-summary'] = stub_nosummary_='stub_no-summary'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_area_areachoicecase_stub_nosummary.command('./	<cr>')
def frr_config_router_ospf6_no_area_areachoicecase_stub_nosummary_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='auto-cost', invoke_without_command=True)
def frr_config_router_ospf6_no_autocost():
    """Calculate OSPF interface cost according to bandwidth"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_autocost.name
    
    if 'OSPF6_NODE|no_auto-cost' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_auto-cost')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_autocost.command('./	<cr>')
def frr_config_router_ospf6_no_autocost_cr():
    pass


@frr_config_router_ospf6_no_autocost.group(cls=FRR_AbbreviationGroup, name='reference-bandwidth', invoke_without_command=True)
def frr_config_router_ospf6_no_autocost_referencebandwidth(no_autocost_referencebandwidth_='no_auto-cost_reference-bandwidth'):
    """Use reference bandwidth method to assign OSPF cost"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_autocost_referencebandwidth.name
    
    if 'OSPF6_NODE|no_auto-cost_reference-bandwidth' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_auto-cost_reference-bandwidth')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_autocost_referencebandwidth.command('./	<cr>')
def frr_config_router_ospf6_no_autocost_referencebandwidth_cr():
    pass


@frr_config_router_ospf6_no_autocost_referencebandwidth.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 4294967)]), invoke_without_command=True)
def frr_config_router_ospf6_no_autocost_referencebandwidth_thereferencebandwidthin():
    """The reference bandwidth in terms of Mbits per second"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_autocost_referencebandwidth_thereferencebandwidthin.name
    data_gen['THE_REFERENCE_BANDWIDTH_IN'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_auto-cost_reference-bandwidth' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_auto-cost_reference-bandwidth')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_autocost_referencebandwidth_thereferencebandwidthin.command('./	<cr>')
def frr_config_router_ospf6_no_autocost_referencebandwidth_thereferencebandwidthin_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='default-information', invoke_without_command=True)
def frr_config_router_ospf6_no_defaultinformation():
    """Control distribution of default information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_defaultinformation.name
    
    if 'OSPF6_NODE|no_default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_defaultinformation.command('./	<cr>')
def frr_config_router_ospf6_no_defaultinformation_cr():
    pass


@frr_config_router_ospf6_no_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_ospf6_no_defaultinformation_originate(no_defaultinformation_originate_='no_default-information_originate'):
    """Distribute a default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_defaultinformation_originate.name
    
    if 'OSPF6_NODE|no_default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_defaultinformation_originate.command('./	<cr>')
def frr_config_router_ospf6_no_defaultinformation_originate_cr():
    pass


@frr_config_router_ospf6_no_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='always', invoke_without_command=True)
def frr_config_router_ospf6_no_defaultinformation_originate_always(always_='always'):
    """Always advertise default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_defaultinformation_originate_always.name
    data_gen['always'] = always_='always'
    
    if 'OSPF6_NODE|no_default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_defaultinformation_originate_always.command('./	<cr>')
def frr_config_router_ospf6_no_defaultinformation_originate_always_cr():
    pass


@frr_config_router_ospf6_no_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospfv3_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_no_defaultinformation_originate_metric(ospfv3_metric, metric_='metric'):
    """OSPFv3 default metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_defaultinformation_originate_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['OSPFV3_METRIC'] = ospfv3_metric
    
    if 'OSPF6_NODE|no_default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_defaultinformation_originate_metric.command('./	<cr>')
def frr_config_router_ospf6_no_defaultinformation_originate_metric_cr():
    pass


@frr_config_router_ospf6_no_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_no_defaultinformation_originate_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 metric type for default routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_defaultinformation_originate_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|no_default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_defaultinformation_originate_metrictype.command('./	<cr>')
def frr_config_router_ospf6_no_defaultinformation_originate_metrictype_cr():
    pass


@frr_config_router_ospf6_no_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ospf6_no_defaultinformation_originate_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_defaultinformation_originate_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'OSPF6_NODE|no_default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_defaultinformation_originate_routemap.command('./	<cr>')
def frr_config_router_ospf6_no_defaultinformation_originate_routemap_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='distance', invoke_without_command=True)
@click.argument('ospf6_administrative_distance', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_ospf6_no_distance(ospf6_administrative_distance, no_distance_='no_distance'):
    """Administrative distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_distance.name
    data_gen['OSPF6_ADMINISTRATIVE_DISTANCE'] = ospf6_administrative_distance
    
    if 'OSPF6_NODE|no_distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_distance.command('./	<cr>')
def frr_config_router_ospf6_no_distance_cr():
    pass


@frr_config_router_ospf6_no_distance.group(cls=FRR_AbbreviationGroup, name='ospf6', invoke_without_command=True)
def frr_config_router_ospf6_no_distance_ospf6():
    """OSPF6 distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_distance_ospf6.name
    
    if 'OSPF6_NODE|no_distance_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_distance_ospf6.command('./	<cr>')
def frr_config_router_ospf6_no_distance_ospf6_cr():
    pass


@frr_config_router_ospf6_no_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='external', invoke_without_command=True)
def frr_config_router_ospf6_no_distance_ospf6_external(no_distance_ospf6_external_='no_distance_ospf6_external'):
    """External routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_distance_ospf6_external.name
    
    if 'OSPF6_NODE|no_distance_ospf6_external' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_external')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_distance_ospf6_external.command('./	<cr>')
def frr_config_router_ospf6_no_distance_ospf6_external_cr():
    pass


@frr_config_router_ospf6_no_distance_ospf6_external.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(1, 255)]), invoke_without_command=True)
def frr_config_router_ospf6_no_distance_ospf6_external_distanceforexternalroutes():
    """Distance for external routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_distance_ospf6_external_distanceforexternalroutes.name
    data_gen['DISTANCE_FOR_EXTERNAL_ROUTES'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_distance_ospf6_external' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_external')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_distance_ospf6_external_distanceforexternalroutes.command('./	<cr>')
def frr_config_router_ospf6_no_distance_ospf6_external_distanceforexternalroutes_cr():
    pass


@frr_config_router_ospf6_no_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='inter-area', invoke_without_command=True)
def frr_config_router_ospf6_no_distance_ospf6_interarea(no_distance_ospf6_interarea_='no_distance_ospf6_inter-area'):
    """Inter-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_distance_ospf6_interarea.name
    
    if 'OSPF6_NODE|no_distance_ospf6_inter-area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_inter-area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_distance_ospf6_interarea.command('./	<cr>')
def frr_config_router_ospf6_no_distance_ospf6_interarea_cr():
    pass


@frr_config_router_ospf6_no_distance_ospf6_interarea.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(1, 255)]), invoke_without_command=True)
def frr_config_router_ospf6_no_distance_ospf6_interarea_distanceforinterarearoutes():
    """Distance for inter-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_distance_ospf6_interarea_distanceforinterarearoutes.name
    data_gen['DISTANCE_FOR_INTER-AREA_ROUTES'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_distance_ospf6_inter-area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_inter-area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_distance_ospf6_interarea_distanceforinterarearoutes.command('./	<cr>')
def frr_config_router_ospf6_no_distance_ospf6_interarea_distanceforinterarearoutes_cr():
    pass


@frr_config_router_ospf6_no_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='intra-area', invoke_without_command=True)
def frr_config_router_ospf6_no_distance_ospf6_intraarea(no_distance_ospf6_intraarea_='no_distance_ospf6_intra-area'):
    """Intra-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_distance_ospf6_intraarea.name
    
    if 'OSPF6_NODE|no_distance_ospf6_intra-area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_intra-area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_distance_ospf6_intraarea.command('./	<cr>')
def frr_config_router_ospf6_no_distance_ospf6_intraarea_cr():
    pass


@frr_config_router_ospf6_no_distance_ospf6_intraarea.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(1, 255)]), invoke_without_command=True)
def frr_config_router_ospf6_no_distance_ospf6_intraarea_distanceforintraarearoutes():
    """Distance for intra-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_distance_ospf6_intraarea_distanceforintraarearoutes.name
    data_gen['DISTANCE_FOR_INTRA-AREA_ROUTES'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_distance_ospf6_intra-area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_intra-area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_distance_ospf6_intraarea_distanceforintraarearoutes.command('./	<cr>')
def frr_config_router_ospf6_no_distance_ospf6_intraarea_distanceforintraarearoutes_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='graceful-restart', invoke_without_command=True)
def frr_config_router_ospf6_no_gracefulrestart(no_gracefulrestart_='no_graceful-restart'):
    """ospf6 graceful restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_gracefulrestart.name
    
    if 'OSPF6_NODE|no_graceful-restart' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_gracefulrestart.command('./	<cr>')
def frr_config_router_ospf6_no_gracefulrestart_cr():
    pass


@frr_config_router_ospf6_no_gracefulrestart.group(cls=FRR_AbbreviationGroup, name='helper',)
def frr_config_router_ospf6_no_gracefulrestart_helper(no_gracefulrestart_helper_='no_graceful-restart_helper'):
    """ospf6 GR Helper"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_gracefulrestart_helper.name
    
    if 'OSPF6_NODE|no_graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='enable', invoke_without_command=True)
def frr_config_router_ospf6_no_gracefulrestart_helper_enable(no_gracefulrestart_helper_enable_='no_graceful-restart_helper_enable'):
    """Enable Helper support"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_gracefulrestart_helper_enable.name
    
    if 'OSPF6_NODE|no_graceful-restart_helper_enable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper_enable')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_gracefulrestart_helper_enable.command('./	<cr>')
def frr_config_router_ospf6_no_gracefulrestart_helper_enable_cr():
    pass


@frr_config_router_ospf6_no_gracefulrestart_helper_enable.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D']), invoke_without_command=True)
def frr_config_router_ospf6_no_gracefulrestart_helper_enable_advertisementrouterid():
    """Advertisement Router-ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_gracefulrestart_helper_enable_advertisementrouterid.name
    data_gen['ADVERTISEMENT_ROUTER-ID'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_graceful-restart_helper_enable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper_enable')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_gracefulrestart_helper_enable_advertisementrouterid.command('./	<cr>')
def frr_config_router_ospf6_no_gracefulrestart_helper_enable_advertisementrouterid_cr():
    pass


@frr_config_router_ospf6_no_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='lsa-check-disable', invoke_without_command=True)
def frr_config_router_ospf6_no_gracefulrestart_helper_lsacheckdisable(lsacheckdisable_='lsa-check-disable'):
    """diasble strict LSA check"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_gracefulrestart_helper_lsacheckdisable.name
    data_gen['lsa-check-disable'] = lsacheckdisable_='lsa-check-disable'
    
    if 'OSPF6_NODE|no_graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_gracefulrestart_helper_lsacheckdisable.command('./	<cr>')
def frr_config_router_ospf6_no_gracefulrestart_helper_lsacheckdisable_cr():
    pass


@frr_config_router_ospf6_no_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='planned-only', invoke_without_command=True)
def frr_config_router_ospf6_no_gracefulrestart_helper_plannedonly(plannedonly_='planned-only'):
    """supported only for planned restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_gracefulrestart_helper_plannedonly.name
    data_gen['planned-only'] = plannedonly_='planned-only'
    
    if 'OSPF6_NODE|no_graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_gracefulrestart_helper_plannedonly.command('./	<cr>')
def frr_config_router_ospf6_no_gracefulrestart_helper_plannedonly_cr():
    pass


@frr_config_router_ospf6_no_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='supported-grace-time', invoke_without_command=True)
@click.argument('grace_interval', metavar='(10-1800)', required=True, type=FRR_TYPE((10, 1800)))
def frr_config_router_ospf6_no_gracefulrestart_helper_supportedgracetime(grace_interval, supportedgracetime_='supported-grace-time'):
    """supported grace timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_gracefulrestart_helper_supportedgracetime.name
    data_gen['supported-grace-time'] = supportedgracetime_='supported-grace-time'
    data_gen['GRACE_INTERVAL'] = grace_interval
    
    if 'OSPF6_NODE|no_graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_gracefulrestart_helper_supportedgracetime.command('./	<cr>')
def frr_config_router_ospf6_no_gracefulrestart_helper_supportedgracetime_cr():
    pass


@frr_config_router_ospf6_no_gracefulrestart.group(cls=FRR_AbbreviationGroup, name='period', invoke_without_command=True)
@click.argument('maximum_length_of_the', metavar='(1-1800)', required=True, type=FRR_TYPE((1, 1800)))
def frr_config_router_ospf6_no_gracefulrestart_period(maximum_length_of_the, period_='period'):
    """Maximum length of the 'grace period'"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_gracefulrestart_period.name
    data_gen['period'] = period_='period'
    data_gen['MAXIMUM_LENGTH_OF_THE'] = maximum_length_of_the
    
    if 'OSPF6_NODE|no_graceful-restart' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_gracefulrestart_period.command('./	<cr>')
def frr_config_router_ospf6_no_gracefulrestart_period_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='interface',)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_ospf6_no_interface(interface_name, interface_='interface'):
    """Disable routing on an IPv6 interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_interface.name
    data_gen['interface'] = interface_='interface'
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_interface.group(cls=FRR_AbbreviationGroup, name='area',)
def frr_config_router_ospf6_no_interface_area(area_='area'):
    """Specify the OSPF6 area ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_interface_area.name
    data_gen['area'] = area_='area'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_interface_area.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D', (0, 4294967295)]), invoke_without_command=True)
def frr_config_router_ospf6_no_interface_area_areachoicecase():
    """OSPF6 area ID in IPv4 address notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_interface_area_areachoicecase.name
    data_gen['AREA_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_interface_area_areachoicecase.command('./	<cr>')
def frr_config_router_ospf6_no_interface_area_areachoicecase_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='log-adjacency-changes', invoke_without_command=True)
def frr_config_router_ospf6_no_logadjacencychanges(no_logadjacencychanges_='no_log-adjacency-changes'):
    """Log changes in adjacency state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_logadjacencychanges.name
    
    if 'OSPF6_NODE|no_log-adjacency-changes' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_log-adjacency-changes')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_logadjacencychanges.command('./	<cr>')
def frr_config_router_ospf6_no_logadjacencychanges_cr():
    pass


@frr_config_router_ospf6_no_logadjacencychanges.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_config_router_ospf6_no_logadjacencychanges_detail(detail_='detail'):
    """Log all state changes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_logadjacencychanges_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'OSPF6_NODE|no_log-adjacency-changes' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_log-adjacency-changes')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_logadjacencychanges_detail.command('./	<cr>')
def frr_config_router_ospf6_no_logadjacencychanges_detail_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='maximum-paths', invoke_without_command=True)
def frr_config_router_ospf6_no_maximumpaths(no_maximumpaths_='no_maximum-paths'):
    """Max no of multiple paths for ECMP support"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_maximumpaths.name
    
    if 'OSPF6_NODE|no_maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_maximumpaths.command('./	<cr>')
def frr_config_router_ospf6_no_maximumpaths_cr():
    pass


@frr_config_router_ospf6_no_maximumpaths.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, [(1, 256)]), invoke_without_command=True)
def frr_config_router_ospf6_no_maximumpaths_numberofpaths():
    """Number of paths"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_maximumpaths_numberofpaths.name
    data_gen['NUMBER_OF_PATHS'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_maximumpaths_numberofpaths.command('./	<cr>')
def frr_config_router_ospf6_no_maximumpaths_numberofpaths_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='ospf6', invoke_without_command=True)
def frr_config_router_ospf6_no_ospf6():
    """Open Shortest Path First (OSPF) for IPv6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_ospf6.name
    
    if 'OSPF6_NODE|no_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_ospf6.command('./	<cr>')
def frr_config_router_ospf6_no_ospf6_cr():
    pass


@frr_config_router_ospf6_no_ospf6.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
def frr_config_router_ospf6_no_ospf6_routerid(no_ospf6_routerid_='no_ospf6_router-id'):
    """Configure OSPF6 Router-ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_ospf6_routerid.name
    
    if 'OSPF6_NODE|no_ospf6_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ospf6_router-id')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_ospf6_routerid.command('./	<cr>')
def frr_config_router_ospf6_no_ospf6_routerid_cr():
    pass


@frr_config_router_ospf6_no_ospf6_routerid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D']), invoke_without_command=True)
def frr_config_router_ospf6_no_ospf6_routerid_specifybyipv4address():
    """specify by IPv4 address notation(e.g. 0.0.0.0)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_ospf6_routerid_specifybyipv4address.name
    data_gen['SPECIFY_BY_IPV4_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_ospf6_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ospf6_router-id')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_ospf6_routerid_specifybyipv4address.command('./	<cr>')
def frr_config_router_ospf6_no_ospf6_routerid_specifybyipv4address_cr():
    pass


@frr_config_router_ospf6_no_ospf6.group(cls=FRR_AbbreviationGroup, name='send-extra-data',)
def frr_config_router_ospf6_no_ospf6_sendextradata(no_ospf6_sendextradata_='no_ospf6_send-extra-data'):
    """Extra data to Zebra for display/use"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_ospf6_sendextradata.name
    
    if 'OSPF6_NODE|no_ospf6_send-extra-data' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ospf6_send-extra-data')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_ospf6_sendextradata.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_config_router_ospf6_no_ospf6_sendextradata_zebra(zebra_='zebra'):
    """To zebra"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_ospf6_sendextradata_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'OSPF6_NODE|no_ospf6_send-extra-data' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ospf6_send-extra-data')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_ospf6_sendextradata_zebra.command('./	<cr>')
def frr_config_router_ospf6_no_ospf6_sendextradata_zebra_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_config_router_ospf6_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_output.name
    
    if 'OSPF6_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_output.command('./	<cr>')
def frr_config_router_ospf6_no_output_cr():
    pass


@frr_config_router_ospf6_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_config_router_ospf6_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_output_file.name
    
    if 'OSPF6_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_output_file.command('./	<cr>')
def frr_config_router_ospf6_no_output_file_cr():
    pass


@frr_config_router_ospf6_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['FILE']), invoke_without_command=True)
def frr_config_router_ospf6_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_config_router_ospf6_no_output_file_pathtodumpoutput_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ospf6d', metavar='FRR_REDIST_STR_OSPF6D', required=True, type=FRR_TYPE('FRR_REDIST_STR_OSPF6D'))
def frr_config_router_ospf6_no_redistribute(frr_redist_help_str_ospf6d, redistribute_='redistribute'):
    """Redistribute"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_redistribute.name
    data_gen['redistribute'] = redistribute_='redistribute'
    data_gen['FRR_REDIST_HELP_STR_OSPF6D'] = frr_redist_help_str_ospf6d
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_redistribute.command('./	<cr>')
def frr_config_router_ospf6_no_redistribute_cr():
    pass


@frr_config_router_ospf6_no_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospf_default_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_no_redistribute_metric(ospf_default_metric, metric_='metric'):
    """Metric for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['OSPF_DEFAULT_METRIC'] = ospf_default_metric
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_redistribute_metric.command('./	<cr>')
def frr_config_router_ospf6_no_redistribute_metric_cr():
    pass


@frr_config_router_ospf6_no_redistribute.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospf_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_no_redistribute_metrictype(set_ospf_external_type, metrictype_='metric-type'):
    """OSPF exterior metric type for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_redistribute_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPF_EXTERNAL_TYPE'] = set_ospf_external_type
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_redistribute_metrictype.command('./	<cr>')
def frr_config_router_ospf6_no_redistribute_metrictype_cr():
    pass


@frr_config_router_ospf6_no_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('route_map_name', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ospf6_no_redistribute_routemap(route_map_name, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['ROUTE_MAP_NAME'] = route_map_name
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_redistribute_routemap.command('./	<cr>')
def frr_config_router_ospf6_no_redistribute_routemap_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='stub-router',)
def frr_config_router_ospf6_no_stubrouter(no_stubrouter_='no_stub-router'):
    """Make router a stub router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_stubrouter.name
    
    if 'OSPF6_NODE|no_stub-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_stub-router']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_stub-router')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_stubrouter.group(cls=FRR_AbbreviationGroup, name='administrative', invoke_without_command=True)
def frr_config_router_ospf6_no_stubrouter_administrative(administrative_='administrative'):
    """Administratively applied, for an indefinite period"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_stubrouter_administrative.name
    data_gen['administrative'] = administrative_='administrative'
    
    if 'OSPF6_NODE|no_stub-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_stub-router']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_stub-router')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_stubrouter_administrative.command('./	<cr>')
def frr_config_router_ospf6_no_stubrouter_administrative_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='summary-address', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_no_summaryaddress(specify_ipv6_prefix, summaryaddress_='summary-address'):
    """External summary address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_summaryaddress.name
    data_gen['summary-address'] = summaryaddress_='summary-address'
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_summaryaddress.command('./	<cr>')
def frr_config_router_ospf6_no_summaryaddress_cr():
    pass


@frr_config_router_ospf6_no_summaryaddress.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_no_summaryaddress_metric(advertised_metric_for_this, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_summaryaddress_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_summaryaddress_metric.command('./	<cr>')
def frr_config_router_ospf6_no_summaryaddress_metric_cr():
    pass


@frr_config_router_ospf6_no_summaryaddress.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_no_summaryaddress_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 exterior metric type for summarised routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_summaryaddress_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_summaryaddress_metrictype.command('./	<cr>')
def frr_config_router_ospf6_no_summaryaddress_metrictype_cr():
    pass


@frr_config_router_ospf6_no_summaryaddress.group(cls=FRR_AbbreviationGroup, name='no-advertise', invoke_without_command=True)
def frr_config_router_ospf6_no_summaryaddress_noadvertise(noadvertise_='no-advertise'):
    """Adverise summary route to the AS"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_summaryaddress_noadvertise.name
    data_gen['no-advertise'] = noadvertise_='no-advertise'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_summaryaddress_noadvertise.command('./	<cr>')
def frr_config_router_ospf6_no_summaryaddress_noadvertise_cr():
    pass


@frr_config_router_ospf6_no_summaryaddress.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('router_tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_config_router_ospf6_no_summaryaddress_tag(router_tag_value, tag_='tag'):
    """Router tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_summaryaddress_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['ROUTER_TAG_VALUE'] = router_tag_value
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_summaryaddress_tag.command('./	<cr>')
def frr_config_router_ospf6_no_summaryaddress_tag_cr():
    pass


@frr_config_router_ospf6_no_summaryaddress_tag.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_no_summaryaddress_tag_metric(advertised_metric_for_this, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_summaryaddress_tag_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_summaryaddress_tag_metric.command('./	<cr>')
def frr_config_router_ospf6_no_summaryaddress_tag_metric_cr():
    pass


@frr_config_router_ospf6_no_summaryaddress_tag.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_no_summaryaddress_tag_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 exterior metric type for summarised routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_summaryaddress_tag_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_summaryaddress_tag_metrictype.command('./	<cr>')
def frr_config_router_ospf6_no_summaryaddress_tag_metrictype_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='timers', invoke_without_command=True)
def frr_config_router_ospf6_no_timers():
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_timers.name
    
    if 'OSPF6_NODE|no_timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_timers.command('./	<cr>')
def frr_config_router_ospf6_no_timers_cr():
    pass


@frr_config_router_ospf6_no_timers.group(cls=FRR_AbbreviationGroup, name='lsa', invoke_without_command=True)
def frr_config_router_ospf6_no_timers_lsa():
    """OSPF6 LSA timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_timers_lsa.name
    
    if 'OSPF6_NODE|no_timers_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_lsa')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_timers_lsa.command('./	<cr>')
def frr_config_router_ospf6_no_timers_lsa_cr():
    pass


@frr_config_router_ospf6_no_timers_lsa.group(cls=FRR_AbbreviationGroup, name='min-arrival', invoke_without_command=True)
def frr_config_router_ospf6_no_timers_lsa_minarrival(no_timers_lsa_minarrival_='no_timers_lsa_min-arrival'):
    """Minimum delay in receiving new version of a LSA"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_timers_lsa_minarrival.name
    
    if 'OSPF6_NODE|no_timers_lsa_min-arrival' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_lsa_min-arrival')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_timers_lsa_minarrival.command('./	<cr>')
def frr_config_router_ospf6_no_timers_lsa_minarrival_cr():
    pass


@frr_config_router_ospf6_no_timers_lsa_minarrival.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(0, 600000)]), invoke_without_command=True)
def frr_config_router_ospf6_no_timers_lsa_minarrival_delayinmilliseconds():
    """Delay in milliseconds"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_timers_lsa_minarrival_delayinmilliseconds.name
    data_gen['DELAY_IN_MILLISECONDS'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_timers_lsa_min-arrival' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_lsa_min-arrival')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_timers_lsa_minarrival_delayinmilliseconds.command('./	<cr>')
def frr_config_router_ospf6_no_timers_lsa_minarrival_delayinmilliseconds_cr():
    pass


@frr_config_router_ospf6_no_timers.group(cls=FRR_AbbreviationGroup, name='throttle', invoke_without_command=True)
def frr_config_router_ospf6_no_timers_throttle():
    """Throttling adaptive timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_timers_throttle.name
    
    if 'OSPF6_NODE|no_timers_throttle' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_throttle')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_timers_throttle.command('./	<cr>')
def frr_config_router_ospf6_no_timers_throttle_cr():
    pass


@frr_config_router_ospf6_no_timers_throttle.group(cls=FRR_AbbreviationGroup, name='spf', invoke_without_command=True)
def frr_config_router_ospf6_no_timers_throttle_spf(no_timers_throttle_spf_='no_timers_throttle_spf'):
    """OSPF6 SPF timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_timers_throttle_spf.name
    
    if 'OSPF6_NODE|no_timers_throttle_spf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_throttle_spf')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_timers_throttle_spf.command('./	<cr>')
def frr_config_router_ospf6_no_timers_throttle_spf_cr():
    pass


@frr_config_router_ospf6_no_timers_throttle_spf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(0, 600000)]), invoke_without_command=True)
@click.argument('initial_hold_time_between', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
@click.argument('maximum_hold_time', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
def frr_config_router_ospf6_no_timers_throttle_spf_delayfromfirstchange(initial_hold_time_between, maximum_hold_time):
    """Delay (msec) from first change received till SPF calculation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_timers_throttle_spf_delayfromfirstchange.name
    data_gen['DELAY_FROM_FIRST_CHANGE'] = FRR_CLI_ARGS[name]
    data_gen['INITIAL_HOLD_TIME_BETWEEN'] = initial_hold_time_between
    data_gen['MAXIMUM_HOLD_TIME'] = maximum_hold_time
    
    if 'OSPF6_NODE|no_timers_throttle_spf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_throttle_spf')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_timers_throttle_spf_delayfromfirstchange.command('./	<cr>')
def frr_config_router_ospf6_no_timers_throttle_spf_delayfromfirstchange_cr():
    pass


@frr_config_router_ospf6_no.group(cls=FRR_AbbreviationGroup, name='write-multiplier', invoke_without_command=True)
@click.argument('maximum_number_of_interface', metavar='(1-100)', required=True, type=FRR_TYPE((1, 100)))
def frr_config_router_ospf6_no_writemultiplier(maximum_number_of_interface, writemultiplier_='write-multiplier'):
    """Write multiplier"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_no_writemultiplier.name
    data_gen['write-multiplier'] = writemultiplier_='write-multiplier'
    data_gen['MAXIMUM_NUMBER_OF_INTERFACE'] = maximum_number_of_interface
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_no_writemultiplier.command('./	<cr>')
def frr_config_router_ospf6_no_writemultiplier_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='ospf6',)
def frr_config_router_ospf6_ospf6(ospf6_='ospf6'):
    """Open Shortest Path First (OSPF) for IPv6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_ospf6.name
    
    if 'OSPF6_NODE|ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_ospf6.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
@click.argument('specify_by_ipv4_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_ospf6_ospf6_routerid(specify_by_ipv4_address, routerid_='router-id'):
    """Configure OSPF6 Router-ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_ospf6_routerid.name
    data_gen['router-id'] = routerid_='router-id'
    data_gen['SPECIFY_BY_IPV4_ADDRESS'] = specify_by_ipv4_address
    
    if 'OSPF6_NODE|ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_ospf6_routerid.command('./	<cr>')
def frr_config_router_ospf6_ospf6_routerid_cr():
    pass


@frr_config_router_ospf6_ospf6.group(cls=FRR_AbbreviationGroup, name='send-extra-data',)
def frr_config_router_ospf6_ospf6_sendextradata(ospf6_sendextradata_='ospf6_send-extra-data'):
    """Extra data to Zebra for display/use"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_ospf6_sendextradata.name
    
    if 'OSPF6_NODE|ospf6_send-extra-data' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ospf6_send-extra-data')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_ospf6_sendextradata.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_config_router_ospf6_ospf6_sendextradata_zebra(zebra_='zebra'):
    """To zebra"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_ospf6_sendextradata_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'OSPF6_NODE|ospf6_send-extra-data' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ospf6_send-extra-data')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_ospf6_sendextradata_zebra.command('./	<cr>')
def frr_config_router_ospf6_ospf6_sendextradata_zebra_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_config_router_ospf6_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_output.name
    
    if 'OSPF6_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_config_router_ospf6_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'OSPF6_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_output_file.command('./	<cr>')
def frr_config_router_ospf6_output_file_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_config_router_ospf6_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_quit.name
    
    if 'OSPF6_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|quit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|quit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'quit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_quit.command('./	<cr>')
def frr_config_router_ospf6_quit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ospf6d', metavar='FRR_REDIST_STR_OSPF6D', required=True, type=FRR_TYPE('FRR_REDIST_STR_OSPF6D'))
def frr_config_router_ospf6_redistribute(frr_redist_help_str_ospf6d, redistribute_='redistribute'):
    """Redistribute"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_redistribute.name
    data_gen['FRR_REDIST_HELP_STR_OSPF6D'] = frr_redist_help_str_ospf6d
    
    if 'OSPF6_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_redistribute.command('./	<cr>')
def frr_config_router_ospf6_redistribute_cr():
    pass


@frr_config_router_ospf6_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospf_default_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_redistribute_metric(ospf_default_metric, metric_='metric'):
    """Metric for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['OSPF_DEFAULT_METRIC'] = ospf_default_metric
    
    if 'OSPF6_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_redistribute_metric.command('./	<cr>')
def frr_config_router_ospf6_redistribute_metric_cr():
    pass


@frr_config_router_ospf6_redistribute.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospf_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_redistribute_metrictype(set_ospf_external_type, metrictype_='metric-type'):
    """OSPF exterior metric type for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_redistribute_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPF_EXTERNAL_TYPE'] = set_ospf_external_type
    
    if 'OSPF6_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_redistribute_metrictype.command('./	<cr>')
def frr_config_router_ospf6_redistribute_metrictype_cr():
    pass


@frr_config_router_ospf6_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('route_map_name', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ospf6_redistribute_routemap(route_map_name, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['ROUTE_MAP_NAME'] = route_map_name
    
    if 'OSPF6_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_redistribute_routemap.command('./	<cr>')
def frr_config_router_ospf6_redistribute_routemap_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='stub-router',)
def frr_config_router_ospf6_stubrouter(stubrouter_='stub-router'):
    """Make router a stub router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_stubrouter.name
    
    if 'OSPF6_NODE|stub-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|stub-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|stub-router']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|stub-router'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|stub-router'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'stub-router')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_stubrouter.group(cls=FRR_AbbreviationGroup, name='administrative', invoke_without_command=True)
def frr_config_router_ospf6_stubrouter_administrative(administrative_='administrative'):
    """Administratively applied, for an indefinite period"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_stubrouter_administrative.name
    data_gen['administrative'] = administrative_='administrative'
    
    if 'OSPF6_NODE|stub-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|stub-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|stub-router']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|stub-router'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|stub-router'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'stub-router')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_stubrouter_administrative.command('./	<cr>')
def frr_config_router_ospf6_stubrouter_administrative_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='summary-address', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_summaryaddress(specify_ipv6_prefix, summaryaddress_='summary-address'):
    """External summary address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_summaryaddress.name
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_summaryaddress.command('./	<cr>')
def frr_config_router_ospf6_summaryaddress_cr():
    pass


@frr_config_router_ospf6_summaryaddress.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_summaryaddress_metric(advertised_metric_for_this, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_summaryaddress_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_summaryaddress_metric.command('./	<cr>')
def frr_config_router_ospf6_summaryaddress_metric_cr():
    pass


@frr_config_router_ospf6_summaryaddress.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_summaryaddress_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 exterior metric type for summarised routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_summaryaddress_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_summaryaddress_metrictype.command('./	<cr>')
def frr_config_router_ospf6_summaryaddress_metrictype_cr():
    pass


@frr_config_router_ospf6_summaryaddress.group(cls=FRR_AbbreviationGroup, name='no-advertise', invoke_without_command=True)
def frr_config_router_ospf6_summaryaddress_noadvertise(noadvertise_='no-advertise'):
    """Don't advertise summary route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_summaryaddress_noadvertise.name
    data_gen['no-advertise'] = noadvertise_='no-advertise'
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_summaryaddress_noadvertise.command('./	<cr>')
def frr_config_router_ospf6_summaryaddress_noadvertise_cr():
    pass


@frr_config_router_ospf6_summaryaddress.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('router_tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_config_router_ospf6_summaryaddress_tag(router_tag_value, tag_='tag'):
    """Router tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_summaryaddress_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['ROUTER_TAG_VALUE'] = router_tag_value
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_summaryaddress_tag.command('./	<cr>')
def frr_config_router_ospf6_summaryaddress_tag_cr():
    pass


@frr_config_router_ospf6_summaryaddress_tag.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_summaryaddress_tag_metric(advertised_metric_for_this, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_summaryaddress_tag_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_summaryaddress_tag_metric.command('./	<cr>')
def frr_config_router_ospf6_summaryaddress_tag_metric_cr():
    pass


@frr_config_router_ospf6_summaryaddress_tag.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_summaryaddress_tag_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 exterior metric type for summarised routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_summaryaddress_tag_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_summaryaddress_tag_metrictype.command('./	<cr>')
def frr_config_router_ospf6_summaryaddress_tag_metrictype_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='timers',)
def frr_config_router_ospf6_timers():
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_ospf6_timers.group(cls=FRR_AbbreviationGroup, name='lsa',)
def frr_config_router_ospf6_timers_lsa(timers_lsa_='timers_lsa'):
    """OSPF6 LSA timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_timers_lsa.name
    
    if 'OSPF6_NODE|timers_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|timers_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers_lsa')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_timers_lsa.group(cls=FRR_AbbreviationGroup, name='min-arrival', invoke_without_command=True)
@click.argument('delay_in_milliseconds', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
def frr_config_router_ospf6_timers_lsa_minarrival(delay_in_milliseconds, minarrival_='min-arrival'):
    """Minimum delay in receiving new version of a LSA"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_timers_lsa_minarrival.name
    data_gen['min-arrival'] = minarrival_='min-arrival'
    data_gen['DELAY_IN_MILLISECONDS'] = delay_in_milliseconds
    
    if 'OSPF6_NODE|timers_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|timers_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers_lsa')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_timers_lsa_minarrival.command('./	<cr>')
def frr_config_router_ospf6_timers_lsa_minarrival_cr():
    pass


@frr_config_router_ospf6_timers.group(cls=FRR_AbbreviationGroup, name='throttle',)
def frr_config_router_ospf6_timers_throttle(timers_throttle_='timers_throttle'):
    """Throttling adaptive timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_timers_throttle.name
    
    if 'OSPF6_NODE|timers_throttle' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|timers_throttle']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers_throttle')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_timers_throttle.group(cls=FRR_AbbreviationGroup, name='spf', invoke_without_command=True)
@click.argument('delay_from_first_change', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
@click.argument('initial_hold_time_between', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
@click.argument('maximum_hold_time', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
def frr_config_router_ospf6_timers_throttle_spf(maximum_hold_time, delay_from_first_change, initial_hold_time_between, spf_='spf'):
    """OSPF6 SPF timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_timers_throttle_spf.name
    data_gen['spf'] = spf_='spf'
    data_gen['DELAY_FROM_FIRST_CHANGE'] = delay_from_first_change
    data_gen['INITIAL_HOLD_TIME_BETWEEN'] = initial_hold_time_between
    data_gen['MAXIMUM_HOLD_TIME'] = maximum_hold_time
    
    if 'OSPF6_NODE|timers_throttle' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|timers_throttle']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers_throttle')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_timers_throttle_spf.command('./	<cr>')
def frr_config_router_ospf6_timers_throttle_spf_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_config_router_ospf6_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'CONFIG_NODE|router_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['CONFIG_NODE|router_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['CONFIG_NODE|router_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['CONFIG_NODE|router_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['CONFIG_NODE|router_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'router_ospf6')
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


@frr_config_router_ospf6_vrf.command('./	<cr>')
def frr_config_router_ospf6_vrf_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='aggregation',)
def frr_config_router_ospf6_vrf_aggregation(aggregation_='aggregation'):
    """External route aggregation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_aggregation.name
    
    if 'OSPF6_NODE|aggregation' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|aggregation'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|aggregation']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|aggregation'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|aggregation'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'aggregation')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_aggregation.group(cls=FRR_AbbreviationGroup, name='timer', invoke_without_command=True)
@click.argument('timer_interval', metavar='(5-1800)', required=True, type=FRR_TYPE((5, 1800)))
def frr_config_router_ospf6_vrf_aggregation_timer(timer_interval, timer_='timer'):
    """Delay timer (in seconds)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_aggregation_timer.name
    data_gen['timer'] = timer_='timer'
    data_gen['TIMER_INTERVAL'] = timer_interval
    
    if 'OSPF6_NODE|aggregation' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|aggregation'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|aggregation']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|aggregation'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|aggregation'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'aggregation')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_aggregation_timer.command('./	<cr>')
def frr_config_router_ospf6_vrf_aggregation_timer_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='area',)
def frr_config_router_ospf6_vrf_area(area_='area'):
    """OSPF6 stub parameters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area.name
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', (0, 4294967295)]),)
def frr_config_router_ospf6_vrf_area_areachoicecase():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase.name
    data_gen['AREA_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='export-list', invoke_without_command=True)
@click.argument('name_of_the_accesslist', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ospf6_vrf_area_areachoicecase_exportlist(name_of_the_accesslist, exportlist_='export-list'):
    """Set the filter for networks announced to other areas"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_exportlist.name
    data_gen['export-list'] = exportlist_='export-list'
    data_gen['NAME_OF_THE_ACCESS-LIST'] = name_of_the_accesslist
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_exportlist.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_exportlist_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='filter-list',)
def frr_config_router_ospf6_vrf_area_areachoicecase_filterlist():
    """Filter prefixes between OSPF6 areas"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_filterlist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('name_of_an_ipv6', metavar='PREFIXLIST_NAME', required=True, type=FRR_TYPE('PREFIXLIST_NAME'))
def frr_config_router_ospf6_vrf_area_areachoicecase_filterlist_prefix(name_of_an_ipv6, filterlist_prefix_='filter-list_prefix'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_filterlist_prefix.name
    data_gen['filter-list_prefix'] = filterlist_prefix_='filter-list_prefix'
    data_gen['NAME_OF_AN_IPV6'] = name_of_an_ipv6
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_filterlist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(10, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ospf6_vrf_area_areachoicecase_filterlist_prefix_prefixinoutbound():
    """Filter networks sent to this area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_filterlist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_filterlist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_filterlist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='import-list', invoke_without_command=True)
@click.argument('name_of_the_accesslist', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ospf6_vrf_area_areachoicecase_importlist(name_of_the_accesslist, importlist_='import-list'):
    """Set the filter for networks from other areas announced to the specified one"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_importlist.name
    data_gen['import-list'] = importlist_='import-list'
    data_gen['NAME_OF_THE_ACCESS-LIST'] = name_of_the_accesslist
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_importlist.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_importlist_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='nssa', invoke_without_command=True)
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa(nssa_='nssa'):
    """Configure OSPF6 area as nssa"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_nssa.name
    data_gen['nssa'] = nssa_='nssa'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='default-information-originate', invoke_without_command=True)
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate(nssa_defaultinformationoriginate_='nssa_default-information-originate'):
    """Originate Type 7 default into NSSA area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate.name
    data_gen['nssa_default-information-originate'] = nssa_defaultinformationoriginate_='nssa_default-information-originate'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospfv3_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate_metric(ospfv3_metric, nssa_defaultinformationoriginate_metric_='nssa_default-information-originate_metric'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate_metric.name
    data_gen['nssa_default-information-originate_metric'] = nssa_defaultinformationoriginate_metric_='nssa_default-information-originate_metric'
    data_gen['OSPFV3_METRIC'] = ospfv3_metric
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate_metric.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate_metric_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate_metrictype(set_ospfv3_external_type, nssa_defaultinformationoriginate_metrictype_='nssa_default-information-originate_metric-type'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate_metrictype.name
    data_gen['nssa_default-information-originate_metric-type'] = nssa_defaultinformationoriginate_metrictype_='nssa_default-information-originate_metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate_metrictype.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_defaultinformationoriginate_metrictype_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='no-summary', invoke_without_command=True)
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_nosummary(nssa_nosummary_='nssa_no-summary'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_nssa_nosummary.name
    data_gen['nssa_no-summary'] = nssa_nosummary_='nssa_no-summary'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_nosummary.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_nosummary_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='range', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range(specify_ipv6_prefix, nssa_range_='nssa_range'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range.name
    data_gen['nssa_range'] = nssa_range_='nssa_range'
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range_cost(advertised_metric_for_this, cost_='cost'):
    """User specified metric for this range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range_cost.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range_cost_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range.group(cls=FRR_AbbreviationGroup, name='not-advertise', invoke_without_command=True)
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range_notadvertise(notadvertise_='not-advertise'):
    """Do not advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range_notadvertise.name
    data_gen['not-advertise'] = notadvertise_='not-advertise'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range_notadvertise.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_nssa_range_notadvertise_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='range', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_vrf_area_areachoicecase_range(specify_ipv6_prefix, range_='range'):
    """Configured address range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_range.name
    data_gen['range'] = range_='range'
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_range.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_range_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='advertise', invoke_without_command=True)
def frr_config_router_ospf6_vrf_area_areachoicecase_range_advertise(advertise_='advertise'):
    """Advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_range_advertise.name
    data_gen['advertise'] = advertise_='advertise'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_range_advertise.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_range_advertise_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_vrf_area_areachoicecase_range_cost(advertised_metric_for_this, cost_='cost'):
    """User specified metric for this range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_range_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_range_cost.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_range_cost_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='not-advertise', invoke_without_command=True)
def frr_config_router_ospf6_vrf_area_areachoicecase_range_notadvertise(notadvertise_='not-advertise'):
    """Do not advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_range_notadvertise.name
    data_gen['not-advertise'] = notadvertise_='not-advertise'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_range_notadvertise.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_range_notadvertise_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='stub', invoke_without_command=True)
def frr_config_router_ospf6_vrf_area_areachoicecase_stub(stub_='stub'):
    """Configure OSPF6 area as stub"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_stub.name
    data_gen['stub'] = stub_='stub'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_stub.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_stub_cr():
    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_stub.group(cls=FRR_AbbreviationGroup, name='no-summary', invoke_without_command=True)
def frr_config_router_ospf6_vrf_area_areachoicecase_stub_nosummary(stub_nosummary_='stub_no-summary'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_area_areachoicecase_stub_nosummary.name
    data_gen['stub_no-summary'] = stub_nosummary_='stub_no-summary'
    
    if 'OSPF6_NODE|area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_area_areachoicecase_stub_nosummary.command('./	<cr>')
def frr_config_router_ospf6_vrf_area_areachoicecase_stub_nosummary_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='auto-cost',)
def frr_config_router_ospf6_vrf_autocost(autocost_='auto-cost'):
    """Calculate OSPF interface cost according to bandwidth"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_autocost.name
    
    if 'OSPF6_NODE|auto-cost' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|auto-cost'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|auto-cost']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|auto-cost'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|auto-cost'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'auto-cost')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_autocost.group(cls=FRR_AbbreviationGroup, name='reference-bandwidth', invoke_without_command=True)
@click.argument('the_reference_bandwidth_in', metavar='(1-4294967)', required=True, type=FRR_TYPE((1, 4294967)))
def frr_config_router_ospf6_vrf_autocost_referencebandwidth(the_reference_bandwidth_in, referencebandwidth_='reference-bandwidth'):
    """Use reference bandwidth method to assign OSPF cost"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_autocost_referencebandwidth.name
    data_gen['reference-bandwidth'] = referencebandwidth_='reference-bandwidth'
    data_gen['THE_REFERENCE_BANDWIDTH_IN'] = the_reference_bandwidth_in
    
    if 'OSPF6_NODE|auto-cost' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|auto-cost'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|auto-cost']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|auto-cost'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|auto-cost'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'auto-cost')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_autocost_referencebandwidth.command('./	<cr>')
def frr_config_router_ospf6_vrf_autocost_referencebandwidth_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='default-information', invoke_without_command=True)
def frr_config_router_ospf6_vrf_defaultinformation():
    """Control distribution of default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_defaultinformation.name
    
    if 'OSPF6_NODE|default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_defaultinformation.command('./	<cr>')
def frr_config_router_ospf6_vrf_defaultinformation_cr():
    pass


@frr_config_router_ospf6_vrf_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_ospf6_vrf_defaultinformation_originate(defaultinformation_originate_='default-information_originate'):
    """Distribute a default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_defaultinformation_originate.name
    
    if 'OSPF6_NODE|default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_defaultinformation_originate.command('./	<cr>')
def frr_config_router_ospf6_vrf_defaultinformation_originate_cr():
    pass


@frr_config_router_ospf6_vrf_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='always', invoke_without_command=True)
def frr_config_router_ospf6_vrf_defaultinformation_originate_always(always_='always'):
    """Always advertise default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_defaultinformation_originate_always.name
    data_gen['always'] = always_='always'
    
    if 'OSPF6_NODE|default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_defaultinformation_originate_always.command('./	<cr>')
def frr_config_router_ospf6_vrf_defaultinformation_originate_always_cr():
    pass


@frr_config_router_ospf6_vrf_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospfv3_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_vrf_defaultinformation_originate_metric(ospfv3_metric, metric_='metric'):
    """OSPFv3 default metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_defaultinformation_originate_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['OSPFV3_METRIC'] = ospfv3_metric
    
    if 'OSPF6_NODE|default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_defaultinformation_originate_metric.command('./	<cr>')
def frr_config_router_ospf6_vrf_defaultinformation_originate_metric_cr():
    pass


@frr_config_router_ospf6_vrf_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_vrf_defaultinformation_originate_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 metric type for default routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_defaultinformation_originate_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_defaultinformation_originate_metrictype.command('./	<cr>')
def frr_config_router_ospf6_vrf_defaultinformation_originate_metrictype_cr():
    pass


@frr_config_router_ospf6_vrf_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ospf6_vrf_defaultinformation_originate_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_defaultinformation_originate_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'OSPF6_NODE|default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_defaultinformation_originate_routemap.command('./	<cr>')
def frr_config_router_ospf6_vrf_defaultinformation_originate_routemap_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='distance', invoke_without_command=True)
@click.argument('ospf6_administrative_distance', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_ospf6_vrf_distance(ospf6_administrative_distance, distance_='distance'):
    """Administrative distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_distance.name
    data_gen['OSPF6_ADMINISTRATIVE_DISTANCE'] = ospf6_administrative_distance
    
    if 'OSPF6_NODE|distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|distance']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_distance.command('./	<cr>')
def frr_config_router_ospf6_vrf_distance_cr():
    pass


@frr_config_router_ospf6_vrf_distance.group(cls=FRR_AbbreviationGroup, name='ospf6', invoke_without_command=True)
def frr_config_router_ospf6_vrf_distance_ospf6(distance_ospf6_='distance_ospf6'):
    """OSPF6 administrative distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_distance_ospf6.name
    
    if 'OSPF6_NODE|distance_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_distance_ospf6.command('./	<cr>')
def frr_config_router_ospf6_vrf_distance_ospf6_cr():
    pass


@frr_config_router_ospf6_vrf_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='external', invoke_without_command=True)
@click.argument('distance_for_external_routes', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_ospf6_vrf_distance_ospf6_external(distance_for_external_routes, external_='external'):
    """External routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_distance_ospf6_external.name
    data_gen['external'] = external_='external'
    data_gen['DISTANCE_FOR_EXTERNAL_ROUTES'] = distance_for_external_routes
    
    if 'OSPF6_NODE|distance_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_distance_ospf6_external.command('./	<cr>')
def frr_config_router_ospf6_vrf_distance_ospf6_external_cr():
    pass


@frr_config_router_ospf6_vrf_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='inter-area', invoke_without_command=True)
@click.argument('distance_for_interarea_routes', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_ospf6_vrf_distance_ospf6_interarea(distance_for_interarea_routes, interarea_='inter-area'):
    """Inter-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_distance_ospf6_interarea.name
    data_gen['inter-area'] = interarea_='inter-area'
    data_gen['DISTANCE_FOR_INTER-AREA_ROUTES'] = distance_for_interarea_routes
    
    if 'OSPF6_NODE|distance_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_distance_ospf6_interarea.command('./	<cr>')
def frr_config_router_ospf6_vrf_distance_ospf6_interarea_cr():
    pass


@frr_config_router_ospf6_vrf_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='intra-area', invoke_without_command=True)
@click.argument('distance_for_intraarea_routes', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_ospf6_vrf_distance_ospf6_intraarea(distance_for_intraarea_routes, intraarea_='intra-area'):
    """Intra-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_distance_ospf6_intraarea.name
    data_gen['intra-area'] = intraarea_='intra-area'
    data_gen['DISTANCE_FOR_INTRA-AREA_ROUTES'] = distance_for_intraarea_routes
    
    if 'OSPF6_NODE|distance_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|distance_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'distance_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_distance_ospf6_intraarea.command('./	<cr>')
def frr_config_router_ospf6_vrf_distance_ospf6_intraarea_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_config_router_ospf6_vrf_end(end_='end'):
    """End current mode and change to enable mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_end.name
    
    if 'OSPF6_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|end'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|end'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'end')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_end.command('./	<cr>')
def frr_config_router_ospf6_vrf_end_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_config_router_ospf6_vrf_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_exit.name
    
    if 'OSPF6_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|exit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|exit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'exit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_exit.command('./	<cr>')
def frr_config_router_ospf6_vrf_exit_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_config_router_ospf6_vrf_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_find.name
    
    if 'OSPF6_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_config_router_ospf6_vrf_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'OSPF6_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_find_fromsearchpattern.command('./	<cr>')
def frr_config_router_ospf6_vrf_find_fromsearchpattern_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='graceful-restart', invoke_without_command=True)
def frr_config_router_ospf6_vrf_gracefulrestart(gracefulrestart_='graceful-restart'):
    """ospf6 graceful restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_gracefulrestart.name
    
    if 'OSPF6_NODE|graceful-restart' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_gracefulrestart.command('./	<cr>')
def frr_config_router_ospf6_vrf_gracefulrestart_cr():
    pass


@frr_config_router_ospf6_vrf_gracefulrestart.group(cls=FRR_AbbreviationGroup, name='grace-period', invoke_without_command=True)
@click.argument('maximum_length_of_the', metavar='(1-1800)', required=True, type=FRR_TYPE((1, 1800)))
def frr_config_router_ospf6_vrf_gracefulrestart_graceperiod(maximum_length_of_the, graceperiod_='grace-period'):
    """Maximum length of the 'grace period'"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_gracefulrestart_graceperiod.name
    data_gen['grace-period'] = graceperiod_='grace-period'
    data_gen['MAXIMUM_LENGTH_OF_THE'] = maximum_length_of_the
    
    if 'OSPF6_NODE|graceful-restart' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_gracefulrestart_graceperiod.command('./	<cr>')
def frr_config_router_ospf6_vrf_gracefulrestart_graceperiod_cr():
    pass


@frr_config_router_ospf6_vrf_gracefulrestart.group(cls=FRR_AbbreviationGroup, name='helper',)
def frr_config_router_ospf6_vrf_gracefulrestart_helper(gracefulrestart_helper_='graceful-restart_helper'):
    """ospf6 GR Helper"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_gracefulrestart_helper.name
    
    if 'OSPF6_NODE|graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='enable', invoke_without_command=True)
def frr_config_router_ospf6_vrf_gracefulrestart_helper_enable(gracefulrestart_helper_enable_='graceful-restart_helper_enable'):
    """Enable Helper support"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_gracefulrestart_helper_enable.name
    
    if 'OSPF6_NODE|graceful-restart_helper_enable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper_enable')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_gracefulrestart_helper_enable.command('./	<cr>')
def frr_config_router_ospf6_vrf_gracefulrestart_helper_enable_cr():
    pass


@frr_config_router_ospf6_vrf_gracefulrestart_helper_enable.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D']), invoke_without_command=True)
def frr_config_router_ospf6_vrf_gracefulrestart_helper_enable_advertisementrouterid():
    """Advertisement Router-ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_gracefulrestart_helper_enable_advertisementrouterid.name
    data_gen['ADVERTISEMENT_ROUTER-ID'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|graceful-restart_helper_enable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper_enable'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper_enable')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_gracefulrestart_helper_enable_advertisementrouterid.command('./	<cr>')
def frr_config_router_ospf6_vrf_gracefulrestart_helper_enable_advertisementrouterid_cr():
    pass


@frr_config_router_ospf6_vrf_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='lsa-check-disable', invoke_without_command=True)
def frr_config_router_ospf6_vrf_gracefulrestart_helper_lsacheckdisable(lsacheckdisable_='lsa-check-disable'):
    """disable strict LSA check"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_gracefulrestart_helper_lsacheckdisable.name
    data_gen['lsa-check-disable'] = lsacheckdisable_='lsa-check-disable'
    
    if 'OSPF6_NODE|graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_gracefulrestart_helper_lsacheckdisable.command('./	<cr>')
def frr_config_router_ospf6_vrf_gracefulrestart_helper_lsacheckdisable_cr():
    pass


@frr_config_router_ospf6_vrf_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='planned-only', invoke_without_command=True)
def frr_config_router_ospf6_vrf_gracefulrestart_helper_plannedonly(plannedonly_='planned-only'):
    """supported only planned restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_gracefulrestart_helper_plannedonly.name
    data_gen['planned-only'] = plannedonly_='planned-only'
    
    if 'OSPF6_NODE|graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_gracefulrestart_helper_plannedonly.command('./	<cr>')
def frr_config_router_ospf6_vrf_gracefulrestart_helper_plannedonly_cr():
    pass


@frr_config_router_ospf6_vrf_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='supported-grace-time', invoke_without_command=True)
@click.argument('grace_interval', metavar='(10-1800)', required=True, type=FRR_TYPE((10, 1800)))
def frr_config_router_ospf6_vrf_gracefulrestart_helper_supportedgracetime(grace_interval, supportedgracetime_='supported-grace-time'):
    """supported grace timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_gracefulrestart_helper_supportedgracetime.name
    data_gen['supported-grace-time'] = supportedgracetime_='supported-grace-time'
    data_gen['GRACE_INTERVAL'] = grace_interval
    
    if 'OSPF6_NODE|graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_gracefulrestart_helper_supportedgracetime.command('./	<cr>')
def frr_config_router_ospf6_vrf_gracefulrestart_helper_supportedgracetime_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='interface',)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_ospf6_vrf_interface(interface_name, interface_='interface'):
    """Enable routing on an IPv6 interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_interface.name
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'OSPF6_NODE|interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|interface']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_interface.group(cls=FRR_AbbreviationGroup, name='area',)
def frr_config_router_ospf6_vrf_interface_area(area_='area'):
    """Specify the OSPF6 area ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_interface_area.name
    data_gen['area'] = area_='area'
    
    if 'OSPF6_NODE|interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|interface']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_interface_area.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D', (0, 4294967295)]), invoke_without_command=True)
def frr_config_router_ospf6_vrf_interface_area_areachoicecase():
    """OSPF6 area ID in IPv4 address notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_interface_area_areachoicecase.name
    data_gen['AREA_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|interface' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|interface'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|interface']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|interface'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|interface'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'interface')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_interface_area_areachoicecase.command('./	<cr>')
def frr_config_router_ospf6_vrf_interface_area_areachoicecase_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_config_router_ospf6_vrf_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_list.name
    
    if 'OSPF6_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_list.command('./	<cr>')
def frr_config_router_ospf6_vrf_list_cr():
    pass


@frr_config_router_ospf6_vrf_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_config_router_ospf6_vrf_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'OSPF6_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_list_permutations.command('./	<cr>')
def frr_config_router_ospf6_vrf_list_permutations_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='log-adjacency-changes', invoke_without_command=True)
def frr_config_router_ospf6_vrf_logadjacencychanges(logadjacencychanges_='log-adjacency-changes'):
    """Log changes in adjacency state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_logadjacencychanges.name
    
    if 'OSPF6_NODE|log-adjacency-changes' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'log-adjacency-changes')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_logadjacencychanges.command('./	<cr>')
def frr_config_router_ospf6_vrf_logadjacencychanges_cr():
    pass


@frr_config_router_ospf6_vrf_logadjacencychanges.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_config_router_ospf6_vrf_logadjacencychanges_detail(detail_='detail'):
    """Log all state changes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_logadjacencychanges_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'OSPF6_NODE|log-adjacency-changes' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|log-adjacency-changes'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'log-adjacency-changes')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_logadjacencychanges_detail.command('./	<cr>')
def frr_config_router_ospf6_vrf_logadjacencychanges_detail_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='maximum-paths', invoke_without_command=True)
@click.argument('number_of_paths', metavar='(1-256)', required=True, type=FRR_TYPE((1, 256)))
def frr_config_router_ospf6_vrf_maximumpaths(number_of_paths, maximumpaths_='maximum-paths'):
    """Max no of multiple paths for ECMP support"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_maximumpaths.name
    data_gen['NUMBER_OF_PATHS'] = number_of_paths
    
    if 'OSPF6_NODE|maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_maximumpaths.command('./	<cr>')
def frr_config_router_ospf6_vrf_maximumpaths_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_config_router_ospf6_vrf_no(no_='no'):
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no.name
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='aggregation', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_aggregation():
    """External route aggregation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_aggregation.name
    
    if 'OSPF6_NODE|no_aggregation' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_aggregation')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_aggregation.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_aggregation_cr():
    pass


@frr_config_router_ospf6_vrf_no_aggregation.group(cls=FRR_AbbreviationGroup, name='timer', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_aggregation_timer(no_aggregation_timer_='no_aggregation_timer'):
    """Delay timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_aggregation_timer.name
    
    if 'OSPF6_NODE|no_aggregation_timer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_aggregation_timer')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_aggregation_timer.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_aggregation_timer_cr():
    pass


@frr_config_router_ospf6_vrf_no_aggregation_timer.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(5, 1800)]), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_aggregation_timer_timerinterval():
    """Timer interval(in seconds)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_aggregation_timer_timerinterval.name
    data_gen['TIMER_INTERVAL'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_aggregation_timer' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_aggregation_timer'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_aggregation_timer')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_aggregation_timer_timerinterval.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_aggregation_timer_timerinterval_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='area',)
def frr_config_router_ospf6_vrf_no_area(area_='area'):
    """OSPF6 area parameters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area.name
    data_gen['area'] = area_='area'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['A.B.C.D', (0, 4294967295)]),)
def frr_config_router_ospf6_vrf_no_area_areachoicecase():
    """6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase.name
    data_gen['AREA_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='export-list', invoke_without_command=True)
@click.argument('name_of_the_accesslist', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ospf6_vrf_no_area_areachoicecase_exportlist(name_of_the_accesslist, exportlist_='export-list'):
    """Unset the filter for networks announced to other areas"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_exportlist.name
    data_gen['export-list'] = exportlist_='export-list'
    data_gen['NAME_OF_THE_ACCESS-LIST'] = name_of_the_accesslist
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_exportlist.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_exportlist_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='filter-list',)
def frr_config_router_ospf6_vrf_no_area_areachoicecase_filterlist():
    """Filter prefixes between OSPF6 areas"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_filterlist.group(cls=FRR_AbbreviationGroup, name='prefix',)
@click.argument('name_of_an_ipv6', metavar='PREFIXLIST_NAME', required=True, type=FRR_TYPE('PREFIXLIST_NAME'))
def frr_config_router_ospf6_vrf_no_area_areachoicecase_filterlist_prefix(name_of_an_ipv6, filterlist_prefix_='filter-list_prefix'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_filterlist_prefix.name
    data_gen['filter-list_prefix'] = filterlist_prefix_='filter-list_prefix'
    data_gen['NAME_OF_AN_IPV6'] = name_of_an_ipv6
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_filterlist_prefix.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(11, ['in', 'out']), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_area_areachoicecase_filterlist_prefix_prefixinoutbound():
    """Filter networks sent to this area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_filterlist_prefix_prefixinoutbound.name
    data_gen['PREFIX_IN_OUT_BOUND'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_filterlist_prefix_prefixinoutbound.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_filterlist_prefix_prefixinoutbound_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='import-list', invoke_without_command=True)
@click.argument('name_of_the_accesslist', metavar='ACCESSLIST6_NAME', required=True, type=FRR_TYPE('ACCESSLIST6_NAME'))
def frr_config_router_ospf6_vrf_no_area_areachoicecase_importlist(name_of_the_accesslist, importlist_='import-list'):
    """Unset the filter for networks announced to other areas"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_importlist.name
    data_gen['import-list'] = importlist_='import-list'
    data_gen['NAME_OF_THE_ACCESS-LIST'] = name_of_the_accesslist
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_importlist.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_importlist_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='nssa', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa(nssa_='nssa'):
    """Configure OSPF6 area as nssa"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa.name
    data_gen['nssa'] = nssa_='nssa'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='default-information-originate', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate(nssa_defaultinformationoriginate_='nssa_default-information-originate'):
    """Originate Type 7 default into NSSA area"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate.name
    data_gen['nssa_default-information-originate'] = nssa_defaultinformationoriginate_='nssa_default-information-originate'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospfv3_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate_metric(ospfv3_metric, nssa_defaultinformationoriginate_metric_='nssa_default-information-originate_metric'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate_metric.name
    data_gen['nssa_default-information-originate_metric'] = nssa_defaultinformationoriginate_metric_='nssa_default-information-originate_metric'
    data_gen['OSPFV3_METRIC'] = ospfv3_metric
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate_metric.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate_metric_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate_metrictype(set_ospfv3_external_type, nssa_defaultinformationoriginate_metrictype_='nssa_default-information-originate_metric-type'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate_metrictype.name
    data_gen['nssa_default-information-originate_metric-type'] = nssa_defaultinformationoriginate_metrictype_='nssa_default-information-originate_metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate_metrictype.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_defaultinformationoriginate_metrictype_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='no-summary', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_nosummary(nssa_nosummary_='nssa_no-summary'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_nosummary.name
    data_gen['nssa_no-summary'] = nssa_nosummary_='nssa_no-summary'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_nosummary.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_nosummary_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa.group(cls=FRR_AbbreviationGroup, name='range', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range(specify_ipv6_prefix, nssa_range_='nssa_range'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range.name
    data_gen['nssa_range'] = nssa_range_='nssa_range'
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range_cost(advertised_metric_for_this, cost_='cost'):
    """User specified metric for this range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range_cost.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range_cost_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range.group(cls=FRR_AbbreviationGroup, name='not-advertise', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range_notadvertise(notadvertise_='not-advertise'):
    """Do not advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range_notadvertise.name
    data_gen['not-advertise'] = notadvertise_='not-advertise'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range_notadvertise.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_nssa_range_notadvertise_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='range', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_vrf_no_area_areachoicecase_range(specify_ipv6_prefix, range_='range'):
    """Configured address range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_range.name
    data_gen['range'] = range_='range'
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_range.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_range_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='advertise', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_area_areachoicecase_range_advertise(advertise_='advertise'):
    """Advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_range_advertise.name
    data_gen['advertise'] = advertise_='advertise'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_range_advertise.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_range_advertise_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='cost', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_vrf_no_area_areachoicecase_range_cost(advertised_metric_for_this, cost_='cost'):
    """User specified metric for this range"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_range_cost.name
    data_gen['cost'] = cost_='cost'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_range_cost.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_range_cost_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_range.group(cls=FRR_AbbreviationGroup, name='not-advertise', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_area_areachoicecase_range_notadvertise(notadvertise_='not-advertise'):
    """Do not advertise"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_range_notadvertise.name
    data_gen['not-advertise'] = notadvertise_='not-advertise'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_range_notadvertise.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_range_notadvertise_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase.group(cls=FRR_AbbreviationGroup, name='stub', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_area_areachoicecase_stub(stub_='stub'):
    """Configure OSPF6 area as stub"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_stub.name
    data_gen['stub'] = stub_='stub'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_stub.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_stub_cr():
    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_stub.group(cls=FRR_AbbreviationGroup, name='no-summary', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_area_areachoicecase_stub_nosummary(stub_nosummary_='stub_no-summary'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_area_areachoicecase_stub_nosummary.name
    data_gen['stub_no-summary'] = stub_nosummary_='stub_no-summary'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_area_areachoicecase_stub_nosummary.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_area_areachoicecase_stub_nosummary_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='auto-cost', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_autocost():
    """Calculate OSPF interface cost according to bandwidth"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_autocost.name
    
    if 'OSPF6_NODE|no_auto-cost' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_auto-cost')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_autocost.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_autocost_cr():
    pass


@frr_config_router_ospf6_vrf_no_autocost.group(cls=FRR_AbbreviationGroup, name='reference-bandwidth', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_autocost_referencebandwidth(no_autocost_referencebandwidth_='no_auto-cost_reference-bandwidth'):
    """Use reference bandwidth method to assign OSPF cost"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_autocost_referencebandwidth.name
    
    if 'OSPF6_NODE|no_auto-cost_reference-bandwidth' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_auto-cost_reference-bandwidth')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_autocost_referencebandwidth.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_autocost_referencebandwidth_cr():
    pass


@frr_config_router_ospf6_vrf_no_autocost_referencebandwidth.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, [(1, 4294967)]), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_autocost_referencebandwidth_thereferencebandwidthin():
    """The reference bandwidth in terms of Mbits per second"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_autocost_referencebandwidth_thereferencebandwidthin.name
    data_gen['THE_REFERENCE_BANDWIDTH_IN'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_auto-cost_reference-bandwidth' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_auto-cost_reference-bandwidth'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_auto-cost_reference-bandwidth')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_autocost_referencebandwidth_thereferencebandwidthin.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_autocost_referencebandwidth_thereferencebandwidthin_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='default-information', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_defaultinformation():
    """Control distribution of default information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_defaultinformation.name
    
    if 'OSPF6_NODE|no_default-information' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_defaultinformation.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_defaultinformation_cr():
    pass


@frr_config_router_ospf6_vrf_no_defaultinformation.group(cls=FRR_AbbreviationGroup, name='originate', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_defaultinformation_originate(no_defaultinformation_originate_='no_default-information_originate'):
    """Distribute a default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_defaultinformation_originate.name
    
    if 'OSPF6_NODE|no_default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_defaultinformation_originate.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_defaultinformation_originate_cr():
    pass


@frr_config_router_ospf6_vrf_no_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='always', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_defaultinformation_originate_always(always_='always'):
    """Always advertise default route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_defaultinformation_originate_always.name
    data_gen['always'] = always_='always'
    
    if 'OSPF6_NODE|no_default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_defaultinformation_originate_always.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_defaultinformation_originate_always_cr():
    pass


@frr_config_router_ospf6_vrf_no_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospfv3_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_vrf_no_defaultinformation_originate_metric(ospfv3_metric, metric_='metric'):
    """OSPFv3 default metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_defaultinformation_originate_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['OSPFV3_METRIC'] = ospfv3_metric
    
    if 'OSPF6_NODE|no_default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_defaultinformation_originate_metric.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_defaultinformation_originate_metric_cr():
    pass


@frr_config_router_ospf6_vrf_no_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_vrf_no_defaultinformation_originate_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 metric type for default routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_defaultinformation_originate_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|no_default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_defaultinformation_originate_metrictype.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_defaultinformation_originate_metrictype_cr():
    pass


@frr_config_router_ospf6_vrf_no_defaultinformation_originate.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('pointer_to_routemap_entries', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ospf6_vrf_no_defaultinformation_originate_routemap(pointer_to_routemap_entries, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_defaultinformation_originate_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['POINTER_TO_ROUTE-MAP_ENTRIES'] = pointer_to_routemap_entries
    
    if 'OSPF6_NODE|no_default-information_originate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_default-information_originate'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_default-information_originate')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_defaultinformation_originate_routemap.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_defaultinformation_originate_routemap_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='distance', invoke_without_command=True)
@click.argument('ospf6_administrative_distance', metavar='(1-255)', required=True, type=FRR_TYPE((1, 255)))
def frr_config_router_ospf6_vrf_no_distance(ospf6_administrative_distance, no_distance_='no_distance'):
    """Administrative distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_distance.name
    data_gen['OSPF6_ADMINISTRATIVE_DISTANCE'] = ospf6_administrative_distance
    
    if 'OSPF6_NODE|no_distance' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_distance.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_distance_cr():
    pass


@frr_config_router_ospf6_vrf_no_distance.group(cls=FRR_AbbreviationGroup, name='ospf6', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_distance_ospf6():
    """OSPF6 distance"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_distance_ospf6.name
    
    if 'OSPF6_NODE|no_distance_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_distance_ospf6_cr():
    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='external', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_distance_ospf6_external(no_distance_ospf6_external_='no_distance_ospf6_external'):
    """External routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_distance_ospf6_external.name
    
    if 'OSPF6_NODE|no_distance_ospf6_external' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_external')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6_external.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_distance_ospf6_external_cr():
    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6_external.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, [(1, 255)]), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_distance_ospf6_external_distanceforexternalroutes():
    """Distance for external routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_distance_ospf6_external_distanceforexternalroutes.name
    data_gen['DISTANCE_FOR_EXTERNAL_ROUTES'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_distance_ospf6_external' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_external'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_external')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6_external_distanceforexternalroutes.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_distance_ospf6_external_distanceforexternalroutes_cr():
    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='inter-area', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_distance_ospf6_interarea(no_distance_ospf6_interarea_='no_distance_ospf6_inter-area'):
    """Inter-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_distance_ospf6_interarea.name
    
    if 'OSPF6_NODE|no_distance_ospf6_inter-area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_inter-area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6_interarea.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_distance_ospf6_interarea_cr():
    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6_interarea.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, [(1, 255)]), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_distance_ospf6_interarea_distanceforinterarearoutes():
    """Distance for inter-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_distance_ospf6_interarea_distanceforinterarearoutes.name
    data_gen['DISTANCE_FOR_INTER-AREA_ROUTES'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_distance_ospf6_inter-area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_inter-area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_inter-area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6_interarea_distanceforinterarearoutes.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_distance_ospf6_interarea_distanceforinterarearoutes_cr():
    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6.group(cls=FRR_AbbreviationGroup, name='intra-area', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_distance_ospf6_intraarea(no_distance_ospf6_intraarea_='no_distance_ospf6_intra-area'):
    """Intra-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_distance_ospf6_intraarea.name
    
    if 'OSPF6_NODE|no_distance_ospf6_intra-area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_intra-area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6_intraarea.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_distance_ospf6_intraarea_cr():
    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6_intraarea.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, [(1, 255)]), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_distance_ospf6_intraarea_distanceforintraarearoutes():
    """Distance for intra-area routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_distance_ospf6_intraarea_distanceforintraarearoutes.name
    data_gen['DISTANCE_FOR_INTRA-AREA_ROUTES'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_distance_ospf6_intra-area' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_distance_ospf6_intra-area'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_distance_ospf6_intra-area')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_distance_ospf6_intraarea_distanceforintraarearoutes.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_distance_ospf6_intraarea_distanceforintraarearoutes_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='graceful-restart', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_gracefulrestart(no_gracefulrestart_='no_graceful-restart'):
    """ospf6 graceful restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_gracefulrestart.name
    
    if 'OSPF6_NODE|no_graceful-restart' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_gracefulrestart_cr():
    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart.group(cls=FRR_AbbreviationGroup, name='helper',)
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper(no_gracefulrestart_helper_='no_graceful-restart_helper'):
    """ospf6 GR Helper"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_gracefulrestart_helper.name
    
    if 'OSPF6_NODE|no_graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='enable', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper_enable(no_gracefulrestart_helper_enable_='no_graceful-restart_helper_enable'):
    """Enable Helper support"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_gracefulrestart_helper_enable.name
    
    if 'OSPF6_NODE|no_graceful-restart_helper_enable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper_enable')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_helper_enable.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper_enable_cr():
    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_helper_enable.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, ['A.B.C.D']), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper_enable_advertisementrouterid():
    """Advertisement Router-ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_gracefulrestart_helper_enable_advertisementrouterid.name
    data_gen['ADVERTISEMENT_ROUTER-ID'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_graceful-restart_helper_enable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper_enable'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper_enable')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_helper_enable_advertisementrouterid.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper_enable_advertisementrouterid_cr():
    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='lsa-check-disable', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper_lsacheckdisable(lsacheckdisable_='lsa-check-disable'):
    """diasble strict LSA check"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_gracefulrestart_helper_lsacheckdisable.name
    data_gen['lsa-check-disable'] = lsacheckdisable_='lsa-check-disable'
    
    if 'OSPF6_NODE|no_graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_helper_lsacheckdisable.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper_lsacheckdisable_cr():
    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='planned-only', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper_plannedonly(plannedonly_='planned-only'):
    """supported only for planned restart"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_gracefulrestart_helper_plannedonly.name
    data_gen['planned-only'] = plannedonly_='planned-only'
    
    if 'OSPF6_NODE|no_graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_helper_plannedonly.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper_plannedonly_cr():
    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_helper.group(cls=FRR_AbbreviationGroup, name='supported-grace-time', invoke_without_command=True)
@click.argument('grace_interval', metavar='(10-1800)', required=True, type=FRR_TYPE((10, 1800)))
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper_supportedgracetime(grace_interval, supportedgracetime_='supported-grace-time'):
    """supported grace timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_gracefulrestart_helper_supportedgracetime.name
    data_gen['supported-grace-time'] = supportedgracetime_='supported-grace-time'
    data_gen['GRACE_INTERVAL'] = grace_interval
    
    if 'OSPF6_NODE|no_graceful-restart_helper' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart_helper'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart_helper')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_helper_supportedgracetime.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_gracefulrestart_helper_supportedgracetime_cr():
    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart.group(cls=FRR_AbbreviationGroup, name='period', invoke_without_command=True)
@click.argument('maximum_length_of_the', metavar='(1-1800)', required=True, type=FRR_TYPE((1, 1800)))
def frr_config_router_ospf6_vrf_no_gracefulrestart_period(maximum_length_of_the, period_='period'):
    """Maximum length of the 'grace period'"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_gracefulrestart_period.name
    data_gen['period'] = period_='period'
    data_gen['MAXIMUM_LENGTH_OF_THE'] = maximum_length_of_the
    
    if 'OSPF6_NODE|no_graceful-restart' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_graceful-restart'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_graceful-restart')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_gracefulrestart_period.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_gracefulrestart_period_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='interface',)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_config_router_ospf6_vrf_no_interface(interface_name, interface_='interface'):
    """Disable routing on an IPv6 interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_interface.name
    data_gen['interface'] = interface_='interface'
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_interface.group(cls=FRR_AbbreviationGroup, name='area',)
def frr_config_router_ospf6_vrf_no_interface_area(area_='area'):
    """Specify the OSPF6 area ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_interface_area.name
    data_gen['area'] = area_='area'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_interface_area.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D', (0, 4294967295)]), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_interface_area_areachoicecase():
    """OSPF6 area ID in IPv4 address notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_interface_area_areachoicecase.name
    data_gen['AREA_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_interface_area_areachoicecase.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_interface_area_areachoicecase_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='log-adjacency-changes', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_logadjacencychanges(no_logadjacencychanges_='no_log-adjacency-changes'):
    """Log changes in adjacency state"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_logadjacencychanges.name
    
    if 'OSPF6_NODE|no_log-adjacency-changes' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_log-adjacency-changes')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_logadjacencychanges.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_logadjacencychanges_cr():
    pass


@frr_config_router_ospf6_vrf_no_logadjacencychanges.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_logadjacencychanges_detail(detail_='detail'):
    """Log all state changes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_logadjacencychanges_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'OSPF6_NODE|no_log-adjacency-changes' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_log-adjacency-changes'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_log-adjacency-changes')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_logadjacencychanges_detail.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_logadjacencychanges_detail_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='maximum-paths', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_maximumpaths(no_maximumpaths_='no_maximum-paths'):
    """Max no of multiple paths for ECMP support"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_maximumpaths.name
    
    if 'OSPF6_NODE|no_maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_maximumpaths.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_maximumpaths_cr():
    pass


@frr_config_router_ospf6_vrf_no_maximumpaths.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, [(1, 256)]), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_maximumpaths_numberofpaths():
    """Number of paths"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_maximumpaths_numberofpaths.name
    data_gen['NUMBER_OF_PATHS'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_maximum-paths' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_maximum-paths'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_maximum-paths')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_maximumpaths_numberofpaths.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_maximumpaths_numberofpaths_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='ospf6', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_ospf6():
    """Open Shortest Path First (OSPF) for IPv6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_ospf6.name
    
    if 'OSPF6_NODE|no_ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_ospf6.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_ospf6_cr():
    pass


@frr_config_router_ospf6_vrf_no_ospf6.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_ospf6_routerid(no_ospf6_routerid_='no_ospf6_router-id'):
    """Configure OSPF6 Router-ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_ospf6_routerid.name
    
    if 'OSPF6_NODE|no_ospf6_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ospf6_router-id')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_ospf6_routerid.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_ospf6_routerid_cr():
    pass


@frr_config_router_ospf6_vrf_no_ospf6_routerid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['A.B.C.D']), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_ospf6_routerid_specifybyipv4address():
    """specify by IPv4 address notation(e.g. 0.0.0.0)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_ospf6_routerid_specifybyipv4address.name
    data_gen['SPECIFY_BY_IPV4_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_ospf6_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_router-id'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ospf6_router-id')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_ospf6_routerid_specifybyipv4address.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_ospf6_routerid_specifybyipv4address_cr():
    pass


@frr_config_router_ospf6_vrf_no_ospf6.group(cls=FRR_AbbreviationGroup, name='send-extra-data',)
def frr_config_router_ospf6_vrf_no_ospf6_sendextradata(no_ospf6_sendextradata_='no_ospf6_send-extra-data'):
    """Extra data to Zebra for display/use"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_ospf6_sendextradata.name
    
    if 'OSPF6_NODE|no_ospf6_send-extra-data' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ospf6_send-extra-data')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_ospf6_sendextradata.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_ospf6_sendextradata_zebra(zebra_='zebra'):
    """To zebra"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_ospf6_sendextradata_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'OSPF6_NODE|no_ospf6_send-extra-data' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_ospf6_send-extra-data'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_ospf6_send-extra-data')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_ospf6_sendextradata_zebra.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_ospf6_sendextradata_zebra_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_output.name
    
    if 'OSPF6_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_output.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_output_cr():
    pass


@frr_config_router_ospf6_vrf_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_output_file.name
    
    if 'OSPF6_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_output_file.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_output_file_cr():
    pass


@frr_config_router_ospf6_vrf_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['FILE']), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_output_file_pathtodumpoutput_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ospf6d', metavar='FRR_REDIST_STR_OSPF6D', required=True, type=FRR_TYPE('FRR_REDIST_STR_OSPF6D'))
def frr_config_router_ospf6_vrf_no_redistribute(frr_redist_help_str_ospf6d, redistribute_='redistribute'):
    """Redistribute"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_redistribute.name
    data_gen['redistribute'] = redistribute_='redistribute'
    data_gen['FRR_REDIST_HELP_STR_OSPF6D'] = frr_redist_help_str_ospf6d
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_redistribute.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_redistribute_cr():
    pass


@frr_config_router_ospf6_vrf_no_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospf_default_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_vrf_no_redistribute_metric(ospf_default_metric, metric_='metric'):
    """Metric for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['OSPF_DEFAULT_METRIC'] = ospf_default_metric
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_redistribute_metric.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_redistribute_metric_cr():
    pass


@frr_config_router_ospf6_vrf_no_redistribute.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospf_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_vrf_no_redistribute_metrictype(set_ospf_external_type, metrictype_='metric-type'):
    """OSPF exterior metric type for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_redistribute_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPF_EXTERNAL_TYPE'] = set_ospf_external_type
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_redistribute_metrictype.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_redistribute_metrictype_cr():
    pass


@frr_config_router_ospf6_vrf_no_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('route_map_name', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ospf6_vrf_no_redistribute_routemap(route_map_name, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['ROUTE_MAP_NAME'] = route_map_name
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_redistribute_routemap.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_redistribute_routemap_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='stub-router',)
def frr_config_router_ospf6_vrf_no_stubrouter(no_stubrouter_='no_stub-router'):
    """Make router a stub router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_stubrouter.name
    
    if 'OSPF6_NODE|no_stub-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_stub-router']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_stub-router')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_stubrouter.group(cls=FRR_AbbreviationGroup, name='administrative', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_stubrouter_administrative(administrative_='administrative'):
    """Administratively applied, for an indefinite period"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_stubrouter_administrative.name
    data_gen['administrative'] = administrative_='administrative'
    
    if 'OSPF6_NODE|no_stub-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_stub-router']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_stub-router'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_stub-router')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_stubrouter_administrative.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_stubrouter_administrative_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='summary-address', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_vrf_no_summaryaddress(specify_ipv6_prefix, summaryaddress_='summary-address'):
    """External summary address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_summaryaddress.name
    data_gen['summary-address'] = summaryaddress_='summary-address'
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_summaryaddress.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_summaryaddress_cr():
    pass


@frr_config_router_ospf6_vrf_no_summaryaddress.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_vrf_no_summaryaddress_metric(advertised_metric_for_this, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_summaryaddress_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_summaryaddress_metric.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_summaryaddress_metric_cr():
    pass


@frr_config_router_ospf6_vrf_no_summaryaddress.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_vrf_no_summaryaddress_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 exterior metric type for summarised routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_summaryaddress_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_summaryaddress_metrictype.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_summaryaddress_metrictype_cr():
    pass


@frr_config_router_ospf6_vrf_no_summaryaddress.group(cls=FRR_AbbreviationGroup, name='no-advertise', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_summaryaddress_noadvertise(noadvertise_='no-advertise'):
    """Adverise summary route to the AS"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_summaryaddress_noadvertise.name
    data_gen['no-advertise'] = noadvertise_='no-advertise'
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_summaryaddress_noadvertise.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_summaryaddress_noadvertise_cr():
    pass


@frr_config_router_ospf6_vrf_no_summaryaddress.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('router_tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_config_router_ospf6_vrf_no_summaryaddress_tag(router_tag_value, tag_='tag'):
    """Router tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_summaryaddress_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['ROUTER_TAG_VALUE'] = router_tag_value
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_summaryaddress_tag.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_summaryaddress_tag_cr():
    pass


@frr_config_router_ospf6_vrf_no_summaryaddress_tag.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_vrf_no_summaryaddress_tag_metric(advertised_metric_for_this, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_summaryaddress_tag_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_summaryaddress_tag_metric.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_summaryaddress_tag_metric_cr():
    pass


@frr_config_router_ospf6_vrf_no_summaryaddress_tag.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_vrf_no_summaryaddress_tag_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 exterior metric type for summarised routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_summaryaddress_tag_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_summaryaddress_tag_metrictype.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_summaryaddress_tag_metrictype_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='timers', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_timers():
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_timers.name
    
    if 'OSPF6_NODE|no_timers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_timers.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_timers_cr():
    pass


@frr_config_router_ospf6_vrf_no_timers.group(cls=FRR_AbbreviationGroup, name='lsa', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_timers_lsa():
    """OSPF6 LSA timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_timers_lsa.name
    
    if 'OSPF6_NODE|no_timers_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_lsa')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_timers_lsa.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_timers_lsa_cr():
    pass


@frr_config_router_ospf6_vrf_no_timers_lsa.group(cls=FRR_AbbreviationGroup, name='min-arrival', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_timers_lsa_minarrival(no_timers_lsa_minarrival_='no_timers_lsa_min-arrival'):
    """Minimum delay in receiving new version of a LSA"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_timers_lsa_minarrival.name
    
    if 'OSPF6_NODE|no_timers_lsa_min-arrival' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_lsa_min-arrival')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_timers_lsa_minarrival.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_timers_lsa_minarrival_cr():
    pass


@frr_config_router_ospf6_vrf_no_timers_lsa_minarrival.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, [(0, 600000)]), invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_timers_lsa_minarrival_delayinmilliseconds():
    """Delay in milliseconds"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_timers_lsa_minarrival_delayinmilliseconds.name
    data_gen['DELAY_IN_MILLISECONDS'] = FRR_CLI_ARGS[name]
    
    if 'OSPF6_NODE|no_timers_lsa_min-arrival' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_lsa_min-arrival'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_lsa_min-arrival')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_timers_lsa_minarrival_delayinmilliseconds.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_timers_lsa_minarrival_delayinmilliseconds_cr():
    pass


@frr_config_router_ospf6_vrf_no_timers.group(cls=FRR_AbbreviationGroup, name='throttle', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_timers_throttle():
    """Throttling adaptive timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_timers_throttle.name
    
    if 'OSPF6_NODE|no_timers_throttle' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_throttle')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_timers_throttle.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_timers_throttle_cr():
    pass


@frr_config_router_ospf6_vrf_no_timers_throttle.group(cls=FRR_AbbreviationGroup, name='spf', invoke_without_command=True)
def frr_config_router_ospf6_vrf_no_timers_throttle_spf(no_timers_throttle_spf_='no_timers_throttle_spf'):
    """OSPF6 SPF timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_timers_throttle_spf.name
    
    if 'OSPF6_NODE|no_timers_throttle_spf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_throttle_spf')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_timers_throttle_spf.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_timers_throttle_spf_cr():
    pass


@frr_config_router_ospf6_vrf_no_timers_throttle_spf.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(9, [(0, 600000)]), invoke_without_command=True)
@click.argument('initial_hold_time_between', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
@click.argument('maximum_hold_time', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
def frr_config_router_ospf6_vrf_no_timers_throttle_spf_delayfromfirstchange(initial_hold_time_between, maximum_hold_time):
    """Delay (msec) from first change received till SPF calculation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_timers_throttle_spf_delayfromfirstchange.name
    data_gen['DELAY_FROM_FIRST_CHANGE'] = FRR_CLI_ARGS[name]
    data_gen['INITIAL_HOLD_TIME_BETWEEN'] = initial_hold_time_between
    data_gen['MAXIMUM_HOLD_TIME'] = maximum_hold_time
    
    if 'OSPF6_NODE|no_timers_throttle_spf' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no_timers_throttle_spf'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_timers_throttle_spf')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_timers_throttle_spf_delayfromfirstchange.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_timers_throttle_spf_delayfromfirstchange_cr():
    pass


@frr_config_router_ospf6_vrf_no.group(cls=FRR_AbbreviationGroup, name='write-multiplier', invoke_without_command=True)
@click.argument('maximum_number_of_interface', metavar='(1-100)', required=True, type=FRR_TYPE((1, 100)))
def frr_config_router_ospf6_vrf_no_writemultiplier(maximum_number_of_interface, writemultiplier_='write-multiplier'):
    """Write multiplier"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_no_writemultiplier.name
    data_gen['write-multiplier'] = writemultiplier_='write-multiplier'
    data_gen['MAXIMUM_NUMBER_OF_INTERFACE'] = maximum_number_of_interface
    
    if 'OSPF6_NODE|no' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|no'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|no']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|no'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|no'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_no_writemultiplier.command('./	<cr>')
def frr_config_router_ospf6_vrf_no_writemultiplier_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='ospf6',)
def frr_config_router_ospf6_vrf_ospf6(ospf6_='ospf6'):
    """Open Shortest Path First (OSPF) for IPv6"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_ospf6.name
    
    if 'OSPF6_NODE|ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_ospf6.group(cls=FRR_AbbreviationGroup, name='router-id', invoke_without_command=True)
@click.argument('specify_by_ipv4_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_config_router_ospf6_vrf_ospf6_routerid(specify_by_ipv4_address, routerid_='router-id'):
    """Configure OSPF6 Router-ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_ospf6_routerid.name
    data_gen['router-id'] = routerid_='router-id'
    data_gen['SPECIFY_BY_IPV4_ADDRESS'] = specify_by_ipv4_address
    
    if 'OSPF6_NODE|ospf6' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|ospf6'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|ospf6']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|ospf6'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|ospf6'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ospf6')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_ospf6_routerid.command('./	<cr>')
def frr_config_router_ospf6_vrf_ospf6_routerid_cr():
    pass


@frr_config_router_ospf6_vrf_ospf6.group(cls=FRR_AbbreviationGroup, name='send-extra-data',)
def frr_config_router_ospf6_vrf_ospf6_sendextradata(ospf6_sendextradata_='ospf6_send-extra-data'):
    """Extra data to Zebra for display/use"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_ospf6_sendextradata.name
    
    if 'OSPF6_NODE|ospf6_send-extra-data' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ospf6_send-extra-data')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_ospf6_sendextradata.group(cls=FRR_AbbreviationGroup, name='zebra', invoke_without_command=True)
def frr_config_router_ospf6_vrf_ospf6_sendextradata_zebra(zebra_='zebra'):
    """To zebra"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_ospf6_sendextradata_zebra.name
    data_gen['zebra'] = zebra_='zebra'
    
    if 'OSPF6_NODE|ospf6_send-extra-data' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|ospf6_send-extra-data'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'ospf6_send-extra-data')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_ospf6_sendextradata_zebra.command('./	<cr>')
def frr_config_router_ospf6_vrf_ospf6_sendextradata_zebra_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_config_router_ospf6_vrf_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_output.name
    
    if 'OSPF6_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_config_router_ospf6_vrf_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'OSPF6_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_output_file.command('./	<cr>')
def frr_config_router_ospf6_vrf_output_file_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_config_router_ospf6_vrf_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_quit.name
    
    if 'OSPF6_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|quit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|quit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'quit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_quit.command('./	<cr>')
def frr_config_router_ospf6_vrf_quit_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='redistribute', invoke_without_command=True)
@click.argument('frr_redist_help_str_ospf6d', metavar='FRR_REDIST_STR_OSPF6D', required=True, type=FRR_TYPE('FRR_REDIST_STR_OSPF6D'))
def frr_config_router_ospf6_vrf_redistribute(frr_redist_help_str_ospf6d, redistribute_='redistribute'):
    """Redistribute"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_redistribute.name
    data_gen['FRR_REDIST_HELP_STR_OSPF6D'] = frr_redist_help_str_ospf6d
    
    if 'OSPF6_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_redistribute.command('./	<cr>')
def frr_config_router_ospf6_vrf_redistribute_cr():
    pass


@frr_config_router_ospf6_vrf_redistribute.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('ospf_default_metric', metavar='(0-16777214)', required=True, type=FRR_TYPE((0, 16777214)))
def frr_config_router_ospf6_vrf_redistribute_metric(ospf_default_metric, metric_='metric'):
    """Metric for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_redistribute_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['OSPF_DEFAULT_METRIC'] = ospf_default_metric
    
    if 'OSPF6_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_redistribute_metric.command('./	<cr>')
def frr_config_router_ospf6_vrf_redistribute_metric_cr():
    pass


@frr_config_router_ospf6_vrf_redistribute.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospf_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_vrf_redistribute_metrictype(set_ospf_external_type, metrictype_='metric-type'):
    """OSPF exterior metric type for redistributed routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_redistribute_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPF_EXTERNAL_TYPE'] = set_ospf_external_type
    
    if 'OSPF6_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_redistribute_metrictype.command('./	<cr>')
def frr_config_router_ospf6_vrf_redistribute_metrictype_cr():
    pass


@frr_config_router_ospf6_vrf_redistribute.group(cls=FRR_AbbreviationGroup, name='route-map', invoke_without_command=True)
@click.argument('route_map_name', metavar='RMAP_NAME', required=True, type=FRR_TYPE('RMAP_NAME'))
def frr_config_router_ospf6_vrf_redistribute_routemap(route_map_name, routemap_='route-map'):
    """Route map reference"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_redistribute_routemap.name
    data_gen['route-map'] = routemap_='route-map'
    data_gen['ROUTE_MAP_NAME'] = route_map_name
    
    if 'OSPF6_NODE|redistribute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|redistribute']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|redistribute'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|redistribute'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'redistribute')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_redistribute_routemap.command('./	<cr>')
def frr_config_router_ospf6_vrf_redistribute_routemap_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='stub-router',)
def frr_config_router_ospf6_vrf_stubrouter(stubrouter_='stub-router'):
    """Make router a stub router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_stubrouter.name
    
    if 'OSPF6_NODE|stub-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|stub-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|stub-router']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|stub-router'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|stub-router'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'stub-router')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_stubrouter.group(cls=FRR_AbbreviationGroup, name='administrative', invoke_without_command=True)
def frr_config_router_ospf6_vrf_stubrouter_administrative(administrative_='administrative'):
    """Administratively applied, for an indefinite period"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_stubrouter_administrative.name
    data_gen['administrative'] = administrative_='administrative'
    
    if 'OSPF6_NODE|stub-router' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|stub-router'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|stub-router']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|stub-router'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|stub-router'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'stub-router')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_stubrouter_administrative.command('./	<cr>')
def frr_config_router_ospf6_vrf_stubrouter_administrative_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='summary-address', invoke_without_command=True)
@click.argument('specify_ipv6_prefix', metavar='X:X::X:X/M', required=True, type=FRR_TYPE('X:X::X:X/M'))
def frr_config_router_ospf6_vrf_summaryaddress(specify_ipv6_prefix, summaryaddress_='summary-address'):
    """External summary address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_summaryaddress.name
    data_gen['SPECIFY_IPV6_PREFIX'] = specify_ipv6_prefix
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_summaryaddress.command('./	<cr>')
def frr_config_router_ospf6_vrf_summaryaddress_cr():
    pass


@frr_config_router_ospf6_vrf_summaryaddress.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_vrf_summaryaddress_metric(advertised_metric_for_this, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_summaryaddress_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_summaryaddress_metric.command('./	<cr>')
def frr_config_router_ospf6_vrf_summaryaddress_metric_cr():
    pass


@frr_config_router_ospf6_vrf_summaryaddress.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_vrf_summaryaddress_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 exterior metric type for summarised routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_summaryaddress_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_summaryaddress_metrictype.command('./	<cr>')
def frr_config_router_ospf6_vrf_summaryaddress_metrictype_cr():
    pass


@frr_config_router_ospf6_vrf_summaryaddress.group(cls=FRR_AbbreviationGroup, name='no-advertise', invoke_without_command=True)
def frr_config_router_ospf6_vrf_summaryaddress_noadvertise(noadvertise_='no-advertise'):
    """Don't advertise summary route"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_summaryaddress_noadvertise.name
    data_gen['no-advertise'] = noadvertise_='no-advertise'
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_summaryaddress_noadvertise.command('./	<cr>')
def frr_config_router_ospf6_vrf_summaryaddress_noadvertise_cr():
    pass


@frr_config_router_ospf6_vrf_summaryaddress.group(cls=FRR_AbbreviationGroup, name='tag', invoke_without_command=True)
@click.argument('router_tag_value', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_config_router_ospf6_vrf_summaryaddress_tag(router_tag_value, tag_='tag'):
    """Router tag"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_summaryaddress_tag.name
    data_gen['tag'] = tag_='tag'
    data_gen['ROUTER_TAG_VALUE'] = router_tag_value
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_summaryaddress_tag.command('./	<cr>')
def frr_config_router_ospf6_vrf_summaryaddress_tag_cr():
    pass


@frr_config_router_ospf6_vrf_summaryaddress_tag.group(cls=FRR_AbbreviationGroup, name='metric', invoke_without_command=True)
@click.argument('advertised_metric_for_this', metavar='(0-16777215)', required=True, type=FRR_TYPE((0, 16777215)))
def frr_config_router_ospf6_vrf_summaryaddress_tag_metric(advertised_metric_for_this, metric_='metric'):
    """Metric"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_summaryaddress_tag_metric.name
    data_gen['metric'] = metric_='metric'
    data_gen['ADVERTISED_METRIC_FOR_THIS'] = advertised_metric_for_this
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_summaryaddress_tag_metric.command('./	<cr>')
def frr_config_router_ospf6_vrf_summaryaddress_tag_metric_cr():
    pass


@frr_config_router_ospf6_vrf_summaryaddress_tag.group(cls=FRR_AbbreviationGroup, name='metric-type', invoke_without_command=True)
@click.argument('set_ospfv3_external_type', metavar='(1-2)', required=True, type=FRR_TYPE((1, 2)))
def frr_config_router_ospf6_vrf_summaryaddress_tag_metrictype(set_ospfv3_external_type, metrictype_='metric-type'):
    """OSPFv3 exterior metric type for summarised routes"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_summaryaddress_tag_metrictype.name
    data_gen['metric-type'] = metrictype_='metric-type'
    data_gen['SET_OSPFV3_EXTERNAL_TYPE'] = set_ospfv3_external_type
    
    if 'OSPF6_NODE|summary-address' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|summary-address']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|summary-address'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|summary-address'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'summary-address')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_summaryaddress_tag_metrictype.command('./	<cr>')
def frr_config_router_ospf6_vrf_summaryaddress_tag_metrictype_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='timers',)
def frr_config_router_ospf6_vrf_timers():
    """Adjust routing timers"""
    global COMMON_DATA_MAP
    
    pass


@frr_config_router_ospf6_vrf_timers.group(cls=FRR_AbbreviationGroup, name='lsa',)
def frr_config_router_ospf6_vrf_timers_lsa(timers_lsa_='timers_lsa'):
    """OSPF6 LSA timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_timers_lsa.name
    
    if 'OSPF6_NODE|timers_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|timers_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers_lsa')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_timers_lsa.group(cls=FRR_AbbreviationGroup, name='min-arrival', invoke_without_command=True)
@click.argument('delay_in_milliseconds', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
def frr_config_router_ospf6_vrf_timers_lsa_minarrival(delay_in_milliseconds, minarrival_='min-arrival'):
    """Minimum delay in receiving new version of a LSA"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_timers_lsa_minarrival.name
    data_gen['min-arrival'] = minarrival_='min-arrival'
    data_gen['DELAY_IN_MILLISECONDS'] = delay_in_milliseconds
    
    if 'OSPF6_NODE|timers_lsa' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|timers_lsa']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|timers_lsa'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers_lsa')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_timers_lsa_minarrival.command('./	<cr>')
def frr_config_router_ospf6_vrf_timers_lsa_minarrival_cr():
    pass


@frr_config_router_ospf6_vrf_timers.group(cls=FRR_AbbreviationGroup, name='throttle',)
def frr_config_router_ospf6_vrf_timers_throttle(timers_throttle_='timers_throttle'):
    """Throttling adaptive timer"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_timers_throttle.name
    
    if 'OSPF6_NODE|timers_throttle' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|timers_throttle']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers_throttle')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_timers_throttle.group(cls=FRR_AbbreviationGroup, name='spf', invoke_without_command=True)
@click.argument('delay_from_first_change', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
@click.argument('initial_hold_time_between', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
@click.argument('maximum_hold_time', metavar='(0-600000)', required=True, type=FRR_TYPE((0, 600000)))
def frr_config_router_ospf6_vrf_timers_throttle_spf(maximum_hold_time, delay_from_first_change, initial_hold_time_between, spf_='spf'):
    """OSPF6 SPF timers"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_timers_throttle_spf.name
    data_gen['spf'] = spf_='spf'
    data_gen['DELAY_FROM_FIRST_CHANGE'] = delay_from_first_change
    data_gen['INITIAL_HOLD_TIME_BETWEEN'] = initial_hold_time_between
    data_gen['MAXIMUM_HOLD_TIME'] = maximum_hold_time
    
    if 'OSPF6_NODE|timers_throttle' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|timers_throttle']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|timers_throttle'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'timers_throttle')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_timers_throttle_spf.command('./	<cr>')
def frr_config_router_ospf6_vrf_timers_throttle_spf_cr():
    pass


@frr_config_router_ospf6_vrf.group(cls=FRR_AbbreviationGroup, name='write-multiplier', invoke_without_command=True)
@click.argument('maximum_number_of_interface', metavar='(1-100)', required=True, type=FRR_TYPE((1, 100)))
def frr_config_router_ospf6_vrf_writemultiplier(maximum_number_of_interface, writemultiplier_='write-multiplier'):
    """Write multiplier"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_vrf_writemultiplier.name
    data_gen['MAXIMUM_NUMBER_OF_INTERFACE'] = maximum_number_of_interface
    
    if 'OSPF6_NODE|write-multiplier' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|write-multiplier'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|write-multiplier']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|write-multiplier'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|write-multiplier'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'write-multiplier')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_vrf_writemultiplier.command('./	<cr>')
def frr_config_router_ospf6_vrf_writemultiplier_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='write-multiplier', invoke_without_command=True)
@click.argument('maximum_number_of_interface', metavar='(1-100)', required=True, type=FRR_TYPE((1, 100)))
def frr_config_router_ospf6_writemultiplier(maximum_number_of_interface, writemultiplier_='write-multiplier'):
    """Write multiplier"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_ospf6_writemultiplier.name
    data_gen['MAXIMUM_NUMBER_OF_INTERFACE'] = maximum_number_of_interface
    
    if 'OSPF6_NODE|write-multiplier' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OSPF6_NODE|write-multiplier'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OSPF6_NODE|write-multiplier']:
            key = key.upper()
        COMMON_DATA_MAP['OSPF6_NODE|write-multiplier'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OSPF6_NODE|write-multiplier'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'write-multiplier')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OSPF6_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OSPF6_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_ospf6_writemultiplier.command('./	<cr>')
def frr_config_router_ospf6_writemultiplier_cr():
    pass

