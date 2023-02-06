<h1><b>Project Name: To-Do API</b></h1>

<h2><b>Introduction</b></h2>
This project is an implementation of REST API for a to-do list application using the FastAPI framework and either MySQL or MongoDB for database management. The API supports authentication and implements CRUD (Create, Read, Update, Delete) functionalities for to-do items.

<h2><b>Requirements</b></h2>
<ul>
<li>FastAPI</li>
<li>Python 3.6+</li>
<li>MySQL/MongoDB</li>
<li>python-dotenv (optional, for environment variables)</li>
 </ul>
 ![image](https://user-images.githubusercontent.com/95700607/217033888-eb6bd28d-ab7c-40e1-a911-d830b25a8f50.png)

 
<h2><b>Installation</b></h2>
<ol>
<li>Clone the repository to your local machine.</li>
<li>Navigate to the project folder and run pip install -r requirements.txt to install the required dependencies.</li>
<li>For database management, either install the MongoDB Community Edition or change the DATABASE_URL in the .env file to the URL of your MongoDB Atlas instance.</li>
<li>Create an .env file in the root of the project and define the path to the database as follows: DATABASE_URL="mongodb://localhost:27017/todoDB".</li></ol>

<h2><b>Usage</b></h2>

To run the project, navigate to the root of the project and run python root.py. The API will be available at http://localhost:8000/.

<h2><b>API Endpoints</b></h2>
The following endpoints are available for CRUD operations on to-do items:<li>
<ul>
<li>POST /todos: Creates a new to-do item.</li>
<li>GET /todos: Retrieves a list of all to-do items.</li>
<li>GET /todos/{id}: Retrieves a specific to-do item by ID.</li>
<li> /todos/{id}: Updates a specific to-do item by ID.</li>
<li>DELETE /todos/{id}: Deletes a specific to-do item by ID.</li></ul>
 
<h2><b>Authentication</b></h2>
 
The API uses basic authentication for secure access to to-do items.

<h2><b>Conclusion</b></h2>

This project provides a simple yet functional REST API for a to-do list application using FastAPI and either MySQL or MongoDB. It can serve as a starting point for further development or customization to meet specific needs.



