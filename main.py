import random
import pygame
import threading
import time
from tkinter import messagebox
from sklearn import tree
from tkinter import *


#machine learning part
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
    image_path = r'.\cards'

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
    paladin = Card(1, 30, "PALADIN", r'\paladin.jpg')
    list_char.append(paladin)
    red_skull = Card(0, 70, "RED SKULL", r'\red_skull.jpg')
    list_char.append(red_skull)
    viper = Card(0, 40, "VIPER", r'\viper.png')
    list_char.append(viper)
    anaconda = Card(0, 51, "ANACONDA", r'\anaconda.jpg')
    list_char.append(anaconda)
    avalanche = Card(0, 45, "AVALANCHE", r'\avalanche.jpg')
    list_char.append(avalanche)
    callisto = Card(0, 45, "CALLISTO", r'\callisto.jpg')
    list_char.append(callisto)
    sandman = Card(0, 74, "SANDMAN", r'\sandman.jpg')
    list_char.append(sandman)
    wolverine = Card(1, 74, "WOLVERINE", r'\wolverine.jpg')
    list_char.append(wolverine)
    chameleon = Card(0, 42, "CHAMELEON", r'\chameleon.jpg')
    list_char.append(chameleon)
    firebird = Card(1, 61, "FIREBIRD", r'\firebird.jpg')
    list_char.append(firebird)
    mr_sinister = Card(0, 44, "MR SINISTER", r'\mr_sinister')
    list_char.append(mr_sinister)
    nighthawk = Card(1, 61, "NIGHTHAWK", r'\nighthawk.jpg')
    list_char.append(nighthawk)
    mastermind = Card(0, 40, "MASTERMIND", r'\mastermind.jpg')
    list_char.append(mastermind)
    silver_surfer = Card(1, 83, "SILVER SURFER", r'\silver_surfer.jpg')
    list_char.append(silver_surfer)
    gorilla_man = Card(1, 45, "GORILLA-MAN", r'\gorilla_man.jpg')
    list_char.append(gorilla_man)
    looter = Card(0, 55, "LOOTER", r'\looter.jpg')
    list_char.append(looter)
    quicksilver = Card(1, 56, "QUICKSILVER", r'\quicksilver.jpg')
    list_char.append(quicksilver)
    patriot = Card(1, 37, "PATRIOT", r'\patriot.jpg')
    list_char.append(patriot)
    carnage = Card(0, 76, "CARNAGE", r'\carnage.jpg')
    list_char.append(carnage)
    nightcrawler = Card(1, 85, "NIGHTCRAWLER", r'\nightcrawler.jpg')
    list_char.append(nightcrawler)
    ms_marvel = Card(1, 58, "Ms. MARVEL", r'\ms_marvel.jpg')
    list_char.append(ms_marvel)
    apocalypse = Card(0, 85, "APOCALYPSE", r'\apocalypse.jpg')
    list_char.append(apocalypse)
    grim_reaper = Card(0, 83, "GRIM REAPER", r'\grim_reaper.jpg')
    list_char.append(grim_reaper)
    valkyrie = Card(1, 73, "VALKYRIE", r'\valkyrie.jpg')
    list_char.append(valkyrie)
    human_torch = Card(1, 57, "HUMAN TORCH", r'\human_torch.jpg')
    list_char.append(human_torch)
    nick_fury = Card(1, 77, "NICK FURY", r'\nick_fury.jpg')
    list_char.append(nick_fury)
    nocturne = Card(1, 38, "NOCTURNE", r'\nocturne.jpg')
    list_char.append(nocturne)
    archangel = Card(1, 40, "ARCHANGEL", r'\archangel.jpg')
    list_char.append(archangel)
    crimson_crusader = Card(1, 53, "CRIMSON CRUSADER", r'\crimson_crusader.jpg')
    list_char.append(crimson_crusader)
    blue_diamond = Card(1, 52, "BLUE DIAMOND", r'\blue_diamond.jpg')
    list_char.append(blue_diamond)
    living_mummy = Card(1, 45, "LIVING MUMMY", r'\living_mummy.jpg')
    list_char.append(living_mummy)
    wasp = Card(1, 50, "WASP", r'\wasp.jpg')
    list_char.append(wasp)
    storm = Card(1, 88, "STORM", r'\storm.jpg')
    list_char.append(storm)
    black_widow = Card(1, 65, "BLACK WIDOW", r'\black_widow.jpg')
    list_char.append(black_widow)
    dark_phoenix = Card(1, 63, "DARK PHOENIX", r'\dark_phoenix.jpg')
    list_char.append(dark_phoenix)
    phoenix = Card(0, 88, "PHOENIX", r'\phoenix.jpg')
    list_char.append(phoenix)
    pyro = Card(0, 43, "PYRO", r'\pyro.jpg')
    list_char.append(pyro)
    gambit = Card(1, 57, "GAMBIT", r'\gambit.jpg')
    list_char.append(gambit)
    she_hulk = Card(1, 65, "SHE-HULK", r'\she_hulk.jpg')
    list_char.append(she_hulk)
    night_thrasher = Card(0, 51, "NIGHT THRASHER", r'\night_thrasher.jpg')
    list_char.append(night_thrasher)
    spider_woman = Card(1, 66, "SPIDER-WOMAN", r'\spider_woman.jpg')
    list_char.append(spider_woman)
    sabretooth = Card(0, 79, "SABRETOOTH", r'\sabretooth.jpg')
    list_char.append(sabretooth)
    mandarin = Card(0, 33, "MANDARIN", r'\mandarin.jpg')
    list_char.append(mandarin)
    the_skrulls = Card(0, 64, "THE SKRULLS", r'\the_skrulls.jpg')
    list_char.append(the_skrulls)
    sage = Card(1, 36, "SAGE", r'\sage.jpg')
    list_char.append(sage)
    kraven = Card(0, 48, "KRAVEN", r'\kraven.jpg')
    list_char.append(kraven)
    doctor_octopus = Card(0, 84, "DOCTOR OCTOPUS", r'\doctor_octopus.jpg')
    list_char.append(doctor_octopus)
    karma = Card(1, 51, "KARMA", r'\karma.jpg')
    list_char.append(karma)
    lionheart = Card(1, 57, "LIONHEART", r'\lionheart.jpg')
    list_char.append(lionheart)
    colossus = Card(1, 52, "COLOSSUS", r'\colossus.jpg')
    list_char.append(colossus)
    blob = Card(0, 50, "BLOB", r'\blob.jpg')
    list_char.append(blob)
    venom = Card(0, 57, "VENOM", r'\venom.jpg')
    list_char.append(venom)
    maximus = Card(0, 33, "MAXIMUS", r'\maximus.jpg')
    list_char.append(maximus)
    mystique = Card(0, 47, "MYSTIQUE", r'\mystique.jpg')
    list_char.append(mystique)
    dracula = Card(0, 91, "DRACULA", r'\dracula.jpg')
    list_char.append(dracula)
    bloodscream = Card(0, 55, "BLOODSCREAM", r'\bloodscream.jpg')
    list_char.append(bloodscream)
    the_thing = Card(1, 64, "THE THING", r'\the_thing.jpg')
    list_char.append(the_thing)
    captain_america = Card(1, 75, "CAPTAIN AMERICA", r'\captain_america.jpg')
    list_char.append(captain_america)
    doctor_strange = Card(1, 54, "DOCTOR STRANGE", r'\doctor_strange.jpg')
    list_char.append(doctor_strange)
    venus = Card(1, 44, "VENUS", r'\venus.jpg')
    list_char.append(venus)
    crossbones = Card(0, 74, "CROSSBONES", r'\crossbones.jpg')
    list_char.append(crossbones)
    professor_x = Card(1, 60, "PROFESSOR X", r'\professor_x.jpg')
    list_char.append(professor_x)
    invisible_woman = Card(1, 57, "INVISIBLE WOMAN", r'\invisible_woman.jpg')
    list_char.append(invisible_woman)
    ant_man = Card(1, 50, "ANT-MAN", r'\ant_man.jpg')
    list_char.append(ant_man)
    blade = Card(1, 80, "BLADE", r'\blade.jpg')
    list_char.append(blade)
    blackheart = Card(0, 71, "BLACKHEART", r'\blackheart.jpg')
    list_char.append(blackheart)
    loki = Card(1, 101, "LOKI", r'\loki.jpg')
    list_char.append(loki)
    magneto = Card(0, 60, "MAGNETO", r'\magneto.jpg')
    list_char.append(magneto)
    punisher = Card(1, 53, "PUNISHER", r'\punisher.jpg')
    list_char.append(punisher)
    diablo = Card(0, 47, "DIABLO", r'\diablo.jpg')
    list_char.append(diablo)
    puma = Card(0, 53, "PUMA", r'\puma.jpg')
    list_char.append(puma)
    dragon_man = Card(0, 44, "DRAGON MAN", r'\dragon_man.jpg')
    list_char.append(dragon_man)
    the_fury = Card(0, 73, "THE FURY", r'\the_fury.jpg')
    list_char.append(the_fury)
    list_name = []


