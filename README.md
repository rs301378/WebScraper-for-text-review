# WebScraper-for-text-review
## Table of Content
* Demo
* Overview
* Technical Aspect
* Installation
* Run
* Deployement on Pivotal
* Directory Tree
* To Do
* Technologies Used
* Team
* Credits

## Demo
Link:- 

## Overview
This is a simple reivew scraper Flask app. This app simply scrap the reviews from flipkart site which include product, customer name, rating, Comment headings or comments and save that data into a `.csv` file.
## Technical Aspect
This project is divided into two parts:-
1. Build scraper using Python, HTML and css.
2. Host a Flask app on Pivotal cloud.

  * A user can enter the keywords into a search bar.
  * Hit enter after entering keywords. In the next page it will show the products reviews.
  * Used flipkart site to show the reviews of products.
  * Used Pivotalto make this app public and use on any platform.
## Installation
The code is written in `Python 3.6`. If you don't have Python installed you can find it [here](https://www.python.org/downloads/ "install python") .To install the required packages and libraries, run this command in the project directory after [clonning](https://www.howtogeek.com/451360/how-to-clone-a-github-repository/ "cloning") the repository.
`pip install -r requirements.txt`
## Run
### Step1.
To run this on local machine, un-comment the line number 87 or 85 and commentline number 86 or 83 in `flask_app.py` file. Then click on `run` button.
### Step2.
Copy the link for e.g. `http://127.0.0.1:8001/` and past it on your broweser and hit enter.
## Deployement on Pivotal
### Step1.
Maintain necessary files like `requirements.txt, Procfile, runtime.txt, manifest,yml` . **Givent in the projrct directory check there.**
### Step2. 
This step would be to follow the instructions given on [Pivotal Documnetation](https://docs.pivotal.io/platform/application-service/2-8/devguide/deploy-apps/rolling-deploy.html "Pivotal Documnetation") to deploy a web app.
## Directory Tree
`|--.idea 
| |--misc.xml
| |--modules.xml
| |--webScrapperText.iml
| |--workspace.xml
|--static/css
| |--fonts
| | |--all.css
| | |--all.min.css
| |--webfonts
| | |--fa-brands-400.lot
| | |--fa-brands-400.svg
| |--main.css
| |--style.css
|--templates
| |--base.html
| |--index.html
| |--results.html
|--Procfile
|--README.md
|--flask_app.py
|--manifest.yml
|--requirements.txt
|--runtime.txt
|--samsung.csv`
## To Do
1. Scrap multiple pages at one time.
2. Add better UI and animations to display the reviews.
## Technologies Used
![Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)   ![Pivotal](https://4.bp.blogspot.com/-C-7zGVquuN0/W3sTKSKPseI/AAAAAAAAEYw/qUs8kXRXHTwV_VnA-sUFIH5aOnum68HKwCLcBGAs/s1600/center-pivotal-logo.png)  ![Flask](https://miro.medium.com/max/438/1*0G5zu7CnXdMT9pGbYUTQLQ.png)
## Team
![Rohit](https://avatars0.githubusercontent.com/u/35064155?s=400&u=55b08cb72de99de06f4f8728e038297e90c8e255&v=4){:height="700px" width="400px"}
## Credits
All the creadits of this project goes to the team of [iNeuron](https://ineuron.ai/ "iNeuron") and Mr. Sudhanshu Kumar.
