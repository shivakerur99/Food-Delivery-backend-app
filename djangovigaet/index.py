import subprocess

# Define your commands
commands = [
    "python manage.py makemigrations",
    "python manage.py migrate",
    "python manage.py runserver"
]

# Execute each command sequentially
for cmd in commands:
    subprocess.run(cmd, shell=True)
