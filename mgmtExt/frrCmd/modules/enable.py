import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_enable_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_enable_find.name
    
    if 'ENABLE_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['ENABLE_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['ENABLE_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['ENABLE_NODE|find'][key] = val
    
    # set ENABLE_NODE -> find table
    COMMON_DATA_MAP['ENABLE_NODE'] = 'find'
    pass


@frr_enable_find.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(3, ['REGEX']), invoke_without_command=True)
@click.argument('to_search_pattern', metavar='REGEX', required=True, type=FRR_TYPE('REGEX'))
def frr_enable_find_fromsearchpattern(to_search_pattern):
    """Search pattern (POSIX regex)"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_enable_find_fromsearchpattern.name
    data_gen['FROM_SEARCH_PATTERN'] = FRR_CLI_ARGS[name]
    data_gen['TO_SEARCH_PATTERN'] = to_search_pattern
    
    if 'ENABLE_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['ENABLE_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['ENABLE_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['ENABLE_NODE|find'][key] = val
    
    # set ENABLE_NODE -> find table
    COMMON_DATA_MAP['ENABLE_NODE'] = 'find'
    pass


@frr_enable_find_fromsearchpattern.command('./	<cr>')
def frr_enable_find_fromsearchpattern_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_enable_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_enable_list.name
    
    if 'ENABLE_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['ENABLE_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['ENABLE_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['ENABLE_NODE|list'][key] = val
    
    # set ENABLE_NODE -> list table
    COMMON_DATA_MAP['ENABLE_NODE'] = 'list'
    pass


@frr_enable_list.command('./	<cr>')
def frr_enable_list_cr():
    pass


@frr_enable_list.group(cls=FRR_AbbreviationGroup, name='permutations', invoke_without_command=True)
def frr_enable_list_permutations(permutations_='permutations'):
    """Print all possible command permutations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_enable_list_permutations.name
    data_gen['permutations'] = permutations_='permutations'
    
    if 'ENABLE_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['ENABLE_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['ENABLE_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['ENABLE_NODE|list'][key] = val
    
    # set ENABLE_NODE -> list table
    COMMON_DATA_MAP['ENABLE_NODE'] = 'list'
    pass


@frr_enable_list_permutations.command('./	<cr>')
def frr_enable_list_permutations_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='no', invoke_without_command=True)
def frr_enable_no():
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_enable_no.name
    
    if 'ENABLE_NODE|le' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['ENABLE_NODE|le'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['ENABLE_NODE|le']:
            key = key.upper()
        COMMON_DATA_MAP['ENABLE_NODE|le'][key] = val
    
    # set ENABLE_NODE -> le table
    COMMON_DATA_MAP['ENABLE_NODE'] = 'le'
    pass


@frr_enable_no.command('./	<cr>')
def frr_enable_no_cr():
    pass


@frr_enable_no.group(cls=FRR_AbbreviationGroup, name='output', invoke_without_command=True)
def frr_enable_no_output():
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_enable_no_output.name
    
    if 'ENABLE_NODE|no_output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['ENABLE_NODE|no_output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['ENABLE_NODE|no_output']:
            key = key.upper()
        COMMON_DATA_MAP['ENABLE_NODE|no_output'][key] = val
    
    # set ENABLE_NODE -> no_output table
    COMMON_DATA_MAP['ENABLE_NODE'] = 'no_output'
    pass


@frr_enable_no_output.command('./	<cr>')
def frr_enable_no_output_cr():
    pass


@frr_enable_no_output.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
def frr_enable_no_output_file(no_output_file_='no_output_file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_enable_no_output_file.name
    
    if 'ENABLE_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['ENABLE_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['ENABLE_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['ENABLE_NODE|no_output_file'][key] = val
    
    # set ENABLE_NODE -> no_output_file table
    COMMON_DATA_MAP['ENABLE_NODE'] = 'no_output_file'
    pass


@frr_enable_no_output_file.command('./	<cr>')
def frr_enable_no_output_file_cr():
    pass


@frr_enable_no_output_file.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['FILE']), invoke_without_command=True)
def frr_enable_no_output_file_pathtodumpoutput():
    """Path to dump output to"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_enable_no_output_file_pathtodumpoutput.name
    data_gen['PATH_TO_DUMP_OUTPUT'] = FRR_CLI_ARGS[name]
    
    if 'ENABLE_NODE|no_output_file' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['ENABLE_NODE|no_output_file'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['ENABLE_NODE|no_output_file']:
            key = key.upper()
        COMMON_DATA_MAP['ENABLE_NODE|no_output_file'][key] = val
    
    # set ENABLE_NODE -> no_output_file table
    COMMON_DATA_MAP['ENABLE_NODE'] = 'no_output_file'
    pass


@frr_enable_no_output_file_pathtodumpoutput.command('./	<cr>')
def frr_enable_no_output_file_pathtodumpoutput_cr():
    pass

