from sklearn import tree



# card game
# type : hero(+5 in both attack)(1), villain(0)
# attack
# output : 1 for player 1, 2 for player 2
class Classifiers:
    clf = tree.DecisionTreeClassifier()

    def run(self):
        features = [[0, 50, 0, 60], [1, 50, 1, 60], [0, 60, 0, 50], [1, 60, 1, 50]]
        labels = [2, 2, 1, 1]

        fea = []
        for i in range(1, 50):
            fea.append(0)
            fea.append(i)
            fea.append(0)
            fea.append(i + 50)
            labels.append(2)
            features.append(fea)
            fea = [1, i, 1, i + 50]
            labels.append(2)
            features.append(fea)
            fea = [0, i + 50, 0, i]
            labels.append(1)
            features.append(fea)
            fea = [1, i + 50, 1, i]
            labels.append(1)
            features.append(fea)
            fea = [1, i, 0, i + 4]
            labels.append(1)
            features.append(fea)
            fea = [1, i, 0, i + 3]
            labels.append(1)
            features.append(fea)
            fea = [1, i, 0, i + 2]
            labels.append(1)
            features.append(fea)
            fea = [1, i, 0, i + 1]
            labels.append(1)
            features.append(fea)
            fea = [1, i, 0, i]
            labels.append(1)
            features.append(fea)
            fea = [0, i + 4, 1, i]
            labels.append(2)
            features.append(fea)
            fea = [0, i + 3, 1, i]
            labels.append(2)
            features.append(fea)
            fea = [0, i + 2, 1, i]
            labels.append(2)
            features.append(fea)
            fea = [0, i + 1, 1, i]
            labels.append(2)
            features.append(fea)
            fea = [0, i, 1, i]
            labels.append(2)
            features.append(fea)
            fea = []
        self.clf = self.clf.fit(features, labels)


class Card:
    types = int()
    attack = int()
    name = str()
    image_path = r'F:\python\card game\cards'

    def __init__(self, types, attack, name, image_path):
        self.types = types
        self.attack = attack
        self.name = name
        self.image_path=self.image_path+image_path


class CreateCard:
    list_char = []
    ice_man = Card(1, 56, "ICE MAN", r'\iceman.png')
    list_char.append(ice_man)
    abomination = Card(0, 58, "ABOMINATION", r'\abomination.jpg')
    list_char.append(abomination)
    red_hulk = Card(0, 79, "RED HULK", r'\red_hulk.jpg')
    list_char.append(red_hulk)
    havok = Card(1, 63, "HAVOK", r'\havok.jpg')
    list_char.append(havok)
    war_machine = Card(1, 53, "WAR MACHINE", r'\war_machine.jpg')
    list_char.append(war_machine)
    quasimodo = Card(0, 67, "QUASIMODO", r'\quasimodo.jpg')
    list_char.append(quasimodo)
    beast = Card(1, 73, "BEAST", r'\beast.jpg')
    list_char.append(beast)
    americop = Card(1, 44, "AMERICOP", r'\americop.jpg')
    list_char.append(americop)
    ultron = Card(0, 39, "ULTRON", r'\ultron.png')
    list_char.append(ultron)
    list_name = []
