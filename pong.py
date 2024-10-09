import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Simple Pong Game')

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up paddle and ball parameters
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
BALL_SIZE = 15

# Paddle positions
left_paddle = pygame.Rect(30, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
right_paddle = pygame.Rect(WIDTH - 40, (HEIGHT - PADDLE_HEIGHT) // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball position and velocity
ball = pygame.Rect(WIDTH // 2, HEIGHT // 2, BALL_SIZE, BALL_SIZE)
ball_velocity = [5, 5]

# Game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle.top > 0:
        left_paddle.y -= 5
    if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += 5
    if keys[pygame.K_UP] and right_paddle.top > 0:
        right_paddle.y -= 5
    if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += 5

    # Move the ball
    ball.x += ball_velocity[0]
    ball.y += ball_velocity[1]

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_velocity[1] = -ball_velocity[1]

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_velocity[0] = -ball_velocity[0]

    # Ball reset if it goes out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.x = WIDTH // 2
        ball.y = HEIGHT // 2
        ball_velocity = [5, 5]  # Reset ball speed

    # Fill the screen with black
    screen.fill(BLACK)

    # Draw paddles and ball
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
