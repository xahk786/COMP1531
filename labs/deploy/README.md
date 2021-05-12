## Lab09 - Exercise - Deploy (2 points)

In this lab exercise, you will write a very simple app, make sure it is type safe and then deploy to Microsoft Azure.

This may help you for the deployment aspect of your project in Iteration 3.

### Part 1 - Functionality

Complete the function definitions in `number_fun.py`. You will need use the `typing` module to put type checking on all of your function definitions- parameters and return values. Some tests to sanity check your code are in `numbers_test.py`, however these will not test whether your typing is correct.

### Part 2 - Flask Server and HTTP Tests

Write a flask server in `server.py` which has endpoints that call each of the functions in `numbers_fun.py`. All endpoints will be `GET` requests and you can choose the output format.

Write a few HTTP tests in `numbers_http_test.py`. Use a global variable to store the URL which you will later replace with the URL of your deployed server on the internet.

