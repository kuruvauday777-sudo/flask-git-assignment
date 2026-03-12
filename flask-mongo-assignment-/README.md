# Flask API with MongoDB Atlas

## Project Overview
This project demonstrates how to build a Flask web application that provides an API endpoint and stores form data in MongoDB Atlas.

The application performs two main tasks:
1. Reads data from a backend JSON file and returns it through an API.
2. Allows users to submit data through a form which is stored in MongoDB Atlas.

---

## Technologies Used
- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML

---

## Project Structure

flask-mongo-assignment  
│  
├── app.py  
├── data.json  
├── templates  
│   ├── form.html  
│   └── success.html  
└── README.md  


## API Route

The `/api` route reads data from `data.json` and returns it as JSON.

Example:

http://127.0.0.1:5000/api

## Form Submission

Users can submit their name and email through a form.  
The submitted data is stored in MongoDB Atlas.


## Running the Application

1. Install dependencies
pip install flask pymongo dnspython

2. Run the Flask app
python3 app.py

3. Open browser
http://127.0.0.1:5000


## Output

- JSON API response from `data.json`
- Form submission stored in MongoDB Atlas
- Success page after submission
