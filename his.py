#!/usr/bin/python
#coding: utf-8

import mechanize
from BeautifulSoup import BeautifulSoup
import filecmp
import os
import smtplib
from email.mime.text import MIMEText


#########CONFIG
MATNR = "10XXXXX"
PASSWORT = "supergeheim"
MAIL_FROM = "noten@example.com"
MAIL_TO = "mymail@example.com"
#########/CONFIG


br = mechanize.Browser()
br.open("https://his-www.dv.fh-frankfurt.de")

br.select_form(name="loginform")
br["asdf"] = MATNR
br["fdsa"] = PASSWORT
br.submit()

#########Go to the Notenübersicht
result = br.open("https://his-www.dv.fh-frankfurt.de/qisserver/rds?state=change&type=1&moduleParameter=studyPOSMenu&nextdir=change&next=menu.vm&subdir=applications&xml=menu&purge=y&navigationPosition=functions%2CstudyPOSMenu&breadcrumb=studyPOSMenu&topitem=functions&subitem=studyPOSMenu")

br.follow_link(text="Notenspiegel")
result = br.follow_link(text_regex="Leistungen für Abschluss 19 Bachelor anzeigen")

frontpage = result.read()

#########Do BS's magic
soup = BeautifulSoup(frontpage)

tables = soup.findAll("td", { "class" : "qis_kontoOnTop"})

#########Generate a HTML-conform, nice table for the mail
counter = 0
resultable = ""
for td in tables:
	if(counter == 0):
		resultable += "<tr>"
	resultable += str(td)
	counter += 1
	if(counter > 8):
		resultable += "</tr>"
		counter = 0


#########Write new stuff and compare with old stuff
with open("notentabelletmp", "w") as file:
	file.write(resultable)

notenolddate = filecmp.cmp("notentabelletmp", "notentabelle")

#########Send the mail if something's new
if(notenolddate == False):
    os.remove("notentabelle")
    os.rename("notentabelletmp", "notentabelle")
    msg = MIMEText("<html><body><table>"+resultable+"</table></body></html>", "html")
    msg["From"] = MAIL_FROM
    msg["To"] = MAIL_TO
    msg["Subject"] = "Es gibt neue Noten!"
    server = smtplib.SMTP("localhost")
    server.sendmail(MAIL_FROM, MAIL_TO, msg.as_string())
else:
    os.remove("notentabelletmp")
