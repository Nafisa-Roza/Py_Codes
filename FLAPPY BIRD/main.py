import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(900 ,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(900 ,random_pipe_pos - 500))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def check_collision(pipes):
    for pipe in pipes:
       if bird_rect.colliderect(pipe):
           return False

    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False

    return True

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe, pipe)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(str(int(score)),True,(255,255,255))
        score_rect = score_surface.get_rect(center = (288,100))
        screen.blit(score_surface,score_rect)

    if game_state == 'game_over':
        score_surface = game_font.render(f'Score: {int(score)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center=(288, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f'High Score: {int(high_score)}', True, (255, 255, 255))
        high_score_rect = score_surface.get_rect(center=(288, 820))
        screen.blit(high_score_surface, high_score_rect)

pygame.init()
screen = pygame.display.set_mode((950, 950))
clock = pygame.time.Clock()
game_font = pygame.font.Font('04B_19.ttf',40)

gravity = 0.25
bird_movement = 0
game_active = True
score = 0
high_score = 0
bg_surface = pygame.image.load('flappy/background.png').convert()

floor_surface = pygame.image.load('flappy/floor.jpg').convert()
floor_x_pos = 0

pipe_surface = pygame.image.load('flappy/pipe1.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE,1200)

pipe_height =[600,800,2000]

bird_surface = pygame.image.load('flappy/meaw.png').convert()

bird_rect = bird_surface.get_rect(center = (100,512))

game_over_surface = pygame.image.load('flappy/gameover.jpg').convert()
game_over_rect = game_over_surface.get_rect(center=(450,512))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement -= 12
            if event.key == pygame.K_SPACE and game_active == False:
                game_active == True
                score = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface,(0,0))

    if game_active:
        bird_movement += gravity
        bird_rect.centery += bird_movement

        screen.blit(bird_surface, bird_rect)
        game_active = check_collision(pipe_list)

        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
        score += 0.01
        score_display('main_game')

    else:
        screen.blit(game_over_surface, game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')

    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0


    pygame.display.update()
    clock.tick(120)