echo off

REM Pulling last version of code from repo
echo Pulling last version of code from repo
git pull origin master

REM Linting: running flake8
echo.
echo Running flake8. Error count:
flake8 --count

REM Testing: running pytest
echo.
echo Running pytest...
echo.
python -m pytest --cov

REM Building the docs: running Sphinx
echo.
echo Running Sphinx
echo.
docs\make html