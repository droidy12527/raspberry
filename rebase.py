from pathlib import Path
import pyrebase
import time
config = {
    "apiKey": "AIzaSyC-qt2eSGN9MolkfLHhU8DKmLXFPnMpuNg",
    "authDomain": "intruderdetector-a5506.firebaseapp.com",
    "databaseURL": "https://intruderdetector-a5506.firebaseio.com",
    "projectId": "intruderdetector-a5506",
    "storageBucket": "intruderdetector-a5506.appspot.com",
    "messagingSenderId": "136524713787",
    "appId": "1:136524713787:web:a82bfb6f69f09e5d37b11e",
    "measurementId": "G-Y5GXZ7BVHV"
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

