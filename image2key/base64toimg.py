# pip install pillow
import base64
import io

import numpy as np
from PIL import Image
import cv2


# Take in base64 string and return cv image
def stringToRGB(base64_string):
    # b64_bytes = base64.b64encode(base64_string)
    # b64_string = b64_bytes.decode()
    #
    # # reconstruct image as an numpy array
    # return cv2.imread(io.BytesIO(base64.b64decode(b64_string)))
    # imgdata = base64.b64decode(str(base64_string))
    # image = Image.open(io.BytesIO(imgdata))
    # return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)
    from PIL import Image
    from base64 import decodebytes

    im = Image.open(io.BytesIO(base64.b64decode(base64_string)))
    return im
