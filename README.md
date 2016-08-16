Our tool. The Junar Uploader
==============

Uploads or updates data in batches to a Junar Site using the Junar API.

Usage:

Copy *settings.py.tpl* to *settings.py* and edit according parameters to your site. Put your auth_key and url.
The **url** parameter like:  

  `http://you_api_url/datastreams/publish`  

Create a csv file with the information for the files to upload.
You can upload a simple spreadsheet with data or define the information for a web service connection.

### <a name="ourtool"></a>
Upload spreadsheet data
-----------------------

You'll need a index csv file with a spreadsheet list.  

Sample for [a spreadsheet with data here](https://docs.google.com/a/okfn.org/spreadsheet/ccc?key=0Aq9agjil66PydGFaRERZOVBEam5KMUFIM1dKVklrRlE#gid=0)  

**Fields**  

 * title: Mandatory. Name for you data. Up to 100 characters
 * description: Optional. Information about this file. Up to 140 characters
 * category: A valid category name. Mandatory
 * tags: A **quoted** comma separated values like: "tag1, tag2, tag3"
 * meta_data: Do not use if you don't need it
 * file_data: Path to readable spreadsheet file
 * table_id: Use *table0* for the first sheet (or single *csv* file)
 * guid: Optional. use it with *clone* for update existing data.
 * clone: Optional. *True* for edit a pre-existing data. Must be applied with *guid*
 * header_row: Optional. Defines a particular row of the dataset as the header row. Use *row0* as the first row.

Call jupload.py with the csv file as parameter. Make sure all the files are readable on their relative locations to the script.

**Sample call:**  
  `python jupload.py info.csv`  

**Consider the following:**  
  * CSV columns must be separated by commas.  
  * CSV file must be saved in utf-8 encoding.  
  * juploader prints the title of the dataset being uploaded and then the response obtained from Junar's API  


juploader for web services
--------------------------------

You can add web services too using the same tool **jupload.py**  
Works like juploader but **uses different parameters**. You can see them in [this CSV file] (https://docs.google.com/spreadsheets/d/1uwSctyt5JMWibZUSChsUrI-hvFh_0oNPNfgkADuhhZM/edit?usp=sharing)  
  
The first column on the csv specify the *type* is a **webservice**, **if you forget this field the process will fail.**  
  
So, defining the fields in the csv file you can add a webservice to your junar account like this:  
  `python jupload.py info-webservices.csv`

You can define more than one web service in the same csv file. You must use **one line** for each web service definition.

**Fields:**  
  * type:  Always *webservice*  
  * title:  The title of the data  
  * description:  Information about this data (140 max length)  
  * category: A valid category name  
  * tags: A **quoted** comma separated values like: "tag1, tag2, tag3"
  * endpoint: The url of the web service  
  * impl_type: Use **14** for *REST/JSON* and **1** for *SOAP/XML*. Others values are not allowed  
  * path_to_data:  Field name for the data with a *$.* prefix. Sample *$.data*. See https://code.google.com/p/json-path/ for reference.
  * path_to_headers: Field name for the headers data (field names) with a *$.* prefix. Sample *$.headers*. See https://code.google.com/p/json-path/ for reference. 
  * token: just if webservice need it  
  * algorithm: just if webservice need it  
  * signature: just if webservice need it  
  * username: just if webservice need it  
  * password: just if webservice need it  
  * create_datastream: Optional. If you want to create a view use = 1  
    * You can't use *clone* on web services.  
