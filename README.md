# Tech Challenge Python Senior
The challenge is to create a program that computes some basic statistics on a collection of small positive integers. You can assume all values will be less than 1,000.

The DataCapture object accepts numbers and returns an object for querying statistics about the inputs. Specifically, the returned object supports querying how many numbers in the collection are less than a value, greater than a value, or within a range. A code example is in the ``` main.py ``` file.

### Challenges conditions
- You cannot import a library that solves it instantly
- The methods ```add()```, ```less()```, ```greater()```, and ```between()``` should have 
constant time O(1)
- The method ```build_stats()``` can be at most linear O(n)
- Apply the best practices you know
- Share a public repo with your project

## Install project packages
To install the packages required to execute the project just run the command ```pip install -r requirements.txt``` in the root project folder.

## Run main file
To run the main file just run the command ```python main.py``` in the root project folder.

## Run project tests
To run the tests, first install the project pacakges and then run the command ```python -m pytest tests/``` in the root project folder.