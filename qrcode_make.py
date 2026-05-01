import qrcode

url = "http://10.182.89.22:5000"

img = qrcode.make(url)

img.save("my_website_qrcode.png")

print("QR Code 已經產生完成！")