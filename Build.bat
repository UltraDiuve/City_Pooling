REM Linting: running flake8
echo "Running flake8"
flake8 --count

REM Testing: running pytest
echo "Running pytest"
python -m pytest --cov

REM Building the docs: running Sphinx
echo "Running Sphinx"
docs\make html