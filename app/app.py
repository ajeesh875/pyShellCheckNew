from flask import Flask, request, render_template, send_from_directory
import os
import json
from app.analyzer import ScriptAnalyzer

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

        @app.route('/download/<format>', methods=['GET'])
        def download_result(format):
            if format == 'html':
                html_filename = 'analysis_result.html'
                html_path = os.path.join('output', html_filename)
                html_content = render_template('results.html', results=self.analyzer.get_analysis_results())
                
                with open(html_path, 'w') as html_file:
                    html_file.write(html_content)

                return send_from_directory('../output', html_filename, as_attachment=True)
            
            elif format == 'json':
                json_filename = 'analysis_result.json'
                json_path = os.path.join('output', json_filename)
                json_content = self.analyzer.get_analysis_results()

                with open(json_path, 'w') as json_file:
                    json.dump(json_content, json_file, indent=4)

                return send_from_directory('../output', json_filename, as_attachment=True)

if __name__ == "__main__":
    app_instance = ShellScriptAnalyzerApp()
    app_instance.configure_routes()  
    app.run(debug=True)
