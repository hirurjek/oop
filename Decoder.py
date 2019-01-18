from PIL import Image, ImageDraw

from pyzbar.pyzbar import decode


class Decoder:

    def decodeImage(self, image):
        decoded_list = decode(image)
        return decoded_list

    def search_qr_code(self, image):
        brush = ImageDraw.Draw(image)
        for qrcode in decode(image):
            rect_place = qrcode.rect
            brush.rectangle(
                (
                        (rect_place.left, rect_place.top),
                        (rect_place.left + rect_place.width, rect_place.top + rect_place.height)
                 ),
                outline='#0088ff'
            )

            brush.polygon(qrcode.polygon, outline='#e945ff')

        return image
