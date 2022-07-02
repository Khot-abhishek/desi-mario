from os import walk
import pygame


def import_folder(path):
    surface_list = []
    print('path:',path)
    for _,__,image_files in walk(path):
        print('img:',image_files)
        for image in image_files:
            image_path = f"{path}/{image}"
            img_surface = pygame.image.load(image_path)
            surface_list.append(img_surface)
    print('returning from support:',surface_list)        
    return surface_list
