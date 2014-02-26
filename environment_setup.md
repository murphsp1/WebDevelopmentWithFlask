cd to project root


    virtualenv venv

This setups the virtual environment named venv

     source venv/bin/activate

This runs the activate script, turning on the virtual environment. With Oh-My-ZShell, I see the following prompt:

    (venv)➜  WebDevelopmentWithFlask git:(master)

Now it is time to load up flask and install into the venv

    pip install flask


## Flask contexts that are available: ##

current_app (Application context) - the application instance for the active application
g (Application context) - a Python dictionary for the app for temporary storage during the handling of a request (reset with each request)
request [request context] - the request object that encapsulates the contents of a HTTP request sent by the client.
session [request context] - the user session, a dictionary that the app can use to store values that are remembered between requests.