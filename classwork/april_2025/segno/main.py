import segno
from PIL import Image
# from PIL.ImageOps import scale
from pyzbar.pyzbar import decode


def generate_qr_code(text:str, file_name:str) -> None:
    text = segno.make(text)
    text.save(file_name, scale=10)
    print("QR Code generated successfully.")


def scan_qr_code(file_name) -> None:
    img = Image.open(file_name)
    print(img)
    decoded_txt = decode(img)
    list(decoded_txt)

    for obj in decoded_txt:
        data = obj.data.decode("utf-8")
        return data


if __name__ == "__main__":
    menu_texts = [
        "Lafenwa in London",
        "April in semicolon",
        "https://etisiobi.com",
        "https://localhost.com"
    ]

    file_names = [
        "dynamite.png",
        "april.png",
        "etisiobi.png",
        "localhost.png",
    ]

    # generate_qr_code(menu_text, sys.argv[1])
    for index in range(len(menu_texts)):
        generate_qr_code(menu_texts[index], file_names[index])

    for file_name in file_names:
        print(scan_qr_code(file_name))
