from PIL import Image
import os

image = Image.open('monro.jpg')
print(image.mode)
red_channel, green_channel, blue_channel = image.split()
red_channel.save('red_channel.jpg')
green_channel.save('green_channel.jpg')
blue_channel.save('blue_channel.jpg')
os.remove('monro.jpg')
new_image = Image.merge('RGB', (red_channel, green_channel, blue_channel))
new_image.save('monro.jpg')

