from bottle import route, run
from bottle import error
from bottle import static_file
from bottle import get, post, request, response
from bottle import route, abort, template, view, install
from bottle_sqlite import SQLitePlugin

install(SQLitePlugin(dbfile='test.db'))

@route('/show/<post_id:int>')
def show(db, post_id):
    c = db.execute('SELECT name, comment FROM comments WHERE post_id = ?', (post_id,))
    row = c.fetchone()
    return template('show_post', name=row['name'], comment=row['comment'])


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')

@route('/download/<filename:path>')
def download(filename):
    return static_file(filename, root='static/', download=filename)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

@route('/restricted')
def restricted():
    abort(401, "Sorry, access denied.")

@route('/iso')
def get_iso():
    response.charset = 'ISO-8859-15'
    return 'This will be sent with ISO-8859-15 encoding.'

@route('/latin9')
def get_latin():
    response.content_type = 'text/html; charset=latin9'
    return 'ISO-8859-15 is also known as latin9.'

@route('/test')
def test():
    return "test Hello World!"

@route('/hello')
def hello():
    return "Hello World!"

@route('/hello')
def hello_again():
    if request.get_cookie("visited"):
        return "Welcome back! Nice to see you again"
    else:
        response.set_cookie("visited", "yes")
        return "Hello there! Nice to meet you"


@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    response.set_cookie("username", username)    
    return template("<p>Welcome {{name}}! You are now logged in.</p>", name=username)
    #if check_login(username, password):
    #    response.set_cookie("account", username, secret='some-secret-key')
    #    return template("<p>Welcome {{name}}! You are now logged in.</p>", name=username)
    #else:
    #    return "<p>Login failed.</p>"

@route('/wiki/<page>')
def wiki(page):
    response.set_header('Content-Language', 'en')
    response.set_header('Set-Cookie', 'name=value')
    response.add_header('Set-Cookie', 'name2=value2')

@route('/hello')
@route('/hello/<name>')
@view('hello_template')
def hello(name='World'):
    return dict(name=name)



"""
Bottle runs on the built-in wsgiref WSGIServer by default. 
This non-threading HTTP server is perfectly fine for development and early production, 
but may become a performance bottleneck when server load increases.

The easiest way to increase performance is to install a multi-threaded server library like "paste" or "cherrypy" 
and tell Bottle to use that instead of the single-threaded server
"""

run(host='localhost', port=8080, debug=True, reloader=True, server='paste')




