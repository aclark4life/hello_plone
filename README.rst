Introduction
============

This is a Plone “Hello, World!” style tutorial/application for Python programmers. See: http://blog.aclark.net/2011/08/20/hello-plone/ for more.

Installation
------------

You can run "Hello, Plone!" like so::

    $ git clone git://github.com/aclark4life/hello_plone.git
    $ cd hello_plone
    $ virtualenv-2.7 .
    $ bin/pip install zc.buildout
    $ bin/buildout
    $ bin/plone fg

Now open http://localhost:8080/Plone/hello
