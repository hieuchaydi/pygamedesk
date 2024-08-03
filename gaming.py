import time
import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
yellow = (255, 255, 0)
red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
gray = (169, 169, 169)
flash_colors = [red, white]

# Display dimensions
dis_width = 800
dis_height = 600

# Create display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Set clock and game parameters
clock = pygame.time.Clock()
snake_block = 10
snake_speed = 15

# Define fonts
font_style = pygame.font.SysFont('arial', 50)
score_font = pygame.font.SysFont('arial', 35)

# Load background image
image_path = 'C:/Users/FPT/OneDrive/Desktop/pygame/media/tree.png'
try:
    background_image = pygame.image.load(image_path)
    background_image = pygame.transform.scale(background_image, (dis_width, dis_height))
except FileNotFoundError:
    print(f"Error: The image file at {image_path} does not exist.")
    pygame.quit()
    quit()

# Function to draw the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, yellow, [x[0], x[1], snake_block, snake_block])

# Function to display a message on the screen
def message(msg, color, pos):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, pos)

# Function to show the score
def show_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [0, 0])

# Function to draw a button
def draw_button(text, color, rect):
    pygame.draw.rect(dis, color, rect)
    text_surf = font_style.render(text, True, black)
    text_rect = text_surf.get_rect(center=(rect[0] + rect[2] / 2, rect[1] + rect[3] / 2))
    dis.blit(text_surf, text_rect)

# Function to check if a button is clicked
def is_button_clicked(rect, pos):
    return pygame.Rect(rect).collidepoint(pos)

# Main game loop
def gameLoop():
    game_over = False
    game_close = False
    pause = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    while not game_over:
        while game_close:
            dis.blit(background_image, (0, 0))
            draw_button("Restart", white, [dis_width / 2 - 100, dis_height / 2 - 50, 200, 50])
            draw_button("Quit", white, [dis_width / 2 - 100, dis_height / 2 + 20, 200, 50])
            message("Game Over!", red, [dis_width / 3, dis_height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if is_button_clicked([dis_width / 2 - 100, dis_height / 2 - 50, 200, 50], pos):
                        gameLoop()  # Restart the game
                    elif is_button_clicked([dis_width / 2 - 100, dis_height / 2 + 20, 200, 50], pos):
                        pygame.quit()
                        quit()

        while pause:
            dis.blit(background_image, (0, 0))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        pause = False
                    elif event.key == pygame.K_q:
                        game_over = True
                        pause = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:
                    pause = True

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change

        dis.blit(background_image, (0, 0))

        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        if snake_Head in snake_List[:-1]:
            game_close = True

        our_snake(snake_block, snake_List)
        show_score(Length_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            for color in flash_colors:
                pygame.draw.rect(dis, color, [foodx, foody, snake_block, snake_block])
                pygame.display.update()
                pygame.time.delay(50)
            foodx = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            foody = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Main menu loop
def main_menu():
    menu = True
    while menu:
        dis.blit(background_image, (0, 0))
        draw_button("Start Game", white, [dis_width / 2 - 100, dis_height / 2 - 100, 200, 50])
        draw_button("View Score", white, [dis_width / 2 - 100, dis_height / 2 - 30, 200, 50])
        draw_button("Quit", white, [dis_width / 2 - 100, dis_height / 2 + 40, 200, 50])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if is_button_clicked([dis_width / 2 - 100, dis_height / 2 - 100, 200, 50], pos):
                    gameLoop()
                elif is_button_clicked([dis_width / 2 - 100, dis_height / 2 - 30, 200, 50], pos):
                    dis.blit(background_image, (0, 0))
                    message("Score: Not Implemented", white, [dis_width / 3, dis_height / 2])
                    pygame.display.update()
                    time.sleep(2)
                elif is_button_clicked([dis_width / 2 - 100, dis_height / 2 + 40, 200, 50], pos):
                    pygame.quit()
                    quit()

main_menu()
