import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # Reference: https://github.com/udacity/cd0037-API-Development-and-Documentation-exercises/blob/master/6_Final_Review/backend/test_flaskr.py
    def test_get_paginated_questions(self):
        """ Tests that questions paginate correctly """
        res = self.client().get("/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(len(data["questions"]))


    def test_404_sent_requesting_beyond_valid_page(self):
        """ Tests that non-existent pages cannot be requested """
        res = self.client().get("/questions?page=1000", json={"difficulty": 1})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")


    def test_get_categories(self):
        """ Tests that Categories can be successfully retrieved """
        res = self.client().get("/categories")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["categories"])
        self.assertEqual(len(data["categories"]))


    def test_get_questions(self):
        """ Tests that Questions can be successfully retrieved """
        res = self.client().get("/categories/1/questions")
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["questions"])
        self.assertTrue(data["categories"])


    def test_delete_question(self):
        """ Tests that a question can be successfully deleted """
        res = self.client().delete('/questions/1')
        data = json.loads(res.data)

        questions = Question.query.filter(Question.id == 1).one_or_none()


        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(data['total_questions'])
        self.assertTrue(len(data['questions']))
        self.assertEqual(question, None)


    def test_add_new_question(self):
        """ Tests that a question can be successfully added """
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)
        

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_422_if_question_creation_fails(self):
        """ Tests for failure when adding new questions """
        res = self.client().post("/questions", json=self.new_question)
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data["message"], "Question creation failed")


    def test_search_questions(self):
        """ Tests that questions can be searched successfully """
        res = self.client().post("/questions", json={"searchTerm": "question"})
        data = json.loads(res.data)


        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data['questions'])
        self.assertIsNotNone(len(data["questions"]))
        

    def test_404_search_questions(self):
        """ Test for if the search yields no results """
        res = self.client().post("/questions", json={
                                    "searchTerm": "question"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "No matching results")

    
    def test_get_question_by_category(self):
        """ Tests that a question can be successfully retrieved by category """
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_questions'])
        self.assertTrue(data['current_category'])
        self.assertTrue(len(data['questions']))

    def test_404_get_question_by_category(self):
        """ Tests to see if category has no questions within """
        res = self.client().get('/categories/1/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Error: Category void of questions")
 


    def test_play_quiz(self):
        """ Tests that the quiz is providing questions properly """ 
        res = self.client().get('/quizzes', json={
                                'previous_questions': [],
                                'quiz_category': 
                                {'id': 7,
                                 'type': 'Science'}
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['quiz_question'])


    def test_404_play_quiz(self):
        """ Test for if the quiz cannot properly retrieve questions """
        res = self.client().get('/quizzes', json={
                                            'previous_questions': []})

        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Failed to retrieve quiz")



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()