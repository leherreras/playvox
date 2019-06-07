import importlib
import inspect
import pkgutil

from pymongo import MongoClient
from pymongo.errors import OperationFailure

from common.paths import MODELS_PATH
from common.utils import get_config
from models import MongoBase


class Storage:
    """
    DB connections main control
    """

    connections = {}

    def __init__(self, config):
        self.config = config

    def connect(self):
        """
        Load available models and create connections

        :return:
        """
        for key, value in self.config.items():
            self.connections[key] = MongoClient('mongodb://{user}:{passwd}@{host}:{port}/{}'.format(key, **value))

            try:
                self.connections[key].server_info()
            except OperationFailure as e:
                exit(str(e))

        for loader, path, is_pkg in pkgutil.walk_packages([MODELS_PATH], 'models.'):
            if not is_pkg:
                db = path.split('.')[-2]
                if db in self.connections:
                    for class_name, class_def in inspect.getmembers(importlib.import_module(path), inspect.isclass):
                        if issubclass(class_def, MongoBase) and class_def.collection_name:
                            setattr(self, class_def.collection_name, class_def(self.connections[db], db))

    def disconnect(self):
        """
        Disconnect all the available connections

        :return:
        """
        for connection in self.connections.values():
            connection.close()


storage = Storage(get_config()['MONGO'])
