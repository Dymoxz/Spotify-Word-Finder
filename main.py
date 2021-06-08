import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import sys
from colorama import init
init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
from termcolor import cprint
from pyfiglet import figlet_format
#import sys
#from PySide6.QtWidgets import QApplication, QMainWindow

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="8e69f7d8ddfa45f1888b56411e0ac440",
                                                           client_secret="0f742321201f4e5996021d59d2608922"))


cprint(figlet_format('Spotify \n Word \n Finder', font='doom'),
       'green', attrs=['bold'])
print('')
print('')

while True:
    with open('animal_names.txt') as input_file:
        animalNames = [line.strip() for line in input_file]

    with open('countries.txt') as input_file:
        countryNames = [line.strip() for line in input_file]
    numbers1000 = list(range(1000))


    def genre1(offset, genre, year):
        i1 = 0
        results1 = sp.search(q='genre:' + genre + ' ' + year, limit=50, offset=offset)
        while i1 < len(whatToSearch):
            for idx, track in enumerate(results1['tracks']['items']):
                #print(idx, track['name'])
                if whatToSearch[i1] in track['name']:
                    foundTrack1 = track['name']
                    print('Genre: ' + genre + 'Year:' + year + '    ' + foundTrack1)

            i1 = i1 + 1

    def artist1(offset, artist, year):
        i1 = 0
        results1 = sp.search(q='artist:' + artist + ' ' + year, limit=50, offset=offset)
        while i1 < len(whatToSearch):
            for idx, track in enumerate(results1['tracks']['items']):
                #print(idx, track['name'])
                if whatToSearch[i1] in track['name']:
                    foundTrack1 = track['name']
                    print('Artist: ' + artist + '    ' + foundTrack1)

            i1 = i1 + 1

    def year1(offset, year):
        i1 = 0
        results1 = sp.search(q='artist:' + year, limit=50, offset=offset)
        while i1 < len(whatToSearch):
            for idx, track in enumerate(results1['tracks']['items']):
                #print(idx, track['name'])
                if whatToSearch[i1] in track['name']:
                    foundTrack1 = track['name']
                    print('Year: ' + year + '    ' + foundTrack1)

            i1 = i1 + 1
    print('')

    searchWhat = input('What do you want to search? (1/2/3): \n 1. Animal Names \n 2. Countries \n 3. Numbers \n 4. Custom Words \n > ')


    if searchWhat == '1':
        whatToSearch = animalNames
    elif searchWhat == '2':
        whatToSearch = countryNames
    elif searchWhat == '3':
        numberAsk = input('What numbers do you want to search? (1/2): \n 1. 0 -> 1000 \n 2. Custom Numbers \n > ')
        if numberAsk == '1':
            whatToSearch = [format(x) for x in numbers1000]
        elif numberAsk == '2':
            numberInput = input('What numbers do you want to search? (e.g: 1, 87, 255): \n > ')
            whatToSearch = [format(x) for x in numberInput]

    elif searchWhat == '4':
        customSearch = input('What words do you want to search? (e.g.: house, car, what, who): \n > ')
        whatToSearch = customSearch.split(',')

    print('')
    amount = input('How much song do you want to search through (max = 1000): \n > ')
    if int(amount) > 1000:
        print('Invalid Value')
        continue
    print('')
    searchBy = input('Do you want to search by (1/2/3): \n 1. Genre \n 2. Artist \n 3. Year \n > ')
    print('')




    if searchBy == '1':
        offsetG1 = 0
        repeatG1 = 0
        amountOfRepeats = int(amount) / 50 - 1
        genreInput = input('Enter genre: \n > ')
        searchByYear = input('Enter year: (leave empty if none) \n > ')
        yearInput = 'year:' + searchByYear
        if yearInput == '':
            while repeatG1 < amountOfRepeats:
                genre1(offset=offsetG1 + 50, genre=genreInput, year=searchByYear)
                offsetG1 += 50
                repeatG1 += 1
        else:
            while repeatG1 < amountOfRepeats:
                genre1(offset=offsetG1 + 50, genre=genreInput, year=yearInput)
                offsetG1 += 50
                repeatG1 += 1
    elif searchBy == '2':
        offsetA1 = 0
        repeatA1 = 0
        amountOfRepeats = int(amount) / 50 - 1
        artistInput = input('Enter artist: \n > ')
        searchByYear = input('Enter year: (leave empty if none) \n > ')
        yearInput = 'year:' + searchByYear
        if yearInput == '':
            while repeatA1 < amountOfRepeats:
                artist1(offset=offsetA1 + 50, artist=artistInput, year=searchByYear)
                offsetA1 += 50
                repeatA1 += 1
        else:
            while repeatA1 < amountOfRepeats:
                artist1(offset=offsetA1 + 50, artist=artistInput, year=yearInput)
                offsetA1 += 50
                repeatA1 += 1
    elif searchBy == '3':
        offsetN1 = 0
        repeatN1 = 0
        amountOfRepeats = int(amount) / 50 - 1
        yearInput = input('Enter year: \n > ')
        while repeatN1 < amountOfRepeats:
            year1(offset=offsetN1 + 50, year=yearInput)
            offsetN1 += 50
            repeatN1 += 1


    else:
        print('Invalid Input')
        continue



    while True:
        answer = str(input('Restart? (y/n): \n > '))
        if answer in ('y', 'n'):
            break
        print('invalid input.')
    if answer == 'y':
        continue
        print('')
    else:
        cprint('Lol Noob xD', 'green')
        break

    print('')
    cprint('Spotify Word Finder', 'green')















