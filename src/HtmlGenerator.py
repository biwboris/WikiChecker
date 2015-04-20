class Generator:
    __begin = ['<!DOCTYPE html>',
               '<html>',
               '<head>',
               '<title>Wikipedia for P</title>',
               '</head>',
               '<body>']
    
    __end = ['</body>',
             '</html>']
    
    def __init__(self, count = 0, mas = []):
        self.__count = count
        self.__mas = mas
        self.__out = []
    
    def gen_ans(self):
        ans = []
        ans.append("In bs wiki are " + str(len(self.__mas)) + " pages with " + str(self.__count) + " external references, that is maximum<br>")
        for i in range(len(self.__mas)):
            elem = self.__mas[i]
            ans.append('<a href="' + elem + '">' + "page " + str(i) + "</a><br>")
        return ans
    
    def gen_out(self):
        html = open("Answer.html", "w")
        print('\n'.join(self.__begin + self.gen_ans() + self.__end), file = html)
        html.close()