import pygame
import time

class Sign:
    def __init__(self, x, y):
        self.size = (300, 200)
        self.color = (235, 235, 0)
        self.x = x
        self.y = y
        self.glx = x
    def show(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size[0], self.size[1]))
        pygame.draw.rect(screen, (100, 100, 100), (self.x, self.y, self.size[0], self.size[1]), 16)
        pygame.draw.rect(screen, (100, 100, 100), (self.x - 7, self.y - 7, 8, 8))    
        pygame.draw.rect(screen, (100, 100, 100), (self.x + self.size[0], self.y - 7, 8, 8))
        pygame.draw.rect(screen, (100, 100, 100), (self.x - 7, self.y + self.size[1], 8, 8))
        pygame.draw.rect(screen, (100, 100, 100), (self.x + self.size[0], self.y + self.size[1], 8, 8))
                         
    def update(self, pos):
        x = pos[0]
        y = pos[1]
        if x >= self.x and x <= self.x + self.size[0] and y >= self.y and y <= self.y + self.size[1]:
            self.x = max(self.x - 2.5, self.glx - 25)
            self.y = max(self.y - 2.5, 235)
            height = self.size[0]
            width = self.size[1]
            height = min(350, height + 5)
            width = min(250, width + 5)
            self.size = (height, width)
            yel = (self.color[1] - 190) * 5
            yel = max(0, yel - 23.5)
            col = (235, 190 + (yel // 5), 235 - yel)
            self.color = col
        else:
            self.x = min(self.x + 2.5, self.glx)
            self.y = min(self.y + 2.5, 260)
            height = self.size[0]
            width = self.size[1]
            height = max(300, height - 5)
            width = max(200, width - 5)
            self.size = (height, width)
            yel = (self.color[1] - 190) * 5
            yel = min(235, yel + 23.5)
            col = (235, 190 + (yel // 5), 235 - yel)
            self.color = col

    def click(self, pos):
        x = pos[0]
        y = pos[1]
        if x >= self.x and x <= self.x + self.size[0] and y >= self.y and y <= self.y + self.size[1]:
            return 1
            
               

def menuShow(screen, bg):
    sg1 = Sign(290, 260)
    sg2 = Sign(690, 260)
    pos = (0, 0)
    tr = 1
    but1 = 0
    but2 = 0
    while tr:
        screen.blit(bg, (0, 0))
        sg1.show(screen)
        sg2.show(screen)
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("Step by step", True, (100, 100, 255))
        screen.blit(text, (290 + (300 - text.get_width()) // 2, 260 + (200 - text.get_height()) // 2))
        text = font.render("User case", True, (100, 100, 255))
        screen.blit(text, (690 + (300 - text.get_width()) // 2, 260 + (200 - text.get_height()) // 2))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                pos = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                if sg1.click(pos) or sg2.click(pos):
                    but1 = sg1.click(pos)
                    but2 = sg2.click(pos)
                    tr = 0
        sg1.update(pos)
        sg2.update(pos)
        pygame.display.update()
        #time.sleep(0.005)
    if but2:
        return inpt(screen, bg)
    elif but1:
        return (2, 2)

def inpt(screen, bg):
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render("Input n and m:", True, (255, 255, 255))
    tr = 1
    st = ""
    while tr:
        screen.blit(bg, (0, 0))
        screen.blit(text, ((1280 - text.get_width()) // 2, (720 - 2 * text.get_height()) // 2))
        text2 = font.render(st, True, (255, 255, 255))
        screen.blit(text2, ((1280 - text2.get_width()) // 2, (720 - 2 * text2.get_height()) // 2 + text2.get_height()))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                if key >= "0" and key <= "9":
                    st = st + key
                elif key == "return":
                    tr = 0
                    break
                elif key == "space":
                    st = st + " "
                elif key == "backspace":
                    st = st[:-1]
        pygame.display.update()
    n, m = [int(i) for i in st.split()]
    return n, m
    
                    
            








        
