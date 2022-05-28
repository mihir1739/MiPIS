# MiPIS
MiPIS (Missing Person Identification System) is an WebApp which can be used for tracking of missing people based on inputs from users. 

The backend is controlled by Django and Python. And uses MySQL for the database to store data. The face similiarity detection is backed by [Face++ API](https://www.faceplusplus.com/face-comparing/#demo). The SMS service used to notify the person is provided by [Vonage API](https://www.vonage.com/).The Face similiarity utilised is K-Means clustering.

The Front End is made through HTML/CSS and JS.The installation is simple as described as follows.

Features
--------
* Finds out a person based on image submited by the user and notifies the concerned authorities.
* Uses Face Recognition as well as Manual Approval before confirming a find claim by a user.
* User is notified through SMS about the whereabouts of the missing person through SMS message.
* A leaderboard of users based on persons correctly found by them!
Future Prospects/ Not Implemented features
------------------------------------------
* User side of the Website can be integrated to a mobile App.

Requirements
-------------
* MySQL needs to be configured with local setting in settings.py
* A Media directory needs to be created if not cloned dirctory. Should be at same level as templates. 
* Other libraries used are mentioned in `requirements.txt`

Installation
------------
* Add the `Server` file to your path.
* It is advised to create a virtual environment in python or use `source MyEnv/bin/activate` in the parent cloned directory the activate My Virtual Environment.
* Now install the required libraries by typing `pip install -r requirements.txt` to install them at once.
* Ensure that MySQL client is setup and running also the settings are properly configured in `settings.py`. If Using Arch linux install mariadb and start it by typing `systemctl start mariadb.service`.And create a database called MiPIS by `CREATE DATABASE MiPIS;`.
* Now at the same directory as `manage.py` run the server through Gunicorn.` gunicorn Server.wsgi` or `python manage.py runserver`. Whatever works out fine.
* Now you can open the WebApp in your LocalHost.

Online Hosted Version Availiable
-------------------------
The Webapp is also hosted here [MiPIS](http://mahakaal17.pythonanywhere.com/). But due to issues with free tier  of PythonAnywhere the face API Times out and gives undesirable issues so local version is preferred.

Thank You For Using Mipis.
