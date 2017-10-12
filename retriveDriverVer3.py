# -*- coding: utf-8 -*-
"""
Dec:修正版本2中漏检目录下包含文件和目录的错误
Created on : 2017.10.12
Author: Iflier
"""
print(__doc__)

import os
import time
import os.path
import argparse

ap = argparse.ArgumentParser()
ap.add_argument('-d', '--dirpath', help="Specifi the target driver",
                default="G", type=str, required=False)
ap.add_argument('-e', '--extend', help="file extend, start with .",
                default=None, type=str)
args = vars(ap.parse_args())

# 把指定的盘符连接成为根目录
root = args['dirpath'].upper() + ":" + os.sep
queryExtend = True if args.get("extend", None) else False

i = 0

start = time.time()

for dirpath, dirnames, filenames in os.walk(root):
    for filename in filenames:
        if all(os.path.splitext(filename)):
            filePath = os.path.join(os.path.join(dirpath, filename))
            if os.path.isfile(filePath):
                if queryExtend:
                    if os.path.splitext(filename)[-1] == args['extend']:
                        print(filePath)
                        i += 1
                else:
                    print(filePath)
                    i += 1

print("指定的盘符：{0}，共包含{1:^+15,d}个文件".format(args['dirpath'].upper(), i))
print("Time of used: {0:^10,.3f} s".format(time.time() - start))
