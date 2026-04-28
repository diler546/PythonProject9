from PIL import Image

try:
    image = Image.open("img/task2/Img.jpg")
    reduced_image = image.reduce(3)
    reduced_image.show()
    reduced_image.save("img/task2/Img2.jpg")

    flipped_h = image.transpose(Image.FLIP_LEFT_RIGHT)
    flipped_v = image.transpose(Image.FLIP_TOP_BOTTOM)
    flipped_h.show()
    flipped_v.show()
    flipped_h.save("img/task2/Img3.jpg")
    flipped_v.save("img/task2/Img4.jpg")
except FileNotFoundError:
    print("Файл не найден")
