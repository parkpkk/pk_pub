import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='pcep',)
def frr_show_srte_pcep(show_srte_pcep_='show_sr-te_pcep'):
    """PCEP info"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_pcep.name
    
    if 'VIEW_NODE|show_sr-te_pcep' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep'][key] = val
    
    # set VIEW_NODE -> show_sr-te_pcep table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_pcep'
    pass


@frr_show_srte_pcep.group(cls=FRR_AbbreviationGroup, name='counters', invoke_without_command=True)
def frr_show_srte_pcep_counters(counters_='counters'):
    """PCEP counters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_pcep_counters.name
    data_gen['counters'] = counters_='counters'
    
    if 'VIEW_NODE|show_sr-te_pcep' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep'][key] = val
    
    # set VIEW_NODE -> show_sr-te_pcep table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_pcep'
    pass


@frr_show_srte_pcep_counters.command('./	<cr>')
def frr_show_srte_pcep_counters_cr():
    pass


@frr_show_srte_pcep.group(cls=FRR_AbbreviationGroup, name='pcc', invoke_without_command=True)
def frr_show_srte_pcep_pcc(pcc_='pcc'):
    """Show current PCC configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_pcep_pcc.name
    data_gen['pcc'] = pcc_='pcc'
    
    if 'VIEW_NODE|show_sr-te_pcep' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep'][key] = val
    
    # set VIEW_NODE -> show_sr-te_pcep table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_pcep'
    pass


@frr_show_srte_pcep_pcc.command('./	<cr>')
def frr_show_srte_pcep_pcc_cr():
    pass


@frr_show_srte_pcep.group(cls=FRR_AbbreviationGroup, name='pce', invoke_without_command=True)
def frr_show_srte_pcep_pce(show_srte_pcep_pce_='show_sr-te_pcep_pce'):
    """Show detailed pce values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_pcep_pce.name
    
    if 'VIEW_NODE|show_sr-te_pcep_pce' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce'][key] = val
    
    # set VIEW_NODE -> show_sr-te_pcep_pce table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_pcep_pce'
    pass


@frr_show_srte_pcep_pce.command('./	<cr>')
def frr_show_srte_pcep_pce_cr():
    pass


@frr_show_srte_pcep.group(cls=FRR_AbbreviationGroup, name='pce-config', invoke_without_command=True)
def frr_show_srte_pcep_pceconfig(show_srte_pcep_pceconfig_='show_sr-te_pcep_pce-config'):
    """Show shared PCE configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_pcep_pceconfig.name
    
    if 'VIEW_NODE|show_sr-te_pcep_pce-config' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce-config'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce-config']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce-config'][key] = val
    
    # set VIEW_NODE -> show_sr-te_pcep_pce-config table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_pcep_pce-config'
    pass


@frr_show_srte_pcep_pceconfig.command('./	<cr>')
def frr_show_srte_pcep_pceconfig_cr():
    pass


@frr_show_srte_pcep_pceconfig.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD', 'default']), invoke_without_command=True)
def frr_show_srte_pcep_pceconfig_choicecase():
    """Show default hard-coded values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_pcep_pceconfig_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_sr-te_pcep_pce-config' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce-config'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce-config']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce-config'][key] = val
    
    # set VIEW_NODE -> show_sr-te_pcep_pce-config table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_pcep_pce-config'
    pass


@frr_show_srte_pcep_pceconfig_choicecase.command('./	<cr>')
def frr_show_srte_pcep_pceconfig_choicecase_cr():
    pass


@frr_show_srte_pcep_pce.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD']), invoke_without_command=True)
def frr_show_srte_pcep_pce_pcename():
    """pce name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_pcep_pce_pcename.name
    data_gen['PCE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_sr-te_pcep_pce' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_pce'][key] = val
    
    # set VIEW_NODE -> show_sr-te_pcep_pce table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_pcep_pce'
    pass


@frr_show_srte_pcep_pce_pcename.command('./	<cr>')
def frr_show_srte_pcep_pce_pcename_cr():
    pass


@frr_show_srte_pcep.group(cls=FRR_AbbreviationGroup, name='session', invoke_without_command=True)
def frr_show_srte_pcep_session(show_srte_pcep_session_='show_sr-te_pcep_session'):
    """Show PCEP Session information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_pcep_session.name
    
    if 'VIEW_NODE|show_sr-te_pcep_session' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_session'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_session']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_session'][key] = val
    
    # set VIEW_NODE -> show_sr-te_pcep_session table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_pcep_session'
    pass


@frr_show_srte_pcep_session.command('./	<cr>')
def frr_show_srte_pcep_session_cr():
    pass


@frr_show_srte_pcep_session.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['WORD']), invoke_without_command=True)
def frr_show_srte_pcep_session_pcename():
    """PCE name"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_pcep_session_pcename.name
    data_gen['PCE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_sr-te_pcep_session' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_session'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_session']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_pcep_session'][key] = val
    
    # set VIEW_NODE -> show_sr-te_pcep_session table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_pcep_session'
    pass


@frr_show_srte_pcep_session_pcename.command('./	<cr>')
def frr_show_srte_pcep_session_pcename_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='policy', invoke_without_command=True)
def frr_show_srte_policy(show_srte_policy_='show_sr-te_policy'):
    """SR-TE Policy"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_policy.name
    
    if 'VIEW_NODE|show_sr-te_policy' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_policy'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_policy']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_policy'][key] = val
    
    # set VIEW_NODE -> show_sr-te_policy table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_policy'
    pass


@frr_show_srte_policy.command('./	<cr>')
def frr_show_srte_policy_cr():
    pass


@frr_show_srte_policy.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_srte_policy_detail(detail_='detail'):
    """Show a detailed summary"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_srte_policy_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_sr-te_policy' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_policy'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_sr-te_policy']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_sr-te_policy'][key] = val
    
    # set VIEW_NODE -> show_sr-te_policy table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_sr-te_policy'
    pass


@frr_show_srte_policy_detail.command('./	<cr>')
def frr_show_srte_policy_detail_cr():
    pass

