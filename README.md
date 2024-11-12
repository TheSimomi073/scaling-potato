## WEBMIN INSTALATOR DOCS

To use it, you must be in root, you can easily do it with "sudo su".

To execute it, use "bash WebminInstalator".

If there's any error, it may be because of the /etc/apt/sources.list.

To solve it, enter the /etc/apt/sources.list, you can do it with "sudo nano /etc/apt/sources.list"
In there, delete any line that contains:

"deb http://download.webmin.com/download/repository sarge contrib"
