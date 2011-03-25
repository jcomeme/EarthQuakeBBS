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

#read form data
form = cgi.FieldStorage()


print '<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"'
print '"http://www.w3.org/TR/html4/loose.dtd"><html><head>'

if (form.has_key('tanName') and form.has_key('title') and form.has_key('content')):
	print '<META HTTP-EQUIV="Refresh" CONTENT="2; URL=EarthQuakeBBS.cgi">'

print '<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">'
print '<meta http-equiv="Content-Style-Type" content="text/css">'
print '<link rel=stylesheet type="text/css" href="default.css"> '
print '<title>地震関連情報掲示板</title></head><body>'
print '<h1>地震関連情報掲示板</h1>'



#write
if (form.has_key('tanName') and form.has_key('title') and form.has_key('content')):
	#conect Database
	con = sqlite3.connect("EarthQuakeBBS.sqlite", isolation_level=None)
	tan = form['tanName'].value
	tit = form['title'].value
	cont = form['content'].value
	now = datetime.datetime.today()
	datestr = "%02d/%02d/%02d %02d:%02d:%02d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)#today's date
	sql = 'insert into kakikomi (tanName, content, datetime, title) values (%s, "%s", "%s", "%s")' % (tan, cont, datestr, tit)
	con.execute(sql)
	
	print '<h4>下記の内容で書き込みました！</h4>'
	print '<hr>'
	print '<div class="space01">'
	print '<br><p>■お名前：%s　　　■書き込み日時：%s' % (tan,datestr)
	print '<div class="title">%s</div>' % tit
	print '<div class="txtbox"><p>%s</p></div>' % cont
	print '</div><br><hr><br>'
	
else:
	print '<h4>全部の項目を記入してください！</h4>'
	#pending
	
	print '<hr>'

#form
print '<form action="EarthQuakeBBS.cgi">'
print '<input type="submit" value="  　戻る　  "></form>'


print '</body></html>'