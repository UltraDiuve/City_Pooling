echo off

REM Pulling last version of code from repo
echo Pulling last version of code from repo
git pull origin master

REM Linting: running flake8
echo.
echo Running flake8...
echo.
flake8 --count

REM Testing: running pytest
echo.
echo Running pytest...
echo.
python -m pytest --cov

REM Building the docs: creating .rst files with apidoc
echo.
echo Running Sphinx apidoc...
echo.
rd /s /q .\docs\source\apidoc-build
sphinx-apidoc -o .\docs\source\apidoc-build\ .\src\ -d 1 --force^
 --module-first --separate --tocfile mods

REM Building the docs: building the html documentation
echo.
echo Running Sphinx to make the html sources...
echo.
docs\make html