from flask import Flask, render_template

app = Flask(__name__)

places = [
    {
        "name": "Rome",
        "description": "Cool place to visit with lots of history",
        "image": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=986&q=80"
    },
    {
        "name": "Texas",
        "description": "Second largest state in the Union. Home to many miles of road and bluebonnets",
        "image": "https://images.unsplash.com/photo-1459111461138-7dc2df20e792?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
    },
    {
        "name": "Alaska",
       
        "image": "https://images.unsplash.com/photo-1531884422565-1b4a26326a31?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
    }
]

@app.route('/')
def home():
    return render_template('home.html', heading='List of some cool places', places=places)

print('__name__', __name__)
if __name__ == '__main__':
    app.debug = True
    app.run()