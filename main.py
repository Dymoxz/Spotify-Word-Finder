import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="8e69f7d8ddfa45f1888b56411e0ac440",
                                                           client_secret="0f742321201f4e5996021d59d2608922"))


cprint(figlet_format('Spotipy \n Word \n Finder', font='doom'),
       'green', attrs=['bold'])
print('')
print('')

while True:
    with open('animal_names.txt') as input_file:
        animalNames = [line.strip() for line in input_file]

    def genre1(offset, genre):
        i1 = 0
        results1 = sp.search(q='genre:' + genre, limit=50, offset=offset)
        while i1 < len(whatToSearch):
            for idx, track in enumerate(results1['tracks']['items']):
                #print(idx, track['name'])
                if whatToSearch[i1] in track['name']:
                    foundTrack1 = track['name']
                    print('Genre: ' + genre + '    ' + foundTrack1)

            i1 = i1 + 1

    def artist1(offset, artist):
        i1 = 0
        results1 = sp.search(q='artist:' + artist, limit=50, offset=offset)
        while i1 < len(whatToSearch):
            for idx, track in enumerate(results1['tracks']['items']):
                #print(idx, track['name'])
                if whatToSearch[i1] in track['name']:
                    foundTrack1 = track['name']
                    print('Artist: ' + artist + '    ' + foundTrack1)

            i1 = i1 + 1

    searchWhat = input('What do you want to search? (1/2): \n 1. Animal Names \n 2. Custom \n')
    if searchWhat == '1':
        whatToSearch = animalNames
    elif searchWhat == '2':
        customSearch = input('What word do you want to search? \n')
        whatToSearch = customSearch.split(',')

    amount = input('How much song do you want to search through (max = 1000): \n')
    if int(amount) > 1000:
        print('Invalid Value')
        continue

    searchBy = input('Do you want to search by (1/2): \n 1. Genre \n 2. Artist \n')





    if searchBy == '2':
        offsetA1 = 0
        repeatA1 = 0
        amountOfRepeats = int(amount) / 50 - 1
        artistInput = input('Enter artist: ')
        while repeatA1 < amountOfRepeats:
            artist1(offset=offsetA1 + 50, artist=artistInput)
            offsetA1 += 50
            repeatA1 += 1

    elif searchBy == '1':
        offsetG1 = 0
        repeatG1 = 0
        amountOfRepeats = int(amount) / 50 - 1
        genreInput = input('Enter genre: ')
        while repeatG1 < amountOfRepeats:
            genre1(offset=offsetG1 + 50, genre=genreInput)
            offsetG1 += 50
            repeatG1 += 1
    else:
        print('Invalid Input')
        continue



    while True:
        answer = str(input('Restart? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Lol Noob xD")
        break
