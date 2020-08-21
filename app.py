from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', heading='Thanks for watching')

print('__name__', __name__)
if __name__ == '__main__':
    app.debug = True
    app.run()