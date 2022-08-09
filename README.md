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
Have two terminals open. Cd into the /backend folder and activate the virtual environment. Be sure that you have followed the steps above to download the dependencies within the virtual environment. Enter the following commands into one of the terminals: 
```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run --reload
```

The server should start up and provide you with a localhost address. Running flask with the --reload flag will allow our API to automatically refresh any time that we make changes.

Now, in the second terminal, cd into the /frontend/src folder and enter: 
```
npm start
```
After a few moments, the application should open in your browser. If it does not automatically open, enter [http://localhost:3000](http://localhost:3000)


## API Reference

### Getting Started 
- Base URL: This application currently can only be run locally. The backend URL that we will be using is 'http://127.0.0.1:5000/'
- Authentication: This version of the application does not require authentication or API keys.


### Error Handling
This API returns 4 different error types: 
- 400: Bad Request
- 404: Resource Not Found
- 422: Not Processable
- 500: Internal Server Error


### Endpoints
#### GET /categories
- General: 
  - Returns a dictionary list of categories, success value, and total number of categories.
  - Results are paginated in groups of 10, though only 6 exist currently. 
  - Sample: 'curl http://127.0.0.1:5000/categories'
```
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true,
  "total_categories": 6
}
```

#### GET /questions
- General: 
  - Returns a list of all available questions, a success value, total number of questions, list of categories, and the current category. 
  - Results are paginated in groups of 10, if that many are available. 
  - Sample: 'curl http://127.0.0.1:5000/questions'
```
 "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```


#### DELETE /questions/<int:question_id>
- General: 
  - Deletes a selected question from the database permanently using its ID. 
  - Returns the ID of the deleted question, a success value, the updated list of questions, and the updated total number of questions. 
  - Sample: 'curl http://127.0.0.1:5000/questions/20 -X DELETE'
```
 "deleted": 20,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```


#### POST /questions
- General: 
  - Creates a new question using JSON parameters: question, answer, difficulty, category
  - Returns the ID of the created question, a success value, the updated questions list, and the updated number of questions
  - Sample: 'curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question": "What year did the United State land on the moon?", "answer": "1969", "difficulty": 2, "category": "4" }'

```
"created": 27,
  "questions": [
    { ... shortened, same response as above
    }
    "success": true,
    "total_questions": 19,
    }
```


#### POST /questions/search
- General: 
  - Uses a user-selected search term to find related questions in the list.
  - Returns a JSON object containing a success value, a paginated list of the current questions that match the search term, the total number of questions, and the current category.
  - Sample: 'curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "moon"}''

```
 "currentCategory": null,
  "questions": [
    {
      "answer": "1969",
      "category": 1,
      "difficulty": 3,
      "id": 25,
      "question": "What year did the United States land on the moon?"
    },
    {
      "answer": "1969",
      "category": 4,
      "difficulty": 2,
      "id": 27,
      "question": "What year did the United State land on the moon?"
    }
  ],
  "success": true,
  "totalQuestions": 2
}
```


#### GET /categories/<int:category_id>/questions
- General: 
  - Filters questions so they appear by category.
  - Returns a JSON object containing a paginated result of questions, a success value, the list of relevant questions, and the total number of questions. 
  - Sample: 'curl http://127.0.0.1:5000/categories/3/questions'
```
 "current_category": {
    "id": 3,
    "type": "Geography"
  },
  "questions": [
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "total_questions": 3
}
```

#### POST /quizzes
- General: 
  - The user selects a category and a list of random questions from that category are produced to begin the game.
  - Returns a JSON object only containing a success value and a singular, random question.
  - Sample: 'curl http://localhost:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions":[], "quiz_category":{"type":"Science","id":1}}''

```
  "question": {
    "answer": "Blood",
    "category": 1,
    "difficulty": 4,
    "id": 22,
    "question": "Hematology is a branch of medicine involving the study of what?"
  },
  "success": true
}
```




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