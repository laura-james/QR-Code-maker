#https://www.codedex.io/projects/generate-a-qr-code-with-python
import qrcode


website_link = input("What website would you like to turn into a QR code?")

qr = qrcode.QRCode(version = 5, box_size = 5, border = 0)
qr.add_data(website_link)
qr.make()

img = qr.make_image(fill_color="orange", back_color="white")#colours dont seem to work
img.save('QR_code.png')
