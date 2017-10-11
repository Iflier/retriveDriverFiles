# -*- coding: utf-8 -*-
"""
Dec:检索出指定盘符下的所有的文件
Created on : 2017010.11
Author: Iflier
"""
print(__doc__)

import os
import os.path
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--dirpath', help="Specifi the target driver", default="G")
args = vars(ap.parse_args())

# 把指定的盘符连接成为根目录
root = args['dirpath'].upper() + ":" + os.sep

i = 0

for dirpath, dirnames, filenames in os.walk(root, topdown=True):
    for filename in filenames:
        if os.path.isfile(os.path.join(root, filename)):
            print(os.path.join(root, filename))
            i += 1
        if not any(dirnames):
            for filename2 in filenames:
                if all(os.path.splitext(filename2)):
                    print(os.path.join(dirpath, filename2))
                    i += 1

print("指定的盘符：{0}，共包含{1:^+15,d}个文件".format(args['dirpath'].upper(), i))
