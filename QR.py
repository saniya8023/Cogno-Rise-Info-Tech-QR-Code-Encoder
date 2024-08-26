import qrcode
import cv2

def create_qr_code(data, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(filename)
    print(f"QR Code created and saved as '{filename}'.")

def decode_qr_code(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, vertices_array, _ = detector.detectAndDecode(img)
    if vertices_array is not None:
        print(f"Decoded data: {data}")
    else:
        print("QR Code not detected")

def main():
    choice = input("Do you want to (E)ncode or (D)ecode a QR code? ")
    if choice.lower() == 'e':
        data = input("Enter the data/URL to encode: ")
        create_qr_code(data)
    elif choice.lower() == 'd':
        img_path = input("Enter the path to the QR code image: ")
        decode_qr_code(img_path)
    else:
        print("Invalid choice. Please select either 'E' or 'D'.")

if __name__ == "__main__":
    main()
