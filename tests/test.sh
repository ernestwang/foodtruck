# install required packages
pip install yolk
pip install funkload

# functional tests
fl-run-test test_load.py


# load tests
fl-run-bench test_load.py LoadTest.test_load


