import qrcode
def main():
    qr = qrcode.QRCode(version=5,box_size=4,border=5)
    data = "adios!"
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black',back_color='white')
    img.save('qr.jpeg')

main()
