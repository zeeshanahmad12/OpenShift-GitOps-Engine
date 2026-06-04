import os


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')

    def get_debug(self):
        return self.DEBUG

    def get_secret(self):
        return self.SECRET_KEY


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
