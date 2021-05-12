from json import dumps
from flask import Flask, request, jsonify
import number_fun
import typing


APP = Flask(__name__)

port = 5000

url = f"http://127.0.0.1:{port}"


@APP.route('/multiply_by_two', methods=['GET'])
def multiply_by_two():

    number = request.args.get('number')
    
    result = number_fun.multiply_by_two(number)
    
    return dumps(result)
    
    
@APP.route('/print_message', methods=['GET'])
def print_message():

    message = request.args.get('message')
    
    result = number_fun.print_message(message)
    
       
    return dumps(result)


@APP.route('/sum_iterable_of_numbers', methods=['GET'])
def sum_iterable_wrapper(): 
    
    numbers = request.args.getlist('numbers')

    result = number_fun.sum_iterable_of_numbers(numbers)
    
    return dumps(result)



@APP.route('/sum_list_of_numbers', methods=['GET'])
def sum_list_wrapper():
    
    numbers = request.args.getlist('numbers')

    result = number_fun.sum_list_of_numbers(numbers)
    
    return dumps(result)

    
@APP.route('/is_in', methods=['GET'])
def is_in_wrapper():
    
    needle = request.args.get("needle")  
    haystack = request.args.getlist("haystack")
    
    result = number_fun.is_in(needle, haystack)
    
    
    return dumps(result)
    

 
@APP.route('/index_of_number', methods=['GET'])
def index_wrapper():
       
    item = request.args.get("item")
    numbers = request.args.getlist("numbers")
    
    result = number_fun.index_of_number(item, numbers)
    
    return dumps(result)


if __name__ == '__main__':
    APP.run(debug = True)

