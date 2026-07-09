#!/bin/bash
# Update package index
sudo apt update

# update python to 3.9
sudo add-apt-repository -y ppa:deadsnakes/ppa
sudo apt update
sudo apt install -y python3.9
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 2

if command -v python3.9 &> /dev/null && command -v pip3.9 &> /dev/null; then
    echo -e "\nalias python3='python3.9'\nalias pip3='pip3.9'" >> ~/.bashrc
    source ~/.bashrc
    python3 --version
fi

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Add Docker repository
sudo add-apt-repository "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/ubuntu focal stable"

# Update package index again
sudo apt update

# Install Docker CE
sudo apt install -y docker-ce

# Add current user to docker group
sudo usermod -aG docker ${USER}

# Configure network bridge settings
echo "net.bridge.bridge-nf-call-iptables=1" | sudo tee -a /etc/sysctl.conf
sudo modprobe br_netfilter
echo "br_netfilter" | sudo tee /etc/modules-load.d/br_netfilter.conf

# Apply sysctl settings
sudo sysctl -p

# Restart Docker
sudo systemctl restart docker

# Install Python3 pip and jq
sudo apt install -y python3-pip jq

sudo apt install quilt -y

# Install j2cli for the current user
sudo -u ${USER} pip3 install --user j2cli
sudo -u ${USER} pip3 install --user --upgrade j2cli

# Install regex and pyang
sudo -u ${USER} pip3 install regex pyang

# Function to check and update PATH
update_path() {
    local user_home=$(eval echo ~${USER})
    local bashrc="${user_home}/.bashrc"
    
    # Check if j2 is in PATH
    if ! command -v j2 &> /dev/null; then
        echo "Adding .local/bin to PATH in .bashrc"
        echo "export PATH=\$PATH:${user_home}/.local/bin" >> "${bashrc}"
        echo "PATH updated in .bashrc"
    fi

    # Source bashrc for the current user
    sudo -u ${USER} bash -c "source ${bashrc}"
}

# Call the PATH update function
update_path

# Verify j2cli installation
echo "Checking j2 version:"
j2 --version || echo "j2cli installation might have issues"

echo "Docker and j2cli installation complete!"
echo "Please log out and log back in, or start a new terminal session to use Docker and j2 without sudo"


# Function to check and create directories
create_directory() {
    local dir_path="$1"
    local user="${SUDO_USER:-$USER}"

    if [ ! -d "$dir_path" ]; then
        echo "Creating directory: $dir_path"
        sudo mkdir -p "$dir_path"
        sudo chown "$user:$user" "$dir_path"
    else
        echo "Directory already exists: $dir_path"
    fi
}

# Check and load overlay module
load_overlay_module() {
    # Check if overlay module is already loaded
    if ! lsmod | grep -q overlay; then
        echo "Loading overlay module..."
        sudo modprobe overlay
        
        # Verify module is loaded
        if lsmod | grep -q overlay; then
            echo "Overlay module loaded successfully"
        else
            echo "Failed to load overlay module"
            exit 1
        fi
    else
        echo "Overlay module is already loaded"
    fi
}

# Main setup function
setup_sonic_build_environment() {
    # Ensure overlay module is loaded
    load_overlay_module

    # Verify overlay module is loaded
    lsmod | grep overlay

    # Create required directories
    create_directory "/var/cache/sonic"
    create_directory "/vcache"
    
    # Create web directories for different Debian versions
    create_directory "/vcache/sonic-slave-buster/web"
    create_directory "/vcache/sonic-slave-bullseye/web"
    create_directory "/vcache/sonic-slave-bookworm/web"

    # Optional: Additional setup steps
    echo "SONiC build environment setup complete"
}

# Run the setup
setup_sonic_build_environment

# Optional: Verify directory permissions
echo "Directory permissions:"
ls -ld /var/cache/sonic /vcache /vcache/sonic-slave-*/web

echo "*************************************************************************"
echo "***Some users configuration need to reconnect new terminal to apply...***"
echo "*************************************************************************"