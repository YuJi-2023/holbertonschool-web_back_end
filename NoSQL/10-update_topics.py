#!/usr/bin/env python3
"""using pyMongo"""


def update_topics(mongo_collection, name, topics):
    """a function changes all topics of a school document based on the name"""
    my_query = {"name": name}
    new_topics = {"$set": {"topics": topics}}
    mongo_collection.update_many(my_query, new_topics)
