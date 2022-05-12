from flaskblog import create_app, db
from flask_script import Manager, Server
from flaskblog.models import User,Post
from flask_migrate import Migrate, MigrateCommand

app = create_app()
manager = Manager(create_app)
manager.add_command('server',Server)

migrate = Migrate(create_app,db)


@manager.shell
def make_shell_context():
    return dict(create_app = create_app,db = db,User = User, Post=Post )

manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    manager.run()
    
