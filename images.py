#!/usr/bin/python
# -*- coding: utf-8 -*-
from os import listdir
from os.path import isfile, isdir, join

# 指定要列出所有檔案的目錄
mypath = "comic/東方三月精（第2部）"

# 取得所有檔案與子目錄名稱
files = listdir(mypath)

i = 1
# 以迴圈處理
for f in files:
  # 產生檔案的絕對路徑
  fullpath = join(mypath, f)
  # 判斷 fullpath 是檔案還是目錄
  if isfile(fullpath):
    print("檔案：", f)
  elif isdir(fullpath):
    
    if len(str(i)) == 1:
        after = "00"
    if len(str(i)) == 2:
        after = "0"

    number = after + str(i)
    i = i + 1

    if len(str(i)) == 1:
        after = "00"
    if len(str(i)) == 2:
        after = "0"

    next_number = after + str(i)

    title = '''title: 東方三月精（第2部) - 第{}話
layout: slides
slide:
  theme: night
  separator: ===
  separator_vertical: ==
  width: 100%
  height: 100%
tags:
  - 漫畫
  - 東方
  - 東方 Prjject
  - 同人
categories:
  - 漫畫
date: 2019-03-01 21:33:03
---
	'''.format(number)

    string = ""

    string = title

    print(title)

    filename = "004" + "-" + number + ".md"

    newpath = "comic/東方三月精（第2部）/"+ f

    files2 = listdir(newpath)
    for f2 in files2:
        value = newpath + "/" + f2
        value = value.replace("comic","\\comic")
        string += "\n" + "\n" + "![東方三月精（第2部）](" + value.replace("/", "\\") + ")" + "\n" + "\n" + "==="

    next_string = "\n" + "\n" + "[(目錄)](/comic/004.html) >> [第 {0} 話](/comic/004-{0}.html)".format(next_number)
    string += next_string
    
    print(string)
    
    with open(filename,"w",encoding="utf-8") as f:
    	f.write(string)

  	#print("目錄：", files2)
    #print("目錄：", "comic/東方三月精（第2部）/"+ f)

    