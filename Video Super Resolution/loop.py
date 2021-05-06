#Super resolution on a video file

from ISR.models import RDN, RRDN
import numpy as np
from PIL import Image
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

directory = './Frames/'

import re

files = os.listdir(directory)

#print(files)

files.sort(key=lambda f: int(re.sub('\D', '', f)))

#processing frames with ascending order name i.e. frame0, frame1, frame2 etc.

#print(files)

for filename in files:

    #sorted_images = sorted(filename, key=natural_sort_key)

    if filename.endswith(".jpg"):

        img = Image.open(directory + filename)

        lr_img = np.array(img)

        #model = RDN(weights='psnr-small')

        model = RRDN(weights='gans')

        sr_img = model.predict(lr_img)
        sr_img = Image.fromarray(sr_img)

        sr_img.save('Upscaled/' + filename)

        print(filename)





