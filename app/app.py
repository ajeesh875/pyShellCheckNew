from flask import Flask, request, render_template, send_from_directory
import os
from werkzeug.utils import secure_filename
from app.analyzer import ScriptAnalyzer
import json
import tempfile

app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config['UPLOAD_FOLDER'] = 'uploads'

class ShellScriptAnalyzerApp:
    def __init__(self):
        self.analyzer = ScriptAnalyzer()

    def configure_routes(self):
        @app.route('/', methods=['GET', 'POST'])
        def upload_file_or_folder():
            if request.method == 'POST':
                selected_action = request.form.get('selectedAction')

                if selected_action == 'folder':
                    # Handle folder
                    folder_path = tempfile.mkdtemp(dir=app.config['UPLOAD_FOLDER'], prefix='uploaded_folder_')

                    # Save all files from the uploaded folder
                    for uploaded_file in request.files.getlist('file_or_folder'):
                        if uploaded_file.filename:
                            file_path = os.path.join(folder_path, secure_filename(uploaded_file.filename))
                            uploaded_file.save(file_path)

                    # Analyze the folder
                    results = self.analyze_folder(folder_path)
                    return render_template('results.html', results=results)

                else:
                    # Handle multiple files
                    files = request.files.getlist('files[]')

                    results = []

                    for file_or_folder in files:
                        if file_or_folder.filename:
                            script_path = self.analyzer.save_uploaded_script(file_or_folder)
                            result = self.analyzer.analyze_script(script_path)
                            result['filename'] = file_or_folder.filename
                            results.append(result)

                    return render_template('results.html', results=results)

            return render_template('upload.html')

        @app.route('/results', methods=['GET'])
        def show_results():
            results = self.analyzer.get_analysis_results()
            return render_template('results.html', results=results)

        @app.route('/download/<format>', methods=['GET'])
        def download_result(format):
            results = self.analyzer.get_analysis_results()
            if format == 'html':
                html_filename = 'analysis_result.html'
                html_path = os.path.join('output', html_filename)
                html_content = render_template('results.html', results=results)
                
                with open(html_path, 'w') as html_file:
                    html_file.write(html_content)

                return send_from_directory('../output', html_filename, as_attachment=True)
            
            elif format == 'json':
                json_filename = 'analysis_result.json'
                json_path = os.path.join('output', json_filename)
                json_content = results

                with open(json_path, 'w') as json_file:
                    json.dump(json_content, json_file, indent=4)

                return send_from_directory('../output', json_filename, as_attachment=True)

    def analyze_folder(self, folder_path):
        shell_script_results = []
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path) and file_path.lower().endswith(('.sh', '.bash', '.zsh')):
                result = self.analyzer.analyze_script(file_path)
                result['filename'] = filename
                shell_script_results.append(result)
        return shell_script_results

if __name__ == "__main__":
    app_instance = ShellScriptAnalyzerApp()
    app_instance.configure_routes()
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
