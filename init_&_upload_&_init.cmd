:python setup.py sdist bdist_wheel
:twine upload dist/*
python worker.py
pause