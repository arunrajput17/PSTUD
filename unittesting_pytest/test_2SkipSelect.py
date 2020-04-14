import mathlib_1
import pytest
import sys

def test_calc_total():
    total = mathlib_1.calc_total(4,5)
    assert total == 9

@pytest.mark.skipif(sys.version_info > (3,5), reason = 'Skipped test on the basis of condition')
def test_calc_multiply():
    result = mathlib_1.calc_multiply(10,3)
    assert result == 30

@pytest.mark.skip(reason='I dont want to run this test at the moment')
def  test_calc_subtract():
    sub_result = mathlib_1.calc_subtract(20,5)
    assert sub_result == 15

def test_dummy():
    assert True

###### Command to see the skipped test reson is pytest -v -rxs

#### Command to run selective test cases by the availability of some name like in this example we 
#### are running only those  test cases which contain 'total' in there name. 
####  pytest -k total
#### For mass summary pytest -k total -v


#### Custom markers #######

@pytest.mark.windows        ## here windows is custom marker and can be anything
def test_windows_1():
    assert True

@pytest.mark.windows   
def test_windows_2():
    assert True

@pytest.mark.mac            ## here mac is custom marker and can be anything
def test_mac_1():
    assert True

@pytest.mark.mac
def test_mac_2():
    assert True

### command to run is pytest -m mac -v
### command with condition if we want to run all other then mac is
### pytest -m "not mac" -v