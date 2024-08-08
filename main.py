import qrcode
import pyshorteners
import sys

args = sys.argv


def generate_qr(link: str, file_name="qr.png") -> None:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=2,
    )
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    print("QR created successfully")
    img.show()


def shorten(long_link) -> str:
    s = pyshorteners.Shortener()
    return s.tinyurl.short(long_link)


if __name__ == "__main__":
    match len(args):
        case 2:
            exit("Too few command line arguments")
        case 3:
            link = args[2]
            if args[1].lower() in ["qr", "shorten"]:
                if args[1].lower() == "qr":
                    generate_qr(link)
                else:
                    print(shorten(link))
            else:
                exit("Specified command doesn't exist")

        case _:
            exit("Too many command line arguments")
