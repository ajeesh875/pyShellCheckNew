import re

pattern_data = '\\$\\((.*?)\\)'
description = 'Command Injection vulnerability detected.'
line = 'output1=$(echo "User input: $user_input1")'

pattern = re.compile(pattern_data)
matches = pattern.finditer(line)

for match in matches:
    matched_text = match.group()
    start_position = match.start()
    end_position = match.end()
    print(f"Matched: '{matched_text}' at position {start_position}-{end_position}")
