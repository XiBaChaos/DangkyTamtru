import pyqrcode
import pandas as pd

# Mã QR cần giải mã
qr_code_data = "QR code data here"

# Giải mã mã QR
qr_code = pyqrcode.create(qr_code_data)
qr_code.png("qr_code.png", scale=6)

# Đọc dữ liệu từ file ảnh QR
from pyzbar.pyzbar import decode
from PIL import Image

qr_data = decode(Image.open('qr_code.png'))
qr_text = qr_data[0][0].decode('utf-8')

# Ghi dữ liệu vào file Excel
data = [[qr_text]]
df = pd.DataFrame(data, columns=["QR code"])
df.to_excel("qr_code.xlsx", index=False)
