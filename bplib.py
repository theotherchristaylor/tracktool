from requests import get
from bs4 import BeautifulSoup

class bp_scrape:
    #"Set of methods to scrape from Beatport URLs"
    def get_top_100(self):
        # Returns list of search terms in the format "Artist - Title"
        url = 'https://www.beatport.com/genre/minimal-deep-tech/14/top-100'

        try:
            response = get(url)
        except:
            print('[-] In Module bplib: Invalid URL')

        #print(response.text[:500])

        soup = BeautifulSoup(response.text, 'html.parser')
        tracks = soup.find_all(class_='buk-track-primary-title')
        artists = soup.find_all(class_='buk-track-artists')

        # Need to throw out first result
        artists = artists[1:]

        terms = []
        for artist, track in zip(artists,tracks):
            term = artist.a.text + ' - ' + track.text
            terms.append(term)

        return terms

scraper = bp_scrape()
print(scraper.get_top_100())