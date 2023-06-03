import requests
import os
import json
from jsmin import jsmin

class Minify:

    dir = ""
    def __init__(self,folder):
        self.dir = folder



    def plzminify(self):
        total = 0
        for root, dirs, files in os.walk(self.dir):
            for file in files:
                if file.endswith(".js"):
                    path = root + "\\" + file
                    file = open(path,"r+",encoding="utf8")
                    if len(file.read()) > 0:
                        file.seek(0)
                        minified = jsmin(file.read())
                        file.truncate(0)
                        file.seek(0)
                        file.write(minified)
                    file.close()


            


Minify(".\cdn_static").plzminify()
