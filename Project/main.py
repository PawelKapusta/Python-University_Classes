import pygame
import random
from pygame import mixer

pygame.font.init()
pygame.mixer.init()

window_width = 800
window_height = 800
table_width = 300
table_height = 600
single_block_size = 30
top_left_x = (window_width - table_width) // 2
top_left_y = window_height - table_height
black_color = (0, 0, 0)
white_color = (255, 255, 255)
grey_color = (128, 128, 128)

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]

shapes = [S, Z, I, O, J, L, T]
colors = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 0, 255), (255, 255, 0), (180, 180, 180)]


class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = colors[shapes.index(shape)]
        self.rotation = 0


def create_grid(locked_pos={}):
    grid = [[black_color for _ in range(10)] for _ in range(20)]

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid


def convert_shape(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def is_valid(shape, grid):
    accepted_positions = [[(j, i) for j in range(10) if grid[i][j] == black_color] for i in range(20)]
    accepted_positions = [j for sub in accepted_positions for j in sub]

    formatted_positions = convert_shape(shape)

    for position in formatted_positions:
        if position not in accepted_positions:
            if position[1] > -1:
                return False
    return True


def is_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True

    return False


def get_shape():
    return Piece(5, 0, random.choice(shapes))


def write_in_the_middle(surface, text, size, color):
    font = pygame.font.SysFont("arial", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (
        top_left_x + table_width / 2 - (label.get_width() / 2), top_left_y + table_height / 2 - label.get_height() / 2))


def draw_grid(surface, grid):
    window_x = top_left_x
    window_y = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, grey_color, (window_x, window_y + i * single_block_size),
                         (window_x + table_width, window_y + i * single_block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, grey_color, (window_x + j * single_block_size, window_y),
                             (window_x + j * single_block_size, window_y + table_height))


def clear_rows(grid, locked):
    counter = 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if black_color not in row:
            counter += 1
            temp = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if counter > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < temp:
                newKey = (x, y + counter)
                locked[newKey] = locked.pop(key)

    return counter


def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('arial', 30)
    label = font.render('Next Shape', 3, white_color)

    window_x = top_left_x + table_width + 50
    window_y = top_left_y + table_height / 2 - 100
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (
                    window_x + j * single_block_size, window_y + i * single_block_size, single_block_size,
                    single_block_size), 0)

    surface.blit(label, (window_x + 10, window_y - 40))


def update_score(current_score):
    score = max_score()

    with open('scores.txt', 'w') as file:
        if int(score) > current_score:
            file.write(str(score))
        else:
            file.write(str(current_score))


def max_score():
    with open('scores.txt', 'r') as file:
        lines = file.readlines()
        score = lines[0].strip()

    return score


def draw_window(surface, grid, score=0, last_score=0):
    surface.fill(black_color)

    pygame.font.init()
    font = pygame.font.SysFont('arial', 60)
    label = font.render('Project game', 1, white_color)

    surface.blit(label, (top_left_x + table_width / 2 - (label.get_width() / 2), 60))

    font = pygame.font.SysFont('arial', 30)
    label = font.render('Score: ' + str(score), 1, white_color)

    window_x = top_left_x + table_width + 50
    window_y = top_left_y + table_height / 2 - 115

    surface.blit(label, (window_x + 20, window_y + 160))

    label = font.render('Best score: ' + last_score, 1, white_color)

    window_x = top_left_x - 230
    window_y = top_left_y + 175

    surface.blit(label, (window_x + 20, window_y + 160))

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],
                             (top_left_x + j * single_block_size, top_left_y + i * single_block_size, single_block_size,
                              single_block_size), 0)

    pygame.draw.rect(surface, white_color, (top_left_x, top_left_y, table_width, table_height), 4)

    draw_grid(surface, grid)


def main(window):
    the_highest_score = max_score()
    locked_positions = {}
    grid = create_grid(locked_positions)

    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not (is_valid(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (is_valid(current_piece, grid)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (is_valid(current_piece, grid)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (is_valid(current_piece, grid)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (is_valid(current_piece, grid)):
                        current_piece.rotation -= 1

        shape_pos = convert_shape(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        draw_window(window, grid, score, the_highest_score)
        draw_next_shape(next_piece, window)
        pygame.display.update()

        if is_lost(locked_positions):
            write_in_the_middle(window, "I'm sorry You lost! :(", 80, white_color)
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            update_score(score)


def main_menu(window):
    run = True
    while run:
        mixer.music.load('music.mp3')
        mixer.music.play(-1)
        window.fill(black_color)
        write_in_the_middle(window, 'Press any key to start your game', 60, white_color)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(window)

    pygame.display.quit()


window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tetris')
main_menu(window)
