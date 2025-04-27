# python-redis-app<br />
<br />
👉 This project demonstrates a simple web application built with Flask and Redis using Docker Compose.<br />
👉 Each time you access the webpage, the counter increments and displays the number of visits.<br />
👉 An image is also served through Flask’s static folder.<br />
    
**Project Structure**<br />
.<br />
.
├── app.py                # Flask application code<br />
├── docker-compose.yml    # Docker Compose file to set up Flask and Redis<br />
├── requirements.txt      # Python dependencies<br />
└── static/<br />
    └── stickman.png      # Static image served on the webpage<br />

**Features**<br />
<br />
    i.Flask app connected to Redis for counting visits.<br />
    ii.Static image serving through Flask.<br />
    iii.Simple containerized setup using Docker Compose.<br />

📢 **Getting Started**<br />

📌 **Prerequisites**<br />
<br />
    👉Docker<br />
    👉Docker Compose<br />

📌 **Steps**<br />
<br />
    👉Clone this repository:<br />
            
        git clone https://github.com/AniketDhanai/python-redis-app.git
        cd python-redis-app
  
📌 **Start the application:**<br />
        
        docker-compose up

📌 **Access the app in your browser:**<br />
            
        http://localhost:5000

📌 **You should see:**<br />
<br />
    👉A "Hello Everyone!" message<br />
    👉A stickman image<br />
    👉A counter showing how many times the page has been visited<br />
    
📌 **Notes**<br />
<br />
    👉The Flask app automatically connects to Redis using the service name redis.<br />
    👉Static files like images must be placed inside the static/ folder.<br />
    👉If you add new Python packages, update the requirements.txt file accordingly.<br />


