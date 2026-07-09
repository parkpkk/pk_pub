# working directory:
sonic-buildimage/src/sonic-frr/frr

# copy all python tool and import.mk

cp frrCmd sonic-buildimage/src/sonic-frr/frr

#edit import.mk
# default import
input_files += ../lib/command.h
input_files += ../lib/route_types.h
input_files += ../lib/vrf.h
input_files += ../lib/mpls.h
input_files += ../lib/log.h
input_files += ../isisd/isisd.h
input_files += ../lib/pbr.h

input_files += ../lib/if.c
input_files += ../lib/command.c
input_files += ../lib/vty.c
input_files += ../lib/memory_vty.c

input_files += ../vtysh/vtysh.c

# optional import

input_files += ../sharpd/sharp_vty.c
input_files += ../nhrpd/nhrp_vty.c
input_files += ../watchfrr/watchfrr_vty.c
input_files += ../ospfd/ospf_vty.c
input_files += ../zebra/zebra_vty.c
input_files += ../zebra/zebra_mpls_vty.c
input_files += ../pbrd/pbr_vty.c
input_files += ../bgpd/rfapi/rfapi_vty.c
input_files += ../bgpd/bgp_vty.c
input_files += ../bgpd/bgp_flowspec_vty.c
input_files += ../bgpd/bgp_evpn_vty.c
#input_files += ../bfdd/bfdd_vty.c
input_files += ../staticd/static_vty.c
input_files += ../eigrpd/eigrp_vty.c
input_files += ../pimd/pim_vty.c

input_files += ../isisd/isis_vty_fabricd.c
input_files += ../isisd/isis_vty_common.c
input_files += ../isisd/isis_cli.c

###zebra
input_files += ../zebra/interface.c
input_files += ../zebra/rtadv.c
input_files += ../zebra/irdp_interface.c
input_files += ../zebra/zebra_vty.c
input_files += ../zebra/zebra_mpls_vty.c
input_files += ../zebra/router-id.c
input_files += ../zebra/debug.c
input_files += ../zebra/zebra_routemap.c

#run decmd script
$ cd sonic-buildimage/src/sonic-frr/frr/frrCmd
$ python3 decmd.py

it will generate yang files and 'main.py'(APP.MODULE) at same path now


######################
update more about app.module
######################

sonic-buildimage/src/sonic-utilities
$ mkdir frr
$ cp main.py sonic-buildimage/src/sonic-utilities/frr
$ cp validated_config_db_connector.py sonic-buildimage/src/sonic-utilities/frr
$ cp frr_types_extension.py sonic-buildimage/src/sonic-utilities/frr
$ cp frr sonic-buildimage/src/sonic-utilities/sonic-utilities-data/bash_completion.d


# edit setup.py
cd sonic-buildimage/src/sonic-utilities
------line ~226-----
		'watchdogutil = watchdogutil.main:watchdogutil',
		'sonic-cli-gen = sonic_cli_gen.main:cli',
		'wol = wol.main:wol',
		'frr = frr.main:frr',   <<<<<================ add
	]
},
install_requires=[
	'bcrypt==3.2.2',
	'click==7.0',
	'cryptography>=3.3.2',

------line ~89-----
        'watchdogutil',
        'sonic_cli_gen',
        'wol',
        'frr',    <<<<<================ add
    ],
    package_data={
        'generic_config_updater': ['gcu_services_validator.conf.json', 'gcu_field_operation_validators.conf.json'],
        'show': ['aliases.ini'],
		
######################
update more about yang
######################
$ cd sonic-buildimage/src/sonic-frr/frr/frrCmd
$ cp sonic-frr* sonic-buildimage/src/sonic-mgmt-common/models/yang/sonic
$ cp yang_sonic/import.mk sonic-buildimage/src/sonic-mgmt-common/models/yang/sonic


######################
update docker-fmp-frr
######################
$ cd sonic-buildimage/src/sonic-frr/frr/frrCmd
$ cp frrbridged sonic-buildimage/dockers/docker-fpm-frr

# edit Dockerfile.j2
$ cd sonic-buildimage/dockers/docker-fpm-frr

------line ~48-----

COPY ["frr", "/usr/share/sonic/templates"]
COPY ["docker_init.sh", "/usr/bin/"]
COPY ["snmp.conf", "/etc/snmp/frr.conf"]
COPY ["frrbridged", "/usr/local/bin/frrbridged"]  <<<<<================ add
COPY ["TSA", "/usr/bin/TSA"]
COPY ["TSB", "/usr/bin/TSB"]
COPY ["TSC", "/usr/bin/TSC"]
COPY ["TS", "/usr/bin/TS"]

# edit supervisord.conf.j2
$ cd sonic-buildimage/dockers/docker-fpm-frr/frr/supervisord

------line ~157-----

[program:bgpmon]
command=/usr/local/bin/bgpmon
priority=6
autostart=false
autorestart=true
startsecs=0
stdout_logfile=syslog
stderr_logfile=syslog
dependent_startup=true
dependent_startup_wait_for=bgpd:running

[program:frrbridged]	 									<<<<<================ add
command=/usr/bin/env python3 /usr/local/bin/frrbridged	 	
priority=6	 												
autostart=false	 											
autorestart=true
startsecs=0
stdout_logfile=syslog
stderr_logfile=syslog
dependent_startup=true
dependent_startup_wait_for=bgpd:running

{% endif %}

# rebuild image
make clean
make init
make SONIC_BUILD_JOBS=32 target/sonic-vs.img.gz