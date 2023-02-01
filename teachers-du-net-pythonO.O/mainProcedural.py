"""
fonction qui return un nombre + un mot au pluriel

total : nombre de pluriels;
singular : mot au singulier;
plural : si le mot au pluriel prends autre chose que 's';
"""
def pluralize(total, singular, plural = None):
    #assert vérifie une condition, si elle est fausse: lance une exception AssertionError
    assert isinstance(total, int) and total >= 0, 'Le total fourni dans la fonction pluralize doit etre un entier >= 0'

    if plural is None:
        plural = singular + 's'

    pluralWord = singular if total <= 1 else plural

    return f'{total} {pluralWord}'


def get_basketball_team_stats(team_name, wins, losses):
    return '[BASKETBALL] STATS : {} : {} - {}.'.format(team_name, pluralize(wins, 'victoire'), pluralize(losses, 'défaite'))


def get_football_teams_stats(team_name, wins, losses):
    return f"[FOOTBALL] STATS : {team_name} : {pluralize(wins, 'victoire')} - {pluralize(losses, 'défaite')}."

if __name__ == '__main__':
    raptors_stats = 'Toronto Raptors-36-14'
    data = raptors_stats.split('-')

    print(get_basketball_team_stats(data[0], int(data[1]), int(data[2])))

    # Premiere methode ouverture d'un fichier
    with open('team.txt') as file:
        data = file.readline().strip().split('-') #strip va enlever le '\n'
 
        print(get_football_teams_stats(data[0], int(data[1]), int(data[2])))

    # Deuxieme methode ouverture d'un fichier qui necessite de le fermer
    file = open('team.txt')
    data = file.readline().strip().split('-') #strip va enlever le '\n'
    print(get_football_teams_stats(data[0], int(data[1]), int(data[2])))
    file.close()