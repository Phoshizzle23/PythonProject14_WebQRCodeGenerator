# QR Code Project
import qrcode

# Text or data to be encoded in the QR Code
data = "Hello, QR Code!"

# Create an instance of the QRCode class
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

# Add data to the QR Code
qr.add_data(data)

# Generate the QR Code
qr.make(fit=True)

# Create an image from the QR Code
qr_image = qr.make_image(fill_color="black", back_color="white")

# Save the QR Code image
qr_image.save("qrcode.png")