import sys
from PIL import Image

img=Image.open(r'C:\Users\TcidCratman\Desktop\out.png') 

img = img.resize((200, 100), Image.NEAREST)
img.save(r'C:\Users\TcidCratman\Desktop\out_1.png')
