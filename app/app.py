from flask import Flask, request, render_template, jsonify
from app.analyzer import ScriptAnalyzer
import os

app = Flask(__name__, template_folder='../templates', static_folder='../static')

class ShellScriptAnalyzerApp:
    def __init__(self):
        self.analyzer = ScriptAnalyzer()

    def configure_routes(self):
        @app.route('/', methods=['GET', 'POST'])
        def upload_file():
            if request.method == 'POST':
                file = request.files['file']
                if file:
                    script_path = self.analyzer.save_uploaded_script(file)
                    results = self.analyzer.analyze_script(script_path)
                    return render_template('results.html', results=results)
            return render_template('upload.html')

        @app.route('/results', methods=['GET'])
        def show_results():
            results = self.analyzer.get_analysis_results()
            return render_template('results.html', results=results)

