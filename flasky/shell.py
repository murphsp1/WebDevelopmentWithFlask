from flask.ext.script import Shell

def make_shell_context():
	return dict(app=app, db=db, User=User, Role=Role)
	manager.add_command("shell", Shell(make_context = make_shell_context))