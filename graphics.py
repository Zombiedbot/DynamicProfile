import pygame
import time


st = (900, 25)
stp = (650, 25)
stg = (650, 350)
sta = (60, 25)
rb = 300
rp = 300
ra = 480
rt = 350
time_const = 0.2
board = 3
num = 1

def setup():
    global st
    global stp
    global stg
    global sta
    global rb
    global rp
    global ra
    global rt
    global time_const
    global board
    global num
    st = (900, 25)
    stp = (650, 25)
    stg = (650, 350)
    sta = (60, 25)
    rb = 300
    rp = 300
    ra = 480
    rt = 350
    time_const = 0.2
    board = 3
    num = 1
    
def wait():
    tj = 1
    while tj:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                tj = 0
                break

def signes(screen):
    font = pygame.font.SysFont("comicsansms", 32)
    text = font.render("Stage 1", True, (255, 255, 255))
    screen.blit(text, (520, 30))
    text1 = font.render("Stage 2", True, (255, 255, 255))
    screen.blit(text1, (450, 450))
    pygame.draw.rect(screen, (48, 213, 200), (440, 450, 150, 50), 5)
    font = pygame.font.SysFont("comicsansms", 64)
    text2 = font.render("Answer:", True, (255, 255, 255))
    screen.blit(text2, (50, 600))


def illustrate(x, y, t, screen):
    st_x = st[0]
    st_y = st[1]
    if t:
        pygame.draw.rect(screen, (0, 200, 0), (st_x + rb * x, st_y + rb * y, rb, rb))
    else:
        pygame.draw.rect(screen, (200, 0, 0), (st_x + rb * x, st_y + rb * y, rb, rb))
    pygame.draw.rect(screen, (128, 128, 128), (st_x + rb * x, st_y + rb * y, rb, rb), board)
    time.sleep(time_const)

def twoProfiles(a, b, screen, pos = -1):
    st_x = stp[0]
    st_y = stp[1]
    y = 0
    for i in range(num):
        bit1 = a % 2
        bit2 = b % 2
        col1 = (0, 0, 0) if bit1 else (255, 255, 255)
        col2 = (0, 0, 0) if bit2 else (255, 255, 255)
        pygame.draw.rect(screen, col1, (st_x, st_y + rp * y, rp, rp))
        pygame.draw.rect(screen, (128, 128, 128), (st_x, st_y + rp * y, rp, rp), board)
        pygame.draw.rect(screen, col2, (st_x + rp, st_y + rp * y, rp, rp))
        pygame.draw.rect(screen, (128, 128, 128), (st_x + rp, st_y + rp * y, rp, rp), board)
        a //= 2
        b //= 2
        y += 1
    if pos >= 0:
        pygame.draw.rect(screen, (253, 241, 0), (st_x, st_y + rp * pos, 2 * rp, 2 * rp), board)

def grid(n, m, screen):
    global rb
    rb /= (1 << n)
    global time_const
    time_const = min(time_const, 4 / (1 << (2*n)))
    global board
    board -= n // 2
    global num
    num = n
    global rp
    rp = min(rp / n, 100)
    global ra
    ra /= (1 << n)
    global rt
    rt /= m
    st_x = st[0]
    st_y = st[1]
    for i in range(1 << n):
        for j in range(1 << n):
            pygame.draw.rect(screen, (128, 128, 128), (st_x + rb * i, st_y + rb * j, rb, rb), board)
    st_x = stg[0]
    st_y = stg[1]
    for i in range(n):
        for j in range(m):
            pygame.draw.rect(screen, (128, 128, 128), (st_x + rp * j, st_y + rp * i, rp, rp), board)
    st_x = sta[0]
    st_y = sta[1]
    for i in range(1 << n):
        for j in range(m):
            pygame.draw.rect(screen, (128, 128, 128), (st_x + rt * j, st_y + ra * i, rt, ra), board)
    pygame.draw.rect(screen, (48, 213, 200), (500, 0, 10, 450))
    pygame.draw.rect(screen, (48, 213, 200), (500, 500, 10, 220))
    pygame.draw.rect(screen, (48, 213, 200), (0, 560, 500, 5))
    pygame.draw.rect(screen, (48, 213, 200), (500, 335, 780, 5))


