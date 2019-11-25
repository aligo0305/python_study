import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="https://ssl.pstatic.net/tveta/libs/1265/1265319/3d4e5ffe2dfe434a743a_20191115144134000.jpg"
htmlURL ="https://tvetamovie.pstatic.net/libs/1263/1263726/0124377d0004b9f93a9a_20191021132502714.mp4-pBASE-v0-f93628-20191021133301416.mp4"

savePath1 ="/Users/ohjune-macpro/Documents/section2/과제1.jpg"
savePath2 ="/Users/ohjune-macpro/Documents/section2/과제1.mp4"

f = dw.urlopen(imgUrl).read()
f2 = dw.urlopen(htmlURL).read()

saveFile1 = open(savePath1,'wb') # w : write , r : read , a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)



print("다운로드 완료!")
