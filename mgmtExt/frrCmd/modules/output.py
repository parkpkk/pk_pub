import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='file', invoke_without_command=True)
@click.argument('path_to_dump_output', metavar='FILE', required=True, type=FRR_TYPE('FILE'))
def frr_output_file(path_to_dump_output, file_='file'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_output_file.name
    data_gen['file'] = file_='file'
    data_gen['PATH_TO_DUMP_OUTPUT'] = path_to_dump_output
    
    if 'VIEW_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|output'][key] = val
    
    # set VIEW_NODE -> output table
    COMMON_DATA_MAP['VIEW_NODE'] = 'output'
    pass


@frr_output_file.command('./	<cr>')
def frr_output_file_cr():
    pass

