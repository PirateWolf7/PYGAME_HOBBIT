# IMPORTAÇÕES
import pygame
import sys
from pygame.locals import *
import os
from pygame import mixer
# DEFINIR TEMPO MÁXIMO PARA 1000 MINUTOS +/-
sys.setrecursionlimit(1000000)

pygame.init()
icon = pygame.image.load(os.path.join('pngs', 'icon.jpg'))
pygame.display.set_icon(icon)

# DEFINIÇÃO DE VARIÁVEIS
altura_chao = 600
largura_tela = 1200
altura_tela = 676
tamanho_tela = (largura_tela, altura_tela)
win = pygame.display.set_mode((largura_tela, altura_tela))
bg_menu = pygame.image.load(os.path.join('pngs', 'bg_menu1.1.jpg'))
bg_niveis = pygame.image.load(os.path.join('pngs', 'bg_niveis.jpg'))
bg3 = pygame.image.load(os.path.join('pngs', 'fundo3.jpg'))
bg3 = pygame.transform.scale(bg3,  (largura_tela, altura_tela))
nivel_rect = pygame.image.load(os.path.join('pngs', 'Nivel Rect.png'))
imagem_option = pygame.image.load(os.path.join('pngs', 'imagem_options.png'))
creditos_imagem = pygame.image.load(
    os.path.join('pngs', 'creditos_imagem.png'))
bilbo_imagem = pygame.image.load(os.path.join('pngs', 'bilbo.jpg'))
bilbo_imagem = pygame.transform.scale(bilbo_imagem, (200, 112.5))
font_size = 30
font = pygame.font.SysFont("", font_size)
score = 0
sprint = 1
perigo = False
game_over = False
fim_nivel1 = False
fim_nivel2 = False
fim_nivel3 = False
nivel = 0
derrotaCount = 0
vitoriaCount = 0
# definir a meta
xi = 1020
yi = 300
xf = xi
yf = 650
cor_meta = (255, 255, 0)
# SONS
au = pygame.mixer.Sound(os.path.join('sons', 'auuu trimmed.wav'))
au.set_volume(0.2)
ogre_som = pygame.mixer.Sound(os.path.join(
    'sons', 'barulhos ogre trimmed.wav'))
ogre_som.set_volume(0.2)
chapada = pygame.mixer.Sound(os.path.join('sons', 'chapada trimmed.wav'))
chapada.set_volume(0.2)
fisga = pygame.mixer.Sound(os.path.join('sons', 'Fisga shoot.wav'))
fisga.set_volume(0.2)
dragaum_voando = pygame.mixer.Sound(os.path.join('sons', 'dragaum Voando.wav'))
dragaum_voando.set_volume(0.2)
fogo_som = pygame.mixer.Sound(os.path.join(
    'sons', 'fogo do dragaum trimmed.wav'))
fogo_som.set_volume(0.2)
vitoria_som = pygame.mixer.Sound(os.path.join('sons', 'vitoria trimmed.wav'))
vitoria_som.set_volume(0.2)
derrota_som = pygame.mixer.Sound(os.path.join('sons', 'you lost! trimmed.wav'))
derrota_som.set_volume(0.2)

# CLASSES


