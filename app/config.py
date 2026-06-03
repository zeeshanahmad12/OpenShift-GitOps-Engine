import os

class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')

class DevelopmentConfig(Config):
    DEBUG = True

class StagingConfig(Config):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False

config = {
    'dev':     DevelopmentConfig,
    'staging': StagingConfig,
    'prod':    ProductionConfig,
    'default': DevelopmentConfig
}
