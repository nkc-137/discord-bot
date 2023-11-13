import os

def get_asset_dir_path():
    return os.getcwd() + r"/assets/"

def get_asset_path(asset_name):
    return get_asset_dir_path() + asset_name