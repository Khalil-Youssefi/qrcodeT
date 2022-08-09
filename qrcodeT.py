__version__ = 'v1.0.2'
import qrcode
import numpy as np

def qrcode2text(img):
    bindata = np.array(img)[::10,::10] + 0
    if bindata.shape[0] % 2 != 0:
        bindata.resize((bindata.shape[0]+1,bindata.shape[1]),refcheck=False)
    twolines_compress = bindata[::2,:] + 2*bindata[1::2,:]
    chars = np.zeros(twolines_compress.shape)
    char_table = [' ','▀','▄','█']
    chars[twolines_compress==0] = ord(char_table[0])
    chars[twolines_compress==1] = ord(char_table[1])
    chars[twolines_compress==2] = ord(char_table[2])
    chars[twolines_compress==3] = ord(char_table[3])
    return chars

def print_qrcode_asText(chars):
    for i in range(chars.shape[0]):
        for j in range(chars.shape[1]):
            print(chr(int(chars[i,j])),end='')
        print()

def qrcode_asText(img):
    print_qrcode_asText(qrcode2text(img))

def qrcodeT(txt):
    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
    )
    qr.add_data(txt)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    qrcode_asText(img)
