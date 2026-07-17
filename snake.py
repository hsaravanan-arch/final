#THE MAIN
#python3 snake_game.py

#imports pygame
import pygame

#imports random
import random

#starts pygame
pygame.init()

#creates the screen
screen = pygame.display.set_mode((800, 600))

#creates the title for the window
pygame.display.set_caption("Colorful Snake Game")

#creates the text fonts
text_font = pygame.font.SysFont("Arial", 20)
large_font = pygame.font.SysFont("Arial", 45)

#this function displays text on the screen
def draw_text(text, font, color, x, y):

    #creates the text image
    img = font.render(text, True, color)

    #places the text on the screen
    screen.blit(img, (x, y))

#creates the pink and purple background color
color = (220, 180, 230)

#creates basic colors
black = (0, 0, 0)
white = (255, 255, 255)
dark_purple = (60, 30, 70)

#creates a list of snake, food, and obstacle colors
game_colors = [
    (0, 0, 225),
    (255, 0, 0),
    (0, 200, 0),
    (255, 255, 0),
    (128, 0, 128),
    (255, 165, 0),
    (255, 105, 180)
]

#creates the size of each snake block
block_size = 20

#controls the snake speed
game_speed = 8

#creates the obstacle positions
#each obstacle has x, y, width, and height
obstacles = [
    pygame.Rect(100, 180, 180, 20),
    pygame.Rect(520, 140, 20, 160),
    pygame.Rect(180, 460, 200, 20),
    pygame.Rect(580, 380, 140, 20)
]

#creates a color for each obstacle
obstacle_colors = [
    random.choice(game_colors),
    random.choice(game_colors),
    random.choice(game_colors),
    random.choice(game_colors)
]

#this function creates a random food location
def create_food():

    #keeps looking for a safe food position
    looking_for_food = True

    while looking_for_food == True:

        #creates the food x position
        new_food_x = random.randrange(20, 780, 20)

        #creates the food y position
        new_food_y = random.randrange(100, 580, 20)

        #creates a rectangle around the food
        new_food_rect = pygame.Rect(
            new_food_x - 15,
            new_food_y - 15,
            30,
            30
        )

        #starts by saying the food is safe
        food_is_safe = True

        #checks every obstacle
        for obstacle in obstacles:

            #checks if the food is touching an obstacle
            if new_food_rect.colliderect(obstacle):
                food_is_safe = False

        #stops looking when the position is safe
        if food_is_safe == True:
            looking_for_food = False

    #returns the food position
    return [new_food_x, new_food_y]

#this function resets the game
def reset_game():

    #creates the snake body
    snake_body = [
        [400, 300],
        [380, 300],
        [360, 300]
    ]

    #creates a list for the snake colors
    snake_colors = []

    #adds a random color for each snake block
    for block in snake_body:
        snake_colors.append(random.choice(game_colors))

    #creates the snake direction
    snake_direction = [block_size, 0]

    #creates the food
    food_position = create_food()

    #chooses a random food color
    food_color = random.choice(game_colors)

    #creates the food directions
    food_x_direction = random.choice([-3, 3])
    food_y_direction = random.choice([-3, 3])

    #creates the score
    score = 0

    #starts the game
    game_over = False

    #keeps track of obstacle collision
    hit_obstacle = False

    return snake_body, snake_colors, snake_direction, food_position, food_color, food_x_direction, food_y_direction, score, game_over, hit_obstacle

#gets all the beginning game information
snake_body, snake_colors, snake_direction, food_position, food_color, food_x_direction, food_y_direction, score, game_over, hit_obstacle = reset_game()

#keeps the screen open
running = True

#controls how fast the game runs
clock = pygame.time.Clock()

