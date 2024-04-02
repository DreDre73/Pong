import random
import pygame

pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Remake")

# Basic Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# FPS
FPS = 60

# Player Dimensions
PLAYER_WIDTH = 20
PLAYER_HEIGHT = HEIGHT / 6

# Ball Dimensions
BALL_WIDTH = 15
BALL_HEIGHT = 15

# Border in middle of screen
BORDER = pygame.Rect(WIDTH // 2 + 4, 0, 1, HEIGHT)

# Player and Ball Velocity
PLAYER_VELOCITY = 6
BALL_X_VELOCITY = 2
BALL_Y_VELOCITY = 2

textX = 10
textY = 10

# Score Font
SCORE_FONT = pygame.font.SysFont('comicsans', 40)


def draw(player1, player2, ball, player1_score, player2_score):
    # Grey Background
    WIN.fill(BLACK)

    # Border
    pygame.draw.rect(WIN, WHITE, BORDER)
    # Left Character
    pygame.draw.rect(WIN, WHITE, player1)
    # Right Character
    pygame.draw.rect(WIN, WHITE, player2)
    # Ball
    pygame.draw.rect(WIN, RED, ball)
    # Score
    player1_score_text = SCORE_FONT.render("Score:" + str(player1_score), True, WHITE)
    player2_score_text = SCORE_FONT.render("Score:" + str(player2_score), True, WHITE)
    WIN.blit(player1_score_text, (WIDTH / 6, 10))
    WIN.blit(player2_score_text, (WIDTH - player2_score_text.get_width() - 120, 10))

    pygame.display.update()


def player1_movement(keys_pressed, player1):
    # Up and Down player movement
    if keys_pressed[pygame.K_w] and player1.y > 10:
        player1.y -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_s] and player1.y < HEIGHT - PLAYER_HEIGHT - 10:
        player1.y += PLAYER_VELOCITY


def player2_movement(keys_pressed, player2):
    # Up and Down player movement
    if keys_pressed[pygame.K_UP] and player2.y > 10:
        player2.y -= PLAYER_VELOCITY
    if keys_pressed[pygame.K_DOWN] and player2.y < HEIGHT - PLAYER_HEIGHT - 10:
        player2.y += PLAYER_VELOCITY


def ball_movement(ball):
    # Ball X and Y velocity/speed
    ball.x += BALL_X_VELOCITY
    ball.y += BALL_Y_VELOCITY


def ball_reset(ball):
    global BALL_X_VELOCITY, BALL_Y_VELOCITY
    # Reset Ball Position and Speed
    ball.x = WIDTH / 2
    ball.y = random.uniform(0, HEIGHT)
    BALL_X_VELOCITY = 2
    BALL_Y_VELOCITY = 2


def ball_collisions(ball, player1, player2):
    global BALL_X_VELOCITY, BALL_Y_VELOCITY

    # Collision with borders
    if ball.bottom >= HEIGHT or ball.top <= 0:
        BALL_Y_VELOCITY *= -1
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_reset(ball)

    # Collision with paddles
    if ball.colliderect(player1):
        BALL_X_VELOCITY *= -1.1
        BALL_Y_VELOCITY *= 1.1

    if ball.colliderect(player2):
        BALL_X_VELOCITY *= -1.1
        BALL_Y_VELOCITY *= 1.1


def main():
    clock = pygame.time.Clock()
    run = True

    # Create rectangle objects
    player1 = pygame.Rect(10, HEIGHT / 3, PLAYER_WIDTH, PLAYER_HEIGHT)
    player2 = pygame.Rect(WIDTH - 30, HEIGHT / 3, PLAYER_WIDTH, PLAYER_HEIGHT)
    ball = pygame.Rect(WIDTH / 2, HEIGHT / 2, BALL_WIDTH, BALL_HEIGHT)

    player1_score = 0
    player2_score = 0

    # Game Loop
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update Score
        if ball.left <= 0:
            player2_score += 1
        if ball.right >= WIDTH:
            player1_score += 1

        keys_pressed = pygame.key.get_pressed()
        WIN.fill(BLACK)
        draw(player1, player2, ball, player1_score, player2_score)
        ball_collisions(ball, player1, player2)
        ball_movement(ball)
        player1_movement(keys_pressed, player1)
        player2_movement(keys_pressed, player2)

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
