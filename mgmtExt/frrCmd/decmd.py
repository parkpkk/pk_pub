import os
import re
import json
import time
from defunc import parse_all_defuns
from denode import parse_install_elements, parse_defunsh, parse_vtysh_exit, parse_graph

from app_logging import LOG
CASE_DICT = {}
YANG_FILE = """
module {MODULE_NAME} {
    namespace "http://github.com/sonic-net/frr/{MODULE_NAME}";
    prefix {PREFIX};
    yang-version 1.1;

    import ietf-inet-types {
        prefix inet;
    }

    organization
        "SONiC";

    contact
        "SONiC";

    description
        "SONIC {PREFIX} FRR YANG";

    revision 2024-12-23 {
        description
            "Initial revision.";
    }
    container {CONTAINER_NAME} {
{YANG_GEN}
    }
}
"""


def read_mk_file(mk_file):
    """
    Read a .mk file and return a dictionary of key/value pairs.
    Lines starting with '#' or with only whitespace are skipped.
    Lines with '+=' are appended to any existing value for the key.
    """
    if not os.path.exists(mk_file):
        LOG.error(f".mk file '{mk_file}' not found.")
        return {}

    variables = {}

    try:
        with open(mk_file, 'r') as file:
            for line in file:
                # Remove any comments and extra whitespace.
                line = line.split('#', 1)[0].strip()
                if not line:
                    continue

                # Process key-value pairs.
                if '+=' in line:
                    key, value = map(str.strip, line.split('+=', 1))
                    # Append value, ensuring a single space separation.
                    variables[key] = (variables.get(
                        key, "") + " " + value).strip()
                elif '=' in line:
                    key, value = map(str.strip, line.split('=', 1))
                    variables[key] = value

    except Exception as e:
        LOG.error(f" reading the .mk file: {e}")
        return {}

    return variables


LIST_IMPORT = []


def process_input_files(mk_file):
    variables = read_mk_file(mk_file)
    if not variables:
        return

    # Get the input files from the parsed variables
    input_files = variables.get('input_files', '').split()
    str_out = ''
    for c_file in input_files:
        # Check if the input file exists
        if '.c' in c_file:
            h_file = c_file.replace('.c', '.h')
            files = [c_file, h_file]
        else:
            files = [c_file]

        for f in files:
            if not os.path.exists(f):
                LOG.error(f"Input file '{f}' not found.")
                continue
            # Process the input file
            try:
                with open(f, 'r') as file:
                    LOG.info(f"Contents of '{f}':")
                    location = f.split('/')[1]
                    if location != 'lib':
                        if location[-1] == 'd':
                            node = location[:-1]
                        else:
                            node = location
                        if node not in LIST_IMPORT:
                            LIST_IMPORT.append(node)

                    str_out = str_out + file.read()
            except Exception as e:
                LOG.error(f" reading the input file '{f}': {e}")

    return str_out


def nodes_graph():
    NODES_DOT = '../doc/figures/nodes.dot'
    graph_content_ = ''
    if os.path.exists(NODES_DOT):
        try:
            with open(NODES_DOT, 'r') as file:
                graph_content_ = file.read()
        except Exception as e:
            LOG.error(f" reading the input file '{input_file}': {e}")
    parsed_graph = parse_graph(graph_content_)
    # for edge in parsed_graph["edges"]:
    #    LOG.info(edge)
    return parsed_graph


VIEW_NODE_LIST = ['add', 'clear', 'configure', 'copy', 'debug', 'disable', 'enable', 'end', 'exit', 'find', 'graceful-restart',
                  'list', 'mtrace', 'no', 'output', 'ping', 'quit', 'show', 'terminal', 'traceroute', 'watchfrr', 'write', '[no]']
CONFIG_NODE_LIST = ['access-list', 'agentx', 'allow-external-route-update', 'allow-reserved-ranges', 'banner', 'bfd', 'bgp', 'clear', 'debug', 'domainname', 'dump', 'enable', 'end', 'evpn', 'exit', 'find', 'fpm', 'frr', 'hostname', 'interface', 'ip', 'ipv6', 'key', 'l2vpn',
                    'line', 'list', 'log', 'mac', 'mpls', 'nexthop-group', 'nhrp', 'no', 'output', 'password', 'pbr', 'pbr-map', 'pseudowire', 'quit', 'route-map', 'router', 'router-id', 'rpki', 'segment-routing', 'service', 'terminal', 'username', 'vni', 'vrf', 'vrrp', 'zebra', '[no]']

UNKNOW_NODE_CMD = {}
#UNKNOW_NODE_CMD['config_list_cmd'] = 'CONFIG_NODE'
#UNKNOW_NODE_CMD['find_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['config_exit_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['config_quit_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['config_end_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['config_help_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['show_cli_graph_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['show_config_candidate_section_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['config_write_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['show_running_config_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['autocomplete_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['config_commit_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['config_commit_comment_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['config_commit_check_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['config_update_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['config_discard_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['show_config_running_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['show_config_candidate_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['show_config_compare_cmd'] = 'CONFIG_NODE'
UNKNOW_NODE_CMD['show_config_transaction_cmd'] = 'CONFIG_NODE'
	
UNKNOW_NODE_CMD['no_match_metric_val_cmd'] = 'RMAP_NODE'
UNKNOW_NODE_CMD['no_match_interface_val_cmd'] = 'RMAP_NODE'
UNKNOW_NODE_CMD['no_match_ip_next_hop_val_cmd'] = 'RMAP_NODE'
UNKNOW_NODE_CMD['no_match_ip_next_hop_prefix_list_val_cmd'] = 'RMAP_NODE'
UNKNOW_NODE_CMD['no_match_ip_address_val_cmd'] = 'RMAP_NODE'
UNKNOW_NODE_CMD['no_match_ip_address_prefix_list_val_cmd'] = 'RMAP_NODE'
UNKNOW_NODE_CMD['no_match_tag_val_cmd'] = 'RMAP_NODE'
UNKNOW_NODE_CMD['set_metric_addsub_cmd'] = 'RMAP_NODE'
UNKNOW_NODE_CMD['no_set_metric_val_cmd'] = 'RMAP_NODE'
UNKNOW_NODE_CMD['no_set_ip_nexthop_val_cmd'] = 'RMAP_NODE'
UNKNOW_NODE_CMD['no_set_tag_val_cmd'] = 'RMAP_NODE'

UNKNOW_NODE_CMD['show_ipv6_ospf6_database_type_adv_router_linkstate_id_cmd'] = 'VIEW_NODE'
UNKNOW_NODE_CMD['show_ipv6_ospf6_database_type_self_originated_linkstate_id_cmd'] = 'VIEW_NODE'
UNKNOW_NODE_CMD['config_list_cmd'] = 'VIEW_NODE'
UNKNOW_NODE_CMD['find_cmd'] = 'VIEW_NODE'
UNKNOW_NODE_CMD['show_cli_graph_vtysh_cmd'] = 'VIEW_NODE'
UNKNOW_NODE_CMD['vtysh_output_file_cmd'] = 'VIEW_NODE'
UNKNOW_NODE_CMD['no_vtysh_output_file_cmd'] = 'VIEW_NODE'
UNKNOW_NODE_CMD['show_ip_bgp_l2vpn_evpn_neighbor_advertised_routes_cmd'] = 'VIEW_NODE'
UNKNOW_NODE_CMD['show_ip_bgp_l2vpn_evpn_rd_neighbor_advertised_routes_cmd'] = 'VIEW_NODE'

def decmd_run():
    IMPORT_MK = "import.mk"  # Path to the .mk file
    c_out = process_input_files(IMPORT_MK)

    node_dict = parse_install_elements(c_out)
    cmd_list = parse_all_defuns(c_out)
    
    #LOG.info('node_dict {}'.format(node_dict))
    existed = []
    
    extra_cmd_list = []
    for i in range(len(cmd_list)):
        cmd_dict = cmd_list[i]
        if cmd_dict["command_name"] in node_dict:
            nodes = node_dict[cmd_dict["command_name"]]
            for NODE in nodes:
                if 'node' not in cmd_dict:
                    cmd_dict["node"] = NODE
                else:
                    new_cmd = cmd_dict.copy()
                    new_cmd['node'] = NODE
                    extra_cmd_list.append(new_cmd)
                    
        else:
            cmd_dict["node"] = 'node'
    cmd_list += extra_cmd_list
        
    clone_cmd_list = []
    no_node_cmds = []
    for i in range(len(cmd_list)):
        cmd_dict = cmd_list[i]
        if 'PROTO_NAME' in cmd_dict['command_string']:
            clone_cmd = cmd_list[i].copy()
            clone_cmd['command_string'] = clone_cmd['command_string'].replace('PROTO_NAME', 'openfabric')
            clone_cmd_list.append(clone_cmd)
            cmd_list[i]['command_string'] = cmd_list[i]['command_string'].replace('PROTO_NAME', 'isis')
        
        if 'node' in cmd_dict["node"]:
            print('special command === {}'.format(cmd_dict['command_string']))
            print(cmd_dict['command_name'])
            if cmd_dict['command_name'] in UNKNOW_NODE_CMD:
                cmd_dict["node"] = UNKNOW_NODE_CMD[cmd_dict['command_name'] ]
            else:
                no_node_cmds.append(cmd_dict['command_name'])

            if cmd_dict['command_string'].split()[0] in CONFIG_NODE_LIST:
                if cmd_dict["node"] == 'VIEW_NODE':
                    clone_cmd = cmd_list[i].copy()
                    clone_cmd["node"] = 'CONFIG_NODE'
                    clone_cmd_list.append(clone_cmd)

        if cmd_dict["node"] == 'VIEW_NODE' or cmd_dict["node"] == 'ENABLE_NODE':
            if cmd_dict['command_string'].split()[0] not in VIEW_NODE_LIST:
                cmd_list[i]['command_type'] = 'REMOVED_COMMAND'

        if cmd_dict["node"] == 'CONFIG_NODE':
            if cmd_dict['command_string'].split()[0] not in CONFIG_NODE_LIST:
                cmd_list[i]['command_type'] = 'REMOVED_COMMAND'
                

    cmd_list += clone_cmd_list
    #print(no_node_cmds)
    #print(len(no_node_cmds))
    #stop_here()

    # for cmd in cmd_list:
    #    LOG.info('cmd name {}'.format(cmd["command_name"]))
    return cmd_list
    
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
    return result


def parse_template(template):
    """
    Parse a CLI-like template containing nested angle-brackets (< >).
    Split on '|' at the top level only, ignoring '|' inside nested brackets.

    E.g. '<type <macip|multicast>|vtep A.B.C.D>' -> 
         ['type <macip|multicast>', 'vtep A.B.C.D']
    """

    # Optional: remove the outer brackets if the entire string is wrapped
    if template.startswith('<') and template.endswith('>'):
        template = template[1:-1].strip()

    # We'll scan through the string and keep track of whether we're inside '< >'
    # The counter `stack` increments when we see '<' and decrements on '>'
    # A top-level '|' (stack == 0) is where we split.
    result = []
    stack = 0
    token = []

    for char in template:
        if char == '<':
            stack += 1
            token.append(char)
        elif char == '>':
            stack -= 1
            token.append(char)
        elif char == '|' and stack == 0:
            # We are at top-level -> split here
            result.append("".join(token).strip())
            token = []
        else:
            token.append(char)

    # Append the last token if any
    if token:
        result.append("".join(token).strip())

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