# initialization
pygame.init()
window = pygame.display.set_mode((900, 600))
pygame.display.set_caption('AVENGERS ASSEMBLE')
icon = pygame.image.load("icon.ico")
pygame.display.set_icon(icon)
title = True
thread_start = False
thread_stop = True
running = True
screen3 = True
p1_imgs = []
p2_imgs = []
score_p1 = 0
score_p2 = 0
game_rem = 5
current_card_p1 = 0
current_card_p2 = 0
turn_player = 1
player1 = ''
player2 = ''
deck = tuple()
reset = False
check = False
end = 0

# important images
#F:\python\card game\heros
#F:\python\card game\cards
title_image = pygame.image.load('titlecard.png')
title1 = pygame.image.load(r'.\heros\1.png')
title2 = pygame.image.load(r'.\heros\2.png')
title3 = pygame.image.load(r'.\heros\3.png')
title4 = pygame.image.load(r'.\heros\4.png')
title5 = pygame.image.load(r'.\heros\5.png')
bg_screen2 = pygame.image.load(r'.\heros\bg1.jpg')
player1_lab = pygame.image.load(r'.\heros\player1.png')
player2_lab = pygame.image.load(r'.\heros\player2.png')
game_name_image = pygame.image.load('game_name.png')
space = pygame.image.load(r'.\heros\space.png')
space2 = pygame.image.load(r'.\heros\space2.png')
tip1 = pygame.image.load(r'.\heros\tip1.png')
cnf = pygame.image.load(r'.\heros\cnf.png')
bg_card = pygame.image.load(r'.\heros\card_back.jpg')
namevs = pygame.image.load(r'.\heros\namevs.png')
split = pygame.image.load(r'.\heros\split.png')
turn = pygame.image.load(r'.\heros\turn.png')
no_turn = pygame.image.load(r'.\heros\no_turn.png')
next_char = pygame.image.load(r'.\heros\next.png')
prev_char = pygame.image.load(r'.\heros\prev.png')
go_button = pygame.image.load(r'.\heros\play.png')
score_button = pygame.image.load(r'.\heros\score.png')
struct = pygame.image.load(r'.\cards\struct.png')
num = []
for i in ('num1.png', 'num2.png', 'num3.png', 'num4.png', 'num5.png'):
    img = pygame.image.load(r'.\heros\\' + i)
    num.append(img)
