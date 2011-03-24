#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__="hara"
__date__ ="$2011/03/23 9:52:16$"

print "Content-Type: text/html"
print

import cgitb
cgitb.enable()

import cgi
import os
import sqlite3
import datetime
import locale
now = datetime.datetime.today()


print '<h1>地震関連情報掲示板</h1>'
print '<h4>地震に関連した情報はここで共有しましょう！</h4>'

print '<hr>'

print '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"'
print '"http://www.w3.org/TR/html4/loose.dtd"><html><head>'
print '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
print '<meta http-equiv="Content-Style-Type" content="text/css">'
print '<meta http-equiv="Content-Script-Type" content="text/javascript">'
print '<link rel=stylesheet type="text/css" href="/jishin/default.css"> '
print '<title>地震関連情報掲示板</title></head><body>'

print '<form method="POST" action="EarthQuakeBBS.cgi">'
print '<p>入力者：<select name="tanName">'
print '<option>　</option>'

#conect Database
con = sqlite3.connect("jishinDB.sqlite", isolation_level=None)

#list of employee
result = con.cursor()
result.execute(u"select * from tanName")
for item in result:
	print '<OPTION value="'
	print "%s" % item[0]
	print '">'
	print "%s" % item[1].encode('utf_8') 
	print '</OPTION>'
print '</select>'

#other form items
print '&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp'
print '<input type="submit" value="  書き込み  "></p>'
print '<p>表題：<input type="text" size="60" name="title"></input><br>'
print '本文：<br><textarea name="content" cols="55" rows="10"></textarea></p>'
print '</form>'
print '<hr>'



form = cgi.FieldStorage()

#write
if (form.has_key('tanName') and form.has_key('title') and form.has_key('content')):
	tan = form['tanName'].value
	tit = form['title'].value
	cont = form['content'].value
	datestr = '%s/%s/%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)
	sql = u'insert into kakikomi (tanName, content, datetime, title) values (%s, "%s", "%s", "%s")' % (tan, cont, datestr, tit)
	print sql
	con.execute(sql)


print '<br><br>'
result = con.cursor()
result.execute(u"select * from kakikomi")
for row in result:
	print row


print '</body></html>'