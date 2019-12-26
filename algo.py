import pygame
import graphics
import menu

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Dynamic profile")

#n, m = [int(i) for i in input().split()]

background_image = pygame.image.load('images/background.jpg')
screen.blit(background_image, (0, 0))
pygame.display.update()

n, m = menu.menuShow(screen, background_image)

screen.blit(background_image, (0, 0))

dp = [[0] * (1 << n) for i in range(1 << n)]
answers = [[0] * (1 << n) for i in range(m)]
graphics.grid(n, m, screen)


(n, m) = (m, n) if n > m else (n, m)
def fillTable(n: int):
    for i in range(1 << n):
        for j in range(1 << n):
            t = True
            for k in range(n - 1):
                bit1 = i & (1 << k)
                bit2 = i & (1 << (k + 1))
                bit3 = j & (1 << k)
                bit4 = j & (1 << (k + 1))
                if bit1 and bit2 and bit3 and bit4:
                    t = False
                    graphics.twoProfiles(i, j, screen, k)
                    break
                if not bit1 and not bit2 and not bit3 and not bit4:
                    t = False
                    graphics.twoProfiles(i, j, screen, k)
                    break
            graphics.illustrate(j, i, t, screen)
            pygame.display.update()
            dp[i][j] = 1 if t else 0
            if t: graphics.twoProfiles(i, j, screen)


fillTable(n)
num = 0
for i in range(1 << n):
    answers[0][i] = 1
    num += 1
    graphics.writeNumTwo(0, i, answers[0][i], screen, background_image)
    graphics.writeNum(0, num, screen, background_image)
    pygame.display.update()

for k in range(1, m):
    num = 0
    for i in range(1 << n):
        for j in range(1 << n):
            graphics.drawInGrid(k, i, j, screen)
            answers[k][i] += dp[i][j] * answers[k - 1][j]
            num += dp[i][j] * answers[k - 1][j]
            graphics.writeNum(k, num, screen, background_image)
            graphics.writeNumTwo(k, i, answers[k][i], screen, background_image)
            pygame.display.update()

ans = 0
for i in range(1 << n):
    ans += answers[m - 1][i]
print(ans)

tr = 1
while tr:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tr = 0
pygame.quit()
