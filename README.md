Simple Mona
===========

This repo is the source code for the http://simplemona.com in its entirety.
This includes all Celery tasks for handling the PowerPool stratum mining servers
output.

Getting Started
===============

Simple Mona makes use of PostgreSQL and Redis, as well as RabbitMQ if you'll
be running a test powerpool instance for end to end testing. Setup is designed
to run on Debian Wheezy. If you're doing development you'll also want to install
Node since Grunt is used.

    # install dotdeb repo
    echo -e 'deb http://packages.dotdeb.org wheezy all\ndeb-src http://packages.dotdeb.org wheezy all' > /etc/apt/sources.list.d/dotdeb.list
    wget http://www.dotdeb.org/dotdeb.gpg
    sudo apt-key add dotdeb.gpg
    # rabbitmq repo
    echo 'deb http://www.rabbitmq.com/debian/ testing main' > /etc/apt/sources.list.d/rabbitmq.list
    wget http://www.rabbitmq.com/rabbitmq-signing-key-public.asc
    sudo apt-key add rabbitmq-signing-key-public.asc
    # and wheezy-backports if you have not already
    echo "deb http://ftp.us.debian.org/debian wheezy-backports main" >> /etc/apt/sources.list
    # then update and install services
    sudo apt-get update
    sudo apt-get install redis-server postgresql-contrib-9.1 postgresql-9.1 postgresql-server-dev-9.1 rabbitmq-server nodejs nodejs-legacy
    # install npm
    sudo curl --insecure https://www.npmjs.org/install.sh | bash

Now you'll want to setup a Python virtual enviroment to run the application in.
This isn't stricly necessary, but not using virtualenv can cause all kinds of 
headache, so it's *highly* recommended. You'll want to setup virtualenvwrapper 
to make this easier.

    # make a new virtual enviroment for simplemona
    mkvirtualenv sm
    # clone the source code repo
    git clone https://github.com/liliff/simplemona.git
    cd simplemona
    pip install -e .
    # install all python dependencies
    pip install -r requirements.txt
    pip install -r dev-requirements.txt
    # install nodejs dependencies for grunt
    sudo npm install -g grunt-cli  # setup grunt binary globally
    npm install  # setup all the grunt libs local to the project

Initialize an empty PostgreSQL database for simplemona.

    # creates a new user with password testing, creates the database, enabled
    # contrib extensions
    ./util/reset_db.sh
    # creates the database schema for simplemona
    python manage.py init_db

Now everything should be ready for running the server. This project uses Grunt
in development to watch for file changes and reload the server.

    grunt watch

This should successfully start the development server if all is well. If not,
taking a look at the webserver log can help a lot. Usually I have this running in a
separate console.

    tail -f webserver.log

It's also Usually I have this running in a
possible that gunicorn is failing to start completely, in which case you can run it
by hand to see what's going wrong.
    
    gunicorn simplecoin.wsgi_entry:app -p gunicorn.pid -b 0.0.0.0:9400 --access-logfile gunicorn.log
    
If you're running powerpool as well you'll need to start a celery worker to process
the tasks (found shares/blocks/stats etc) that it generates. You can run the worker
like this:
    
    python simplecoin/celery_entry.py -l INFO --beat

Contributing
============

If you are looking to contribute back to the original project, please fork the
original project at simplecrypto/simplecoin.

You should only send pull requests to this project if they are meant for 
simplemona.com and not for the simplecoin project in general. I will also be
merging upstream changes on a regular basis, so you can expect your changes to
be reflected back to this repo if accepted upstream. Feel free, however, to
send a pull request here if it is rejected upstream, and I'll consider it.
