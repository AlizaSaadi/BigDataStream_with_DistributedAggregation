Overview:
This project implements a real-time pipeline for fetching, categorizing, and processing Bitcoin price data using Kafka, Hadoop, and MapReduce. It consists of the following components:

Producer: Fetches live price data from Coinbase API and publishes it to Kafka topics based on price ranges.

Consumer: Consumes Kafka messages and appends them to HDFS files for further processing.

MapReduce: Processes stored HDFS data to calculate statistics such as the average price.

Features:

Real-Time Data Ingestion: Fetches Bitcoin prices from the Coinbase API and streams them to Kafka.

Dynamic Topic Categorization: Routes data to Kafka topics based on price ranges.

HDFS Integration: Stores categorized data in HDFS files for scalable processing.

MapReduce Statistics: Computes average prices using a MapReduce job.


Requirements:

Python 3.x,
Kafka,
Hadoop


