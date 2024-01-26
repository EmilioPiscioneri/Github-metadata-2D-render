# Module not in same directory
import sys
sys.path.append("/python-programming/Github metadata no 2D render/")
thisFolder = "/python-programming/Github metadata 2D render/"
from githubInterface import githubReceiver
import requests
import os
from PIL import Image
import pygame
# open the font files

receiver = githubReceiver()

# Example file showing a basic pygame "game loop"
import pygame


avatarPadding = (10,0) # How much padding there is between avatar and text
aboutTextPadding = (0,10) # How much padding there is between title and about text
titleFontSize = 96
aboutFontSize = 32
#Hard code the github values for now
author = "nodejs"
repo = "node"
githubAboutData = receiver.getAbout(author,repo) # Get github data as string
#print(githubAboutData) #print the data
avatar = receiver.getOrganisationPhoto("nodejs") # get avatar url
avatarFileResponse = requests.get(avatar)
avatarFileResponse.close() # close the connnection to server
avatarFileLocalPath = thisFolder+"/avatar"
# if(os.path.exists(avatarFileLocalPath)):
#Doesn't matter if file exists will create anyway
avatarFileOnDisk = open(avatarFileLocalPath,"+bw") # open file for writing in binary mode
avatarFileOnDisk.write(avatarFileResponse.content)
avatarPilImage = Image.open(avatarFileOnDisk) # load the image on the PIL module
avatarFormat = avatarPilImage.format.lower() # Get format in lowercase

avatarPilImage.close() # close the file

newAvatarFilePath = avatarFileLocalPath+"."+avatarFormat

if os.path.exists(newAvatarFilePath):
    os.remove(newAvatarFilePath)

os.rename(avatarFileLocalPath, newAvatarFilePath) # change file name to match file type 

avatarFileOnDisk = open(newAvatarFilePath,"rb") # open for reading in binary
avatarImage = pygame.image.load(avatarFileOnDisk) # load avatar for pygame 

avatarImageDimensions = (avatarImage.get_size()[0],0)

titleTextLocation = avatarImageDimensions + avatarPadding # pre-compute
titleTextStr = author+"/"+repo


#print(avatarImage)

avatarFileOnDisk.close() # close the file

# avatarFileOnDisk = open(avatarFileLocalPath, "+br") # open file for reading in binary mode
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Got quit event")
            running = False
            

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((19,19,20))

    # RENDER YOUR GAME HERE

    # key = pygame.key.get_pressed()
    
    
    #Reder text
    titleText = pygame.font.SysFont("Arial Nova",titleFontSize) # create text object
    titleTextSurace = titleText.render(titleTextStr,True,"white")
    aboutText = pygame.font.SysFont("Arial Nova",aboutFontSize)
    aboutTextSurface = aboutText.render(githubAboutData,True,"white")
    aboutTextLocation = (titleTextLocation[0], titleTextLocation[1] + titleTextSurace.get_size()[1] + aboutTextPadding[1])
    

    # render to screen
    screen.blit(avatarImage, (0,0)) # Render the avatar image
    screen.blit(titleTextSurace, titleTextLocation)
    screen.blit(aboutTextSurface, aboutTextLocation)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(75)  # limits FPS 

print("closing")
pygame.quit()

#cleanup

#close font files
