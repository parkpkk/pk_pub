import re
import regex
from app_logging import LOG

def extract_defines(content):
    """
    Extract #define macros from a C file, including multi-line macros.
    """
    # Regular expression to match #define macros
    define_pattern = re.compile(
        r"#define\s+(\w+)\s+(\\\n(?:.*\\\n)*.*|.*)",  # Match #define with continuation \
        re.MULTILINE
    )

    defines = {}
    for match in define_pattern.finditer(content):
        macro_name = match.group(1)
        macro_body = match.group(2).replace("\\\n", "").strip()  # Replace line continuations
        if macro_name not in defines and 'FABRIC' not in macro_body and '->' not in macro_body:
            #if macro_name == 'DAEMONS_LIST':
            #    print(macro_body)
            #    stop_here()
            defines[macro_name] = macro_body
        
    for key, value in defines.items():
        # Replace macro names in values with their definitions, if they exist
        for macro, macro_value in defines.items():
            value = value.replace(macro, macro_value)
        defines[key] = value
        
    #for name, value in defines.items():
    #    LOG.info(f"{name} = {value}")

    return defines

def find_target_node(content):
    nodes = []
    for line in content.split('\n'):
        if re.search(r'vty->node\s*=', line):
            node = line.split('=')[1].strip().replace(';', '')
            if node.isupper():
                nodes.append(node)
    return nodes
    
def collapse_multiline_command(text: str) -> str:
    # Remove newlines and leading/trailing spaces
    text = re.sub(r'\s*\n\s*', ' ', text.strip())
    # Collapse multiple spaces to one
    text = re.sub(r'\s+', ' ', text)
    # Handle indent-aware collapsing of <...> blocks
    # Collapse the bracketed section by identifying the start and end
    pattern = r'\[<(.+?)>\]'
    match = re.search(pattern, text)
    if match:
        block = match.group(1)
        # Clean internal whitespace again
        block = re.sub(r'\s*\|\s*', '|', block)
        block = re.sub(r'\s+', ' ', block)
        return text[:match.start()] + f"[<{block}>]" + text[match.end():]
    return text

