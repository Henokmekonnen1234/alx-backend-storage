#!/usr/bin/env python3
"""
This module will insert data to school collection
"""

def insert_school(mongo_collection, **kwargs):
    """ This methos will insert data to school collecction from
        **kwargs
        """
    if mongo_collection.find() is None or kwargs is None:
        return []
    else:
        result = mongo_collection.insert_one(kwargs)
        return str(result.inserted_id)
