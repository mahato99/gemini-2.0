import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20
SNAKE_COLOR = (0, 255, 0)  # Green
FOOD_COLOR = (255, 0, 0)  # Red
BACKGROUND_COLOR = (0, 0, 0)  # Black
TEXT_COLOR = (255, 255, 255) # White
FPS = 10

# --- Directions ---
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# --- Functions ---

def draw_block(surface, color, position):
    """Draws a single block on the screen."""
    block = pygame.Rect((position[0] * BLOCK_SIZE, position[1] * BLOCK_SIZE), (BLOCK_SIZE, BLOCK_SIZE))
    pygame.draw.rect(surface, color, block)

def display_score(surface, score):
    """Displays the current score on the screen."""
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, TEXT_COLOR)
    surface.blit(score_text, (10, 10))

def game_over_screen(surface, score):
    """Displays the game over screen."""
    font = pygame.font.Font(None, 48)
    game_over_text = font.render("Game Over", True, TEXT_COLOR)
    score_text = font.render(f"Final Score: {score}", True, TEXT_COLOR)
    
    text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

    surface.blit(game_over_text, text_rect)
    surface.blit(score_text, score_rect)
    pygame.display.flip()
    pygame.time.delay(3000) # pause for 3 seconds before quitting

def main():
    """Main game loop."""
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()

    # Initial Snake
    snake = [(SCREEN_WIDTH // (2*BLOCK_SIZE), SCREEN_HEIGHT // (2*BLOCK_SIZE))]
    snake_direction = RIGHT

    # Food
    food = (random.randrange(0, SCREEN_WIDTH // BLOCK_SIZE), random.randrange(0, SCREEN_HEIGHT // BLOCK_SIZE))

    score = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and snake_direction != DOWN:
                    snake_direction = UP
                elif event.key == pygame.K_DOWN and snake_direction != UP:
                    snake_direction = DOWN
                elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                    snake_direction = LEFT
                elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                    snake_direction = RIGHT

        # Move the snake
        head_x, head_y = snake[0]
        new_head = (head_x + snake_direction[0], head_y + snake_direction[1])
        snake.insert(0, new_head)

        # Check for food
        if snake[0] == food:
            score += 1
            food = (random.randrange(0, SCREEN_WIDTH // BLOCK_SIZE), random.randrange(0, SCREEN_HEIGHT // BLOCK_SIZE))
        else:
            snake.pop()  # Remove tail if no food eaten

        # Check for collisions (walls or self)
        if (
            snake[0][0] < 0
            or snake[0][0] >= SCREEN_WIDTH // BLOCK_SIZE
            or snake[0][1] < 0
            or snake[0][1] >= SCREEN_HEIGHT // BLOCK_SIZE
            or snake[0] in snake[1:]
        ):
            game_over = True

        # Draw everything
        screen.fill(BACKGROUND_COLOR)
        for segment in snake:
            draw_block(screen, SNAKE_COLOR, segment)
        draw_block(screen, FOOD_COLOR, food)
        display_score(screen, score)
        pygame.display.flip()

        clock.tick(FPS)
    
    game_over_screen(screen,score)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
