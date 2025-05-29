import pygame
from pygame.locals import*
from sys import exit 

pygame.init()

largura = 800
altura = 600

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Menu Interativo")

preto =(0, 0, 0)
blue = (0, 0, 255)

def drawMenu():
    tela.fill(preto)
    font = pygame.font.Font(None,74)
    text = font.render("Menu", True, blue)
    tela.blit(text,(350, 50))

    botaoStart = pygame.Rect(300,200,200,50)
    pygame.draw.rect(tela, blue, botaoStart)
    text = font.render("Iniciar jogo", True, preto)
    tela.blit(text, (botaoStart.x + 20, botaoStart.y + 10))

    botaoSair = pygame.Rect(300,300,200,50)
    pygame.draw.rect(tela, blue, botaoSair)
    text = font.render("Sair", True, preto)
    tela.blit(text,(botaoSair.x + 80, botaoSair.y + 10))

    return botaoStart, botaoSair


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame,quit()
            exit()

    botaoStart, botaoSair = drawMenu()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if botaoStart.collidepoint(event.pos):
            print("Iniciar Jogo")
        elif botaoSair.collidepoint(event.pos):
            pygame.quit()
            exit()    

    


    pygame.display.update()