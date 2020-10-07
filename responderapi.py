#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Responder API
Checking out K.R.'s Responder library. Requires '$ pip install responder'
"""

import responder
import random

insults = [
    "Everyone who ever loved you was wrong.",
    "You're not pretty enough to be this stupid.",
    "You are depriving some village somewhere of an idiot.",
    "I'm jealous of all the people that haven't met you.",
    "I don't have the time or the crayons to explain this to you.",
    "I'm not as stupid as you look.",
    "Your parents are disappointed in you.",
    "I'd agree with you, but then we'd both be wrong.",
    "Your birth certificate is an apology letter from the condom factory.",
    "Are your parents cousins?",
    "If you were twice as smart as you are, you'd be half as smart as you think you are."
]

api = responder.API()


@api.route('/')
def index(req, resp):
    resp.content = 'Simple API examples with Responder'


@api.route('/api/search/{keyword}')
def search_by_keyword(req, resp: responder.Response, keyword: str):
    resp.media = {'Searching': keyword}


@api.route('/api/director/{director_name}')
def search_by_director(req, resp: responder.Response, director_name: str):
    resp.media = {'Director': director_name}


@api.route('/api/movie/{imdb_number}')
def movie_by_imdb(req, resp: responder.Response, imdb_number: str):
    resp.media = {'Movie IMDB': imdb_number}


@api.route('/api/insult/')
def get_insult(req, resp: responder.Response):
    insult = random.choice(insults)
    resp.media = {'Insult': insult}


api.run()
