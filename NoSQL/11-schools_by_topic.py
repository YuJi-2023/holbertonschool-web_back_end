#!/usr/bin/env python3
"""using pyMongo"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    my_query = {"topics": topic}
    my_list = mongo_collection.find(my_query)
    return my_list
