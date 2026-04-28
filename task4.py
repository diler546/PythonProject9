from PIL import Image, ImageDraw, ImageFont

images = ["Img.jpg", "Img2.jpg"]

try:
    font = ImageFont.truetype("img/task4/CS.otf", size=30)
except OSError:
    font = ImageFont.load_default()

for filename in images:
    try:
        image = Image.open("img/task4/"+filename).convert("RGBA")
    except FileNotFoundError as message:
        print("Файл не найден: ", message)
        exit()

    watermark = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(watermark)

    draw.text((20, 20), "DILER Studio", fill=(255, 255, 255, 128), font=font)

    result = Image.alpha_composite(image, watermark)

    new_filename = filename.split(".")
    new_filename = new_filename[0] + ".png"

    try:
        result.save("img/task4/"+new_filename)
    except FileNotFoundError as message:
        print("Файл не найден: ", message)
        exit()

    result.show()


