import glob
from PIL import Image

cats = glob.glob('cats/*.webp')

for cat in cats:
    img = Image.open(cat)
    img123 = cat.replace("cats\\cat", "").replace(".webp", "")
    img.save(f'newcat/cat{img123}.jpg', 'jpg')