from bplib import get_top_100, get_genres


#url = 'https://www.beatport.com/genre/minimal-deep-tech/14/top-100'
#print(get_top_100(url))
base_url = 'https://www.beatport.com'
genres = get_genres()

genre_list = []

ref = 1
for name in genres:
    print(str(ref) + ': ' + name)
    genre_list.append(name)
    ref += 1

print('Choose a genre: ')
genre_index = int(input())

genre = genre_list[genre_index - 1]
genre_link = genres[genre]
#print(genre_link)

full_url = base_url + genre_link + '/top-100'

#print(full_url)

top_100 = get_top_100(full_url)

print(top_100)
