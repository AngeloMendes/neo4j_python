###test python+neo4j

init:
`docker-compose up` && `pipenv shell`

run tests:
- `pytest tests/py2neo/*`  //run tests for model classes using py2neo 
- `pytest tests/neomodel/*` //run tests for model classes using neomodel

helpful links:
- [Get started neo4j](https://neo4j.com/developer/get-started/)
- [docker-compose neo4j](https://towardsdatascience.com/get-going-with-neo4j-and-jupyter-lab-through-docker-a1994e0e95c6)
- [Neomodel](https://neomodel.readthedocs.io/en/latest/)
- [Py2neo OGM](https://py2neo.org/2021.1/ogm/index.html#module-py2neo.ogm)