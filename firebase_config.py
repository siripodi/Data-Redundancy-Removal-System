import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("data-redundancy-removal-322ff-firebase-adminsdk-fbsvc-d45ff3bc5b.json")

firebase_admin.initialize_app(cred)

db = firestore.client()