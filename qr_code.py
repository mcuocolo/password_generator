import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import VerticalGradiantColorMask

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=5,
)
qr.add_data('uenmh2nsu2xy')
img = qr.make_image(fill_color="#0080ff", back_color="white")
# type(img)  # qrcode.image.pil.PilImage
img.save("qr-images/box_size20_border10.png")

# img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
# img_1.save("qr-images/rounded.png")
# img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=VerticalGradiantColorMask())
# img_2.save("qr-images/gradient.png")
# img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path="src/naruto.png")
# img_1.save("qr-images/naruto.png")