from PIL import Image

image_1 = Image.open(r'program lang cloud.png')
im_1 = image_1.convert('RGB')
im_1.save(r'program lang cloud.pdf')