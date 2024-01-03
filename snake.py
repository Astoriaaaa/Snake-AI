import pygame
import time
import random
from neuralnet import *

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
orange = (255, 165, 0)
width, height = 600, 390

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("NeuralNine Snake Game")

clock = pygame.time.Clock()

snake_size = 30
snake_speed = 30

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 25)

def print_score(score, snakeNumber, gen, points, cr):
    text = score_font.render("score: " + str(score) + " snake number: " + str(snakeNumber + 1) + " Generation: " + str(gen + 1) + " Points: " + str(points) + " steps: " + str(cr), True, orange)
    game_display.blit(text, [0, 0])

def draw_snake(snake_size, snake_pixels): 
    for pixel in snake_pixels: 
        pygame.draw.rect(game_display, white, (pixel[0], pixel[1], snake_size, snake_size))


def run_game(player, snakeNumber, gen): 

    maxsteps = 300
    curentSteps = 0
    points = 0
    currentDirection = 'UP'

    game_over = False
    game_close = False


    x = random.randint(0, 19) * 30
    y = random.randint(0, 12) * 30


    snake_pixels = []
    snake_length = 1

    target_x = random.randint(0, 20) * 30
    target_y = random.randint(0, 13) * 30

    while not game_over: 
        if curentSteps == maxsteps: 
            return points
        distancetofoodx = abs(target_x - x)
        distancetofoody = abs(target_y - y)
        state = ""
        if currentDirection == 'UP':
            if y - 30 <= 0 or [x, y - 30] in snake_pixels: 
                state += "0"
            else: state += "1"
            if x - 30 <= 0 or [x - 30, y] in snake_pixels: 
                state += "0"
            else: state += "1"
            if x + 30 >= width or [x + 30, y] in snake_pixels: 
                state += "0"
            else: state += "1"
            if target_y > y: state += "0" 
            else: state += "1"
            if target_x > x: state += "0" 
            else: state += "1"
            if target_x < x: state += "0"
            else: state += "1"
        
        if currentDirection == 'R': 
            if x + 30 <= width or [x + 30, y] in snake_pixels: state += "0"
            else: state += "1"
            if y - 30 <= 0 or [x, y - 30] in snake_pixels: state += "0"
            else: state += "1"
            if y + 30 >= width or [x, y + 30] in snake_pixels: state += "0"
            else: state += "1"
            if target_x < x: state += "0" 
            else: state += "1"
            if target_y > y: state += "0" 
            else: state += "1"
            if target_y < y: state += "0"
            else: state += "1"

        if currentDirection == 'D': 
            if y + 30 <= height or [x, y + 30] in snake_pixels: state += "0"
            else: state += "1"
            if x + 30 <= width or [x + 30, y] in snake_pixels: state += "0"
            else: state += "1"
            if x - 30 >= width or [x - 30, y] in snake_pixels: state += "0"
            else: state += "1"
            if target_y < y: state += "0" 
            else: state += "1"
            if target_x < x: state += "0" 
            else: state += "1"
            if target_x > x: state += "0"
            else: state += "1"

        if currentDirection == 'L': 
            if x - 30 <= width or [x - 30, y] in snake_pixels: state += "0"
            else: state += "1"
            if y + 30 <= 0 or [x, y + 30] in snake_pixels: state += "0"
            else: state += "1"
            if y - 30 >= width or [x, y - 30] in snake_pixels: state += "0"
            else: state += "1"
            if target_x > x: state += "0" 
            else: state += "1"
            if target_y < y: state += "0" 
            else: state += "1"
            if target_y > y: state += "0"
            else: state += "1"

        diretion = neuralnet(state, player)

        if currentDirection == 'UP': 
            if diretion == 'F': 
                y -= 30
            if diretion == 'R': 
                x += 30
                currentDirection = 'R'
            if diretion == 'L': 
                x -= 30
                currentDirection = 'L'
        elif currentDirection == 'D': 
            if diretion == 'F': 
                y += 30
            if diretion == 'R': 
                x -= 30
                currentDirection = 'L'
            if diretion == 'L': 
                x += 30
                currentDirection = 'R'
        elif currentDirection == 'R': 
            if diretion == 'F': 
                x += 30
            if diretion == 'R': 
                y += 30
                currentDirection = 'D'
            if diretion == 'L': 
                y -= 30
                currentDirection = "UP"
        elif currentDirection == 'L': 
            if diretion == 'F': 
                x -= 30
            if diretion == 'R': 
                y -= 30
                currentDirection == 'UP'
            if diretion == 'L': 
                y += 30
                currentDirection == 'D'
        curentSteps += 1

        currectdistancetofoodx = abs(target_x - x)
        currectdistancetofoody = abs(target_y - y)

        
        snake_pixels.append([x, y])  

        if len(snake_pixels) > snake_length: 
            del snake_pixels[0]

        for pixel in snake_pixels[:-1] : 
            if pixel == [x, y]: 
                game_over == True
                return points
            
        if x>= width or x<= 0 or y >= height or y < 0: 
            game_over == True
            return points
            
        if currectdistancetofoodx > distancetofoodx or currectdistancetofoody > distancetofoody: 
            points -= 50
        else: points += 20


        if x == target_x and y == target_y: 
            points += 1000
            target_x = random.randint(1, 19) * 30
            target_y = random.randint(1, 12) * 30
            snake_length += 1


        game_display.fill(black)
        pygame.draw.rect(game_display, orange, [target_x, target_y, snake_size, snake_size])
        draw_snake(snake_size, snake_pixels)
        print_score(snake_length - 1, snakeNumber, gen, points, curentSteps)

        pygame.display.update()

       
        
        clock.tick(100)


    



                