class Player(object):
    def __init__(self, x, y, largura_player, altura_player):
        self.x = x
        self.y = y
        self.largura_player = largura_player
        self.altura_player = altura_player
        self.tamanho_player = (largura_player, altura_player)
        self.vel_i = 10
        self.vel = 1
        self.isJump = False
        self.jumpCount = 4
        self.jumpCountFrame = 0
        self.left = False
        self.right = False
        self.walkCount = 0
        self.hitcount = 0
        self.virado = 1  # é 1 se estiver virado para a direita e -1 para a esquerda
        self.paradoCount = 0
        self.hitbox = pygame.Rect(self.x, self.y, 64, 64)
        self.cor = (255, 255, 0)
        self.vidas = 3
        self.colisao = 0
        self.limite = 0
        self.ataque = 0
        self.atacando = 0
        self.ataqueCount = 0
        self.bloco = 0
        self.blocoCount = 0

    def draw(self, win):
        if hobbit.walkCount + 1 >= 10:
            hobbit.walkCount = 0
        if hobbit.left and self.bloco == 0 and hobbit.atacando == 0:
            win.blit(mover_esquerda[hobbit.walkCount//1], (hobbit.x, hobbit.y))
            hobbit.walkCount += 1*sprint
        elif hobbit.right and self.bloco == 0 and hobbit.atacando == 0:
            win.blit(mover_direita[hobbit.walkCount//(1)],
                     (hobbit.x, hobbit.y))
            hobbit.walkCount += 1*sprint
        elif hobbit.isJump and hobbit.bloco == 0 and hobbit.atacando == 0:
            if hobbit.virado == 1:
                win.blit(
                    salto_direita[hobbit.jumpCountFrame//1], (hobbit.x, hobbit.y))
            else:
                win.blit(
                    salto_esquerda[hobbit.jumpCountFrame//1], (hobbit.x, hobbit.y))
        else:
            if hobbit.paradoCount == 4:
                hobbit.paradoCount = 0
            if hobbit.virado == 1 and hobbit.atacando == 0 and hobbit.bloco == 0:
                win.blit(
                    parado_direita[hobbit.paradoCount//1], (hobbit.x, hobbit.y))
                hobbit.paradoCount += 1
            elif hobbit.virado == -1 and hobbit.atacando == 0 and hobbit.bloco == 0:
                win.blit(
                    parado_esquerda[hobbit.paradoCount], (hobbit.x, hobbit.y))
                hobbit.paradoCount += 1
        if hobbit.atacando == 1 and hobbit.bloco == 0:
            if hobbit.virado == 1:
                win.blit(
                    ataque_direita[hobbit.ataqueCount], (hobbit.x, hobbit.y))
                hobbit.ataqueCount += 1
            if hobbit.virado == -1:
                win.blit(
                    ataque_esquerda[hobbit.ataqueCount], (hobbit.x, hobbit.y))
                hobbit.ataqueCount += 1
            if hobbit.ataqueCount == 17:
                hobbit.ataqueCount = 0
                hobbit.atacando = 0
        if hobbit.bloco == 1:
            if hobbit.virado == 1:
                win.blit(bloco_direita[hobbit.blocoCount],
                         (hobbit.x, hobbit.y))
                hobbit.blocoCount += 1
            if hobbit.virado == -1:
                win.blit(bloco_esquerda[hobbit.blocoCount],
                         (hobbit.x, hobbit.y))
                hobbit.blocoCount += 1

            if hobbit.blocoCount == 3:
                hobbit.blocoCount = 0
        if hobbit.colisao == 1:
            au.play()
            if hobbit.right:
                win.blit(hit_direita[1], (hobbit.x, hobbit.y))
            if hobbit.left:
                win.blit(hit_esquerda[1], (hobbit.x, hobbit.y))
            hobbit.colisao = 0

        self.hitbox = pygame.Rect(self.x+120, self.y+100, 60, 85)


# CRIAÇÃO DO PLAYER
hobbit = Player(100, altura_chao-150, 300, 300)


class Inimigos(object):
    def __init__(self, x, y, largura_inimigo, altura_inimigo, fim):
        self.x = x
        self.y = y
        self.largura_inimigo = largura_inimigo
        self.altura_inimigo = altura_inimigo
        self.tamanho_inimigo = (largura_inimigo, altura_inimigo)
        self.fim = fim
        self.caminho = [self.x, self.fim]
        self.walkCount = 0
        self.vel = 3
        self.virado = 1  # é 1 se estiver virado para a direita e -1 para a esquerda
        self.hitbox = (self.x, self.y, 31, 57)
        self.zona = (self.x, self.y, 300, 300)
        self.visible = True
        self.saude = 9
        self.vel_relativa = 0
        self.walkRight = []
        self.walkLeft = []
        self.idleRight = []
        self.idelLeft = []
        self.ataqueR = []
        self.ataqueL = []

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 11:
                self.walkCount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkCount//1], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.walkLeft[self.walkCount//1], (self.x, self.y))
                self.walkCount += 1
            # barra de vida do goblin
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0]-10, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(
                win, (0, 128, 0), (self.hitbox[0]-10, self.hitbox[1] - 20, 50 - 5 * (9 - self.saude), 10))
            # hitbox do goblin
            self.hitbox = pygame.Rect(self.x+35, self.y+10, 31, 75)

    def draw_nivel2(self, win):
        if self.visible:
            if self.walkCount >= 5:
                self.walkCount = 0
            win.blit(self.idleLeft[self.walkCount], (self.x, self.y))
            self.walkCount += 1
            # barra de vida do goblin
            # parte vermelha que fica por trás
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0]-10, self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(
                win, (0, 128, 0), (self.hitbox[0]-10, self.hitbox[1] - 20, 50 - 5 * (9 - self.saude), 10))
            # hitbox do goblin
            self.hitbox = pygame.Rect(self.x+35, self.y+30, 31, 50)

    def draw_nivel2_goblin2(self, win):
        self.move()
        if self.visible:
            if perigo == False:
                if self.walkCount + 1 >= 7:
                    self.walkCount = 0
                if self.vel > 0:
                    win.blit(
                        self.walkRight[self.walkCount//1], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(
                        self.walkLeft[self.walkCount//1], (self.x, self.y))
                    self.walkCount += 1
            else:
                if self.walkCount + 1 >= 4:
                    self.walkCount = 0
                if self.vel > 0:
                    win.blit(self.ataqueR[self.walkCount//1], (self.x, self.y))
                    self.walkCount += 1
                else:
                    win.blit(self.ataqueL[self.walkCount//1], (self.x, self.y))
                    self.walkCount += 1
            # barra de vida do goblin
            # parte vermelha que fica por trás
            pygame.draw.rect(win, (255, 0, 0),
                             (self.hitbox[0]-10, self.hitbox[1] - 20, 50, 10))
            # parte verde que vai diminuindo 10% a cada saude que diminui
            pygame.draw.rect(
                win, (0, 128, 0), (self.hitbox[0]-10, self.hitbox[1] - 20, 50 - 5 * (9 - self.saude), 10))
            # hitbox do goblin
            self.hitbox = pygame.Rect(self.x+35, self.y+30, 31, 50)
            # hitbox da área para ativar o ataque do goblin (área de perigo)
            self.zona = pygame.Rect(self.x-102, self.y-102, 300, 300)

    def draw_nivel3(self, win):
        if self.visible:
            if self.walkCount >= 4:
                self.walkCount = 0
            win.blit(self.ataqueL[self.walkCount], (self.x, self.y))
            self.walkCount += 1
            # barra de vida do DRAGAO
            # parte vermelha que fica por trás
            pygame.draw.rect(win, (255, 0, 0), (largura_tela /
                             2-200, self.hitbox[1] - 20, 500, 10))
            pygame.draw.rect(win, (0, 128, 0), (largura_tela/2-200,
                             self.hitbox[1] - 20, 500 - 50 * (9 - self.saude), 10))
            # hitbox do DRAGAO
            self.hitbox = pygame.Rect(self.x+150, self.y+30, 450, 450)
            nome_dragao = get_font(70).render("Dragaum", True, (255, 255, 255))
            win.blit(nome_dragao, (550, 30))
        else:
            # vida do dragao quando acaba fica toda vermelha
            pygame.draw.rect(win, (255, 0, 0), (largura_tela /
                             2-200, self.hitbox[1] - 20, 500, 10))
            nome_dragao = get_font(70).render("Dragaum", True, (255, 255, 255))
            win.blit(nome_dragao, (550, 30))

    def move(self):
        if self.vel > 0:  # se estiver a andar para a direira
            if self.x < self.caminho[1]:  # se ainda não chegou ao fim
                self.x += self.vel  # anda mais um passo
            else:  # se chegou ao fim
                self.vel = self.vel * -1  # dá a volta
                self.walkCount = 0  # faz reset ao walkCount
        else:  # se estiver a andar para a esquerda
            if self.x > self.caminho[0]:  # se ainda não chegou ao inicio
                self.x += self.vel-goblin.vel_relativa  # anda mais um passo
            else:  # se chegou ao inicio
                self.vel = self.vel * -1  # dá a volta
                self.walkCount = 0  # faz reset ao walkCount

    def hit(self):
        chapada.play()
        if self.saude > 0:
            self.saude -= 1
        else:
            self.visible = False


# DEFINIÇÃO DOS INIMIGOS
goblin = Inimigos(500, altura_chao-50, 100, 100, 600)
goblin2 = Inimigos(500, altura_chao-60, 100, 100, 600)
goblin3 = Inimigos(700, altura_chao-60, 100, 100, 800)
dragao = Inimigos(700, 0, 100, 100, 800)

# LOAD DOS FRAMES DOS INIMIGOS
goblin.walkRight = []
for i in range(1, 12):
    frame = pygame.image.load(os.path.join('pngs', f'R{i}E.png'))
    frame = pygame.transform.scale(frame, (100, 100))
    goblin.walkRight.append(frame)
goblin.walkLeft = []
for i in range(1, 12):
    frame = pygame.transform.flip(goblin.walkRight[i-1], True, False)
    goblin.walkLeft.append(frame)

goblin2.idleRight = []
for i in range(1, 6):
    frame = pygame.image.load(os.path.join(
        'pngs/goblin nivel2', f'Idle{i}.png'))
    goblin2.idleRight.append(frame)
goblin2.idleLeft = []
for i in range(1, 6):
    frame = pygame.transform.flip(goblin2.idleRight[i-1], True, False)
    goblin2.idleLeft.append(frame)

goblin3.idleRight = []
for i in range(1, 6):
    frame = pygame.image.load(os.path.join(
        'pngs/goblin nivel2', f'Idle{i}.png'))
    goblin3.idleRight.append(frame)
goblin3.idleLeft = []
for i in range(1, 6):
    frame = pygame.transform.flip(goblin3.idleRight[i-1], True, False)
    goblin3.idleLeft.append(frame)

goblin3.walkRight = []
for i in range(1, 8):
    frame = pygame.image.load(os.path.join(
        'pngs/goblin nivel2', f'walkR{i}.png'))
    goblin3.walkRight.append(frame)
goblin3.walkLeft = []
for i in range(1, 8):
    frame = pygame.transform.flip(goblin3.walkRight[i-1], True, False)
    goblin3.walkLeft.append(frame)

goblin3.ataqueR = []
for i in range(1, 5):
    frame = pygame.image.load(os.path.join(
        'pngs/goblin nivel2', f'ataqueR{i}.png'))
    goblin3.ataqueR.append(frame)
goblin3.ataqueL = []
for i in range(1, 5):
    frame = pygame.transform.flip(goblin3.ataqueR[i-1], True, False)
    goblin3.ataqueL.append(frame)

dragao.ataqueL = []
for i in range(1, 5):
    frame = pygame.image.load(os.path.join(
        'pngs/dragao_nivel3', f'dragao{i}.png'))
    frame = pygame.transform.scale(frame, (500, 500))
    dragao.ataqueL.append(frame)


class Projetil(object):
    def __init__(self, x, y, raio, cor, virado):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.virado = virado
        self.vel = 25 * virado
        self.forma = pygame.Rect(self.x, self.y, self.raio*2, self.raio*2)

    def draw(self, win):
        pygame.draw.ellipse(win, self.cor, self.forma)


# DEFINIÇÃO DA LISTA DE BALAS
balas = []

# DEFINIÇÃO DO FOGO DO DRAGÃO (LISTA (fogos) COM 3 FRAMES (fogo1, fogo2, fogo3))
fogoCount = 0
fogo1 = pygame.image.load(os.path.join('pngs/dragao_nivel3', f'fogo1.png'))
fogo1 = pygame.transform.scale(fogo1, (100, 100))
fogo2 = pygame.image.load(os.path.join('pngs/dragao_nivel3', f'fogo2.png'))
fogo2 = pygame.transform.scale(fogo2, (100, 100))
fogo3 = pygame.image.load(os.path.join('pngs/dragao_nivel3', f'fogo3.png'))
fogo3 = pygame.transform.scale(fogo3, (100, 100))
fogos = [fogo1, fogo2, fogo3]
for fogo in fogos:
    fogo_x = xi-350
    fogo_y = 270
    fogo_vel = 10
    fogo_hitbox = pygame.Rect(fogo_x+10, fogo_y+50, 50, 40)


class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(
                self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(
                self.text_input, True, self.base_color)


# LOAD DOS FRAMES PARA O PLAYER, BACKGROUND, ETC
parado_direita = []
for i in range(1, 5):
    frame = pygame.image.load(os.path.join('pngs', f'Hobbit - idle{i}.png'))
    frame = pygame.transform.scale(frame, hobbit.tamanho_player)
    parado_direita.append(frame)
parado_esquerda = []
for i in range(1, 5):
    frame = pygame.transform.flip(parado_direita[i-1], True, False)
    frame = pygame.transform.scale(frame, hobbit.tamanho_player)
    parado_esquerda.append(frame)
mover_direita = []
for i in range(1, 11):
    frame = pygame.image.load(os.path.join('pngs', f'Hobbit - run{i}.png'))
    frame = pygame.transform.scale(frame, (300, 300))
    mover_direita.append(frame)
mover_esquerda = []
for i in range(1, 11):
    frame = pygame.transform.flip(mover_direita[i-1], True, False)
    frame = pygame.transform.scale(frame, (300, 300))
    mover_esquerda.append(frame)
salto_direita = []
for i in range(1, 11):
    frame = pygame.image.load(os.path.join('pngs', f'Hobbit - jumpt{i}.png'))
    frame = pygame.transform.scale(frame, (300, 300))
    salto_direita.append(frame)
salto_esquerda = []
for i in range(1, 11):
    frame = pygame.transform.flip(salto_direita[i-1], True, False)
    frame = pygame.transform.scale(frame, (300, 300))
    salto_esquerda.append(frame)
hit_direita = []
for i in range(1, 5):
    frame = pygame.image.load(os.path.join('pngs', f'Hobbit - hit{i}.png'))
    frame = pygame.transform.scale(frame, (300, 300))
    hit_direita.append(frame)
hit_esquerda = []
for i in range(1, 5):
    frame = pygame.transform.flip(hit_direita[i-1], True, False)
    frame = pygame.transform.scale(frame, (300, 300))
    hit_esquerda.append(frame)
ataque_direita = []
for i in range(1, 18):
    frame = pygame.image.load(os.path.join('pngs', f'Hobbit - attack{i}.png'))
    frame = pygame.transform.scale(frame, (300, 300))
    ataque_direita.append(frame)
ataque_esquerda = []
for i in range(1, 18):
    frame = pygame.transform.flip(ataque_direita[i-1], True, False)
    frame = pygame.transform.scale(frame, (300, 300))
    ataque_esquerda.append(frame)
bloco_direita = []
for i in range(10, 13):
    frame = pygame.image.load(os.path.join('pngs', f'Hobbit - block{i}.png'))
    frame = pygame.transform.scale(frame, (300, 300))
    bloco_direita.append(frame)
bloco_esquerda = []
for i in range(10, 13):
    frame = pygame.transform.flip(bloco_direita[i-10], True, False)
    frame = pygame.transform.scale(frame, (300, 300))
    bloco_esquerda.append(frame)

bg = []
for i in range(1, 4):
    frame = pygame.image.load(os.path.join(
        'pngs', f'background_layer_{i}.png')).convert_alpha()
    frame = pygame.transform.scale(frame, tamanho_tela)
    bg.append(frame)

chao1 = pygame.image.load(os.path.join('pngs', 'floor_1.png')).convert_alpha()
chao1 = pygame.transform.scale(chao1, (1000, 100))
chao2 = pygame.image.load(os.path.join('pngs', 'floor_2.png')).convert_alpha()
chao2 = pygame.transform.scale(chao2, (1000, 100))
chao3 = pygame.image.load(os.path.join('pngs', 'floor_3.png')).convert_alpha()
chao3 = pygame.transform.scale(chao3, (1000, 100))
porta1 = pygame.image.load(os.path.join('pngs', 'Living gazebo2.png'))
porta1 = pygame.transform.scale(porta1, (500, 500))
porta12 = pygame.image.load(os.path.join('pngs', 'Living gazebo22.png'))
porta2 = pygame.image.load(os.path.join('pngs', 'porta2.png'))
porta2 = pygame.transform.scale(porta2, (500, 500))
porta22 = pygame.image.load(os.path.join('pngs', 'porta22.png'))
porta22 = pygame.transform.scale(porta22, (500, 500))
porta23 = pygame.image.load(os.path.join('pngs', 'porta23.png'))
porta23 = pygame.transform.scale(porta23, (500, 500))
porta3 = pygame.image.load(os.path.join('pngs', 'porta3.png'))
porta3 = pygame.transform.scale(porta3, (500, 500))
vida = pygame.image.load(os.path.join('pngs', 'heart.png'))
vida2 = pygame.image.load(os.path.join('pngs', 'heart2.png'))
pedra = pygame.image.load(os.path.join('pngs', 'pedra.png'))
pedra = pygame.transform.scale(pedra, (100, 100))

clock = pygame.time.Clock()

# FUNÇÕES

bg_image_width = bg[0].get_width()


def draw_bg():
    # DESENHAR OS VÁRIOS BACKGROUNDS
    if nivel == 1 or nivel == 2:
        for w in range(50):
            win.blit(bg[0], ((w*bg_image_width)+scroll1, 0))
            win.blit(bg[1], ((w*bg_image_width)+scroll2, 0))
            win.blit(bg[2], ((w*bg_image_width)+scroll3, 0))
    if nivel == 3:
        win.blit(bg3, (0, 0))
    # CORAÇÕES QUE DESAPARECEM QUANDO O HOBBIT PERDE VIDA:
    if hobbit.vidas == 3:
        win.blit(vida, (1100, 20))
        win.blit(vida, (1045, 20))
        win.blit(vida, (990, 20))
    elif hobbit.vidas == 2:
        win.blit(vida2, (1100, 20))
        win.blit(vida, (1045, 20))
        win.blit(vida, (990, 20))
    elif hobbit.vidas == 1:
        win.blit(vida2, (1100, 20))
        win.blit(vida2, (1045, 20))
        win.blit(vida, (990, 20))
    else:
        win.blit(vida2, (1100, 20))
        win.blit(vida2, (1045, 20))
        win.blit(vida2, (990, 20))


def var_reset():  # RESETAR VARIÁVEIS PARA MUDANÇAS DE JANELA
    global scroll1, scroll2, scroll3, xi, yi, xf, yf, fim_nivel1, fim_nivel2, fim_nivel3, game_over, perigo, balas, fogo_x, fogo_y, derrota_som, derrotaCount, vitoriaCount
    scroll1 = 0
    scroll2 = 0
    scroll3 = 0
    hobbit.x = 100
    hobbit.y = altura_chao-150
    hobbit.virado = 1
    xi = 1020
    yi = 300
    xf = xi
    yf = 650
    fim_nivel1 = False
    fim_nivel2 = False
    fim_nivel3 = False
    goblin.x = 500
    goblin.y = altura_chao-50
    goblin.fim = 600
    hobbit.vidas = 3
    game_over = False
    goblin.caminho[0] = goblin.x
    goblin.caminho[1] = goblin.fim
    goblin2.x = 500
    goblin3.x = 700
    goblin3.fim = 800
    goblin3.caminho[0] = goblin3.x
    goblin3.caminho[1] = goblin3.fim
    perigo = False
    balas = []
    dragao.visible = True
    fogo_y = 270
    fogo_x = xi-350
    dragao.x = 700
    dragao.y = 0
    dragao.saude = 9
    goblin.saude = 9
    goblin2.saude = 9
    goblin3.saude = 9
    hobbit.atacando = 0
    derrotaCount = 0
    vitoriaCount = 0


def get_font(size):  # RETORNA O FICHEIRO TTF COM A FONTE
    # return pygame.font.Font("pngs/Elfica.ttf", size)
    return pygame.font.Font("pngs/Mistral.ttf", size)


def draw_game_over():
    global derrotaCount

    if derrotaCount == 0:
        derrota_som.play(0)
        derrotaCount += 1

    placa_game_over = pygame.Rect(
        largura_tela/2-400, altura_tela/2-200, 800, 400)
    pygame.draw.rect(win, "gold3", placa_game_over)
    placa_game_over_titulo = get_font(70).render(
        "GAME OVER", True, (255, 255, 255))
    win.blit(placa_game_over_titulo, (largura_tela/2-300, altura_tela/2-200))
    PLAY_REPEAT.update(win)


def draw_fim_nivel1():
    global vitoriaCount

    if vitoriaCount == 0:
        vitoria_som.play(0)
        vitoriaCount += 1

    placa_fim_nivel1 = pygame.Rect(
        largura_tela/2-400, altura_tela/2-200, 800, 400)
    pygame.draw.rect(win, "gold3", placa_fim_nivel1)
    placa_fim_nivel1_titulo = get_font(70).render(
        "Nível 1 passado", True, (255, 255, 255))
    win.blit(placa_fim_nivel1_titulo, (largura_tela/2-300, altura_tela/2-200))
    n_vidas = get_font(50).render(
        f"Vidas restantes: {hobbit.vidas}", True, (255, 255, 255))
    win.blit(n_vidas, (largura_tela/2-380, altura_tela/2-80))
    n_pontos = get_font(50).render(f"Pontos: {score}", True, (255, 255, 255))
    win.blit(n_pontos, (largura_tela/2-380, altura_tela/2-10))
    PLAY_NEXT.update(win)


def draw_fim_nivel2():
    global vitoriaCount

    if vitoriaCount == 0:
        vitoria_som.play(0)
        vitoriaCount += 1

    placa_fim_nivel2 = pygame.Rect(
        largura_tela/2-400, altura_tela/2-200, 800, 400)
    pygame.draw.rect(win, "gold3", placa_fim_nivel2)
    placa_fim_nivel2_titulo = get_font(70).render(
        "Nível 2 passado", True, (255, 255, 255))
    win.blit(placa_fim_nivel2_titulo, (largura_tela/2-300, altura_tela/2-200))
    n_vidas = get_font(50).render(
        f"Vidas restantes: {hobbit.vidas}", True, (255, 255, 255))
    win.blit(n_vidas, (largura_tela/2-380, altura_tela/2-80))
    n_pontos = get_font(50).render(f"Pontos: {score}", True, (255, 255, 255))
    win.blit(n_pontos, (largura_tela/2-380, altura_tela/2-10))
    PLAY_NEXT.update(win)


def draw_fim_nivel3():
    global vitoriaCount

    if vitoriaCount == 0:
        vitoria_som.play(0)
        vitoriaCount += 1

    placa_fim_nivel3 = pygame.Rect(
        largura_tela/2-400, altura_tela/2-200, 800, 400)
    pygame.draw.rect(win, "gold3", placa_fim_nivel3)
    placa_fim_nivel3_titulo = get_font(70).render(
        "Nível 3 passado", True, (255, 255, 255))  # o hat_centered poe o fundo do texto preto
    win.blit(placa_fim_nivel3_titulo, (largura_tela/2-300, altura_tela/2-200))
    n_vidas = get_font(50).render(
        f"Vidas restantes: {hobbit.vidas}", True, (255, 255, 255))
    win.blit(n_vidas, (largura_tela/2-380, altura_tela/2-80))
    n_pontos = get_font(50).render(f"Pontos: {score}", True, (255, 255, 255))
    win.blit(n_pontos, (largura_tela/2-380, altura_tela/2-10))

    PLAY_NEXT.update(win)


def redrawGameWindow_nivel1():
    global score
    global derrotaCount

    draw_bg()  # desenha os bg
    for i in range(50):  # desenha o chao1
        win.blit(chao1, (xi-1100+i*1000, 600))
    win.blit(porta1, (xi-280, 250))
    nivel1_titulo = get_font(70).render(
        "Nível 1", True, "#b68f40")  # definição do título
    win.blit(nivel1_titulo, (200, 0))  # desenha o título
    # definição do texto dos pontos
    pontos = get_font(30).render(f"Score: {score}", True, "gold")
    win.blit(pontos, (1000, 100))  # desenha os pontos
    hobbit.draw(win)  # desenha o player
    goblin.draw(win)  # desenha o goblin

    for bala in balas:
        bala.draw(win)  # desenha as balas

    win.blit(porta12, (xi-280, 250))  # desenha a porta12
    win.blit(porta12, (xi-240, 250))
    win.blit(porta12, (xi-200, 250))
    win.blit(porta12, (xi-160, 250))
    win.blit(porta12, (xi-120, 250))

    PLAY_BACK.update(win)  # desenha o botão back dentro do nível 1

    if fim_nivel1:
        draw_fim_nivel1()  # desenha a placa de fim de nível 1
    if game_over:
        draw_game_over()  # desenha a placa de game over

    pygame.display.update()
    play_nivel1()  # VOLTAR PARA A FUNÇÃO PRINCIPAL DO NÍVEL 1


def redrawGameWindow_nivel2():
    global score

    draw_bg()
    for i in range(50):
        win.blit(chao2, (xi-1100+i*1000, 610))
    win.blit(porta1, (xi-1200, 250))
    win.blit(porta2, (xi-280, 250))
    nivel2_titulo = get_font(70).render("Nível 2", True, "#b68f40")
    win.blit(nivel2_titulo, (200, 0))
    pontos = get_font(30).render(f"Score: {score}", True, "gold")
    win.blit(pontos, (1000, 100))
    hobbit.draw(win)
    goblin2.draw_nivel2(win)
    goblin3.draw_nivel2_goblin2(win)

    for bala in balas:
        bala.draw(win)  # desenhar as balas

    win.blit(porta23, (xi-100, 250))
    win.blit(porta22, (xi-280, 250))

    PLAY_BACK.update(win)  # mostra o botao back dentro do play

    if fim_nivel2:
        draw_fim_nivel2()
    if game_over:
        draw_game_over()

    pygame.display.update()
    play_nivel2()


def redrawGameWindow_nivel3():
    global score
    global fogo_hitbox
    global fogoCount

    draw_bg()
    for i in range(50):
        win.blit(chao3, (xi-1100+i*1000, 610))

    win.blit(porta3, (xi-1200, 250))
    nivel3_titulo = get_font(70).render("Nível 3", True, "#b68f40")
    win.blit(nivel3_titulo, (200, 0))
    pontos = get_font(30).render(f"Score: {score}", True, "gold")
    win.blit(pontos, (1000, 100))
    hobbit.draw(win)
    dragao.draw_nivel3(win)

    for bala in balas:
        bala.draw(win)  # desenhar as balas

    # ANIMAÇÃO DO FOGO
    if fogoCount == 3:
        fogoCount = 0
    win.blit(fogos[fogoCount], (fogo_x, fogo_y))
    fogoCount += 1
    fogo_hitbox = pygame.Rect(fogo_x+10, fogo_y+50, 50, 40)

    win.blit(pedra, (xi-50, 540))
    PLAY_BACK.update(win)

    if fim_nivel3 == True:
        draw_fim_nivel3()
    if game_over:
        draw_game_over()

    pygame.display.update()
    play_nivel3()

# JANELAS(CREDITOS / PLAY / NÍVEIS / HOW TO PLAY/ MENU)


def creditos_janela():  # ECRÃ DOS CRÉDITOS
    while True:
        pygame.display.set_caption("CRÉDITOS")
        CREDITOS_MOUSE_POS = pygame.mouse.get_pos()
        win.fill("white")
        win.blit(creditos_imagem, (0, 0))
        win.blit(bilbo_imagem, (900, 450))
        CREDITOS_BACK = Button(image=None, pos=(1000, 600),
                               text_input="BACK", font=get_font(40), base_color="Black", hovering_color="Green")
        CREDITOS_BACK.changeColor(CREDITOS_MOUSE_POS)
        CREDITOS_BACK.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if CREDITOS_BACK.checkForInput(CREDITOS_MOUSE_POS):
                    menu()

        pygame.display.update()


def play():  # ECRÃ DOS NÍVEIS

    # carrega a musica desta janela
    mixer.music.load(os.path.join(
        'musica', 'The Fellowship of the Ring Soundtrack-09-Many Meetings.mp3'))
    mixer.music.play(-1)  # toca a musica em loop
    mixer.music.set_volume(0.1)  # altera o volume para todas as musicas

    while True:
        pygame.display.set_caption("MAPA DOS NÍVEIS")
        win.blit(bg_niveis, (0, 0))
        PLAY_MOUSE_POS = pygame.mouse.get_pos()
        play_titulo = get_font(70).render("NÍVEIS", True, "brown")
        win.blit(play_titulo, (40, 30))
        nivel1 = Button(image=nivel_rect, pos=(200, 200), text_input="Nível 1", font=get_font(
            40), base_color="burlywood1", hovering_color="gold")
        nivel2 = Button(image=nivel_rect, pos=(500, 200), text_input="Nível 2", font=get_font(
            40), base_color="burlywood1", hovering_color="gold")
        nivel3 = Button(image=nivel_rect, pos=(800, 200), text_input="Nível 3", font=get_font(
            40), base_color="burlywood1", hovering_color="gold")
        back = Button(image=None, pos=(70, 450), text_input="BACK", font=get_font(
            40), base_color="brown", hovering_color="burlywood1")
        back.changeColor(PLAY_MOUSE_POS)

        for button in [nivel1, nivel2, nivel3, back]:
            button.changeColor(PLAY_MOUSE_POS)
            button.update(win)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if nivel1.checkForInput(PLAY_MOUSE_POS):
                    # DEFINIR A MÚSICA E OS SONS PRESENTES NO NÍVEL 1
                    mixer.music.load(os.path.join(
                        'musica', 'The Fellowship of the Ring ST-05-The Black Rider.mp3'))
                    mixer.music.play(-1)
                    ogre_som.play(-1)
                    # ENTRAR NO NÍVEL 1
                    play_nivel1()
                if nivel2.checkForInput(PLAY_MOUSE_POS):
                    mixer.music.load(os.path.join(
                        'musica', 'The Fellowship of the Ring Soundtrack-07-A Knife in the Dark.mp3'))
                    mixer.music.play(-1)
                    ogre_som.play(-1)
                    play_nivel2()
                if nivel3.checkForInput(PLAY_MOUSE_POS):
                    mixer.music.load(os.path.join(
                        'musica', 'LOTR TRIMMED BALROG.mp3'))
                    mixer.music.play(-1)
                    dragaum_voando.play(-1)
                    play_nivel3()
                if back.checkForInput(PLAY_MOUSE_POS):
                    menu()
        pygame.display.update()


# variáveis para a definição da velocidade de cada background nos níveis 1 e 2
scroll1 = 0
scroll2 = 0
scroll3 = 0


def play_nivel1():  # ECRÃ DO NÍVEL 1
    global xi, yi, xf, yf, PLAY_MOUSE_POS, PLAY_BACK, PLAY_NEXT, PLAY_REPEAT, scroll1, scroll2, scroll3, sprint, fim_nivel1, game_over, bala, balas, score, nivel, fps

    # DEFINIÇÃO DE UMA VARIVEL PARA A POSIÇÃO DO RATO
    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    # DEFINIÇÃO DE BUTÕES
    PLAY_BACK = Button(image=None, pos=(100, 50), text_input="BACK", font=get_font(
        40), base_color="olive", hovering_color="gold")
    PLAY_BACK.changeColor(PLAY_MOUSE_POS)
    PLAY_NEXT = Button(image=pygame.image.load("pngs/Next Rect.png"), pos=(300, 600),
                       text_input="NEXT", font=get_font(50), base_color="#d7fcd4", hovering_color="GOLD")
    PLAY_NEXT.changeColor(PLAY_MOUSE_POS)
    # ESTE NAO PODE FICAR NAS MESMAS COORDENADAS DO ANTERIOR SENAO QUANDO CLICO ELE ASSUME QUE ESTOU A CLICAR NO ANTERIOR E NAO NESETE
    PLAY_REPEAT = Button(image=pygame.image.load("pngs/Next Rect.png"), pos=(600, 600),
                         text_input="REPEAT", font=get_font(50), base_color="#d7fcd4", hovering_color="GOLD")
    PLAY_REPEAT.changeColor(PLAY_MOUSE_POS)

    nivel = 1

    pygame.display.set_caption("NÍVEL 1")

    run = True
    while run:
        pygame.time.delay(100)
        fps = 30
        clock.tick(fps)
        # COLISAO DO HOBBIT COM GOBLIN
        if goblin.visible:
            if hobbit.hitbox.colliderect(goblin.hitbox):
                hobbit.colisao = 1
                if hobbit.x+hobbit.largura_player/2 < goblin.x + goblin.largura_inimigo/2:
                    hobbit.x -= 100
                if hobbit.x+hobbit.largura_player/2 > goblin.x + goblin.largura_inimigo/2:
                    hobbit.x += 100
                if hobbit.colisao == 1:
                    if (hobbit.bloco == 0 or hobbit.bloco == 1 and hobbit.x+hobbit.largura_player/2 < goblin.x + goblin.largura_inimigo/2 and hobbit.virado == -1) or (hobbit.bloco == 1 and hobbit.x+hobbit.largura_player/2 > goblin.x + goblin.largura_inimigo/2 and hobbit.virado == 1):
                        hobbit.vidas -= 1  # RETIRAR UMA VIDA AO HOBBIT CASO COLIDA COM O GOBLIN
        else:
            ogre_som.stop()  # PARAR O SOM DO GOBLIN CASO ESTE MORRA

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    var_reset()
                    ogre_som.stop()
                    derrota_som.stop()
                    vitoria_som.stop()
                    play()
                if PLAY_NEXT.checkForInput(PLAY_MOUSE_POS):
                    var_reset()
                    mixer.music.load(os.path.join(
                        'musica', 'The Fellowship of the Ring Soundtrack-07-A Knife in the Dark.mp3'))
                    mixer.music.play(-1)
                    ogre_som.play(-1)
                    derrota_som.stop()
                    vitoria_som.stop()
                    play_nivel2()
                if PLAY_REPEAT.checkForInput(PLAY_MOUSE_POS):
                    var_reset()
                    score = 0
                    derrota_som.stop()
                    vitoria_som.stop()
                    play_nivel1()

        # BALAS
        for bala in balas:
            # COLISAO DAS BALAS COM GOBLIN
            if goblin.hitbox.colliderect(bala.forma) and goblin.visible:
                goblin.hit()
                score += 1
                balas.pop(balas.index(bala))

            # POSIÇÃO DAS BALAS
            if bala.vel > 0 and hobbit.virado > 0:
                if hobbit.limite == 1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel-hobbit.vel_i*sprint
                else:
                    bala.forma[0] += bala.vel
            elif bala.vel < 0 and hobbit.virado > 0:
                if hobbit.limite == 1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel - hobbit.vel_i*2*sprint
                bala.forma[0] += bala.vel - hobbit.vel_i*sprint
            elif bala.vel > 0 and hobbit.virado < 0:
                if hobbit.limite == -1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel + hobbit.vel_i*2*sprint
                else:
                    bala.forma[0] += bala.vel + hobbit.vel_i*sprint
            elif bala.vel < 0 and hobbit.virado < 0:
                if hobbit.limite == -1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel+hobbit.vel_i*sprint
                else:
                    bala.forma[0] += bala.vel

        # DEFINIR FUNÇÕES DE TECLAS
        teclas = pygame.key.get_pressed()
        # ataque
        # fim_nivel1 e game_over são condições de paragem de todas as teclas
        if teclas[K_SPACE] and fim_nivel1 == False and game_over == False:
            hobbit.ataque = 1
            hobbit.atacando = 1
        if hobbit.atacando == 1:  # enquanto está a atacar (animar os frames)
            if hobbit.ataqueCount == 9:  # quando passar neste frame a bala aparece
                bala = Projetil(round(hobbit.x+hobbit.largura_player // 2), round(
                    hobbit.y+hobbit.altura_player//2), 6, "brown4", hobbit.virado)
                balas.append(bala)
                fisga.play()
        else:
            hobbit.ataque = 0

        # escudo/bloco
        if teclas[K_v] and fim_nivel1 == False and game_over == False:
            hobbit.bloco = 1
        else:
            hobbit.bloco = 0

        # mudar a velocidade do player:
        if (teclas[K_b]):
            sprint = 2
        else:
            sprint = 1

        # andar para a esquerda
        if (teclas[K_LEFT] or teclas[K_a]) and (hobbit.x > 100 or scroll3 < 0) and hobbit.bloco == 0 and fim_nivel1 == False and game_over == False:
            hobbit.left = True
            hobbit.right = False
            hobbit.virado = -1
            hobbit.vel = -1
            if (hobbit.x > 100):
                hobbit.x -= hobbit.vel_i * sprint
            if 100 < hobbit.x < 800:
                hobbit.limite = 0
                scroll1 += 1 * sprint
                scroll2 += 2 * sprint
                scroll3 += 3 * sprint
                xi += hobbit.vel_i * sprint
                xf = xi
                goblin.caminho[0] += (hobbit.vel_i) * sprint
                goblin.caminho[1] += (hobbit.vel_i) * sprint
                goblin.x += (hobbit.vel_i) * sprint
            if hobbit.x <= 100 and scroll3 <= 0:
                hobbit.limite = -1
                scroll3 += 3 + hobbit.vel_i * sprint
                scroll1 = (scroll3 - 2) * 1/3
                scroll2 = (scroll3 - 1) * 2/3
                xi += hobbit.vel_i*2 * sprint
                xf = xi
                goblin.caminho[0] += (hobbit.vel_i)*2 * sprint
                goblin.caminho[1] += (hobbit.vel_i)*2 * sprint

        # andar para a direita
        elif (teclas[K_RIGHT] or teclas[K_d]) and hobbit.bloco == 0 and fim_nivel1 == False and game_over == False:
            hobbit.left = False
            hobbit.right = True
            hobbit.virado = 1
            hobbit.vel = 1
            if hobbit.x + hobbit.largura_player < largura_tela-100:
                hobbit.x += hobbit.vel_i * sprint
            if 100 < hobbit.x < 800:
                hobbit.limite = 0
                scroll1 -= 1 * sprint
                scroll2 -= 2 * sprint
                scroll3 -= 3 * sprint
                xi -= hobbit.vel_i * sprint
                xf = xi
                goblin.caminho[0] -= (hobbit.vel_i) * sprint
                goblin.caminho[1] -= (hobbit.vel_i) * sprint
                goblin.x -= (hobbit.vel_i) * sprint
            if hobbit.x >= 800:
                hobbit.limite = 1
                scroll3 -= (3 + hobbit.vel_i) * sprint
                scroll1 = (scroll3 - 2) * 1/3
                scroll2 = (scroll3 - 1) * 2/3
                xi -= hobbit.vel_i*2 * sprint
                xf = xi
                goblin.caminho[0] -= (hobbit.vel_i*2) * sprint
                goblin.caminho[1] -= (hobbit.vel_i*2) * sprint
        else:
            hobbit.left = False
            hobbit.right = False
            hobbit.walkCount = 0

        if not (hobbit.isJump):
            if (teclas[K_UP] or teclas[K_w]) and hobbit.bloco == 0 and fim_nivel1 == False and game_over == False:
                hobbit.isJump = True
        else:
            if hobbit.jumpCount >= -4 and hobbit.jumpCountFrame < 9:
                a = 20
                hobbit.y -= a * hobbit.jumpCount
                hobbit.jumpCount -= 1
                hobbit.jumpCountFrame += 1
            else:
                hobbit.isJump = False
                hobbit.jumpCount = 4
                hobbit.jumpCountFrame = 0

        # COLISAO DO PLAYER COM A META (FIM DO NÍVEL 1)
        if hobbit.hitbox.clipline(xi, yi, xi, yf) and hobbit.vidas > 0:
            fim_nivel1 = True
        elif hobbit.vidas == 0:
            game_over = True

        # CHAMADA À FUNÇÃO QUE REDESENHA A JANELA DO NÍVEL 1
        redrawGameWindow_nivel1()


def play_nivel2():
    global xi, yi, xf, yf, PLAY_MOUSE_POS, PLAY_BACK, PLAY_NEXT, PLAY_REPEAT, scroll1, scroll2, scroll3, sprint, fim_nivel2, game_over, bala, balas, score, perigo, nivel, fps

    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    PLAY_BACK = Button(image=None, pos=(100, 50), text_input="BACK", font=get_font(
        40), base_color="olive", hovering_color="gold")
    PLAY_BACK.changeColor(PLAY_MOUSE_POS)
    PLAY_NEXT = Button(image=pygame.image.load("pngs/Next Rect.png"), pos=(300, 600),
                       text_input="NEXT", font=get_font(50), base_color="#d7fcd4", hovering_color="GOLD")
    PLAY_NEXT.changeColor(PLAY_MOUSE_POS)
    # ESTE NAO PODE FICAR NAS MESMAS COORDENADAS DO ANTERIOR SENAO QUANDO CLICO ELE ASSUME QUE ESTOU A CLICAR NO ANTERIOR E NAO NESETE
    PLAY_REPEAT = Button(image=pygame.image.load("pngs/Next Rect.png"), pos=(600, 600),
                         text_input="REPEAT", font=get_font(50), base_color="#d7fcd4", hovering_color="GOLD")
    PLAY_REPEAT.changeColor(PLAY_MOUSE_POS)

    nivel = 2

    pygame.display.set_caption("NÍVEL 2")

    run = True
    while run:
        pygame.time.delay(100)
        fps = 30
        clock.tick(fps)

        if goblin2.visible == False and goblin3.visible == False:
            ogre_som.stop()

        if hobbit.hitbox.colliderect(goblin2.hitbox) and goblin2.visible:
            hobbit.colisao = 1
            if hobbit.x+hobbit.largura_player/2 < goblin2.x + goblin2.largura_inimigo/2:
                hobbit.x -= 100
            if hobbit.x+hobbit.largura_player/2 > goblin2.x + goblin2.largura_inimigo/2:
                hobbit.x += 100
            if hobbit.colisao == 1:
                hobbit.cor = (0, 0, 0)
                if (hobbit.bloco == 0 or hobbit.bloco == 1 and hobbit.x+hobbit.largura_player/2 < goblin2.x + goblin2.largura_inimigo/2 and hobbit.virado == -1) or (hobbit.bloco == 1 and hobbit.x+hobbit.largura_player/2 > goblin2.x + goblin2.largura_inimigo/2 and hobbit.virado == 1):
                    hobbit.vidas -= 1

        if hobbit.hitbox.colliderect(goblin3.hitbox) and goblin3.visible:
            hobbit.colisao = 1
            if hobbit.x+hobbit.largura_player/2 < goblin3.x + goblin3.largura_inimigo/2:
                hobbit.x -= 100
            if hobbit.x+hobbit.largura_player/2 > goblin3.x + goblin3.largura_inimigo/2:
                hobbit.x += 100
            if hobbit.colisao == 1:
                hobbit.cor = (0, 0, 0)
                if (hobbit.bloco == 0 or hobbit.bloco == 1 and hobbit.x+hobbit.largura_player/2 < goblin3.x + goblin3.largura_inimigo/2 and hobbit.virado == -1) or (hobbit.bloco == 1 and hobbit.x+hobbit.largura_player/2 > goblin3.x + goblin3.largura_inimigo/2 and hobbit.virado == 1):
                    hobbit.vidas -= 1

        # VERIFICAÇÃO DE COLISÃO COM A ZONA DE PERIGO DO GOBLIN 3
        if hobbit.hitbox.colliderect(goblin3.zona):
            perigo = True
        else:
            perigo = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    var_reset()
                    ogre_som.stop()
                    derrota_som.stop()
                    vitoria_som.stop()
                    play()
                if PLAY_NEXT.checkForInput(PLAY_MOUSE_POS):
                    var_reset()
                    mixer.music.load(os.path.join(
                        'musica', 'LOTR TRIMMED BALROG.mp3'))
                    mixer.music.play(-1)
                    dragaum_voando.play(-1)
                    derrota_som.stop()
                    vitoria_som.stop()
                    ogre_som.stop()
                    play_nivel3()
                if PLAY_REPEAT.checkForInput(PLAY_MOUSE_POS):
                    var_reset()
                    score = 0
                    derrota_som.stop()
                    vitoria_som.stop()
                    play_nivel2()

        # BALAS
        for bala in balas:
            # COLISAO DAS BALAS COM OS GOBLINS
            if goblin2.hitbox.colliderect(bala.forma) and goblin2.visible:
                goblin2.hit()
                score += 1
                balas.pop(balas.index(bala))
            if goblin3.hitbox.colliderect(bala.forma) and goblin3.visible:
                goblin3.hit()
                score += 1
                balas.pop(balas.index(bala))
            # POSIÇÃO DAS BALAS
            if bala.vel > 0 and hobbit.virado > 0:
                if hobbit.limite == 1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel-hobbit.vel_i*sprint
                else:
                    bala.forma[0] += bala.vel
            elif bala.vel < 0 and hobbit.virado > 0:
                if hobbit.limite == 1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel - hobbit.vel_i*2*sprint
                bala.forma[0] += bala.vel - hobbit.vel_i*sprint
            elif bala.vel > 0 and hobbit.virado < 0:
                if hobbit.limite == -1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel + hobbit.vel_i*2*sprint
                else:
                    bala.forma[0] += bala.vel + hobbit.vel_i*sprint
            elif bala.vel < 0 and hobbit.virado < 0:
                if hobbit.limite == -1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel+hobbit.vel_i*sprint
                else:
                    bala.forma[0] += bala.vel

        # DEFINIR FUNÇÕES DE TECLAS
        teclas = pygame.key.get_pressed()

        if teclas[K_SPACE] and fim_nivel2 == False and game_over == False:
            hobbit.ataque = 1
            hobbit.atacando = 1
        if hobbit.atacando == 1:
            if hobbit.ataqueCount == 9:
                bala = Projetil(round(hobbit.x+hobbit.largura_player // 2), round(
                    hobbit.y+hobbit.altura_player//2), 6, "brown4", hobbit.virado)
                balas.append(bala)
                fisga.play()
        else:
            hobbit.ataque = 0

        if teclas[K_v] and fim_nivel2 == False and game_over == False:
            hobbit.bloco = 1
        else:
            hobbit.bloco = 0

        if (teclas[K_b]):
            sprint = 2
        else:
            sprint = 1

        if (teclas[K_LEFT] or teclas[K_a]) and (hobbit.x > 100 or scroll3 < 0) and hobbit.bloco == 0 and fim_nivel2 == False and game_over == False:
            hobbit.left = True
            hobbit.right = False
            hobbit.virado = -1
            hobbit.vel = -1
            if (hobbit.x > 100):
                hobbit.x -= hobbit.vel_i * sprint
            if 100 < hobbit.x < 800:
                hobbit.limite = 0
                scroll1 += 1 * sprint
                scroll2 += 2 * sprint
                scroll3 += 3 * sprint
                xi += hobbit.vel_i * sprint
                xf = xi
                goblin2.x += (hobbit.vel_i) * sprint
                goblin3.caminho[0] += (hobbit.vel_i) * sprint
                goblin3.caminho[1] += (hobbit.vel_i) * sprint
                goblin3.x += (hobbit.vel_i) * sprint
            if hobbit.x <= 100 and scroll3 <= 0:
                hobbit.limite = -1
                scroll3 += 3 + hobbit.vel_i * sprint
                scroll1 = (scroll3 - 2) * 1/3
                scroll2 = (scroll3 - 1) * 2/3
                xi += hobbit.vel_i*2 * sprint
                xf = xi
        elif (teclas[K_RIGHT] or teclas[K_d]) and hobbit.bloco == 0 and fim_nivel2 == False and game_over == False:
            hobbit.left = False
            hobbit.right = True
            hobbit.virado = 1
            hobbit.vel = 1
            if hobbit.x + hobbit.largura_player < largura_tela-100:
                hobbit.x += hobbit.vel_i * sprint
            if 100 < hobbit.x < 800:
                hobbit.limite = 0
                scroll1 -= 1 * sprint
                scroll2 -= 2 * sprint
                scroll3 -= 3 * sprint
                xi -= hobbit.vel_i * sprint
                xf = xi
                goblin2.x -= (hobbit.vel_i) * sprint
                goblin3.caminho[0] -= (hobbit.vel_i) * sprint
                goblin3.caminho[1] -= (hobbit.vel_i) * sprint
                goblin3.x -= (hobbit.vel_i) * sprint
            if hobbit.x >= 800:
                hobbit.limite = 1
                scroll3 -= (3 + hobbit.vel_i) * sprint
                scroll1 = (scroll3 - 2) * 1/3
                scroll2 = (scroll3 - 1) * 2/3
                xi -= hobbit.vel_i*2 * sprint
                xf = xi
        else:
            hobbit.left = False
            hobbit.right = False
            hobbit.walkCount = 0

        if not (hobbit.isJump):
            if (teclas[K_UP] or teclas[K_w]) and fim_nivel2 == False and game_over == False:
                hobbit.isJump = True
        else:
            if hobbit.jumpCount >= -4 and hobbit.jumpCountFrame < 9:
                a = 20
                hobbit.y -= a * hobbit.jumpCount
                hobbit.jumpCount -= 1
                hobbit.jumpCountFrame += 1
            else:
                hobbit.isJump = False
                hobbit.jumpCount = 4
                hobbit.jumpCountFrame = 0

        # COLISAO DO PLAYER COM A META (FIM DO NÍVEL 2)
        if hobbit.hitbox.clipline(xi, yi, xi, yf) and hobbit.vidas > 0:
            fim_nivel2 = True
        elif hobbit.vidas == 0:
            game_over = True

        redrawGameWindow_nivel2()


def play_nivel3():  # ECRÃ DO JOGO
    global xi, yi, xf, yf, PLAY_MOUSE_POS, PLAY_BACK, PLAY_NEXT, PLAY_REPEAT, scroll1, scroll2, scroll3, sprint, fim_nivel3, game_over, bala, balas, score, perigo, fogo_y, fogo_x, fogo_vel, fogo_hitbox, nivel, fps

    PLAY_MOUSE_POS = pygame.mouse.get_pos()
    PLAY_BACK = Button(image=None, pos=(100, 50), text_input="BACK", font=get_font(
        40), base_color="olive", hovering_color="gold")
    PLAY_BACK.changeColor(PLAY_MOUSE_POS)
    PLAY_NEXT = Button(image=pygame.image.load("pngs/Next Rect.png"), pos=(300, 600),
                       text_input="NEXT", font=get_font(50), base_color="#d7fcd4", hovering_color="GOLD")
    PLAY_NEXT.changeColor(PLAY_MOUSE_POS)
    # ESTE NAO PODE FICAR NAS MESMAS COORDENADAS DO ANTERIOR SENAO QUANDO CLICO ELE ASSUME QUE ESTOU A CLICAR NO ANTERIOR E NAO NESETE
    PLAY_REPEAT = Button(image=pygame.image.load("pngs/Next Rect.png"), pos=(600, 600),
                         text_input="REPEAT", font=get_font(50), base_color="#d7fcd4", hovering_color="GOLD")
    PLAY_REPEAT.changeColor(PLAY_MOUSE_POS)

    nivel = 3

    pygame.display.set_caption("NÍVEL 3")

    run = True
    while run:
        pygame.time.delay(100)
        fps = 30
        clock.tick(fps)

        if hobbit.hitbox.colliderect(fogo_hitbox):
            hobbit.colisao = 1
            hobbit.x -= 100*hobbit.virado
            if hobbit.x+hobbit.largura_player/2 < fogo_hitbox[0]+fogo_hitbox[2]/2:
                hobbit.x -= 100
            if hobbit.x+hobbit.largura_player/2 > fogo_hitbox[0]+fogo_hitbox[2]/2:
                hobbit.x += 100
            if hobbit.colisao == 1:
                hobbit.cor = (0, 0, 0)
                if (hobbit.bloco == 0 or hobbit.bloco == 1 and hobbit.x+hobbit.largura_player/2 < fogo_hitbox[0]+fogo_hitbox[2]/2 and hobbit.virado == -1) or (hobbit.bloco == 1 and hobbit.x+hobbit.largura_player/2 > fogo_hitbox[0]+fogo_hitbox[2]/2 and hobbit.virado == 1):
                    hobbit.vidas -= 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                    var_reset()
                    dragaum_voando.stop()
                    fogo_som.stop()
                    derrota_som.stop()
                    vitoria_som.stop()
                    play()
                if PLAY_NEXT.checkForInput(PLAY_MOUSE_POS):
                    var_reset()
                    mixer.music.load(os.path.join(
                        'musica', 'TheFellowshipoftheRingST-17-The Breaking of the Fellowship.mp3'))
                    mixer.music.play(-1)
                    mixer.music.set_volume(0.1)
                    derrota_som.stop()
                    vitoria_som.stop()
                    dragaum_voando.stop()
                    fogo_som.stop()
                    creditos_janela()
                if PLAY_REPEAT.checkForInput(PLAY_MOUSE_POS):
                    var_reset()
                    score = 0
                    derrota_som.stop()
                    vitoria_som.stop()
                    play_nivel3()

        # BOLAS DE FOGO
        if fogo_y >= altura_tela and dragao.visible:  # resetar a posição do fogo quando ele desaparece da tela
            fogo_y = 270
            fogo_x = xi-350
            fogo_som.play()
        # mover o fogo
        fogo_x -= fogo_vel
        fogo_y += fogo_vel

        # SOM DO DRAGÃO
        if dragao.visible == False:
            dragaum_voando.stop()

        # BALAS
        for bala in balas:
            # COLISAO DAS BALAS COM GOBLIN
            if dragao.hitbox.colliderect(bala.forma) and dragao.visible:
                dragao.hit()
                score += 1
                balas.pop(balas.index(bala))
            # POSIÇÃO DAS BALAS
            if bala.vel > 0 and hobbit.virado > 0:
                if hobbit.limite == 1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel-hobbit.vel_i*sprint
                else:
                    bala.forma[0] += bala.vel
            elif bala.vel < 0 and hobbit.virado > 0:
                if hobbit.limite == 1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel - hobbit.vel_i*2*sprint
                bala.forma[0] += bala.vel - hobbit.vel_i*sprint
            elif bala.vel > 0 and hobbit.virado < 0:
                if hobbit.limite == -1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel + hobbit.vel_i*2*sprint
                else:
                    bala.forma[0] += bala.vel + hobbit.vel_i*sprint
            elif bala.vel < 0 and hobbit.virado < 0:
                if hobbit.limite == -1 and hobbit.walkCount != 0:
                    bala.forma[0] += bala.vel+hobbit.vel_i*sprint
                else:
                    bala.forma[0] += bala.vel

        # DEFINIR FUNÇÕES DE TECLAS
        teclas = pygame.key.get_pressed()

        if teclas[K_SPACE] and fim_nivel3 == False and game_over == False:
            hobbit.ataque = 1
            hobbit.atacando = 1
        if hobbit.atacando == 1:
            if hobbit.ataqueCount == 9:
                bala = Projetil(round(hobbit.x+hobbit.largura_player // 2), round(
                    hobbit.y+hobbit.altura_player//2), 6, "brown4", hobbit.virado)
                balas.append(bala)
                fisga.play()
        else:
            hobbit.ataque = 0

        if teclas[K_v] and fim_nivel3 == False and game_over == False:
            hobbit.bloco = 1
        else:
            hobbit.bloco = 0

        if (teclas[K_b]):
            sprint = 2
        else:
            sprint = 1

        if (teclas[K_LEFT] or teclas[K_a]) and (hobbit.x > 100 or scroll3 < 0) and hobbit.bloco == 0 and fim_nivel3 == False and game_over == False:
            hobbit.left = True
            hobbit.right = False
            hobbit.virado = -1
            hobbit.vel = -1
            if (hobbit.x > 100):
                hobbit.x -= hobbit.vel_i * sprint
            if 100 < hobbit.x < 800:
                hobbit.limite = 0
                scroll1 += 1 * sprint
                scroll2 += 2 * sprint
                scroll3 += 3 * sprint
                xi += hobbit.vel_i * sprint
                xf = xi
                dragao.x += (hobbit.vel_i) * sprint
                fogo_x += hobbit.vel_i * sprint
            if hobbit.x <= 100 and scroll3 <= 0:
                hobbit.limite = -1
                scroll3 += 3 + hobbit.vel_i * sprint
                scroll1 = (scroll3 - 2) * 1/3
                scroll2 = (scroll3 - 1) * 2/3
                xi += hobbit.vel_i*2 * sprint
                xf = xi
                dragao.x += hobbit.vel_i*2 * sprint
                fogo_x += hobbit.vel_i*2 * sprint
        elif (teclas[K_RIGHT] or teclas[K_d]) and hobbit.bloco == 0 and fim_nivel3 == False and game_over == False:
            hobbit.left = False
            hobbit.right = True
            hobbit.virado = 1
            hobbit.vel = 1
            if hobbit.x + hobbit.largura_player < largura_tela-100:
                hobbit.x += hobbit.vel_i * sprint
            if 100 < hobbit.x < 800:
                hobbit.limite = 0
                scroll1 -= 1 * sprint
                scroll2 -= 2 * sprint
                scroll3 -= 3 * sprint
                xi -= hobbit.vel_i * sprint
                xf = xi
                dragao.x -= (hobbit.vel_i) * sprint
                fogo_x -= hobbit.vel_i * sprint
            if hobbit.x >= 800:
                hobbit.limite = 1
                scroll3 -= (3 + hobbit.vel_i) * sprint
                scroll1 = (scroll3 - 2) * 1/3
                scroll2 = (scroll3 - 1) * 2/3
                xi -= hobbit.vel_i*2 * sprint
                xf = xi
                dragao.x -= (hobbit.vel_i)*2 * sprint
                fogo_x -= hobbit.vel_i * 2 * sprint
        else:
            hobbit.left = False
            hobbit.right = False
            hobbit.walkCount = 0

        if not (hobbit.isJump):
            if (teclas[K_UP] or teclas[K_w]) and fim_nivel3 == False and game_over == False:
                hobbit.isJump = True
        else:
            if hobbit.jumpCount >= -4 and hobbit.jumpCountFrame < 9:
                a = 20
                hobbit.y -= a * hobbit.jumpCount
                hobbit.jumpCount -= 1
                hobbit.jumpCountFrame += 1
            else:
                hobbit.isJump = False
                hobbit.jumpCount = 4
                hobbit.jumpCountFrame = 0

        # COLISAO DO PLAYER COM A META (FIM DO NÍVEL 3)
        if hobbit.hitbox.clipline(xi, yi, xi, yf) and hobbit.vidas > 0:
            hobbit.cor = (255, 0, 0)
            fim_nivel3 = True
        elif hobbit.vidas == 0:
            game_over = True

        redrawGameWindow_nivel3()


def options():  # ECRÃ DAS OPÇÕES (com as instruções)

    while True:
        pygame.display.set_caption("COMO JOGAR")
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        win.blit(imagem_option, (0, 0))
        OPTIONS_BACK = Button(image=None, pos=(largura_tela/2, 650), text_input="BACK",
                              font=get_font(40), base_color="Black", hovering_color="Green")
        OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_BACK.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                    menu()

        pygame.display.update()


def menu():  # ECRÃ DO MENU INICIAL
    mixer.music.set_volume(0.1)
    mixer.music.load(os.path.join('musica', 'SHIRE TRIMMED LOTR.mp3'))
    mixer.music.play(-1)

    while True:
        pygame.display.set_caption("MENU")
        win.blit(bg_menu, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        MENU_TEXT = get_font(70).render("Main Menu", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(950, 90))
        PLAY_BUTTON = Button(image=pygame.image.load("pngs/Play Rect.png"), pos=(950, 220),
                             text_input="PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        HOW_BUTTON = Button(image=pygame.image.load("pngs/Options Rect.png"), pos=(950, 350),
                            text_input="HOW TO PLAY", font=get_font(50), base_color="#d7fcd4", hovering_color="White")
        CREDITOS_BUTTON = Button(image=pygame.image.load("pngs/Quit Rect.png"), pos=(950, 480),
                                 text_input="CRÉDITOS", font=get_font(50), base_color="#d7fcd4", hovering_color="White")

        win.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, HOW_BUTTON, CREDITOS_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(win)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if HOW_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if CREDITOS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    mixer.music.load(os.path.join(
                        'musica', 'TheFellowshipoftheRingST-17-The Breaking of the Fellowship.mp3'))
                    mixer.music.play(-1)
                    mixer.music.set_volume(0.1)
                    creditos_janela()

        pygame.display.update()


menu()
