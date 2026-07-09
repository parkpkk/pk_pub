import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='compare', invoke_without_command=True)
def frr_show_configuration_compare(show_configuration_compare_='show_configuration_compare'):
    """Compare two different configurations"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare.name
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare.command('./	<cr>')
def frr_show_configuration_compare_cr():
    pass


@frr_show_configuration_compare.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['json', 'xml']), invoke_without_command=True)
def frr_show_configuration_compare_outputformat():
    """Change output format to JSON"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_outputformat.name
    data_gen['OUTPUT_FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_outputformat.command('./	<cr>')
def frr_show_configuration_compare_outputformat_cr():
    pass


@frr_show_configuration_compare_outputformat.group(cls=FRR_AbbreviationGroup, name='translate', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_configuration_compare_outputformat_translate(yang_module_translator, translate_='translate'):
    """Translate output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_outputformat_translate.name
    data_gen['translate'] = translate_='translate'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_outputformat_translate.command('./	<cr>')
def frr_show_configuration_compare_outputformat_translate_cr():
    pass


@frr_show_configuration_compare.group(cls=FRR_AbbreviationGroup, name='running', invoke_without_command=True)
def frr_show_configuration_compare_running(show_configuration_compare_running_='show_configuration_compare_running'):
    """Running configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_running.name
    
    if 'VIEW_NODE|show_configuration_compare_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare_running'
    pass


@frr_show_configuration_compare_running.command('./	<cr>')
def frr_show_configuration_compare_running_cr():
    pass


@frr_show_configuration_compare_running.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['json', 'xml']), invoke_without_command=True)
def frr_show_configuration_compare_running_outputformat():
    """Change output format to JSON"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_running_outputformat.name
    data_gen['OUTPUT_FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_compare_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare_running'
    pass


@frr_show_configuration_compare_running_outputformat.command('./	<cr>')
def frr_show_configuration_compare_running_outputformat_cr():
    pass


@frr_show_configuration_compare_running_outputformat.group(cls=FRR_AbbreviationGroup, name='translate', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_configuration_compare_running_outputformat_translate(yang_module_translator, translate_='translate'):
    """Translate output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_running_outputformat_translate.name
    data_gen['translate'] = translate_='translate'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_configuration_compare_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare_running'
    pass


@frr_show_configuration_compare_running_outputformat_translate.command('./	<cr>')
def frr_show_configuration_compare_running_outputformat_translate_cr():
    pass


@frr_show_configuration_compare_running.group(cls=FRR_AbbreviationGroup, name='running', invoke_without_command=True)
def frr_show_configuration_compare_running_running(show_configuration_compare_running_running_='show_configuration_compare_running_running'):
    """Running configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_running_running.name
    
    if 'VIEW_NODE|show_configuration_compare_running_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare_running_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare_running_running'
    pass


@frr_show_configuration_compare_running_running.command('./	<cr>')
def frr_show_configuration_compare_running_running_cr():
    pass


@frr_show_configuration_compare_running_running.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['json', 'xml']), invoke_without_command=True)
def frr_show_configuration_compare_running_running_outputformat():
    """Change output format to JSON"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_running_running_outputformat.name
    data_gen['OUTPUT_FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_compare_running_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare_running_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare_running_running'
    pass


@frr_show_configuration_compare_running_running_outputformat.command('./	<cr>')
def frr_show_configuration_compare_running_running_outputformat_cr():
    pass


@frr_show_configuration_compare_running_running_outputformat.group(cls=FRR_AbbreviationGroup, name='translate', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_configuration_compare_running_running_outputformat_translate(yang_module_translator, translate_='translate'):
    """Translate output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_running_running_outputformat_translate.name
    data_gen['translate'] = translate_='translate'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_configuration_compare_running_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare_running_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare_running_running'
    pass


@frr_show_configuration_compare_running_running_outputformat_translate.command('./	<cr>')
def frr_show_configuration_compare_running_running_outputformat_translate_cr():
    pass


@frr_show_configuration_compare_running.group(cls=FRR_AbbreviationGroup, name='transaction', invoke_without_command=True)
@click.argument('transaction_id', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_configuration_compare_running_transaction(transaction_id, transaction_='transaction'):
    """Configuration transaction"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_running_transaction.name
    data_gen['transaction'] = transaction_='transaction'
    data_gen['TRANSACTION_ID'] = transaction_id
    
    if 'VIEW_NODE|show_configuration_compare_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare_running'
    pass


@frr_show_configuration_compare_running_transaction.command('./	<cr>')
def frr_show_configuration_compare_running_transaction_cr():
    pass


@frr_show_configuration_compare_running_transaction.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['json', 'xml']), invoke_without_command=True)
def frr_show_configuration_compare_running_transaction_outputformat():
    """Change output format to JSON"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_running_transaction_outputformat.name
    data_gen['OUTPUT_FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_compare_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare_running'
    pass


@frr_show_configuration_compare_running_transaction_outputformat.command('./	<cr>')
def frr_show_configuration_compare_running_transaction_outputformat_cr():
    pass


@frr_show_configuration_compare_running_transaction_outputformat.group(cls=FRR_AbbreviationGroup, name='translate', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_configuration_compare_running_transaction_outputformat_translate(yang_module_translator, translate_='translate'):
    """Translate output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_running_transaction_outputformat_translate.name
    data_gen['translate'] = translate_='translate'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_configuration_compare_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare_running'
    pass


