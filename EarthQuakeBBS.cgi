#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__="hara"
__date__ ="$2011/03/23 9:52:16$"

print "Content-Type: text/html"
print

#import cgitb
#cgitb.enable()

import cgi
import sqlite3
import datetime



print '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"'
print '"http://www.w3.org/TR/html4/loose.dtd"><html><head>'
print '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
print '<meta http-equiv="Content-Style-Type" content="text/css">'
print '<link rel=stylesheet type="text/css" href="default.css"> '
print '<title>地震関連情報掲示板</title></head><body>'


###################
# conect Database #
###################
con = sqlite3.connect("EarthQuakeBBS.sqlite", isolation_level=None)
#count rows
cresult = con.cursor()
cresult.execute("select count(id) from kakikomi")
for citem in cresult:
	countOfRow = citem[0]

###################
# get request     #
###################
form = cgi.FieldStorage()

#get page
if form.has_key('page') :
	page = form['page'].value
else:
	page = 1

if countOfRow // 10 != countOfRow / 10.0:
	numOfPage = countOfRow // 10 + 1
else:
	numOfPage = countOfRow / 10



print '<h1>地震関連情報掲示板</h1>'
print '<h4>地震に関連した情報はここで共有しましょう！</h4>'
print '<hr>'

#form
print '<form method="POST" action="post.cgi">'

#list of employee
print '<p>お名前：<select name="tanName">'
print '<option>　</option>'
result = con.cursor()
result.execute(u"select * from tanName")
for item in result:
	print '<option value="%s">%s</option>' % (item[0], item[1].encode('utf_8'))

print '</select>'

#other form items
print '　　　　　　　　　　　'
print '<input type="submit" value="  書き込み  "></p>'
print '<p>タイトル：<input type="text" size="60" name="title"></input><br>'
print '本文：<br><textarea name="content" cols="55" rows="10"></textarea></p>'
print '</form>'
print '<hr>'


#page number
counter = numOfPage
num = 1
while counter:
	if int(page) == num:
		print '[%s]  ' % (num)
	else:
		print '<a href="EarthQuakeBBS.cgi?page=%s">[%s]</a>  ' % (num, num)
	num = num + 1
	counter = counter - 1
print '<hr>'


#contents
result = con.cursor()
pagecount = ((int(page) - 1) * 10)
listSQL = u"select * from kakikomi order by id desc limit 10 offset %s" % pagecount
result.execute(listSQL)
for row in result:
	crst = con.cursor()
	prg = u'select name from tanName where id = "%s"' % row[1]
	crst.execute(prg)

	for item in crst:
		nameStr = item[0].encode('utf-8')

	print '<div class="space01">'
	print '<br><p>■お名前：%s　　　■書き込み日時：%s' % (nameStr,row[3].encode('utf-8'))
	print '<div class="title">%s</div>' % row[4].encode('utf-8')#title
	print '<div class="txtbox"><p>%s</p></div>' % row[2].encode('utf-8')#content
	print '</div><br><hr><br>'


#page number
counter = numOfPage
num = 1
while counter:
	if int(page) == num:
		print '[%s]  ' % (num)
	else:
		print '<a href="EarthQuakeBBS.cgi?page=%s">[%s]</a>  ' % (num, num)
	num = num + 1
	counter = counter - 1
print '<br>'


print '</body></html>'