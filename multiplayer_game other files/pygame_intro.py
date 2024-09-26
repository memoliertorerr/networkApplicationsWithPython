#Pygame tutorial
import pygame

#Initializing the pygame
pygame.init()

#Set constants for the game
WINDOWS_WIDTH = 600
WINDOWS_HEIGHT = 600
ROUND_TIME = 25

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PLAYER_COLOR = (125, 55, 200)

FPS = 30
clock = pygame.time.Clock()
font = pygame.font.SysFont('gabriola', 28)

#Create game windows
display_surface = pygame.display.set_mode((WINDOWS_WIDTH, WINDOWS_HEIGHT))
pygame.display.set_caption("---PyGame Experiment---")

#Create classes
class Player():
    '''A player class the user can control'''
    def __init__(self, x, y, size, color):
        '''Initialize the player class'''
        #Set the player values
        self.x = x
        self.y = y
        self.size = size
        self.color = color

        #Initialize other player values
        self.dx = 0
        self.dy = 0
        self.coord = (self.x, self.y, self.size, self.size)

    def update(self):
        '''Update the player by changing the coordinates in the playspace'''
        #Check to see if a key is being held down
        keys = pygame.key.get_pressed()

        #Create a rect to chart player movement
        player_rect = pygame.draw.rect(display_surface, self.color, self.coord)

        #Move the player
        if keys[pygame.K_UP] or keys[pygame.K_w] and player_rect.top > 0:
            self.dx = 0
            self.dy = -1 * self.size
        elif keys[pygame.K_DOWN] or keys[pygame.K_s] and player_rect.bottom < WINDOWS_HEIGHT:
            self.dx = 0
            self.dy = 1 * self.size
        elif keys[pygame.K_LEFT] or keys[pygame.K_a] and player_rect.left > 0:
            self.dx = -1 * self.size
            self.dy = 0
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d] and player_rect.right < WINDOWS_WIDTH:
            self.dx = 1 * self.size
            self.dy = 0
        else:
            self.dx = 0
            self.dy = 0
        
        #Update the coordinates of the player
        self.x += self.dx
        self.y += self.dy
        self.coord = (self.x, self.y, self.size, self.size)


class Game():
    '''Class to control the gameplay'''
    def __init__(self, player):
        '''Intialize the game class'''
        self.player = player

        #Create variables to hold the state of the game
        self.frame_count = 0 #Help determine how long 1 second is
        self.round_time = ROUND_TIME #current round time


    def update(self):
        '''Update the game by advancing the clock, update the player too'''
        #Advance the in-game tier
        self.frame_count += 1
        if self.frame_count % FPS == 0:
            self.round_time -= 1
            self.frame_count = 0

        #Update the player
        self.player.update()


    def draw(self):
        '''Draw the game and game assets to the playspace'''
        #Draw the player
        pygame.draw.rect(display_surface, self.player.color, self.player.coord)

        #Create the round time text and draw it
        time_text = font.render(f"Time: {self.round_time}", True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.center = (WINDOWS_WIDTH/2, 15)
        display_surface.blit(time_text, time_rect)


#Create the player and game object
my_player = Player(0, 0, 25, PLAYER_COLOR)
my_game = Game(my_player)

#The main game loop
running = True
while running:
    #Check to see if user wants to quit
    for event in pygame.event.get():    #Other events get ignored
        if event.type == pygame.QUIT:
            running = False
    
    #Filling the surface
    display_surface.fill(BLACK)

    #Update and draw the assets
    my_game.update()
    my_game.draw()
    
    #Update the display and tick the clock
    pygame.display.update()
    clock.tick(FPS)