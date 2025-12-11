from PIL import Image, ImageFilter

img = Image.open("Pokedex\pikachu.jpg")

print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)

filtered_img.save("blur.png", "png")
