import yaml
import logging.config

with open("logging.yaml", "r") as file:
    yaml_dict = yaml.safe_load(file)
logging.config.dictConfig(yaml_dict)
