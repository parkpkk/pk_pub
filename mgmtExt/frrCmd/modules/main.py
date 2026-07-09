import os
import json
import click
import time
import importlib
import inspect
import subprocess
import utilities_common.cli as clicommon

from swsscommon.swsscommon import SonicV2Connector
from frr.validated_config_db_connector import ValidatedConfigDBConnector
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *

from click.utils import echo
from threading import Thread
show_state_th = Thread(target=lambda: show_state_db('vtysh'))

import sys
first_arg = sys.argv[1] if len(sys.argv) > 1 else ""
second_arg = sys.argv[2] if len(sys.argv) > 2 else ""
third_arg = sys.argv[3] if len(sys.argv) > 3 else ""

state_db = SonicV2Connector()
state_db.connect(state_db.STATE_DB)

def exec_cmd(commands):
    cmd = ["vtysh"] + [arg for c in commands for arg in ["-c", c]]
    #print('run commands: {}'.format(cmd))
    try:
        result = subprocess.run(cmd, text=True, capture_output=True, timeout=1)
        data = result.stdout
    except subprocess.TimeoutExpired:
        data = "Command timed out!"
    print(data)
    
def show_state_db(key):
    #twamp_table_keys = state_db.keys(state_db.STATE_DB, "FRR_VTYSH_RETURN|*")
    global CONFIG_DB
    save_config = None
    non_config_cmd = ['show', 'ping', 'traceroute', 'list', 'find', 'exit',
                      'quit', 'end', 'write', 'enable', 'disable', 'watchfrr', 'clear', 'no']
    for i in range(10):
        time.sleep(0.05)
        if len(COMMON_DATA_MAP) < 2:
            continue
        cmds = []
        for k , v in COMMON_DATA_MAP.items():
            if '|' in k:
                keys = k.split('|')
                if keys[0] in COMMON_DATA_MAP:
                    main_node = keys[0]
                    cmd_1st = keys[1].split('_')[0]
                    key_store = COMMON_DATA_MAP[keys[0]]
                    
                    if type(key_store) == tuple and key_store[0].split('|')[-1] != keys[1]:
                        continue

                    ### make list cmd
                    if main_node == 'CONFIG_NODE':
                        cmds.append('configure terminal')
                    if type(key_store) == tuple:
                        temp_cmd = list(key_store)
                        cmd = []
                        for cs in temp_cmd:
                            cmd.append(cs.replace('|', ' ').replace('_', ' '))
                        n_cmd = ' '.join(cmd)
                        if len(cmds) > 0 and n_cmd.startswith(cmds[-1]):
                            n_cmd = n_cmd.replace(f'{cmds[-1]} ', '')
                    elif type(key_store) == str:
                        n_cmd = key_store.replace('_', ' ')
                    for a, b in COMMON_DATA_MAP[k].items(): 
                        if a.islower() or b not in n_cmd:
                            n_cmd += f' {b}'
                    if n_cmd not in cmds:
                        cmds.append(n_cmd)
                    
                    #print(cmds)
                    ### check non-config cmd
                    if main_node == 'VIEW_NODE' or cmd_1st in non_config_cmd:
                        if cmd_1st == 'no' or cmd_1st == 'clear':
                            temp_key_store = list(key_store)[0]
                            temp_key_store = temp_key_store.replace('no|', '').replace('no_', '')
                            temp_key_store = temp_key_store.replace('clear|', '').replace('clear_', '')
                            keys = temp_key_store.split('|')

                            keys.append(key_store[1])
                            my_dict = CONFIG_DB.get_entry(main_node, '|'.join(keys))
                            if my_dict:
                                CONFIG_DB.set_entry(main_node, '|'.join(keys), None)
                            else:
                                #print(f"Cannot del with key: {'|'.join(keys)}")
                                my_dict = CONFIG_DB.get_entry(main_node, '|'.join(keys.pop()))
                                if my_dict:
                                    CONFIG_DB.set_entry(main_node, '|'.join(keys), None)
                                else:
                                    #print(f"Cannot del with key: {'|'.join(keys)}")
                                    pass
                              
                        continue

                    CONFIG_DB.set_entry(main_node, key_store, None)
                    time.sleep(0.005)
                    CONFIG_DB.set_entry(main_node, key_store, {})
                    time.sleep(0.005)
                    for a, b in COMMON_DATA_MAP[k].items():
                        time.sleep(0.005)
                        #print(f'{main_node}-{key_store}-{(a,b)}')
                        CONFIG_DB.mod_entry(main_node, key_store, {a:b})
                    if main_node == 'VIEW_NODE' and 'write' in key_store:
                        save_config = 'write_terminal'
        if len(cmds) > 0:
            exec_cmd(cmds)
        break
        
    for i in range(30):
        time.sleep(0.05)          
        val = state_db.get_all(state_db.STATE_DB, 'FRR_VTYSH_RETURN|{}'.format(key))
    
        if val.get('vtysh') and len(val.get('vtysh')) > 0:    
            if val.get('vtysh') == 'XXXXX':
                break
            print('{}'.format(val.get('vtysh')))
            break
            
    #send signal read status finish     
    CONFIG_DB.set_entry('CONFIG_STATE', 'state_read', {})
    
    if save_config:
        CONFIG_DB.set_entry('VIEW_NODE', save_config, None)
        CONFIG_DB.set_entry('VIEW_NODE', save_config, {})
        for i in range(20):
            time.sleep(0.1)          
            val = state_db.get_all(state_db.STATE_DB, 'FRR_VTYSH_RETURN|{}'.format(key))
        
            if val.get('vtysh') and len(val.get('vtysh')) > 0:    
                if val.get('vtysh') == 'XXXXX':
                    break
                frr_config = val.get('vtysh')
                if 'configuration' in frr_config:
                    with open("/tmp/frr_all.conf", "w") as f:
                        f.write(frr_config)
                break

