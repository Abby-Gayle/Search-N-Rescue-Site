# Search-N-Rescue-Site

About the Project/Project Title
This was created to help the company Grazioso Salvare to be able to help them see which dogs could be good candidates for search and rescue training. There are specific types of dogs they are looking for, and this program would help them get the dogs so they can start training. We created an interactive website to help companies filter out the animals they are looking for with locations.

Motivation
This project was created to improve the search process of Grazioso Salvare, to help them find specific dogs. We wanted to make something easy to use and search for the dogs they need. We created an interactive site for them to look through the shelters and easily filter out what they want.

Getting Started
To get a local copy up and running you will have to create a username and password in the admin database. The animal shelter data will be imported into the animal’s collection in the aac database. You can easily import the crud file this will help with creating, reading, updating, and deleting any information in the database if needed.
To be able to use the website just boot it up and from there you will be able to filter by what dog type you are looking for. How this works is the code imports the crud.py file connecting the mongodb of animal shelter information. Using the read retrieves the data for it to be able to be displayed on the site. The user can choose using the radio buttons to filter specific types of dogs for the search and rescue.
A challenge for this was figuring out how to make a list of key/value pairs. I had to do a little bit of reading then found an example that helped me out in the book Mastering MongoDB ch5 CRUD using python driver. Another challenge was learning how to make the radio buttons and then learning how to make them work with each other. I used the website called plotty saw an example and took that and ran with it. It was easy to make but when having the buttons interact was were it took me about an hour but it was my fault for not being to observant. I was making the input the variable in the function I just needed to make another variable for the parameter was all, everything worked afterwards.

Installation
MongoDB I used this software to store and be able to manage the animal shelter data. This is how we can create and read animal records from the database. Python and pymongo were used in creating code that would interact with mongo database. Dash was used to create an interactive site. Plotly was used when creating the pie chart. Dash Leaflet was used to display the map.
To Install:
Python: https://www.python.org/downloads/
Mongodb: https://www.mongodb.com/try/download/community
All others can be installed in terminal: pip install pymongo dash plotly dash-leaflet

Usage

Code Example
This code shows how we read the animal records from the mongo database. It also shows how the data is updated based on what button is clicked for filtering.  
 <img width="975" height="538" alt="image" src="https://github.com/user-attachments/assets/e20a7f6b-f996-403c-8cc4-4e4ecc441c76" />


Tests
Testing the CRUD program 1st import the CRUD module then create an object. This object will be able to help connect to the mongodb. This will allow the site to have animal database information. Created filters that allow the site to change based on what the user wants to see. Chart was checked that as the data changes the chart also shows the data specific to what is shown. Tested the map by making sure depending on animal selected the location is changed based on area of animal. 


Screenshots

Starter page:
<img width="782" height="395" alt="image" src="https://github.com/user-attachments/assets/a2fca957-ed8a-4e22-9f0b-d6a9ad8b1c50" />
<img width="800" height="235" alt="image" src="https://github.com/user-attachments/assets/ea29ec0a-2491-4a3a-91ed-f33529892ed5" />
  
Disaster rescue page:
 <img width="950" height="488" alt="image" src="https://github.com/user-attachments/assets/f4f333b2-5290-4a14-aaaa-37344e3fc33c" />

Mountain rescue page:
 <img width="844" height="431" alt="image" src="https://github.com/user-attachments/assets/a4b91f4d-c50c-4351-a86a-370bb98c9ab8" />

Water rescue page:
<img width="731" height="353" alt="image" src="https://github.com/user-attachments/assets/d4990a76-6993-4864-b5bd-b3575d98ec30" />
 <img width="749" height="311" alt="image" src="https://github.com/user-attachments/assets/db966d4f-4dcd-4478-91d8-4202a2ddff04" />

Contact
Your name: Abigail Gutierrez


The way to write programs that are maintainable, readable, and adaptable are by creating the CRUD python code. This is a code that I can easily use on different code to be able
to use on other programs, I want to use the CRUD method on. Also having easy to read comments helps to if other people or myself way later on comes back to it and update something. When coming to the problem at first it can seem overwhelming especially because I felt like I was unsure what to do at first but breaking everything down piece by piece and doing a bit of research on the software helped me out a lot. Computer scientists try to develop software that would help make people's lives easier, I think. They try and solve problems to help out everyone. The project would help the company be able to pick and choose the dogs they were looking for without having to go through and look at all the animals in the shelter.
