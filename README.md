Junar Uploader
==============

Uploads data to a Junar Site using the Junar API.

usage:

copy settings.py.tpl to settings.py and edit according to your site (url
and auth_key)

create a csv file with the information for the files to upload. Sample
spreadsheet here:

https://docs.google.com/a/okfn.org/spreadsheet/ccc?key=0Aq9agjil66PydGFaRERZOVBEam5KMUFIM1dKVklrRlE#gid=0

call jupload.py with the csv file as parameter. Make sure all the files are
readable on their relative locations to the script.

csv columns must be separated by commas.

csv file must be saved in utf-8 encoding.

juploader prints the title of the dataset beign uploaded and then the response obtained from Junar's API

---------------------------

juploader for adding webservices
================================

Now you can add webservices too using jupload_webservice.py
Works like juploader but uses diferent parameters. You can see them in this CSV file:

https://docs.google.com/spreadsheets/d/1uwSctyt5JMWibZUSChsUrI-hvFh_0oNPNfgkADuhhZM/edit?usp=sharing
