import sys
import numpy as np
from PIL import Image

   
def MyFilter(Box):
     temp_arr=[0 for i in range(9)]
     counter = 0;
     for v in range (3):
          for h in  range (3):
               temp_arr[counter]=Box[v][h]
               counter = counter + 1
     temp_arr=np.sort( temp_arr)
     return  temp_arr[4]
     

img = Image.open(sys.argv[1])
img1= np.array(img,dtype=np.uint8)
Matrix = [[0 for x in range(img.size[0])] for y in range(img.size[1])] 


for i in range(img.size[0]-2): 
    for y in range(img.size[1]-2):
          local = img1[i:i+3, y:y+3]
          Matrix[i+1][y+1]=MyFilter(local)

#finish part
Image = np.asarray(Matrix,dtype=np.uint8)
Image.fromarray(Image,'L').save('clearImage.png','PNG')
