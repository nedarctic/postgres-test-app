import sys
import os

# 1️⃣ Add your project folder to the Python path
sys.path.insert(0, '/home/justuski/repositories/postgres-test-app')

# 2️⃣ Set Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'postgres_test_project.settings'

# 3️⃣ Activate your virtual environment
activate_env = '/home/justuski/virtualenv/repositories/postgres-test-app/3.10/bin/activate_this.py'
with open(activate_env) as file_:
    exec(file_.read(), dict(__file__=activate_env))

# 4️⃣ Get Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
