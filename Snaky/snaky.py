import random
import pygame
import sys
from pygame.locals import *

class Config:
    FPS = 10
    WINDOW_WIDTH = 640
    WINDOW_HEIGHT = 480
    CELL_SIZE = 40
    CELL_WIDTH = WINDOW_WIDTH // CELL_SIZE
    CELL_HEIGHT = WINDOW_HEIGHT // CELL_SIZE
    COLORS = {
        'white': (255, 255, 255),
        'black': (0, 0, 0),
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'dark_green': (0, 155, 0),
        'dark_gray': (40, 40, 40)
    }

class SnakeGame:
    def __init__(self):
        assert Config.WINDOW_WIDTH % Config.CELL_SIZE == 0, "Window width must be a multiple of cell size."
        assert Config.WINDOW_HEIGHT % Config.CELL_SIZE == 0, "Window height must be a multiple of cell size."
        pygame.init()
        self.fps_clock = pygame.time.Clock()
        self.display_surf = pygame.display.set_mode((Config.WINDOW_WIDTH, Config.WINDOW_HEIGHT))
        pygame.display.set_caption('IQDOTNET CODE - SNAKY')
        self.font = pygame.font.Font('freesansbold.ttf', 18)
        self.apple_sound = pygame.mixer.Sound('apple_crunch.wav')
        self.game_over_sound = pygame.mixer.Sound('game_over.wav')
        self.start_screen_text = self.font.render('Press any key to start', True, Config.COLORS['white'])
        self.game_over_text = self.font.render('Game Over! Press any key to play again', True, Config.COLORS['white'])

    def run(self):
        self.show_start_screen()
        while True:
            if not self.run_game():
                self.show_game_over_screen()

    def run_game(self):
        worm_coords = self.get_initial_snake_coords()
        direction = 'right'
        apple = self.get_random_location(worm_coords)
        score = 0
        speed = Config.FPS

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.terminate()
                    new_direction = self.update_direction(event.key, direction)
                    if new_direction:
                        direction = new_direction

            if self.is_collision(worm_coords):
                self.game_over_sound.play()
                return False

            if worm_coords[0] == apple:
                self.apple_sound.play()
                score += 1
                speed += 1  # Increase speed as score increases
                apple = self.get_random_location(worm_coords)
            else:
                del worm_coords[-1]

            new_head = self.get_new_head_position(worm_coords[0], direction)
            worm_coords.insert(0, new_head)

            self.draw_everything(worm_coords, apple, score)
            pygame.display.update()
            self.fps_clock.tick(speed)

    def update_direction(self, event_key, current_direction):
        direction_map = {
            K_LEFT: 'left',
            K_a: 'left',
            K_RIGHT: 'right',
            K_d: 'right',
            K_UP: 'up',
            K_w: 'up',
            K_DOWN: 'down',
            K_s: 'down',
        }
        opposite_direction = {'up': 'down', 'down': 'up', 'left': 'right', 'right': 'left'}
        new_direction = direction_map.get(event_key)
        if new_direction and new_direction != opposite_direction[current_direction]:
            return new_direction
        return None

    def is_collision(self, worm_coords):
        head = worm_coords[0]
        if (head['x'] < 0 or head['x'] >= Config.CELL_WIDTH or head['y'] < 0 or head['y'] >= Config.CELL_HEIGHT
            or len(set(tuple(segment.values()) for segment in worm_coords)) != len(worm_coords)):
            return True
        return False

    def get_new_head_position(self, head, direction):
        directions = {
            'up': {'x': head['x'], 'y': head['y'] - 1},
            'down': {'x': head['x'], 'y': head['y'] + 1},
            'left': {'x': head['x'] - 1, 'y': head['y']},
            'right': {'x': head['x'] + 1, 'y': head['y']}
        }
        return directions[direction]

    def get_random_location(self, worm):
        valid_locations = [{'x': x, 'y': y} for x in range(Config.CELL_WIDTH) for y in range(Config.CELL_HEIGHT) if {'x': x, 'y': y} not in worm]
        return random.choice(valid_locations)

    def get_initial_snake_coords(self):
        startx = random.randint(5, Config.CELL_WIDTH - 6)
        starty = random.randint(5, Config.CELL_HEIGHT - 6)
        return [{'x': startx, 'y': starty}, {'x': startx - 1, 'y': starty}, {'x': startx - 2, 'y': starty}]

    def draw_everything(self, worm_coords, apple, score):
        self.display_surf.fill(Config.COLORS['black'])
        self.draw_grid()
        self.draw_worm(worm_coords)
        self.draw_apple(apple)
        self.draw_score(score)

    def draw_grid(self):
        for x in range(0, Config.WINDOW_WIDTH, Config.CELL_SIZE):
            pygame.draw.line(self.display_surf, Config.COLORS['dark_gray'], (x, 0), (x, Config.WINDOW_HEIGHT))
        for y in range(0, Config.WINDOW_HEIGHT, Config.CELL_SIZE):
            pygame.draw.line(self.display_surf, Config.COLORS['dark_gray'], (0, y), (Config.WINDOW_WIDTH, y))

    def draw_worm(self, worm_coords):
        for coord in worm_coords:
            rect = pygame.Rect(coord['x'] * Config.CELL_SIZE, coord['y'] * Config.CELL_SIZE, Config.CELL_SIZE, Config.CELL_SIZE)
            pygame.draw.rect(self.display_surf, Config.COLORS['dark_green'], rect)
            inner_rect = pygame.Rect(coord['x'] * Config.CELL_SIZE + 4, coord['y'] * Config.CELL_SIZE + 4, Config.CELL_SIZE - 8, Config.CELL_SIZE - 8)
            pygame.draw.rect(self.display_surf, Config.COLORS['green'], inner_rect)

    def draw_apple(self, coord):
        rect = pygame.Rect(coord['x'] * Config.CELL_SIZE, coord['y'] * Config.CELL_SIZE, Config.CELL_SIZE, Config.CELL_SIZE)
        pygame.draw.rect(self.display_surf, Config.COLORS['red'], rect)

    def draw_score(self, score):
        score_surf = self.font.render(f'Score: {score}', True, Config.COLORS['white'])
        score_rect = score_surf.get_rect()
        score_rect.topleft = (Config.WINDOW_WIDTH - 120, 10)
        self.display_surf.blit(score_surf, score_rect)

    def show_start_screen(self):
        self.display_surf.fill(Config.COLORS['black'])
        start_screen_rect = self.start_screen_text.get_rect(center=(Config.WINDOW_WIDTH // 2, Config.WINDOW_HEIGHT // 2))
        self.display_surf.blit(self.start_screen_text, start_screen_rect)
        pygame.display.update()
        self.wait_for_key()

    def show_game_over_screen(self):
        self.display_surf.fill(Config.COLORS['black'])
        game_over_rect = self.game_over_text.get_rect(center=(Config.WINDOW_WIDTH // 2, Config.WINDOW_HEIGHT // 2))
        self.display_surf.blit(self.game_over_text, game_over_rect)
        pygame.display.update()
        self.wait_for_key()

    def wait_for_key(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.terminate()
                elif event.type == KEYDOWN:
                    return

    def terminate(self):
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    game = SnakeGame()
    game.run()
#IQDOTNET CODE - by Nelson Guajardo