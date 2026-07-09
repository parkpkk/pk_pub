import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='module', invoke_without_command=True)
def frr_show_yang_module(show_yang_module_='show_yang_module'):
    """Show loaded modules"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_module.name
    
    if 'VIEW_NODE|show_yang_module' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang_module']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'][key] = val
    
    # set VIEW_NODE -> show_yang_module table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang_module'
    pass


@frr_show_yang_module.command('./	<cr>')
def frr_show_yang_module_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='module-translator', invoke_without_command=True)
def frr_show_yang_moduletranslator(moduletranslator_='module-translator'):
    """Show loaded YANG module translators"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_moduletranslator.name
    data_gen['module-translator'] = moduletranslator_='module-translator'
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@frr_show_yang_moduletranslator.command('./	<cr>')
def frr_show_yang_moduletranslator_cr():
    pass


@frr_show_yang_module.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_yang_module_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_module_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang_module' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang_module']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'][key] = val
    
    # set VIEW_NODE -> show_yang_module table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang_module'
    pass


@frr_show_yang_module_daemonslist.command('./	<cr>')
def frr_show_yang_module_daemonslist_cr():
    pass


@frr_show_yang_module.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['WORD']),)
def frr_show_yang_module_modulename():
    """3"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_module_modulename.name
    data_gen['MODULE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang_module' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang_module']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'][key] = val
    
    # set VIEW_NODE -> show_yang_module table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang_module'
    pass


@frr_show_yang_module_modulename.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['compiled', 'summary', 'tree', 'yang', 'yin']), invoke_without_command=True)
def frr_show_yang_module_modulename_modulenamechoicecase():
    """Display compiled module in YANG format"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_module_modulename_modulenamechoicecase.name
    data_gen['MODULE-NAME_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang_module' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang_module']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'][key] = val
    
    # set VIEW_NODE -> show_yang_module table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang_module'
    pass


@frr_show_yang_module_modulename_modulenamechoicecase.command('./	<cr>')
def frr_show_yang_module_modulename_modulenamechoicecase_cr():
    pass


@frr_show_yang_module_modulename_modulenamechoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_yang_module_modulename_modulenamechoicecase_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_module_modulename_modulenamechoicecase_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang_module' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang_module']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'][key] = val
    
    # set VIEW_NODE -> show_yang_module table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang_module'
    pass


@frr_show_yang_module_modulename_modulenamechoicecase_daemonslist.command('./	<cr>')
def frr_show_yang_module_modulename_modulenamechoicecase_daemonslist_cr():
    pass


@frr_show_yang_module.group(cls=FRR_AbbreviationGroup, name='module-translator', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_yang_module_moduletranslator(yang_module_translator, moduletranslator_='module-translator'):
    """YANG module translator"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_module_moduletranslator.name
    data_gen['module-translator'] = moduletranslator_='module-translator'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_yang_module' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang_module']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'][key] = val
    
    # set VIEW_NODE -> show_yang_module table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang_module'
    pass


@frr_show_yang_module_moduletranslator.command('./	<cr>')
def frr_show_yang_module_moduletranslator_cr():
    pass


@frr_show_yang_module_moduletranslator.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_yang_module_moduletranslator_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_module_moduletranslator_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang_module' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang_module']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'][key] = val
    
    # set VIEW_NODE -> show_yang_module table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang_module'
    pass


@frr_show_yang_module_moduletranslator_daemonslist.command('./	<cr>')
def frr_show_yang_module_moduletranslator_daemonslist_cr():
    pass


@frr_show_yang_module_moduletranslator.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['WORD']),)
def frr_show_yang_module_moduletranslator_modulename():
    """5"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_module_moduletranslator_modulename.name
    data_gen['MODULE_NAME'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang_module' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang_module']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'][key] = val
    
    # set VIEW_NODE -> show_yang_module table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang_module'
    pass


@frr_show_yang_module_moduletranslator_modulename.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['compiled', 'summary', 'tree', 'yang', 'yin']), invoke_without_command=True)
def frr_show_yang_module_moduletranslator_modulename_modulenamechoicecase():
    """Display compiled module in YANG format"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_module_moduletranslator_modulename_modulenamechoicecase.name
    data_gen['MODULE-NAME_CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang_module' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang_module']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'][key] = val
    
    # set VIEW_NODE -> show_yang_module table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang_module'
    pass


@frr_show_yang_module_moduletranslator_modulename_modulenamechoicecase.command('./	<cr>')
def frr_show_yang_module_moduletranslator_modulename_modulenamechoicecase_cr():
    pass


@frr_show_yang_module_moduletranslator_modulename_modulenamechoicecase.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_yang_module_moduletranslator_modulename_modulenamechoicecase_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_module_moduletranslator_modulename_modulenamechoicecase_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang_module' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang_module']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang_module'][key] = val
    
    # set VIEW_NODE -> show_yang_module table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang_module'
    pass


@frr_show_yang_module_moduletranslator_modulename_modulenamechoicecase_daemonslist.command('./	<cr>')
def frr_show_yang_module_moduletranslator_modulename_modulenamechoicecase_daemonslist_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='operational-data', invoke_without_command=True)
@click.argument('xpath_expression_specifying_the', metavar='XPATH', required=True, type=FRR_TYPE('XPATH'))
def frr_show_yang_operationaldata(xpath_expression_specifying_the, operationaldata_='operational-data'):
    """Show YANG operational data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_operationaldata.name
    data_gen['operational-data'] = operationaldata_='operational-data'
    data_gen['XPATH_EXPRESSION_SPECIFYING_THE'] = xpath_expression_specifying_the
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@frr_show_yang_operationaldata.command('./	<cr>')
def frr_show_yang_operationaldata_cr():
    pass


