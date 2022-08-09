import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

# REFERENCE FOR THIS WHOLE FILE: 
# https://github.com/udacity/cd0037-API-Development-and-Documentation-exercises/blob/master/6_Final_Review/backend/flaskr/__init__.py

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE  

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  # Reference: https://flask-cors.readthedocs.io/en/1.10.0/
  cors = CORS(app, resources={r'/*': {'origins': '*'}})


  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
      response.headers.add("Access-Control-Allow-Headers", 
                          "Content-Type,Authorization,true")
      response.headers.add("Access-Control-Allow-Methods", 
                            "GET,PUT,POST,DELETE,OPTIONS")

      return response


  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  # References: 
  # https://knowledge.udacity.com/questions/578305
  # https://knowledge.udacity.com/questions/501641
  @app.route("/categories", methods=['GET'])
  def get_categories(): 
      selection = Category.query.all()
      current_categories = paginate_questions(request, selection)

      categories = Category.query.all()
      categories_dict = {}
      for category in categories: 
                  categories_dict[category.id] = category.type

      if len(current_categories) == 0:
          abort(404)

      return jsonify(
        {
          "success": True, 
          "categories": categories_dict,
          "total_categories": len(Category.query.all()),
        }
      )


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  # References: 
  # https://knowledge.udacity.com/questions/221888
  # https://knowledge.udacity.com/questions/578073
  # https://knowledge.udacity.com/questions/578305
  @app.route("/questions", methods=['GET'])
  def get_questions(): 
      selection = Question.query.order_by(Question.id).all()
      current_questions = paginate_questions(request, selection)
      
      categories = Category.query.all()
      categories_dict = {}
      for category in categories: 
                  categories_dict[category.id] = category.type

      if len(current_questions) == 0:
          abort(404)

      return jsonify(
        {
          "success": True, 
          "questions": current_questions,
          "total_questions": len(Question.query.all()),
          "categories": categories_dict,
          "current_category": None,
        }
      )



  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route("/questions/<int:question_id>", methods=["DELETE"])
  def delete_question(question_id):
      try:
          question = Question.query.filter(
                          Question.id == question_id).one_or_none()

          if question is None:
              abort(404)

          question.delete()
          selection = Question.query.order_by(Question.id).all()
          current_questions = paginate_questions(request, selection)

          return jsonify(
              {
                  "success": True,
                  "deleted": question_id,
                  "questions": current_questions,
                  "total_questions": len(Question.query.all()),
              }
          )

      except:
          abort(422)



  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route("/questions", methods=["POST"])
  def add_question():
        body = request.get_json()

        new_question = body.get("question", None)
        new_answer = body.get("answer", None)
        new_difficulty = body.get("difficulty", None)
        new_category = body.get("category", None)
        search = body.get("searchTerm", None)

        try:
            if search:
                selection = Question.query.filter(
                    Question.new_questions.ilike("%{}%".format(search))
                ).all()
                
                current_questions = paginate_questions(request, selection)

                return jsonify(
                    {
                        "success": True,
                        "questions": current_questions,
                        "total_questions": len(current_questions),
                    }
                )
            else:
                question = Question(
                      question=new_question, 
                      answer=new_answer, 
                      difficulty=new_difficulty,
                      category=new_category
                      )
                question.insert()

                selection = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, selection)

                return jsonify(
                    {
                        "success": True,
                        "created": question.id,
                        "questions": current_questions,
                        "total_questions": len(Question.query.all()),
                    }
                )

        except:
            abort(422)



  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''
  # Reference: https://knowledge.udacity.com/questions/566457
  @app.route("/questions/search", methods=["POST"])
  def search_questions():
      body = request.get_json()
      search = body.get("searchTerm", None)
      try:
          if search:
              selection = Question.query.order_by(Question.id).filter(
                  Question.question.ilike("%{}%".format(search))).all()
              
              current_questions = paginate_questions(request, selection)

              return jsonify(
                  {
                      "success": True,
                      "questions": current_questions,
                      "totalQuestions": len(selection),
                      "currentCategory": None,
                  })
      except:
          abort(404)



  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  # Reference: https://knowledge.udacity.com/questions/578305
  @app.route("/categories/<int:category_id>/questions", methods=['GET'])
  def get_question_by_category(category_id): 
      category = Category.query.filter_by(id = category_id).one_or_none()
      if category is None:
          abort(404)

      questions = Question.query.filter_by(category = str(category_id)).all()
      current_questions = paginate_questions(request, questions)
      if len(questions) == 0:
          abort(404)

      return jsonify(
        {
          "success": True, 
          "questions": current_questions,
          "total_questions": len(questions),
          "current_category": category.format(),
        }
      )



  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  # References: 
  # https://knowledge.udacity.com/questions/69090
  # https://knowledge.udacity.com/questions/78359
  @app.route("/quizzes", methods=['POST'])
  def play_quiz(): 
      try: 
          body = request.get_json()

          quiz_category = body.get('quiz_category', None).get('id')
          previous_questions = body.get('previous_questions', None)

          if quiz_category == 0: 
              quiz_questions = Question.query.filter(
                    Question.id.notin_(previous_questions)).all()
          else:
              quiz_questions = Question.query.filter(
                Question.id.notin_(previous_questions),
                Question.category == category_id).all()
          
          quiz_question = None
          if(quiz_questions):
              quiz_question = random.choice(quiz_questions)

          return jsonify({
              'success': True,
              'question': quiz_question.format()
          })
      except: 
            abort(422)



  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(404)
  def not_found(error):
      return (
          jsonify({
            "success": False, 
            "error": 404, 
            "message": "Resource not found"})
      ), 404

  @app.errorhandler(422)
  def unprocessable(error):
      return (jsonify({
          "success": False, 
          "error": 422, 
          "message": "Unprocessable"
      })), 422

  @app.errorhandler(400)
  def bad_request(error):
      return jsonify({
            "success": False, 
            "error": 400, 
            "message": "Bad request"
      }), 400

  @app.errorhandler(500)
  def server_error(error):
      return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal server error"
      }), 500

  return app

    