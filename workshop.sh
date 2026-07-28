git clone -b 202511 --recurse-submodules https://github.com/sonic-net/sonic-buildimage.git

rm -f target/python-wheels/bookworm/sonic_yang_mgmt.* target/python-wheels/bookworm/sonic_frr_mgmt.* target/python-wheels/trixie/sonic_yang_mgmt.* target/debs/bookworm/sonic-mgmt-framework* target/debs/bookworm/sonic-mgmt-common* target/debs/bookworm/sonic-mgmt-framework* target/docker-test.gz target/sonic-vs.img.gz

make init

make configure PLATFORM=vs

make SONIC_BUILD_JOBS=16 target/sonic-vs.img.gz

