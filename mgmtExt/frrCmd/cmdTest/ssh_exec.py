#!/usr/bin/env python3
"""
ssh_exec.py  --host 192.168.1.10  --user ubuntu  --cmd "uptime" --cmd "df -h /"
             [--port 22] [--password *** | --pkey /path/to/key] [--timeout 5]
"""
import re
import time
import datetime
import random
import signal
import sys
import argparse, sys, paramiko, getpass
import json
import yaml
from types import SimpleNamespace        # std-lib, no extra package
from app_logging import Logging
from pathlib import Path

def handle_sigint(signum, frame):
    print("\nCaught Ctrl+C (SIGINT). Exiting gracefully...")
    sys.exit(0)

def clean_unbalanced_brackets(text):
    pairs = {'<': '>', '{': '}', '[': ']'}
    openers = set(pairs.keys())
    closers = set(pairs.values())
    stack = []
    result = []

    for char in text:
        if char in openers:
            stack.append((char, len(result)))  # store bracket and position
            result.append(char)
        elif char in closers:
            # check if matching opener is on the stack
            if stack and pairs[stack[-1][0]] == char:
                stack.pop()
                result.append(char)
            else:
                # unmatched closer, skip it
                continue
        else:
            result.append(char)

    # Remove unmatched openers from result by position
    for opener, index in reversed(stack):
        result.pop(index)

    return ''.join(result)
    
# Function to handle splitting while preserving brackets
def split_cli_preserving_brackets(input_text):
    result = []
    temp = ""
    stack = 0  # Tracks depth of <>, {}, or other delimiters
    open_delimiters = "<{["
    close_delimiters = ">}]"

    for char in input_text:
        if char in open_delimiters:
            if stack == 0 and temp.strip():
                # Add text before the opening delimiter
                result.append(temp.strip())
                temp = ""
            stack += 1
        elif char in close_delimiters:
            stack -= 1
        if stack > 0 or char != " ":
            temp += char
        elif temp.strip():
            result.append(temp.strip())  # Add standalone words
            temp = ""

    if temp.strip():  # Add any remaining part
        result.append(temp.strip())
    for i in range(len(result)):
        if '<<' in result[i]:
            elem = split_complex_choice(result[i])[0]
            result[i] = split_cli_preserving_brackets(elem)
            #result[i] = elem
        elem = result[i]
        if elem.count('<') >= 2 or '|>' in elem or ' ' in elem:
            print(f'elem=== {elem}')
            tokens = parse_prototype(elem)
            print(f'token=== {tokens}')
            if 'no' in tokens:
                token = 'no'
            elif len(tokens) == 1:
                token = parse_prototype(elem)[0]
            else:
                token = parse_prototype(elem)[1]
            result[i] = split_cli_preserving_brackets(token)
            
    # Now flatten
    flattened = []
    for item in result:
        if isinstance(item, list):
            flattened.extend(item)
        else:
            flattened.append(item)
                
    return flattened

def split_complex_choice(input_text):

    result = []
    temp = ""
    stack = []
    pairs = {"<": ">", "{": "}", "[": "]"}

    for char in input_text:
        if char in pairs:
            stack.append(pairs[char])
            temp += char
        elif char in pairs.values():
            if stack and char == stack[-1]:
                stack.pop()
            temp += char
        elif char == "|" and len(stack) == 1:
            result.append(temp.strip())
            temp = ""
        else:
            temp += char

    if temp.strip():
        result.append(temp.strip())
        
    for i in range(len(result)):
        result[i] = clean_unbalanced_brackets(result[i])

    return result
    
def parse_prototype(expression):
    """
    Splits a prototype string into top-level alternatives using the '|' character,
    while ignoring any '|' characters that appear within nested bracket pairs.

    It first removes any outer matching brackets (like <...>, [...], {...}, or (...))
    that enclose the entire expression. Then, processing the string character by character,
    it tracks nested brackets using a stack. A '|' is considered a separator only when
    the stack is empty.

    Example cases:
    
      1) "<type <macip|multicast>|vtep A.B.C.D>"
         -> ["type <macip|multicast>", "vtep A.B.C.D"]
         
      2) "<WORD|<A.B.C.D|X:X::X:X> <multihop|local-address <A.B.C.D|X:X::X:X>|interface IFNAME|vrf NAME>>"
         -> ["WORD", "<A.B.C.D|X:X::X:X> <multihop|local-address <A.B.C.D|X:X::X:X>|interface IFNAME|vrf NAME>"]
      
      3) "<view|vrf>"
         -> ["view", "vrf"]
      
      4) "<vrf <NAME|all>|>"
         -> ["vrf <NAME|all>", ""]
    """
    expr = expression.strip()
    
    # Remove outer brackets if they wrap the entire expression.
    if (expr.startswith('<') and expr.endswith('>')) or \
       (expr.startswith('[') and expr.endswith(']')) or \
       (expr.startswith('{') and expr.endswith('}')) or \
       (expr.startswith('(') and expr.endswith(')')):
        expr = expr[1:-1].strip()

    # Define matching bracket pairs.
    bracket_pairs = {'<': '>', '[': ']', '{': '}', '(': ')'}
    stack = []
    tokens = []
    current = []
    
    for char in expr:
        if char in bracket_pairs:
            # If an opening bracket is encountered, push its matching closing bracket.
            stack.append(bracket_pairs[char])
            current.append(char)
        elif stack and char == stack[-1]:
            # If the character matches the expected closing bracket, pop from the stack.
            stack.pop()
            current.append(char)
        elif char == '|' and not stack:
            # If at top level (no open brackets) and a '|' is found,
            # finish the current token and start a new one.
            tokens.append("".join(current).strip())
            current = []
        else:
            current.append(char)
    
    # Append the final token (even if it is empty).
    tokens.append("".join(current).strip())
    
    return tokens
    