def generate_cmd_tree(cmd_tree, command_elements, descriptions):

    count_pre = 0
    count = 0
    elem_pre = None
    command_array = []
    #print(f'================-{command_elements}')
    #print(f'================-{descriptions}\n\n')
    for i in range(len(command_elements)):
        elem = command_elements[i]

        '''
        c_type = classify_type(elem)
        n_type = ''
        if i > 0 and i+3 < len(command_elements):
            n_elem = command_elements[i+1]
            n_type = classify_type(n_elem)
            
        ### concat 'continuos containers'  
        if c_type == 'enum' and n_type == 'enum':
            command_elements[i+1] = '{}_{}'.format(elem, n_elem)
            continue
        '''

        if '_' in elem and elem.replace('_', '').islower():
            result = elem.split('_')
            desc = descriptions[i-len(result)+1:i+1]
            desc_n = descriptions[i-len(result)+1:]

        else:
            elem_list = [part for part in re.split(r'[ |]', elem.replace('<|', '<').replace('|>', '>')) if part]
            count = len(elem_list)

            desc = descriptions[i+count_pre:i+count_pre+count]
            desc_n = descriptions[i+count_pre:]
            count_pre += count-1

        change_cmd_flag = False
        '''
        if elem == '<(1-99)|standard WORD>':
            elem = 'standard <(1-99)|WORD>'
            desc_n[0], desc_n[1] = desc_n[1], desc_n[0]
            change_cmd_flag = True
        if elem == '<(100-500)|expanded WORD>':
            elem = 'expanded <(100-500)|WORD>'
            desc_n[0], desc_n[1] = desc_n[1], desc_n[0]
            change_cmd_flag = True
        '''
        '''
        if elem == '<A.B.C.D/M|A.B.C.D A.B.C.D>':
            elem = 'A.B.C.D/M'
            desc_n.pop(1)
            desc_n.pop(1)
        '''
        '''
        if elem == '<view|vrf>':
            elem = 'view'
            desc_n = [desc_n[0]]
        if elem == '<NAME|all>':
            elem = 'all'
            desc_n = [desc_n[1]]
        '''
        
        #if elem == 'WORD' and command_elements[i-1] == 'ip':
        #    print(descriptions)
        #    check_here()
        #if '<' in elem and '>' in elem and '|' not in elem:
        #    elem = elem.replace('<', '').replace('>', '')
        
        if elem == '<AA:BB:CC>':
            elem = 'AA:BB:CC' 
            
        if elem == '<VRFNAME>':
            elem = 'VRFNAME'
            
        if elem == '<A.B.C.D>':
            elem = 'A.B.C.D'
            
        if elem == '<(1-10000)>':
            elem = '(1-10000)'
        if elem == '<(1-4094)>':
            elem = '(1-4094)'
        if elem == '<(1-65535)>':
            elem = '(1-65535)'
            
        if elem == '<A.B.C.D|X:X::X:X|>':
            elem = '<A.B.C.D|X:X::X:X>'
            
        if elem == '<A.B.C.D/M|X:X::X:X/M|>':
            elem = '<A.B.C.D/M|X:X::X:X/M>'
            
        if elem == '<(0-7)>':
            elem = '(0-7)'
            
        if elem == '<blackhole>':
            elem = 'blackhole'
            
        if elem == '<NAME>':
            elem = 'NAME'
            
        if elem == '<rt|route-target>':
            elem = 'route-target'
            desc_n = [desc_n[0]]
        if elem == '<route-target6|rt6>':
            elem = 'route-target6'
            desc_n = [desc_n[0]]
        if elem == '<rt|route-target|route-target6|rt6>':
            elem = 'route-target6'
            desc_n = [desc_n[0]]
        if elem == '<rt|route-target6|rt6>':
            elem = 'route-target6'
            desc_n = [desc_n[0]]
            
        '''
        if elem == '<rt|route-target>':
            elem = 'route-target'
            desc_n = [desc_n[0]]
        if elem == '<route-target6|rt6>':
            elem = 'route-target6'
            desc_n = [desc_n[0]]
        '''

        if elem == '<X:X:X:X:X:X|X:X:X:X:X:X/M>':
            elem = 'X:X:X:X:X:X'
            desc_n = [desc_n[0]]
        if elem == '<0-255>':
            elem = '(0-255)'
        if elem == '<1-32>':
            elem = '(1-32)'
        if elem == '<1-65535>':
            elem = '(1-65535)'
        if elem == '5-1800':
            elem = '(5-1800)'
        if elem == '0-255':
            elem = '(0-255)'
        if elem == 'CMD_RANGE_STR':
            elem = '(1-256)'
        '''
        if elem == 'view' and command_elements[i+1] == 'WORD':
            break
        if elem == 'password' and command_elements[i+1] == '<(8-8)|>':
            command_elements[i+1] = '(8-8)'
        '''

        if '<<' in elem or '>>' in elem or elem.count('<') >= 2 or '|>' in elem or '{' in elem or ' ' in elem or change_cmd_flag:
            h = len([part for part in re.split(r'[{ <|>}]', elem) if part])

            if '<<' in elem or '>>' in elem:
                tokens = split_complex_choice(elem)
            else:
                tokens = parse_prototype(elem)
            j = 0
            LOG.info('tokens: {}'.format(tokens))

            for token in tokens:

                # LOG.info('case token: {}'.format(split_cli_preserving_brackets(token) + command_elements[i+1:]))
                # LOG.info('case desc_n: {}'.format(desc_n))
                k = len([part for part in re.split(
                    r'[ {<|>}]', token) if part])
                desc = desc_n[j: j+k] + desc_n[h:]
                # LOG.info('case desc: {}, lentoken {}'.format(desc, len(token)))
                j += k
                # if len(token) > 0:
                generate_cmd_tree(cmd_tree, split_cli_preserving_brackets(
                    token) + command_elements[i+1:], desc)
            if change_cmd_flag:
                break

            #if '|>' in elem:
            #    count_pre -= 1

            continue

        command_array.append(elem)
        

        key_in_cases = []
        indent = 0
        nk = None

            

            
        if '<' in elem and '|' in elem and '>' in elem:
            ks = elem.replace('<', '').replace('>', '').split('|')
        else:
            ks = [elem]
            
        count = len(ks)
            
        for k, v in cmd_tree.items():
            ###
            #if elem == 'X:X::X:X/M' and '<A.B.C.D|A.B.C.D/M|X:X::X:X|X:X::X:X/M>' in cmd_tree:
            #    print(len(cmd_tree))
            #    stop_here() 
            if '<' in k and '|' in k and '>' in k:
                kk = k.replace('<', '').replace('>', '').split('|')
            else:
                kk = [k]
                    
            if len(kk) == len(ks):
                continue

            print(f'000xxxxxxx-{kk}')
            if set(kk).issubset(set(ks)):

                for k in kk:

                    indent = ks.index(k)
                    ks.remove(k)
                    if len(ks) > 1:
                        elem = f'<{"|".join(ks)}>'
                    elif len(ks) == 1:
                        elem = ks[0]
                    
                    del desc[indent]
                    
                desc_ = v['desc']
                if len(kk) > 1:
                    kk = f'<{"|".join(kk)}>'
                elif len(kk) == 1:
                    kk = kk[0]
                    desc_ = [v['desc'][0]]
                key_in_cases = [elem, [kk], desc_]
                #generate_cmd_tree(cmd_tree, [k] + command_elements[i+1:], v['desc'] + desc_n)   
                continue
                
            if set(ks).issubset(set(kk)):
                for s in ks:
                    indent = kk.index(s)
                    kk.remove(s)
                    if len(kk) > 1:
                        nk = f'<{"|".join(kk)}>'
                    elif len(kk) == 1:
                        nk = kk[0]
                    key_in_cases = [k, nk]
                    del cmd_tree[k]['desc'][indent]
                continue
                

        if len(key_in_cases) == 3:
            
            print(f'111xxxxxxx-{key_in_cases[1]}')
            print(f'111xxxxxxx-{key_in_cases[2]}')
            #print(f'xxxxxxx-{desc_n}')
            #print(f'xxxxxxx-{desc_n[count:]}')
            print(f'xxxxxxxxx-{command_elements[i+1:]}')
            generate_cmd_tree(cmd_tree, key_in_cases[1] + command_elements[i+1:], key_in_cases[2] + desc_n[count:]) 
                
        if len(key_in_cases) == 2:
 
            k = key_in_cases[0]
            nk = key_in_cases[1]
            cmd_tree[nk] = cmd_tree[k].copy()
            del cmd_tree[k]
                    
        if elem not in cmd_tree:
            # LOG.info('cmd_tree: {}'.format(cmd_tree))
            cmd_tree[elem] = {}
            cmd_tree[elem]['desc'] = desc
            if elem == '<cr>' and desc[0] != 'end_cmd' and 'change_node' not in desc[0]:
                print(command_elements)
                print(descriptions)
                stop_here()
        else: 
            if elem == '<cr>' and 'change_node' in desc[0] and 'change_node' not in cmd_tree[elem]['desc'][0]:
                #print(desc[0])
                #print(cmd_tree[elem]['desc'])
                #stop_here()
                cmd_tree[elem]['desc'] = [desc[0]]
                
            
        cmd_tree = cmd_tree[elem]
    return command_array


def cmd_tree_concat(cmd_tree):
    for k in list(cmd_tree.keys()):
        v = cmd_tree[k]
        if '_NODE' in k:
            cmd_tree_concat(v)
            continue
        if k == '<cr>' or k == 'desc':
            continue
        list_kn = []
        if classify_type(k) == 'enum' and type(v) == dict and len(v) >= 2:
            for kn in list(v.keys()):
                vn = v[kn]

                flag = False
                if kn == '<cr>' or kn == 'desc' or classify_type(kn) != 'enum':
                    continue
                if len(vn) == 2:
                    if '<cr>' in vn:
                        continue
                    for key in list(vn.keys()):
                        if key == '<cr>' or key == 'desc':
                            continue
                        if classify_type(key) != 'enum':
                            flag = True
                            break
                if flag == True:
                    continue

                cmd_tree[f'{k}_{kn}'] = cmd_tree[k][kn].copy()
                cmd_tree[f'{k}_{kn}']['desc'] = cmd_tree[k]['desc'] + \
                    cmd_tree[f'{k}_{kn}']['desc']
                list_kn.append(kn)

            for kn in list_kn:
                del cmd_tree[k][kn]

            if len(list_kn) > 0:
                if (len(cmd_tree[k]) == 2 and '<cr>' in cmd_tree[k]) or len(cmd_tree[k]) == 1:
                    del cmd_tree[k]
                cmd_tree_concat(cmd_tree)
                break
        if len(list_kn) == 0:
            cmd_tree_concat(v)

MODULES = []

def generate_command_tree(cmd_list, module='CONFIG'):

    cmd_template_list = []
    for cmd_dict in cmd_list:
        if "node" not in cmd_dict:
            LOG.info('NOOOOO node: {}'.format(cmd_dict['command_string']))
            stop_here()
            continue
    LOG.info('generate_command_tree: {}'.format(len(cmd_list)))
    for cmd_dict in cmd_list:

        if 'node' not in cmd_dict:
            print(cmd_dict['command_string'])
            stop_here()
            continue
            
        if cmd_dict['node'] == 'ENABLE_NODE':
            cmd_dict['node'] = 'VIEW_NODE'
            
        default_cmd_list = ['config_list_cmd', 'find_cmd', 'vtysh_output_file_cmd', 'no_vtysh_output_file_cmd']
        cmd_name = cmd_dict['command_name']
            
        if module != cmd_dict['node'] and cmd_name not in default_cmd_list:
            continue
        else:
            cmd_dict['node'] = module
            
        if not cmd_dict['command_string']:
            stop_here()
            continue
            
        if '$' in cmd_dict['command_string']:
            cmd_dict['command_string'] = re.sub(r'\$\w+', '', cmd_dict['command_string'])
            #continue

        #if cmd_dict['command_type'] == 'NEXT_NODE_CLI' and cmd_dict['command_string'] == 'router ospf6 [vrf NAME]':
        #    cmd_dict['next_node'] = 'OSPF6_NODE'
            
        #if cmd_dict['command_type'] == 'NEXT_NODE_CLI' and cmd_dict['node'] not in BASE_NODE_LIST:
            #print(cmd_dict['command_string'])
            #print(cmd_dict['node'])
            #stop_here()
            #continue
            
        if cmd_dict['command_type'] == 'REMOVED_COMMAND':
            cmd_dict['command_string'] = "XXXXXX " + cmd_dict['command_string'] 
            continue
            
        #if cmd_dict['command_string'] == 'nexthop-group NHGNAME':
        #    print(cmd_dict)
        #    stop_here()
        #if cmd_dict['command_type'] == 'NEXT_NODE_CLI':
        #    if 'next_node' not in cmd_dict:
        #        print(cmd_dict)
        #        stop_here()

        first_ele = cmd_dict['command_string'].split()[0]

        command_string_org = cmd_dict['command_string']
            
        command_string_org = command_string_org.replace(
            'address-family <l2vpn evpn>', 'address-family <l2vpn|evpn>')
            
        descriptions_org = cmd_dict["descriptions"]

        fs = [part for part in re.split(r'[<|>]', first_ele) if part]
        for i in range(len(fs)):
            if len(fs) == 1:
                command_string = command_string_org
                descriptions = descriptions_org.copy()
            else:
                command_string = command_string_org.replace(first_ele, fs[i])
                descriptions = descriptions_org.copy()
                del descriptions[i]

            # LOG.info('module {} {}'.format(module, cmd_dict['node']))



            # modify []
            # EX: BGP_NODE neighbor WORD interface [peer-group WORD]
            # so [peer-group WORD] will be changed to <peer-group WORD|>

            command_string = command_string.replace(
                '[', '<').replace(']', '|>')
                
            command_elements = split_cli_preserving_brackets(command_string)

            #    continue

            if 'SUBGlobal' in command_string:
                LOG.info('check error command: {}'.format(command_string))
                stop_here()
            # if 'ipv6 address X:X::X:X/M' in command_string :
            #    LOG.info('check error command: {}'.format(command_string))
            #    stop_here()
            if 'Redistribute' in command_string:
                LOG.info('check error command: {}'.format(command_string))
                stop_here()
                
            if '+rtt' in command_string:
                continue

            if '<no|> <rt|route-target|route-target6|rt6>' in command_string:
                LOG.info('check error command: {}'.format(command_string))
                LOG.info('check error command: {}'.format(descriptions))
                #stop_here()
                #continue
                

            if len(descriptions) < len(command_elements):
                LOG.info('check error command: {}'.format(
                    cmd_dict['command_string']))
                stop_here()
                
            #if '(1-16777215) mac WORD <json|>' in command_string:
            #    print(command_string)
            #    print(descriptions)
            #    stop_here()
            
            
            LOG.info('command_string {} {}'.format(
                cmd_dict['node'], command_string))

            cmd_tree = CMD_TREE

            # add end
            command_elements.append('<cr>')
            if 'next_node' in cmd_dict:
                descriptions.append(f"change_node {cmd_dict['next_node']}")
            else:
                descriptions.append('end_cmd')

            '''
            if command_elements[0] == '<no|>':
                command_elements[0] = 'no'
                # add NODE
                more_command_elements = command_elements[1:]
                more_command_elements.insert(0, cmd_dict['node'])
                more_descriptions = descriptions[1:]
                more_descriptions.insert(0, '{} node related command'.format(cmd_dict['node']))
                generate_cmd_tree(cmd_tree, more_command_elements, more_descriptions)
                cmd_tree = CMD_TREE
            '''

            # add NODE
            command_elements.insert(0, cmd_dict['node'])
            descriptions.insert(
                0, '{} node related command'.format(cmd_dict['node']))

            generate_cmd_tree(cmd_tree, command_elements, descriptions)
            print('111111')
            # save cmd teamplate
            
            # command_elements = command_elements[1:-1]
        command_strings = split_cli_preserving_brackets(command_string_org)
        command_strings.insert(0, cmd_dict['node'])
        current_node = cmd_dict['node']
        while True:
            if current_node in NEXT_NODE_CMD_DICT and current_node not in BASE_NODE_LIST:
                cmd_str = NEXT_NODE_CMD_DICT[current_node]['cmd_str']
                command_strings.insert(0, cmd_str[0])
                current_node = NEXT_NODE_CMD_DICT[current_node]['org_node']
                command_strings.insert(0, current_node)
            else:
                break
        if ' '.join(command_strings) not in cmd_template_list:
            cmd_template_list.append(' '.join(command_strings))

    # concat continuous parent in tree
    cmd_tree_concat(CMD_TREE)
    if len(cmd_template_list) > 0:
        try:
            with open('./tree/{}.tree'.format(module), "w") as command_tree_file:
                command_tree_file.write(json.dumps(cmd_tree, indent=4))
        except Exception as e:
            LOG.error(e)

        try:
            MODULES.append(module)
            with open('./template/{}.template'.format(module), "w") as cmd_template_file:
                cmd_template_file.write(
                    "\n".join(list(dict.fromkeys(cmd_template_list))) + "\n")
            
        except Exception as e:
            LOG.error(e)


