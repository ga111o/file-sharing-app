from flask import Flask, send_file, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    html = '''
    <!doctype html>
    <title>test</title>
    <a href="/download"><button>click here!</button></a>
    '''
    return render_template_string(html)

@app.route('/download')
def download_file():
    path = "source.zip"
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
