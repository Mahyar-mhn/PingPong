import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 9
PADDLE_SPEED = 7

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

BALL_ORANGE = (255, 140, 0)
PADDLE_BLUE = (0, 0, 255)
BACKGROUND_GRAY = (192, 192, 192)
SCOREBOARD_YELLOW = (255, 255, 0)
SCORE_GOLD = (255, 215, 0)

score1 = 0
score2 = 0

PLAYER1_NAME = 'A'
PLAYER2_NAME = 'B'

# make the ball to be the center of the screen for start
BALL = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
PADDLE1 = pygame.Rect(50, HEIGHT // 2 - 60, 10, 120)
PADDLE2 = pygame.Rect(WIDTH - 60, HEIGHT // 2 - 60, 10, 120)

ball_dx = BALL_SPEED * random.choice((1, -1))
ball_dy = BALL_SPEED * random.choice((1, -1))

paddle1_dy = 0
paddle2_dy = 0

ball_in_motion = True


def draw_scores():
    font = pygame.font.Font(None, 36)
    score1_text = font.render(f"{PLAYER1_NAME} : {score1}", True, SCORE_GOLD)
    score2_text = font.render(f"{PLAYER2_NAME} : {score2}", True, SCORE_GOLD)

    screen.blit(score1_text, (10, 10))
    screen.blit(score2_text, (WIDTH - score2_text.get_width() - 10, 10))


def check_collision(ball, paddle):
    if ball.colliderect(paddle):
        return True
    return False


def reset_all_positions():
    side = random.choice(("left", "right"))
    if side == "left":
        BALL.x = 70
        ball_dx = BALL_SPEED
    else:
        BALL.x = WIDTH - 100
        ball_dx = -BALL_SPEED

    ball_dy = HEIGHT // 2 - 15
    return ball_dx


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                paddle2_dy = -PADDLE_SPEED

            elif event.key == pygame.K_DOWN:
                paddle2_dy = PADDLE_SPEED

            elif event.key == pygame.K_SPACE:
                ball_in_motion = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.KEYDOWN:
                paddle2_dy = 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1_dy = -PADDLE_SPEED
    elif keys[pygame.K_s]:
        paddle1_dy = PADDLE_SPEED
    else:
        paddle1_dy = 0

    if ball_in_motion:
        BALL.x += ball_dx
        BALL.y += ball_dy

    if BALL.top <= 0 or BALL.bottom >= HEIGHT:
        ball_dy *= -1

    if check_collision(BALL, PADDLE1) or check_collision(BALL, PADDLE2):
        ball_dx *= -1

    if BALL.left <= 0:
        score2 += 1
        if score2 == 5:
            running = False
        else:
            ball_dx = reset_all_positions()
            ball_in_motion = False
    elif BALL.right >= WIDTH:
        score1 += 1
        if score1 == 5:
            running = False
        else:
            ball_dx = reset_all_positions()
            ball_in_motion = False

    PADDLE1.y += paddle1_dy
    PADDLE2.y += paddle2_dy

    if PADDLE1.top <= 0:
        PADDLE1.top = 0
    if PADDLE1.bottom >= HEIGHT:
        PADDLE1.bottom = HEIGHT

    if PADDLE2.top <= 0:
        PADDLE2.top = 0
    if PADDLE2.bottom >= HEIGHT:
        PADDLE2.bottom = HEIGHT

    screen.fill(BACKGROUND_GRAY)

    pygame.draw.rect(screen, PADDLE_BLUE, PADDLE1)
    pygame.draw.rect(screen, PADDLE_BLUE, PADDLE2)
    pygame.draw.ellipse(screen, BALL_ORANGE, BALL)

    draw_scores()
    pygame.display.flip()

    pygame.time.delay(30)

pygame.quit()