def classify_type(key, value=None):

    first = key[0]
    two = key[:2]
    check = 'CONT'

    tmp_key = key.replace('.', '').replace('/', '')

    if tmp_key.isupper():
        check = "STRING"

    if 'LNH_OPTIONS' in key:
        check = "STRING"

    if '_NODE' in key:
        check = "CONT"

    if key == 'NAME':
        check = "STRING"

    if key == 'ALIAS_NAME':
        check = "STRING"

    if key == 'BMPTARGETS':
        check = "STRING"

    # if key == 'json':
    #    check = "STRING"

    if key == 'ISIS_MT_NAMES':
        check = "STRING"

    if key == 'A.B.C.D' or key == '[A.B.C.D]':
        check = "IPV4"

    if key == 'A.B.C.D/M':
        check = "IPV4-PREFIX"

    if key == 'X:X::X:X':
        check = "IPV6"

    if key == 'X:X::X:X/M':
        check = "IPV6-PREFIX"

    if key == 'IFNAME':
        check = "IFNAME"

    if key == 'CMD_RANGE_STR':
        check = "STRING"

    if key == 'KEY' or key == 'AUTH_KEY':
        check = "KEY"
        
    if key == 'ASN:NN_OR_IP-ADDRESS:NN':
        check = "STRING"
        
        
    if first == '(':
        check = "NUM"
    elif first == '<':
        check = "CASES"
    elif first == '{':
        check = "CASES"
    elif first == '[':
        check = "CASES"

    elif first == '*':
        check = "STRING"

    if value and len(value) == 2 and check == 'CONT':

        for k, v in value.items():
            if k != 'desc' and k != '<cr>':
                check_next = classify_type(k)
                # LOG.info('check_next: {} - {} {}'.format(value, check_next, len(value)))
                if (check_next != 'CONT' and check_next != 'enum') or k == 'inbound':
                    check_next = 'LEAF'
                    check = 'LEAF'
                    break

        if 'desc' in value and '<cr>' in value:
            check = 'LEAF'

    # if '_' in key and ':' not in key and 'AUTH_KEY' not in key:
    #    check = 'CONT'

    if not value and check == 'CONT':
        check = 'enum'

    if check == 'CONT' and 'community-list' in key and 'show' not in key:
        check = 'LIST'

    if value and len(value) == 1 and check == 'CASES':
        check = 'CHOICE-CASE'

    return check


def make_type(value, indent=0):
    y_type = 'string'
    type_str = ''

    if value and len(value) > 0:
        check = 'string'
        for k, v in value.items():
            if k != 'desc' and k != '<cr>':
                k = k.replace('[', '').replace(']', '')
                check = classify_type(k)
            else:
                continue

            indentation = " " * (indent * 4)  # Use 4 spaces for indentation
            if check == 'IPV4':
                type_str += f"{indentation}type inet:ipv4-address;\n"

            if check == 'IPV4-PREFIX':
                type_str += f"{indentation}type inet:ipv4-prefix;\n"

            if check == 'IPV6':
                type_str += f"{indentation}type inet:ipv6-address;\n"

            if check == 'IPV6-PREFIX':
                type_str += f"{indentation}type inet:ipv6-prefix;\n"

            if check == 'STRING':
                type_str += f"{indentation}type string;\n"

            if check == 'IFNAME':
                type_str += f"{indentation}type string;\n"

            if check == 'KEY':
                type_str += f"{indentation}type string;\n"

            if check == 'NUM':
                type_str += f"{indentation}type int32;\n"

            if check == 'enum':
                type_str += f"{indentation}type enumeration {{\n"
                type_str += f"{indentation}    enum {k};\n"
                type_str += f"{indentation}}}\n"

            if check == 'CASES':
                LOG.info('k: {}'.format(k))
                cases = [part for part in re.split(r'[{<|>}]', k) if part]
                # LOG.info('cases: {}'.format(cases))

                add_indent = ''
                union_type = False
                for case in cases:
                    if classify_type(case) != 'enum':
                        union_type = True
                if len(cases) > 1 and union_type:
                    add_indent = " "*4
                    indent += 1
                    type_str += f"{indentation}type union {{\n"

                enum_cases = []
                for case in cases:
                    if classify_type(case) == 'enum':
                        enum_cases.append(case)
                    else:
                        more_cases = case.split()
                        for more_case in more_cases:
                            n_value = {more_case: v}
                            type_str += make_type(n_value, indent)

                if len(enum_cases) > 0:
                    type_str += f"{indentation+add_indent}type enumeration {{\n"

                    for enum in enum_cases:
                        n_value = {enum: v}
                        type_str += f"{indentation}    enum {enum};\n"
                        # type_str += make_type(n_value, indent+1)

                    type_str += f"{indentation+add_indent}}}\n"

                if len(cases) > 1 and union_type:
                    type_str += f"{indentation}}}\n"

    return type_str


def clean_leaf(leaf):
    leaf = leaf.replace('.', '-').replace(':', '-').replace('/', '_').replace('(', '').replace(')',
                                                                                               '').replace('|', '-or-').replace(' ', '_').replace('<', '').replace('>', '').replace('---', '').replace('*', 'all')
    if leaf[0].isdigit():
        leaf = 'n' + leaf
    return leaf


KEY_MAP = {}
N_KEY_MAP = {}
container_indent = {}
app_group = 'frr'
CONT_EXT = {}
CLICK_MAP = {}
APP_FRR = ''

BASE_NODE_LIST = ['VIEW_NODE', 'ENABLE_NODE', 'CONFIG_NODE']

###
# parent mean prvious container
# apps means current container split with '_' that joins multi container
###


def add_app_click(parent_list, key, value, main_node, sub_node, click_type='group'):
    global APP_FRR
    print(f'=====xxxx-{key}')
    key_bak = key

    pp = []
    LOG.info('===case parent_list: {}'.format(parent_list))
    if key == 'VIEW_NODE' or key == 'ENABLE_NODE':
        return parent_list

    parent_tmp_list = []
    # find next node group/command

    if key not in BASE_NODE_LIST and key in NEXT_NODE_CMD_DICT:
        parent_list = NEXT_NODE_CMD_DICT[key]['cmd_str'].copy()
        print(parent_list)
        # remove command in list
        parent_list.pop(0)

        if len(parent_list) > 0 and 'frr_' in parent_list[0]:
            return parent_list
        else:
            LOG.error('NEXT_NODE_CMD_DICT: {}'.format(NEXT_NODE_CMD_DICT[key]))
            check_error_here()

    print(f'=====xxxx-{parent_list}')
    print(f'=====xxxx-{key}')

    parent = parent_list[0]
    if parent not in BASE_NODE_LIST and parent in NEXT_NODE_CMD_DICT:
        parent_list = NEXT_NODE_CMD_DICT[parent]['cmd_str'].copy()
        # remove command in list
        parent_list.pop(0)
        # return parent_list

    for parent in parent_list:

        if '_NODE' in parent:
            if parent == 'VIEW_NODE':
                parent = 'frr'
            if parent in BASE_NODE_LIST:
                parent = parent.replace('_NODE', '').replace('_', '-').lower()

        if 'frr' not in parent:
            parent = 'frr_' + parent

        b_parent = parent
        app_key = key

        print(f'yyyy{b_parent}-{key}')
        if key.endswith('_NODE'):
            if key != 'CONFIG_NODE':
                continue
            app_key = key.replace('_NODE', '').replace('_', '-').lower()
            apps = [app_key]
        else:
            apps = app_key.split('_')

        if len(value['desc']) == 0:
            value['desc'] = [key]

        # LOG.info('case parent: {}'.format(parent))
        # LOG.info('case apps: {}'.format(apps))

        for i in range(len(apps)):
            # if apps[i] == parent.split('_')[-1]:
            #    continue

            # LOG.info('case CLICK_MAP: {}'.format(CLICK_MAP))
            
            b_parent += '_{}'.format(apps[i])

            if b_parent in CLICK_MAP:
                # LOG.info('case CLICK_MAP: {}'.format(CLICK_MAP[b_parent]))
                parent = b_parent
                continue

            if value['desc'] and len(value['desc']) > i:
                desc = value['desc'][i]
            else:
                desc = ''


            parent += '_{}'.format(apps[i])

            if parent not in CLICK_MAP:
                LOG.info('case parent: {}'.format(parent))
                CLICK_MAP[parent] = {}
                # 'group' is default 'frr_group' is new for frr_vtysh
                CLICK_MAP[parent]['type'] = click_type

                # add on 05082025
                pre_parent = parent.rsplit('_', 1)[0]
                if pre_parent in CLICK_MAP:
                    CLICK_MAP[parent]['length'] = CLICK_MAP[pre_parent]['length'] + 1
                elif pre_parent == 'frr':
                    CLICK_MAP[parent]['length'] = 1
                else:
                    check_error_here()
                    
                ###

                CLICK_MAP[parent]['desc'] = desc
                CLICK_MAP[parent]['main_node'] = main_node
                CLICK_MAP[parent]['sub_node'] = sub_node

                if '<cr>' not in value:
                    CLICK_MAP[parent]['type'] = 'group'
                    if click_type == 'frr_group':
                        CLICK_MAP[parent]['type'] = 'frr_group_non'
                if len(value) >= 2 and '<cr>' in value:
                    CLICK_MAP[parent]['type'] = 'without_command'
                    if click_type == 'frr_group':
                        CLICK_MAP[parent]['type'] = 'frr_group'
                if len(value) == 2 and '<cr>' in value and value['<cr>']['desc'] == 'end_cmd':
                    CLICK_MAP[parent]['type'] = 'command'
                    if click_type == 'frr_group':
                        CLICK_MAP[parent]['type'] = 'frr_group'


                for k, v in CLICK_MAP.items():
                    if k in parent and CLICK_MAP[k]['type'] == 'command':
                        CLICK_MAP[k]['type'] = 'without_command'

        pp.append(b_parent)

    return pp


