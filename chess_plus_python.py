from chessdotcom import get_leaderboards, get_player_stats, get_player_game_archives
import pprint
import requests

printer = pprint.PrettyPrinter()


def printLeaderboards():
    data = get_leaderboards().json
    categories = data.keys()

    for category in categories:
        print('Category: ', category)

        for idx, entry in enumerate(data[category]):
            print(f'Rank: {idx + 1} | Username: {entry["username"]} | Rating: {entry["score"]}')


def getPlayerRating(username):
    data = get_player_stats(username).json
    categories = ['chess_blitz', 'chess_rapid', 'chess_bullet']

    for category in categories:
        print('Category: ', category)
        print(f'Current: {data[category]["last"]["rating"]}')
        print(f'Best: {data[category]["best"]["rating"]}')
        print(f'Record: {data[category]["record"]}')


def getMostRecentGame(username):
    data = get_player_game_archives(username).json
    url = data['archives'][-1]
    games = requests.get(url).json()
    game = games['games'][-1]
    printer.pprint(game)


getMostRecentGame('timruscica')