mjolnir = pygame.image.load(r'.\heros\mjolnir.png')
thor1 = pygame.image.load(r'.\heros\thor1.png')
thor2 = pygame.image.load(r'.\heros\thor2.png')
crack = pygame.image.load(r'.\heros\crack.png')
the = pygame.image.load(r'.\heros\the.png')
winner_ = pygame.image.load(r'.\heros\winner.png')
is_ = pygame.image.load(r'.\heros\is.png')
namede = pygame.image.load(r'.\heros\namede.png')
restart = pygame.image.load(r'.\heros\restart.png')
info = pygame.image.load(r'.\heros\info.png')


# functions
def out():
    pygame.mixer.music.load('click.mp3')
    pygame.mixer.music.play()
    exit(1)


def title_card(x, y):
    window.blit(title_image, (x, y))


def start_title_thread(x, y):
    global thread_start, thread_stop
    thread_start = True
    thread_stop = False
    if thread_stop:
        return
    time.sleep(0.25)
    if thread_stop:
        return
    pygame.mixer.music.load('titletrack.mp3')
    if thread_stop:
        return
    pygame.mixer.music.play()
    if thread_stop:
        return
    time.sleep(1.35)
    if thread_stop:
        return
    window.blit(title1, (0, 0))
    if thread_stop:
        return
    time.sleep(1.35)
    if thread_stop:
        return
    window.blit(title2, (650, 5))
    if thread_stop:
        return
    time.sleep(1.35)
    if thread_stop:
        return
    window.blit(title3, (450, 10))
    if thread_stop:
        return
    window.blit(title4, (350, 10))
    if thread_stop:
        return
    time.sleep(1.5)
    if thread_stop:
        return
    window.blit(title5, (20, 550))
    if thread_stop:
        return
    thread_stop = True


