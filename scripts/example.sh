#!/bin/bash

# This is a sample shell script with some vulnerabilities for testing

# Vulnerability 1: Command Injection
user_input="; echo 'Command injection successful';"
output=$(echo "User input: $user_input")

# Vulnerability 1: Command Injection
user_input1="; echo 'Command injection successful';"
output1=$(echo "User input: $user_input1")

# Vulnerability 2: Unsafe Variable Usage
password="secret"
echo "Password is: $password"

# No vulnerabilities here
echo "This is a safe command."

# Vulnerability 3: Another Command Injection
filename="file.txt"
rm $filename
