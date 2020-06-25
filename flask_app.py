'''
Created on 26June2020
@author: Rohit Sharma
'''
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen as uReq

app = Flask(__name__)


@app.route('/', methods=['GET'])  # route to display the home page
@cross_origin() # when we deploy our code on different kind of servers it will not created any issue.
def homePage():
    return render_template("index.html")

# GET is used to send the request to the server by URL and POST is used to send the request to the server by any body.
@app.route('/review', methods=['POST', 'GET'])  # route to show the review comments in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            searchString = request.form['content'].replace(" ", "") # replace blank with data and append it to the url.
            flipkart_url = "https://www.flipkart.com/search?q=" + searchString
            uClient = uReq(flipkart_url) # returns https response
            flipkartPage = uClient.read() # here it returns all the information regarding url
            uClient.close()
            flipkart_html = bs(flipkartPage, "html.parser") # beautifulsoap creates propoer indentation of the data
            bigboxes = flipkart_html.findAll("div", {"class": "bhgxx2 col-12-12"}) # here this line find all the classes with "bhgxx2 col-12-12" this name
            del bigboxes[0:3]
            box = bigboxes[0]
            productLink = "https://www.flipkart.com" + box.div.div.div.a['href'] # from the product list get the link of all the products
            prodRes = requests.get(productLink)
            prodRes.encoding = 'utf-8' # encode the data (English)
            prod_html = bs(prodRes.text, "html.parser") # parse the data again inside the product
            print(prod_html)
            commentboxes = prod_html.find_all('div', {'class': "_3nrCtb"}) # get all the commments rating etc.
            # dump all the data into CSV file
            filename = searchString + ".csv"
            fw = open(filename, "w")
            headers = "Product, Customer Name, Rating, Heading, Comment \n"
            fw.write(headers)
            # trying to extract the data one-by-one
            reviews = []
            for commentbox in commentboxes:
                try:
                    # name.encode(encoding='utf-8')
                    name = commentbox.div.div.find_all('p', {'class': '_3LYOAd _3sxSiS'})[0].text
                except:
                    name = 'No Name'
                try:
                    # rating.encode(encoding='utf-8')
                    rating = commentbox.div.div.div.div.text
                except:
                    rating = 'No Rating'
                try:
                    # commentHead.encode(encoding='utf-8')
                    commentHead = commentbox.div.div.div.p.text
                except:
                    commentHead = 'No Comment Heading'
                try:
                    comtag = commentbox.div.div.find_all('div', {'class': ''})
                    # custComment.encode(encoding='utf-8')
                    custComment = comtag[0].div.text
                except Exception as e:
                    print("Exception while creating dictionary: ", e)

                mydict = {"Product": searchString, "Name": name, "Rating": rating, "CommentHead": commentHead,
                          "Comment": custComment}
                reviews.append(mydict)
            return render_template('results.html', reviews=reviews[0:(len(reviews) - 1)])
        except Exception as e:
            print('The Exception message is: ', e)
            return 'Something is Wrong!'
    # return render_template('results.html')

    else:
        return render_template('index.html')

#port = int(os.getenv("PORT"))
if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=5000)
    #app.run(host='0.0.0.0', port=port) #for sever
    app.run(host='127.0.0.1', port=8001, debug=True)
