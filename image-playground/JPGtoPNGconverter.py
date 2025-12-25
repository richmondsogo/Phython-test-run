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

# This block of code is responsible for iterating through the files in the source folder specified by
# the user. For each file, it checks if the file has a ".jpg" or ".jpeg" extension. If the file is a
# JPG or JPEG image, it opens the image using the PIL library, converts it to RGB format, and then
# saves the converted image as a PNG file in the destination folder.
num_processed_images = 0

for file in os.listdir(source_folder):
    root, ext = os.path.splitext(file)

    if ext.lower() in [".jpg", ".jpeg"]:
        src_path = os.path.join(source_folder, file)
        converted_img = root + ".png"
        dest_path = os.path.join(dest_folder, converted_img)

        with Image.open(src_path) as img:
            img.convert("RGB").save(dest_path)
        num_processed_images += 1

print(f"Total files converted: {num_processed_images}")
