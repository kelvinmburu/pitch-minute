from flask import Flask, render_template,url_for

app = Flask(__name__)

posts = [
    {'title':'kelvin blog',
     'author':'Jane Dode',
     'date_posted':'May 09, 2022'
     },
      {'title':'Jane blog',
     'author':'Kelvin Dode',
     'date_posted':'May 11, 2022'
     }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)



@app.route("/about")
def about():
    return render_template("about.html",title='About')

if __name__ == '__main__':
    app.run(debug=True)