def add_click_detail(key, value, app_group, leaf_name, main_node, sub_node, list_key=[], prefix=False):

    if prefix and classify_type(key) != 'enum':
        add_prefix = '-'.join(leaf_name.split('_'))
        app_group = add_app_click(
            app_group, add_prefix.lower(), value, main_node, sub_node, click_type='frr_group')

            
    LOG.info('key: {}, classify_type(key): {}'.format(key, classify_type(key)))
    LOG.info('leaf_name: {}, classify_type(leaf_name): {}'.format(
        leaf_name, classify_type(leaf_name)))

    if classify_type(leaf_name) == 'enum':
        app_group = add_app_click(app_group, leaf_name, value, main_node, sub_node)
        if key in leaf_name:
            key = leaf_name
        # LOG.info('leaf_name: {}, app_group: {}'.format(leaf_name, app_group))
    elif classify_type(key) == 'enum':
        app_group = add_app_click(app_group, key, value, main_node, sub_node)
        


    #if key == 'NHGNAME' and 'frr_config_nexthop-group' in app_group:
    #    print(value)
    #    print(app_group)
    #    stop_here()
        
    for parent in app_group:
        if parent not in CLICK_MAP:
            #check_error_here()
            pass
        else:

            if 'arg_list' not in CLICK_MAP[parent]:
                CLICK_MAP[parent]['arg_list'] = []
                
            arg_data = {}
            arg_data['arg_name'] = leaf_name.lower()
            arg_data['DB_STORE'] = leaf_name
            #if leaf_name == '1':
            #    stop_here()
            arg_data['arg_var'] = key
            arg_data['arg_desc'] = value['desc']

            exist = False
            for arg_list in CLICK_MAP[parent]['arg_list']:
                if arg_list['arg_name'] == arg_data['arg_name'] and arg_list['DB_STORE'] == arg_data['DB_STORE']:
                    exist = True
                    break
            if not exist:
                CLICK_MAP[parent]['arg_list'].append(arg_data)

                    #return app_group
            else:
                continue

            print(f'AAAAAAAAA {key}||{parent}')
            print(f"AAAAAAAAA {CLICK_MAP[parent]['length']}")
            


            arg_list_length = len(CLICK_MAP[parent]['arg_list'])
            #if arg_list_length > 1 and prefix==False:
            #    CLICK_MAP[parent]['length'] += (arg_list_length)

            LOG.info('append arg data: {}'.format(arg_data))

            if '<cr>' in value and len(value['<cr>']['desc']) == 0:
                LOG.info('1111111')
                value['<cr>']['desc'] = ['end_cmd']

            type_bak = CLICK_MAP[parent]['type']
            if '<cr>' in value and value['<cr>']['desc'][0] == 'end_cmd':
                LOG.info('222222')
                CLICK_MAP[parent]['type'] = 'without_command'
            if '<cr>' in value and len(value) == 2 and value['<cr>']['desc'][0] == 'end_cmd':
                LOG.info('3333333')
                CLICK_MAP[parent]['type'] = 'command'
            if '<cr>' in value and 'change_node' in value['<cr>']['desc'][0]:
                LOG.info('4444444')
                CLICK_MAP[parent]['type'] = 'without_command'
                NEXT_NODE = value['<cr>']['desc'][0].split()[1]
                LOG.info('===NEXT_NODE: {}'.format(NEXT_NODE))
                
                if NEXT_NODE in NEXT_NODE_CMD_DICT and 'list_keys' not in CLICK_MAP:
                    NEXT_NODE_CMD_DICT[NEXT_NODE]['cmd_str'].append(parent)
                    if 'keys' in NEXT_NODE_CMD_DICT[NEXT_NODE]:
                        CLICK_MAP[parent]['list_keys'] = NEXT_NODE_CMD_DICT[NEXT_NODE]['keys']

                else:
                    check_error_here()
            LOG.info('parent: {}, type: {}'.format(
                parent, CLICK_MAP[parent]['type']))

            if 'frr_group' in type_bak:
                LOG.info('55555555')
                if CLICK_MAP[parent]['type'] == 'group':
                    CLICK_MAP[parent]['type'] = 'frr_group_non'

                elif CLICK_MAP[parent]['type'] == 'command':
                    CLICK_MAP[parent]['type'] = 'frr_group'
                else:
                    CLICK_MAP[parent]['type'] = type_bak
            if CLICK_MAP[parent]['type'] == 'frr_group_non' and '<cr>' in value:
                LOG.info('6666666')
                CLICK_MAP[parent]['type'] = 'frr_group'
                
            if 'BGP_NODE' in key:
                LOG.info(f'xxxx-{key}')
                LOG.info(f'xxxx-{arg_data}')
                #LOG.info(f'xxxx-{CLICK_MAP[parent]['type']}")
                #stop_here()

    return app_group
    
def BYTE_ARRAY(line):
    return bytearray(line, "utf-8")

def app_module_build():
    global CLICK_MAP

    # FRR app.module init
    app_frr = bytearray()
    app_frr_map = {}

    CLICK_MAP = dict(sorted(CLICK_MAP.items()))
    for k, v in CLICK_MAP.items():
        apps = k.split('_')
        app_group = '_'.join(apps[:len(apps)-1])
        func_name = None
        
        '''
        if len(apps) > 6 and 'frr_config_router_bgp_as-number' in k:
            config_router_bgp_asnumber = '_'.join(apps[2:6])
            if config_router_bgp_asnumber not in app_frr_map:
                app_frr_map[config_router_bgp_asnumber] = BYTE_ARRAY(FRR_MODULE)
            app_frr = app_frr_map[config_router_bgp_asnumber]
            
        elif len(apps) == 5 and 'frr_config_router_bgp' in k:
            if 'frr_config_router_bgp' not in app_frr_map:
                app_frr_map['frr_config_router_bgp'] = BYTE_ARRAY(INIT_FRR)
            app_frr = app_frr_map['frr_config_router_bgp']
        '''

        if len(apps) > 4 and 'frr_config_router' in k:
            config_router = '_'.join(apps[2:4])
            if config_router not in app_frr_map:
                app_frr_map[config_router] = BYTE_ARRAY(FRR_MODULE)
            app_frr = app_frr_map[config_router]
            
        elif len(apps) > 3 and 'frr_show' in k:
            show = '_'.join(apps[1:3])
            if show not in app_frr_map:
                app_frr_map[show] = BYTE_ARRAY(FRR_MODULE)
            app_frr = app_frr_map[show]
            
        elif len(apps) > 2:
            module = '_'.join(apps[1:2])
            if module not in app_frr_map:
                app_frr_map[module] = BYTE_ARRAY(FRR_MODULE)
            app_frr = app_frr_map[module]

        elif len(apps) < 3:
            if 'frr' not in app_frr_map:
                app_frr_map['frr'] = BYTE_ARRAY(INIT_FRR)
            app_frr = app_frr_map['frr']
                
            
        LOG.info('BUILD apps: {}'.format(apps))
        #print(apps[-1])
        #time.sleep(1)
        #LOG.info('BUILD v: {}'.format(v))
        # add group/command

        # these case will special
        #if apps[-1] == 'large-community-list':
        #    v['type'] = 'group'
        #    if 'arg_list' in v:
        #        del v['arg_list']
        
        if apps[-1] == 'show':
            v['type'] = 'group'

        if v['type'] == 'command':
            app_frr.extend(BYTE_ARRAY(add_group(app_group, apps[-1], v['desc'])))
            app_frr[:] = app_frr.replace(
                b'{invoke_without_command}', b' invoke_without_command=True')
            app_frr.extend(BYTE_ARRAY(add_cr('{}_{}'.format(app_group, apps[-1]))))

        elif v['type'] == 'without_command':
            app_frr.extend(BYTE_ARRAY(add_group(app_group, apps[-1], v['desc'])))
            app_frr[:] = app_frr.replace(
                b'{invoke_without_command}', b' invoke_without_command=True')
            app_frr.extend(BYTE_ARRAY(add_cr('{}_{}'.format(app_group, apps[-1]))))

        elif v['type'] == 'group':
            app_frr.extend(BYTE_ARRAY(add_group(app_group, apps[-1], v['desc'])))
            app_frr[:] = app_frr.replace(b'{invoke_without_command}', b'')
            if apps[-1] == 'config':
                app_frr[:] = app_frr.replace(b'{argument_extend_db}', b'')

        elif v['type'] == 'frr_group' and len(v['arg_list']) > 0:
            app_frr.extend(BYTE_ARRAY(add_frr_group(
                app_group, apps[-1], CLICK_MAP[app_group]['length']+1, v['arg_list'][0]['arg_var'], v['desc'])))
            app_frr[:] = app_frr.replace(
                b'{invoke_without_command}', b' invoke_without_command=True')
            app_frr.extend(BYTE_ARRAY( add_cr('{}_{}'.format(app_group, apps[-1]))))

        elif v['type'] == 'frr_group_non' and len(v['arg_list']) > 0:
            if app_group == 'frr_config_bgp_extcommunity-list_expanded-num':
                print(CLICK_MAP[app_group]['length'])

            app_frr.extend(BYTE_ARRAY(add_frr_group(
                app_group, apps[-1], CLICK_MAP[app_group]['length']+1, v['arg_list'][0]['arg_var'], str(CLICK_MAP[app_group]['length']))))
            app_frr[:] = app_frr.replace(b'{invoke_without_command}', b'')

        # add argument
        if 'arg_list' not in v and v['type'] == 'without_command':
            app_frr[:] = app_frr.replace(b'{args}', b'')
            app_frr[:] = app_frr.replace(b'\n{argument_extend}', b'')

        elif 'arg_list' not in v:
            app_frr[:] = app_frr.replace(b'{argument_extend_db}', b'')
            app_frr[:] = app_frr.replace(b'{args}', b'')
            app_frr[:] = app_frr.replace(b'\n{argument_extend}', b'')
            continue

        func_name = f'{app_group}_{apps[-1]}'

        keys_list = {}
        if 'list_keys' in v:
            keys_list = v['list_keys']
        if v['main_node'] not in BASE_NODE_LIST:
            keys_list['PREFIX'] = 'WORD'

        arg_list = []
        leaf_list = []
        arguments = []


        if 'arg_list' in v:
            #LOG.info('BUILD arg_list000: {}'.format(v['arg_list']))
            if 'frr_group' in v['type'] and len(v['arg_list']) > 0:
                # v['arg_list'].pop(0)
                if len(v['arg_list']) == 1:
                    app_frr[:] = app_frr.replace(b'{argument_extend}\n', b'')
                if k == 'frr_config_bgp_large-community-list_standard-num':
                    print(v['length'])
                    print(v['type'])
                    #stop_here()
                
            for arg in v['arg_list']:
                arg_name = arg['arg_name']
                leaf_name = arg['DB_STORE']
                arg_var = arg['arg_var']
                if '_NODE' in arg_var:
                    continue
                

                # these case will special
                if arg_name == 'from':
                    arg_name = 'FROM'
                if arg_name == 'for':
                    arg_name = 'FOR'
                '''
                if arg_name == 'from':
                    arg_name = 'FROM'
                if app_group == 'frr_config_bgp_large-community-list':
                    if arg_name == 'expanded' and arg_var != 'WORD':
                        arg_var = '<(100-500)|WORD>'
                    if arg_name == 'standard' and arg_var != 'WORD':
                        arg_var = '<(1-99)|WORD>'
                '''
                
                if leaf_name in leaf_list:
                    continue
                if len(v['arg_list']) == 1 and arg_var.isdigit():
                    arg_list.append(f"{arg_name}='{arg_var}'")
                    app_frr[:] = app_frr.replace(b'{argument_extend}\n', b'')
                elif len(v['arg_list']) == 1 and classify_type(arg_var) == 'enum':
                    arg_list.append(f"{arg_var.replace('-', '')}_='{arg_var}'")
                    app_frr[:] = app_frr.replace(b'{argument_extend}\n', b'')
                elif arg_var == leaf_name and classify_type(leaf_name) == 'enum':
                    arg_list.append(f"{arg_var.replace('-', '')}_='{arg_var}'")
                    if arg_var == 'BGP_NODE':
                        stop_here()
                else:
                    arg_list.append(arg_name.replace('-', ''))
                    arguments.append(add_argument(arg_name, arg_var))

                leaf_list.append(leaf_name)
                LOG.info(f"xxxx{v['arg_list']}")
                LOG.info('BUILD leaf_list: {}'.format(leaf_list))
                LOG.info('BUILD arguments: {}'.format(arguments))
                
        if len(arguments) > 0 and app_group != 'frr':
            CLICK_MAP[k]['length'] += len(arguments)
            
        if 'frr_group' in v['type'] and len(v['arg_list']) > 0:
            arguments.pop(0)
            #if k == 'frr_config_bgp_large-community-list':
            #    stop_here()

            
        app_frr[:] = app_frr.replace(b'{argument_extend}', '\n'.join(arguments).encode("utf-8"))
        # LOG.info('BUILD argument: {}'.format(arguments))

        # check_here()
        # add extend DB
        main_node = v['main_node']
        sub_node = v['sub_node']
        #LOG.info('BUILD arg_list: {}'.format(arg_list))
        #LOG.info('BUILD leaf_list: {}'.format(leaf_list))

        arg_tmp = None
        leaf_tmp = None
        del_list = []
        for i in range(len(arg_list)):
            #print(i)
            #print(arg_list)
            if '=' in arg_list[i]:
                if not arg_tmp:
                    arg_tmp = arg_list[i]
                    leaf_tmp = leaf_list[i]
                elif len(arg_list[i]) > len(arg_tmp):
                    #arg_list.remove(arg_list[i])
                    #leaf_list.remove(leaf_list[i])
                    #break
                    del_list.append([arg_list[i], leaf_list[i]])
                elif len(arg_list[i]) < len(arg_tmp):
                    #arg_list.remove(arg_tmp)
                    #leaf_list.remove(leaf_tmp)
                    #break
                    del_list.append([arg_tmp, leaf_tmp])

        for tmp in del_list:
            if tmp[0] in arg_list:
                arg_list.remove(tmp[0])
            if tmp[1] in leaf_list:
                leaf_list.remove(tmp[1])

        extend_db = add_extend_db(
            main_node, sub_node, arg_list, leaf_list, keys_list, func_name, v['type'])

        # if v['type'] != 'group':
        #    extend_db += "\n    show_state_db('vtysh')"
        app_frr[:] = app_frr.replace(b'{argument_extend_db}', extend_db.encode("utf-8"))

        # swap default argument to end

        if len(arg_list) > 1 and '=' in arg_list[0]:
            arg_list[-1], arg_list[0] = arg_list[0], arg_list[-1]

        if 'frr_group' in v['type'] and len(v['arg_list']) > 0:
            arg_list.pop(0)
        pass_args = ', '.join(arg_list)
        pass_args = pass_args

        app_frr[:] = app_frr.replace(b'{args}', pass_args.encode("utf-8"))
        

    for k , val in app_frr_map.items():
        if k == 'frr':
            val.extend(BYTE_ARRAY(DYNAMIC_IMPORT))
            with open(f'main.py', "w") as frr_app_main:
                frr_app_main.write(val.decode("utf-8"))
        else:
            k = k.replace("-", "")
            path = f'modules/{k}.py'
            if 'router_' in k:
                path = f'modules/config_router/{k}.py'
            if 'show_' in k:
                path = f'modules/main_show/{k}.py'
            with open(path, "w") as frr_app_module:
                frr_app_module.write(val.decode("utf-8"))


