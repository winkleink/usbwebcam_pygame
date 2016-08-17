import sys
import pygame
import pygame.camera

pygame.init()
pygame.camera.init()

width = 320
height = 240
# create display based on width and height above
screen = pygame.display.set_mode((width,height),0)

# get camera lists.  assuming only 1 
cam_list = pygame.camera.list_cameras()
# set webcam
webcam = pygame.camera.Camera(cam_list[0],(width,height))
# start the webcam
webcam.start()

while True:
    # get  image
    imagecam = webcam.get_image()
    # blit to screen
    screen.blit(imagecam,(0,0))

    # updates display
    pygame.display.update()

    # check for quit event or key pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            webcam.stop()
            pygame.quit()
            sys.exit()
