# Python Club - University of Ottawa

A Webapp built with the Django framework displaying information and events for the University of Ottawa Python Club.


# How to Run Locally

- Fork this repo
- Navigate to the root directory of the project
- <b>pip install -r requirements/development.txt</b>
- vim settings/dispatch.py
- Fill the blank on this line with your computer name `if '_______' in socket.gethostname():`
- <b>python manage.py migrate</b>
- Run the tests
- <b>py.test -v</b>
- Run <b>python manage.py runserver</b> to start the local server
- Visit <b>http://127.0.0.1:8000/</b> to view the running app
- Visit <b>http://127.0.0.1:8000/admin/</b> to log into the admin site (username: admin, pass: admin123)

# screenshots

![](./screenshot1.png)

![](./screenshot2.png)

![](./screenshot3.png)



# NOTES

Site built from template: https://startbootstrap.com/template-overviews/freelancer/

Django Tutorial: https://docs.djangoproject.com/en/1.10/intro/tutorial01/

Host Django on Google App Engine: https://cloud.google.com/python/django/appengine


# DEV NOTES

add twitter widget in contact section

add interactive python interpreter: http://www.skulpt.org/

add newsletter sign up form in contact section