def parse_defun(content):

    # Regex patterns for parsing different parts of DEFUN, DEFUN_NOSH, DEFUN_HIDDEN, and DEFPY
    #defun_pattern = re.compile(r"(?:DEFUN|DEFUN_HIDDEN|DEFUN_YANG)\s*\(\s*([^\s,]+),\s*([^\s,]+),\s*(.*?),\s*(.*?)\)", re.DOTALL)
    defun_pattern = re.compile(r"(?:DEFUN|DEFUN_HIDDEN|DEFUN_YANG|ALIAS|DEFSH)\s*\(\s*([^\s,]+),\s*([^\s,]+),\s*(.*?),\s*(.*?)\)", re.DOTALL)
    
    defunsh_pattern = re.compile(
        r'DEFUNSH\s*\(\s*'            # Match DEFUNSH keyword
        r'(\w+)\s*,\s*'               # Capture multiple Command IDs (hex values separated by '|')
        r'([\w_]+)\s*,\s*'            # Capture Command Name
        r'([\w_]+)\s*,\s*'            # Capture Command Variable
        r'([\s\S]+?),\s*'             # Capture Command Template (handles multiline templates)
        r'([\s\S]+?)'                 # Capture Descriptions (multiline support)
        r'\)\s*\{'                    # Match closing bracket of DEFUNSH macro
    )

    defunnosh_pattern = re.compile(r"(?:DEFUN_NOSH|DEFUN_YANG_NOSH)\s*\(\s*([^\s,]+),\s*([^\s,]+),\s*(.*?),\s*(.*?)\)", re.DOTALL)
    
    defpynosh_pattern = re.compile(r"(?:DEFPY_NOSH|DEFPY_YANG_NOSH)\s*\(\s*([^\s,]+),\s*([^\s,]+),\s*(.*?),\s*(.*?)\)", re.DOTALL)
    
    defpy_pattern = re.compile(r"(?:DEFPY|DEFPY_YANG)\s*\(\s*([^\s,]+),\s*([^\s,]+),\s*(.*?),\s*(.*?)\)", re.DOTALL)

    # Try to match DEFUN or DEFUN_NOSH or DEFUN_HIDDEN

    cmd_type = 'CURRENT_NODE_CLI'
    cmd_string = None
    
    content = re.sub(r'\$[\w-]+', '', content) # remove $xxx

    defun_match = defun_pattern.search(content)

    if defun_match:
        func_name = defun_match.group(1).strip()
        cmd_name = defun_match.group(2).strip()
        cmd_string = defun_match.group(3).strip()
        #if 'mtrace ' in cmd_string:
        #    LOG.info('cmd_string: {}'.format(cmd_string))
        #    stop_here()


    # Try to match DEFPY
    defpynosh_match = defpynosh_pattern.search(content)
    if defpynosh_match:
        cmd_type = 'NEXT_NODE_CLI'
        func_name = defpynosh_match.group(1).strip()
        cmd_name = defpynosh_match.group(2).strip()
        cmd_string = defpynosh_match.group(3).strip()

    defpy_match = defpy_pattern.search(content)
    if defpy_match:
        func_name = defpy_match.group(1).strip()
        cmd_name = defpy_match.group(2).strip()
        cmd_string = defpy_match.group(3).strip()

    defunnosh_match = defunnosh_pattern.search(content)
    if defunnosh_match:
        cmd_type = 'NEXT_NODE_CLI'
        func_name = defunnosh_match.group(1).strip()
        cmd_name = defunnosh_match.group(2).strip()
        cmd_string = defunnosh_match.group(3).strip()

    defunsh_match = defunsh_pattern.search(content)
    description_lines = []
    if defunsh_match:
        cmd_type = 'NEXT_NODE_CLI'
        func_name = defunsh_match.group(2).strip()
        cmd_name = defunsh_match.group(3).strip()
        cmd_string = defunsh_match.group(4).strip()

        cmd_description = defunsh_match.group(5)
        description_lines = [desc.strip().strip('"') for desc in cmd_description.split("\n") if desc.strip()]
        
        #LOG.info('cmd_string: {}'.format(cmd_string))
        #LOG.info('description_lines: {}'.format(content))
        #if 'router eigrp ' in cmd_string:
        #    stop_here()
        
    if not cmd_string:
        return None

    # Parse descriptions (start after the command string and end at ')\n')
    description_start = content.find(f'{cmd_string}') + len(cmd_string)
    description_end = content.find(")\n{", description_start)
    description_section = content[description_start:description_end]

    # Extract valid description lines without ',' or ''

    if len(description_lines) == 0:
        cmd_string = cmd_string.replace("\n", "")
        cmd_string = ' '.join(cmd_string.split())
        #LOG.info('cmd_string: {}'.format(cmd_string))
        for line in description_section.splitlines():
            if not line.strip().startswith("//"):
                line = line.strip().strip('"').strip(',').replace("\t", "")
                line = ' '.join([part for part in line.split(' ') if part])
                #LOG.info('description_lines: {}'.format(line))
                if line:
                    #LOG.info('description_lines: {}'.format(line))
                    description_lines.append(line)
    if ')' in description_lines:
        for i in range(len(description_lines)):
            #print(i)
            #print(description_lines)
            if description_lines[i] == ')':
                description_lines = description_lines[:i]
                break
    if '#' in cmd_string:
        cmd_string = cmd_string.split('#')[0]

    #if defunsh_match:
    #    LOG.info('description_lines: {}'.format(description_lines))
    # Result
    
    

    cmd_string = cmd_string.replace('keep indent.py happy */', '')
    cmd_string = collapse_multiline_command(cmd_string)
    cmd_string = cmd_string.replace('{ ', '{')
    cmd_string = cmd_string.replace(' }', '}')
    cmd_string = cmd_string.replace('[ ', '[')
    cmd_string = cmd_string.replace(' ]', ']')
    cmd_string = cmd_string.replace(' |', '|')
    cmd_string = cmd_string.replace('| ', '|')
    cmd_string = cmd_string.replace('< ', '<')
    cmd_string = cmd_string.replace(' >', '>')
    cmd_string = cmd_string.replace(')(', ') (')
    cmd_string = re.sub(r'([A-Za-z])([({\[])', r'\1 \2', cmd_string)

    if cmd_string == 'cmdstr':
        return None
       
    next_node = find_target_node(content)
    
    parts = re.split(r'[<>\|\[\]\{\} ]+', cmd_string)
    parts = [p for p in parts if (p != '')]
    
    description_lines = description_lines[-len(parts):]
    if len(description_lines) == 0:
        description_lines = parts
    if len(description_lines) != len(parts):
        print(cmd_string)
        print(description_lines)
        if cmd_string == 'clear foo LINE...':
            return None
        stop_here()
        return None

    result = {
        "command_type": cmd_type,
        "function_name": func_name,
        "command_name": cmd_name,
        "command_string": cmd_string,
        "descriptions": description_lines,
    }
    
    if len(next_node) > 0 and cmd_type == 'NEXT_NODE_CLI':

        result["next_node"] = next_node[0]
    return result

