from ensurepip import version
import qrcode 
from PIL import Image

qr=qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
        
    
    ) # this QRCODE give functionality to change boarder and color of qrcode etc etc
qr.add_data("https://github.com/narendragolla1")
qr.make(fit=True)
img=qr.make_image(fill_color='blue',back_color='black')
img.save("github.png")


