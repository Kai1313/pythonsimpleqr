import qrcode
import datetime

def qrgenerator(typed, qr_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add data to the QR code
    data = typed
    print(typed)
    qr.add_data(data)
    # Generate the QR code
    qr.make(fit=True)
    # Create an image from the QR code
    qr_image = qr.make_image(fill="black", back_color="white")
    qr_image.save(qr_name)