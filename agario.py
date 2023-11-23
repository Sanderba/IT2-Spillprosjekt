import pygame, random

class Matbit:
    def __init__(self):     
        self.bilde = pygame.image.load("bilder/Valg.png").convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde, (30, 30))
        self.ramme = self.bilde.get_rect()  
        self.ramme.centerx = random.randint(0,BREDDE)
        self.ramme.centery = random.randint(0, HOYDE)
    def tegn(self,vindu):
        vindu.blit(self.bilde, self.ramme)

class Celle:
    def __init__(self, navn: str, radius: int, bildesti: str, x:int,y:int):
        self.navn = navn
        self.radius = radius
        self.bilde = pygame.image.load(bildesti).convert_alpha()
        self.bilde = pygame.transform.scale(self.bilde, (self.radius * 2, self.radius * 2))
        self.ramme = self.bilde.get_rect()
        self.ramme.centerx = x
        self.ramme.centerx = y
    
    def beveg(self):
        pass
    
    def spis(self):
        pass

    def tegn(self, vindu):
        vindu.blit(self.bilde, self.ramme)

pygame.init()
BREDDE = 600
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()

demokrat = Celle("DEMO", 50, "bilder/joe_biden.png", 100, 200)
repub = Celle("REPU", 25, "bilder/trump.png", 500, 400)


matbit1 = Matbit()
matbit2 = Matbit()

while True:

    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    
    
    vindu.fill("white")
    demokrat.tegn(vindu)
    matbit1.tegn(vindu)
    repub.tegn(vindu)

        
    pygame.display.flip()
    klokke.tick(FPS)