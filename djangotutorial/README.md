### Premise 

The Tufts Bobsledding Society has a rich history of competing for the university at the highest level. To help them in their task of going to the olypmics, they've begun to develop an api to help manage their sleds and their team members. However, the bobsled team is understandably not tech savy and need your help to understand the current state of their api and extend it to their needs.
### Understand and Explore 

#### Set Up the Dev Environment
1. Clone Repo
    ```
    git clone 
    ```
2. Create an isolated virtual environment for you app and its dependencies.
    ```
    python3 -m venv env
    ```
3. Activate the virtual environment.
    ```
    source env/bin/activate
    ```
4. Install the app's dependencies within the scope of the virtual environment.
    ```
    pip install -r requirements.txt
    ```
5. Tell Django where to find the development settings by setting a specific environment variable.
    ```
    export DJANGO_SETTINGS_MODULE=djangotutorial.settings.dev
    ```
6. Change to main app directory.
    ```
    cd djangotutorial
    ```
##### Get a Local Database in Working Order and Add Dummy Data

5. Run the makemigrations command to see if the database schema needs to updated to reflect changes in the app's models.
    ```
    python manage.py makemigrations
    ```
3. Run the migrate command to do the actual converting of your data in the database to the new representation. This is how data can persist in the database even if the fundamental structure gets changed. The data must be migrated.
    ```
    python manage.py migrate
    ```
4. Now with the database structure set, and our old data now migrated to the new format, we can now load json data that reflects our models directly into our database. This is a great way for quickly re-populating a database with dummy data.
    ```
    python manage.py loaddata data.json
    ```
6. Navigate to [http:localhost:8000/api/sleds/](http:localhost:8000/api/sleds/) and see what response you get from the api for that route. Map the logic of handling the request by looking at urls.py for the route definition then views.py to see where the request gets passed to then serializers.py to see how django decides what data to present in the response returned. 

7. Create an admin account for the admin interface with `python manage.py createsuperuser`
8. Log in with the newly created user at [http://localhost:8000/admin/](http://localhost:8000/admin/), and add yourself as a Team member to a sled through the interface.
9. Hit the api url for all of the society's team members [http://localhost:8000/api/members/](http://localhost:8000/api/members/) again, and you should see yourself!
10. Its great to check and see that the route is working well, but what if we wrote some tests to that for us? Run `python manage.py test api` to run tests defined in api/test.py to double check all is well.

Now that we've got a decent understanding of what the api currently looks like, lets extend it!

### Extend

The existing Tuft's Bobsled Society works great, but is limited in functionality.

Specifically, bobsleds are expensive and the society needs to ramp up fundraising in order
to have enough money to make the trip to Sochi in 2020. 

The bobsled society leans on its extensive alumni network to crowdsource donations, and wants
to use its fancy django api to track donors and donations. 

They not only want to permanently store this information, they also want api calls to process new donations, list all donors, and then also see what teams have had the most fundraising.

The spec asks, at the very least, for:

1. A representation of a donation that allows you to optionally donate in the name of particular team.
2. A POST route to /api/donations/ that adds a new donation to the database.
3. A GET route to /api/donors/ that returns a list of donors in the database. 
4. A GET route to /api/donations/ that allows an optional query parameter in the request and returns a list of donations for each team.

#### Hints
* The null=True attribute on a field, allows the field to be optional (the value is set to null) in the database, but still can be set later after intitialization. null=False means the field must always have a non-null value. 
* If you want return only of a subset of instances of a model, the best way is to override the queryset or use a [filter](https://www.django-rest-framework.org/api-guide/filtering/).

### Extend-Extend 

The society is pleased with your work so far, but there's one 
critical issue with how things stand! The bobsled society doesn't want everyone to know about their donations information.

Lock down the api so that only accounts with valid authentication tokens can access them! 

Specifically at the very least:

* Use a token based authentication backend to protect the /donations and /donors routes from people not affliated with the society. A token authentication backend simply means a username and password pair are submited to and verified by, your application. If the credentials are valid, the client gets return a unique, secret string that can be used to identify themself in subsequent requests. With django, safetly generating and storing these paswords and tokens is largely done for you. So there's much authentication that you need to write yourself.  
* Use djangorestframework permission classes to restrict the routes based on the authorization token in a request's header.
* There also needs an api route for people to get an associated token that they can use by submitting a valid username and password to the server.

https://www.django-rest-framework.org/api-guide/authentication/#tokenauthentication