from PIL import Image

image = Image.open('monro.jpg')
print(image.mode)
red_channel, green_channel, blue_channel = image.split()
red_channel.save('red_channel.jpg')
green_channel.save('green_channel.jpg')
blue_channel.save('blue_channel.jpg')

