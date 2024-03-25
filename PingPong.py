import pygame
import random

pygame.init()
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 9
PADDLE_SPEED = 7

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")


TABLE_GREEN: (0, 102, 0)
BALL_ORANGE: (255, 140, 0)
PADDLE_BLUE: (0, 0, 255)
BACKGROUND_GRAY: (192, 192, 192)
SCOREBOARD_YELLOW: (255, 255, 0)
NET_WHITE: (255, 255, 255)
SCORE_GOLD: (255, 215, 0)

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


