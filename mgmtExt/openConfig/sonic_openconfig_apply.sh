#!/bin/bash

# 1. Path Definitions
# Use $() for pwd command, but use ${} or $ for variables
MGMT_DIR=$(pwd)/..
SOURCE_DIR="${MGMT_DIR}/openConfig"
TARGET_DIR="${MGMT_DIR}/../src/sonic-mgmt-common/models/yang/sonic"
IMPORT_MK="import.mk"
PYTHON_SCRIPT="tree2dict.py"

# Change to the working directory
# Use double quotes to handle potential spaces in paths
cd "$SOURCE_DIR" || { echo "❌ Source directory not found: $SOURCE_DIR"; exit 1; }

# 2. Execute the Python conversion script
echo "🚀 Starting YANG conversion process from $IMPORT_MK..."
python3 "$PYTHON_SCRIPT"

# Check if Python script executed successfully
if [ $? -ne 0 ]; then
    echo "❌ Error occurred while running $PYTHON_SCRIPT. Please check Python logic or $IMPORT_MK."
    exit 1
fi

# 3. Create target directory if it doesn't exist
if [ ! -d "$TARGET_DIR" ]; then
    echo "📂 Target directory missing, creating: $TARGET_DIR"
    mkdir -p "$TARGET_DIR"
fi

# 4. Scan import.mk to identify and copy generated files
echo "🚚 Copying generated 'sonic-*.yang' files to SONiC system path..."

while IFS= read -r line || [ -n "$line" ]; do
    # Skip empty lines and comments
    [[ -z "$line" || "$line" =~ ^# ]] && continue

    # Extract base filename from import.mk path (e.g., openconfig-acl)
    filename=$(basename "$line" .yang)
    generated_file="sonic-${filename}.yang"

    # Copy the file only if it exists
    if [ -f "$generated_file" ]; then
        cp -v "$generated_file" "$TARGET_DIR/"
    else
        echo "⚠️ Warning: Generated file not found: $generated_file"
    fi
done < "$IMPORT_MK"

echo "--------------------------------------------------"
echo "✅ Process completed! YANG models are located at: $TARGET_DIR"
ls -l "$TARGET_DIR"/sonic-openconfig*