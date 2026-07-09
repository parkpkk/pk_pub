import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *


@click.group(cls=FRR_AbbreviationGroup, name='access-vlan', invoke_without_command=True)
def frr_show_evpn_accessvlan(show_evpn_accessvlan_='show_evpn_access-vlan'):
    """Access VLANs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_accessvlan.name
    
    if 'VIEW_NODE|show_evpn_access-vlan' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan'][key] = val
    
    # set VIEW_NODE -> show_evpn_access-vlan table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_access-vlan'
    pass


@frr_show_evpn_accessvlan.command('./	<cr>')
def frr_show_evpn_accessvlan_cr():
    pass


@frr_show_evpn_accessvlan.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_evpn_accessvlan_detail(show_evpn_accessvlan_detail_='show_evpn_access-vlan_detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_accessvlan_detail.name
    
    if 'VIEW_NODE|show_evpn_access-vlan_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_access-vlan_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_access-vlan_detail'
    pass


@frr_show_evpn_accessvlan_detail.command('./	<cr>')
def frr_show_evpn_accessvlan_detail_cr():
    pass


@frr_show_evpn_accessvlan_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_accessvlan_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_accessvlan_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_access-vlan_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_access-vlan_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_access-vlan_detail'
    pass


@frr_show_evpn_accessvlan_detail_json.command('./	<cr>')
def frr_show_evpn_accessvlan_detail_json_cr():
    pass


@frr_show_evpn_accessvlan.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_accessvlan_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_accessvlan_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_access-vlan' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan'][key] = val
    
    # set VIEW_NODE -> show_evpn_access-vlan table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_access-vlan'
    pass


@frr_show_evpn_accessvlan_json.command('./	<cr>')
def frr_show_evpn_accessvlan_json_cr():
    pass


@frr_show_evpn_accessvlan.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, [(1, 4094)]), invoke_without_command=True)
def frr_show_evpn_accessvlan_vlanid():
    """VLAN ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_accessvlan_vlanid.name
    data_gen['VLAN_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_evpn_access-vlan' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan'][key] = val
    
    # set VIEW_NODE -> show_evpn_access-vlan table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_access-vlan'
    pass


@frr_show_evpn_accessvlan_vlanid.command('./	<cr>')
def frr_show_evpn_accessvlan_vlanid_cr():
    pass


@frr_show_evpn_accessvlan_vlanid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_accessvlan_vlanid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_accessvlan_vlanid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_access-vlan' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_access-vlan'][key] = val
    
    # set VIEW_NODE -> show_evpn_access-vlan table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_access-vlan'
    pass


@frr_show_evpn_accessvlan_vlanid_json.command('./	<cr>')
def frr_show_evpn_accessvlan_vlanid_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='arp-cache',)
def frr_show_evpn_arpcache():
    """ARP and ND cache"""
    global COMMON_DATA_MAP
    
    pass


@frr_show_evpn_arpcache.group(cls=FRR_AbbreviationGroup, name='vni',)
def frr_show_evpn_arpcache_vni(show_evpn_arpcache_vni_='show_evpn_arp-cache_vni'):
    """VxLAN Network Identifier"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni.name
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni'
    pass


@frr_show_evpn_arpcache_vni.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_all(show_evpn_arpcache_vni_all_='show_evpn_arp-cache_vni_all'):
    """All VNIs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_all.name
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni_all'
    pass


@frr_show_evpn_arpcache_vni_all.command('./	<cr>')
def frr_show_evpn_arpcache_vni_all_cr():
    pass


@frr_show_evpn_arpcache_vni_all.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_all_detail(show_evpn_arpcache_vni_all_detail_='show_evpn_arp-cache_vni_all_detail'):
    """Neighbor details for all vnis in detail"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_all_detail.name
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni_all_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni_all_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni_all_detail'
    pass


@frr_show_evpn_arpcache_vni_all_detail.command('./	<cr>')
def frr_show_evpn_arpcache_vni_all_detail_cr():
    pass


@frr_show_evpn_arpcache_vni_all_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_all_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_all_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni_all_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni_all_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni_all_detail'
    pass


@frr_show_evpn_arpcache_vni_all_detail_json.command('./	<cr>')
def frr_show_evpn_arpcache_vni_all_detail_json_cr():
    pass


@frr_show_evpn_arpcache_vni_all.group(cls=FRR_AbbreviationGroup, name='duplicate', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_all_duplicate(show_evpn_arpcache_vni_all_duplicate_='show_evpn_arp-cache_vni_all_duplicate'):
    """Duplicate address list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_all_duplicate.name
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni_all_duplicate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_duplicate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_duplicate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_duplicate'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni_all_duplicate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni_all_duplicate'
    pass


