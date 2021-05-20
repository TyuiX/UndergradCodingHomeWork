# Jason Zhang
# jasozhang
# 112710259
# CSE 101
# Lab Assignment 10


class Player:
    def __init__(self, name, points):
        self.name = name
        self.points = points

    def __lt__(self, other):
        return self.name < other.name

    def __str__(self):
        return f"Player('{self.name}', {self.points})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.name == other.name and self.points == other.points


class Team:
    def __init__(self, name, players=None):
        self.name = name
        self.players = [] if players is None else players

    def add_player(self, name, points):
        player = Player(name, points)
        self.players.append(player)

    def add_players(self, players_info):
        players = [Player(name, points) for name, points in players_info]
        self.players.extend(players)

    def __str__(self):
        return f"Team('{self.name}', {self.players})"

    def __repr__(self):
        return self.__str__()


def verify_players(correct_players, players_selected):
    if players_selected is None:
        return False
    if len(correct_players) != len(players_selected):
        return False
    for ind in range(len(correct_players)):
        if correct_players[ind] != players_selected[ind]:
            return False
    return True


def find_above_avg_players(team):
    abvavg = []
    totalpoint = []
    for i in team.players:
        totalpoint.append(i.points)
    for i in team.players:
        if i.points >= (sum(totalpoint)/len(team.players)):
            abvavg.append(i)
    return abvavg