@frr_show_yang_operationaldata.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_yang_operationaldata_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_operationaldata_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@frr_show_yang_operationaldata_daemonslist.command('./	<cr>')
def frr_show_yang_operationaldata_daemonslist_cr():
    pass


@frr_show_yang_operationaldata.group(cls=FRR_AbbreviationGroup, name='format',)
def frr_show_yang_operationaldata_format(format_='format'):
    """Set the output format"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_operationaldata_format.name
    data_gen['format'] = format_='format'
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@frr_show_yang_operationaldata_format.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['json', 'xml']), invoke_without_command=True)
def frr_show_yang_operationaldata_format_formatoutputformat():
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_operationaldata_format_formatoutputformat.name
    data_gen['FORMAT_OUTPUT_FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@frr_show_yang_operationaldata_format_formatoutputformat.command('./	<cr>')
def frr_show_yang_operationaldata_format_formatoutputformat_cr():
    pass


@frr_show_yang_operationaldata_format_formatoutputformat.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_yang_operationaldata_format_formatoutputformat_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_operationaldata_format_formatoutputformat_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@frr_show_yang_operationaldata_format_formatoutputformat_daemonslist.command('./	<cr>')
def frr_show_yang_operationaldata_format_formatoutputformat_daemonslist_cr():
    pass


@frr_show_yang_operationaldata.group(cls=FRR_AbbreviationGroup, name='translate', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_yang_operationaldata_translate(yang_module_translator, translate_='translate'):
    """Translate operational data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_operationaldata_translate.name
    data_gen['translate'] = translate_='translate'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@frr_show_yang_operationaldata_translate.command('./	<cr>')
def frr_show_yang_operationaldata_translate_cr():
    pass


@frr_show_yang_operationaldata_translate.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_yang_operationaldata_translate_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_operationaldata_translate_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@frr_show_yang_operationaldata_translate_daemonslist.command('./	<cr>')
def frr_show_yang_operationaldata_translate_daemonslist_cr():
    pass


@frr_show_yang_operationaldata.group(cls=FRR_AbbreviationGroup, name='with-config', invoke_without_command=True)
def frr_show_yang_operationaldata_withconfig(withconfig_='with-config'):
    """Merge configuration data"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_operationaldata_withconfig.name
    data_gen['with-config'] = withconfig_='with-config'
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@frr_show_yang_operationaldata_withconfig.command('./	<cr>')
def frr_show_yang_operationaldata_withconfig_cr():
    pass


@frr_show_yang_operationaldata_withconfig.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_yang_operationaldata_withconfig_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_yang_operationaldata_withconfig_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_yang' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_yang'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_yang']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_yang'][key] = val
    
    # set VIEW_NODE -> show_yang table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_yang'
    pass


@frr_show_yang_operationaldata_withconfig_daemonslist.command('./	<cr>')
def frr_show_yang_operationaldata_withconfig_daemonslist_cr():
    pass

