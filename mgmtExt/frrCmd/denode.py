import re
import os
from app_logging import LOG

vtysh_c = './vtysh/vtysh.c'
def vtysh_content():
    str_out = ''
    if not os.path.exists(vtysh_c):
        LOG.info(f"Error: Input file '{vtysh_c}' not found.")
        
    # Process the input file
    try:
        with open(vtysh_c, 'r') as file:
            LOG.info(f"Contents of '{vtysh_c}':")
            str_out = file.read()
    except Exception as e:
        LOG.info(f"Error reading the input file '{vtysh_c}': {e}")
    return str_out

def parse_install_elements(content):
    # Regex pattern for install_element
    
    install_pattern = re.compile(r"install_element\((\w+),\s*&([\w_]+)\);")

    results = []
    results_ = {}
    for match in install_pattern.finditer(content):
        node = match.group(1)  # Capture the node (e.g., OSPF_NODE)
        command_name = match.group(2)  # Capture the command name (e.g., ospf_passive_interface_addr_cmd)
        results.append({"node": node, "command_name": command_name})
        if command_name in results_:
            results_[command_name].append(node)
        else:
            results_[command_name] = [node]
        #LOG.info('command_name: {}'.format(command_name))
        #LOG.info('node: {}'.format(node))
    #LOG.info('result: {}'.format(results_))
    #return results
    return results_
    
def parse_graph(content):
    # Regex pattern to extract nodes and commands
    edge_pattern = re.compile(r'(\w+)\s*->\s*(\w+)\s*\[\s*label="([^"]+)"\s*\];')

    nodes = set()
    edges = []

    for match in edge_pattern.finditer(content):
        source = match.group(1)
        target = match.group(2)
        command = match.group(3)

        # Add nodes to the set
        nodes.add(source)
        nodes.add(target)

        # Append edge with command
        if target == 'BGP_NODE':
            command = 'router bgp [(1-4294967295) [<view|vrf> VIEWVRFNAME]]'
        if target == 'EIGRP_NODE':
            command = 'router eigrp (1-65535) [vrf NAME]'
            
        edges.append({"nosh": source, "nosh_command": command, "next_nosh": target})
        
    edges.append({"nosh": 'CONFIG_NODE', "nosh_command": 'pbr-map PBRMAP seq (1-700)', "next_nosh": 'PBRMAP_NODE'})
    edges.append({"nosh": 'CONFIG_NODE', "nosh_command": 'bfd', "next_nosh": 'BFD_NODE'})

    return {"nodes": nodes, "edges": edges}
    
    
def parse_defunsh(content):
    """
    Parse DEFUNSH blocks to extract command string, description, and target node.

    Args:
        content (str): The C code containing DEFUNSH definitions.

    Returns:
        list: A list of dictionaries with keys 'command', 'description', and 'node'.
    """
    #content = vtysh_content()
    # Regex pattern to match DEFUNSH blocks
    pattern = re.compile(
        r"DEFUNSH\([^,]+,\s*[^,]+,\s*[^,]+,\s*\"(.*?)\",\n\s*(\".*?\")\)\s*\{\n.*?vty->node = (\w+);",
        re.DOTALL
    )

    results = []
    for match in pattern.finditer(content):
        command = match.group(1).strip()
        description = match.group(2).replace("\"", "").replace("\t", "")
        description_lines = []
        for line in description.splitlines():
            if not line.strip().startswith("//"):
                line = line.strip()
                if line:
                    description_lines.append(line)

        node = match.group(3).strip()

        results.append({
            "command_string": command,
            "descriptions": description_lines,
            "node": node
        })

    return results

# Example content
content = """
DEFUNSH(VTYSH_BGPD, address_family_ipv6_multicast,
	address_family_ipv6_multicast_cmd, "address-family ipv6 multicast",
	"Enter Address Family command mode\n"
	"Address Family\n"
	"Address Family modifier\n")
{
	vty->node = BGP_IPV6M_NODE;
	return CMD_SUCCESS;
}

DEFUNSH(VTYSH_BGPD, address_family_ipv6_vpn, address_family_ipv6_vpn_cmd,
	"address-family ipv6 vpn",
	"Enter Address Family command mode\n"
	"Address Family\n"
	"Address Family modifier\n")
{
	vty->node = BGP_VPNV6_NODE;
	return CMD_SUCCESS;
}

DEFUNSH(VTYSH_BGPD, address_family_ipv6_labeled_unicast,
	address_family_ipv6_labeled_unicast_cmd,
	"address-family ipv6 labeled-unicast",
	"Enter Address Family command mode\n"
	"Address Family\n"
	"Address Family modifier\n")
{
	vty->node = BGP_IPV6L_NODE;
	return CMD_SUCCESS;
}
"""

