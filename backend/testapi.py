from os import getenv
import unittest
import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from src.api import create_app
from src.database.models import setup_db, Movies, Actors

database_path = os.getenv("DATABASE_URI")
assistant = os.getenv("ASSISTANT")
director = os.getenv("DIRECTOR")
producer = os.getenv("PRODUCER")


class CastingAgencyTestCase(unittest.TestCase):

	def setup(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path = database_path
        self.db = setup_db(self.app, self.database_path)
        self.db.drop_all()
        self.db.create_all()	

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
        

    def tearDown(self):

        pass	


    def test_get_homepage_success(self):
        res = self.client().get('/')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_actors_success(self):
    	res = self.client().get('/actors')
    	data = json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['success'], True)


    def test_get_movies_success(self):
    	res = self.client().get('/movies')
    	data = json.loads(res.data)

    	self.assertEqual(res.status_code, 200)
    	self.assertEqual(data['success'], True)


    def test_get_actor_success(self):
        res = self.client().get('/actors/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_movie_success(self):
        res = self.client().get('/movies/1')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_actors_detail_success(self):
        res = self.client().get('/actors-detail',json={},
            headers={'Authorization': f'Bearer {assistant}'})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_movies_detail_success(self):
        res = self.client().get('/movies-detail',json={},
            headers={'Authorization': f'Bearer {assistant}'})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_actor_detail_success(self):
        res = self.client().get('/actors/1/detail',json={},
            headers={'Authorization': f'Bearer {director}'})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_actor_detail_fail(self):
        res = self.client().get('/actors/1/detail',json={},
            headers={'Authorization': f'Bearer {assistant}'})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    def test_get_movie_detail_success(self):
        res = self.client().get('/movies/1/detail',json={},
            headers={'Authorization': f'Bearer {director}'})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_get_movie_detail_fail(self):
        res = self.client().get('/movies/1/detail',json={},
            headers={'Authorization': f'Bearer {assistant}'})

        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)


    