import configparser
import sys
import os

stroption = "test"
strkey = "username"


def get_keyvalue(stroption, strkey):
    config = configparser.ConfigParser()
    config.sections()
    path = cur_file_dir()
    print(path)
    confile = path + "\configure.cfg"
    config.read(confile)
#    config.read(r'F:\spotlightdev-autotesting\SpotlightDev-AutoTesting\downloadfromweb\configure.cfg')
    if stroption in config:
        if strkey in config[stroption]:
            data = config[stroption][strkey]
            print(data)
            return data
        else:
            print("option:" + stroption + "doesn't include the key ：" + strkey)
    else:
        print("Configure.cfg doesn't include option :" + stroption + strkey)


def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


