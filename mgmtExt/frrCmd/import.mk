# default import
input_files += ./MACRO.h

# lib headers
input_files += ../lib/command.h
input_files += ../lib/json.h
input_files += ../lib/log.h
input_files += ../lib/mpls.h
input_files += ../lib/pbr.h
input_files += ../lib/route_types.h
input_files += ../lib/vrf.h

# lib sources
input_files += ../lib/agentx.c
input_files += ../lib/command.c
input_files += ../lib/debug.c
#input_files += ../lib/ferr.c
input_files += ../lib/filter.c
input_files += ../lib/filter_cli.c
input_files += ../lib/grammar_sandbox.c
input_files += ../lib/hash.c
input_files += ../lib/if_rmap.c
input_files += ../lib/keychain.c
input_files += ../lib/lib_vty.c
input_files += ../lib/log_vty.c
input_files += ../lib/module.c
input_files += ../lib/nexthop_group.c
input_files += ../lib/northbound_cli.c
input_files += ../lib/northbound_confd.c
input_files += ../lib/northbound_sysrepo.c
input_files += ../lib/plist.c
input_files += ../lib/resolver.c
input_files += ../lib/routemap.c
input_files += ../lib/routemap_cli.c
input_files += ../lib/spf_backoff.c
input_files += ../lib/thread.c
input_files += ../lib/vty.c
input_files += ../lib/vrf.c
input_files += ../lib/workqueue.c
#input_files += ../lib/zlog_5424_cli.c

# babeld
input_files += ../babeld/babel_interface.c
input_files += ../babeld/babel_zebra.c
input_files += ../babeld/babeld.c

# bfdd
input_files += ../bfdd/bfdd_cli.c
input_files += ../bfdd/bfdd_vty.c

# bgpd headers
input_files += ../bgpd/bgp_vty.h

# bgpd sources
input_files += ../bgpd/bgp_attr.c
input_files += ../bgpd/bgp_bfd.c
input_files += ../bgpd/bgp_bmp.c
input_files += ../bgpd/bgp_community_alias.c
input_files += ../bgpd/bgp_debug.c
input_files += ../bgpd/bgp_dump.c
input_files += ../bgpd/bgp_errors.c
input_files += ../bgpd/bgp_evpn_vty.c
input_files += ../bgpd/bgp_filter.c
input_files += ../bgpd/bgp_flowspec_vty.c
input_files += ../bgpd/bgp_labelpool.c
input_files += ../bgpd/bgp_memory.c
input_files += ../bgpd/bgp_mplsvpn.c
input_files += ../bgpd/bgp_nexthop.c
input_files += ../bgpd/bgp_routemap.c
input_files += ../bgpd/bgp_route.c
input_files += ../bgpd/bgp_rpki.c
input_files += ../bgpd/bgp_vty.c
input_files += ../bgpd/rfapi/bgp_rfapi_cfg.c
input_files += ../bgpd/rfapi/rfapi.c
input_files += ../bgpd/rfapi/rfapi_vty.c
input_files += ../bgpd/rfapi/vnc_debug.c
input_files += ../bgpd/rfp-example/librfp/rfp_example.c

# eigrpd
input_files += ../eigrpd/eigrp_routemap.c
input_files += ../eigrpd/eigrp_dump.c
input_files += ../eigrpd/eigrp_vty.c
input_files += ../eigrpd/eigrp_cli.c

# isisd headers
input_files += ../isisd/isisd.h

# isisd sources
input_files += ../isisd/isis_cli.c
input_files += ../isisd/isis_ldp_sync.c
input_files += ../isisd/isis_redist.c
input_files += ../isisd/isis_spf.c
input_files += ../isisd/isis_sr.c
input_files += ../isisd/isis_te.c
input_files += ../isisd/isis_vty_fabricd.c
input_files += ../isisd/isisd.c

# ldpd
input_files += ../ldpd/ldp_vty_cmds.c

# nhrpd
input_files += ../nhrpd/nhrp_vty.c

