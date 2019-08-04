**********************
Build and Deploy
**********************

Introduction
####################################################

This project does not consist in an application that is avalaible for end users, 
but rather the GitHub pages in which its presentation is stored:

* The aim of the Deploy step is to push the new version of the documentation online.
* The aim of the Build step is to check that everything is ok and produce the new
  version of the documentation.

Build steps: lint, test and make documentation 
####################################################

As the project is exclusively written in Python, no build per se is necessary for 
the code part. However, as it is good practice, some checks are mandatory before 
actually build the new version of the docs.

The real Build is when the Sphinx documentation is produced from .rst files, 
Jupyter Notebook and .py files.

Linting: running Flake8
***********************

The linter used on this project is `Flake8 <http://flake8.pycqa.org/en/latest/>`_.

The command to run it a simple one. Just open a command prompt, navigate 
to project folder root and run:
::

    flake8 --count

No warning or error should arise, a single `0` should be printed out.

Unit testing: running Pytest
****************************

Tests have to be written and run prior to any deployment to production. The 
package used on this project is `Pytest <https://docs.pytest.org/en/latest/>`_.

There is a little boilerplate I had to come to to make it work.

The folder structure of this project is the following:
::

    City pooling
    ├── src                     # src is where source code for packages is
    │   ├── geography
    │   │   ├── __init__.py
    │   │   └── geography.py
    │   ├── solver
    │   │   ├── __init__.py
    │   │   └── ...
    │   └── ...
    ├── test                    # tests are outside the src directory
    │   └── test_geography.py
    │   └── ...
    └── docs                    # all Sphinx files
        ├── build               # result of Sphinx build (documentation)
        │   ├── index.html
        │   ├── geography.html
        │   └── ...
        └── source              # where Jupyter notebook and .rst files are
