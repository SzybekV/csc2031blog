import secrets

from flask import Flask
from blog.views import blog_blueprint
from main.views import main_blueprint
from users.views import users_blueprint

app = Flask(__name__)

app.config['SECRET_KEY'] = secrets.token_hex(16)

app.register_blueprint(blog_blueprint)
app.register_blueprint(main_blueprint)
app.register_blueprint(users_blueprint)

if __name__ == '__main__':
    app.run()
