# shortURLGenerator

ShortURLGenerator is a simple and lightweight HTTP-based RESTful API built using the Flask framework for managing short URLs and redirecting clients. This project allows you to create short aliases for long URLs, making it convenient for sharing and tracking links. 

It supports the following features:
1. Generate a short URL from a long url
2. Redirect a short URL to a long url
3. List the number of times a short url has been accessed in the last 24 hours, past week, and all time
4. Support short URL deletion

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
  - [Run the Application](#run-the-application)
  - [API Endpoints](#api-endpoints)
- [Design Considerations and Assumptions](#design-considerations-and-assumptions)
- [Improvements](#improvements)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Pip (Python package installer)
- Docker

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/ustbsheila/shortURLGenerator.git

## Usage
### Run the Application

1. Run the application using Docker. It will pull required MySQL image, install python packages and run the application in containers. 

   ```bash
    docker-compose up -d
   ```
   
    The application will run on http://127.0.0.1:8080/ by default. Open this URL in your browser or use a tool like Postman to interact with the API.

### API Endpoints
1. Shorten URL
   - Endpoint: api/v1/shorten
   - Method: `POST`
   - Request Body:
     ```
      {
        "long_url": "https://www.example.com"
      }
     ```
   - Response:
     - If the given short url exists, it will return a successful status code 200.
     ```
      {
        "short_url": "http://localhost:8080/api/v1/5d02642a"
      }
     ```
     - If the given short url doesn't exist, it will create a shorten URL and return a successful status code 200.
     ```
      {
        "short_url": "http://localhost:8080/api/v1/5d02642a"
      }
     ```
2. Redirect to Original URL
   - Endpoint: api/v1/<short_url>
   - Method: `GET`
   - Example: `http://localhost:8080/api/v1/5d02642a`
   - Response: 
     - If the given short url exists, it will return a successful redirect status code 302 (We use 302 redirect here to better keep track of short URL access stats which is supported below.)
     - If the given short url doesn't exist, it will return 404 NOT FOUND.
     ```
     {
       "Error": "Short URL 5d02642aaa not found!"
     }
     ```
3. Access Statistics
   - Endpoint: api/v1/stats/<short_url>
   - Method: `GET`
   - Example: `http://localhost:8080/api/v1/stats/5d02642a`
   - Response:
     - If the given short url exists, it will return a successful status code 200.
     ```
      {
      "last_24_hours_access_stats": 5,
      "past_week_access_stats": 30
      "all_time_access_stats": 200
      }
     ```
     - If the given short url doesn't exist, it will return 404 NOT FOUND.
     ```
     {
       "Error": "Short URL 5d02642aaa not found!"
     }
     ```
4. Delete Short URL
   - Endpoint: api/v1/delete/<short_url>
   - Method: `DELETE`
   - Example: `http://localhost:8080/api/v1/delete/5d02642a`
   - Response:
     - If the given short url exists, it will return a successful status code 200.
     ```
     {
       "Message": "Short URL 5d02642a deleted successfully."
     }
     ```
     - If the given short url doesn't exist, it will return 404 NOT FOUND.
     ```
     {
       "Error": "Short URL 5d02642aaa not found!"
     }
     ```
     
## Design Considerations and Assumptions
### Short URL System Design
This short URL generation system is designed to handle various considerations to ensure scalability, data integrity, and performance. Below are the key design considerations and assumptions that influenced the system architecture:
### Short URL Characteristics:
1. Unique Short URLs:
  - No duplicate short URLs are allowed. Each short URL is unique and corresponds to one long URL.
2. Longevity of Short URLs:
  - Short links can either be permanent (live forever) or can be deleted by the user. Considering data integrity and privacy, when shorten URLs are deleted, all associated information like stats are deleted.
3. Shortened URL Format:
  - Shortened URLs are converted by CRC32 hash function. Based on the back-envolop calculation below, it's not sufficient to support millions of daily URL shorten request. But it' good starting point for the application. We can easily upgrade the hash function later.

### System Scalability:
1. Scale Expectations: The system is designed to scale and support millions of short URLs.
2. The system is expected to handle write operations for creating short URLs at a rate of 12 URLs per second, allowing for the support of 1 million URLs per day.
3. Assuming a read/write ratio of 10:1, the system is designed to handle read operations at a rate of 116 URLs per second.
4. Assuming a write/delete ratio of 10:1, the system is designed to handle delete operations at a rate of 1 URLs per second.
5. Since CRC32 generates a 32-bit checksum, there are possible unique CRC32 values, which is equal to ~4 billion. This provides a sufficiently large space of unique values for the first billion shorten URLs.
6. Assuming average URL length is 100, storage over 10 years will require 4 billion * 100 bytes = 0.4 TB

### Storage Requirements:
1. Data Storage
   - The system assumes an average URL length of 100 bytes.
2. Storage Calculation
   - Over the 10-year period, the storage requirement is estimated to be 0.4 TB based on 4 billion records.

### Choice of Database - MySQL:
1. Relational Data Model
    - MySQL provides a reliable and robust relational database model, suitable for storing the structured data associated with short URLs.
2. ACID Compliance 
   - MySQL adheres to the ACID (Atomicity, Consistency, Isolation, Durability) properties, ensuring data consistency and reliability.
      Scalability:
3. MySQL scalability
   - MySQL supports horizontal and vertical scaling, allowing the system to scale as the data volume increases over time.
4. Transaction Support:
   - Transactions are crucial for maintaining data integrity, and MySQL's support for transactions ensures that operations are performed reliably.

## Improvements
To enhance the system, the following improvements can be considered:
1. Better Hash Function:
    - To support more users and reduce the likelihood of collisions, consider implementing a more robust hash function (e.g., SHA-256) for short URL generation. Update the hash resolution function accordingly.
2. Cache Implementation:
    - Introduce caching mechanisms to improve performance. Caching commonly accessed short URLs or frequently queried data can significantly reduce database load and enhance response times.
3. Other Enhancements:
    - Explore additional improvements based on evolving requirements or emerging technologies. This may include optimizing database queries, implementing asynchronous processing, or integrating with content delivery networks (CDNs) for faster content delivery.