def game_name(x, y):
    if not thread_start:
        window.blit(game_name_image, (x, y))
        t1 = threading.Thread(target=start_title_thread, args=(x, y))
        t1.start()
        return
    else:
        return


def screen2():
    window.fill([255, 255, 255])
    bg_screen2.set_alpha(150)
    window.blit(bg_screen2, (0, 0))
    window.blit(player1_lab, (150, 270))
    window.blit(player2_lab, (550, 270))
    window.blit(space, (80, 150))
    window.blit(space, (480, 150))
    window.blit(tip1, (150, 30))
    window.blit(cnf, (650, 480))
    window.blit(info, (3, 545))


def player_name(x, y):
    global running
    global screen3
    text = ''
    running = True
    font = pygame.font.SysFont(None, 46)
    img = font.render('sysfont', True, (255, 255, 255))
    rect = img.get_rect()
    pygame.draw.rect(img, (0, 0, 0), rect, 1)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                out()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pygame.mixer.music.load('click3.mp3')
                    pygame.mixer.music.play()
                    running = False
                elif event.key == pygame.K_BACKSPACE:
                    text = text[:-1]
                    window.blit(space, (x - 40, 150))
                    img1 = font.render(text, True, (0, 0, 0))
                    window.blit(img1, (x, y))
                else:
                    if len(text) < 15:
                        text += event.unicode
                        window.blit(space, (x - 40, 150))
                        img1 = font.render(text, True, (0, 0, 0))
                        window.blit(img1, (x, y))
        pygame.display.update()
    return text


def start_shuffle_thread(x, y):
    for i in (0, 5, 10):
        pygame.mixer.music.play()
        window.blit(bg_card, (x + i, y))
        time.sleep(1)
    pygame.mixer.music.play()
    time.sleep(1)
    pygame.mixer.music.play()
    time.sleep(1)


def screen_3():
    window.fill([255, 255, 255])
    bg_screen2.set_alpha(150)
    window.blit(bg_screen2, (0, 0))
    window.blit(namevs, (10, 10))
    window.blit(namevs, (585, 10))
    window.blit(turn, (250, 80))
    window.blit(no_turn, (585, 80))
    window.blit(split, (420, 10))
    window.blit(next_char, (85, 80))
    window.blit(prev_char, (10, 80))
    window.blit(next_char, (820, 80))
    window.blit(prev_char, (745, 80))
    window.blit(go_button, (400, 450))
    window.blit(score_button, (310, 220))
    window.blit(space2, (310, 270))
    window.blit(score_button, (475, 220))
    window.blit(space2, (475, 270))
    font = pygame.font.SysFont('consolas', 36)
    img = font.render('sysfont', True, (255, 255, 255))
    rect = img.get_rect()
    pygame.draw.rect(img, (0, 0, 0), rect, 1)
    name1 = font.render(player1, True, (255, 255, 255))
    window.blit(name1, (20, 20))
    name2 = font.render(player2, True, (255, 255, 255))
    window.blit(name2, (595, 20))
    window.blit(struct, (20, 150))
    window.blit(struct, (595, 150))
    deck = ([], [])
    cardo = CreateCard()
    for i in range(0, 5):
        a = random.randint(0, len(cardo.list_char) - 1)
        deck[0].append(cardo.list_char[a])
        a = random.randint(0, (len(cardo.list_char) - 1))
        deck[1].append(cardo.list_char[a])
    window.blit(info, (3, 545))
    return deck