#keeps the game running
while running:

    #checks what the user does
    for event in pygame.event.get():

        #checks if the user closes the screen
        if event.type == pygame.QUIT:
            running = False

        #checks if the user presses a key
        if event.type == pygame.KEYDOWN:

            #checks the keys while the game is running
            if game_over == False:

                #moves the snake left
                if event.key == pygame.K_LEFT:
                    if snake_direction[0] != block_size:
                        snake_direction = [-block_size, 0]

                #moves the snake right
                elif event.key == pygame.K_RIGHT:
                    if snake_direction[0] != -block_size:
                        snake_direction = [block_size, 0]

                #moves the snake up
                elif event.key == pygame.K_UP:
                    if snake_direction[1] != block_size:
                        snake_direction = [0, -block_size]

                #moves the snake down
                elif event.key == pygame.K_DOWN:
                    if snake_direction[1] != -block_size:
                        snake_direction = [0, block_size]

            #checks the keys after game over
            else:

                #restarts the game
                if event.key == pygame.K_r:
                    snake_body, snake_colors, snake_direction, food_position, food_color, food_x_direction, food_y_direction, score, game_over, hit_obstacle = reset_game()

                    #gives the obstacles new colors
                    for number in range(len(obstacle_colors)):
                        obstacle_colors[number] = random.choice(game_colors)

                #quits the game
                elif event.key == pygame.K_q:
                    running = False

    #runs the movement when the game is not over
    if game_over == False:

        #moves the food horizontally
        food_position[0] = food_position[0] + food_x_direction

        #moves the food vertically
        food_position[1] = food_position[1] + food_y_direction

        #changes the food direction at the left or right wall
        if food_position[0] <= 15 or food_position[0] >= 785:
            food_x_direction = food_x_direction * -1
            food_color = random.choice(game_colors)

        #changes the food direction at the top or bottom wall
        if food_position[1] <= 95 or food_position[1] >= 585:
            food_y_direction = food_y_direction * -1
            food_color = random.choice(game_colors)

        #gets the snake head
        snake_head = snake_body[0]

        #creates the new snake head position
        new_head = [
            snake_head[0] + snake_direction[0],
            snake_head[1] + snake_direction[1]
        ]

        #creates a rectangle around the new snake head
        new_head_rect = pygame.Rect(
            new_head[0],
            new_head[1],
            block_size,
            block_size
        )

        #keeps track of which obstacle was touched
        obstacle_number_touched = -1

        #checks every obstacle
        for obstacle_number in range(len(obstacles)):

            #checks if the snake touches the obstacle
            if new_head_rect.colliderect(obstacles[obstacle_number]):
                obstacle_number_touched = obstacle_number

        #checks if the snake hits the outside wall
        if new_head[0] < 0:
            game_over = True

        elif new_head[0] >= 800:
            game_over = True

        elif new_head[1] < 80:
            game_over = True

        elif new_head[1] >= 600:
            game_over = True

        #checks if the snake hits an obstacle
        elif obstacle_number_touched != -1:

            #changes the touched obstacle color
            obstacle_colors[obstacle_number_touched] = random.choice(
                game_colors
            )

            #remembers that an obstacle was touched
            hit_obstacle = True

            #ends the game
            game_over = True

        #checks if the snake hits its body
        elif new_head in snake_body:
            game_over = True

        else:

            #adds the new head to the snake
            snake_body.insert(0, new_head)

            #creates rectangles to check food collision
            snake_rect = pygame.Rect(
                new_head[0],
                new_head[1],
                block_size,
                block_size
            )

            food_rect = pygame.Rect(
                food_position[0] - 15,
                food_position[1] - 15,
                30,
                30
            )

            #checks if the snake touches the food
            if snake_rect.colliderect(food_rect):

                #adds one point to the score
                score = score + 1

                #adds one new random colored block
                snake_colors.append(random.choice(game_colors))

                #moves the food to a random location
                food_position = create_food()

                #gives the food a new random direction
                food_x_direction = random.choice([-3, 3])
                food_y_direction = random.choice([-3, 3])

                #changes the food color
                food_color = random.choice(game_colors)

            else:

                #removes the last block when food is not eaten
                snake_body.pop()

    #fills the screen with the background color
    screen.fill(color)

    #creates the white game area
    pygame.draw.rect(screen, white, (0, 80, 800, 520))

    #calls the title text
    draw_text(
        "Welcome to the Snake Game!!",
        text_font,
        black,
        235,
        15
    )

    #calls the instructions
    draw_text(
        "Use the direction buttons to navigate the snake to eat the food",
        text_font,
        black,
        100,
        45
    )

    #shows the score
    draw_text(
        "Score: " + str(score),
        text_font,
        black,
        10,
        10
    )

    #draws the food
    pygame.draw.circle(
        screen,
        food_color,
        (food_position[0], food_position[1]),
        15
    )

    #draws every obstacle
    for obstacle_number in range(len(obstacles)):

        #gets the obstacle
        obstacle = obstacles[obstacle_number]

        #gets the obstacle color
        obstacle_color = obstacle_colors[obstacle_number]

        #draws the obstacle
        pygame.draw.rect(
            screen,
            obstacle_color,
            obstacle
        )

        #draws a black border around the obstacle
        pygame.draw.rect(
            screen,
            black,
            obstacle,
            2
        )

    #draws every snake body block
    for block_number in range(len(snake_body)):

        #gets the current snake block
        block = snake_body[block_number]

        #gets the current snake block color
        block_color = snake_colors[block_number]

        #draws the snake block
        pygame.draw.rect(
            screen,
            block_color,
            (block[0], block[1], block_size, block_size)
        )

        #draws a black border around the snake block
        pygame.draw.rect(
            screen,
            black,
            (block[0], block[1], block_size, block_size),
            1
        )

    #shows the game over screen
    if game_over == True:

        #draws the game over box
        pygame.draw.rect(
            screen,
            dark_purple,
            (170, 180, 460, 250)
        )

        #shows game over
        draw_text(
            "GAME OVER",
            large_font,
            white,
            265,
            205
        )

        #shows the final score
        draw_text(
            "Final Score: " + str(score),
            text_font,
            white,
            325,
            275
        )

        #shows obstacle message
        if hit_obstacle == True:
            draw_text(
                "You touched an obstacle!",
                text_font,
                white,
                290,
                305
            )

        #shows the winner or loser message
        if score > 5:
            draw_text(
                "Congratulations you won!!",
                text_font,
                white,
                280,
                335
            )

        else:
            draw_text(
                "Sorry, you lost",
                text_font,
                white,
                335,
                335
            )

        #shows restart instructions
        draw_text(
            "Press R to start again",
            text_font,
            white,
            295,
            370
        )

        #shows quit instructions
        draw_text(
            "Press Q to quit",
            text_font,
            white,
            325,
            400
        )

    #shows the screen
    pygame.display.update()

    #controls the speed
    clock.tick(game_speed)

#closes pygame
pygame.quit()