
Axie Marketplace GraphQL Query
This repository contains a Python script to query the Axie Infinity Marketplace using GraphQL. With this script, you can retrieve information about Axies available for sale based on specific criteria.

Prerequisites
Before using this script, ensure you have:

Python installed on your machine
An Axie Infinity API key (Replace the placeholder api_key with your actual API key)
Usage
Clone this repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/axie-marketplace-query.git
Navigate to the cloned directory:
bash
Copy code
cd axie-marketplace-query
Open the Python script axie_query.py and replace the placeholder API key with your actual API key.

Run the script:

bash
Copy code
python axie_query.py
Description
This script sends a GraphQL query to the Axie Infinity Marketplace API endpoint. The query retrieves Axies available for sale based on specified criteria such as breed count, classes, and part point attributes. The response includes detailed information about each Axie, including its ID, class, breed count, experience points, auction order details, and parts.

Disclaimer
Please note that this script is provided for educational purposes only. Use it responsibly and respect the terms of service of the Axie Infinity platform.