### 'frr' group ('frr ...')
@click.group(cls=FRR_AbbreviationGroup, name='frr')
@clicommon.pass_db
def frr(db):
    """frr-related configuration tasks"""
    global CONFIG_DB
    CONFIG_DB = ValidatedConfigDBConnector(db.cfgdb)
    show_state_th.start()
    pass
    

@frr.group(cls=FRR_AbbreviationGroup, name='add',)
def frr_add(add_='add'):
    """Add"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_add.name
    
    if 'VIEW_NODE|add' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|add'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|add']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|add'][key] = val
    
    # set VIEW_NODE -> add table
    COMMON_DATA_MAP['VIEW_NODE'] = 'add'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='clear',)
def frr_clear(clear_='clear'):
    """Reset functions"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_clear.name
    
    if 'VIEW_NODE|clear' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|clear'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|clear']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|clear'][key] = val
    
    # set VIEW_NODE -> clear table
    COMMON_DATA_MAP['VIEW_NODE'] = 'clear'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='config',)

def frr_config():
    """CONFIG_NODE node related command"""
    global COMMON_DATA_MAP
    
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='configure', invoke_without_command=True)
def frr_configure(configure_='configure'):
    """Configuration from vty interface"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_configure.name
    
    if 'VIEW_NODE|configure' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|configure'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|configure']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|configure'][key] = val
    
    # set VIEW_NODE -> configure table
    COMMON_DATA_MAP['VIEW_NODE'] = 'configure'
    pass


@frr_configure.command('./	<cr>')
def frr_configure_cr():
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='copy',)
@click.argument('config_filename', metavar='FILENAME', required=True, type=FRR_TYPE('FILENAME'))
def frr_copy(config_filename, copy_='copy'):
    """Copy configuration"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_copy.name
    data_gen['CONFIG_FILENAME'] = config_filename
    
    if 'VIEW_NODE|copy' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|copy'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|copy']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|copy'][key] = val
    
    # set VIEW_NODE -> copy table
    COMMON_DATA_MAP['VIEW_NODE'] = 'copy'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='debug',)
def frr_debug(debug_='debug'):
    """Debugging functions"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_debug.name
    
    if 'VIEW_NODE|debug' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|debug'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|debug']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|debug'][key] = val
    
    # set VIEW_NODE -> debug table
    COMMON_DATA_MAP['VIEW_NODE'] = 'debug'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='disable', invoke_without_command=True)
def frr_disable(disable_='disable'):
    """Turn off privileged mode command"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_disable.name
    
    if 'VIEW_NODE|disable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|disable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|disable']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|disable'][key] = val
    
    # set VIEW_NODE -> disable table
    COMMON_DATA_MAP['VIEW_NODE'] = 'disable'
    pass


