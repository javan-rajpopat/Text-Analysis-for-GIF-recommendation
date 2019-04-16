from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('blog.html')


@app.route('/hello_world2', methods=["GET", "POST"])
def hello_world2():
    user_input = request.form['user_input']
    # output = shreya_func(user_input,score)
    output = ['http://webarchive.loc.gov/all/20150318155641/http://media.giphy.com/media/1000eGIbYHercI/giphy.gif',
              'http://webarchive.loc.gov/all/20150318155641/http://media.giphy.com/media/1000fHsBSKSL6w/giphy.gif']
    return render_template('blog2.html',output = output)


if __name__ == '__main__':
    app.run()
