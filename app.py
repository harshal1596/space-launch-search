import requests
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from elasticsearch import Elasticsearch

es = Elasticsearch([{'port': 9200, 'host': 'localhost'}])
app = Flask(__name__)
api = Api(app)

headers = {
    'Content-Type': "application/json"
}
space_flight_news_api = 'https://api.spaceflightnewsapi.net/v3/articles'

INDEX_NAME = 'space_flight_news_articles'


class SearchDocument(Resource):
    def post(self, query):
        body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "summary", "url"]
                }
            }
        }
        search_results = es.search(index=INDEX_NAME, body=body)
        if len(search_results['hits']['hits']):
            return jsonify(search_results)
        else:
            return {'Error': "Data not found"}, 404


class AddDataElasticSearch(Resource):
    def post(self):
        req_data = requests.request("GET", url=space_flight_news_api, headers=headers)
        data = req_data.json()
        add_data_to_elasticsearch(data)

        return {'Message': 'Data is added to elasticsearch.'}


def add_data_to_elasticsearch(data):
    for article in data:
        body = {
            'id': article['id'],
            'title': article['title'],
            'summary': article['summary'],
            'url': article['url']
        }
        try:
            es.index(index=INDEX_NAME, doc_type='space_flight_news', body=body)
        except Exception as e:
            return {'Error': e}


api.add_resource(AddDataElasticSearch, '/insert')
api.add_resource(SearchDocument, '/search/<query>')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