def get_keys(indent, value, parent=None):

    keys = {}
    for n_key, n_value in value.items():
        if n_key == 'desc' or n_key == '<cr>':
            continue

        if classify_type(n_key) == 'CASES':
            leaf_name = find_leaf_name_from_desc(f'CHOICE_CASE', n_key)
            keys[leaf_name] = n_key
            #if n_key == '<deny|permit>':
            #    print(keys)
            #    stop_here()

        else:
            if classify_type(n_key) == 'enum':
                keys[n_key] = n_key
                continue
            leaf_name = find_leaf_name_from_desc(n_value['desc'][0], n_key)
            # LOG.critical('key: {}'.format(key))
            keys[leaf_name] = n_key

    # keys = [k for k, v in keys.items() if k]
    return keys


def cmdtree_to_yang(data, indent=0, parent=None, main_node='', sub_node=''):
    global container_indent  # , app_group

    global APP_FRR
    """
    Converts a dictionary into a YANG module structure.

    Args:
        data (dict): The dictionary to convert.
        indent (int): The current indentation level.

    Returns:
        str: A string representing the YANG module.
    """
    LOG.info(
        '\n==============================================================================\n')

    yang_str = ""
    frr_str = ""
    app_group = parent.copy()

    indentation = " " * (indent * 4)  # Use 4 spaces for indentation

    # need container on indent == 3
    if indent == 3 and '<import|export>' in data:
        bak_value = data['<import|export>']
        del data['<import|export>']
        data['import'] = bak_value
        data['export'] = bak_value

    # need container on indent == 3
    if indent == 3 and '<ip|ipv6>' in data:
        bak_value = data['<ip|ipv6>']
        del data['<ip|ipv6>']
        data['ip'] = bak_value
        data['ipv6'] = bak_value
    LOG.info('app_group: {}'.format(parent))
    for key, value in (data.items()):
        LOG.info('key: {}-{}-{}'.format(key, indent, len(data)))
            

        if key == 'desc' or key == '<cr>':
            continue

        # get description
        desc_list = value['desc']

        # LOG.info('key: {}, desc_list: {}'.format(key, desc_list))
        yang_type = classify_type(key, value)
        # LOG.info('yang_type: {}'.format(yang_type))

        if indent == 2:
            main_node = key
        if indent == 3:
            sub_node = key
            #if 'show_bgp' in key:
            #    continue
            #if key == 'no_isis_fast-reroute_ti-lfa_level-1_node-protection':
            #    stop_here()
        # all indent 3 must be container
        if indent == 3 and yang_type != 'CONT' and yang_type != 'LIST':
            yang_type = 'CONT'

        # all indent 4 must be leaf or leaf-list
        if indent >= 4 and yang_type == 'CONT':
            yang_type = 'LEAF'

        # add more prefix case
        add_more_prefix = False
        if indent >= 4 and len(data) > 2:
            LOG.info(f'XXXXXXX-{len(data)}')
            branch_count = 0
            for k in list(data.keys()):
                #LOG.info(f'kkkkk-{k}')
                if k != 'desc':
                    branch_count += 1
            if branch_count > 1:
                add_more_prefix = True

        # LOG.info('type: {}'.format(yang_type))
        cont_ext = False

        if '_NODE' in key:
            parent = ['frr']

        LOG.info('parent: {}'.format(parent))
        LOG.info('key: {}, desc_list: {}'.format(key, desc_list))
        LOG.info('add_more_prefix: {}, len(data): {}'.format(
            add_more_prefix, len(data)))
        LOG.info('============')

        next_node_dict_p = {}
        if yang_type == 'CONT' or yang_type == 'LIST':

            # app.module add_group
            # LOG.info('case add main group: {} {}'.format(key, parent))
            LOG.info('app_group: {}'.format(parent))
            app_group = add_click_detail(key, value, parent, key, main_node, sub_node)
            #parent = app_group.copy()
            LOG.info('app_group: {}'.format(app_group))

            parent = [main_node]

            # check change node cmd and set it to LIST
            for k, v in NEXT_NODE_CMD_DICT.items():
                if key.replace('_', ' ') in v['cmd_str'][0] and v['org_node'] == parent[0]:
                    yang_type = 'LIST_NODE_NEXT'
                    next_node_dict_p = NEXT_NODE_CMD_DICT[k]
                    next_node_dict_p['keys'] = {}

            if '_NODE' in parent[0] and '_NODE' not in key and parent[0] not in BASE_NODE_LIST:
                yang_type = 'LIST_NODE'

        else:
            pass

        if f'{main_node}_{sub_node}' not in KEY_MAP:
            KEY_MAP[f'{main_node}_{sub_node}'] = []

        exist_leaf = KEY_MAP[f'{main_node}_{sub_node}']

        keys = {}

        if yang_type == 'CONT':
            # print container
            yang_str += f"{indentation}container {key} {{\n"
            yang_str += cmdtree_to_yang(value, indent + 1, app_group, main_node, sub_node)
            yang_str += f"{indentation}}}\n"

        elif 'LIST' in yang_type:
            #if key == '<rt|route-target|route-target6|rt6>':
            #    continue
            # print KEY
            if yang_type == 'LIST' or yang_type == 'LIST_NODE_NEXT' and '<cr>' not in value:
                keys = get_keys(indent, value, key)

            if yang_type != 'LIST':
                keys['PREFIX'] = 'WORD'

            if len(next_node_dict_p) > 0:
                next_node_dict_p['keys'] = keys

            ks = [k for k, v in keys.items() if k]
            # if key == 'ipv6':
            #    print(json.dumps(value, indent=4))
            #    stop_here()

            if len(keys) > 0:
                yang_str += f"{indentation}list {key.upper()} {{\n"
                yang_str += f"{indentation}    key \"{' '.join(ks)}\";\n"

                if yang_type != 'LIST':
                    yang_str += f"{indentation}    leaf PREFIX {{\n"
                    yang_str += f"{indentation}        type string; \n"
                    yang_str += f"{indentation}    }} \n"
            else:
                yang_str += f"{indentation}container {key} {{\n"

            yang_str += cmdtree_to_yang(value, indent + 1, app_group, main_node, sub_node)

            yang_str += f"{indentation}}}\n"

        elif 'CASES' in yang_type or 'CHOICE' in yang_type:

            leaf_name = find_leaf_name_from_desc(f'CHOICE_CASE', key)
            if len(data) == 2 and '<cr>' not in data:
                leaf_name = '{}_{}'.format(parent[0].split('_')[-1].upper(), leaf_name)
                
            elif parent[0].split('_')[-1] == 'vn':
                leaf_name = f'VN_{leaf_name}'
            elif parent[0].split('_')[-1] == 'un':
                leaf_name = f'UN_{leaf_name}'
            elif parent[0].split('_')[-1] == 'prefix' and leaf_name in exist_leaf:
                leaf_name = f'SECOND_{leaf_name}'
            print(f'leafname-{leaf_name}')
            app_group = add_click_detail(
                key, value, parent, leaf_name, main_node, sub_node, prefix=True)

            global CASE_DICT
            if 'CHOICE_CASE' in leaf_name and key not in CASE_DICT:
                CASE_DICT[key] = value["desc"]
                with open('casessssss', "a") as xxxxx:
                    xxxxx.write(f'{key}\n{value["desc"]}\n')

            if leaf_name in exist_leaf:
                yang_str += cmdtree_to_yang(value, indent, app_group, main_node, sub_node)
                continue

            exist_leaf.append(leaf_name)
            n_value = {key: value}

            yang_str += f"{indentation}leaf {leaf_name} {{\n"
            yang_str += make_type(n_value, indent + 1)
            yang_str += f"{indentation}}}                  //{key} {value['desc']}\n"

            LOG.info('app_group: {}-{}'.format(key, app_group))

            yang_str += cmdtree_to_yang(value, indent, app_group, main_node, sub_node)

        elif yang_type == 'LEAF':
                
            LOG.info('yang_type: {},  LEAF key: {} parent: {} add_more_prefix: {}'.format(
                yang_type, key, parent, add_more_prefix))

            if classify_type(key) == 'enum':
                if f'{main_node}_{sub_node}_{indent}' not in N_KEY_MAP:
                    N_KEY_MAP[f'{main_node}_{sub_node}_{indent}'] = []
                    
                n_exist_leaf = N_KEY_MAP[f'{main_node}_{sub_node}_{indent}']
                # APP.MODULE
                
                for n_key, n_value in value.items():

                    if '<cr>' in value:
                        # APP.MODULE
                        if key.isnumeric():
                            leaf_name = find_leaf_name_from_desc(desc_list[0], key)
                        else:
                            leaf_name = key
                            
                        app_group = add_click_detail(
                            key, value, parent, leaf_name, main_node, sub_node, prefix=add_more_prefix)
                        if leaf_name not in exist_leaf:
                            yang_str += f"{indentation}leaf {leaf_name} {{\n"
                            yang_str += f"{indentation}    type enumeration {{\n"
                            yang_str += f"{indentation}        enum {key};\n"
                            yang_str += f"{indentation}    }}\n"
                            yang_str += f"{indentation}}}                  //{key}\n"

                            exist_leaf.append(leaf_name)
                            
                        if leaf_name not in n_exist_leaf:
                            n_exist_leaf.append(leaf_name)

                    if n_key != 'desc' and n_key != '<cr>':
                        if classify_type(n_key) == 'enum':

                            leaf_name = f'{key}_{n_key}'

                            # APP.MODULE

                            app_group = add_click_detail(
                                n_key, n_value, parent, leaf_name, main_node, sub_node, prefix=add_more_prefix)

                            if leaf_name in exist_leaf:
                                LOG.info('app_group: {}'.format(app_group))
                                yang_str += cmdtree_to_yang(n_value, indent, app_group, main_node, sub_node)
                                continue
                            else:
                                exist_leaf.append(leaf_name)
                                n_exist_leaf.append(leaf_name)
                                yang_str += f"{indentation}leaf {leaf_name} {{\n"
                                yang_str += f"{indentation}    type enumeration {{\n"
                                yang_str += f"{indentation}        enum {leaf_name};\n"
                                yang_str += f"{indentation}    }}\n"
                                yang_str += f"{indentation}}}                  //{n_key}\n"

                        else:
                            #nn_value = {n_key: n_value}
                            #if key in exist_leaf:
                                #if n_key == 'X:X:X:X:X:X':
                                #if 'frr_show_ip_ospf_instance-id_neighbor' in app_group and n_key == 'A.B.C.D':
                                #    print(app_group)
                                #    stop_here()
                                #app_group = add_click_detail(
                                #    key, value, parent, key, main_node, sub_node, prefix=add_more_prefix)
                                #LOG.info('app_group: {}'.format(app_group))
                                #yang_str += cmdtree_to_yang(
                                #    nn_value, indent, app_group, main_node, sub_node)
                                #continue
                            #exist_leaf.append(key)

                            '''
                            if len(value) == 2:
                                yang_str += f"{indentation}leaf {key} {{\n"
                                yang_str += f"{indentation}    type boolean; \n"
                                yang_str += f"{indentation}}}                  //{key}\n"  
                                
                                ### APP.MODULE
                                leaf_name = find_leaf_name_from_desc(n_value['desc'][0], n_key)
                                app_group = add_click_detail(n_key, n_value, parent, key, prefix=add_more_prefix)
                                if leaf_name in exist_leaf:
                                    LOG.info('app_group: {}'.format(app_group))
                                    continue
                                exist_leaf.append(leaf_name)
                                yang_str += f"{indentation}leaf {leaf_name} {{\n"
                                yang_str += make_type(nn_value, indent + 1)
                                yang_str += f"{indentation}}}                  //{n_key}\n"
                                
                                yang_str += cmdtree_to_yang(nn_value, indent, parent)
                                continue
                            else:
                            '''
                            if len(value) > 1:
                                # APP.MODULE
                                # LOG.info('n_key: {}, '.format(n_key))
                                leaf_name = key
                                #if leaf_name in n_exist_leaf and leaf_name == 'host':
                                #    leaf_name = 'Host'
                                app_group = add_click_detail(
                                    key, value, parent, leaf_name, main_node, sub_node, prefix=add_more_prefix)
                                if key not in n_exist_leaf:
                                    yang_str += f"{indentation}leaf {key} {{\n"
                                    yang_str += f"{indentation}    type enumeration {{\n"
                                    yang_str += f"{indentation}        enum {key};\n"
                                    yang_str += f"{indentation}    }}\n"
                                    yang_str += f"{indentation}}}                  //{key}\n"

                                    n_exist_leaf.append(leaf_name)
                                    
                                LOG.info('app_group: {}'.format(app_group))
                                yang_str += cmdtree_to_yang(value,
                                                            indent, app_group, main_node, sub_node)

                                break



                        # LOG.info('n_value: {}'.format(n_value))
                        LOG.info('app_group: {}'.format(app_group))
                        yang_str += cmdtree_to_yang(n_value, indent, app_group, main_node, sub_node)

            else:
                check_this_case()

        else:

            LOG.info('yang_type: {},  LEAF key: {}, parent: {}, add_more_prefix: {}'.format(
                yang_type, key, parent, add_more_prefix))
            LOG.info('description: {}'.format(desc_list))
            if key == '(0-60000)':
                leaf_name = find_leaf_name_from_desc(desc_list[0], key, parent)
            else:
                leaf_name = find_leaf_name_from_desc(desc_list[0], key)

            #LOG.info('xxxxkey: {}, exist_leaf: {}'.format(
            #    leaf_name, exist_leaf))
            # if key == 'ALIAS_NAME':
            #    print(yang_type)
            #    stop_here()
            # APP.MODULE
            LOG.info('parent: {}'.format(parent))
            LOG.info('app_group: {}'.format(app_group))
            
            if leaf_name == 'VNI_NUMBER':
                add_more_prefix = True
            if leaf_name == 'CONFIGURATION_FILE_TO_READ':
                add_more_prefix = True
            if leaf_name == 'OSPF_ADMINISTRATIVE_DISTANCE':
                add_more_prefix = True
                
            if leaf_name == 'MPLS-TE_EDGE_ID' and key == 'A.B.C.D':
                leaf_name = 'MPLS-TE_EDGE_ID_V4'
            if leaf_name == 'MPLS-TE_EDGE_ID' and key == 'X:X::X:X':
                leaf_name = 'MPLS-TE_EDGE_ID_V6'
                add_more_prefix = True

            if leaf_name == 'MPLS-TE_SUBNET_ID' and key == 'A.B.C.D/M':
                leaf_name = 'MPLS-TE_SUBNET_ID_V4'
            if leaf_name == 'MPLS-TE_SUBNET_ID' and key == 'X:X::X:X/M':
                leaf_name = 'MPLS-TE_SUBNET_ID_V6'
                add_more_prefix = True
                
            #if leaf_name == 'SOURCE_ADDRESS_TO_MATCH' and 'frr_config_access-list_rule-action_ip_host' in parent:
            #    stop_here()
            #if leaf_name == 'DESTINATION_ADDRESS_TO_MATCH' and 'frr_config_access-list_rule-action_ip_host' in parent:
            #    stop_here()
                

            #if key == 'MSG...':
            #    stop_here()
            if key[-3:] == '...':
                parent = add_click_detail(
                    key, value, parent, f'FROM_{leaf_name}', main_node, sub_node, prefix=True)

                app_group = add_click_detail(
                    key, value, parent, f'TO_{leaf_name}', main_node, sub_node, prefix=False) 
                #leaf_name = 'XXXXXXXXXXXX'
                #if key == 'MSG...':
                #    print(parent)
                #    print(leaf_name)
                #    stop_here()
            else:
                app_group = add_click_detail(
                    key, value, parent, leaf_name, main_node, sub_node, prefix=add_more_prefix)
                    
            LOG.info('app_group: {}'.format(app_group))
            
            #if leaf_name == 'A_PATH_THAT_HAS':
            #    stop_here()
            
            if leaf_name in exist_leaf:
                LOG.info('app_group: {}'.format(app_group))
                yang_str += cmdtree_to_yang(value, indent, app_group, main_node, sub_node)
                continue
            exist_leaf.append(leaf_name)

            if key[-3:] == '...':
                if key == 'MSG...':
                    yang_str += f"{indentation}leaf-list {leaf_name} {{\n"
                else:
                    yang_str += f"{indentation}leaf-list {leaf_name} {{\n"
            else:
                yang_str += f"{indentation}leaf {leaf_name} {{\n"

            n_value = {key: value}
            yang_str += make_type(n_value, indent + 1)
            yang_str += f"{indentation}}}                  //{key}\n"
            
            LOG.info('app_group: {}'.format(app_group))
            yang_str += cmdtree_to_yang(value, indent, app_group, main_node, sub_node)

    return yang_str


