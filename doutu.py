import re
import requests
import pymysql

# 使用pymysql   保存数据到数据库
# 在数据库内 创建实例
db = pymysql.connect(host='192.168.1.103',port=3306,user='pythonuser',passwd='123456',db='pythondb',charset='utf8')
# 创建游标
cursor = db.cursor()
# cursor.execute('select * from images')
# cursor.execute("(insert into images('name','imageurl')values('{}','{}'))".format(imagename,imageurl))
# print(cursor.fetchall())




# 获取图表列表
def getImageList(page):
    html= requests.get('https://www.doutula.com/photo/list/?page=%d' %page).text
    # print(html)
    # 正则表达式运用 * 是取 0 至 无限长度  . 是任意字符  分组 ()
    reg = r'data-original="(.*?)".*?alt="(.*?)"'
    # compliie 增加效率 S  多行匹配
    reg1 = re.compile(reg,re.S)
    imageList = re.findall(reg1,html)

    for image in imageList:
    	# print(image[0])
    	imagename = image[1]
    	imageurl = image[0]
    	cursor.execute("insert into images(name,imageurl)values('{}','{}')".format(imagename,imageurl))
    	print('正在保存 %s'%imagename)
    	db.commit()

# range范围   >=1 and <1001
for i in range(1,1001):
	print('正在保存第%d页' %i)
	getImageList(i)
 