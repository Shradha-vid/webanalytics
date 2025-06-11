from flask import Flask, request, render_template, make_response, session

app = Flask(__name__)


# ---------- Home Page ----------
@app.route('/')
def home():
    return render_template('home.html')


# ---------- GET Form ----------
@app.route('/loginget')
def login_get():
    return render_template('loginget.html')


@app.route('/loginresult')
def login_result():
    username = request.args.get('username')
    password = request.args.get('password')
    return f"""
        <h3>Received via GET:</h3>
            <h3>hello {username}</h3>
        <a href='/'>Go Home</a>
    """


# ---------- POST Form ----------
@app.route('/login', methods=['GET', 'POST'])
def login_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        return f"""
            <h3>Received via POST:</h3>
            <h3>hello {username}</h3>
            <a href='/'>Go Home</a>
        """
    return render_template('login.html')


# ---------- Query Parameter Example ----------
@app.route('/search')
def search():
    query = request.args.get('q', 'No query provided')
    return f"<h2>Search Results for: {query}</h2><br><a href='/'>Go Home</a>"


app.secret_key = 'mysecretkey'  # Needed for session, internally used by Flask to sign session cookies


# ---------- Cookie and session Example ----------

@app.route('/cookie-session')
def cookie_session_form():
    return render_template('cookie_session.html')


@app.route('/set-cookie-session', methods=['POST'])
def set_cookie_and_session():
    name = request.form['name']

    # Set cookie and session
    # make_response is used to create a response object
    resp = make_response(f"""
        <h3>Cookie & Session Set</h3>
        Cookie Value: {name}<br>
        Session Value: {name}<br>
        <a href='/show-cookie-session'>View Stored Values</a><br>
        <a href='/'>Go Home</a>
    """)
    # creating a new cookie
    resp.set_cookie('username', name)

    #creating a new session
    session['user'] = name
    return resp


@app.route('/show-cookie-session')
def show_cookie_and_session():

    # Retrieve cookie and session values if the cookie and session exist with the key 
    #'username' and 'user' or else return 'No cookie set' and 'No session set'
    
    cookie_val = request.cookies.get('username', 'No cookie set')
    session_val = session.get('user', 'No session set')
    return f"""
        <h3>Stored Values</h3>
        Cookie: {cookie_val}<br>
        Session: {session_val}<br>
        <a href='/'>Go Home</a>
    """


if __name__ == '__main__':
    app.run(debug=True)