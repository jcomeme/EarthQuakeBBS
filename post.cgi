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

#read form data
form = cgi.FieldStorage()

#write
if (form.has_key('tanName') and form.has_key('title') and form.has_key('content')):
	#conect Database
	con = sqlite3.connect("EarthQuakeBBS.sqlite", isolation_level=None)
	tan = form['tanName'].value
	tit = form['title'].value
	cont = form['content'].value
	now = datetime.datetime.today()
	datestr = '%s/%s/%s %s:%s:%s' % (now.year, now.month, now.day, now.hour, now.minute, now.second)#today's date
	sql = 'insert into kakikomi (tanName, content, datetime, title) values (%s, "%s", "%s", "%s")' % (tan, cont, datestr, tit)
	print sql
	con.execute(sql)
	
	print '<h4>下記の内容で書き込みました！</h4>'
	print '<hr>'
	
	#pending
	print '<p>%s, %s, %s, %s</p>' % (tan, cont, datestr, tit)
	
else:
	print '<h4>全部の項目を記入してください！</h4>'
	#pending
	
	print '<hr>'

#form
print '<form action="EarthQuakeBBS.cgi">'
print '<p></p>'
print '<input type="submit" value="  戻る  "></form>'


print '</body></html>'