
#coding=utf-8

from bs4 import BeautifulSoup
import requests
songlist = []
artistlist=[]
header_info =  {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'ahtena_is_show=true; _unsign_token=746be7ef88681900f9d7cf070c8700c8; bdshare_firstime=1460471307481; cna=4WmOD5po5DkCAT2tKQi2AMGX; gid=146313980795253; ahtena_is_show=false; t_sign_auth=1; _xiamitoken=d244b94e94980a0d90114343d0323dbc; CNZZDATA921634=cnzz_eid%3D1642382752-1460105591-%26ntime%3D1463494773; CNZZDATA2629111=cnzz_eid%3D2045210303-1460104194-%26ntime%3D1463494145; l=Apubr8-4hSbX2/1aE-Gw8ZiOq/UFcK9y',
    'Host':'www.xiami.com',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
}
for i in range(1,81):
    myurl = 'http://www.xiami.com/space/lib-song/u/6170942/page/'+'%s'%i
    r = requests.get(myurl,headers = header_info)

    soup = BeautifulSoup(r.text,"html.parser")

    songinfo = soup.find_all('td',class_="song_name")#.find('a')
    #print songinfo[0].find('a').get('title')
    for song in songinfo:
        songlist.append(song.find('a').get('title'))
        artistlist.append(song.find(class_="artist_name").get('title'))
    print ("page %d clear")%i

list = ''
num = 0
for i in range(0,len(songlist)):
    songunit = artistlist[i]+' - '+songlist[i]
    filenameNode = '<FileName>'+songunit+'</FileName>\n'
    fileNode = '<File>\n'+filenameNode+'</File>\n'
    list += fileNode
    num = num + 1
    print ('%d/1982')%num
listname = 'xiamilove'
list = '<?xml version="1.0" ?>\n<List ListName="' + listname + '">\n'+list+'</List>'
newlist = list.encode('utf-8')
file = open('xiamilove.kgl','w')
file.write(newlist)
file.close()
print 'Mission Complete'