import qrcode

# URL to be encoded in the QR Code
url = "https://www.youtube.com/watch?v=RtZxoGdPSd4"

# Create an instance of the QRCode class
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

# Add the URL to the QR Code
qr.add_data(url)

# Generate the QR Code
qr.make(fit=True)

# Create an image from the QR Code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR Code image
qr_image.save("qrcodeweb1.png")