def drawInGrid(col, i, j, screen, n, m):
    st_x = stg[0]
    st_y = stg[1]
    y = 0
    ii = i
    jj = j
    col -= 1
    for hhhh in range(num):
        bit1 = i % 2
        bit2 = j % 2
        col1 = (0, 0, 0) if bit1 else (255, 255, 255)
        col2 = (0, 0, 0) if bit2 else (255, 255, 255)
        pygame.draw.rect(screen, col1, (st_x + col * rp, st_y + rp * y, rp, rp))
        pygame.draw.rect(screen, (128, 128, 128), (st_x  + col * rp, st_y + rp * y, rp, rp), board)
        pygame.draw.rect(screen, col2, (st_x + (col + 1) * rp, st_y + rp * y, rp, rp))
        pygame.draw.rect(screen, (128, 128, 128), (st_x + (col + 1) * rp, st_y + rp * y, rp, rp), board)
        i //= 2
        j //= 2
        y += 1
    st_x = sta[0]
    st_y = sta[1]
    if n == m == 2:
        for ig in range(128):
            pygame.draw.rect(screen, (128 - ig, 128 - ig, 128), (st[0] + rb * ii, st[1] + rb * jj, rb, rb), board)
            pygame.draw.rect(screen, (128 + ig, 128 + ig // 4, 128 - ig), (st_x + col * rt, st_y + ra * jj, rt, ra), board)
            pygame.display.update()
    pygame.draw.rect(screen, (0, 0, 128), (st[0] + rb * ii, st[1] + rb * jj, rb, rb), board)
    pygame.draw.rect(screen, (255, 156, 0), (st_x + col * rt, st_y + ra * jj, rt, ra), board)
    pygame.display.update()
    if n == m == 2:
        wait()
        for ig in range(128):
            pygame.draw.rect(screen, (ig, ig, 128), (st[0] + rb * ii, st[1] + rb * jj, rb, rb), board)
            pygame.draw.rect(screen, (255 - ig, 156 - ig // 4, ig), (st_x + col * rt, st_y + ra * jj, rt, ra), board)
            pygame.display.update()
    time.sleep(time_const)
    pygame.draw.rect(screen, (128, 128, 128), (st_x + col * rt, st_y + ra * jj, rt, ra), board)
    pygame.draw.rect(screen, (128, 128, 128), (st[0] + rb * ii, st[1] + rb * jj, rb, rb), board)
    

def writeNum(col, nnum, screen, image):
    figures = 0
    n1 = nnum
    st_x = stg[0]
    st_y = stg[1]
    screen.blit(image, (st_x + rp * col, st_y + rp * num),
                (st_x + rp * col, st_y + rp * num, rp, 2 * rp))
    while n1:
        figures += 1
        n1 //= 10
    figures = max(1, figures)
    size = rp / figures
    size = min(size, 50)
    font = pygame.font.SysFont("comicsansms", int(size * 1.25))
    text = font.render(str(nnum), True, (255, 255, 255))
    screen.blit(text, (st_x + rp * col, st_y + rp * num))

def writeNumTwo(col, j, nnum, screen, image):
    figures = 0
    st_x = sta[0]
    st_y = sta[1]
    n1 = nnum
    while n1:
        figures += 1
        n1 //= 10
    figures = max(1, figures)
    screen.blit(image, (st_x + rt * col, st_y + ra * j),
                (st_x + rt * col, st_y + ra * j, rt, ra))
    pygame.draw.rect(screen, (128, 128, 128), (st_x + rt * col, st_y + ra * j, rt, ra), board)
    size = min(ra - 2 * board, 1.25 * rt / figures)
    font = pygame.font.SysFont("comicsansms", int(size))
    text = font.render(str(nnum), True, (255, 255, 255))
    screen.blit(text, (st_x + rt * col + board, st_y + ra * j - size / 4 + board))

def printAns(screen, ans):
    a = ans
    figures = 0
    while a:
        figures += 1
        a //= 10
    size = int(250 / figures)
    font = pygame.font.SysFont("comicsansms", min(64, size))
    text2 = font.render(str(ans), True, (255, 255, 255))
    screen.blit(text2, (300, 600 + 64 - min(64, size)))
