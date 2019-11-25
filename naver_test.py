import sys
import io
import urllib.request as dw

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

imgUrl ="https://land.naver.com/article/divisionInfo.nhn?rletTypeCd=A01&tradeTypeCd=all&hscpTypeCd=&cortarNo=1171000000&articleOrderCode=(id:asideRltrMbrProfileInfoLayer)"

savePath1 ="/Users/ohjune-macpro/Documents/section2/네이버 테스트.txt"


f = dw.urlopen(imgUrl).read()

saveFile1 = open(savePath1,'wb') # w : write , r : read , a : add
saveFile1.write(f)
saveFile1.close()

with open(savePath2,'wb') as saveFile2:
    saveFile2.write(f2)



print("다운로드 완료!")
