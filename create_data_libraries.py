"""
Python script create_data_libraries

Created by Anne Pajon under user 'pajon01' on 14/03/2016

Install bioblend
$ virtualenv venv
$ source venv/bin/activate
$ pip install bioblend
$ python create_data_libraries.py
"""

from bioblend import galaxy
import os

gi = galaxy.GalaxyInstance('http://52.90.209.254/', 'f005d6227c38c3917610c6fdd8267aab')
lc = galaxy.libraries.LibraryClient(gi)

# Create training library every time from scratch
TRAINING_LIB_NAME = 'GalaxyCam Training'

training_lib = lc.get_libraries(name=TRAINING_LIB_NAME)
# Delete library
for l in training_lib:
    lc.delete_library(library_id=l['id'])
# create library
training_lib = lc.create_library(name=TRAINING_LIB_NAME, description='Data Libraries for Galaxy Training course')
print training_lib

# Create training library folders and sub-folders
FOLDERS = ['data_visualisation', 'getting_started', 'interval_operations', 'loading_data', 'workflows']

for f in FOLDERS:
    print f
    training_folder = lc.create_folder(library_id=training_lib['id'], folder_name=f)
    print training_folder

    for filename in os.listdir(os.path.join('data_libraries', f)):
        if os.path.isfile(os.path.join('data_libraries', f, filename)):
            print filename
            lc.upload_file_from_local_path(library_id=training_lib['id'], file_local_path=os.path.join('data_libraries', f, filename), folder_id=training_folder[0]['id'], dbkey='hg19')

    for path, subdirs, files in os.walk(os.path.join('data_libraries', f)):
        for subf in subdirs:
            print subf
            training_subfolder = lc.create_folder(library_id=training_lib['id'], base_folder_id=training_folder[0]['id'], folder_name=subf)
            print training_subfolder
            for filename in os.listdir(os.path.join('data_libraries', f, subf)):
                if os.path.isfile(os.path.join('data_libraries', f, subf, filename)):
                    print filename
                    lc.upload_file_from_local_path(library_id=training_lib['id'], file_local_path=os.path.join('data_libraries', f, subf, filename), folder_id=training_subfolder[0]['id'], dbkey='hg19')

