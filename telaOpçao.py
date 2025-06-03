import pygame
from pygame.locals import*
from sys import exit 

pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Menu Interativo")

preto =(0, 0, 0)
azul = (0, 0, 255)

fontePadrao = pygame.font.Font(None, 74)
estado = "menu"


def drawMenu():
    tela.fill(preto)
    font = fontePadrao
    texto = font.render("Menu", True, azul)
    tela.blit(texto,(350, 50))

    botaoStart = pygame.Rect(300,200,200,50)
    pygame.draw.rect(tela, azul, botaoStart)
    texto = fontePadrao.render("Iniciar jogo", True, preto)
    tela.blit(texto, (botaoStart.x + 20, botaoStart.y + 10))

    botaoSair = pygame.Rect(300,300,200,50)
    pygame.draw.rect(tela, azul, botaoSair)
    texto = fontePadrao.render("Sair", True, preto)
    tela.blit(texto,(botaoSair.x + 80, botaoSair.y + 10))

    return botaoStart, botaoSair

def selecaoDeClasse():
    tela.fill(preto)
    texto = fontePadrao.render("Esolha sua classe", True, azul)
    tela.blit(texto,(200,50))


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame,quit()
            exit()


    if estado == "menu":
        botaoStart, botaoSair = drawMenu()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if botaoStart.collidepoint(event.pos): 
            estado = "selecaoDeClasse"
        elif botaoSair.collidepoint(event.pos):
            pygame.quit()
            exit()    

    elif estado == "selecaoDeClasse":
        selecaoDeClasse()

    pygame.display.update()