# ospf6d
input_files += ../ospf6d/ospf6_abr.c
input_files += ../ospf6d/ospf6_area.c
input_files += ../ospf6d/ospf6_asbr.c
input_files += ../ospf6d/ospf6_auth_trailer.c
input_files += ../ospf6d/ospf6_bfd.c
input_files += ../ospf6d/ospf6_flood.c
input_files += ../ospf6d/ospf6_gr.c
input_files += ../ospf6d/ospf6_gr_helper.c
input_files += ../ospf6d/ospf6_intra.c
input_files += ../ospf6d/ospf6_interface.c
input_files += ../ospf6d/ospf6_lsa.c
input_files += ../ospf6d/ospf6_message.c
input_files += ../ospf6d/ospf6_neighbor.c
input_files += ../ospf6d/ospf6_nssa.c
input_files += ../ospf6d/ospf6_route.c
input_files += ../ospf6d/ospf6_spf.c
input_files += ../ospf6d/ospf6_top.c
input_files += ../ospf6d/ospf6_zebra.c
input_files += ../ospf6d/ospf6d.c

# ospfd
input_files += ../ospfd/ospf_bfd.c
input_files += ../ospfd/ospf_dump.c
input_files += ../ospfd/ospf_gr.c
input_files += ../ospfd/ospf_opaque.c
input_files += ../ospfd/ospf_routemap.c
input_files += ../ospfd/ospf_ri.c
input_files += ../ospfd/ospf_sr.c
input_files += ../ospfd/ospf_te.c
input_files += ../ospfd/ospf_vty.c
input_files += ../ospfd/ospf_ldp_sync.c

# pathd
input_files += ../pathd/path_cli.c
input_files += ../pathd/path_pcep_cli.c
input_files += ../pathd/path_ted.c

# pbrd
input_files += ../pbrd/pbr_vty.c

# pimd
input_files += ../pimd/pim6_cmd.c
input_files += ../pimd/pim6_mld.c
input_files += ../pimd/pim_cmd.c

# ripd
input_files += ../ripd/rip_cli.c
input_files += ../ripd/rip_debug.c
input_files += ../ripd/ripd.c

# ripngd
input_files += ../ripngd/ripng_cli.c
input_files += ../ripngd/ripng_debug.c
input_files += ../ripngd/ripngd.c

# sharpd
input_files += ../sharpd/sharp_vty.c

# staticd
input_files += ../staticd/static_vty.c

# tests
input_files += ../tests/helpers/c/main.c
input_files += ../tests/isisd/test_isis_spf.c
input_files += ../tests/lib/cli/test_cli.c
input_files += ../tests/lib/test_heavy.c
input_files += ../tests/lib/test_heavy_thread.c
input_files += ../tests/lib/test_heavy_wq.c
input_files += ../tests/lib/test_resolver.c
input_files += ../tests/ospfd/test_ospf_spf.c

# vrrpd
input_files += ../vrrpd/vrrp_vty.c

# vtysh
input_files += ../vtysh/vtysh.c
input_files += ../vtysh/vtysh_config.c
input_files += ../vtysh/vtysh_user.c

# watchfrr
input_files += ../watchfrr/watchfrr_vty.c

# zebra
input_files += ../zebra/debug.c
input_files += ../zebra/debug_nl.c
input_files += ../zebra/dplane_fpm_nl.c
input_files += ../zebra/if_netlink.c
input_files += ../zebra/interface.c
input_files += ../zebra/ioctl.c
input_files += ../zebra/irdp_interface.c
input_files += ../zebra/router-id.c
input_files += ../zebra/rtadv.c
input_files += ../zebra/zebra_dplane.c
input_files += ../zebra/zebra_fpm.c
input_files += ../zebra/zebra_mlag_vty.c
input_files += ../zebra/zebra_mpls_vty.c
input_files += ../zebra/zebra_ptm.c
input_files += ../zebra/zebra_pw.c
input_files += ../zebra/zebra_routemap.c
input_files += ../zebra/zebra_srv6_vty.c
input_files += ../zebra/zebra_vrf.c
input_files += ../zebra/zebra_vty.c
input_files += ../zebra/zserv.c
