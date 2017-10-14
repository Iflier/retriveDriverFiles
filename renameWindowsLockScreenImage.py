# -*- coding: utf-8 -*-
"""
Dec: 重命名来自于Windows锁屏的无后缀名的文件为.jpg
使用前找到无后缀的锁屏图片，并且把它们复制到glob.glob("  ")参数中指定的路径下，该脚本会把它们重命名后的文件放到这个脚本所在的目录下
Created on : 2017.10.11
Author: Iflier
"""
print(__doc__)

import os
import glob

for i, fileNoSuffix in enumerate(glob.glob("x:\\xxxxx\\PIC\\*"), 1):
    print(fileNoSuffix)
    os.rename(fileNoSuffix, str(i) + ".jpg")
print("Done.")
