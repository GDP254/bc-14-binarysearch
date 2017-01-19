# Binary Search Andelab

Solution to the following assignment.

First, you are to create a BinarySearch class, that inherits from the list class the following:

the __init__() takes two integers as parameters, a and b. a is the length of the list to be created and b is the step or difference between consecutive values. It should also initialize an instance variablelength`, that returns the number of elements in the array

Once you are done, create another method called search, it will take just one argument which is the value you are to find. The search function should return a dictionary object, which contains

count, the number of times you function iterated to find the index of the number in question index, the index of the number in question

The search method should implement the binary search algorithm, each time you iterate, you should increase the count, to test how efficient your implementation is.

python version: 2.7.12

Requirements: pytest 3.0.5

If you have pytest installed simply run pytest else use the following command from within this directory to install it before doing so:

pip install -r requirements.txt

If you would like to run without pytest simply run the file suffixed with _test