def find_leaf_name_from_desc(desc_list, key, parent=None):

    if type(parent) == list:
        # if len(parent) > 1:
        #    there_is_error_need_to_check()
        parent = parent[0]
        
    if 'e.g' in desc_list:
        desc_list = desc_list.split('e.g')[0].strip()
    desc_list = re.sub(r"\s*[\(\[\<].*?[\)\]\>]", "", desc_list)
    desc_list = desc_list.replace('.', '').replace(';', '').replace('|', '_')

    desc = [part for part in desc_list.split() if part]
    if len(desc) >= 3:
        if desc[0].isnumeric():
            desc = desc[1:]
        desc = desc[:4]
        if parent and classify_type(parent) == 'enum' and 'table_range' not in parent and 'password' not in parent and 'ipv6_route' not in parent and 'ip_route' not in parent and 'ospf-lsa' not in parent and 'border-routers' not in parent and 'database' not in parent:
            desc = parent.split('_')[-1:]
            
    if 'Hexadecimal' in desc:
        desc = ['Hexadecimal_value']
    if 'regular-expression' in desc:
        desc = ['REGULAR_EXPRESSION']


        
    key_desc_pairs = {
        '<1|ead>': ['EAD_TYPE'],
        '<2|macip>': ['MACIP_TYPE'],
        '<3|multicast>': ['MULTICAST_TYPE'],
        '<(100-500)|WORD>': ['EXPANDED_COMMUNITY_LIST_NUMBER'],
        '<(1-99)|WORD>': ['STANDARD_COMMUNITY_LIST_NUMBER'],
        '<reject|blackhole>': ['drop_action'],
        '<deny|permit>': ['rule_action'],
        '<INTERFACE|Null0>': ['ifname'],
        '<cisco|zebra>': ['platform'],
        '<errors|event|labels|zebra>': ['ldp_debug_category'],
        '<recv|sent>': ['communication_mode'],
        '<implicit-null|explicit-null>': ['mpls_label_mode'],
        '<version|defaults>': ['config_metadata'],
        '<kern|user|mail|daemon|auth|syslog|lpr|news|uucp|cron|local0|local1|local2|local3|local4|local5|local6|local7>': ['syslog_facility'],
        '<urib-only|mrib-only|mrib-then-urib|lower-distance|longer-prefix>': ['rib_lookup_mode'],
        '(1-99)': ['STANDARD_NUM'],
        '(100-500)': ['EXPANDED_NUM'],
        '<emergencies|alerts|critical|errors|warnings|notifications|informational|debugging>': ['MSG_TYPE'],
        '<zebra|ripd|ripngd|ospfd|ospf6d|ldpd|bgpd|isisd|fabricd|pimd|staticd>': ['routing_daemon'],
        '<zebra|ripd|ripngd|ospfd|ospf6d|bgpd|isisd|pbrd|fabricd|pimd|staticd>': ['routing_daemon'],
        '<zebra|bgpd|ripd|ripngd|ospfd|ospf6d|isisd|fabricd|nhrpd|ldpd|babeld|eigrpd|pimd|pim6d|pbrd|staticd|bfdd|vrrpd|pathd>': ['daemons_list'],
        '<babeld|bgpd|fabricd|ldpd|ospfd|pbrd|pimd|ripngd|vrrpd|bfdd|eigrpd|isisd|nhrpd|ospf6d|pathd|pim6d|ripd|staticd|zebra>': ['daemons_list'],
        '<any|babel|bgp|connected|eigrp|isis|kernel|nhrp|openfabric|ospf|rip|static|table|vnc>': ['FRR_IP_PROTOCOL'],
        '<any|babel|bgp|connected|isis|kernel|nhrp|openfabric|ospf6|ripng|static|table|vnc>': ['FRR_IP6_PROTOCOL'],
        '<babel|bgp|connected|eigrp|isis|kernel|nhrp|openfabric|ospf|rip|static|table|vnc>': ['FRR_IP_REDIST'],
        '<babel|bgp|connected|eigrp|isis|kernel|nhrp|openfabric|rip|static|table|vnc>': ['FRR_IP_REDIST'],
        '<babel|bgp|connected|isis|kernel|nhrp|openfabric|ospf6|ripng|static|table|vnc>': ['FRR_IP6_REDIST'],
        '<router|network|inter-prefix|inter-router|as-external|group-membership|type-7|link|intra-prefix>': ['lsa_record'],
        '<json|nexthop-group>': ['format'],
        '<memory|file>': ['storage_type'],
        '<nexthop|import>': ['WATCH_FOR_CHANGE'],
        '<ip|ipv6>': ['LABEL_FORWARD'],
        '<all|common|event|interface|kernel|route|vici>': ['log_category'],
        '<cache|shortcut>': ['route_cache_mode'],
        '<ipv4|ipv6|l2vpn>': ['Address_Family'],
        '<unicast|multicast|vpn|labeled-unicast|flowspec|evpn>': ['Address_Family_modifier_extend'],
        '<unicast|multicast|vpn>': ['Address_Family_modifier'],
        '<in|out>': ['In_out_bound'],
        '<internal|external>': ['BGP_PEER'],
        '<(1-4294967295)|internal|external>': ['BGP_PEER'],
        '<disable-connected-check|enforce-multihop>': ['EBGP peer using'],
        '<ipv4|ipv6>': ['Address Family'],
        '<asbr-summary|external|network|router|summary|nssa-external|opaque-link|opaque-area|opaque-as>': ['ospf_lsa_type'],
        '<max-age|self-originate>': ['lsa_status'],
        '<advertise-queue|advertised-routes|packet-queue>': ['routing_queue'],
        '<nht|import-check>': ['tracking_mode'],
        '<macip|multicast|es|prefix>': ['route_type'],
        '<fib|route>': ['ip_table_type'],
        '<vn|un>': ['overlay_address_mode'],
        '<all|holddown|imported|local|remote>': ['registration_filter'],
        '<active|removed>': ['query_status'],
        '<explicit-null|implicit-null>': ['mpls_label'],
        '<disable|head-end-replication>': ['bum_flooding_mode'],
        '<as-set|no-as-set>': ['as_set_mode'],
        '<both|import|export>': ['route_direction'],
        '<import|export>': ['filter_direction'],
        '<ospf|table>': ['route_source'],
        '<both|all|extended|standard|large>': ['community_type'],
        '<both|send|receive>': ['filter_capability'],
        '<area-password|domain-password>': ['authentication_scope'],
        '<ipv4-unicast|ipv4-mgmt|ipv6-unicast|ipv4-multicast|ipv6-multicast|ipv6-mgmt|ipv6-dstsrc>': ['ip_topology'],
        '<ipv4|ipv6>': ['redistribute_ip'],
        '<level-1|level-2>': ['isis_level'],
        '<narrow|transition|wide>': ['metric_style'],
        '<level-1|level-1-2|level-2-only>': ['isis_router_level'],
        '<clear|md5>': ['authentication_type'],
        '<send-only|validate>': ['pdu_mode'],
        '<broadcast|non-broadcast|point-to-multipoint|point-to-point>': ['ospf_network_type'],
        '<shortcut|redirect>': ['shortcut_redirect_mode'],
        '<md5|clear>': ['authentication_method'],
        '<high|medium|low>': ['router_preference'],
        '<null|message-digest>': ['ospf_authentication_type'],
        '<md5|hmac-sha-256>': ['crypto_algorithm'],
        '<cisco|ibm|shortcut|standard>': ['abr_type'],
        '<message-digest|null>': ['authentication_type'],
        '<enable|disable>': ['shortcut_state'],
        '<translate-candidate|translate-never|translate-always>': ['nssa_translate_mode'],
        '<default|enable|disable>': ['shortcut_mode'],
        '<rt|route-target|route-target6|rt6>': ['route_target_list'],
        '<exist-map|non-exist-map>': ['Advertise_outes_only'],
        '<flap-statistics|dampened-routes|routes>': ['bgp_neighbor_route_stats'],
        '<bestpath|multipath>': ['bgp_path_selection'],
        '<multicast|labeled-unicast>': ['address_family_modifier'],
        '<view|vrf>': ['instance_view_vrf'],
        '<valid|invalid|notfound>': ['rpki_validation_state'],
        '<vpnv4|vpnv6>': ['address_family_type'],
        '<intra-area|inter-area|external-1|external-2>': ['route_type_filter'],
        '<intra-area|inter-area|external-1|external-2|detail|summary>': ['route_filter_detail_summary'],
        '<match|detail>': ['route_prefix_match_detail'],
        '<file|memory>': ['config_write_target'],
        '<common|kernel|filter|timeout|interface|route|all>': ['logging_message_type'],
        '<advertised-routes|received-routes|filtered-routes>': ['bgp_neighbor_route_direction'],
        '<candidate|running>': ['configuration_state'],
        '<json|xml>': ['output_format'],
        '<rfapi-query|import-bi-attach|import-del-remote|verbose>': ['rfapi_debug_options'],
        '<leak-from-vrf|leak-to-vrf|rmap-event|label>': ['vrf_leak_event_label'],
        '<hello|dd|ls-request|ls-update|ls-ack|all>': ['ospf_packet_type'],
        '<generate|flooding|install|refresh|aggregate>': ['lsa_operation_type'],
        '<status|events|timers>': ['nsm_status_event_timer'],
        '<interface|redistribute>': ['zebra_interface_redistribute'],
        '<unknown|hello|dbdesc|lsreq|lsupdate|lsack|all>': ['ospf_debug_packet_type'],
        '<send|recv|send-hdr|recv-hdr>': ['debug_packet_direction'],
        '<siaquery|siareply|ack|hello|probe|query|reply|request|retry|stub|terse|update|all>': ['eigrp_packet_type'],
        '<send|recv|all>': ['eigrp_packet_event'],
        '<on|off>': ['response_filter_toggle'],
        '<A.B.C.D|A.B.C.D/M|X:X::X:X|X:X::X:X/M>': ['Network'],
        '<router|network|inter-prefix|inter-router|as-external|nssa|link|intra-prefix|unknown>': ['lsa_types'],
        '<originate|examine|flooding>': ['lsa_actions'],
    }

    key_desc_pairs['__special_cases__'] = {
        '(0-255)':  ['cost_value'],
        'MSG': ['message'],
        'ASN:NN_OR_IP-ADDRESS': ['bgp_identifier'],
        'RT': ['router_target'],
        'AA:BB:CC': ['LARGE_COMMUNITY'],
        'LINE': ['LIST'],
        'AA:NN': ['COMMUNITY_NUMBER'],
        'A.B.C.D/M': ['IP_PREFIX'],
        'A.B.C.D|X:X::X:X': ['ip_address'],
        'A.B.C.D|X:X::X:X|dynamic': ['protocol_address'],
        'LNH_OPTIONS': ['local-next-hop'],
        'YY:YY:YY:YY:YY:YY': ['mac_address'],
        'kernel|connected|static': ['routing_protocol']
    }
    

    for k, v in key_desc_pairs['__special_cases__'].items():
        if k in key:
            desc = key_desc_pairs['__special_cases__'][k]
    if key in key_desc_pairs:
        desc = key_desc_pairs[key]

    return '_'.join(desc).upper().replace('/', '').replace('\'S', '').replace('(', '').replace(')', '').replace('[', '').replace(']', '').replace('@', '').replace('\'', '').replace('_E.G.', '').replace(' ', '_').replace(',', '').replace('>', '')