def update_score():
    global score_p1, score_p2, current_card_p1, current_card_p2, turn_player, game_rem, running
    game_rem = game_rem - 1
    classify = Classifiers()
    classify.run()
    card_p1 = deck[0].pop(current_card_p1)
    card_p2 = deck[1].pop(current_card_p2)
    i1 = p1_imgs.pop(current_card_p1)
    i2 = p2_imgs.pop(current_card_p2)
    if card_p1.attack == card_p2.attack and card_p1.types == card_p2.types:
        score_p1 = score_p1 + (10 * (5 - game_rem))
        score_p2 = score_p2 + (10 * (5 - game_rem))
    else:
        result = classify.clf.predict([[card_p1.types, card_p1.attack, card_p2.types, card_p2.attack]])
        if result[0] == 1:
            score_p1 = score_p1 + (10 * (5 - game_rem))
        elif result[0] == 2:
            score_p2 = score_p2 + (10 * (5 - game_rem))
    window.blit(space2, (310, 270))
    window.blit(space2, (475, 270))
    font = pygame.font.SysFont('consolas', 36)
    img = font.render('sysfont', True, (0, 0, 0))
    rect = img.get_rect()
    pygame.draw.rect(img, (0, 0, 0), rect, 1)
    name1 = font.render(str(score_p1), True, (0, 0, 0))
    window.blit(name1, (320, 280))
    name2 = font.render(str(score_p2), True, (0, 0, 0))
    window.blit(name2, (485, 280))
    if game_rem > 0:
        window.blit(p1_imgs[0], (20, 150))
        window.blit(p2_imgs[0], (595, 150))
        window.blit(num[0], (25, 195))
        window.blit(num[0], (600, 195))
        window.blit(turn, (250, 80))
        window.blit(no_turn, (585, 80))
        current_card_p1 = 0
        current_card_p2 = 0
        turn_player = 1
    else:
        window.blit(struct, (20, 150))
        window.blit(struct, (595, 150))


def move():
    global thread_stop, end
    if end:
        return
    pygame.mixer.music.load('title2.mp3')
    pygame.mixer.music.play()
    y = 550
    while y != -200:
        if end:
            return
        window.fill([255, 255, 255])
        window.blit(mjolnir, (400, y))
        time.sleep(0.05)
        y = y - 5
    y = -400
    t = 0.075
    dt = 0.0005
    while y < 250:
        if end:
            return
        window.fill([255, 255, 255])
        window.blit(thor1, (300, y))
        time.sleep(t)
        t = t - dt
        dt = dt + 0.000001
        y = y + 5
    window.fill([255, 255, 255])
    window.blit(thor2, (420, 250))
    window.blit(crack, (110, 450))
    window.blit(thor2, (420, 250))
    pygame.mixer.music.stop()
    window.fill([255, 0, 0])
    window.blit(crack, (110, 450))
    window.blit(thor2, (420, 250))
    thread_stop = True
    time.sleep(1)
    if end:
        return
    pygame.mixer.music.load('titletrack.mp3')
    pygame.mixer.music.play()
    window.blit(the, (160, 65))
    time.sleep(1.2)
    if end:
        return
    window.blit(winner_, (350, 65))
    time.sleep(1.3)
    if end:
        return
    window.blit(is_, (650, 65))
    time.sleep(1.4)
    if end:
        return
    window.blit(namede, (245, 150))
    time.sleep(1.5)
    if end:
        return
    if score_p2 > score_p1:
        win = player2
    elif score_p1 > score_p2:
        win = player1
    else:
        win = 'Both. Because it\'s a tie'
    font = pygame.font.SysFont('consolas', 36)
    img = font.render('sysfont', True, (255, 255, 255))
    rect = img.get_rect()
    pygame.draw.rect(img, (0, 0, 0), rect, 1)
    name1 = font.render(win, True, (255, 255, 255))
    window.blit(name1, (260, 160))
    time.sleep(0.1)
    if end:
        return
    window.blit(restart, (30, 500))


