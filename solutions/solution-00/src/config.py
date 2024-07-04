"""
This module exports configuration classes for the Flask application.

- DevelopmentConfig
- TestingConfig
- ProductionConfig

"""

from abc import ABC
import os
from datetime import timedelta


class Config(ABC):
    """
    Initial configuration settings
    This class should not be instantiated directly
    """

    DEBUG = False
    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configuration settings
    This configuration is used when running the application locally

    This is useful for development and debugging purposes.

    To check if the application is running in development mode, you can use:
    ```
    app = Flask(__name__)

    if app.debug:
        # Do something
    ```
    """

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "sqlite:///hbnb_dev.db")
    DEBUG = True

    JWT_SECRET_KEY = 'super-secret'  # Change this to your preferred secret key
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)  # Token expiration time


class TestingConfig(Config):
    """
    Testing configuration settings
    This configuration is used when running tests.
    You can enabled/disable things across the application

    To check if the application is running in testing mode, you can use:
    ```
    app = Flask(__name__)

    if app.testing:
        # Do something
    ```

    """

    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

    JWT_SECRET_KEY = 'super-secret'  # Change this to your preferred secret key
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)  # Token expiration time


class ProductionConfig(Config):
    """
    Production configuration settings
    This configuration is used when you create a
    production build of the application

    The debug or testing options are disabled in this configuration.
    """

    TESTING = False
    DEBUG = False

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://hbnbuser:hbnb@localhost/hbnb_prod"
    )

    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'super-secret-prod')  # Change this to your production secret key
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)  # Token expiration time for production