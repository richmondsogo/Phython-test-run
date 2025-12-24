# This Python code snippet is using the PIL (Python Imaging Library) module to work with images.
# Here's a breakdown of what each part of the code is doing:
from PIL import Image

# img1 = Image.open("Pokedex\pikachu.jpg")

# These lines of code are providing information about the image `img` that has been opened using the
# PIL module:
# print(img)
# print(img.format)
# print(img.size)
# print(img.mode)
# print(dir(img))


# filtered_img = img.convert("L")
# filtered_img.save("grey.png", "png")

# filtered_img.show()

# crooked_filtered_img = filtered_img.rotate(45)
# crooked_filtered_img.save("grey.png", "png")

# new_size = filtered_img.resize((300, 300))
# new_size.save("grey.png", 'png')

# box = (100,100,400,400)
# region = filtered_img.crop(box)
# region.save("grey.png", "png")

# This code snippet is opening an image file named "tv aesthetic painting.JPG" using the PIL module.
# It then resizes the image to fit within a box of maximum size 400x400 while preserving the aspect
# ratio. Finally, it saves the resized image as "4nsq45shed.png" in PNG format.
img2 = Image.open('./tv aesthetic painting.JPG')
img2.thumbnail((400, 400))
img2.save("4nsq45shed.png", "png")


# print(img2.size)
# The code snippet `a,b = img2.size` is unpacking the size of the image `img2` into two variables `a`
# and `b`. This means that `a` will store the width of the image and `b` will store the height of the
# image.
# a,b = img2.size

# The code `changed_img = img2.resize((a,b))` is resizing the image `img2` to the dimensions specified
# by the variables `a` and `b`, which represent the width and height of the original image. 
# changed_img = img2.resize((a,b))
# changed_img.save("Jordan.png")