def winner():
    time.sleep(0.5)
    window.fill([255, 255, 255])
    bg_screen2.set_alpha(150)
    window.blit(bg_screen2, (0, 0))
    window.blit(mjolnir, (400, 550))
    thread = threading.Thread(target=move)
    thread.start()


def show_info():
    root = Tk()
    root.withdraw()
    messagebox.showinfo('HOW TO PLAY!!!!', 'Welcome Gamers, this is a two player game. Both Players should enter '
                                           'names as per instructed on first page. When on Playing screen, '
                                           'the control is shown as a red dot on a purple box. Both players should '
                                           'select '
                                           'one card each and one of them will win the round or maybe in case of a '
                                           'tie both will get benefits of scores. Points will be provided 10 in first '
                                           'round, 20 in 2nd, etc. There will be total 5 rounds. Once they are '
                                           'finished winner is decided and displayed. You can even restart a game '
                                           'once game is over. Good Luck!!')
    root.lift()


def show_error(message):
    root = Tk()
    root.withdraw()
    messagebox.showerror('No Entry', message)
    root.lift()


def check_name():
    global check
    if player1 == '' or player2 == '':
        show_error('Seems like forgot to enter the name of one or two players!!!')
        window.blit(space, (80, 150))
        window.blit(space, (480, 150))
    elif player1 == player2:
        show_error('Both players\' names must not be same!!!')
        window.blit(space, (80, 150))
        window.blit(space, (480, 150))
    elif (not player1.isalpha()) or (not player2.isalpha()):
        show_error('Invalid name entered!!!')
        window.blit(space, (80, 150))
        window.blit(space, (480, 150))
    else:
        check = True


