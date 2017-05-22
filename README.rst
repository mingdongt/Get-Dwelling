GetDwelling
===========

An interactive web application providing live gathering, processing, visualisation and analysis on dwelling data in Melbourne during the period 2002-2016.

**Home**
.. image:: https://github.com/mingdongt/Get-Dwelling/blob/master/web_pages/Home.png
**Data Source Page**
.. image:: https://github.com/mingdongt/Get-Dwelling/blob/master/web_pages/Data%20source.png
**Data Analyze Page**
.. image:: https://github.com/mingdongt/Get-Dwelling/blob/master/web_pages/Data%20analyze.png
**Pivot Table PAge**
.. image:: https://github.com/mingdongt/Get-Dwelling/blob/master/web_pages/Pivot%20Table.png

Data source
-----------


Data collected as part of the City of Melbourne's Census of Land Use and Employment (CLUE). The data covers the period 2002-2016. The dwelling data is based on the Council's property rates database, using a simplified classification schema of Residential Apartment, House/Townhouse and Student Apartment. The count of dwellings per residential building is shown.

**New Column**

New column "Dwelling number class" got added to make it possible to classify records based on dwelling number class instead of unique values which are too many.

**File Format Transfer**

The original data file is transferred from csv format to hdf5 format to make it read fastest.

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html


Basic Commands
--------------


Running Locally With Docker
^^^^^^^^^^^^^^^^^^^^^^^^^^^
**Build the Stack**

This can take a while, especially the first time you run this particular command on your development system::

    $ docker-compose -f dev.yml build

**Boot the System**

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f dev.yml up

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html


