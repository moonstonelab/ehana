import os
import configparser

config_str = """
[DEFAULT]
store = sqlite
sqlitefile = todo.db
csvfile = todo.csv
"""

_default_config_file = "config.ini"

def file_exists(file_path):
    return os.path.exists(file_path)

if file_exists(_default_config_file):
    config = configparser.ConfigParser()
    config.read(_default_config_file)
else:
    config = configparser.ConfigParser()
    config.read_string(config_str)

if os.environ.get("ehana_store"):
    config["DEFAULT"]["store"] = os.environ.get("ehana_store")
if os.environ.get("ehana_sqlitefile"):
    config["DEFAULT"]["sqlitefile"] = os.environ.get("ehana_sqlitefile")
if os.environ.get("ehana_csvfile"):
    config["DEFAULT"]["csvfile"] = os.environ.get("ehana_csvfile")
