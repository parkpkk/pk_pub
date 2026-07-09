import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='nves', invoke_without_command=True)
def frr_show_vnc_nves(show_vnc_nves_='show_vnc_nves'):
    """List known NVEs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_nves.name
    
    if 'VIEW_NODE|show_vnc_nves' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_nves'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_nves']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_nves'][key] = val
    
    # set VIEW_NODE -> show_vnc_nves table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_nves'
    pass


@frr_show_vnc_nves.command('./	<cr>')
def frr_show_vnc_nves_cr():
    pass


@frr_show_vnc_nves.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['vn', 'un']),)
def frr_show_vnc_nves_overlayaddressmode():
    """3"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_nves_overlayaddressmode.name
    data_gen['OVERLAY_ADDRESS_MODE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vnc_nves' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_nves'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_nves']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_nves'][key] = val
    
    # set VIEW_NODE -> show_vnc_nves table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_nves'
    pass


@frr_show_vnc_nves_overlayaddressmode.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', 'X:X::X:X']), invoke_without_command=True)
def frr_show_vnc_nves_overlayaddressmode_overlayaddressmodeipaddress():
    """IPv4 interface address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_nves_overlayaddressmode_overlayaddressmodeipaddress.name
    data_gen['OVERLAY-ADDRESS-MODE_IP_ADDRESS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vnc_nves' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_nves'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_nves']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_nves'][key] = val
    
    # set VIEW_NODE -> show_vnc_nves table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_nves'
    pass


@frr_show_vnc_nves_overlayaddressmode_overlayaddressmodeipaddress.command('./	<cr>')
def frr_show_vnc_nves_overlayaddressmode_overlayaddressmodeipaddress_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='queries', invoke_without_command=True)
def frr_show_vnc_queries(show_vnc_queries_='show_vnc_queries'):
    """List active queries"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_queries.name
    
    if 'VIEW_NODE|show_vnc_queries' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_queries'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_queries']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_queries'][key] = val
    
    # set VIEW_NODE -> show_vnc_queries table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_queries'
    pass


@frr_show_vnc_queries.command('./	<cr>')
def frr_show_vnc_queries_cr():
    pass


@frr_show_vnc_queries.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D', 'A.B.C.D/M', 'X:X::X:X', 'X:X::X:X/M', 'X:X:X:X:X:X']), invoke_without_command=True)
def frr_show_vnc_queries_ipprefix():
    """Limit output to a particualr IPV4 address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_queries_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vnc_queries' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_queries'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_queries']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_queries'][key] = val
    
    # set VIEW_NODE -> show_vnc_queries table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_queries'
    pass


@frr_show_vnc_queries_ipprefix.command('./	<cr>')
def frr_show_vnc_queries_ipprefix_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='registrations', invoke_without_command=True)
def frr_show_vnc_registrations(show_vnc_registrations_='show_vnc_registrations'):
    """List active prefix registrations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_registrations.name
    
    if 'VIEW_NODE|show_vnc_registrations' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations'][key] = val
    
    # set VIEW_NODE -> show_vnc_registrations table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_registrations'
    pass


@frr_show_vnc_registrations.command('./	<cr>')
def frr_show_vnc_registrations_cr():
    pass


@frr_show_vnc_registrations.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D', 'A.B.C.D/M', 'X:X::X:X', 'X:X::X:X/M', 'X:X:X:X:X:X']), invoke_without_command=True)
def frr_show_vnc_registrations_ipprefix():
    """Limit output to a particualr IPV4 address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_registrations_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vnc_registrations' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations'][key] = val
    
    # set VIEW_NODE -> show_vnc_registrations table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_registrations'
    pass


@frr_show_vnc_registrations_ipprefix.command('./	<cr>')
def frr_show_vnc_registrations_ipprefix_cr():
    pass


@frr_show_vnc_registrations.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['all', 'holddown', 'imported', 'local', 'remote']), invoke_without_command=True)
def frr_show_vnc_registrations_registrationfilter():
    """show all registrations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_registrations_registrationfilter.name
    data_gen['REGISTRATION_FILTER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vnc_registrations' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations'][key] = val
    
    # set VIEW_NODE -> show_vnc_registrations table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_registrations'
    pass


@frr_show_vnc_registrations_registrationfilter.command('./	<cr>')
def frr_show_vnc_registrations_registrationfilter_cr():
    pass


@frr_show_vnc_registrations_registrationfilter.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', 'A.B.C.D/M', 'X:X::X:X', 'X:X::X:X/M', 'X:X:X:X:X:X']), invoke_without_command=True)
def frr_show_vnc_registrations_registrationfilter_ipprefix():
    """Limit output to a particualr IPV4 address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_registrations_registrationfilter_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vnc_registrations' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_registrations'][key] = val
    
    # set VIEW_NODE -> show_vnc_registrations table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_registrations'
    pass


@frr_show_vnc_registrations_registrationfilter_ipprefix.command('./	<cr>')
def frr_show_vnc_registrations_registrationfilter_ipprefix_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='responses', invoke_without_command=True)
def frr_show_vnc_responses(show_vnc_responses_='show_vnc_responses'):
    """List recent query responses"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_responses.name
    
    if 'VIEW_NODE|show_vnc_responses' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses'][key] = val
    
    # set VIEW_NODE -> show_vnc_responses table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_responses'
    pass


@frr_show_vnc_responses.command('./	<cr>')
def frr_show_vnc_responses_cr():
    pass


@frr_show_vnc_responses.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['A.B.C.D', 'A.B.C.D/M', 'X:X::X:X', 'X:X::X:X/M', 'X:X:X:X:X:X']), invoke_without_command=True)
def frr_show_vnc_responses_ipprefix():
    """Limit output to a particualr IPV4 address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_responses_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vnc_responses' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses'][key] = val
    
    # set VIEW_NODE -> show_vnc_responses table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_responses'
    pass


@frr_show_vnc_responses_ipprefix.command('./	<cr>')
def frr_show_vnc_responses_ipprefix_cr():
    pass


@frr_show_vnc_responses.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['active', 'removed']), invoke_without_command=True)
def frr_show_vnc_responses_querystatus():
    """show only active query responses"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_responses_querystatus.name
    data_gen['QUERY_STATUS'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vnc_responses' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses'][key] = val
    
    # set VIEW_NODE -> show_vnc_responses table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_responses'
    pass


@frr_show_vnc_responses_querystatus.command('./	<cr>')
def frr_show_vnc_responses_querystatus_cr():
    pass


@frr_show_vnc_responses_querystatus.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['A.B.C.D', 'A.B.C.D/M', 'X:X::X:X', 'X:X::X:X/M', 'X:X:X:X:X:X']), invoke_without_command=True)
def frr_show_vnc_responses_querystatus_ipprefix():
    """Limit output to a particualr IPV4 address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_responses_querystatus_ipprefix.name
    data_gen['IP_PREFIX'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_vnc_responses' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc_responses'][key] = val
    
    # set VIEW_NODE -> show_vnc_responses table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc_responses'
    pass


@frr_show_vnc_responses_querystatus_ipprefix.command('./	<cr>')
def frr_show_vnc_responses_querystatus_ipprefix_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='summary', invoke_without_command=True)
def frr_show_vnc_summary(summary_='summary'):
    """Display VNC status summary"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_vnc_summary.name
    data_gen['summary'] = summary_='summary'
    
    if 'VIEW_NODE|show_vnc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_vnc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_vnc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_vnc'][key] = val
    
    # set VIEW_NODE -> show_vnc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_vnc'
    pass


@frr_show_vnc_summary.command('./	<cr>')
def frr_show_vnc_summary_cr():
    pass

