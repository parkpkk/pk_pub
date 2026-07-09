import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='vrf', invoke_without_command=True)
@click.argument('the_vrf_name', metavar='NAME', required=True, type=FRR_TYPE('NAME'))
def frr_show_routerid_vrf(the_vrf_name, vrf_='vrf'):
    """Specify the VRF"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_routerid_vrf.name
    data_gen['vrf'] = vrf_='vrf'
    data_gen['THE_VRF_NAME'] = the_vrf_name
    
    if 'VIEW_NODE|show_router-id' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_router-id'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_router-id']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_router-id'][key] = val
    
    # set VIEW_NODE -> show_router-id table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_router-id'
    pass


@frr_show_routerid_vrf.command('./	<cr>')
def frr_show_routerid_vrf_cr():
    pass

