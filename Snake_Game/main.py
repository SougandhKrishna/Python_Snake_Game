import pygame
import random

pygame.init()   # The main game window

screen_width = 800  #Screen Width
screen_height = 800 #Screen Height

dis = pygame.display.set_mode((screen_width, screen_height))    #Making Screen

pygame.display.set_caption('Snake Game')    #Title
background_image = pygame.image.load("Untitled1.png")

clock = pygame.time.Clock()

#Defining some standard Colours
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
orange = (255, 165, 0)
yellow = (255, 255 ,0)

red1 = (255, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0,255,0)

blue1 = (50, 150, 255)
bright_blue = (75, 225, 255)


position_of_snake = 10  #Starting Position of Snake

#Position of obstacles
obs1 = 30
obs2 = 50
obs3 = 80
obs4 = 100
obs5 = 130
obs6 = 150
obs7 = 180
obs8 = 200
obs9 = 230
obs10 = 250
obs11 = 550
obs12 = 570
obs13 = 600
obs14 = 620
obs15 = 650
obs16 = 670
obs17 = 700
obs18 = 720
obs19 = 750
obs20 = 770

#Sound Effects
streak2 = pygame.mixer.Sound('laser2.mp3')
streak1 = pygame.mixer.Sound('laser1.mp3')
streak3 = pygame.mixer.Sound('laser3.mp3')
streak4 = pygame.mixer.Sound('laser4.mp3')
streak5 = pygame.mixer.Sound('laser5.mp3')
streak6 = pygame.mixer.Sound('streak5.mp3')
streak7 = pygame.mixer.Sound('streak6.mp3')
poison = pygame.mixer.Sound('poison.mp3')
loose = pygame.mixer.Sound('lose.mp3')
mov = pygame.mixer.Sound('switch3.wav')
mov_over = pygame.mixer.Sound('coin.mp3')
hemlo = pygame.mixer.Sound('instruction.mp3')

# Function to store the increased length of the snake in the form of a list
def new_snake(position_of_pixel, body_list):
    for part in body_list:
        pygame.draw.rect(dis, white, [part[0], part[1], position_of_pixel, position_of_pixel])


# Function to display the score
def display_of_score(score):
    font = pygame.font.SysFont('freesansbold', 60)
    text = font.render("Score: " + str(score), True, white)
    dis.blit(text, [10, 10])

def display_msg(fonts,size,texts,x_pos,y_pos,color,background=None):
    font = pygame.font.SysFont(fonts,size)
    text = font.render(texts, True, color,background)
    textRect = text.get_rect()
    textRect.center = ((x_pos, y_pos))
    dis.blit(text, textRect)
    pygame.display.update()

def button(msg, x, y, w, h, ic, ac,color,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(dis, ac,(x,y,w,h))
        #mov_over.play()
        if click[0] == 1 and action != None:
            mov_over.play()
            action()
    else:
        pygame.draw.rect(dis, ic,(x,y,w,h))

    display_msg('comicsansms', 40, msg, x+(w/2), y+(h/2), color)


def pause():
    loop = 1

    display_msg('freesansbold', 125, 'PAUSED', (screen_width/2),screen_height/4, white)
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    loop = 0

def blit_text(surface, text, pos, font, color=yellow,color2=black):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color,color2)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


def instructions():

    instruction = True
    pygame.mixer.Sound.play(hemlo)

    while instruction:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        text = "1: Obstacles are fixed objects and are diplayed by blocks RED in color.\n" \
               "2: Use Arrow keys to move the snake around the screen.\n" \
               "3: Eating the food(represented by GREEN) will result in increase in length of the snake by unity.\n" \
               "4: While eating the poison(represented by BLUE) will result in decrease in length by unity.\n" \
               "5: Each time the speed of the snake(WHITE in color) will increase.\n" \
               "6: Press ESC Key for pausing and the spacebar for resuming the game.\n" \
               "7: Hitting the boundaries will result in the end of game.\n" \
               "8: Similarly if length of snake decreases beyond one it will end the game.\n" \
               "9: Avoid obstacles if you can :)\n" \
               "10: Food and poison will be spawning randomly across the map.\n"
        font = pygame.font.SysFont('Arial', 28)

        dis.blit(background_image, [0, 0])
        blit_text(dis, text, (40, 70), font)
        pygame.display.update()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 100<mouse[0]<100+150 and 550<mouse[1]<550+80:
            pygame.draw.rect(dis, bright_blue, (100, 550, 150, 80))

            if click[0]==1:
                mov_over.play()
                game_intro()
        else:
            pygame.draw.rect(dis,blue1, (100, 550, 150, 80))

        if 550<mouse[0]<550+150 and 550<mouse[1]<550+80:
            pygame.draw.rect(dis, bright_blue, (550, 550, 150, 80))

            if click[0]==1:
                mov_over.play()
                quitgame()
        else:
            pygame.draw.rect(dis, blue1, (550, 550, 150, 80))

        display_msg('freesansbold', 40, 'GO BACK', 100 + 150 / 2, 550 + 80 / 2, black)
        display_msg('freesansbold', 40, 'QUIT', 550 + 150 / 2, 550 + 80 / 2, black)
        clock.tick(5)


