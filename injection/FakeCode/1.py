from Generation_Of_Images import Generate_Images, Show_Image , Extra

IMGS = Generate_Images(prompt="woulverine")

print(IMGS)

IMGS_TO_SHOW = Show_Image(IMGS)

IMGS_TO_SHOW.open(0)

IMGS_TO_SHOW.open(1)

IMGS_TO_SHOW.close(0)

IMGS_TO_SHOW.close(1)