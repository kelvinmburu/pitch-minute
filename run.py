from  flask_migrate import Migrate, MigrateCommand
from flask_script import Manager,Server
from flask_sqlalchemy import SQLAlchemy
from flaskblog import create_app

app = create_app()

manager = Manager(app)
manager.add_command('server', Server)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    app.run(debug=True)
    
