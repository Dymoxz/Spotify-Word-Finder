import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="8e69f7d8ddfa45f1888b56411e0ac440",
                                                           client_secret="0f742321201f4e5996021d59d2608922"))

print('SPOTIPY ANIMAL FINDER')
print('')
print('')

while True:
    with open('animal_names.txt') as input_file:
        animalNames = [line.strip() for line in input_file]

    def genre1(offset, genre):
        i1 = 0
        results1 = sp.search(q='genre:' + genre, limit=50, offset=offset)
        while i1 < len(animalNames):
            for idx, track in enumerate(results1['tracks']['items']):
                #print(idx, track['name'])
                if animalNames[i1] in track['name']:
                    foundTrack1 = track['name']
                    print('Genre: ' + genre + '    ' + foundTrack1)

            i1 = i1 + 1

    def artist1(offset, artist):
        i1 = 0
        results1 = sp.search(q='artist:' + artist, limit=50, offset=offset)
        while i1 < len(animalNames):
            for idx, track in enumerate(results1['tracks']['items']):
                #print(idx, track['name'])
                if animalNames[i1] in track['name']:
                    foundTrack1 = track['name']
                    print('Artist: ' + artist + '    ' + foundTrack1)

            i1 = i1 + 1

    searchBy = input('Do you want to search by (1/2): \n 1. Genre \n 2. Artist \n')


    if searchBy == '2':
        offsetA1 = 0
        repeatA1 = 0
        artistInput = input('Enter artist: ')
        while repeatA1 < 19:
            artist1(offset=offsetA1 + 50, artist=artistInput)
            offsetA1 += 50
            repeatA1 += 1

    elif searchBy == '1':
        offsetG1 = 0
        repeatG1 = 0
        genreInput = input('Enter genre: ')
        while repeatG1 < 19:
            genre1(offset=offsetG1 + 50, genre=genreInput)
            offsetG1 += 50
            repeatG1 += 1

    while True:
        answer = str(input('Restart? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break
