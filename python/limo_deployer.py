#!/usr/bin/python

import sys
import requests

def deploy(type, version_code, version_name, file_name):
    staging_url = 'http://stagingbackoffice.net/android'
    f = {'file': open(file_name)}
    param = {'type':type, 'version_code':version_code, 'version_name':version_name}
    r = requests.post(staging_url, data=param, files=f)
    print r

def main(argv):
    type = argv[1]
    version_code = argv[2]
    version_name = argv[3]
    file_name = argv[4]

    print str.format("deploy: {0}, {1}({2}), file: {3}", type, version_name, version_code, file_name)
    # deploy(type, version_code, version_name, file_name)

main(sys.argv)