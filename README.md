Junar Uploader
==============

Uploads data to a Junar Site using the Junar API.

Usage:

Copy *settings.py.tpl* to *settings.py* and edit according parameters to your site. Put your auth_key and url.
The **url** parameter like:

	`http://you_api_url/datastreams/publish`

Create a csv file with the information for the files to upload.
You can upload a simple spreadsheet whit data or define the information for a webservice connection.

Upload spreadsheet data
-----------------------

Sample for [a spreadsheet whit data here](https://docs.google.com/a/okfn.org/spreadsheet/ccc?key=0Aq9agjil66PydGFaRERZOVBEam5KMUFIM1dKVklrRlE#gid=0)

Call jupload.py with the csv file as parameter. Make sure all the files are readable on their relative locations to the script.

Sample call:
	`python jupload.py info.csv`

Consider the following:
  * Csv columns must be separated by commas.
  * Csv file must be saved in utf-8 encoding.
  * juploader prints the title of the dataset beign uploaded and then the response obtained from Junar's API


juploader for webservices
--------------------------------

You can add webservices too using the same tool **jupload.py**
Works like juploader but uses diferent parameters. You can see them in [this CSV file] (https://docs.google.com/spreadsheets/d/1uwSctyt5JMWibZUSChsUrI-hvFh_0oNPNfgkADuhhZM/edit?usp=sharing)
The first column on the csv specify the *type* is a **webservice**, if you forget this field the process will fail.

So, defining the fields in the csv file you can add a webservice to your junar account like this:
	`python jupload.py info-webservices.csv`

You can define more than one webservice in the same csv file. You must use one line for each webservice definition.

Notes:
  * For the *impl_type* field use **14** for *REST/JSON* and **1** for *SOAP/XML*
  * Include the *status* column for puslish (3) or no (1=default)