# install required packages
pip install django 
pip install djangorestframework 
pip install dj_database_url
pip install MySQL-python
pip install yolk
pip install funkload

# functional tests locally
cd ..
python manage.py test

# load tests, for server
cd tests
fl-run-bench test_load.py LoadTest.test_load


