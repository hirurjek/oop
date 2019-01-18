from PIL import Image, ImageDraw

from pyzbar.pyzbar import decode

if __name__ == '__main__':

    image = Image.open('../src/qrcode_rotated.png').convert('RGB')
    draw = ImageDraw.Draw(image)
    for barcode in decode(image):
        print(barcode.data.decode('utf-8'))
        rect = barcode.rect
        draw.rectangle(
            (
                (rect.left, rect.top),
                (rect.left + rect.width, rect.top + rect.height)
            ),
            outline='#0080ff'
        )

        draw.polygon(barcode.polygon, outline='#e945ff')

    image.save('bounding_box_and_polygon.png')





