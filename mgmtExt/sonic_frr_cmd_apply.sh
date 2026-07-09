#!/bin/bash
#
# -----------------------------------------------------------------------------
# Script Name : sonic_frr_clis_apply.sh
# Version     : 1.0
# Description : SONiC FRR 8.5.1 Integration Build Script
# Author      : [Your Name or Organization]
# License     : [Optional - MIT, GPL, etc.]
# -----------------------------------------------------------------------------
#
# Summary:
# This script automates the integration of FRR (Free Range Routing) version 8.5.1
# with SONiC (Software for Open Networking in the Cloud), including Sonic Translib
# components that enhance routing protocol management and support.
#
# Features:
# - Integrates Sonic Translib 8.5.1 with FRR 8.5.1
# - Generates YANG models and Python CLI modules from FRR definitions
# - Deploys files to SONiC packages: sonic-utilities, sonic-mgmt-common, docker-fpm-frr
# - Enables enhanced routing configuration via CLIs and YANG support
#
# Requirements:
# - Root privileges
# - Functional SONiC build environment (Docker, Git, Make, etc.)
# - Sonic Translib 8.5.1 files located at: mgmtExt/frrCmd
# - Minimum: 16GB RAM, 20GB free disk space, Linux with loop & overlay modules
#
# Usage:
#   sudo ./sonic_frr_integration.sh
#
# Estimated Build Time: 1–2 hours depending on system performance
# -----------------------------------------------------------------------------

# Enable debug output for each command
set -x

# -----------------------------------------------------------------------------
# Step 0: Set up environment variables
# -----------------------------------------------------------------------------
SONIC_SRC=$(pwd)/..
echo "SONiC source directory: $SONIC_SRC"

# -----------------------------------------------------------------------------
# Step 1: Prepare FRR source tree with Translib integration
# -----------------------------------------------------------------------------

echo "Copying Sonic Translib 8.5.1 components into FRR source directory..."
cp -r ${SONIC_SRC}/mgmtExt/frrCmd ${SONIC_SRC}/src/sonic-frr/frr

# Navigate to FRR source and check out the target FRR version
cd ${SONIC_SRC}/src/sonic-frr/frr
git checkout frr-8.5.1

# Generate YANG models and Python modules from FRR CLI definitions
cd frrCmd
echo "Generating YANG and CLI modules using decmd.py..."
mkdir -p yang
mkdir -p tree
mkdir -p template
mkdir -p modules/config_router
mkdir -p modules/main_show
python3 decmd.py

# -----------------------------------------------------------------------------
# Step 2: Stage generated files
# -----------------------------------------------------------------------------

echo "Staging generated files for distribution..."

# Stage support and CLI files
cp -r modules ${SONIC_SRC}/mgmtExt/frrCmd                                # CLI submodules
cp -r yang ${SONIC_SRC}/mgmtExt/frrCmd
cp -r tree ${SONIC_SRC}/mgmtExt/frrCmd
cp -r template ${SONIC_SRC}/mgmtExt/frrCmd

# Clean up translib source and revert to original Git branch
rm -rf ${SONIC_SRC}/src/sonic-frr/frr/frrCmd
cd ../
git checkout -

# -----------------------------------------------------------------------------
# Step 3: Distribute files to SONiC source tree
# -----------------------------------------------------------------------------

echo "Deploying FRR CLI and YANG modules into SONiC source tree..."

cd ${SONIC_SRC}/mgmtExt
FRR_DIR="${SONIC_SRC}/mgmtExt/frrCmd"

if [ -d "$FRR_DIR" ]; then
    echo "Staged files found. Proceeding with distribution..."

    # -------------------------------
    # 3.1 Distribute to sonic-utilities
    # -------------------------------
    mkdir -p ${SONIC_SRC}/src/sonic-utilities/frr

    # CLI main and modules
    cp -r frrCmd/modules/* ${SONIC_SRC}/src/sonic-utilities/frr

    # -------------------------------
    # 3.2 Distribute to sonic-mgmt-common
    # -------------------------------
    #cp frrCmd/yang_sonic/import.mk ${SONIC_SRC}/src/sonic-mgmt-common/models/yang/sonic
	#cp frrCmd/yang/sonic-frr-*.yang ${SONIC_SRC}/src/sonic-mgmt-common/models/yang/sonic

    # -------------------------------
    # 3.4 Cleanup
    # -------------------------------
    #rm -rf ${FRR_DIR}

else
    echo "Error: Expected staging directory $FRR_DIR not found. Aborting..."
    exit 1
fi

echo "FRR 8.5.1 integration complete. You may now rebuild the SONiC image."

# Prepare for Rebuild the SONiC virtual switch image
echo "Prepare for Rebuilding SONiC virtual switch image..."

# Remove existing packages to force rebuild

FILE="$SONIC_SRC/target/debs/bookworm/sonic-eventd_1.0.0-0_amd64.deb"
if [ -f "$FILE" ]; then
    echo "$FILE exists, removing..."
    rm ${SONIC_SRC}/target/debs/bookworm/sonic-eventd_1.0.0-0_amd64.*
    sleep 1
else
    echo "$FILE not found"
fi

FILE="$SONIC_SRC/target/debs/bookworm/sonic-mgmt-common_1.0.0_amd64.deb"
if [ -f "$FILE" ]; then
    echo "$FILE exists, removing..."
    rm ${SONIC_SRC}/target/debs/bookworm/sonic-mgmt-common_1.0.0_amd64.*
    sleep 1
else
    echo "$FILE not found"
fi

FILE="$SONIC_SRC/target/python-wheels/bookworm/sonic_utilities-1.2-py3-none-any.whl"
if [ -f "$FILE" ]; then
    echo "$FILE exists, removing..."
    rm ${SONIC_SRC}/target/python-wheels/bookworm/sonic_utilities-1.2-py3-none-any.whl*
    sleep 1
else
    echo "$FILE not found"
fi

FILE="$SONIC_SRC/target/docker-fpm-frr.gz"
if [ -f "$FILE" ]; then
    echo "$FILE exists, removing..."
    rm ${SONIC_SRC}/target/docker-fpm-frr.*
    sleep 1
else
    echo "$FILE not found"
fi

# Remove existing image and rebuild
# Build initial VS image
cd ${SONIC_SRC}
FILE="$SONIC_SRC/target/sonic-vs.img.gz"
if [ -f "$FILE" ]; then
    echo "$FILE exists, continue..."
	rm target/sonic-vs.img.gz
fi