@frr_show_evpn_arpcache_vni_all_duplicate.command('./	<cr>')
def frr_show_evpn_arpcache_vni_all_duplicate_cr():
    pass


@frr_show_evpn_arpcache_vni_all_duplicate.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_all_duplicate_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_all_duplicate_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni_all_duplicate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_duplicate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_duplicate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all_duplicate'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni_all_duplicate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni_all_duplicate'
    pass


@frr_show_evpn_arpcache_vni_all_duplicate_json.command('./	<cr>')
def frr_show_evpn_arpcache_vni_all_duplicate_json_cr():
    pass


@frr_show_evpn_arpcache_vni_all.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_all_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_all_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni_all'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni_all'
    pass


@frr_show_evpn_arpcache_vni_all_json.command('./	<cr>')
def frr_show_evpn_arpcache_vni_all_json_cr():
    pass


@frr_show_evpn_arpcache_vni.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, [(1, 16777215)]), invoke_without_command=True)
def frr_show_evpn_arpcache_vni_vninumber():
    """VNI number"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_vninumber.name
    data_gen['VNI_NUMBER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni'
    pass


@frr_show_evpn_arpcache_vni_vninumber.command('./	<cr>')
def frr_show_evpn_arpcache_vni_vninumber_cr():
    pass


@frr_show_evpn_arpcache_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='duplicate', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_vninumber_duplicate(duplicate_='duplicate'):
    """Duplicate address list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_vninumber_duplicate.name
    data_gen['duplicate'] = duplicate_='duplicate'
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni'
    pass


@frr_show_evpn_arpcache_vni_vninumber_duplicate.command('./	<cr>')
def frr_show_evpn_arpcache_vni_vninumber_duplicate_cr():
    pass


@frr_show_evpn_arpcache_vni_vninumber_duplicate.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_vninumber_duplicate_json(duplicate_json_='duplicate_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_vninumber_duplicate_json.name
    data_gen['duplicate_json'] = duplicate_json_='duplicate_json'
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni'
    pass


@frr_show_evpn_arpcache_vni_vninumber_duplicate_json.command('./	<cr>')
def frr_show_evpn_arpcache_vni_vninumber_duplicate_json_cr():
    pass


@frr_show_evpn_arpcache_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='ip', invoke_without_command=True)
@click.argument('neighbor_address', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_evpn_arpcache_vni_vninumber_ip(neighbor_address, ip_='ip'):
    """Neighbor"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_vninumber_ip.name
    data_gen['ip'] = ip_='ip'
    data_gen['NEIGHBOR_ADDRESS'] = neighbor_address
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni'
    pass


@frr_show_evpn_arpcache_vni_vninumber_ip.command('./	<cr>')
def frr_show_evpn_arpcache_vni_vninumber_ip_cr():
    pass


@frr_show_evpn_arpcache_vni_vninumber_ip.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_vninumber_ip_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_vninumber_ip_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni'
    pass


@frr_show_evpn_arpcache_vni_vninumber_ip_json.command('./	<cr>')
def frr_show_evpn_arpcache_vni_vninumber_ip_json_cr():
    pass


@frr_show_evpn_arpcache_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_vninumber_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_vninumber_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni'
    pass


@frr_show_evpn_arpcache_vni_vninumber_json.command('./	<cr>')
def frr_show_evpn_arpcache_vni_vninumber_json_cr():
    pass


@frr_show_evpn_arpcache_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='vtep', invoke_without_command=True)
@click.argument('remote_vtep_ip_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_evpn_arpcache_vni_vninumber_vtep(remote_vtep_ip_address, vtep_='vtep'):
    """Remote VTEP"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_vninumber_vtep.name
    data_gen['vtep'] = vtep_='vtep'
    data_gen['REMOTE_VTEP_IP_ADDRESS'] = remote_vtep_ip_address
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni'
    pass


@frr_show_evpn_arpcache_vni_vninumber_vtep.command('./	<cr>')
def frr_show_evpn_arpcache_vni_vninumber_vtep_cr():
    pass


@frr_show_evpn_arpcache_vni_vninumber_vtep.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_arpcache_vni_vninumber_vtep_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_arpcache_vni_vninumber_vtep_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_arp-cache_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_arp-cache_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_arp-cache_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_arp-cache_vni'
    pass


@frr_show_evpn_arpcache_vni_vninumber_vtep_json.command('./	<cr>')
def frr_show_evpn_arpcache_vni_vninumber_vtep_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='es', invoke_without_command=True)
def frr_show_evpn_es(show_evpn_es_='show_evpn_es'):
    """Ethernet Segment"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_es.name
    
    if 'VIEW_NODE|show_evpn_es' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es'][key] = val
    
    # set VIEW_NODE -> show_evpn_es table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es'
    pass


@frr_show_evpn_es.command('./	<cr>')
def frr_show_evpn_es_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='es-evi', invoke_without_command=True)
def frr_show_evpn_esevi(show_evpn_esevi_='show_evpn_es-evi'):
    """Ethernet Segment per EVI"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_esevi.name
    
    if 'VIEW_NODE|show_evpn_es-evi' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'][key] = val
    
    # set VIEW_NODE -> show_evpn_es-evi table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es-evi'
    pass