def parse_all_defuns(content):
    #parse_define(content)
    defines = extract_defines(content)
    
    sorted_keys_desc = sorted(defines.keys(), key=len, reverse=True)


    if 'DEFUNSH(VTYSH' in content:
        for line in content.splitlines():
            if 'DEFUNSH(VTYSH' in line:
                match = re.search(r'DEFUNSH\s*\(\s*(\w+)', line)
                if match:
                    #print("Found:", match.group(1))
                    find = match.group(1)
                    content = content.replace(find, 'abcdef')

    '''
    pattern = r"(?<!\w)(" + "|".join(map(re.escape, sorted_keys_desc)) + r")(?!\w)"
    def replacer(match):
        key = match.group(1)
        return defines[key]
    content = re.sub(pattern, replacer, content)
    
    '''
    kkkk = []
    for key in sorted_keys_desc:
        if 'REDIST_HELP_STR' in key and 'ZEBRA' not in key and '_OSPFD' not in key and  '_ISISD' in content:
            continue
        if 'REDIST_STR' in key and 'ZEBRA' not in key and '_OSPFD' not in key and '_ISISD' in content:
            continue
        if 'PROTO_NAME' in key:
            continue
        #pattern = rf"(?<!\w){re.escape(key)}(?!\w)"
        #content = content.replace(key, defines[key])

        if key in content and key != 'GR' and key != 'ADD':
            content = content.replace(key, defines[key])


    #if 'BGP_AFI_SAFI_HELP_STR' in defines:
    #    print(defines['BGP_AFI_SAFI_HELP_STR'])
    #    stop_here()
    #LOG.info('name: {}'.format(key))

    # Match all DEFUN, DEFUN_NOSH, DEFUN_HIDDEN, and DEFPY blocks correctly
    content = content.replace('CMD_RANGE_STR(1, MULTIPATH_NUM)', "CMD_RANGE_STR")
    
    # Regular expression to remove text between /* and */
    pattern = re.compile(r"/\*.*?\*/", re.DOTALL)
    content = re.sub(pattern, "", content)

    #defun_blocks = re.findall(r"(?:DEFUN|DEFUN_HIDDEN|DEFUN_YANG|DEFUN_NOSH|DEFUN_YANG_NOSH|DEFUNSH|DEFPY_NOSH|DEFPY_YANG_NOSH|DEFPY|DEFPY_YANG|ALIAS|DEFSH)\s*\(.*?\)\s*\{.*?\}", content, re.DOTALL)
    defun_blocks = re.findall(
        r'(?:ALIAS|DEFSH)\s*\([\s\S]*?\)\n'
        r'|(?:DEFUN(?:_[A-Z]+)?|DEFUNSH|DEFPY(?:_[A-Z]+)?)\s*\([\s\S]*?\)\s*\{[\s\S]*?\}',
        content,
        re.DOTALL
    )
    
    '''
    pattern = r"""
    (?P<block>
        (?:DEFUN(?:_NOSH|_HIDDEN)?|DEFPY|DEFPY_NOSH)      # Match DEFUN, DEFUN_NOSH, DEFUN_HIDDEN, or DEFPY or DEFPY_NOSH
        \s*\(.*?\)\s*                          # Match the parameter list in parentheses (non-greedy)
        \{                                     # Match the opening brace of the block
        (?:                                    # Start non-capturing group for block content
            [^{}]+                           # Match any text that is not a brace
          |                                  # OR
            (?&block)                        # Recursively match a nested block
        )*                                     # Repeat as needed
        \}                                     # Match the closing brace of the block
    )
    """

    # Use the VERBOSE and DOTALL flags for clarity and to let '.' match newlines.
    defun_blocks = regex.findall(pattern, content, regex.VERBOSE | regex.DOTALL)
    '''
    results = []
    
    for block in defun_blocks:
    #ifndef FABRICD
        #block = block.replace(")\n", "$\n") # change end of block fung from ) to $
        block = "\n".join(
            line for line in block.splitlines() if not line.lstrip().startswith("#")
        )
        #block = block.replace('\n#ifndef FABRICD', '')
        #block = block.replace('\n#endif', '')
        block = block.replace("\\n", "\n")
        block = block.replace("\"", "")
        block = block.replace("\\", "")
        block = block.replace('\\\n ', ' ')
        block = block.replace('][', '] [')
        block = block.replace(');', 'end_cmd')
        block = block.replace('<+/-metric>', 'METRIC')
        
        #if  'FRR_IP_' in block and '_ISISD' in block:
        #    print(block)
        #    stop_here()
        
        
        #if 'mtrace ' in block:
            #print('XXXXXX {}'.format(block))
            #print('XXXXXX {}'.format(parse_defun(block)))
            #stop_here()
        #if 'DEFUNSH' in block:
        #    LOG.info('block: {}'.format(block))
        
        result = parse_defun(block)
        if result:
            results.append(result)
            #if 'nexthop-group ' in block:
                #print('XXXXXX {}'.format(block))
                #print('XXXXXX {}'.format(result))
                #stop_here()

    return results

