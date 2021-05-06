#Super resolution on a single image

from ISR.models import RDN, RRDN
import numpy as np
from PIL import Image
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' #ignores some of the errors we don't care about

#model = RRDN(weights='gans')

img = Image.open('Frames/frame0.jpg')

lr_img = np.array(img)

#model = RDN(weights='psnr-small') #there are other models also please refer to ISR documentation for more, I am using GAN bases approach for the super resolution

model = RRDN(weights='gans')

sr_img = model.predict(lr_img)
sr_img = Image.fromarray(sr_img)

sr_img.save('Upscaled/frame0.jpg')


