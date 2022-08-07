# Full Stack API Final Project


## Full Stack Trivia

Full Stack Trivia is a project through Udacity that tasks students with building a trivia API that can:

1. Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer.
2. Delete questions.
3. Add questions and require that they include question and answer text.
4. Search for questions based on a text query string.
5. Play the quiz game, randomizing either all questions or within a specific category.

Premise: Udacity wishes to create bonding experiences for employees and students. Thus, Udacity has hired you to build a Trivia Api that the team and students can play during weekly meetings.

"Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others."
    -Udacity

## Pre-requisites and Local Development
To run this project, developers should have the following installed on their local machine: Python 3.7, pip, node, and npm. Further dependencies are required in both the frontend and backend directories.
### Python 3.7
This project is compatible with Python 3.7. Follow this [documentation](https://www.python.org/downloads/release/python-370/) to download Python 3.7 to your local machine. 

### Pip
Follow this [documentation](https://pip.pypa.io/en/stable/cli/pip_install/) to install pip on your local machine. 

### Node
Follow this [documentation](https://nodejs.org/en/) to install node on your local machine. 

### NPM (Node Package Manager)
Follow this [documentation](https://www.npmjs.com/) to install npm on your local machine. 

### Backend 
This project makes use of a virtual environment, which will need to be installed. Cd into the backend directory and follow the instructions found in this [documentation](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/) to install virtualenv. 

Once virtualenv is installed, create a virtual environment and activate it. Once in the virtual environment, run the following command to install the required dependencies: 
```
pip install -r requirements.txt
```

#### Key Dependencies
[Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

[SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

[Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.



### Frontend 
The /frontend directory in this project holds the package.json file. To install this file, simply open a terminal, cd into the frontend folder, and enter the command: 
```
npm install
```

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```
psql trivia < trivia.psql
```

Or if you are on Windows, run this instead: 
```
psql -d trivia -U db_owner -a -f trivia.psql
```

## Running The Server
Have two terminals open. Cd into the backend and activate the virtual environment. Be sure that you have followed the steps above to download the dependencies within the virtual environment. Enter the following commands into one of the terminals: 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
```
Now in the same terminal, cd into the frontend folder and enter:
```
flask run --reload
```
The server should start up and provide you with a localhost address. Now, in the second terminal, cd into the frontend/src folder and enter: 
```
npm start
```
After a few moments, the application should open in your browser. If it does not automatically open, enter [http://localhost:3000](http://localhost:3000)


## Testing
To run tests, enter the following commands into a terminal:
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```

or if you are on Windows:
```
drop database trivia_test
create database trivia_test
psql -d trivia_test -U db_owner -a -f trivia.psql
python test_flaskr.py
```