# Example usage
if __name__ == "__main__":
    c_functions = """
    DEFUN (no_router_ospf,
           no_router_ospf_cmd,
           "no router ospf [{(1-65535)|vrf NAME}]",
           NO_STR
           "Enable a routing process\n"
           "Start OSPF configuration\n"
           "Instance ID\n"
           VRF_CMD_HELP_STR)
    {
        struct ospf *ospf;
        unsigned short instance = 0;

        ospf = ospf_cmd_lookup_ospf(vty, argv, argc, 0, &instance);
        if (ospf == NULL) {
            if (instance)
                return CMD_NOT_MY_INSTANCE;
            else
                return CMD_WARNING;
        }
        ospf_finish(ospf);

        return CMD_SUCCESS;
    }

    DEFUN_NOSH (router_bgp,
                router_bgp_cmd,
                "router bgp <1-65535>",
                "Enable a routing process\n"
                "BGP protocol\n"
                "AS number\n")
    {
        struct bgp *bgp;

        bgp = bgp_lookup(as_number);
        if (!bgp) {
            return CMD_WARNING;
        }

        return CMD_SUCCESS;
    }

    DEFUN_HIDDEN (hidden_cmd,
                  hidden_cmd_key,
                  "hidden command",
                  "This is a hidden command\n")
    {
        return CMD_SUCCESS;
    }

    DEFPY (py_test,
           py_test_cmd,
           "test py command",
           "Test command implemented in Python\n")
    {
        return CMD_SUCCESS;
    }
    """

    results = parse_all_defuns(c_functions)
    for result in results:
        LOG.info("Function Name:", result["function_name"])
        LOG.info("Command Name:", result["command_name"])
        LOG.info("Command String:", result["command_string"])
        LOG.info("Descriptions:", result["descriptions"])
        #LOG.info("---")
