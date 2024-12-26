# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 11:42:27 2024

@author: user
"""

import firebase_admin
from firebase_admin import db,credentials

if not firebase_admin._apps:
 cred = credentials.Certificate("test2024-310f6-firebase-adminsdk-jszf0-987303813f.json")
 firebase_admin.initialize_app(cred,{"databaseURL":"https://test2024-310f6-default-rtdb.firebaseio.com"})


  


#ref = db.reference("/")
# Update the database
#ref.update({"hello":999})
db.reference("/hello").get()
ttt = db.reference("/hello").get()
print(ttt)