import sputnik as spk
import simplejson as json

search_terms = []

def search(terms):
    res = spk.search(terms)
    for track in res:
        print track

def search2(terms):
    for result in spk.search(terms):
        print result


def main():
    search("nine inch nails broken")


if __name__ == '__main__':
    main()
