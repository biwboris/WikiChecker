from src.Loader import Loader
from src.WikiParser import Parser
from src.HtmlGenerator import Generator

def main():
    url = "https://bs.wikipedia.org/wiki/Kategorija:Stranice_sa_istim_argumentima_kod_poziva_%C5%A1ablona"
    wiki = Loader(url).load()
    
    max_count = 0
    ans = []
    for k in range(9):
        mode = 1
        j = 0
        for i in range(155, len(wiki)):
            line = wiki[i]
            if mode == 1:
                if '<h2>\\xc4' == line[:8]:
                    mode = -2
            elif mode < 0:
                mode += 1
            else:
                j += 1
                count = Parser("https://bs.wikipedia.org" + line.split('"')[1]).parse()
                if count > max_count:
                    max_count = count
                    ans = [line.split('"')[1]]
                elif count == max_count:
                    ans.append(line.split('"')[1])
                if k != 8 and j == 200:
                    url = "https://bs.wikipedia.org" + line.split('"')[-4]
                    bug_ind = url.find("&amp")
                    wiki = Loader(url[:bug_ind + 1] + url[bug_ind + 5:]).load()
                    break
    Generator(max_count, ans).gen_out()

if __name__ == "__main__":
    main()