def quitgame():
    pygame.quit()
    quit()


def game_intro():
    pygame.mixer.init()
    pygame.mixer.music.load("intro.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(loops=-1)

    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

        dis.fill((238,232,170))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 100<mouse[0]<100+250 and 450<mouse[1]<450+80:

            pygame.draw.rect(dis, bright_blue, (100, 450, 250, 80))
            if click[0]==1:
                mov_over.play()
                pygame.mixer.music.stop()
                loop_of_game()
        else:
            pygame.draw.rect(dis,blue1, (100, 450, 250, 80))

        if 475<mouse[0]<475+250 and 450<mouse[1]<450+80:
            pygame.draw.rect(dis, bright_blue, (475, 450, 250, 80))

            if click[0]==1:
                mov_over.play()
                pygame.mixer.music.stop()
                quitgame()
        else:
            pygame.draw.rect(dis, blue1, (475, 450, 250, 80))

        if 350-62.5<mouse[0]<350-62.5+250 and 570<mouse[1]<570+80:
            pygame.draw.rect(dis, bright_blue, (287.5, 570, 250, 80))

            if click[0]==1:
                mov_over.play()
                instructions()
        else:
            pygame.draw.rect(dis, blue1, (287.5, 570, 250, 80))

        display_msg('showcardgothic', 125, 'SNAKE GAME', screen_width / 2, screen_height / 3,white, black)
        display_msg('freesansbold', 40, 'LETS PLAY!!', 100 + 250 / 2, 450 + 80 / 2, black)
        display_msg('freesansbold', 40, 'QUIT', 475 + 250 / 2, 450 + 80 / 2, black)
        display_msg('freesansbold', 40, 'INSTRUCTIONS', 287.5 + 250 / 2, 570 + 80 / 2, black)
        clock.tick(5)

def loop_of_game():

    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=-1)

    game_finishes = False
    game_closes = False

    x1 = screen_width/2
    y1 = screen_height/2

    x1_new = 0
    y1_new = 0

    food_on_x = round(random.randrange(0, screen_width - position_of_snake)/10.0) * 10.0
    food_on_y = round(random.randrange(0, screen_height - position_of_snake)/10.0) * 10.0
    psn_on_x = round(random.randrange(0, screen_width - position_of_snake) / 10.0) * 10.0
    psn_on_y = round(random.randrange(0, screen_height - position_of_snake) / 10.0) * 10.0

    body_of_snake = []  # Variable to store the increasing length of the snake
    length_of_snake = 3  # The initial length of the snake
    snake_speed = 20  # This is the speed of the snake
    streak = 0 #used to measure the streak of eating the food

# This is the loop that controls the whole game. Each time the snake's direction is changed with the arrow
# head keys, the loop works in such a way that it changes the direction of the snake accordingly. The snake's
# position is inclined towards the piece of food upon which it will feed and thus will have a increase in its
# length by 1 unit and also an increase in the speed of the snake.
# The game ends when one touches the boundaries of the screen or touches any of the obstacles which are red
# in colour. Also the game ends when you try to change the direction of the snake moving when its length becomes
# greater than or equal to 3 units.

    while not game_finishes:

        while game_closes == True:
            pygame.mixer.music.fadeout(5)
            display_msg('freesansbold', 100, 'GAME OVER!!', screen_width / 2, screen_height /2.5, white)

            if length_of_snake<3:
                display_of_score(0)
            else:
                display_of_score(length_of_snake - 3)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("Retry", 100, 435, 200, 100, green, bright_green,black,loop_of_game)
            button("Quit", 500, 435, 200, 100, red, bright_red,black, quitgame)

            pygame.display.update()
            clock.tick(15)

        # This is the loop for controlling the movement of the snake using the arrow keys. The modules of pygame
        # have been directly used here.

        for i in pygame.event.get():

            if i.type == pygame.QUIT:
                quitgame()

            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    pygame.mixer.Sound.play(mov)
                    x1_new = -position_of_snake
                    y1_new = 0

                elif i.key == pygame.K_RIGHT:
                    pygame.mixer.Sound.play(mov)
                    x1_new = position_of_snake
                    y1_new = 0

                elif i.key == pygame.K_UP:
                    pygame.mixer.Sound.play(mov)
                    y1_new = -position_of_snake
                    x1_new = 0

                elif i.key == pygame.K_DOWN:
                    pygame.mixer.Sound.play(mov)
                    y1_new = position_of_snake
                    x1_new = 0

                elif i.key == pygame.K_ESCAPE:
                    pause()

        # For the snake hitting the boundaries of the screen or changing the direction of the moving snake.
        if x1 >= screen_width or x1 < 0 or y1 >= screen_height or y1 < 0:
            pygame.mixer.Sound.play(loose)
            game_closes = True

        # Changing the co-ordinates of the snake's position.
        x1 += x1_new
        y1 += y1_new

        dis.fill(black)  # The colour of the main game window

        pygame.draw.rect(dis, green, [food_on_x, food_on_y, position_of_snake, position_of_snake])
        pygame.draw.rect(dis, blue, [psn_on_x, psn_on_y, position_of_snake, position_of_snake])

        pygame.draw.rect(dis, red1, [obs2, obs2, 10, 10])
        pygame.draw.rect(dis, red1, [obs4, obs4, 10, 10])
        pygame.draw.rect(dis, red1, [obs6, obs6, 10, 10])
        pygame.draw.rect(dis, red1, [obs8, obs8, 10, 10])
        pygame.draw.rect(dis, red1, [obs10, obs10, 10, 10])
        pygame.draw.rect(dis, red1, [obs11, obs11, 10, 10])
        pygame.draw.rect(dis, red1, [obs13, obs13, 10, 10])
        pygame.draw.rect(dis, red1, [obs15, obs15, 10, 10])
        pygame.draw.rect(dis, red1, [obs17, obs17, 10, 10])
        pygame.draw.rect(dis, red1, [obs19, obs19, 10, 10])
        pygame.draw.rect(dis, red1, [obs10, obs11, 10, 10])
        pygame.draw.rect(dis, red1, [obs8, obs13, 10, 10])
        pygame.draw.rect(dis, red1, [obs6, obs15, 10, 10])
        pygame.draw.rect(dis, red1, [obs4, obs17, 10, 10])
        pygame.draw.rect(dis, red1, [obs2, obs19, 10, 10])
        pygame.draw.rect(dis, red1, [obs19, obs2, 10, 10])
        pygame.draw.rect(dis, red1, [obs17, obs4, 10, 10])
        pygame.draw.rect(dis, red1, [obs15, obs6, 10, 10])
        pygame.draw.rect(dis, red1, [obs13, obs8, 10, 10])
        pygame.draw.rect(dis, red1, [obs11, obs10, 10, 10])

