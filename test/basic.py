import sputnik
import simplejson as json


def main():
    s = sputnik.search("nine inch nails")
    print "Number of results: " + str(s.info['num_results'])
    for track in s:
        print '- ' + track['name']
        print '\t ' + track['album']['name']
        artists = [ar['name'] for ar in track['artists']]
        print '\t ' + ', '.join(artists)


if __name__ == '__main__':
    main()
