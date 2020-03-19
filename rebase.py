from pathlib import Path
import pyrebase
import time
config = {
    "apiKey": "AIzaSyCsRnBbJru3Jg5crfEkJnpvFvSlzWJatWc",
    "authDomain": "intuderdetector.firebaseapp.com",
    "databaseURL": "https://intuderdetector.firebaseio.com",
    "projectId": "intuderdetector",
    "storageBucket": "intuderdetector.appspot.com",
    "messagingSenderId": "834194595303",
    "appId": "1:834194595303:web:d5bcdd3c6de997f7f7f142
}
folder_name = time.strftime("%d-%m-%Y")
file_name = time.strftime("%H:%M")
Path(file_name+'.jpg').touch()
print(file_name+' '+ folder_name + ' was sucessfully uploaded')
prath = pyrebase.initialize_app(config)
storage = prath.storage()
path_cloud = folder_name+"/"+file_name+".jpg"
path_local = file_name+'.jpg'
storage.child(path_cloud).put(path_local)

