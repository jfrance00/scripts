import os


app_name = input("Name of the app: ")
app_path = input("Desired path of the app (C:users/julie/... or default to cwd)")

if not app_path:
    app_path = os.getcwd()

os.chdir(app_path)  #routes to desired path to open new app folder
os.mkdir('root')    # opens root directory for the app
os.chdir('root')


with open('wsgi.py', 'w') as f:
    f.write(f"""
from {app_name} import app

if __name__ == '__main__'
    app.run(debug=True)
""")

os.mkdir(app_name)   # creates app folder
os.mkdir(os.path.join(app_name, 'templates'))
os.mkdir(os.path.join(app_name, 'static'))

with open(os.path.join(app_name, "__init__.py"), 'w') as f:
    f.write(f"""
import flask

app = flask.Flask(__name__)

from . import views
""")

with open(os.path.join(app_name, 'views.py'), 'w') as f:
    f.write(f"""
from . import app

@app.route('/')
def index():
    return 'hello world'
""")

with open(os.path.join(app_name, 'templates/base.html'), 'w') as f:
    f.write(f"""
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{{ title }}</title>
  <meta name="author" content="">
  <meta name="description" content="">
  <meta name="viewport" content="width=device-width, initial-scale=1">
</head>

<body>
  <p>Hello, world!</p>

  <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
</body>
</html>
""")



