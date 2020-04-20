class BaseConfig(object):
    DEBUG = True
    DEVELOPMENT = True
    HOST = "127.0.0.1"
    PORT = 5000
    SEND_FILE_MAX_AGE_DEFAULT = 0


class BackendConfig(BaseConfig):
    PORT = 5000

class FrontendConfig(BaseConfig):
    PORT = 5001