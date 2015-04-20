from Loader import Loader

class Parser:
    __count = 0
    
    def __init__(self, url):
        self.__data = Loader(url).load()
    
    def find_begin(self):
        for i in range(max(len(self.__data) // 6, 50), len(self.__data) - 200):
            try:
                if "Reference" == self.__data[i].split('"')[3]:
                    return i + 2
            except Exception:
                pass
        return 0
    
    def parse(self):
        i = self.find_begin()
        if i == 0:
            return 0
        while self.__data[i][:3] == "<li":
            self.__count += 1
            i += 1
        return self.__count
