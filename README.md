# Chemovator_challenge

### Solution
#### Requirements
* Run requirements.txt file to install the required packages.
#### Files
* **database.py :** Creates postgres database.
* **models.py :** Contains the DocInfo class that has two attributes (file_name: primary key , keyphrases) and which will be mapped to a table on the database.
* **keyphrases_extractor.py :** Contains functions for cleaning the text, defining the extractor and extracting the keyphrases.
* **settings.py :** Contains database settings.
* **main.py :** Execution file (extracting keyphrases from xml file and filling the newly created table with the entries that were provided from extraction).
* **patent_doc_database.log :** Contains status messages or any other output streams.
#### Usage
This solution can be executed via main.py.
#### Algorithms
###### 1- Keyphrases extraction
As shown in the figures 1 and 2, These are the results of a recent benchmark that measured 
the performance of several keywords extraction models using a dataset of 2000 samples.

![alt text](../../models_time.png)
<figcaption align = "center"><b>Fig.1 - Elapsed time in seconds</b></figcaption>

According to the time elapsed in seconds in figure 1, Rake outperforms all other algorithms 
by a significant margin. Rake processes 2000 documents in only two seconds, which is impressive.

![alt text](../../models_acc.png)
<figcaption align = "center"><b>Fig.2 - Accuracy results</b></figcaption>

The results in the figure 2 are as follows if we were to simply take accuracy into account, which is calculated 
as the ratio of average matched keywords to average keywords per document and as
you can see KeyBERT wins on all other algorithms from the accuracy perspective by a great deal
even though Rake is performing quite well also.

Given that we are just working with some sample data, **KeyBERT would certainly claim the top rank for being the most precise algorithm capable of extracting keyphrases.**
(if we require accuracy over anything else and we are not constrained by time).

But in case that we are processing **hundreds of millions of documents**, **Rake would be the 
best algorithm in terms of efficiency** (Given the short amount of time it takes to perform the extraction,It makes sense to have such a good performance score).

Since we are dealing with **some sample data and time is not a constraint**, I decided to use **KeyBERT**.
###### 2- Database
In order to store the results (extracted keyphrases per document), I decided to use 
**Postgres (an object-relational database)** which is one of the most advanced open source relational database systems
along with **SQLAlchemy** library that facilitates the communication between Python programs and databases and which is used as an Object Relational Mapper (ORM) also that translates Python classes to tables statements.

![alt text](../../original.jpg)
