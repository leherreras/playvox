import os
import pkgutil
import uuid

import yaml

from common.paths import CONFIG_PATH


def get_config():
    """
    Parses configuration file

    :return:
    """
    with open(os.path.join(CONFIG_PATH, 'config.yml'), 'r') as f:
        cfg = yaml.load(f, Loader=yaml.BaseLoader)
    return cfg