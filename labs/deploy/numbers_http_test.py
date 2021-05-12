from json import dumps
import pytest
import flask
from flask import Flask
import requests
import json


import server


def test_multiply_two():
    data = {'number' : 5}
    
    resp = requests.get(server.url + '/multiply_by_two', params=data)
    load = resp.json()
    
    assert resp.status_code == 200
    assert load == 10

def test_message():
    data = {'message' : 'message'}
    
    resp = requests.get(server.url + '/print_message', params=data)
    load = resp.json()
    
    assert resp.status_code == 200
    assert load == 'message'

   
def test_sum_num():
    data = {'numbers' : [1,2,3]}
    
    resp = requests.get(server.url + '/sum_list_of_numbers', params=data)
    load = resp.json()
    
    assert resp.status_code == 200
    assert load == 6

   
def test_sum_iterable():
    data = {'numbers' : {1,2,3,4,5}}
    
    resp = requests.get(server.url + '/sum_iterable_of_numbers', params=data)
    load = resp.json()
    
    assert resp.status_code == 200
    assert load == 15


    
def test_isin():
    data = {'needle' : 3, 'haystack' : [1,2,3,4,5]}
    
    resp = requests.get(server.url + '/is_in', params=data)
    load = resp.json()
    
    assert resp.status_code == 200
    assert load 
    
   
       
