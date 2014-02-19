hisnotify
=========

Mails you about new exam results


Nutzen
------

Dieses kleine Python-Script fragt das HIS der FH Frankfurt ab, wertet die Notenübersicht aus und verschickt eine Mail, sobald neue Noten eingegangen sind.
Praktisch, wenn man sehr neugierig ist, sich aber nicht dauernd umständlich auf der HIS-Seite einloggen und durchklicken will.

Voraussetzungen
---------------

Zusätzlich zu den Standardbibliotheken in Python2 wird noch benötigt:

* Beautiful Soup
* mechanize

Leider läuft mechanize momentan nur auf Python2, weshalb Beautiful Soup nur in der Version 3 verwendet werden kann.


Konfiguration
-------------

In der Datei his.py müssen noch die Werte

* Matrikelnummer
* Passwort
* Absenderadresse
* E-Mail Adresse

angepasst werden.


Danach muss noch ein cronjob oder ähnliches eingerichtet werden, dass die Seite abfragt.
Bitte stell die Frequenz dafür nicht zu hoch ein, um nicht unnötig Last auf den HIS-Servern zu erzeugen.
Ein paar Mal am Tag sollte reichen.


Stabilität
----------

Beim ersten Durchlauf gibt es noch eine Fehlermeldung, da eine Datei fehlt. Beim Zweiten sollte dann alles wunderbar funktionieren.
Getestet ist die Software allerdings nur in dem Studiengang Informationssystemtechnik der FH Frankfurt, sollte aber, nach evtl. nötigen, leichten Anpassungen,
auch auf anderen HIS-Plattformen und für andere Studiengänge lauffähig sein.
