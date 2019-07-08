from flask import Flask, session, redirect, url_for, request, render_template, send_from_directory

app = Flask(__name__)

@app.route('/login')
def index():
    return "success"


@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] and request.form['password']:
            return redirect(url_for('index'))
        else:
            return render_template('login.html')

    return render_template('login.html')

if __name__ == '__main__':
    app.run(port=12345, debug=False)
