# health-nyc

This is a project that pulls data from NYCOpenData: https://opendata.cityofnewyork.us/ and does aggregations on the data to understand trends. 

PLAN:

* -> Read the data into spark, run aggs, cleanse and stage the data
* -> Stream the data to a Kafka Topic
* -> Consume from the kafka topic
* -> write to a caching layer (redis)
* -> consume message from redis
* -> push to a Postgres DB.

{ Using Docker compose for env setup }