@frr_show_evpn_esevi.command('./	<cr>')
def frr_show_evpn_esevi_cr():
    pass


@frr_show_evpn_esevi.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_evpn_esevi_detail(show_evpn_esevi_detail_='show_evpn_es-evi_detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_esevi_detail.name
    
    if 'VIEW_NODE|show_evpn_es-evi_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_es-evi_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es-evi_detail'
    pass


@frr_show_evpn_esevi_detail.command('./	<cr>')
def frr_show_evpn_esevi_detail_cr():
    pass


@frr_show_evpn_esevi_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_esevi_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_esevi_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_es-evi_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_es-evi_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es-evi_detail'
    pass


@frr_show_evpn_esevi_detail_json.command('./	<cr>')
def frr_show_evpn_esevi_detail_json_cr():
    pass


@frr_show_evpn_esevi.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_esevi_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_esevi_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_es-evi' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'][key] = val
    
    # set VIEW_NODE -> show_evpn_es-evi table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es-evi'
    pass


@frr_show_evpn_esevi_json.command('./	<cr>')
def frr_show_evpn_esevi_json_cr():
    pass


@frr_show_evpn_esevi.group(cls=FRR_AbbreviationGroup, name='vni', invoke_without_command=True)
@click.argument('vni', metavar='(1-16777215)', required=True, type=FRR_TYPE((1, 16777215)))
def frr_show_evpn_esevi_vni(vni, vni_='vni'):
    """VxLAN Network Identifier"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_esevi_vni.name
    data_gen['vni'] = vni_='vni'
    data_gen['VNI'] = vni
    
    if 'VIEW_NODE|show_evpn_es-evi' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'][key] = val
    
    # set VIEW_NODE -> show_evpn_es-evi table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es-evi'
    pass


@frr_show_evpn_esevi_vni.command('./	<cr>')
def frr_show_evpn_esevi_vni_cr():
    pass


@frr_show_evpn_esevi_vni.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_evpn_esevi_vni_detail(detail_='detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_esevi_vni_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_evpn_es-evi' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'][key] = val
    
    # set VIEW_NODE -> show_evpn_es-evi table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es-evi'
    pass


@frr_show_evpn_esevi_vni_detail.command('./	<cr>')
def frr_show_evpn_esevi_vni_detail_cr():
    pass


@frr_show_evpn_esevi_vni_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_esevi_vni_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_esevi_vni_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_evpn_es-evi' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'][key] = val
    
    # set VIEW_NODE -> show_evpn_es-evi table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es-evi'
    pass


@frr_show_evpn_esevi_vni_detail_json.command('./	<cr>')
def frr_show_evpn_esevi_vni_detail_json_cr():
    pass


@frr_show_evpn_esevi_vni.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_esevi_vni_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_esevi_vni_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_es-evi' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es-evi'][key] = val
    
    # set VIEW_NODE -> show_evpn_es-evi table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es-evi'
    pass


@frr_show_evpn_esevi_vni_json.command('./	<cr>')
def frr_show_evpn_esevi_vni_json_cr():
    pass


@frr_show_evpn_es.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_evpn_es_detail(show_evpn_es_detail_='show_evpn_es_detail'):
    """Detailed information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_es_detail.name
    
    if 'VIEW_NODE|show_evpn_es_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_es_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es_detail'
    pass


