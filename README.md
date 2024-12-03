# Wishapp

This project is used to demonstrate the use of FastAPI by building a simple REST API for a wish list application.
The project is divided into multiple steps. Each step can be accessed by checking out the respective branch.

## Installation
The project is built with python 3.12. We haven't tested it with the older version, but since it's just using the basic
features of FastAPI, it should work with older versions as well.
We recommend using poetry to manage the dependencies. However, we've also included a `requirements.txt` file for those 
who prefer using pip and virtual envs.
### Poetry
```shell
poetry install
```
### Pip
```shell
python -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

## Running the app
```shell
python -m app.server
```

## Steps
### Step 1: Basic FastAPI Application
```shell
git checkout origin/step-1
```
In the first step, we will create a simple FastAPI application with a basic project structure.

### Step 2: Wishapp APIs
```shell
git checkout origin/step-2
```

#### What is an API?
* A set of rules and protocols that allow different software systems to communicate with each other.
* APIs enable interaction between applications without needing direct human intervention.

#### What is a REST API?
* REST = Representational State Transfer
* Key Characteristics:
  * Stateless: Each request from a client to the server must contain all the information needed to process it.
  * Resource-Oriented: Focuses on resources, identified by URLs.
  * Standard HTTP Methods: CRUD operations mapped to HTTP verbs (GET, POST, PUT, DELETE).
  * Popularity: REST is widely used due to its simplicity and scalability.

#### Design considerations
* Direct vs Full Path Endpoints
* New endpoints vs Nested Endpoints
* Singular vs Plural Nouns
* Filtering, Sorting, and Pagination