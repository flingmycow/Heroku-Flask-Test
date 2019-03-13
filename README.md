# Simple Heroku Flask Test

A very simple (and not finished) Flask app that is deployed on Heroku!

## Requirements

### Procfile
```web: gunicorn app:app```
Where the first `app` represents the name of the python file that runs your application or the name of the module it is in. The second `app` represents your app name.
- Ex. If your python file is called my_app.py and the Flask object is my_flask_app then your procfile string should say ```web: gunicorn my_app:my_flask_app```

### requirements.txt
A .txt file containing the Python packages required to run your Python app.

### runtime.txt
A .txt file containing the version of Python Heroku should run to execute your app.

### app.py and other files
Make sure you have 
```
if __name__ == '__main__':
    app.run(debug=True)
```