@frr_show_evpn_es_detail.command('./	<cr>')
def frr_show_evpn_es_detail_cr():
    pass


@frr_show_evpn_es_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_es_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_es_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_es_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_es_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es_detail'
    pass


@frr_show_evpn_es_detail_json.command('./	<cr>')
def frr_show_evpn_es_detail_json_cr():
    pass


@frr_show_evpn_es.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, ['NAME']), invoke_without_command=True)
def frr_show_evpn_es_esid():
    """ES ID"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_es_esid.name
    data_gen['ES_ID'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_evpn_es' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es'][key] = val
    
    # set VIEW_NODE -> show_evpn_es table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es'
    pass


@frr_show_evpn_es_esid.command('./	<cr>')
def frr_show_evpn_es_esid_cr():
    pass


@frr_show_evpn_es_esid.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_es_esid_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_es_esid_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_es' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es'][key] = val
    
    # set VIEW_NODE -> show_evpn_es table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es'
    pass


@frr_show_evpn_es_esid_json.command('./	<cr>')
def frr_show_evpn_es_esid_json_cr():
    pass


@frr_show_evpn_es.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_es_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_es_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_es' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_es']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_es'][key] = val
    
    # set VIEW_NODE -> show_evpn_es table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_es'
    pass


@frr_show_evpn_es_json.command('./	<cr>')
def frr_show_evpn_es_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn'][key] = val
    
    # set VIEW_NODE -> show_evpn table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn'
    pass


@frr_show_evpn_json.command('./	<cr>')
def frr_show_evpn_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='l2-nh', invoke_without_command=True)
def frr_show_evpn_l2nh(show_evpn_l2nh_='show_evpn_l2-nh'):
    """Layer2 nexthops"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_l2nh.name
    
    if 'VIEW_NODE|show_evpn_l2-nh' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_l2-nh'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_l2-nh']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_l2-nh'][key] = val
    
    # set VIEW_NODE -> show_evpn_l2-nh table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_l2-nh'
    pass


@frr_show_evpn_l2nh.command('./	<cr>')
def frr_show_evpn_l2nh_cr():
    pass


@frr_show_evpn_l2nh.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_l2nh_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_l2nh_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_l2-nh' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_l2-nh'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_l2-nh']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_l2-nh'][key] = val
    
    # set VIEW_NODE -> show_evpn_l2-nh table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_l2-nh'
    pass


@frr_show_evpn_l2nh_json.command('./	<cr>')
def frr_show_evpn_l2nh_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='mac',)
def frr_show_evpn_mac():
    """MAC addresses"""
    global COMMON_DATA_MAP
    
    pass


@frr_show_evpn_mac.group(cls=FRR_AbbreviationGroup, name='vni',)
def frr_show_evpn_mac_vni(show_evpn_mac_vni_='show_evpn_mac_vni'):
    """VxLAN Network Identifier"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni.name
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_evpn_mac_vni_all(show_evpn_mac_vni_all_='show_evpn_mac_vni_all'):
    """All VNIs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_all.name
    
    if 'VIEW_NODE|show_evpn_mac_vni_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni_all'
    pass


@frr_show_evpn_mac_vni_all.command('./	<cr>')
def frr_show_evpn_mac_vni_all_cr():
    pass


