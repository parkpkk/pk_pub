
// String used in command syntax
#define FRR_IP_PROTOCOL_MAP_STR_ZEBRA \
  "<any|babel|bgp|connected|eigrp|isis|kernel|nhrp|openfabric|ospf|rip|static|table|vnc>"

// Help string for each protocol token
#define FRR_IP_PROTOCOL_MAP_HELP_STR_ZEBRA \
  "Any of the above protocols\n" \
  "Babel routing protocol (Babel)\n" \
  "Border Gateway Protocol (BGP)\n" \
  "Connected routes (directly attached subnet or host)\n" \
  "Enhanced Interior Gateway Routing Protocol (eigrp)\n" \
  "Intermediate System to Intermediate System (IS-IS)\n" \
  "Kernel routes (not installed via the zebra RIB)\n" \
  "Next Hop Resolution Protocol (NHRP)\n" \
  "OpenFabric Routing Protocol\n" \
  "Open Shortest Path First (OSPFv2)\n" \
  "Routing Information Protocol (RIP)\n" \
  "Statically configured routes\n" \
  "Non-main Kernel Routing Table\n" \
  "Virtual Network Control (VNC)\n"

#define FRR_REDIST_STR_OSPFD \
  "<babel|bgp|connected|eigrp|isis|kernel|nhrp|openfabric|ospf|rip|static|table|vnc>"

// Help string for each protocol token
#define FRR_REDIST_HELP_STR_OSPFD \
  "Babel routing protocol (Babel)\n" \
  "Border Gateway Protocol (BGP)\n" \
  "Connected routes (directly attached subnet or host)\n" \
  "Enhanced Interior Gateway Routing Protocol (eigrp)\n" \
  "Intermediate System to Intermediate System (IS-IS)\n" \
  "Kernel routes (not installed via the zebra RIB)\n" \
  "Next Hop Resolution Protocol (NHRP)\n" \
  "OpenFabric Routing Protocol\n" \
  "Open Shortest Path First (OSPFv2)\n" \
  "Routing Information Protocol (RIP)\n" \
  "Statically configured routes\n" \
  "Non-main Kernel Routing Table\n" \
  "Virtual Network Control (VNC)\n"

#define FRR_IP_REDIST_STR_ZEBRA \
  "<babel|bgp|connected|eigrp|isis|kernel|nhrp|openfabric|rip|static|table|vnc>"

// Help string for each protocol token
#define FRR_IP_REDIST_HELP_STR_ZEBRA \
  "Babel routing protocol (Babel)\n" \
  "Border Gateway Protocol (BGP)\n" \
  "Connected routes (directly attached subnet or host)\n" \
  "Enhanced Interior Gateway Routing Protocol (eigrp)\n" \
  "Intermediate System to Intermediate System (IS-IS)\n" \
  "Kernel routes (not installed via the zebra RIB)\n" \
  "Next Hop Resolution Protocol (NHRP)\n" \
  "OpenFabric Routing Protocol\n" \
  "Routing Information Protocol (RIP)\n" \
  "Statically configured routes\n" \
  "Non-main Kernel Routing Table\n" \
  "Virtual Network Control (VNC)\n"
  

#define FRR_IP6_PROTOCOL_MAP_STR_ZEBRA \
  "<any|babel|bgp|connected|isis|kernel|nhrp|openfabric|ospf6|ripng|static|table|vnc>"

#define FRR_IP6_PROTOCOL_MAP_HELP_STR_ZEBRA \
  "Any of the above protocols\n" \
  "Babel routing protocol (Babel)\n" \
  "Border Gateway Protocol (BGP)\n" \
  "Connected routes (directly attached subnet or host)\n" \
  "Intermediate System to Intermediate System (IS-IS)\n" \
  "Kernel routes (not installed via the zebra RIB)\n" \
  "Next Hop Resolution Protocol (NHRP)\n" \
  "OpenFabric Routing Protocol\n" \
  "Open Shortest Path First (IPv6) (OSPFv3)\n" \
  "Routing Information Protocol (RIP)\n" \
  "Statically configured routes\n" \
  "Non-main Kernel Routing Table\n" \
  "Virtual Network Control (VNC)\n"
  
#define FRR_IP6_REDIST_STR_ZEBRA \
  "<babel|bgp|connected|isis|kernel|nhrp|openfabric|ospf6|ripng|static|table|vnc>"

#define FRR_IP6_REDIST_HELP_STR_ZEBRA \
  "Babel routing protocol (Babel)\n" \
  "Border Gateway Protocol (BGP)\n" \
  "Connected routes (directly attached subnet or host)\n" \
  "Intermediate System to Intermediate System (IS-IS)\n" \
  "Kernel routes (not installed via the zebra RIB)\n" \
  "Next Hop Resolution Protocol (NHRP)\n" \
  "OpenFabric Routing Protocol\n" \
  "Open Shortest Path First (IPv6) (OSPFv3)\n" \
  "Routing Information Protocol (RIP)\n" \
  "Statically configured routes\n" \
  "Non-main Kernel Routing Table\n" \
  "Virtual Network Control (VNC)\n"
  
#define DAEMONS_LIST \
  "<zebra|bgpd|ripd|ripngd|ospfd|ospf6d|isisd|fabricd|nhrpd|ldpd|babeld|eigrpd|pimd|pim6d|pbrd|staticd|bfdd|vrrpd|pathd>"
  
#define DAEMONS_STR \
  "For the zebra daemon\n" \
  "For the bgpd daemon\n" \
  "For the ripd daemon\n" \
  "For the ripngd daemon\n" \
  "For the ospfd daemon\n" \
  "For the ospf6d daemon\n" \
  "For the isisd daemon\n" \
  "For the fabricd daemon\n" \
  "For the nhrpd daemon\n" \
  "For the ldpd daemon\n" \
  "For the babeld daemon\n" \
  "For the eigrpd daemon\n" \
  "For the pimd daemon\n" \
  "For the pim6d daemom\n" \
  "For the pbrd daemon\n" \
  "For the staticd daemon\n" \
  "For the bfdd daemon\n" \
  "For the vrrpd daemon\n" \
  "For the pathd daemon\n"


#define PIM_STR "PIM information\n"

#define PROTO_NAME "isis"