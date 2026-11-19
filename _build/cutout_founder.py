# Вырез фона у фото основателя → founder.png с прозрачностью
from rembg import remove
from PIL import Image

src = '../assets/img/founder.jpg'
dst = '../assets/img/founder.png'
img = Image.open(src).convert('RGB')
out = remove(img)
out.save(dst)
print('saved', dst, out.size)