@frr_show_evpn_mac_vni_all.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_evpn_mac_vni_all_detail(show_evpn_mac_vni_all_detail_='show_evpn_mac_vni_all_detail'):
    """Detailed Information On Each VNI MAC"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_all_detail.name
    
    if 'VIEW_NODE|show_evpn_mac_vni_all_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni_all_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni_all_detail'
    pass


@frr_show_evpn_mac_vni_all_detail.command('./	<cr>')
def frr_show_evpn_mac_vni_all_detail_cr():
    pass


@frr_show_evpn_mac_vni_all_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_mac_vni_all_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_all_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_mac_vni_all_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni_all_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni_all_detail'
    pass


@frr_show_evpn_mac_vni_all_detail_json.command('./	<cr>')
def frr_show_evpn_mac_vni_all_detail_json_cr():
    pass


@frr_show_evpn_mac_vni_all.group(cls=FRR_AbbreviationGroup, name='duplicate', invoke_without_command=True)
def frr_show_evpn_mac_vni_all_duplicate(show_evpn_mac_vni_all_duplicate_='show_evpn_mac_vni_all_duplicate'):
    """Duplicate address list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_all_duplicate.name
    
    if 'VIEW_NODE|show_evpn_mac_vni_all_duplicate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_duplicate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_duplicate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_duplicate'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni_all_duplicate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni_all_duplicate'
    pass


@frr_show_evpn_mac_vni_all_duplicate.command('./	<cr>')
def frr_show_evpn_mac_vni_all_duplicate_cr():
    pass


@frr_show_evpn_mac_vni_all_duplicate.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_mac_vni_all_duplicate_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_all_duplicate_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_mac_vni_all_duplicate' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_duplicate'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_duplicate']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all_duplicate'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni_all_duplicate table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni_all_duplicate'
    pass


@frr_show_evpn_mac_vni_all_duplicate_json.command('./	<cr>')
def frr_show_evpn_mac_vni_all_duplicate_json_cr():
    pass


@frr_show_evpn_mac_vni_all.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_mac_vni_all_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_all_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_mac_vni_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni_all'
    pass


@frr_show_evpn_mac_vni_all_json.command('./	<cr>')
def frr_show_evpn_mac_vni_all_json_cr():
    pass


