import qrcode
import zbarlight
from PIL import Image

# Tạo mã QR
img = qrcode.make('Hello, Py!')

# Lưu mã QR vào file
img.save('qr.png')

# Đọc thông tin từ file ảnh chứa mã QR
with open('qr.png', 'rb') as f:
    qr = Image.open(f)
    qr.load()
    codes = zbarlight.scan_codes('qrcode', qr)
    if codes:
        print('QR code content:', codes[0].decode('utf-8'))
    else:
        print('No QR code found.')
