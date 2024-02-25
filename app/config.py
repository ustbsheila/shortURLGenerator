class Config:
    # Flask app configuration
    DEBUG = True  # Set to False in production

    # Database configuration
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://ustbsheila:12345@localhost:3306/shorturldb'  # Local development
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Host info is used to returned with complete shorten URL
    RUNNING_HOST = "http://localhost:8080"