@frr_show_configuration_compare_running_transaction_outputformat_translate.command('./	<cr>')
def frr_show_configuration_compare_running_transaction_outputformat_translate_cr():
    pass


@frr_show_configuration_compare.group(cls=FRR_AbbreviationGroup, name='transaction', invoke_without_command=True)
@click.argument('transaction_id', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_configuration_compare_transaction(transaction_id, transaction_='transaction'):
    """Configuration transaction"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_transaction.name
    data_gen['transaction'] = transaction_='transaction'
    data_gen['TRANSACTION_ID'] = transaction_id
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_transaction.command('./	<cr>')
def frr_show_configuration_compare_transaction_cr():
    pass


@frr_show_configuration_compare_transaction.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['json', 'xml']), invoke_without_command=True)
def frr_show_configuration_compare_transaction_outputformat():
    """Change output format to JSON"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_transaction_outputformat.name
    data_gen['OUTPUT_FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_transaction_outputformat.command('./	<cr>')
def frr_show_configuration_compare_transaction_outputformat_cr():
    pass


@frr_show_configuration_compare_transaction_outputformat.group(cls=FRR_AbbreviationGroup, name='translate', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_configuration_compare_transaction_outputformat_translate(yang_module_translator, translate_='translate'):
    """Translate output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_transaction_outputformat_translate.name
    data_gen['translate'] = translate_='translate'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_transaction_outputformat_translate.command('./	<cr>')
def frr_show_configuration_compare_transaction_outputformat_translate_cr():
    pass


@frr_show_configuration_compare_transaction.group(cls=FRR_AbbreviationGroup, name='running', invoke_without_command=True)
def frr_show_configuration_compare_transaction_running(running_='running'):
    """Running configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_transaction_running.name
    data_gen['running'] = running_='running'
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_transaction_running.command('./	<cr>')
def frr_show_configuration_compare_transaction_running_cr():
    pass


@frr_show_configuration_compare_transaction_running.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['json', 'xml']), invoke_without_command=True)
def frr_show_configuration_compare_transaction_running_outputformat():
    """Change output format to JSON"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_transaction_running_outputformat.name
    data_gen['OUTPUT_FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_transaction_running_outputformat.command('./	<cr>')
def frr_show_configuration_compare_transaction_running_outputformat_cr():
    pass


@frr_show_configuration_compare_transaction_running_outputformat.group(cls=FRR_AbbreviationGroup, name='translate', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_configuration_compare_transaction_running_outputformat_translate(yang_module_translator, translate_='translate'):
    """Translate output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_transaction_running_outputformat_translate.name
    data_gen['translate'] = translate_='translate'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_transaction_running_outputformat_translate.command('./	<cr>')
def frr_show_configuration_compare_transaction_running_outputformat_translate_cr():
    pass


@frr_show_configuration_compare_transaction.group(cls=FRR_AbbreviationGroup, name='transaction', invoke_without_command=True)
@click.argument('transaction_id', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_configuration_compare_transaction_transaction(transaction_id, transaction_='transaction'):
    """Configuration transaction"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_transaction_transaction.name
    data_gen['transaction'] = transaction_='transaction'
    data_gen['TRANSACTION_ID'] = transaction_id
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_transaction_transaction.command('./	<cr>')
def frr_show_configuration_compare_transaction_transaction_cr():
    pass


@frr_show_configuration_compare_transaction_transaction.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['json', 'xml']), invoke_without_command=True)
def frr_show_configuration_compare_transaction_transaction_outputformat():
    """Change output format to JSON"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_transaction_transaction_outputformat.name
    data_gen['OUTPUT_FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_transaction_transaction_outputformat.command('./	<cr>')
def frr_show_configuration_compare_transaction_transaction_outputformat_cr():
    pass


@frr_show_configuration_compare_transaction_transaction_outputformat.group(cls=FRR_AbbreviationGroup, name='translate', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_configuration_compare_transaction_transaction_outputformat_translate(yang_module_translator, translate_='translate'):
    """Translate output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_compare_transaction_transaction_outputformat_translate.name
    data_gen['translate'] = translate_='translate'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_configuration_compare' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_compare'][key] = val
    
    # set VIEW_NODE -> show_configuration_compare table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_compare'
    pass


@frr_show_configuration_compare_transaction_transaction_outputformat_translate.command('./	<cr>')
def frr_show_configuration_compare_transaction_transaction_outputformat_translate_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='running', invoke_without_command=True)
def frr_show_configuration_running(show_configuration_running_='show_configuration_running'):
    """Running configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running.name
    
    if 'VIEW_NODE|show_configuration_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running'
    pass


@frr_show_configuration_running.command('./	<cr>')
def frr_show_configuration_running_cr():
    pass


@frr_show_configuration_running.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_configuration_running_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running'
    pass


@frr_show_configuration_running_daemonslist.command('./	<cr>')
def frr_show_configuration_running_daemonslist_cr():
    pass


@frr_show_configuration_running.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['json', 'xml']), invoke_without_command=True)
def frr_show_configuration_running_outputformat():
    """Change output format to JSON"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_outputformat.name
    data_gen['OUTPUT_FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running'
    pass


@frr_show_configuration_running_outputformat.command('./	<cr>')
def frr_show_configuration_running_outputformat_cr():
    pass


@frr_show_configuration_running_outputformat.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_configuration_running_outputformat_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_outputformat_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running'
    pass


@frr_show_configuration_running_outputformat_daemonslist.command('./	<cr>')
def frr_show_configuration_running_outputformat_daemonslist_cr():
    pass


@frr_show_configuration_running_outputformat.group(cls=FRR_AbbreviationGroup, name='translate', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_configuration_running_outputformat_translate(yang_module_translator, translate_='translate'):
    """Translate output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_outputformat_translate.name
    data_gen['translate'] = translate_='translate'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_configuration_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running'
    pass


@frr_show_configuration_running_outputformat_translate.command('./	<cr>')
def frr_show_configuration_running_outputformat_translate_cr():
    pass


@frr_show_configuration_running_outputformat_translate.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_configuration_running_outputformat_translate_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_outputformat_translate_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running'
    pass


@frr_show_configuration_running_outputformat_translate_daemonslist.command('./	<cr>')
def frr_show_configuration_running_outputformat_translate_daemonslist_cr():
    pass


@frr_show_configuration_running_outputformat_translate.group(cls=FRR_AbbreviationGroup, name='with-defaults', invoke_without_command=True)
def frr_show_configuration_running_outputformat_translate_withdefaults(withdefaults_='with-defaults'):
    """Show default values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_outputformat_translate_withdefaults.name
    data_gen['with-defaults'] = withdefaults_='with-defaults'
    
    if 'VIEW_NODE|show_configuration_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running'
    pass


@frr_show_configuration_running_outputformat_translate_withdefaults.command('./	<cr>')
def frr_show_configuration_running_outputformat_translate_withdefaults_cr():
    pass


@frr_show_configuration_running_outputformat_translate_withdefaults.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_configuration_running_outputformat_translate_withdefaults_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_outputformat_translate_withdefaults_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running'
    pass


@frr_show_configuration_running_outputformat_translate_withdefaults_daemonslist.command('./	<cr>')
def frr_show_configuration_running_outputformat_translate_withdefaults_daemonslist_cr():
    pass


@frr_show_configuration_running_outputformat.group(cls=FRR_AbbreviationGroup, name='with-defaults', invoke_without_command=True)
def frr_show_configuration_running_outputformat_withdefaults(withdefaults_='with-defaults'):
    """Show default values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_outputformat_withdefaults.name
    data_gen['with-defaults'] = withdefaults_='with-defaults'
    
    if 'VIEW_NODE|show_configuration_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running'
    pass


@frr_show_configuration_running_outputformat_withdefaults.command('./	<cr>')
def frr_show_configuration_running_outputformat_withdefaults_cr():
    pass


@frr_show_configuration_running_outputformat_withdefaults.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_configuration_running_outputformat_withdefaults_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_outputformat_withdefaults_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_running' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running'][key] = val
    
    # set VIEW_NODE -> show_configuration_running table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running'
    pass


@frr_show_configuration_running_outputformat_withdefaults_daemonslist.command('./	<cr>')
def frr_show_configuration_running_outputformat_withdefaults_daemonslist_cr():
    pass


@frr_show_configuration_running.group(cls=FRR_AbbreviationGroup, name='with-defaults', invoke_without_command=True)
def frr_show_configuration_running_withdefaults(show_configuration_running_withdefaults_='show_configuration_running_with-defaults'):
    """Show default values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_withdefaults.name
    
    if 'VIEW_NODE|show_configuration_running_with-defaults' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running_with-defaults'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running_with-defaults']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running_with-defaults'][key] = val
    
    # set VIEW_NODE -> show_configuration_running_with-defaults table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running_with-defaults'
    pass


@frr_show_configuration_running_withdefaults.command('./	<cr>')
def frr_show_configuration_running_withdefaults_cr():
    pass


@frr_show_configuration_running_withdefaults.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['zebra', 'bgpd', 'ripd', 'ripngd', 'ospfd', 'ospf6d', 'isisd', 'fabricd', 'nhrpd', 'ldpd', 'babeld', 'eigrpd', 'pimd', 'pim6d', 'pbrd', 'staticd', 'bfdd', 'vrrpd', 'pathd']), invoke_without_command=True)
def frr_show_configuration_running_withdefaults_daemonslist():
    """For the zebra daemon"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_running_withdefaults_daemonslist.name
    data_gen['DAEMONS_LIST'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_running_with-defaults' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running_with-defaults'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_running_with-defaults']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_running_with-defaults'][key] = val
    
    # set VIEW_NODE -> show_configuration_running_with-defaults table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_running_with-defaults'
    pass


@frr_show_configuration_running_withdefaults_daemonslist.command('./	<cr>')
def frr_show_configuration_running_withdefaults_daemonslist_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='transaction', invoke_without_command=True)
def frr_show_configuration_transaction(show_configuration_transaction_='show_configuration_transaction'):
    """Configuration transaction"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_transaction.name
    
    if 'VIEW_NODE|show_configuration_transaction' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'][key] = val
    
    # set VIEW_NODE -> show_configuration_transaction table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_transaction'
    pass


@frr_show_configuration_transaction.command('./	<cr>')
def frr_show_configuration_transaction_cr():
    pass


@frr_show_configuration_transaction.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, [(1, 4294967295)]), invoke_without_command=True)
def frr_show_configuration_transaction_transactionid():
    """Transaction ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_transaction_transactionid.name
    data_gen['TRANSACTION_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_transaction' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'][key] = val
    
    # set VIEW_NODE -> show_configuration_transaction table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_transaction'
    pass


@frr_show_configuration_transaction_transactionid.command('./	<cr>')
def frr_show_configuration_transaction_transactionid_cr():
    pass


@frr_show_configuration_transaction_transactionid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['with-defaults', 'changes']), invoke_without_command=True)
def frr_show_configuration_transaction_transactionid_choicecase():
    """Show default values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_transaction_transactionid_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_transaction' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'][key] = val
    
    # set VIEW_NODE -> show_configuration_transaction table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_transaction'
    pass


@frr_show_configuration_transaction_transactionid_choicecase.command('./	<cr>')
def frr_show_configuration_transaction_transactionid_choicecase_cr():
    pass


@frr_show_configuration_transaction_transactionid.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(6, ['json', 'xml']), invoke_without_command=True)
def frr_show_configuration_transaction_transactionid_outputformat():
    """Change output format to JSON"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_transaction_transactionid_outputformat.name
    data_gen['OUTPUT_FORMAT'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_transaction' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'][key] = val
    
    # set VIEW_NODE -> show_configuration_transaction table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_transaction'
    pass