# Now these statements are changing the length the length of the snake with every intake of food. The length
# of the snake is changed as a manner appending the list.

        # Placing the food now on new locations for everytime after the snake gets the food.

        if x1 == food_on_x and y1 == food_on_y:

            food_on_x = round(random.randrange(0, screen_width - position_of_snake)/10.0) * 10.0
            food_on_y = round(random.randrange(0, screen_height - position_of_snake)/10.0) * 10.0
            length_of_snake += 1
            snake_speed += 2
            streak += 1

            if streak == 1:
                pygame.mixer.Sound.play(streak1)

            if streak == 2:
                pygame.mixer.Sound.play(streak2)

            if streak == 3:
                pygame.mixer.Sound.play(streak3)

            if streak == 4:
                pygame.mixer.Sound.play(streak4)

            if streak >= 5:
                pygame.mixer.Sound.play(streak5)

            if streak == 8:
                pygame.mixer.Sound.play(streak6)

            if streak == 10:
                pygame.mixer.Sound.play(streak7)

        if x1 == psn_on_x and y1 == psn_on_y:
            streak = 0
            pygame.mixer.Sound.play(poison)

            if length_of_snake == 1:
                length_of_snake = 3
                game_closes = True
                pygame.mixer.Sound.play(loose)

            else:
                psn_on_x = round(random.randrange(0, screen_width - position_of_snake) / 10.0) * 10.0
                psn_on_y = round(random.randrange(0, screen_height - position_of_snake) / 10.0) * 10.0
                length_of_snake -= 1
                snake_speed += 2

        head_of_snake = []   #[10,10]
        head_of_snake.append(x1)
        head_of_snake.append(y1)
        body_of_snake.append(head_of_snake)
        if len(body_of_snake) > length_of_snake:
            counter = 0
            while len(body_of_snake) != length_of_snake:
                del body_of_snake[counter]
                counter += 1

        a = len(body_of_snake)
        for i in body_of_snake[a - 1]:
            if i == head_of_snake:
                game_closes = True
                pygame.mixer.Sound.play(loose)

        new_snake(position_of_snake, body_of_snake)

        pygame.display.update()

        if (x1 == obs2 and y1 == obs2) or (x1 == obs4 and y1 == obs4) or (x1 == obs6 and y1 == obs6) or (x1 == obs8 and y1 == obs8) or (x1 == obs10 and y1 == obs10) or (x1 == obs11 and y1 == obs11) or (x1 == obs13 and y1 == obs13) or (x1 == obs15 and y1 == obs15) or (x1 == obs17 and y1 == obs17) or (x1 == obs19 and y1 == obs19) or (x1 == obs10 and y1 == obs11) or (x1 == obs8 and y1 == obs13) or (x1 == obs6 and y1 == obs15) or (x1 == obs4 and y1 == obs17) or (x1 == obs2 and y1 == obs19) or (x1 == obs11 and y1 == obs10) or (x1 == obs13 and y1 == obs8) or (x1 == obs15 and y1 == obs6) or (x1 == obs17 and y1 == obs4) or (x1 == obs19 and y1 == obs2):
            game_closes = True
            pygame.mixer.Sound.play(loose)

        clock.tick(snake_speed)


game_intro()
quitgame()

