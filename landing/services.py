from core.mongodb import db

def save_contact(data):
    """
    Save a contact form submission to MongoDB
    """
    collection = db["contacts"]
    collection.insert_one(data)

def get_contacts():
    """
    Retrieve all contacts
    """
    collection = db["contacts"]
    return list(collection.find())