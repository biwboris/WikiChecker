import urllib.request

class Loader:
    def __init__(self, url):
        self.__url = url
    
    def load(self):
        return urllib.request.urlopen(self.__url).readlines()
    
    def get_url(self):
        return self.__url