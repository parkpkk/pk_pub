import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='atom', invoke_without_command=True)
def frr_show_l2vpn_atom():
    """Show Any Transport over MPLS information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom.name
    
    if 'VIEW_NODE|show_l2vpn_atom' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom'
    pass


@frr_show_l2vpn_atom.command('./	<cr>')
def frr_show_l2vpn_atom_cr():
    pass


@frr_show_l2vpn_atom.group(cls=FRR_AbbreviationGroup, name='binding', invoke_without_command=True)
def frr_show_l2vpn_atom_binding(show_l2vpn_atom_binding_='show_l2vpn_atom_binding'):
    """Show AToM label binding information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_binding.name
    
    if 'VIEW_NODE|show_l2vpn_atom_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_binding'
    pass


@frr_show_l2vpn_atom_binding.command('./	<cr>')
def frr_show_l2vpn_atom_binding_cr():
    pass


@frr_show_l2vpn_atom_binding.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D']), invoke_without_command=True)
def frr_show_l2vpn_atom_binding_destinationaddressofthe():
    """Destination address of the VC"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_binding_destinationaddressofthe.name
    data_gen['DESTINATION_ADDRESS_OF_THE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_l2vpn_atom_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_binding'
    pass


@frr_show_l2vpn_atom_binding_destinationaddressofthe.command('./	<cr>')
def frr_show_l2vpn_atom_binding_destinationaddressofthe_cr():
    pass


@frr_show_l2vpn_atom_binding_destinationaddressofthe.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_l2vpn_atom_binding_destinationaddressofthe_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_binding_destinationaddressofthe_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_l2vpn_atom_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_binding'
    pass


@frr_show_l2vpn_atom_binding_destinationaddressofthe_json.command('./	<cr>')
def frr_show_l2vpn_atom_binding_destinationaddressofthe_json_cr():
    pass


@frr_show_l2vpn_atom_binding.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_l2vpn_atom_binding_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_binding_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_l2vpn_atom_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_binding'
    pass


@frr_show_l2vpn_atom_binding_json.command('./	<cr>')
def frr_show_l2vpn_atom_binding_json_cr():
    pass


@frr_show_l2vpn_atom_binding.group(cls=FRR_AbbreviationGroup, name='local-label', invoke_without_command=True)
@click.argument('locally_assigned_label_value', metavar='(16-1048575)', required=True, type=FRR_TYPE((16, 1048575)))
def frr_show_l2vpn_atom_binding_locallabel(locally_assigned_label_value, locallabel_='local-label'):
    """Match locally assigned label values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_binding_locallabel.name
    data_gen['local-label'] = locallabel_='local-label'
    data_gen['LOCALLY_ASSIGNED_LABEL_VALUE'] = locally_assigned_label_value
    
    if 'VIEW_NODE|show_l2vpn_atom_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_binding'
    pass


@frr_show_l2vpn_atom_binding_locallabel.command('./	<cr>')
def frr_show_l2vpn_atom_binding_locallabel_cr():
    pass


@frr_show_l2vpn_atom_binding_locallabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_l2vpn_atom_binding_locallabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_binding_locallabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_l2vpn_atom_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_binding'
    pass


@frr_show_l2vpn_atom_binding_locallabel_json.command('./	<cr>')
def frr_show_l2vpn_atom_binding_locallabel_json_cr():
    pass


@frr_show_l2vpn_atom_binding.group(cls=FRR_AbbreviationGroup, name='remote-label', invoke_without_command=True)
@click.argument('remotely_assigned_label_value', metavar='(16-1048575)', required=True, type=FRR_TYPE((16, 1048575)))
def frr_show_l2vpn_atom_binding_remotelabel(remotely_assigned_label_value, remotelabel_='remote-label'):
    """Match remotely assigned label values"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_binding_remotelabel.name
    data_gen['remote-label'] = remotelabel_='remote-label'
    data_gen['REMOTELY_ASSIGNED_LABEL_VALUE'] = remotely_assigned_label_value
    
    if 'VIEW_NODE|show_l2vpn_atom_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_binding'
    pass


@frr_show_l2vpn_atom_binding_remotelabel.command('./	<cr>')
def frr_show_l2vpn_atom_binding_remotelabel_cr():
    pass


@frr_show_l2vpn_atom_binding_remotelabel.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_l2vpn_atom_binding_remotelabel_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_binding_remotelabel_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_l2vpn_atom_binding' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_binding'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_binding table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_binding'
    pass


@frr_show_l2vpn_atom_binding_remotelabel_json.command('./	<cr>')
def frr_show_l2vpn_atom_binding_remotelabel_json_cr():
    pass


@frr_show_l2vpn_atom.group(cls=FRR_AbbreviationGroup, name='vc', invoke_without_command=True)
def frr_show_l2vpn_atom_vc(show_l2vpn_atom_vc_='show_l2vpn_atom_vc'):
    """Show AToM virtual circuit information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_vc.name
    
    if 'VIEW_NODE|show_l2vpn_atom_vc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_vc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_vc'
    pass


