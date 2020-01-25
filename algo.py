import pygame
import graphics
import menu

def main(n, m, screen):
    background_image = pygame.image.load('images/background.jpg')
    screen.blit(background_image, (0, 0))
    (n, m) = (m, n) if n > m else (n, m)
    dp = [[0] * (1 << n) for i in range(1 << n)]
    answers = [[0] * (1 << n) for i in range(m)]
    graphics.setup()
    graphics.grid(n, m, screen)
    graphics.signes(screen)

    def wait():
        tj = 1
        while tj:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    tj = 0
                    break

    pygame.display.update()
    def fillTable(n: int):
        if n == m == 2:
            wait()
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
                if t: graphics.twoProfiles(i, j, screen)
                pygame.display.update()
                if n == m == 2:
                    wait()
                dp[i][j] = 1 if t else 0


    fillTable(n)
    num = 0
    for i in range(1 << n):
        answers[0][i] = 1
        num += 1
        graphics.writeNumTwo(0, i, answers[0][i], screen, background_image)
        graphics.writeNum(0, num, screen, background_image)
        pygame.display.update()
        if n == m == 2:
            wait()

    for k in range(1, m):
        num = 0
        for i in range(1 << n):
            for j in range(1 << n):
                graphics.drawInGrid(k, i, j, screen, n, m)
                answers[k][i] += dp[i][j] * answers[k - 1][j]
                num += dp[i][j] * answers[k - 1][j]
                graphics.writeNum(k, num, screen, background_image)
                graphics.writeNumTwo(k, i, answers[k][i], screen, background_image)
                pygame.display.update()
                

    ans = 0
    for i in range(1 << n):
        ans += answers[m - 1][i]
    print(ans)

    graphics.printAns(screen, ans)
    pygame.display.update()
    if n == m == 2:
        wait()
