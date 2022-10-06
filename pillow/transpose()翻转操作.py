'''
transpose参数method: Image.Transpose.FLIP_LEFT_RIGHT:左右水平翻转;
            Image.Transpose.FLIP_TOP_BOTTOM:上下垂直翻转;
            Image.Transpose.ROTATE_90:图像旋转 90 度;
            Image.Transpose.ROTATE_180:图像旋转 180 度;
            Image.Transpose.ROTATE_270:图像旋转 270 度;
            Image.Transpose.TRANSPOSE:图像转置;
            Image.Transpose.TRANSVERSE:图像横向翻转.
'''
from PIL import Image
im = Image.open(r'pillow\image\fly.png')
im_transpose = im.transpose(Image.Transpose.TRANSPOSE)
im_transpose.show()