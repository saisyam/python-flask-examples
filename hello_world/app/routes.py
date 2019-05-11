from app import app

@app.route('/')
@app.route('/index')
def index():
    return '''
        <html>
            <head>
                <title>Hello! World</title>
            </head>
            <body>
                <h1>Hello! World</h1>
            </body>
        </html>
    '''