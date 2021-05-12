import datetime
import csv
from weather import weather

def test_doc():
    assert weather('08-08-2010', "Albury") == (10.8, -10.0)
    

def test_nonexistent_parameters():
    assert weather('01-01-2004', "UNSW") == (None, None)
    

def test_empty_location():
    assert weather('01-01-2004'," ") == (None, None)


def test_empty_parameters():
    assert weather(''," ") == (None, None)   

def test_nonexistent_date():
    assert weather('05-05-3000', "Albury") == (None, None)