# Parse the content
'''
parsed_results = parse_defunsh(content)

# Display results
for result in parsed_results:
    LOG.info(f"Command: {result['command_string']}")
    LOG.info(f"Description: {result['descriptions']}")
    LOG.info(f"Node: {result['node']}")
    LOG.info("---")
'''

# Example usage
vtysh_exit_code = """
static int vtysh_exit(struct vty *vty)
{
    switch (vty->node) {
    case VIEW_NODE:
    case ENABLE_NODE:
        exit(0);
        break;
    case CONFIG_NODE:
        vty->node = ENABLE_NODE;
        break;
    case INTERFACE_NODE:
    case PW_NODE:
    case LOGICALROUTER_NODE:
    case VRF_NODE:
    case NH_GROUP_NODE:
    case ZEBRA_NODE:
    case BGP_NODE:
    case RIP_NODE:
    case RIPNG_NODE:
    case OSPF_NODE:
    case OSPF6_NODE:
    case EIGRP_NODE:
    case BABEL_NODE:
    case LDP_NODE:
    case LDP_L2VPN_NODE:
    case ISIS_NODE:
    case OPENFABRIC_NODE:
    case RMAP_NODE:
    case PBRMAP_NODE:
    case VTY_NODE:
    case KEYCHAIN_NODE:
    case BFD_NODE:
    case RPKI_NODE:
        vtysh_execute("end");
        vtysh_execute("configure terminal");
        vty->node = CONFIG_NODE;
        break;
    case BGP_VPNV4_NODE:
    case BGP_VPNV6_NODE:
    case BGP_IPV4_NODE:
    case BGP_IPV4M_NODE:
    case BGP_IPV4L_NODE:
    case BGP_IPV6_NODE:
    case BGP_IPV6M_NODE:
    case BGP_IPV6L_NODE:
    case BGP_FLOWSPECV4_NODE:
    case BGP_FLOWSPECV6_NODE:
    case BGP_VRF_POLICY_NODE:
    case BGP_EVPN_NODE:
    case BGP_VNC_DEFAULTS_NODE:
    case BGP_VNC_NVE_GROUP_NODE:
    case BGP_VNC_L2_GROUP_NODE:
        vty->node = BGP_NODE;
        break;
    case BGP_EVPN_VNI_NODE:
        vty->node = BGP_EVPN_NODE;
        break;
    case LDP_IPV4_NODE:
    case LDP_IPV6_NODE:
        vty->node = LDP_NODE;
        break;
    case LDP_IPV4_IFACE_NODE:
        vty->node = LDP_IPV4_NODE;
        break;
    case LDP_IPV6_IFACE_NODE:
        vty->node = LDP_IPV6_NODE;
        break;
    case LDP_PSEUDOWIRE_NODE:
        vty->node = LDP_L2VPN_NODE;
        break;
    case KEYCHAIN_KEY_NODE:
        vty->node = KEYCHAIN_NODE;
        break;
    case LINK_PARAMS_NODE:
        vty->node = INTERFACE_NODE;
        break;
    case BFD_PEER_NODE:
        vty->node = BFD_NODE;
        break;
    default:
        break;
    }
    return CMD_SUCCESS;
}
"""

def parse_vtysh_exit(function_code=vtysh_exit_code):
    """
    Parse the vtysh_exit function to extract origin and next node relationships.

    Args:
        function_code (str): The C code for the vtysh_exit function.

    Returns:
        list: A list of dictionaries where each dictionary contains 'origin' and 'next' keys.
    """
    function_code = vtysh_content()
    
    function_pattern = re.compile(r"static int vtysh_exit\(.*?\)\s*\{.*?\}", re.DOTALL)

    # Extract the vtysh_exit function
    function_match = function_pattern.search(function_code)
    if not function_match:
        return []  # Return an empty list if the function is not found

    # Extract the matched function's content
    function_body = function_match.group(0)
    
    
    # Regex to match case and assignment statements
    case_pattern = re.compile(r"case\s+(\w+):")
    assign_pattern = re.compile(r"vty->node\s*=\s*(\w+);")

    # Split the function into lines
    lines = function_body.splitlines()

    # Variables to track the current case statements and assignments
    current_cases = []
    node_relationships = []

    for line in lines:
        # Check for case statement
        case_match = case_pattern.search(line)
        if case_match:
            current_cases.append(case_match.group(1))

        # Check for node assignment
        assign_match = assign_pattern.search(line)
        if assign_match:
            next_node = assign_match.group(1)
            for origin_node in current_cases:
                node_relationships.append({
                    "origin": origin_node,
                    "parent": next_node
                })
            current_cases = []  # Reset cases after processing an assignment

    return node_relationships


'''
# Parse the function
parsed_nodes = parse_vtysh_exit(vtysh_exit_code)

# Display results
for relationship in parsed_nodes:
    LOG.info(f"Origin Node: {relationship['origin']}, Parent Node: {relationship['parent']}")
    
'''