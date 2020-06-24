from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print "OK"; 
    return "Index page"

@app.route('/featurex')
def featurex():
    # implementation of featurex
    return "Feature x page"


if __name__ == '__main__':
    app.run()
