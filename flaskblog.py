from flask import Flask, render_template,url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'acd6b60c667a94557bce0aec3c409354'

posts = [
    {'author':'Kelvin Mburu',
     'title':'Blog Post 1',
     'content':'First Post Content',
     'date_posted':'May 09, 2022'
     },
      {'author':'Kelvin Doe',
     'title':'Blog Post 2',
     'content':'Second Post Content',
     'date_posted':'May 19, 2022'
     }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)



@app.route("/about")
def about():
    return render_template("about.html",title='About')


@app.route("/register")
def register():
    form = RegistrationForm()
    
    return render_template("register.html", title='Register',form=form)

@app.route("/login")
def login():
    form = LoginForm()
    
    return render_template("login.html", title='Login',form=form)

if __name__ == '__main__':
    app.run(debug=True)