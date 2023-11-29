# analyzer.py

import os
import re
import json
from collections import defaultdict
from werkzeug.utils import secure_filename

class ScriptAnalyzer:
    def __init__(self):
        self.regex_config = self.load_regex_config()

    def load_regex_config(self):
        config_file = "config/regex_config.json"
        with open(config_file, 'r') as file:
            json_content = json.load(file)
        return [
            {
                "pattern": content['pattern'],
                "description": content['description'],
                "cve": content.get('cve'),
                "explanation": content.get('explanation'),
                "severity": content['severity']
            }
            for content in json_content
        ]

    def analyze_vulnerabilities(self, script_content):
        vulnerabilities = defaultdict(list)
        script_lines = script_content.splitlines()

        for line_number, line in enumerate(script_lines, start=1):
            for rule in self.regex_config:
                pattern = re.compile(rule["pattern"])
                matches = pattern.finditer(line)

                for match in matches:
                    start, end = match.span()
                    word = line[start:end]
                    vulnerability_data = {
                        "line_number": line_number,
                        "word": word,
                        "cve": rule["cve"],
                        "explanation": rule["explanation"],
                        "severity": rule["severity"]
                    }
                    vulnerabilities[rule["description"]].append(vulnerability_data)
        return dict(vulnerabilities)

    def save_uploaded_script(self, file):
        script_filename = secure_filename(file.filename)
        script_path = os.path.join('scripts', script_filename)
        file.save(script_path)
        return script_path

    def analyze_script(self, script_path):
        with open(script_path, 'r') as script_file:
            script_content = script_file.read()
        vulnerabilities = self.analyze_vulnerabilities(script_content)

        # Sort results based on severity (Critical, High, Medium, Low)
        sorted_results = sorted(
            vulnerabilities.items(),
            key=lambda x: max(item["severity"] for item in x[1]),
            reverse=True
        )

        result = {
            "vulnerabilities": dict(sorted_results),
            "script_path": script_path,
        }

        output_file = f'output/analysis_result.json'
        with open(output_file, 'w') as json_output:
            json.dump(result, json_output, indent=4)

        return result
