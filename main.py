import pygame

pygame.init()

window_size = (800, 600)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(window_size)

font = pygame.font.SysFont('Arial', 48)

hello_world = font.render("Hello world!", 1, (255, 0, 255), (255, 255, 255))

x, y = (0, 0)
game_running = True
while game_running:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    screen.fill((0, 0, 0))
    screen.blit(hello_world, (x, y))
    x += 5
    pygame.display.update()
pygame.quit()