import subprocess

# Install curl
subprocess.run(['sudo', 'apt', 'install', 'curl'])

# Download the Brave browser keyring
subprocess.run(['sudo', 'curl', '-fsSLo', '/usr/share/keyrings/brave-browser-archive-keyring.gpg', 'https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg'])

# Add Brave browser repository to sources.list.d
subprocess.run(['echo', 'deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg] https://brave-browser-apt-release.s3.brave.com/ stable main', '|', 'sudo', 'tee', '/etc/apt/sources.list.d/brave-browser-release.list'])

# Update package list
subprocess.run(['sudo', 'apt', 'update'])

# Install Brave browser
subprocess.run(['sudo', 'apt', 'install', 'brave-browser'])
