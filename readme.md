#ARPixelSite Backend

**This Project consists of a set of serialized API endpoints for the website dashboard of ARPixel app.**

**Note:** This project uses a **MySql** database and a MySql server needs to be running.
If you want to use **sqlite3**, change the database settings in settings.py.

To run the Django server and use the **Django Rest Framework (DRF)** browsable API on a web browser,

1. `sudo /etc/init.d/mysql start` to start MySQL server
2. `mysql -u root -p` login as root and create a new user
3. `CREATE DATABASE dbname;` to create a database for the Django app
3. `CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'password';` to create new user
4. `GRANT ALL PRIVILEGES ON dbname . * TO 'newuser'@'localhost';` to grant permissions
5. Edit the database settings in the `settings.py` file to reflect the above changes.
6. Create a **Python3** virtual env
   `virtualenv -p python3 envname`
7. Activate the virtual env
   `source envname/bin/activate` if envname is in current directory.
8. Change into the ARPixelSite directory
   `cd ARPixelSite`
9. Install requirements and dependencies (some of them might not be essential and can be deleted from the requirements.txt file especially if errors occur)
	`pip install -r requirements.txt`
10. make migrations
   `python manage.py makemigrations`
11. migrate
   `python manage.py migrate`
12. Create a superuser
   `python manage.py createsuperuser`
13. Start the server
   `python manage.py runserver`
14. Visit `127.0.0.1:8000/admin` on your web browser and create some users to start with
15. Visit `127.0.0.1:8000` to login and start using the DRF's browsable API
16. After authentication, you can upload Image Targets, 3D Object Targets and Text Targets.

There are two apps

1. **authenticateclients**

- `authenticateclients` handles the authentication of the client uploaders.
It has a `UploaderClient` model which is a `OneToOne` relationship with the Django `User` model.
Having such a model provides the advantage of flexibilty in creating custom attributes for the uploader client.
(The uploader client is the one who will be using the website to upload his advertising needs)
The `username/accountname` is used as username in this model.
- Then there is a `UploaderClientSerializer` which inherits from the DRF's `HyperlinkedModelSerializer`.
This is used for serializing data into `JSON` and for deserializing back from JSON.
The frontend will be interacting with the backend using this format.
The create and update of CRUD have been overridden to suit the UploaderClient model's needs.
- `Class based views` have been used.
Since DRF's browsable API is used for testing this project, the views are very basic and suffice to test the API endpoints.
There are two views - one view `lists` all the current UploaderClients and another displays the `details` of the selected UploaderClient. There has been heavy usage of DRF"s `hyperlinking` and one can easily navigate the browsable API via the links.
The users have to be created via Django's `admin` interface and a view has not been made for it.
But once users have been created, they can upload and modify targets.
- To see list of all UploaderClients ( only if you are superuser ) , visit `127.0.0.1:8000/uploaderclient/`
To see detail of an individual UploaderClient ( if you are authenticated ) , visit `127.0.0.1:8000/uploaderclient/<id>/`
- `Permissions` to view and access different parts of the API and permissions for not safe methods like `DELETE` have been created.

2. **clientupload**

- `clientupload` handles the uploading of relevant data by authenticated UploaderClients.
There are three models `ImageTarget`, `Object3DTarget` and `TextTarget` corresponding to each type of object that the mobile app is expected to recognize. All the three models have `ForeignKey` relationship with the UploaderClient who uploads them. Each model has its save and delete methods to override the default ones.
- The files will be uploaded in the `media` directory under appropriate subdirectories.
Care has also been taken that the targets on being DELETED will be removed from the filesystem.
- There are `three serializers` corresponding to each model.
It converts data into JSON and converts back data from JSON. The serializers inherit from DRF's `HyperlinkedModelSerializer` and provide extensive `hyperlinking` between instances of the different classes.
A create method of CRUD has been written to suit the needs of the three models.
The serializers also `associate` the currently logged in UploaderClient to the uploaded content.
- `Class based views` have been used here again.
There are three views which `list` all the targets of the corresponding model uploaded by the logged in UploaderClient. There are three other views which provide `details` of each of the uploads.
- To view the list of image targets, visit `127.0.0.1:8000/imagetarget/` and for viewing the details of an imagetarget, visit `127.0.0.1:8000/imagetarget/<id>/` . Similar for Object3DTargets and TextTargets Hyperlinking has been provided everywhere. Also note that views have corresponding permissions which have to be satisfied in order to access them.
One can `modify` a preexisting upload by visiting its detailed view and having requisite permissions.
One can `add` a new upload by visiting the list of targets view.
- `Permissions` have been created to access various views and to restrict access to dangerous methods like DELETE.



One can always use the `admin` interface for everything. Care has been taken to provide appropriate permissions. One more feature about this project is that one can always use the `Django CMS app` if one wishes and one just needs to tweak around a bit in the settings.py to enable its use.
A complete generator for a **RESTful API** based backend has been created.








