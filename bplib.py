from requests import get
from bs4 import BeautifulSoup


def get_top_100(url):
    # Returns list of search terms in the format "Artist - Title"
    #url = 'https://www.beatport.com/genre/minimal-deep-tech/14/top-100'
    response = None
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

def get_genres():
    # Returns dictionary of genres in the form { 'Genre Name':'link' }
    try:
        response = get('https://www.beatport.com/')
    except:
        print("Error in reaching beatport.com")
        return 0
    genre_dict = {}
    soup = BeautifulSoup(response.text, 'html.parser')
    genres = soup.find_all(class_='genre-drop-list__genre')
    for item in genres:
        #print(item.text + ': ' + item['href'])
        genre_dict[item.text] = item['href']
    return genre_dict