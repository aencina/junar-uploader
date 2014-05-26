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

You'll need a index csv file with a spreadsheet list.  

Sample for [a spreadsheet whit data here](https://docs.google.com/a/okfn.org/spreadsheet/ccc?key=0Aq9agjil66PydGFaRERZOVBEam5KMUFIM1dKVklrRlE#gid=0)  

**Fields**  

 * title: Name for you data
 * description: Information about this file (140 max length)
 * category: A valid category name
 * tags: A **quoted** comma separated values like: "tag1, tag2, tag3"
 * meta_data: Do not use if yopu don't need it
 * file_data: Path to readable spreadsheet file
 * table_id: Use *table0* for the first sheet (or single *csv* file)

Call jupload.py with the csv file as parameter. Make sure all the files are readable on their relative locations to the script.

**Sample call:**  
  `python jupload.py info.csv`  

**Consider the following:**  
  * Csv columns must be separated by commas.  
  * Csv file must be saved in utf-8 encoding.  
  * juploader prints the title of the dataset beign uploaded and then the response obtained from Junar's API  


juploader for webservices
--------------------------------

You can add webservices too using the same tool **jupload.py**  
Works like juploader but **uses diferent parameters**. You can see them in [this CSV file] (https://docs.google.com/spreadsheets/d/1uwSctyt5JMWibZUSChsUrI-hvFh_0oNPNfgkADuhhZM/edit?usp=sharing)  
  
The first column on the csv specify the *type* is a **webservice**, **if you forget this field the process will fail.**  
  
So, defining the fields in the csv file you can add a webservice to your junar account like this:  
  `python jupload.py info-webservices.csv`

You can define more than one webservice in the same csv file. You must use **one line** for each webservice definition.

**Fields:**  
  * type:  Always *webservice*  
  * title:  The title of the data  
  * description:  Information about this data (140 max length)  
  * category: A valid category name  
  * tags: A **quoted** comma separated values like: "tag1, tag2, tag3"
  * endpoint: The url of the webservice  
  * impl_type: Use **14** for *REST/JSON* and **1** for *SOAP/XML*. Others values are not allowed  
  * path_to_data:  Field name for the data with a *$.* prefix. Sample *$.data*  
  * path_to_headers: Field name for the headers data (field names) with a *$.* prefix. Sample *$.headers*  
  * token: just if webservice need it  
  * algorithm: just if webservice need it  
  * signature: just if webservice need it  
  * username: just if webservice need it  
  * password: just if webservice need it  
  * create_datastream: Optional. If you want to create a view use = 1  
  * status: Optional. For publish dataset and view (if *create_datastream*) use 3. Default is 1 (pending revision).  
  * data_source and select_statement: Optionals. If you want to define more about fields you can use this field.  
  * You can't use *clone* on webservices.  
  
  
  

