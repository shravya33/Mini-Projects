import qrcode
from PIL import Image
import os

def generate_qr(data, filename="qrcode.png", fill_color="black", back_color="white", size=10):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    print("File will be saved to:", os.getcwd())

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

# Example usage
if __name__ == "__main__":
    data_to_encode = input("Enter text or URL to encode: ")
    output_file = input("Enter output filename (default: qrcode.png): ") or "qrcode.png"
    
    generate_qr(data_to_encode, filename=output_file)