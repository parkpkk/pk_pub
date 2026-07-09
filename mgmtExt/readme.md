# SONiC FRR 8.5.1 Integration Script

## Overview
**Script Name:** `sonic_frr_clis_apply.sh`

This script automates the integration of **FRR (Free Range Routing) version 8.5.1** into the SONiC build environment. It handles the generation of YANG models and Python CLI wrappers from FRR definitions and distributes them to the correct SONiC packages (`sonic-utilities`, `sonic-mgmt-common`, etc.).

Finally, it cleans up specific build artifacts to ensure the next `make` command rebuilds the modified components.

## Prerequisites

### 1. System Requirements
* **OS:** Linux (Ubuntu/Debian recommended for SONiC builds).
* **Privileges:** Root (`sudo`) access is required.
* **Dependencies:** Python 3, Git, standard build tools (`make`, `cp`, `rm`).

### 2. Directory Structure
**Important:** The script relies on relative paths (`$(pwd)/..`). It **must** be placed inside a directory (e.g., `frrCmd`) located at the root of your SONiC source tree.

Your directory layout should look like this:

```text
sonic-buildimage/            <-- Root of your SONiC repo ($SONIC_SRC)
├── src/
│   ├── sonic-frr/
│   ├── sonic-utilities/
│   └── sonic-mgmt-common/
├── target/                  <-- Build artifacts
└── frrCmd/                  <-- WORKING DIRECTORY
    ├── sonic_frr_clis_apply.sh  <-- This script
    └── frrCmd/    <-- Source files containing decmd.py
        ├── decmd.py
        └── (other translib source files)