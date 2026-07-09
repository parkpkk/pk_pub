import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_config_router_openfabric_end(end_='end'):
    """End current mode and change to enable mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_end.name
    
    if 'OPENFABRIC_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|end'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|end'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'end')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_end.command('./	<cr>')
def frr_config_router_openfabric_end_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_config_router_openfabric_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_exit.name
    
    if 'OPENFABRIC_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|exit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|exit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'exit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_exit.command('./	<cr>')
def frr_config_router_openfabric_exit_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_config_router_openfabric_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_find.name
    
    if 'OPENFABRIC_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_config_router_openfabric_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'OPENFABRIC_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|find'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|find'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'find')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_find_fromsearchpattern.command('./	<cr>')
def frr_config_router_openfabric_find_fromsearchpattern_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_config_router_openfabric_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_list.name
    
    if 'OPENFABRIC_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_list.command('./	<cr>')
def frr_config_router_openfabric_list_cr():
    pass


@frr_config_router_openfabric_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_config_router_openfabric_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'OPENFABRIC_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|list'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|list'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'list')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_list_permutations.command('./	<cr>')
def frr_config_router_openfabric_list_permutations_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='no', invoke_without_command=True)
def frr_config_router_openfabric_no():
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_no.name
    
    if 'OPENFABRIC_NODE|out' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|out'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|out']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|out'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|out'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'out')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_no.command('./	<cr>')
def frr_config_router_openfabric_no_cr():
    pass


@frr_config_router_openfabric_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_config_router_openfabric_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_no_output.name
    
    if 'OPENFABRIC_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|no_output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|no_output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_no_output.command('./	<cr>')
def frr_config_router_openfabric_no_output_cr():
    pass


@frr_config_router_openfabric_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_config_router_openfabric_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_no_output_file.name
    
    if 'OPENFABRIC_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_no_output_file.command('./	<cr>')
def frr_config_router_openfabric_no_output_file_cr():
    pass


@frr_config_router_openfabric_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['FILE']), invoke_without_command=True)
def frr_config_router_openfabric_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'OPENFABRIC_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|no_output_file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|no_output_file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'no_output_file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_config_router_openfabric_no_output_file_pathtodumpoutput_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_config_router_openfabric_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_output.name
    
    if 'OPENFABRIC_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_config_router_openfabric_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'OPENFABRIC_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|output'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|output'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'output')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_output_file.command('./	<cr>')
def frr_config_router_openfabric_output_file_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_config_router_openfabric_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_config_router_openfabric_quit.name
    
    if 'OPENFABRIC_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['OPENFABRIC_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['OPENFABRIC_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['OPENFABRIC_NODE|quit'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['OPENFABRIC_NODE|quit'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'quit')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'OPENFABRIC_NODE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['OPENFABRIC_NODE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_config_router_openfabric_quit.command('./	<cr>')
def frr_config_router_openfabric_quit_cr():
    pass

