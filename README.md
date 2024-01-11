# Shell Script Analyzer

The Shell Script Analyzer is a tool designed to analyze shell scripts for potential vulnerabilities and security issues. It identifies and reports vulnerabilities such as command injection, unsafe variable usage, and more.

## Features

- **Command Injection Detection**: Detects potential command injection vulnerabilities in shell scripts.

- **Unsafe Variable Usage Detection**: Identifies instances of unsafe variable usage where sensitive data may be exposed.

- **User-Friendly Web Interface**: Provides a user-friendly web interface for users to upload shell scripts and view analysis results.

- **JSON Output**: Generates JSON reports of the analysis results for further processing or integration with other tools.

- **Upload convenience**: Upload single shell script files or entire folders for analysis.

## Getting Started

Follow these instructions to get the project up and running on your local machine.

### Prerequisites

- Python 3.x
- Flask (Python web framework)

### Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/shell-script-analyzer.git
   
2. Change into the project directory:
cd ShellScriptAnalyzer

3. Create a virtual environment (optional but recommended):
   python -m venv venv
   
4. Activate the virtual environment:

    On Windows:
venv\Scripts\activate

5. Install project dependencies:
pip install -r requirements.txt

## Usage

### Analyzing Shell Scripts

1. Start the application:

   ```shell
   python main.py
   
2. Access the web interface in your browser at http://localhost:5000.

3. Upload a shell script file or entire folder to analyze.

4. View the analysis results, which will include detected vulnerabilities.

## Configuration

You can configure the regular expressions used for vulnerability detection by modifying the config/regex_config.json file.