DYNAMIC_IMPORT = """
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
"""

FRR_MODULE = """import click
from frr.frr_types_extension import create_flexible_type as FRR_TYPE
from frr.frr_types_extension import *

"""


INIT_FRR = """import os
import json
import click
import time
import importlib
import inspect
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

def show_state_db(key):
    #twamp_table_keys = state_db.keys(state_db.STATE_DB, "FRR_VTYSH_RETURN|*")
    global CONFIG_DB
    save_config = None
    for i in range(10):
        time.sleep(0.05)
        if len(COMMON_DATA_MAP) < 2:
            continue
        for k , v in COMMON_DATA_MAP.items():
            if '|' in k:
                keys = k.split('|')
                if keys[0] in COMMON_DATA_MAP:
                    main_node = keys[0]
                    key_store = COMMON_DATA_MAP[keys[0]]
                    CONFIG_DB.set_entry(main_node, key_store, None)
                    time.sleep(0.005)
                    CONFIG_DB.set_entry(main_node, key_store, {})
                    time.sleep(0.005)
                    for a, b in COMMON_DATA_MAP[k].items():
                        CONFIG_DB.mod_entry(main_node, key_store, {a:b})
                        time.sleep(0.005)
                    if main_node == 'VIEW_NODE' and 'write' in key_store:
                        save_config = 'write_terminal'
                        
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
    \"\"\"frr-related configuration tasks\"\"\"
    global CONFIG_DB
    CONFIG_DB = ValidatedConfigDBConnector(db.cfgdb)
    show_state_th.start()
    pass
    
"""

EXTEND_DB = """#ctx = click.get_current_context()
    #config_db = ValidatedConfigDBConnector(db.cfgdb)
    
    {data_gen}
    
    if '{main_node}|{sub_node}' not in COMMON_DATA_MAP:
        COMMON_DATA_MAP['{main_node}|{sub_node}'] = {}

    for key, val in data_gen.items():
        if key.islower() and key in COMMON_DATA_MAP['{main_node}|{sub_node}']:
            key = key.upper()
        COMMON_DATA_MAP['{main_node}|{sub_node}'][key] = val
    {keys_gen}
"""

FRR_GROUP = """
@{parent_group}.group(cls=FRR_AbbreviationGroup, name=frr_group_choice({indent}, {args_var}),{invoke_without_command})
{argument_extend}
def {parent_group}_{group_name_clean}({args}):
    \"\"\"{group_desc}\"\"\"
    global COMMON_DATA_MAP
    {argument_extend_db}
    pass

"""

GROUP = """
@{parent_group}.group(cls=FRR_AbbreviationGroup, name='{group_name}',{invoke_without_command})
{argument_extend}
def {parent_group}_{group_name_clean}({args}):
    \"\"\"{group_desc}\"\"\"
    global COMMON_DATA_MAP
    {argument_extend_db}
    pass

"""

COMMAND = """
@{parent_group}.command('{command}')
{argument_extend}
def {parent_group}_{command_name_clean}({args}):
    \"\"\"{command_desc}\"\"\"
    global COMMON_DATA_MAP
    {argument_extend_db}
    COMMON_DATA_MAP = {}
    pass

"""

CR = """
@{parent_group}.command('./\t<cr>')
def {parent_group}_cr():
    pass

"""

ARGUMENT = """@click.argument('{leaf}', metavar='{leaf_name}', required={required}, type={leaf_type}{default})"""

OPTION = """@click.option(--'{leaf}', metavar='{leaf_name}', required={required}, type={leaf_type}{default}), help={leaf_desc}"""


FUNC_DEF = """
@clicommon.pass_db
def {func_name}(db{args}):
    \"\"\"{func_desc}\"\"\"
    
    {argument_extend_db}
    return
    
"""

def find_longest_common_substring(str1, str2):
    """Finds the longest common substring between two strings."""
    # Determine which string is shorter
    if len(str1) > len(str2):
        short_str, long_str = str2, str1
    else:
        short_str, long_str = str1, str2

    # Iterate from the longest possible substring down to the shortest
    for length in range(len(short_str), 0, -1):
        for i in range(len(short_str) - length + 1):
            substring = short_str[i:i + length]
            if substring in long_str:
                return substring
    return "" # No common substring found
    
def add_extend_db(main_node, sub_node, args_list, leaf_list, keys_list=None, func_name=None, atype='group'):
    if len(leaf_list) > 1 and classify_type(leaf_list[-1]) == 'enum':
        last_element = leaf_list.pop()
        leaf_list.insert(0, last_element)
        
        last_element = args_list.pop()
        args_list.insert(0, last_element)
        
    #if 'BGP_NODE' in leaf_list:
    #    stop_here()
        

        
    extend_db = EXTEND_DB
    sub_node = find_longest_common_substring(sub_node, func_name)
    
    extend_db = extend_db.replace('{main_node}', main_node)
    extend_db = extend_db.replace('{sub_node}', sub_node)

    key_store = []
    key_store_str = ''
    keys_gen = ''
    if keys_list and len(keys_list) > 0:
        keys_gen += f"\n    #######################"
        #keys_gen += f"\n    keys_list = {keys_list}"
        keys_gen += f"\n    key_store = []"
        keys_gen += f"\n    global PREFIX_TMP"
        keys_gen += f"\n    for k, v in COMMON_DATA_MAP['{main_node}|{sub_node}'].items():"
        #keys_gen += f"\n        if k in keys_list:"
        keys_gen += f"\n        if k.islower() and k != v:"
        keys_gen += f"\n            key_store.append(k)"
        keys_gen += f"\n        if k != v or '_NODE' not in v:"
        keys_gen += f"\n            key_store.append(v)"
        keys_gen += f"\n    key_store.insert(0, '{sub_node}')"
        keys_gen += f"\n    previous_key = key_store[:-1]"
        keys_gen += f"\n    if PREFIX_TMP and '{main_node}' not in BASE_NODE:"
        keys_gen += "\n        pre_key = PREFIX_TMP.split('|')[-1]"
        keys_gen += "\n        if key_store[0].startswith(pre_key):"
        keys_gen += "\n            if '|' not in PREFIX_TMP:"
        keys_gen += "\n                PREFIX_TMP = PREFIX_TMP.replace(f'{pre_key}', '')"
        keys_gen += "\n            else:"
        keys_gen += "\n                PREFIX_TMP = PREFIX_TMP.replace(f'|{pre_key}', '')"
        keys_gen += "\n        if PREFIX_TMP != '' and key_store[0] not in PREFIX_TMP:"
        keys_gen += "\n            key_store[0] = f'{PREFIX_TMP}|{key_store[0]}'"
        keys_gen += "\n            if len(previous_key) == 0:"
        keys_gen += "\n                previous_key = [PREFIX_TMP]"
        keys_gen += "\n            else:"
        keys_gen += "\n                previous_key[0] = f'{PREFIX_TMP}|{previous_key[0]}'"
        keys_gen += "\n        if PREFIX_TMP.endswith(f'|{key_store[0]}'):"
        keys_gen += "\n            key_store[0] = PREFIX_TMP"
        keys_gen += f"\n    "
        # keys_gen += f"\n    if len(previous_key) > 0:"
        # keys_gen += f"\n        config_db.set_entry('{main_node}', tuple(previous_key), None)"
        # keys_gen += f"\n    config_db.set_entry('{main_node}', tuple(key_store), COMMON_DATA_MAP['{main_node}|{sub_node}'])"
        keys_gen += f"\n    COMMON_DATA_MAP['{main_node}'] = tuple(key_store)"
        keys_gen += f"\n    PREFIX_TMP = '|'.join(key_store)\n"
    else:
        keys_gen += f"\n    # set {main_node} -> {sub_node} table"
        # keys_gen += f"\n    config_db.set_entry('{main_node}', '{sub_node}', COMMON_DATA_MAP['{main_node}|{sub_node}'])"
        keys_gen += f"\n    COMMON_DATA_MAP['{main_node}'] = '{sub_node}'"

    data_gen = "data_gen = {}"
    if func_name:
        data_gen += "\n    name = {}.name".format(func_name.replace('-', ''))
        #data_gen += "\n    data_gen[name] = name"
    for i in range(len(leaf_list)):
        if '=' in args_list[i]:
            sub = args_list[i].split('=')[1].replace("'", '')
            if sub == sub_node:
                continue
        if i == 0 and leaf_list[i].isupper() and func_name and 'frr' in atype:
            data_gen += "\n    data_gen['{}'] = FRR_CLI_ARGS[name]".format(
                leaf_list[i])
        else:
            data_gen += "\n    data_gen['{}'] = {}".format(
                leaf_list[i], args_list[i])
            # if '=' not in args_list[i]:
            #    data_gen += "\n    FRR_CLI_GROUP.append({})".format(args_list[i])
    # if func_name:
    #    keys_gen += f"\n    if {func_name}.invoke_without_command == True:"
    #    keys_gen += f"\n        config_db.set_entry('SONIC_FRR', 'SONIC_FRR_CLIS', {{'cli': FRR_CLI_GROUP}})"

    extend_db = extend_db.replace('{data_gen}', data_gen)
    extend_db = extend_db.replace('{keys_gen}\n', keys_gen)
    return extend_db


