import pygame

CANVAS_SIZE = 400
CELL_SIZE = 40
ERASER_SIZE = 20
BACKGROUND_COLOR = (255, 255, 255)
GRID_COLOR = (0, 0, 255) 
ERASER_COLOR = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((CANVAS_SIZE, CANVAS_SIZE))
pygame.display.set_caption("Eraser Tool")

grid = []
for row in range(0, CANVAS_SIZE, CELL_SIZE):
    for col in range(0, CANVAS_SIZE, CELL_SIZE):
        rect = pygame.Rect(col, row, CELL_SIZE, CELL_SIZE)
        grid.append(rect)


running = True
while running:
    screen.fill(BACKGROUND_COLOR) 

    for rect in grid:
        pygame.draw.rect(screen, GRID_COLOR, rect)

    mouse_x, mouse_y = pygame.mouse.get_pos()
    eraser = pygame.Rect(mouse_x, mouse_y, ERASER_SIZE, ERASER_SIZE)

    if pygame.mouse.get_pressed()[0]:  
        grid = [rect for rect in grid if not rect.colliderect(eraser)]

    pygame.draw.rect(screen, ERASER_COLOR, eraser)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip() 

pygame.quit()
