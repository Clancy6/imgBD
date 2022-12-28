# -*- coding: utf-8 -*-
import os
import sys
import imagesize
import shutil
import urllib.parse


"""
pip install pytest-shutil
pip install imagesize
"""

def fread(f):#逐行读取文件
    with open(f, encoding='utf-8') as file_obj:
        contents = file_obj.read()
    return(contents.split("\n"))

def get_path_file(files_path):
    data = []
    for root, dirs, files in os.walk(files_path, topdown=False):
        for name in files:
            f_p = os.path.join(root, name).replace("\\", "/")
            data.append(f_p)
    return data

def getImg(path):#网上抄的
    Type = ['jpg','jieg','png','bmp','gif','webp','JPG','JPEG','PNG','BMP','GIF','WEBP','Gif']
    # 返回指定路径的文件夹名称
    dirs = os.listdir(path)
    # 循环遍历该目录下的照片
    for dir in dirs:
        # 拼接字符串
        pa = path+dir
        # 判断是否为照片
        if not os.path.isdir(pa):
            for imgType in Type:
                if(os.path.splitext(os.path.basename(pa))[-1][1:] == imgType):
                    # 使用生成器循环输出
                    yield pa

if __name__ == '__main__':
    ListFile = sys.argv[1]
    for path_i in range(len(fread(ListFile))):
        with open(str(path_i+1)+'.html', 'w') as f:
            f.write("")
    HTML = """
<!DOCTYPE html>
<meta name="viewport" content="width=device-width,initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no"/>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>List of Images</title>
</head>
<style type="text/css">
        @font-face {
    font-family:CaviarDreams;
    src:url("https://Clancy6.github.io/imgDB/font/CaviarDreams-1.ttf");
	}

	.main1{
	    font-family: CaviarDreams
	}
</style>
    <body>
        <div class="main1">
<!-- $imgPath -->
        </div>
    </body>
</html>
    """
    i=1
    #for path in fread(ListFile):
    for path_i in range(len(fread(ListFile))):
        path = fread(ListFile)[path_i]
        for imgPath in getImg(path):
            w, h = imagesize.get(imgPath)#350,
            h1 = int(350*int(h)/int(w))#保持纵横比缩放
            imgPath = imgPath.replace("\\", "\/")#替换\为/
            #'<a href="%s" target="_blank"><img src="%s" alt="%s" width="150" height="150"></a>\n'%(imgPath, imgPath ,imgPath)
            #img_HTML = '<center><a href="%s" target="_blank"><img src="%s" alt="%s" width="%d" height="%d"></a></center>\n<!-- $imgPath -->'%(imgPath, imgPath ,imgPath, int(w), h1)
            img_HTML = '</br><center><a href="%s" target="_blank"><img src="%s" alt="%s" width="350" ></a>\n<p>%s</p></center>\n<!-- $imgPath -->'%(urllib.parse.quote(imgPath), urllib.parse.quote(imgPath) ,os.path.basename(imgPath),os.path.basename(imgPath))
            HTML = HTML.replace("<!-- $imgPath -->", img_HTML)
            print(i," : \n",HTML,"\n\n")
            i+=1
        with open(str(path_i+1)+'.html', 'a', encoding= "utf-8") as f:
            f.write(HTML)
        print("Successfully.")
