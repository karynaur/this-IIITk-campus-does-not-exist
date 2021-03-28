import glob
import os

images=glob.glob("images/*.png")

for i,j in enumerate(images):
   os.rename(j,'im'+str(i)+'.png')


