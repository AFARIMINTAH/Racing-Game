import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Racing Game")

# Car settings
car_width = 50
car_height = 100
player_x = screen_width // 2
player_y = screen_height - 120
player_speed = 10

# Obstacle settings
obstacle_width = 50
obstacle_height = 100
obstacle_speed = 10
obstacle_x = random.randint(0, screen_width - obstacle_width)
obstacle_y = -100

# Clock to control the frame rate
clock = pygame.time.Clock()

def draw_player(x, y):
    pygame.draw.rect(screen, blue, (x, y, car_width, car_height))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, red, (x, y, obstacle_width, obstacle_height))

def is_collision(player_x, player_y, obstacle_x, obstacle_y):
    if (player_x < obstacle_x < player_x + car_width or player_x < obstacle_x + obstacle_width < player_x + car_width) and \
       (player_y < obstacle_y < player_y + car_height or player_y < obstacle_y + obstacle_height < player_y + car_height):
        return True
    return False

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Move the player car
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - car_width:
        player_x += player_speed

    # Move the obstacle
    obstacle_y += obstacle_speed

    # Check if obstacle is off the screen
    if obstacle_y > screen_height:
        obstacle_y = -obstacle_height
        obstacle_x = random.randint(0, screen_width - obstacle_width)

    # Check for collision
    if is_collision(player_x, player_y, obstacle_x, obstacle_y):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    # Fill the screen with white
    screen.fill(white)

    # Draw the player car
    draw_player(player_x, player_y)

    # Draw the obstacle
    draw_obstacle(obstacle_x, obstacle_y)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
