import pygame
pygame.init()

# Screen definition
screen_size = screen_width, screen_height = 1920, 1080
screen = pygame.display.set_mode(screen_size)

# Initial position of the player
player_width, player_height = 100, 25
player_x, player_y = screen_width / 2 - 50, screen_height * 2 / 3
player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
player_speed = 5

# Initial position of the ball
ball_radius = 8
ball_x, ball_y = player_x + player_width / 2 - ball_radius, player_y - ball_radius * 2
ball_rect = pygame.Rect(ball_x, ball_y, ball_radius * 2, ball_radius * 2)
ball_speed = [2, 2]

running = True
game_started = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        if player_rect.left <= 0:
            pass
        else:
            if game_started:
                player_rect.move_ip(player_speed * -1, 0)
            else:
                player_rect.move_ip(player_speed * -1, 0)
                ball_rect.move_ip(player_speed * -1, 0)
    if keys[pygame.K_RIGHT]:
        if player_rect.right >= screen_width:
            pass
        else:
            if game_started:
                player_rect.move_ip(player_speed * 1, 0)
            else:
                player_rect.move_ip(player_speed * 1, 0)
                ball_rect.move_ip(player_speed * 1, 0)

    if keys[pygame.K_SPACE] and not game_started:
        game_started = True

    if game_started:
        if ball_rect.left <= 0 or ball_rect.right >= screen_width:
            ball_speed[0] = -ball_speed[0]
        if ball_rect.top <= 0:
            ball_speed[1] = -ball_speed[1]
        if ball_rect.bottom == player_rect.top and ball_rect.centerx >= player_rect.left and ball_rect.centerx <= player_rect.right:
            ball_speed[1] = -ball_speed[1]
        ball_rect.move_ip(ball_speed)

    screen.fill(color="black")
    pygame.draw.rect(screen, color="green", rect=player_rect)
    pygame.draw.circle(screen, color="red", center=ball_rect.center, radius=ball_radius)
    pygame.time.delay(10)
    pygame.display.update()

pygame.quit()
