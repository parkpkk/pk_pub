git clone -b etri-202505-mgmt --recurse-submodules https://gitlab.w2sh.synology.me/sonic/sonic-buildimage.git

git clone -b 202511 --recurse-submodules https://github.com/sonic-net/sonic-buildimage.git

make init

make configure PLATFORM=vs

make SONIC_BUILD_JOBS=16 target/sonic-vs.img.gz

qemu-img info sonic-vs-test.img

qemu-img convert -p -f qcow2 -O vmdk sonic-vs-test.img sonic-vs-test.vmdk

qemu-img convert -p -f qcow2 -O vdi sonic-vs-click.img sonic-vs-click.vdi

tar zcvf u2004-test-base-vdi.tgz u2004-test-base.vdi

gzip -c sonic-vs-etri.img > sonic-vs-etri.img.gz
