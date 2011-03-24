#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__="hara"
__date__ ="$2011/03/23 9:52:16$"

print "Content-Type: text/html"
print

import cgitb
cgitb.enable()

import cgi
import sqlite3
import datetime



print '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"'
print '"http://www.w3.org/TR/html4/loose.dtd"><html><head>'
print '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
#print '<meta http-equiv="Content-Style-Type" content="text/css">'
#print '<meta http-equiv="Content-Script-Type" content="text/javascript">'
#print '<link rel=stylesheet type="text/css" href="default.css"> '
print '<title>地震関連情報掲示板</title></head><body>'
print '<h1>地震関連情報掲示板</h1>'
print '<h4>地震に関連した情報はここで共有しましょう！</h4>'
print '<hr>'

#form
print '<form method="POST" action="post.cgi">'

#list of employee
print '<p>お名前：<select name="tanName">'
print '<option>　</option>'

#conect Database
con = sqlite3.connect("EarthQuakeBBS.sqlite", isolation_level=None)

result = con.cursor()
result.execute(u"select * from tanName")
for item in result:
	print '<option value="%s">%s</option>' % (item[0], item[1].encode('utf_8'))

print '</select>'

#other form items
print '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'
print '<input type="submit" value="  書き込み  "></p>'
print '<p>タイトル：<input type="text" size="60" name="title"></input><br>'
print '本文：<br><textarea name="content" cols="55" rows="10"></textarea></p>'
print '</form>'
print '<hr>'



form = cgi.FieldStorage()

#write
if (form.has_key('tanName') and form.has_key('title') and form.has_key('content')):
	tan = form['tanName'].value
	tit = form['title'].value
	cont = form['content'].value
	now = datetime.datetime.today()
	datestr = '%s/%s/%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)#today's date
	sql = u'insert into kakikomi (tanName, content, datetime, title) values (%s, "%s", "%s", "%s")' % (tan, str(cont).encode('utf-8'), str(datestr), str(tit))
	print sql
	con.execute(sql)



print '<br><br>'
result = con.cursor()
result.execute(u"select * from kakikomi order by id desc limit 10")
for row in result:
	crst = con.cursor()
	prg = u'select name from tanName where id = "%s"' % row[1]
	crst.execute(prg)
	for item in crst:
		nameStr = item[0].encode('utf-8')
	
	print '<br><p>■お名前：%s　　　■書き込み日時：%s' % (nameStr,row[3].encode('utf-8'))
	print '<br><b>　　☆%s</b></p>' % row[4].encode('utf-8')#title
	print '<p>%s</p>' % row[2].encode('utf-8')#content


	#print row[3].encode('utf-8')#datetime

	print '<br><hr>'



print '</body></html>'