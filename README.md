# FastAPI CRUD Application with Image Upload to MongoDB
This FastAPI application provides a basic CRUD (Create, Read, Update, Delete) API with image upload functionality. It uses MongoDB as the database for storing data and images.


## Features

- Create, Read, Update, and Delete operations for a model with image upload.
- Image files are stored in MongoDB.

## Tech Stack

- FastAPI: FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

- MongoDB: MongoDB is a NoSQL database that stores data in flexible, JSON-like documents.

## Getting Started

### Prerequisites

- Python 3.7+
- MongoDB installed and running


### Installation

1. Clone the repository:
    ```bash
   https://github.com/meakshayraut/Demo-APi.git
   
2. Install the dependencies:
   **pip install -r requirements.txt**
   
3. Set up MongoDB:
   Create a MongoDB database and configure the connection in the .env file.
   
4. Run the FastAPI application:
   **uvicorn main:app --reload**

   Visit *http://localhost:8000/docs* in your browser to access the Swagger documentation and test the API.


## Acknowledgements

[FastAPI Documentation](https://fastapi.tiangolo.com/) <br />
[MongoDB Documentation](https://docs.mongodb.com/)
   

