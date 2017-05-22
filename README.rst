GetDwelling
===========

An interactive web application providing live gathering, processing, visualisation and analysis on dwelling data in Melbourne during the period 2002-2016.

**Home**

.. image:: https://github.com/mingdongt/Get-Dwelling/blob/master/web_pages/Home.png

**Data Source Page**

.. image:: https://github.com/mingdongt/Get-Dwelling/blob/master/web_pages/Data%20source.png

**Data Analyze Page**

.. image:: https://github.com/mingdongt/Get-Dwelling/blob/master/web_pages/Data%20analyze.png

**Pivot Table Page**

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


Getting Up and Running Locally With Docker
--------------

The steps below will get you up and running with a local development environment. All of these commands assume you are in the root of project.

Prerequisites
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You’ll need at least Docker 1.10.

If you don’t already have it installed, follow the instructions for your OS:

On Mac OS X, you’ll need Docker for Mac_.

On Windows, you’ll need Docker for Windows_.

On Linux, you’ll need docker-engine_.

.. _Mac: https://docs.docker.com/docker-for-mac/#check-versions-of-docker-engine-compose-and-machine

.. _Windows: https://docs.docker.com/docker-for-windows/

.. _docker-engine: https://docs.docker.com/engine/installation/


1. Build the Stack
^^^^^^^^^^^^^^^^^^^^^^^^^^^

This can take a while, especially the first time you run this particular command on your development system::

    $ docker-compose -f dev.yml build


2. Boot the System
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Open a terminal at the project root and run the following for local development::

    $ docker-compose -f dev.yml up

3. Run the application
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that the server’s running, visit http://127.0.0.1:8000/ with your Web browser.