def add_group(parent_group, group_name, desc=''):
    group = GROUP
    if len(parent_group.split('_')) == 2:
        group = group.replace('@{parent_group}.', '@click.')
    if len(parent_group.split('_')) == 3 and 'frr_show_' in parent_group:
        group = group.replace('@{parent_group}.', '@click.')
    if len(parent_group.split('_')) == 4 and 'frr_config_router_' in parent_group:
        group = group.replace('@{parent_group}.', '@click.')

    group = group.replace('{parent_group}', parent_group.replace('-', ''))
    group = group.replace('{group_name}', group_name)
    group = group.replace('{group_name_clean}', group_name.replace('-', ''))
    group = group.replace('{group_desc}', desc)
        
    return group


def add_frr_group(parent_group, group_name, indent, args_var, desc=''):
    group = FRR_GROUP
    if len(parent_group.split('_')) == 2:
        group = group.replace('@{parent_group}.', '@click.')
    if len(parent_group.split('_')) == 3 and 'frr_show_' in parent_group:
        group = group.replace('@{parent_group}.', '@click.')
    if len(parent_group.split('_')) == 4 and 'frr_config_router_' in parent_group:
        group = group.replace('@{parent_group}.', '@click.')
        
    group = group.replace('{parent_group}', parent_group.replace('-', ''))
    group = group.replace('{indent}', str(indent))
    group = group.replace('{group_name_clean}', group_name.replace('-', ''))
    group = group.replace('{group_desc}', desc)
    
    args_var = args_var.replace('...', '')
        
    if 'CASES' in classify_type(args_var):
        CASES = [part for part in re.split(r'[<|>]', args_var) if (
            part and classify_type(part) != 'enum')]

        cases = [part for part in re.split(r'[<|>]', args_var) if (
            part and classify_type(part) == 'enum')]
        if len(cases) > 0 and len(CASES) == 0:
            group = group.replace('{args_var}', '{}'.format(cases))

        if len(CASES) > 0:
            type_args_var = []
            for c in CASES:
                if classify_type(c) == 'NUM':
                    type_args_var.append(c.replace('-', ', '))
                else:
                    type_args_var.append(f"'{c}'")

            for c in cases:
                type_args_var.append(f"'{c}'")

            make_type = f"[{', '.join(type_args_var)}]"
            group = group.replace('{args_var}', make_type)

    elif classify_type(args_var) == 'NUM':
        group = group.replace('{args_var}', '[{}]'.format(
            args_var.replace('-', ', ')))

    else:
        make_type = f"['{args_var}']"
        group = group.replace('{args_var}', make_type)

    return group


def add_command(parent_group, c, desc=''):
    command = COMMAND
    command = command.replace('{parent_group}', parent_group.replace('-', ''))
    command = command.replace('{command}', c)
    command = command.replace('{command_name_clean}', c.replace('-', ''))
    command = command.replace('{command_desc}', desc)
    
    if len(parent_group.split('_')) == 2:
        command = command.replace(f'@{parent_group}.', '@click.')
    if len(parent_group.split('_')) == 3 and 'frr_show_' in parent_group:
        group = group.replace(f'@{parent_group}.', '@click.')
    if len(parent_group.split('_')) == 4 and 'frr_config_router_' in parent_group:
        group = group.replace(f'@{parent_group}.', '@click.')
        
    return command


def add_cr(parent_group, desc=''):
    cr = CR
    cr = cr.replace('{parent_group}', parent_group.replace('-', ''))
    return cr


def add_argument(leaf, leaf_name, leaf_type='str', required='True'):
    leaf_name = leaf_name.replace('...', '')

    argument = ARGUMENT
    argument = argument.replace('{leaf}', leaf.replace('-', ''))
    argument = argument.replace('{leaf_name}', leaf_name)
    argument = argument.replace('{required}', required)
    # argument = argument.replace('{leaf_desc}', help)

    if leaf == leaf_name and classify_type(leaf) == 'enum':
        argument = argument.replace('{default}', ', default="{}"'.format(leaf))

    elif 'CASES' in classify_type(leaf_name):
        CASES = [part for part in re.split(r'[<|>]', leaf_name) if (
            part and classify_type(part) != 'enum')]

        cases = [part for part in re.split(r'[<|>]', leaf_name) if (
            part and classify_type(part) == 'enum')]
        if len(cases) > 0 and len(CASES) == 0:
            argument = argument.replace(
                '{leaf_type}', 'click.Choice({})'.format(cases))

        if len(CASES) > 0:
            type_args = []
            for c in CASES:
                if classify_type(c) == 'NUM':
                    type_args.append(c.replace('-', ', '))
                else:
                    type_args.append(f"'{c}'")

            if len(cases) > 0:
                enum_type = f"'ENUM({', '.join(cases)})'"
                type_args.append(enum_type)

            make_type = f"FRR_TYPE({', '.join(type_args)})"
            argument = argument.replace('{leaf_type}', make_type)

    elif classify_type(leaf_name) == 'NUM':
        argument = argument.replace(
            '{leaf_type}', 'FRR_TYPE({})'.format(leaf_name.replace('-', ', ')))

    else:
        make_type = f"FRR_TYPE('{leaf_name}')"
        argument = argument.replace('{leaf_type}', make_type)

    argument = argument.replace('{default}', '')
    argument = argument.replace('{leaf_type}', leaf_type)

    return argument


def add_func(func_name, args, func_desc, argument_extend_db=''):
    func_def = FUNC_DEF
    func_def = func_def.replace('{func_name}', func_name.replace('-', ''))
    func_def = func_def.replace('{args}', args)
    func_def = func_def.replace('{func_desc}', func_desc)
    func_def = func_def.replace('{argument_extend_db}', argument_extend_db)
    return func_def


def clean_cmd(cmd):
    cmd = cmd.replace('[', '').replace(']', '').replace(
        '{', '').replace('}', '').replace('|', ' ')
    return cmd


NEXT_NODE_CMD_DICT = {}


def find_list(cmd_str, NODE, NEXT_NODE):
    if NEXT_NODE not in NEXT_NODE_CMD_DICT and 'exit' not in cmd_str:
        NEXT_NODE_CMD_DICT[NEXT_NODE] = {}
        NEXT_NODE_CMD_DICT[NEXT_NODE]['org_node'] = NODE
        NEXT_NODE_CMD_DICT[NEXT_NODE]['cmd_str'] = [cmd_str]


if __name__ == "__main__":

    cmd_list = decmd_run()
    edges = nodes_graph()["edges"]
    # LOG.info('edges: {}'.format(edges))
    # stop_here()
    # finding next node command
    cmd_list = sorted(
        cmd_list, key=lambda x: x["command_string"], reverse=True)
    cmd_list = sorted(cmd_list, key=lambda x: len(x['node']))
    
    '''
    for cmd in cmd_list:
        if cmd['node'] == 'VIEW_NODE' or cmd['node'] == 'ENABLE_NODE':
            with open('./template/XXXXXXX.template', "a") as cmd_template_file:
                cmd_template_file.write(f'{cmd["command_string"]}\n')
    '''
    
    for i in range(len(cmd_list)):
        cmd = cmd_list[i]

        if cmd['command_type'] == 'NEXT_NODE_CLI':
            LOG.info('NEXT_NODE_CLI: {}'.format(
                clean_cmd(cmd['command_string'])))
            if 'next_node' in cmd:
                cmd_list[i]['command_type'] = 'NEXT_NODE_CLI_MATCH'
                find_list(cmd['command_string'], cmd['node'], cmd['next_node'])
                continue
            for edge in edges:
                if cmd['command_type'] == 'NEXT_NODE_CLI' and clean_cmd(cmd['command_string']) == clean_cmd(edge['nosh_command']):
                    cmd_list[i]['next_node'] = edge['next_nosh']
                    find_list(cmd['command_string'],
                              cmd['node'], edge['next_nosh'])
                    cmd_list[i]['command_type'] = 'NEXT_NODE_CLI_MATCH'
                    break
        # if 'router isis WORD [vrf NAME]' in cmd_list[i]['command_string']:
        #    print('{}'.format(cmd_list[i]['command_string']))
        #    print('{}'.format(cmd_list[i]['command_type']))
        #    print('{}'.format(NEXT_NODE_CMD_DICT))
        #    stop_here()

    LOG.info('NEXT_NODE_CMD_DICT: {}'.format(NEXT_NODE_CMD_DICT))
    #node_dict = {}
    #node_dict['CONFIG_NODE'] = {'BGP_NODE': {}}
    '''
    def make_node_dict(node_dict):
        if len(node_dict) > 0:
            for n in node_dict:
                node_dict_n = node_dict[n]
                for k, v in NEXT_NODE_CMD_DICT.items():
                    if v['org_node'] == n:
                        if k not in node_dict_n:
                            node_dict_n[k] = {}
                make_node_dict(node_dict_n)
    '''
    #make_node_dict(node_dict)
    #print(node_dict)
    #print('node_dict: {}'.format(json.dumps(node_dict, indent=4)))
            
    LIST_IMPORT = BASE_NODE_LIST.copy()
    for k, v in NEXT_NODE_CMD_DICT.items():
        if v['org_node'] in LIST_IMPORT:
            if k not in LIST_IMPORT:
                LIST_IMPORT.append(k)
            continue
        kk = v['org_node']
        while kk in NEXT_NODE_CMD_DICT:
            if NEXT_NODE_CMD_DICT[kk]['org_node'] in LIST_IMPORT:
                if kk not in LIST_IMPORT:
                    LIST_IMPORT.append(kk)
                break
            kk = NEXT_NODE_CMD_DICT[kk]['org_node']

    # add config node as default
    #LIST_IMPORT.insert(0, 'config')
    #LIST_IMPORT.insert(0, 'enable')
    #LIST_IMPORT.insert(0, 'view')
    #LIST_IMPORT.append('interface')
    #LIST_IMPORT.append('vrf')

    #LIST_IMPORT = ['config']
    #print(LIST_IMPORT)
    #LIST_IMPORT = ['CONFIG_NODE', 'BGP_NODE']
    #stop_here()
    #LIST_IMPORT = ['VIEW_NODE', 'ENABLE_NODE']
    global CMD_TREE
    for node in LIST_IMPORT:
        CMD_TREE = {}
        if node == '1DE':
            #stop_here()
            continue
        generate_command_tree(cmd_list, node.upper())
        print('CMD_TREE: {}'.format(json.dumps(CMD_TREE, indent=4)))


        yang_str = cmdtree_to_yang(CMD_TREE, 2, ['frr'])

        DATA_YANG = YANG_FILE.replace('{MODULE_NAME}', 'sonic-frr-{}'.format(node)).replace('{PREFIX}', 'frr-{}'.format(
            node)).replace('{CONTAINER_NAME}', 'sonic-frr-{}'.format(node)).replace('{YANG_GEN}', yang_str)
        # LOG.info(DATA_YANG)

        with open('./yang/sonic-frr-{}.yang'.format(node), "w") as yangfile:
            yangfile.write(DATA_YANG)

    # FRR app.module generate
    # print('CLICK_MAP: {}'.format(json.dumps(CLICK_MAP, indent=4)))
    app_module_build()
    #print(MODULES)
    #stop_here()

