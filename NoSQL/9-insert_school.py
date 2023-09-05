#!/usr/bin/env python3
"""using pyMongo"""
import sys


def insert_school(mongo_collection, **kwargs):
    """a function inserts a new document in a collection based on kwargs"""
    document = kwargs
    new_doc = mongo_collection.insert_one(document)
    return new_doc.inserted_id
