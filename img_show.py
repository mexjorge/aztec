from PIL import Image
imagen_pil = Image.open('sol.jpg')
imagen_pil.rotate(45).show()