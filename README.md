# shortURLGenerator

ShortURLGenerator is a simple and lightweight HTTP-based RESTful API built using the Flask framework for managing short URLs and redirecting clients. This project allows you to create short aliases for long URLs, making it convenient for sharing and tracking links.

## Features

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
- [Design Considerations](#design-considerations)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- Pip (Python package installer)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/short-url-generator.git

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
     
## Design Considerations
This system may eventually scale to support millions of short URLs. 
A short URL: 
1. Has one long URL 
2. No duplicate short URLs are allowed to be created.
3. Short links can live forever or can be deleted by the user.
4. Shortened URL can be a combination of numbers (0-9) and characters (a-z, A-Z).

Application level:
1. Write operation: support 10 million URLs / day = 116 URLs / second
2. Read operation: assuming the read / write ratio is 10:1. Read operation per second: 1160 URLs / second
3. Delete operation: assuming the write / delete ration is 10:1. Delete operation persecond: 12 URLs / second
4. Assuming our application will run for 10 years and based on above assumpitons, we will have (10 - 1) million * 365 * 10 = 33 billion records
5. Assuming average URL length is 100, storage over 10 years will require 33 billion * 100 bytes = 3 TB