@frr_disable.command('./	<cr>')
def frr_disable_cr():
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='enable', invoke_without_command=True)
def frr_enable(enable_='enable'):
    """Turn on privileged mode command"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_enable.name
    
    if 'VIEW_NODE|enable' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|enable'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|enable']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|enable'][key] = val
    
    # set VIEW_NODE -> enable table
    COMMON_DATA_MAP['VIEW_NODE'] = 'enable'
    pass


@frr_enable.command('./	<cr>')
def frr_enable_cr():
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='end', invoke_without_command=True)
def frr_end(end_='end'):
    """End current mode and change to enable mode."""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_end.name
    
    if 'VIEW_NODE|end' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|end'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|end']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|end'][key] = val
    
    # set VIEW_NODE -> end table
    COMMON_DATA_MAP['VIEW_NODE'] = 'end'
    pass


@frr_end.command('./	<cr>')
def frr_end_cr():
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='exit', invoke_without_command=True)
def frr_exit(exit_='exit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_exit.name
    
    if 'VIEW_NODE|exit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|exit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|exit']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|exit'][key] = val
    
    # set VIEW_NODE -> exit table
    COMMON_DATA_MAP['VIEW_NODE'] = 'exit'
    pass


@frr_exit.command('./	<cr>')
def frr_exit_cr():
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='find',)
def frr_find(find_='find'):
    """Find CLI command matching a regular expression"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_find.name
    
    if 'VIEW_NODE|find' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|find'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|find']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|find'][key] = val
    
    # set VIEW_NODE -> find table
    COMMON_DATA_MAP['VIEW_NODE'] = 'find'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='graceful-restart',)
def frr_gracefulrestart():
    """Graceful Restart commands"""
    global COMMON_DATA_MAP
    
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='list', invoke_without_command=True)
def frr_list(list_='list'):
    """Print command list"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_list.name
    
    if 'VIEW_NODE|list' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|list'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|list']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|list'][key] = val
    
    # set VIEW_NODE -> list table
    COMMON_DATA_MAP['VIEW_NODE'] = 'list'
    pass


@frr_list.command('./	<cr>')
def frr_list_cr():
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='mtrace', invoke_without_command=True)
@click.argument('word_value', metavar='WORD', required=True, type=FRR_TYPE('WORD'))
def frr_mtrace(word_value, mtrace_='mtrace'):
    """Multicast trace route to multicast source"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_mtrace.name
    data_gen['WORD_VALUE'] = word_value
    
    if 'VIEW_NODE|mtrace' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|mtrace'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|mtrace']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|mtrace'][key] = val
    
    # set VIEW_NODE -> mtrace table
    COMMON_DATA_MAP['VIEW_NODE'] = 'mtrace'
    pass


@frr_mtrace.command('./	<cr>')
def frr_mtrace_cr():
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='no',)
def frr_no():
    """Negate a command or set its defaults"""
    global COMMON_DATA_MAP
    
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='output',)
def frr_output(output_='output'):
    """Direct vtysh output to file"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_output.name
    
    if 'VIEW_NODE|output' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|output'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|output']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|output'][key] = val
    
    # set VIEW_NODE -> output table
    COMMON_DATA_MAP['VIEW_NODE'] = 'output'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='ping',)
def frr_ping(ping_='ping'):
    """Send echo messages"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_ping.name
    
    if 'VIEW_NODE|ping' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|ping'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|ping']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|ping'][key] = val
    
    # set VIEW_NODE -> ping table
    COMMON_DATA_MAP['VIEW_NODE'] = 'ping'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='quit', invoke_without_command=True)
def frr_quit(quit_='quit'):
    """Exit current mode and down to previous mode"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_quit.name
    
    if 'VIEW_NODE|quit' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|quit'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|quit']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|quit'][key] = val
    
    # set VIEW_NODE -> quit table
    COMMON_DATA_MAP['VIEW_NODE'] = 'quit'
    pass


@frr_quit.command('./	<cr>')
def frr_quit_cr():
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='show',)
def frr_show(show_='show'):
    """Show running system information"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_show.name
    
    if 'VIEW_NODE|show' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|show'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|show']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|show'][key] = val
    
    # set VIEW_NODE -> show table
    COMMON_DATA_MAP['VIEW_NODE'] = 'show'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='terminal',)