# ---- 1. read TEMPLATE file --------------------------------------------------
def template(node):
    file_path = Path(f'./template/{node.upper()}.template')          # <-- replace with your file
    cmd_template = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:                 # line includes the trailing "\n"
                line = line.rstrip("\n")   # strip newline if you need a clean string
                line = line.replace('{', '<').replace('}', '>').replace('[', '<').replace(']', '|>')
                cmd_template.append(para_input(line))
    except:
        return []
    return cmd_template
    
def para_input(command_string):
    command_elements = split_cli_preserving_brackets(command_string)
    print(f'>>>>>>> {command_elements}')
    for i in range(len(command_elements)):
        elem = command_elements[i]

        if elem[0] == '[' and elem[-1] == ']':
            if '|' not in elem:
                elem = elem[1:-1]
            else:
                elem = ''
        elif elem[0] == '<' and elem[-1] == '>':
            elems = [part for part in re.split(r'[<|>]', elem) if part]
            elem = elems[0]
            if len(elems) > 1:
                elem = elems[0]
                
        if elem and elem[0] == '(' and elem[-1] == ')':
            elem = elem.replace('(', '').replace(')', '')
            int_range = elem.split('-')
            int_range = [part for part in elem.split('-') if part]
            if int_range[0] == int_range[1]:
                int_range[0] = f'-{int_range[0]}'
            #print(int_range[0])
            #print(int_range[1])
            if int_range[1] == '4294967295|METRIC':
                int_range[1] = '4294967295'
            elem = str(random.randint(int(int_range[0]), int(int_range[1])))
        else:
            pass

        #if ' ' in elem:
        #    elem = para_input(' '.join(elem.split()))
        
        #LOG.info(elem)
        if elem.isupper() and elem in PARA:
            elem = PARA[elem]
            
        if elem == 'cr' or elem == '<cr>':
            elem = ''

        command_elements[i] = elem
        
    command_elements = [s for s in command_elements if s != '']
    print(' '.join(command_elements))
    return ' '.join(command_elements)
            

def read_yaml_config(filepath='config.yml'):
    """Reads and parses a YAML configuration file."""
    try:
        with open(filepath, 'r') as file:
            config = yaml.safe_load(file)
        return config
    except FileNotFoundError:
        print("The file '{filepath}' was not found.")
        return None
    except yaml.YAMLError as exc:
        print(f" parsing YAML file: {exc}")
        return None
    
def cmd_exec(client, cmd):

    stdin, stdout, stderr = client.exec_command(cmd)
    # stream output live
    for line in stdout:
        if 'Unknown command' in line:
            return False
        if 'syntax error' in line:
            return False
    for line in stderr:
        if 'No such command' in line:
            return False
        if 'Missing command' in line:
            return False
    for line in stdout:   
        sys.stdout.write(line)
    for line in stderr:
        sys.stderr.write(line)
    exit_status = stdout.channel.recv_exit_status()
    #LOG.info(f"→ exit {exit_status}")
    if exit_status > 0:
        for line in stdout:
            sys.stdout.write(line)
        for line in stderr:
            sys.stderr.write(line)
            
    if exit_status < 3:
        return True
    return False
    
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def parse():
    p = argparse.ArgumentParser(description="Run command(s) over SSH")
    p.add_argument("--node", default='all')
    return p.parse_args()

