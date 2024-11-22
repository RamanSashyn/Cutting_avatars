from PIL import Image

image = Image.open('monro.jpg')
red_channel, green_channel, blue_channel = image.split()

coordinates_red_1 = (50, 0, red_channel.width, red_channel.height)
cropped_red_1 = red_channel.crop(coordinates_red_1)

coordinates_red_2 = (25, 0, red_channel.width - 25, red_channel.height)
cropped_red_2 = red_channel.crop(coordinates_red_2)

image1_red = cropped_red_1
image2_red = cropped_red_2.resize(image1_red.size)
image3_red = Image.blend(image1_red, image2_red, 0.5)

coordinates_blue_1 = (0, 0, blue_channel.width - 50, blue_channel.height)
cropped_blue_1 = blue_channel.crop(coordinates_blue_1)

coordinates_blue_2 = (25, 0, blue_channel.width - 25, blue_channel.height)
cropped_blue_2 = blue_channel.crop(coordinates_blue_2)

image1_blue = cropped_blue_1
image2_blue = cropped_blue_2.resize(image1_blue.size)
image3_blue = Image.blend(image1_blue, image2_blue, 0.5)

coordinates_green = (25, 0, green_channel.width - 25, green_channel.height)
green_channel_cropped = green_channel.crop(coordinates_green)

new_image = Image.merge("RGB", (image3_red, image3_blue, green_channel_cropped))

new_image.save("new_image.jpg")

new_image.thumbnail((80, 80))

new_image.save("avatar.jpg")