# title screen
def start():
    pygame.mixer.music.load('click2.mp3')
    pygame.mixer.music.play()
    global title, thread_stop, thread_start, running, screen3, p1_imgs, p2_imgs, score_p2, score_p1, game_rem
    global current_card_p1, current_card_p2, turn_player, deck, player1, player2, reset, check, end
    reset = False
    title = True
    thread_start = False
    thread_stop = True
    running = True
    screen3 = True
    check = False

    # screen2
    screen2()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                out()
            if pygame.mouse.get_pressed()[0] and 150 <= pygame.mouse.get_pos()[1] <= 240:
                pygame.mixer.music.load('click2.mp3')
                pygame.mixer.music.play()
                if 80 <= pygame.mouse.get_pos()[0] <= 440:
                    player1 = player_name(120, 180)
                    running = True
                elif 480 <= pygame.mouse.get_pos()[0] <= 840:
                    player2 = player_name(520, 180)
                    running = True
            elif pygame.mouse.get_pressed()[0] and 480 <= pygame.mouse.get_pos()[1] <= 580 and 650 <= \
                    pygame.mouse.get_pos()[
                        0] <= 860:
                check_name()
                if check:
                    pygame.mixer.music.load('click2.mp3')
                    pygame.mixer.music.play()
                    deck = screen_3()
                    running = False
                    break
            elif pygame.mouse.get_pressed()[0] and 545 <= pygame.mouse.get_pos()[1] <= 595 and 5 <= \
                    pygame.mouse.get_pos()[0] <= 50:
                show_info()
        pygame.display.update()

    # loading images of cards
    p1_imgs = []
    p2_imgs = []
    for i in range(0, 5):
        img = pygame.image.load(deck[0][i].image_path)
        img2 = pygame.image.load(deck[1][i].image_path)
        p1_imgs.append(img)
        p2_imgs.append(img2)
    score_p1 = 0
    score_p2 = 0
    game_rem = 5

    # screen of new game
    window.blit(p1_imgs[0], (20, 150))
    window.blit(p2_imgs[0], (595, 150))
    window.blit(num[0], (25, 195))
    window.blit(num[0], (600, 195))
    current_card_p1 = 0
    current_card_p2 = 0
    turn_player = 1
    thread_start = False
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                out()
            elif pygame.mouse.get_pressed()[0] and 80 < pygame.mouse.get_pos()[1] < 138:
                if 10 < pygame.mouse.get_pos()[0] < 75 and current_card_p1 >= 1 and turn_player == 1:
                    pygame.mixer.music.load('click2.mp3')
                    pygame.mixer.music.play()
                    current_card_p1 = current_card_p1 - 1
                    window.blit(p1_imgs[current_card_p1], (20, 150))
                    window.blit(num[current_card_p1], (25, 195))
                elif 85 < pygame.mouse.get_pos()[0] < 155 and current_card_p1 < len(deck[0]) - 1 and turn_player == 1:
                    pygame.mixer.music.load('click2.mp3')
                    pygame.mixer.music.play()
                    current_card_p1 = current_card_p1 + 1
                    window.blit(p1_imgs[current_card_p1], (20, 150))
                    window.blit(num[current_card_p1], (25, 195))
                elif 740 < pygame.mouse.get_pos()[0] < 810 and current_card_p2 >= 1 and turn_player == 2:
                    pygame.mixer.music.load('click2.mp3')
                    pygame.mixer.music.play()
                    current_card_p2 = current_card_p2 - 1
                    window.blit(p2_imgs[current_card_p2], (595, 150))
                    window.blit(num[current_card_p2], (600, 195))
                elif 820 < pygame.mouse.get_pos()[0] < 885 and current_card_p2 < len(deck[1]) - 1 and turn_player == 2:
                    pygame.mixer.music.load('click2.mp3')
                    pygame.mixer.music.play()
                    current_card_p2 = current_card_p2 + 1
                    window.blit(p2_imgs[current_card_p2], (595, 150))
                    window.blit(num[current_card_p2], (600, 195))
                elif 250 < pygame.mouse.get_pos()[0] < 310 and turn_player == 1:
                    pygame.mixer.music.load('click3.mp3')
                    pygame.mixer.music.play()
                    turn_player = 2
                    window.blit(no_turn, (250, 80))
                    window.blit(turn, (585, 80))
                elif 585 < pygame.mouse.get_pos()[0] < 645 and turn_player == 2:
                    pygame.mixer.music.load('click3.mp3')
                    pygame.mixer.music.play()
                    turn_player = 1
                    window.blit(turn, (250, 80))
                    window.blit(no_turn, (585, 80))
            elif pygame.mouse.get_pressed()[0] and 400 < pygame.mouse.get_pos()[0] < 490 and 455 < \
                    pygame.mouse.get_pos()[
                        1] < 545:
                pygame.mixer.music.load('click.mp3')
                pygame.mixer.music.play()
                update_score()
                if game_rem == 0:
                    pygame.mixer.music.load('click.mp3')
                    pygame.mixer.music.play()
                    running = False
                    break
            elif pygame.mouse.get_pressed()[0] and 545 <= pygame.mouse.get_pos()[1] <= 595 and 5 <= \
                    pygame.mouse.get_pos()[0] <= 50:
                show_info()
        if not thread_start:
            pygame.mixer.music.load('shuffle.mp3')
            t1 = threading.Thread(target=start_shuffle_thread, args=(330, 10))
            t1.start()
            t2 = threading.Thread(target=start_shuffle_thread, args=(460, 10))
            t2.start()
            thread_start = True
        pygame.display.update()

    running = True
    winner()
    end = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = 1
                out()
            if pygame.mouse.get_pressed()[0] and 30 < pygame.mouse.get_pos()[0] < 135 and 500 < pygame.mouse.get_pos()[
                1] < 590:
                reset = True
                running = False
                break
        pygame.display.update()
    if reset:
        start()


while title:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            out()
        elif pygame.mouse.get_pressed()[0] == 1 or pygame.key.get_pressed()[13] == 1:
            pygame.mixer.music.load('click2.mp3')
            pygame.mixer.music.play()
            thread_stop = True
            screen2()
            title = False
            break
    if not thread_start:
        window.fill([255, 0, 0])
        title_card(270, 150)
        game_name(10, 300)
    pygame.display.update()

start()
