import yaml
import os


# @TODO : Change the logic to read the YAML configuration file from S3 using boto3 ?
class Configuration(dict):
    def __init__(self, file_name, env):
        self._env = env
        self._file_name = file_name
        if os.path.isfile(self._file_name):
            with open(self._file_name) as data:
                yaml_data = data.read()
            yaml_dict = yaml.load(yaml_data)[env]
            for key, value in yaml_dict.items():
                dict.__setitem__(self, key, value)
