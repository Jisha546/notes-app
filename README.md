To‑Do App
A full‑stack web application where you can manage your daily tasks.
Built with React on the frontend and FastAPI on the backend.

Table of Contents
Features

Folder Structure
Tech Stack
Setup & Run
Backend Setup
Frontend Setup
API Endpoints
Screenshots
Author
License

Features
Add new tasks
See all tasks in a list
Mark tasks as done
Delete tasks
Responsive user interface
API powered by FastAPI

Folder Structure
csharp
Copy code
project/
├── backend/                # Backend FastAPI app
│   ├── main.py             # FastAPI routes & logic
│   └── requirements.txt    # (optional) Python dependencies
│
├── frontend/               # Frontend React app
│   ├── public/
│   └── src/
│       ├── App.js          # Main React component
│       └── index.js
│
├── README.md               # This file
├── .gitignore
Tech Stack
Layer	Technology
Frontend	React.js, Axios
Backend	Python, FastAPI
Server	Uvicorn
Optional DB	SQLite/Postgres

Setup & Run
Backend Setup
1Navigate to the backend folder:

bash
Copy code
cd backend
2Create and activate a virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate       # On Windows
# or
source venv/bin/activate    # On Linux/Mac
3Install dependencies:

bash
Copy code
pip install fastapi uvicorn
4 Run the backend server:

bash
Copy code
uvicorn main:app --reload
Backend is now running at:
http://127.0.0.1:8000

 Frontend Setup
1Navigate to the frontend folder:

bash
Copy code
cd frontend
2 Install dependencies:

bash
Copy code
npm install
3 Start the React development server:

bash
Copy code
npm start
Frontend is now running at:
http://localhost:3000

API Endpoints
Method	Endpoint	Description
GET	/todos	Fetch all tasks
POST	/todos	Add a new task
DELETE	/todos/{task_id}	Delete a task by ID

Sample JSON for POST:

json
Copy code
{
  "task": "Buy groceries"
}
Sample JSON response:

json
Copy code
[
  {"id": 1, "task": "Buy groceries", "completed": false}
]
Screenshots
Frontend	Backend


Author
Jisha George
GitHub Profile

License
This project is licensed under the MIT License — see the LICENSE file for details.

