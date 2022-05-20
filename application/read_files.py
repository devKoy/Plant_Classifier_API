from io import BytesIO
from PIL import Image


def read_files(file) -> Image.Image:
    image = Image.open(BytesIO(file)).resize((256, 256), Image.NEAREST).convert("RGB")
    return image