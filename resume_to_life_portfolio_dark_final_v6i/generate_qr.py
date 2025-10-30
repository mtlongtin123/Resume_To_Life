# Generate a QR code for your live site URL.
# Usage:
#   pip install qrcode[pil]
#   python generate_qr.py "https://your-live-domain.tld"
import sys
import qrcode

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_qr.py <url>")
        sys.exit(1)
    url = sys.argv[1].strip()
    img = qrcode.make(url)
    img.save("assets/qr.png")
    print("Saved QR to assets/qr.png")

if __name__ == "__main__":
    main()
