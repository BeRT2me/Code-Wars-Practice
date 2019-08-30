import itertools as it


def fight(robot_1, robot_2, tactics):
    robots = [robot_1, robot_2]
    if robot_1['speed'] < robot_2['speed']: robots.reverse()
    for tactic_1, tactic_2 in it.zip_longest(robots[0]['tactics'], robots[1]['tactics']):
        try: robots[1]['health'] -= tactics[tactic_1]
        except KeyError: pass
        if robots[1]['health'] <= 0: break
        try: robots[0]['health'] -= tactics[tactic_2]
        except KeyError: pass
        if robots[0]['health'] <= 0: break
    if robots[0]['health'] > robots[1]['health']:
        return "{} has won the fight.".format(robots[0]['name'])
    elif robots[0]['health'] < robots[1]['health']:
        return "{} has won the fight.".format(robots[1]['name'])
    return "The fight was a draw."
