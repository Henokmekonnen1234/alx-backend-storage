#!/usr/bin/env python3
"""
This module will return all the data in the collection
"""

def list_all(mongo_collection):
    """ This methos will return all the data in mongo_collection

    Args:
        mongo_collection (object): mongo object

    Returns:
        list: return lists of datas
    """
    if mongo_collection.find() is None:
        return []
    else:
        return mongo_collection.find()
