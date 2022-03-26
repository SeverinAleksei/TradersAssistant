"""Flask app configuration."""
#from os import environ, path
#from dotenv import load_dotenv

#basedir = path.abspath(path.dirname(__file__))
#load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from environment variables."""

    FLASK_APP = 'wsgi.py'