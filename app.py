from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '''
    <h1>🎉 Hello World from GitHub + OpenShift!</h1>
    <p>My LLM application is running!</p>
    <p>✅ Python Flask is working</p>
    <p>✅ Deployed from Git automatically</p>
    <p>✅ Ready for Oracle database integration</p>
    <p>🚀 Next step: Add LLM features!</p>
    '''

@app.route('/health')
def health():
    return {'status': 'healthy', 'message': 'Application is running!'}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
