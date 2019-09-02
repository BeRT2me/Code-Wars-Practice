def who_eats_who(zoo_input):
    animals = {'antelope': ['grass'], 'big-fish': ['little-fish'], 'bug': ['leaves'],
               'bear': ['big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'],
               'chicken': ['bug'], 'cow': ['grass'], 'fox': ['chicken', 'sheep'],
               'giraffe': ['leaves'], 'lion': ['antelope', 'cow'], 'panda': ['leaves'],
               'sheep': ['grass']}
    zoo = zoo_input.split(',')
    output = []
    i = 0
    while True:
        try:
            if i - 1 < 0:
                raise IndexError
            elif zoo[i - 1] in animals.get(zoo[i], []):
                output.append('{} eats {}'.format(zoo[i], zoo.pop(i - 1)))
                i = 0
            elif zoo[i + 1] in animals.get(zoo[i], []):
                output.append('{} eats {}'.format(zoo[i], zoo.pop(i + 1)))
                i = 0
            else:
                i += 1
        except IndexError:
            try:
                if zoo[i + 1] in animals.get(zoo[i], []):
                    output.append('{} eats {}'.format(zoo[i], zoo.pop(i + 1)))
                    i = 0
                elif i < len(zoo) + 1:
                    i += 1
            except IndexError:
                output.append(','.join(zoo))
                break
    return [zoo_input] + output


zoo_animals = "fox,bug,chicken,grass,sheep"
expected = ["fox,bug,chicken,grass,sheep",
            "chicken eats bug",
            "fox eats chicken",
            "sheep eats grass",
            "fox eats sheep",
            "fox"]
