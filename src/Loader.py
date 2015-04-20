import urllib.request

class Loader:
    def __init__(self, url):
        self.__url = url
    
    def load(self):
        loaded = list(map(str, urllib.request.urlopen(self.__url).readlines()))
        for i in range(len(loaded)):
            loaded[i] = loaded[i][2:-3]
        return loaded
    
    def get_url(self):
        return self.__url
