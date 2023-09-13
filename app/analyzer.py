import re
import json
from collections import defaultdict

class ScriptAnalyzer:
    def __init__(self):
        self.regex_config = self.load_regex_config()

    def load_regex_config(self):
        config_file = "config/regex_config.json"
        with open(config_file, 'r') as file:
            json_content = json.load(file)
            # Load the regular expressions and descriptions from the JSON config file
        return [(content['pattern'], content['description']) for content in json_content]

    def analyze_vulnerabilities(self, script_content):
        vulnerabilities = defaultdict(list)
        script_lines = script_content.splitlines()
        line_number = 1

        for line in script_lines:
            for pattern_data, description in self.regex_config:
                pattern = re.compile(pattern_data)
                matches = pattern.finditer(line)

                for match in matches:
                    start, end = match.span()
                    word = line[start:end]
                    vulnerabilities[description].append((line_number, word))

            line_number += 1

        return vulnerabilities

    def save_uploaded_script(self, file):
        script_path = f'scripts/{file.filename}'
        file.save(script_path)
        return script_path

    def analyze_script(self, script_path):
        with open(script_path, 'r') as script_file:
            script_content = script_file.read()
        vulnerabilities = self.analyze_vulnerabilities(script_content)

        output_file = f'output/analysis_result.json'
        result = {
            "vulnerabilities": vulnerabilities,
            "script_path": script_path,
        }
        with open(output_file, 'w') as json_output:
            json.dump(result, json_output, indent=4)

        return result

    def get_analysis_results(self):
        output_file = f'output/analysis_result.json'
        with open(output_file, 'r') as json_file:
            return json.load(json_file)
