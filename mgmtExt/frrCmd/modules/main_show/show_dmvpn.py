import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_dmvpn_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_dmvpn_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_dmvpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_dmvpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_dmvpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_dmvpn'][key] = val
    
    # set VIEW_NODE -> show_dmvpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_dmvpn'
    pass


@frr_show_dmvpn_json.command('./	<cr>')
def frr_show_dmvpn_json_cr():
    pass