@frr_show_l2vpn_atom_vc.command('./	<cr>')
def frr_show_l2vpn_atom_vc_cr():
    pass


@frr_show_l2vpn_atom_vc.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, ['A.B.C.D']), invoke_without_command=True)
def frr_show_l2vpn_atom_vc_destinationaddressofthe():
    """Destination address of the VC"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_vc_destinationaddressofthe.name
    data_gen['DESTINATION_ADDRESS_OF_THE'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_l2vpn_atom_vc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_vc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_vc'
    pass


@frr_show_l2vpn_atom_vc_destinationaddressofthe.command('./	<cr>')
def frr_show_l2vpn_atom_vc_destinationaddressofthe_cr():
    pass


@frr_show_l2vpn_atom_vc_destinationaddressofthe.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_l2vpn_atom_vc_destinationaddressofthe_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_vc_destinationaddressofthe_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_l2vpn_atom_vc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_vc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_vc'
    pass


@frr_show_l2vpn_atom_vc_destinationaddressofthe_json.command('./	<cr>')
def frr_show_l2vpn_atom_vc_destinationaddressofthe_json_cr():
    pass


@frr_show_l2vpn_atom_vc.group(cls=FRR_AbbreviationGroup, name='interface', invoke_without_command=True)
@click.argument('interface_name', metavar='IFNAME', required=True, type=FRR_TYPE('IFNAME'))
def frr_show_l2vpn_atom_vc_interface(interface_name, interface_='interface'):
    """Local interface of the pseudowire"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_vc_interface.name
    data_gen['interface'] = interface_='interface'
    data_gen['INTERFACE_NAME'] = interface_name
    
    if 'VIEW_NODE|show_l2vpn_atom_vc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_vc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_vc'
    pass


@frr_show_l2vpn_atom_vc_interface.command('./	<cr>')
def frr_show_l2vpn_atom_vc_interface_cr():
    pass


@frr_show_l2vpn_atom_vc_interface.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_l2vpn_atom_vc_interface_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_vc_interface_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_l2vpn_atom_vc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_vc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_vc'
    pass


@frr_show_l2vpn_atom_vc_interface_json.command('./	<cr>')
def frr_show_l2vpn_atom_vc_interface_json_cr():
    pass


@frr_show_l2vpn_atom_vc.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_l2vpn_atom_vc_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_vc_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_l2vpn_atom_vc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_vc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_vc'
    pass


@frr_show_l2vpn_atom_vc_json.command('./	<cr>')
def frr_show_l2vpn_atom_vc_json_cr():
    pass


@frr_show_l2vpn_atom_vc.group(cls=FRR_AbbreviationGroup, name='vc-id', invoke_without_command=True)
@click.argument('vc_id', metavar='(1-4294967295)', required=True, type=FRR_TYPE((1, 4294967295)))
def frr_show_l2vpn_atom_vc_vcid(vc_id, vcid_='vc-id'):
    """VC ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_vc_vcid.name
    data_gen['vc-id'] = vcid_='vc-id'
    data_gen['VC_ID'] = vc_id
    
    if 'VIEW_NODE|show_l2vpn_atom_vc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_vc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_vc'
    pass


@frr_show_l2vpn_atom_vc_vcid.command('./	<cr>')
def frr_show_l2vpn_atom_vc_vcid_cr():
    pass


@frr_show_l2vpn_atom_vc_vcid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_l2vpn_atom_vc_vcid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_l2vpn_atom_vc_vcid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_l2vpn_atom_vc' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_l2vpn_atom_vc'][key] = val
    
    # set VIEW_NODE -> show_l2vpn_atom_vc table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_l2vpn_atom_vc'
    pass


@frr_show_l2vpn_atom_vc_vcid_json.command('./	<cr>')
def frr_show_l2vpn_atom_vc_vcid_json_cr():
    pass

