# pytest -moduleName myModule
# pytest -DirectoryName myDirectory
# pytest -k "expression"
# pytest -m "expression", uses "pytest.mark" decorator
# -v verbose, -q quiet, -s don't capture console output, --ignore, --maxfail

import pytest
from pyfrc.tests import *


def Sample_Test():
    assert True


def pytest_configure(config):
    config.addinivalue_line(
        "ExampleMark", "Params: mark test to run with params"
    )

@pytest.fixture()
def setup1():
    print("\nSetup 1")
    yield
    print("\nTeardown 1")


@pytest.fixture()
def setup2(request):
    print("\nSetup 2")
    
    def teardown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

def test1(setup1):
    print("Executing test1!")
    assert True

def test2(setup2):
    print("Executing test2!")
    assert True


####
@pytest.fixture(params=[1,2,3])
def setup_params(request):
    retVal = request.param 
    print("\nSetup Params! retVal = {}".format(retVal) )
    return retVal

@pytest.mark.Params
def testParams(setup_params):
    print("\nSetup = {}".format(setup_params) )
    assert True

###

if __name__ == '__main__': 
    pytest.main(['-v', '-s', __file__])
#pytest.main()
#pytest.main("-x mytestdir")
#pytest.main(['-x', 'mytestdir'])