from io import BytesIO
from PIL import Image


def read_files(file) -> Image.Image:
    image = Image.open(BytesIO(file)).resize((260, 260), Image.NEAREST).convert("RGB")
    return image