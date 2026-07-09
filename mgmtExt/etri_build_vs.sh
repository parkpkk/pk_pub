#!/bin/bash
########################################################################
# This script is for build sonic image of the virtual swtich platform.
# This script is used to automatically build the sonic image on our CI/CD/CT platfrom
# written by seong@etri.re.kr
########################################################################

SONIC_BUILD_JOBS=4
SONIC_BUILD_RETRY_COUNT=4
SONIC_BUILD_RETRY_INTERVAL=600

BUILD_BRANCH=etri-202505-mgmt
BUILD_RETRY_COUNT=4

SONIC_SRC=$(pwd)/..

sudo modprobe overlay
sudo modprobe loop

run_with_retry() {
	BUILD_PLATFORM=$1

	### clone the sonic-buildimage repository
	#git clone -b etri-202505-mgmt --recurse-submodules https://thinguyen:Nmtlovedttn2924@gitlab.w2sh.synology.me/sonic/sonic-buildimage.git
	
	### ensure the 'overlay' module is loaded on your development system

	### enter the source directory
	#cd sonic-buildimage
	cd $SONIC_SRC

	### execute make init one after cloning the repo.
	### or after fetching remote repo with submodule updates.
	make init

	### execute make configure once to configure ASIC.
	make configure PLATFORM=$BUILD_PLATFORM

	### build SONiC image with 4 jobs in parallel.
	### Note: You can set this higher, but 4 is a good number for most cases and is well-suited.

	for ((i=1; i<=$BUILD_RETRY_COUNT; i++))
	do
		# Check if sonic-eventd is already built
		FILE="$SONIC_SRC/target/debs/bullseye/sonic-eventd_1.0.0-0_amd64.deb"
		if [ -f "$FILE" ]; then
			echo "$FILE exists, continue..."
		else
			echo "$FILE not found!"
			echo "build $FILE..."
			make SONIC_BUILD_JOBS=$SONIC_BUILD_JOBS target/debs/bullseye/sonic-eventd_1.0.0-0_amd64.deb
		fi
	
		make SONIC_BUILD_JOBS=$SONIC_BUILD_JOBS all 2>&1 | tee build-$BUILD_PLATFORM-multijob-$i.log 
		EXIT_CODE=${PIPESTATUS[0]}
		if [ $EXIT_CODE -eq 0 ]; then
			echo "^^^^^^^^^^^^^^^^^^^^^^ SUCCESS sonic-buildimage on the parallel $i try ^^^^^^^^^^^^^^^^^^^^^^^^"
			break
		fi

		### as a last resort, try with single job.
		if (( $i == $BUILD_RETRY_COUNT )); then
			for ((j=1; j<=$BUILD_RETRY_COUNT; j++))
			do
				make SONIC_BUILD_JOBS=1 all 2>&1 | tee build-$BUILD_PLATFORM-singlejob-$j.log 
				EXIT_CODE=${PIPESTATUS[0]}
				if [ $EXIT_CODE -eq 0 ]; then
					echo "^^^^^^^^^^^^^^^^^^^^^^ SUCCESS sonic-buildimage on the single $j try ^^^^^^^^^^^^^^^^^^^^^^^^"
					break
				fi
			done
		fi
	done
}

CUR_DIR=$PWD

#mkdir -p platform-vs; cd platform-vs
run_with_retry vs &

cd $CUR_DIR
