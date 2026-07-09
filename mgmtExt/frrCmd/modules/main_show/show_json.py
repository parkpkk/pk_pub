import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='nexthop-group', invoke_without_command=True)
def frr_show_json_nexthopgroup(nexthopgroup_='nexthop-group'):
    """Nexthop Group Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_json_nexthopgroup.name
    data_gen['nexthop-group'] = nexthopgroup_='nexthop-group'
    
    if 'VIEW_NODE|show_json' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_json'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_json']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_json'][key] = val
    
    # set VIEW_NODE -> show_json table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_json'
    pass


@frr_show_json_nexthopgroup.command('./	<cr>')
def frr_show_json_nexthopgroup_cr():
    pass