@frr_show_configuration_transaction_transactionid_outputformat.command('./	<cr>')
def frr_show_configuration_transaction_transactionid_outputformat_cr():
    pass


@frr_show_configuration_transaction_transactionid_outputformat.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(7, ['with-defaults', 'changes']), invoke_without_command=True)
def frr_show_configuration_transaction_transactionid_outputformat_choicecase():
    """Show default values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_transaction_transactionid_outputformat_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_transaction' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'][key] = val
    
    # set VIEW_NODE -> show_configuration_transaction table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_transaction'
    pass


@frr_show_configuration_transaction_transactionid_outputformat_choicecase.command('./	<cr>')
def frr_show_configuration_transaction_transactionid_outputformat_choicecase_cr():
    pass


@frr_show_configuration_transaction_transactionid_outputformat.group(cls=FRR_AbbreviationGroup, name='translate', invoke_without_command=True)
@click.argument('yang_module_translator', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_configuration_transaction_transactionid_outputformat_translate(yang_module_translator, translate_='translate'):
    """Translate output"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_transaction_transactionid_outputformat_translate.name
    data_gen['translate'] = translate_='translate'
    data_gen['YANG_MODULE_TRANSLATOR'] = yang_module_translator
    
    if 'VIEW_NODE|show_configuration_transaction' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'][key] = val
    
    # set VIEW_NODE -> show_configuration_transaction table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_transaction'
    pass


@frr_show_configuration_transaction_transactionid_outputformat_translate.command('./	<cr>')
def frr_show_configuration_transaction_transactionid_outputformat_translate_cr():
    pass


@frr_show_configuration_transaction_transactionid_outputformat_translate.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(8, ['with-defaults', 'changes']), invoke_without_command=True)
def frr_show_configuration_transaction_transactionid_outputformat_translate_choicecase():
    """Show default values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_configuration_transaction_transactionid_outputformat_translate_choicecase.name
    data_gen['CHOICE_CASE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_configuration_transaction' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_configuration_transaction'][key] = val
    
    # set VIEW_NODE -> show_configuration_transaction table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_configuration_transaction'
    pass


@frr_show_configuration_transaction_transactionid_outputformat_translate_choicecase.command('./	<cr>')
def frr_show_configuration_transaction_transactionid_outputformat_translate_choicecase_cr():
    pass

