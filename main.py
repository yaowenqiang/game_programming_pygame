import pygame

pygame.init()

window_size = (800, 600)
clock = pygame.time.Clock()
screen = pygame.display.set_mode(window_size)

font = pygame.font.SysFont('Arial', 48)

hello_world = font.render("Hello world!", 1, (255, 0, 255), (255, 255, 255))
hello_world_size = hello_world.get_size()
direction_x = 1
direction_y = 1

x, y = (0, 0)
game_running = True
while game_running:
    clock.tick(40)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
    screen.fill((0, 0, 0))

    mouse_position = pygame.mouse.get_pos()
    x, y = mouse_position
    if x + hello_world_size[0] > 800:
        x = 800 - hello_world_size[0]
    if y + hello_world_size[1] > 600:
        y = 600 - hello_world_size[1]




    # x += 5 * direction_x
    # y += 5 * direction_x
    # if x + hello_world_size[0] > 800 or x < 0:
    #     direction_x *= -1
    # if y + hello_world_size[1] > 600 or y < 0:
    #     direction_y *= -1
    screen.blit(hello_world, (x, y))
    pygame.display.update()
pygame.quit()
