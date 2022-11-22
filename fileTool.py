#!/usr/bin/python
# -*- coding: utf-8 -*-
# 遍历所有文件夹，将指定格式文件，批量另存为word  
import os
import re
import sys
import docx

arrs = []
def writeIn(res):
    doc = docx.Document()
    # 存在该目录就移除
    if os.path.exists('content.docx'):
       path = '/Users/mark/content.docx'
       os.remove(path)
    doc.add_paragraph(res)
    doc.save('content.docx')
    print("写入完成")  

def readFile(path):
    with open(path, mode='r', encoding='utf-8') as f:
    # seek()移动光标至指定位置
        f.seek(0)
    # read()读取整个文件，将文件内容放到一个字符串变量中，文件大于可用内存时不适用
        res = f.read()
        print("开始写入内容...")  
        arrs.append(res);

def all_path(dirname):
    tab = input('请输入要打印的文件后缀: ')
    print("文件后缀:", tab)
    for maindir, subdir, file_name_list in os.walk(dirname):
        # print("1主目录:", maindir) #当前主目录
        # print("2主目录下所有目录:", subdir) #当前主目录下的所有目录
        # print("3下的所有文件:", file_name_list) #当前主目录下的所有文件
        for filename in file_name_list:
            apath = os.path.join(maindir, filename)#合并成一个完整路径
            portion = os.path.splitext(apath) #分离文件名和扩展名
            # print("portion:", portion)  
            ext = portion[1]  # 获取文件后缀 [0]获取的是除了文件名以外的内容
            # print("4扩展名:", ext)  
            if ext == tab:
                readFile(apath)

dirname = input('请输入要遍历的文件夹路径: ')
all_path(dirname)
writeIn(''.join(arrs))