def frr_terminal(terminal_='terminal'):
    """Set terminal line parameters"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_terminal.name
    
    if 'VIEW_NODE|terminal' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|terminal'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|terminal']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|terminal'][key] = val
    
    # set VIEW_NODE -> terminal table
    COMMON_DATA_MAP['VIEW_NODE'] = 'terminal'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='traceroute',)
def frr_traceroute(traceroute_='traceroute'):
    """Trace route to destination"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_traceroute.name
    
    if 'VIEW_NODE|traceroute' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|traceroute'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|traceroute']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|traceroute'][key] = val
    
    # set VIEW_NODE -> traceroute table
    COMMON_DATA_MAP['VIEW_NODE'] = 'traceroute'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='watchfrr',)
def frr_watchfrr(watchfrr_='watchfrr'):
    """Watchfrr Specific sub-command"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_watchfrr.name
    
    if 'VIEW_NODE|watchfrr' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|watchfrr'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|watchfrr']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|watchfrr'][key] = val
    
    # set VIEW_NODE -> watchfrr table
    COMMON_DATA_MAP['VIEW_NODE'] = 'watchfrr'
    pass


@frr.group(cls=FRR_AbbreviationGroup, name='write', invoke_without_command=True)
def frr_write(write_='write'):
    """Write running configuration to memory, network, or terminal"""
    global COMMON_DATA_MAP
    #ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    data_gen = {}
    name = frr_write.name
    
    if 'VIEW_NODE|write' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['VIEW_NODE|write'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['VIEW_NODE|write']:
            key = key.upper()
        COMMON_DATA_MAP['VIEW_NODE|write'][key] = val
    
    # set VIEW_NODE -> write table
    COMMON_DATA_MAP['VIEW_NODE'] = 'write'
    pass


@frr_write.command('./	<cr>')
def frr_write_cr():
    pass


main = importlib.import_module(f'frr.main')
module_name = None
if first_arg:
    module_name = first_arg

if len(get_incomplete()) > 0:
    module_name = get_incomplete()[1]

if module_name:
    try:
        module_name = module_name.replace('-','')
        module = importlib.import_module(f'frr.{module_name}')
        add_func = getattr(main, f'frr_{module_name}')
        for name, obj in inspect.getmembers(module):
            if isinstance(obj, click.Command):
                if len(name.split('_')) == 3:
                    func = getattr(module, name)
                    add_func.add_command(func)
                    
        module_path = module_name  
        module_name = None
        if second_arg:
            module_name = second_arg

        if len(get_incomplete()) > 1:
            module_name = get_incomplete()[2]

        if module_path == 'show' and module_name:
            module_name = module_name.replace('-','')
            show_module = module
            try:
                module = importlib.import_module(f'frr.main_{module_path}.{module_path}_{module_name}')
                add_func = getattr(show_module, f'frr_{module_path}_{module_name}')
                for name, obj in inspect.getmembers(module):
                    if isinstance(obj, click.Command):
                        if len(name.split('_')) == 4:
                            func = getattr(module, name)
                            add_func.add_command(func)
            except Exception as e:
                #echo(str(e).replace(' ', '_'))
                pass
                
        if module_path == 'config' and module_name == 'router':
            config_module = module
            module_path = 'config_router'
            module_name = None
            config_module = module
            if third_arg:
                module_name = third_arg

            if len(get_incomplete()) > 1:
                module_name = get_incomplete()[3]
            if module_name:
                try:
                    module = importlib.import_module(f'frr.{module_path}.router_{module_name}')
                    add_func = getattr(config_module, f'frr_{module_path}_{module_name}')
                    for name, obj in inspect.getmembers(module):
                        if isinstance(obj, click.Command):
                            if len(name.split('_')) == 5:
                                func = getattr(module, name)
                                add_func.add_command(func)
                except Exception as e:
                    #echo(str(e).replace(' ', '_'))
                    pass
    except Exception as e:
        #echo(str(e).replace(' ', '_'))
        pass
