import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='NODE',)
def frr_1DE_NODE():
    """"""
    global COMMON_DATA_MAP
    
    pass


@frr_1DE_NODE.group(cls=FRR_AbbreviationGroup, name='RELATED',)
def frr_1DE_NODE_RELATED():
    """"""
    global COMMON_DATA_MAP
    
    pass


@frr_1DE_NODE_RELATED.group(cls=FRR_AbbreviationGroup, name='COMMAND',)

def frr_1DE_NODE_RELATED_COMMAND():
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_1DE_NODE_RELATED_COMMAND.name
    
    if '1DE|' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['1DE|'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['1DE|']:
            key = key.upper()
        COMMON_DATA_MAP['1DE|'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['1DE|'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, '')
    previous_key = key_store[:-1]
    if PREFIX_TMP and '1DE' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['1DE'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_1DE_NODE_RELATED_COMMAND.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_1DE_NODE_RELATED_COMMAND_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_1DE_NODE_RELATED_COMMAND_output.name
    data_gen['output'] = output_='output'
    
    if 'output|' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['output|'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['output|']:
            key = key.upper()
        COMMON_DATA_MAP['output|'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['output|'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, '')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'output' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['output'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_1DE_NODE_RELATED_COMMAND_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_1DE_NODE_RELATED_COMMAND_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_1DE_NODE_RELATED_COMMAND_output_file.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'output|file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['output|file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['output|file']:
            key = key.upper()
        COMMON_DATA_MAP['output|file'][key] = val
    
    #######################
    key_store = []
    global PREFIX_TMP
    for k, v in COMMON_DATA_MAP['output|file'].items():
        if k.islower() and k != v:
            key_store.append(k)
        if k != v or '_NODE' not in v:
            key_store.append(v)
    key_store.insert(0, 'file')
    previous_key = key_store[:-1]
    if PREFIX_TMP and 'output' not in BASE_NODE:
        pre_key = PREFIX_TMP.split('|')[-1]
        if key_store[0].startswith(pre_key):
            if '|' not in PREFIX_TMP:
                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')
            else:
                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')
        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:
            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'
            if len(previous_key) == 0:
                previous_key = [PREFIX_TMP]
            else:
                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'
        if PREFIX_TMP.endswith(f'|{key_store[0]}'):
            key_store[0] = PREFIX_TMP
    
    COMMON_DATA_MAP['output'] = tuple(key_store)
    PREFIX_TMP = '|'.join(key_store)

    pass


@frr_1DE_NODE_RELATED_COMMAND_output_file.command('./	<cr>')
def frr_1DE_NODE_RELATED_COMMAND_output_file_cr():
    pass

