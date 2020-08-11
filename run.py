## running the application created by web_app package

from web_app import app  #importing app instance from __init__.py of the package

if __name__ == '__main__':
    app.run(debug=True)