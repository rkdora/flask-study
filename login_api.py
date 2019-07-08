from flask import Flask, render_template
import flask

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/mypage')
def mypage():
    # login = True
    login = False
    if login is False:
        return flask.jsonify({
            "code" : 400,
            "msg"  : "Bad Request"
        })

    user_data = {"user_name": "ryuto"}
    return flask.jsonify({
        "code" : 200,
        "msg"  : "OK",
        "result": user_data
    })

if __name__ == '__main__':
  app.run(port=8000, debug=True)
