
# space-launch-search-api
This application ingests the data from the public API spaceflightnews.net (https://api.spaceflightnewsapi.net/v3/articles), fetches the articles from the api and inserts data into Elasticsearch. This application also contains REST api which takes a keyword and able to give list of articles which contains the keyword.

# Required tools
1. Elasticsearch
2. Python 3.x.x
3. requirements.txt is provided along with the project

# Steps
1. Create the virtual environment
2. Activate the virtual environment
3. Go to the project directory
4. Install requirements.txt using command - pip install -r requirements.txt
5. Run the app.py using - python app.py
6. Open the Postman and create new request
7. Insert data into elasticsearch index using API "http://127.0.0.1:5000/insert" 
8. Go to API http://127.0.0.1:5000/search/{{keyword}} to get the list of articles with the matching keyword.
 


