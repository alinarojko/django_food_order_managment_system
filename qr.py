import qrcode
# import pillow through pip install

image = qrcode.make("httt://127.0.0.1:8000")
image.save("qr.png")