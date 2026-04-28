from PIL import Image

try:
    image = Image.open("img/task1/Img1.jpg")
except FileNotFoundError:
    print("Файл не найден")
    exit()
image.show()
print("Информация об изображении:")
print(f"Размер: {image.width} px X {image.height} px")
print(f"Формат: {image.format}")
print(f"Цветовая модель: {image.mode}")