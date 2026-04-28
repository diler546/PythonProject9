from PIL import Image, ImageFilter

images = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]

try:
    for filename  in images:
        image = Image.open("img/task3/old/"+filename)
        filtered = image.filter(ImageFilter.CONTOUR)
        filtered.save("img/task3/new/"+filename)
except FileNotFoundError:
    print("Файл не найден")