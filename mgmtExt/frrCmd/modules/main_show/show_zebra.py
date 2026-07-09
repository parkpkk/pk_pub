import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='client', invoke_without_command=True)
def frr_show_zebra_client(show_zebra_client_='show_zebra_client'):
    """Client information brief"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_client.name
    
    if 'VIEW_NODE|show_zebra_client' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_client'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra_client']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_client'][key] = val
    
    # set VIEW_NODE -> show_zebra_client table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra_client'
    pass


@frr_show_zebra_client.command('./	<cr>')
def frr_show_zebra_client_cr():
    pass


@frr_show_zebra_client.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_zebra_client_summary(summary_='summary'):
    """Brief Summary"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_client_summary.name
    data_gen['summary'] = summary_='summary'
    
    if 'VIEW_NODE|show_zebra_client' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_client'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra_client']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_client'][key] = val
    
    # set VIEW_NODE -> show_zebra_client table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra_client'
    pass


@frr_show_zebra_client_summary.command('./	<cr>')
def frr_show_zebra_client_summary_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='dplane', invoke_without_command=True)
def frr_show_zebra_dplane(show_zebra_dplane_='show_zebra_dplane'):
    """Zebra dataplane information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_dplane.name
    
    if 'VIEW_NODE|show_zebra_dplane' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane'][key] = val
    
    # set VIEW_NODE -> show_zebra_dplane table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra_dplane'
    pass


@frr_show_zebra_dplane.command('./	<cr>')
def frr_show_zebra_dplane_cr():
    pass


@frr_show_zebra_dplane.group(cls=FRR_AbbreviationGroup, name='detailed', invoke_without_command=True)
def frr_show_zebra_dplane_detailed(detailed_='detailed'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_dplane_detailed.name
    data_gen['detailed'] = detailed_='detailed'
    
    if 'VIEW_NODE|show_zebra_dplane' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane'][key] = val
    
    # set VIEW_NODE -> show_zebra_dplane table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra_dplane'
    pass


@frr_show_zebra_dplane_detailed.command('./	<cr>')
def frr_show_zebra_dplane_detailed_cr():
    pass


@frr_show_zebra_dplane.group(cls=FRR_AbbreviationGroup, name='providers', invoke_without_command=True)
def frr_show_zebra_dplane_providers(show_zebra_dplane_providers_='show_zebra_dplane_providers'):
    """Zebra dataplane provider information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_dplane_providers.name
    
    if 'VIEW_NODE|show_zebra_dplane_providers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane_providers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane_providers']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane_providers'][key] = val
    
    # set VIEW_NODE -> show_zebra_dplane_providers table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra_dplane_providers'
    pass


@frr_show_zebra_dplane_providers.command('./	<cr>')
def frr_show_zebra_dplane_providers_cr():
    pass


@frr_show_zebra_dplane_providers.group(cls=FRR_AbbreviationGroup, name='detailed', invoke_without_command=True)
def frr_show_zebra_dplane_providers_detailed(detailed_='detailed'):
    """Detailed output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_dplane_providers_detailed.name
    data_gen['detailed'] = detailed_='detailed'
    
    if 'VIEW_NODE|show_zebra_dplane_providers' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane_providers'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane_providers']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_dplane_providers'][key] = val
    
    # set VIEW_NODE -> show_zebra_dplane_providers table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra_dplane_providers'
    pass


@frr_show_zebra_dplane_providers_detailed.command('./	<cr>')
def frr_show_zebra_dplane_providers_detailed_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='fpm',)
def frr_show_zebra_fpm(show_zebra_fpm_='show_zebra_fpm'):
    """Forwarding Path Manager information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_fpm.name
    
    if 'VIEW_NODE|show_zebra_fpm' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_fpm'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra_fpm']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_fpm'][key] = val
    
    # set VIEW_NODE -> show_zebra_fpm table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra_fpm'
    pass


@frr_show_zebra_fpm.group(cls=FRR_AbbreviationGroup, name='stats', invoke_without_command=True)
def frr_show_zebra_fpm_stats(stats_='stats'):
    """Statistics"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_fpm_stats.name
    data_gen['stats'] = stats_='stats'
    
    if 'VIEW_NODE|show_zebra_fpm' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_fpm'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra_fpm']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_fpm'][key] = val
    
    # set VIEW_NODE -> show_zebra_fpm table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra_fpm'
    pass


@frr_show_zebra_fpm_stats.command('./	<cr>')
def frr_show_zebra_fpm_stats_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='mlag', invoke_without_command=True)
def frr_show_zebra_mlag(mlag_='mlag'):
    """The mlag role on this machine"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_mlag.name
    data_gen['mlag'] = mlag_='mlag'
    
    if 'VIEW_NODE|show_zebra' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra'][key] = val
    
    # set VIEW_NODE -> show_zebra table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra'
    pass


@frr_show_zebra_mlag.command('./	<cr>')
def frr_show_zebra_mlag_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='router',)
def frr_show_zebra_router():
    """The Zebra Router Information"""
    global COMMON_DATA_MAP
    
    pass


@frr_show_zebra_router.group(cls=FRR_AbbreviationGroup, name='table',)
def frr_show_zebra_router_table(show_zebra_router_table_='show_zebra_router_table'):
    """Table Information about this Zebra Router"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_router_table.name
    
    if 'VIEW_NODE|show_zebra_router_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_router_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra_router_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_router_table'][key] = val
    
    # set VIEW_NODE -> show_zebra_router_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra_router_table'
    pass


@frr_show_zebra_router_table.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_zebra_router_table_summary(summary_='summary'):
    """Summary Information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_zebra_router_table_summary.name
    data_gen['summary'] = summary_='summary'
    
    if 'VIEW_NODE|show_zebra_router_table' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_router_table'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_zebra_router_table']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_zebra_router_table'][key] = val
    
    # set VIEW_NODE -> show_zebra_router_table table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_zebra_router_table'
    pass


@frr_show_zebra_router_table_summary.command('./	<cr>')
def frr_show_zebra_router_table_summary_cr():
    pass

