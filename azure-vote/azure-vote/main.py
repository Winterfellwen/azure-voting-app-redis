from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_vm')
def get_vm():
    result = subprocess.run(['pwsh', '-c', 'Connect-AzAccount; Get-AzVM'], capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return f"Error: {result.stderr}"

if __name__ == '__main__':
    app.run()
