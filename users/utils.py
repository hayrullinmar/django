import os
from django.core import management
import bz2
from io import BytesIO
import sys

# old_stdout = sys.stdout
# sys.stdout = mystdout = StringIO()
# def dump_custom
filename = 'fixtures/users/users.json'
if not os.path.exists(os.path.dirname(filename)):
    os.makedirs(os.path.dirname(filename))

with open(filename, 'w+', buffering=1024) as f:
    management.call_command('dumpdata', 'users', indent=4, stdout=f)

# with bz2.BZ2File('users.json.bz2', 'w', buffering=1024) as file:
#     out = BytesIO()
#     management.call_command('dumpdata', 'users', indent=4, stdout=out)
#     file.write(out)

# sys.stdout = old_stdout
print("ok")

