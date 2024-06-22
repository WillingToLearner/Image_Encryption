
try:
    import pygame
    from pygame import surfarray
    from pygame.locals import *
    import copy
except ImportError:
    raise ImportError('Error Importing Pygame/surfarray/time module')

# Function to load a file, and return an array of pixels
def getPixelArray(filename):
    image = pygame.image.load(filename)
    return pygame.surfarray.array3d(image)

# To get the new coordinates from the old coordinates
def iterate(x, y, N):
    return (y % N, (x + y) % N)

pixels = getPixelArray('cat.jpg')   # choose the image to use
pix2 = copy.copy(pixels)   # Copy the pixel array

size = pixels.shape[:2]    # Find out the size of the image
if not size[0] == size[1]:
    print ("I was expecting a square image!")

N = size[0]   # The side length of the square

size = [2*i for i in size]   # We will zoom in by a factor of 2.

# Create the display window
screen = pygame.display.set_mode(size) 
pygame.display.set_caption("The Fibonacci Feline Map")
pygame.display.flip()

interval = 300   # How long to wait between frames, in milliseconds

done = False
while not done:
    for e in pygame.event.get():
        if e.type == QUIT:
            done = True    # exit gracefully

    # loop over the pixel coordinates
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            # use the Fibonacci rule for moving the pixels around
            pt = iterate(i, j, N)
            # copy each pixel into the new array
            pix2[i, j, :] = pixels[pt[0], pt[1], :]
            
    pixels = copy.copy(pix2)   # make a copy, for the next loop
    mysurf = surfarray.make_surface(pixels)   # display the scrambled image
    pygame.transform.scale2x(mysurf, screen)
    pygame.display.flip()
    pygame.time.delay(interval)  # wait for "interval" milliseconds

pygame.quit()