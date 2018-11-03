# SudoCode

This repository contains the code for the SudoCode airplane website, built using the Django web framework. To initiate the project:

    python3 -m pip install -r requirements.txt
    python3 -OO manage.py makemigrations
    python3 -OO manage.py migrate
    python3 -OO manage.py migrate --run-syncdb

After this, run

    python3 -OO manage.py airports

to fill the database with the latest airports.

Then, run:

    python3 -OO manage.py runserver

to start the site in DEBUG mode.

To run the server in shell mode, run:

    python3 -OO manage.py shell

# Production

In production, we will be using the "game" username. We will be using the nginx server software, and a custom systemd service called "sudocode" will be set up to run our gunicorn workers.

Use the start.sh, stop.sh and restart.sh files to manage the site service.
