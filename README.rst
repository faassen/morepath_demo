Morepath demo
=============

Demonstrating a Morepath app. To get running against development
version of Morepath, do the following in a virtualenv:

$ cd morepath_demo
$ python bootstrap.py
$ bin/buildout

This will get the Morepath and Reg sources, and other dependencies.

After this you can start up the demo app using:

$ bin/mpdemo

You can access the app on http://localhost:8080 after this.