@frr_show_evpn_mac_vni_all.group(cls=FRR_AbbreviationGroup, name='vtep', invoke_without_command=True)
@click.argument('remote_vtep_ip_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_evpn_mac_vni_all_vtep(remote_vtep_ip_address, vtep_='vtep'):
    """Remote VTEP"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_all_vtep.name
    data_gen['vtep'] = vtep_='vtep'
    data_gen['REMOTE_VTEP_IP_ADDRESS'] = remote_vtep_ip_address
    
    if 'VIEW_NODE|show_evpn_mac_vni_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni_all'
    pass


@frr_show_evpn_mac_vni_all_vtep.command('./	<cr>')
def frr_show_evpn_mac_vni_all_vtep_cr():
    pass


@frr_show_evpn_mac_vni_all_vtep.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_mac_vni_all_vtep_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_all_vtep_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_mac_vni_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni_all'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni_all'
    pass


@frr_show_evpn_mac_vni_all_vtep_json.command('./	<cr>')
def frr_show_evpn_mac_vni_all_vtep_json_cr():
    pass


@frr_show_evpn_mac_vni.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, [(1, 16777215)]), invoke_without_command=True)
def frr_show_evpn_mac_vni_vninumber():
    """VNI number"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_vninumber.name
    data_gen['VNI_NUMBER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni_vninumber.command('./	<cr>')
def frr_show_evpn_mac_vni_vninumber_cr():
    pass


@frr_show_evpn_mac_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_evpn_mac_vni_vninumber_detail(detail_='detail'):
    """Detailed Information On Each VNI MAC"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_vninumber_detail.name
    data_gen['detail'] = detail_='detail'
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni_vninumber_detail.command('./	<cr>')
def frr_show_evpn_mac_vni_vninumber_detail_cr():
    pass


@frr_show_evpn_mac_vni_vninumber_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_mac_vni_vninumber_detail_json(detail_json_='detail_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_vninumber_detail_json.name
    data_gen['detail_json'] = detail_json_='detail_json'
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni_vninumber_detail_json.command('./	<cr>')
def frr_show_evpn_mac_vni_vninumber_detail_json_cr():
    pass


@frr_show_evpn_mac_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='duplicate', invoke_without_command=True)
def frr_show_evpn_mac_vni_vninumber_duplicate(duplicate_='duplicate'):
    """Duplicate address list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_vninumber_duplicate.name
    data_gen['duplicate'] = duplicate_='duplicate'
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni_vninumber_duplicate.command('./	<cr>')
def frr_show_evpn_mac_vni_vninumber_duplicate_cr():
    pass


@frr_show_evpn_mac_vni_vninumber_duplicate.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_mac_vni_vninumber_duplicate_json(duplicate_json_='duplicate_json'):
    """"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_vninumber_duplicate_json.name
    data_gen['duplicate_json'] = duplicate_json_='duplicate_json'
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni_vninumber_duplicate_json.command('./	<cr>')
def frr_show_evpn_mac_vni_vninumber_duplicate_json_cr():
    pass


@frr_show_evpn_mac_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_mac_vni_vninumber_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_vninumber_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni_vninumber_json.command('./	<cr>')
def frr_show_evpn_mac_vni_vninumber_json_cr():
    pass


@frr_show_evpn_mac_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='mac', invoke_without_command=True)
@click.argument('mac_address_', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_evpn_mac_vni_vninumber_mac(mac_address_, mac_='mac'):
    """MAC"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_vninumber_mac.name
    data_gen['mac'] = mac_='mac'
    data_gen['MAC_ADDRESS_'] = mac_address_
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni_vninumber_mac.command('./	<cr>')
def frr_show_evpn_mac_vni_vninumber_mac_cr():
    pass


@frr_show_evpn_mac_vni_vninumber_mac.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_mac_vni_vninumber_mac_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_vninumber_mac_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni_vninumber_mac_json.command('./	<cr>')
def frr_show_evpn_mac_vni_vninumber_mac_json_cr():
    pass


@frr_show_evpn_mac_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='vtep', invoke_without_command=True)
@click.argument('remote_vtep_ip_address', metavar='A.B.C.D', required=True, type=FRR_TYPE('A.B.C.D'))
def frr_show_evpn_mac_vni_vninumber_vtep(remote_vtep_ip_address, vtep_='vtep'):
    """Remote VTEP"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_vninumber_vtep.name
    data_gen['vtep'] = vtep_='vtep'
    data_gen['REMOTE_VTEP_IP_ADDRESS'] = remote_vtep_ip_address
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni_vninumber_vtep.command('./	<cr>')
def frr_show_evpn_mac_vni_vninumber_vtep_cr():
    pass


@frr_show_evpn_mac_vni_vninumber_vtep.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_mac_vni_vninumber_vtep_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_mac_vni_vninumber_vtep_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_mac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_mac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_mac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_mac_vni'
    pass


@frr_show_evpn_mac_vni_vninumber_vtep_json.command('./	<cr>')
def frr_show_evpn_mac_vni_vninumber_vtep_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='next-hops',)
def frr_show_evpn_nexthops():
    """Remote VTEPs"""
    global COMMON_DATA_MAP
    
    pass


@frr_show_evpn_nexthops.group(cls=FRR_AbbreviationGroup, name='vni',)
def frr_show_evpn_nexthops_vni(show_evpn_nexthops_vni_='show_evpn_next-hops_vni'):
    """L3 VNI"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_nexthops_vni.name
    
    if 'VIEW_NODE|show_evpn_next-hops_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_next-hops_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_next-hops_vni'
    pass


@frr_show_evpn_nexthops_vni.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_evpn_nexthops_vni_all(show_evpn_nexthops_vni_all_='show_evpn_next-hops_vni_all'):
    """All VNIs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_nexthops_vni_all.name
    
    if 'VIEW_NODE|show_evpn_next-hops_vni_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni_all'][key] = val
    
    # set VIEW_NODE -> show_evpn_next-hops_vni_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_next-hops_vni_all'
    pass


@frr_show_evpn_nexthops_vni_all.command('./	<cr>')
def frr_show_evpn_nexthops_vni_all_cr():
    pass


@frr_show_evpn_nexthops_vni_all.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_nexthops_vni_all_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_nexthops_vni_all_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_next-hops_vni_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni_all'][key] = val
    
    # set VIEW_NODE -> show_evpn_next-hops_vni_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_next-hops_vni_all'
    pass


@frr_show_evpn_nexthops_vni_all_json.command('./	<cr>')
def frr_show_evpn_nexthops_vni_all_json_cr():
    pass


@frr_show_evpn_nexthops_vni.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, [(1, 16777215)]), invoke_without_command=True)
def frr_show_evpn_nexthops_vni_vninumber():
    """VNI number"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_nexthops_vni_vninumber.name
    data_gen['VNI_NUMBER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_evpn_next-hops_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_next-hops_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_next-hops_vni'
    pass


@frr_show_evpn_nexthops_vni_vninumber.command('./	<cr>')
def frr_show_evpn_nexthops_vni_vninumber_cr():
    pass


@frr_show_evpn_nexthops_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='ip', invoke_without_command=True)
@click.argument('host_address', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_evpn_nexthops_vni_vninumber_ip(host_address, ip_='ip'):
    """Ip address"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_nexthops_vni_vninumber_ip.name
    data_gen['ip'] = ip_='ip'
    data_gen['HOST_ADDRESS'] = host_address
    
    if 'VIEW_NODE|show_evpn_next-hops_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_next-hops_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_next-hops_vni'
    pass


@frr_show_evpn_nexthops_vni_vninumber_ip.command('./	<cr>')
def frr_show_evpn_nexthops_vni_vninumber_ip_cr():
    pass


@frr_show_evpn_nexthops_vni_vninumber_ip.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_nexthops_vni_vninumber_ip_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_nexthops_vni_vninumber_ip_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_next-hops_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_next-hops_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_next-hops_vni'
    pass


@frr_show_evpn_nexthops_vni_vninumber_ip_json.command('./	<cr>')
def frr_show_evpn_nexthops_vni_vninumber_ip_json_cr():
    pass


@frr_show_evpn_nexthops_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_nexthops_vni_vninumber_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_nexthops_vni_vninumber_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_next-hops_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_next-hops_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_next-hops_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_next-hops_vni'
    pass


@frr_show_evpn_nexthops_vni_vninumber_json.command('./	<cr>')
def frr_show_evpn_nexthops_vni_vninumber_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='rmac',)
def frr_show_evpn_rmac():
    """RMAC addresses"""
    global COMMON_DATA_MAP
    
    pass


@frr_show_evpn_rmac.group(cls=FRR_AbbreviationGroup, name='vni',)
def frr_show_evpn_rmac_vni(show_evpn_rmac_vni_='show_evpn_rmac_vni'):
    """L3 VNI"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_rmac_vni.name
    
    if 'VIEW_NODE|show_evpn_rmac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_rmac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_rmac_vni'
    pass


@frr_show_evpn_rmac_vni.group(cls=FRR_AbbreviationGroup, name='all', invoke_without_command=True)
def frr_show_evpn_rmac_vni_all(show_evpn_rmac_vni_all_='show_evpn_rmac_vni_all'):
    """All VNIs"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_rmac_vni_all.name
    
    if 'VIEW_NODE|show_evpn_rmac_vni_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni_all'][key] = val
    
    # set VIEW_NODE -> show_evpn_rmac_vni_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_rmac_vni_all'
    pass


@frr_show_evpn_rmac_vni_all.command('./	<cr>')
def frr_show_evpn_rmac_vni_all_cr():
    pass


@frr_show_evpn_rmac_vni_all.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_rmac_vni_all_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_rmac_vni_all_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_rmac_vni_all' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni_all'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni_all']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni_all'][key] = val
    
    # set VIEW_NODE -> show_evpn_rmac_vni_all table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_rmac_vni_all'
    pass


@frr_show_evpn_rmac_vni_all_json.command('./	<cr>')
def frr_show_evpn_rmac_vni_all_json_cr():
    pass


@frr_show_evpn_rmac_vni.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(5, [(1, 16777215)]), invoke_without_command=True)
def frr_show_evpn_rmac_vni_vninumber():
    """VNI number"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_rmac_vni_vninumber.name
    data_gen['VNI_NUMBER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_evpn_rmac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_rmac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_rmac_vni'
    pass


@frr_show_evpn_rmac_vni_vninumber.command('./	<cr>')
def frr_show_evpn_rmac_vni_vninumber_cr():
    pass


@frr_show_evpn_rmac_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_rmac_vni_vninumber_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_rmac_vni_vninumber_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_rmac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_rmac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_rmac_vni'
    pass


@frr_show_evpn_rmac_vni_vninumber_json.command('./	<cr>')
def frr_show_evpn_rmac_vni_vninumber_json_cr():
    pass


@frr_show_evpn_rmac_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='mac', invoke_without_command=True)
@click.argument('macaddress_', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_show_evpn_rmac_vni_vninumber_mac(macaddress_, mac_='mac'):
    """MAC"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_rmac_vni_vninumber_mac.name
    data_gen['mac'] = mac_='mac'
    data_gen['MAC-ADDRESS_'] = macaddress_
    
    if 'VIEW_NODE|show_evpn_rmac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_rmac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_rmac_vni'
    pass


@frr_show_evpn_rmac_vni_vninumber_mac.command('./	<cr>')
def frr_show_evpn_rmac_vni_vninumber_mac_cr():
    pass


@frr_show_evpn_rmac_vni_vninumber_mac.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_rmac_vni_vninumber_mac_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_rmac_vni_vninumber_mac_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_rmac_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_rmac_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_rmac_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_rmac_vni'
    pass


@frr_show_evpn_rmac_vni_vninumber_mac_json.command('./	<cr>')
def frr_show_evpn_rmac_vni_vninumber_mac_json_cr():
    pass


@click.group(cls=FRR_AbbreviationGroup, name='vni', invoke_without_command=True)
def frr_show_evpn_vni(show_evpn_vni_='show_evpn_vni'):
    """VxLAN Network Identifier"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_vni.name
    
    if 'VIEW_NODE|show_evpn_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_vni'
    pass


@frr_show_evpn_vni.command('./	<cr>')
def frr_show_evpn_vni_cr():
    pass


@frr_show_evpn_vni.group(cls=FRR_AbbreviationGroup, name='detail', invoke_without_command=True)
def frr_show_evpn_vni_detail(show_evpn_vni_detail_='show_evpn_vni_detail'):
    """Detailed Information On Each VNI"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_vni_detail.name
    
    if 'VIEW_NODE|show_evpn_vni_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_vni_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_vni_detail'
    pass


@frr_show_evpn_vni_detail.command('./	<cr>')
def frr_show_evpn_vni_detail_cr():
    pass


@frr_show_evpn_vni_detail.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_vni_detail_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_vni_detail_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_vni_detail' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni_detail'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni_detail']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni_detail'][key] = val
    
    # set VIEW_NODE -> show_evpn_vni_detail table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_vni_detail'
    pass


@frr_show_evpn_vni_detail_json.command('./	<cr>')
def frr_show_evpn_vni_detail_json_cr():
    pass


@frr_show_evpn_vni.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_vni_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_vni_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_vni'
    pass


@frr_show_evpn_vni_json.command('./	<cr>')
def frr_show_evpn_vni_json_cr():
    pass


@frr_show_evpn_vni.group(cls=FRR_AbbreviationGroup, name=frr_group_choice(4, [(1, 16777215)]), invoke_without_command=True)
def frr_show_evpn_vni_vninumber():
    """VNI number"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_vni_vninumber.name
    data_gen['VNI_NUMBER'] = FRR_CLI_ARGS[name]
    
    if 'VIEW_NODE|show_evpn_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_vni'
    pass


@frr_show_evpn_vni_vninumber.command('./	<cr>')
def frr_show_evpn_vni_vninumber_cr():
    pass


@frr_show_evpn_vni_vninumber.group(cls=FRR_AbbreviationGroup, name='json', invoke_without_command=True)
def frr_show_evpn_vni_vninumber_json(json_='json'):
    """JavaScript Object Notation"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show_evpn_vni_vninumber_json.name
    data_gen['json'] = json_='json'
    
    if 'VIEW_NODE|show_evpn_vni' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show_evpn_vni'][key] = val
    
    # set VIEW_NODE -> show_evpn_vni table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show_evpn_vni'
    pass


@frr_show_evpn_vni_vninumber_json.command('./	<cr>')
def frr_show_evpn_vni_vninumber_json_cr():
    pass

