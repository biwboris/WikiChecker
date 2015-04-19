from Loader import Loader

def main():
    url = "https://bs.wikipedia.org/wiki/Kategorija:Stranice_sa_istim_argumentima_kod_poziva_%C5%A1ablona"
    html = Loader(url).load()
    
main()