def main():
    global PARA
    config = read_yaml_config()
    user = config['connection']['user']
    password = config['connection']['password']
    host = config['connection']['host']
    port = config['connection']['port']
    timeout = config['connection']['timeout']
    #nodes = [item.lstrip('-') for item in config['nodes'].split()]
    nodes = [item.lstrip('-').strip() for item in config["nodes"]]
    print(f'nodes-{nodes}')
    PARA = config['regexps']
    args = parse()
    
    with open('node_map.tree', 'r') as file:
        node_tree = json.loads(file.read())
        
    if args.node != 'all':
        nodes = [args.node]
    
    if not (password):
        # try key-agent first, else ask interactively
        try: _ = paramiko.Agent().get_keys()
        except Exception: pass
        else:
            if not list(_):                # no key in agent
                password = getpass.getpass(f"{user}@{host}'s password: ")

    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # production: use known_hosts
    #try:
    client.connect(
        hostname=host,
        port=port,
        username=user,
        password=password,
        key_filename=None,
        timeout=timeout,
    )
    

    log_name = ''
    for ns in nodes:
        ns = [ns]
        
        def get_nodes(ns, node_tree):
            if len(node_tree) > 0:
                for n in node_tree.keys():
                    ns.append(n)
                    get_nodes(ns, node_tree[n])
              
        if ns[0] in node_tree['CONFIG_NODE']:
            print(node_tree['CONFIG_NODE'][ns[0]])
            get_nodes(ns, node_tree['CONFIG_NODE'][ns[0]])
            
        try:
            for handler in LOG.handlers[:]:
                LOG.removeHandler(handler) 
        except Exception as e:
            print(e)
            
        LOG = Logging(ns[0]).getLogger()

        for node in ns:
            total = 0
            frr_success = 0
            frr_fail = 0
            sonic_success = 0
            sonic_fail = 0
            differ = 0
            
            start = datetime.datetime.now()
                
            template_cmd = template(node)
            if len(template_cmd) == 0:
                continue
            LOG.info(f'\nStart time {start.strftime("%Y-%m-%d %H:%M:%S")}')
            LOG.info(f"=== {node} NODE ===")

            for cmd in template_cmd:
                total += 1
                time.sleep(0.3)

                ### frr's vtysh

                cmds = []
                cmd_tmp = []
                for c in cmd.split():
                    if '_NODE' in c:
                        if c == 'CONFIG_NODE':
                            cmds.append("-c 'configure terminal'")
                        elif len(cmd_tmp) > 0:
                            cmds.append(f"-c '{' '.join(cmd_tmp)}'")
                            cmd_tmp = []
                    else:
                        cmd_tmp.append(c)
                        
                cmds.append(f"-c '{' '.join(cmd_tmp)}'")
                cmd_run = f"vtysh {' '.join(cmds)}"
                cmd_run_node = ' '.join(cmd_tmp)
                
                result_frr = cmd_exec(client, cmd_run)
                if result_frr:
                    LOG.info(f"[#{total}/{len(template_cmd)}][FRR]   {cmd_run} --> success")
                    frr_success +=1
                else:
                    LOG.info(f"[#{total}/{len(template_cmd)}][FRR]   {cmd_run} -->fail")
                    frr_fail +=1
                
                time.sleep(0.2)
                ### frr's vtysh
                if node == 'VIEW_NODE':
                    cmd_prefix = 'frr'
                else:
                    cmd_prefix = 'frr config'
                
                cmd_tmp = cmd.split()
                for i in range(len(cmd_tmp)):
                    if '_NODE' in cmd_tmp[i]:
                        cmd_tmp[i] = ''
                        
                cmd = cmd_prefix + ' '.join(cmd_tmp)
                cmd.replace('<cr>', '')
                result_sonic = cmd_exec(client, cmd)
                if result_sonic and result_frr:
                    LOG.info(f"[#{total}/{len(template_cmd)}][SONIC] {cmd} --> success")
                    sonic_success +=1
                else:
                    LOG.info(f"[#{total}/{len(template_cmd)}][SONIC] {cmd} --> fail")
                    result_sonic = False
                    sonic_fail +=1
                    
                if result_frr and result_sonic :
                    if result_frr:
                        LOG.info(f"[#{total}/{len(template_cmd)}][compare] SAME")
                    else:
                        LOG.info(f"[#{total}/{len(template_cmd)}][compare] SAME")
                elif not result_frr and not result_sonic :
                        LOG.info(f"[#{total}/{len(template_cmd)}][compare] SAME")
                else:
                    LOG.info(f"[#{total}/{len(template_cmd)}][compare] DIFFER")
                    differ += 1
                    #stop_here()
                
                LOG.info('-----------')
                    
            finish = datetime.datetime.now()
            LOG.info(f'[{node}]')
            LOG.info(f'End time {finish.strftime("%Y-%m-%d %H:%M:%S")}\tDuration {finish-start}')
            LOG.info(f'Total CMDs: {total}')
            LOG.info(f'FRR Success: {frr_success}(rate: {int(frr_success*100/total)}%)')
            LOG.info(f'FRR Fail: {frr_fail}')
            
            LOG.info(f'SONIC Success: {sonic_success}(rate: {int(sonic_success*100/total)}%)')
            LOG.info(f'SONIC Fail: {sonic_fail}')
            LOG.info(f'Same: {total - differ}')
            LOG.info(f'Differ: {differ}')
                


    #except Exception as e:
    #    print('connect error: {}'.format(e))
    #    client.close()
        
if __name__ == "__main__":
    # Register the signal handler
    signal.signal(signal.SIGINT, handle_sigint)
    
    main()
