from PIL import Image, ImageFilter

before = Image.open("courtyard.bmp")
after = before.filter(ImageFilter.BoxBlur(100))
after.save("out-100.bmp")