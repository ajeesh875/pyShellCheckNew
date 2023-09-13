from app.app import app, ShellScriptAnalyzerApp
import os

if __name__ == "__main__":
    app_instance = ShellScriptAnalyzerApp()
    app_instance.configure_routes()
    app.run(debug=True)  # Use the 'app' object to run the Flask application
