from py2neo import Graph
from os import getenv
from dotenv import load_dotenv
load_dotenv()

graph_db = Graph(getenv('URL_DB'))
