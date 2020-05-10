'''
import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
'''
import os
from app import create_app, db
# from app.models import User, Role
from flask_migrate import Migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run()


@app.shell_context_processor
def make_shell_context():
    return dict(db=db)
