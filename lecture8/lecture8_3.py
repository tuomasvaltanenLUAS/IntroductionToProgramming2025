# install Pillow instead of PIL
from PIL import Image, ImageDraw

# create a mew image
# for colors, search for color picker in Google to use the built-in tool
img = Image.new('RGB', (500, 300), (119, 142, 168))

# create a new drawing object
draw = ImageDraw.Draw(img)

# "draw" some text in the picture
# in mathematics we are used to start drawing from (0, 0)
# from bottom left, but in computer graphics, 0, 0 is TOP LEFT
# e.g. 100, 200 means literally:
# 100 pixels to the right, 200 pixels down
# see: https://www.plus2net.com/python/images/pil-text-anchor.jpg
draw.text((10, 10), "Hello world!", fill=(255, 255, 0))


# in ellipse on similar shapes, we have two sets of coordinates
# e.g. here 100, 100 and 200, 200
# xy = 100, 100 is starting point
# and 200, 200 is the bottom right
# means the ellipse size is 100 x 100 (200 - 100 = 100)
draw.ellipse((100, 100, 200, 200), fill=(208, 141, 240), outline=(0, 0, 0))

img.save("pillow_test.png")