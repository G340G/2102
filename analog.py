from PIL import Image
import numpy as np
import random

def vhs_corrupt():
    img = Image.open("frame.jpg")
    arr = np.array(img)

    # horizontal jitter
    for i in range(0, arr.shape[0], 10):
        shift = random.randint(-10,10)
        arr[i] = np.roll(arr[i], shift, axis=0)

    # color channel shift
    arr[:,:,0] = np.roll(arr[:,:,0], 5, axis=1)

    Image.fromarray(arr).save("corrupted.jpg")
