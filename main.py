import pygame

pygame.init()
screen = pygame.display.set_mode((750, 750))
running = True

pos = 375,375
tile_size = 30
def draw_block_grid(screen, row, col, tile_size):
    for r in range(row):
        for c in range(col):
             x = c * tile_size
             y = r * tile_size

             Rect = pygame.Rect(x,y,tile_size,tile_size)
             
             pygame.draw.rect(screen,(128, 128, 128),Rect, 0)
             pygame.draw.line(screen,"black",(0,r * tile_size),(750,r * tile_size))
             pygame.draw.line(screen,"black",(c * tile_size,0),(c * tile_size,750))
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        

    #pygame.draw.rect(screen, (0,0,255), (0,0,30,30))
    draw_block_grid(screen, 150, 150, tile_size)
    pygame.draw.rect(screen,(0, 0, 255),(0,0,30,30), 0)
    pygame.display.flip()
    