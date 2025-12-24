# This Python script is a JPG to PNG converter. Here's a breakdown of what the script does:
import sys
import os
from PIL import Image

# This part of the script is checking the number of command-line arguments passed when running the
# script. If the number of arguments is not equal to 3, it exits the script and displays an error
# message indicating the correct usage of the script.
if len(sys.argv) != 3:
    sys.exit(
        "Error: Something went wrong | Usage: python3 JPGtoPNGconverter.py <source_fwhaolder> <destination_folder>"
    )

else:
    script_name, arg1, arg2 = sys.argv
    source_folder = arg1
    dest_folder = arg2


# This part of the script is checking if the destination folder specified by the user exists. If the
# destination folder does not exist, it creates the folder using `os.mkdir(dest_folder)`. This ensures
# that the script has a valid destination folder to save the converted PNG images.
if not os.path.isdir(dest_folder):
    os.mkdir(dest_folder)


# This part of the script is iterating over the files in the source folder specified by the user. For
# each file, it checks if the file has a ".jpg" or ".jpeg" extension using
# `file.lower().endswith((".jpg", ".jpeg"))`. If the file is a JPG or JPEG image, it constructs the
# source path by joining the source folder path with the file name.
for file in os.listdir(source_folder):
    if file.lower().endswith((".jpg", ".jpeg")):
        src_path = os.path.join(source_folder, file)
        converted_img = file.lower().replace(".jpg", ".png").replace(".jpeg", ".png")
        dest_path = os.path.join(dest_folder, converted_img)
        with Image.open(src_path) as img:
            img.convert("RGB").save(dest_path)
