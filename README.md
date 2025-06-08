# MCQ Generator App

This is a Flask-based web application that allows users to take multiple-choice quizzes on various topics.

## Features

- Choose from multiple topics: Math, Science, Java, NoSQL
- Displays all questions of the selected topic on one page  
- Four options per question with radio buttons
- Only one option selectable per question
- Displays final score after quiz submission

## How to Run the Project

1. Clone the repository:
```
git clone https://github.com/rudrakshiii8/mcq-generator.git
cd mcq-generator
```

2. Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\activate   # Windows
# Or on Mac/Linux:
# source venv/bin/activate
```

3. Install dependencies:
```
pip install -r requirements.txt
```

4. Run the app:
```
python app.py
```

5. Open your browser and visit:
```
http://127.0.0.1:5000
```

## Available Topics

- Math  
- Science  
- Java  
- NoSQL  

## Project Structure

```
mcq-generator/
│
├── templates/
│   └── index.html
├── app.py
├── mcq_data.py
├── requirements.txt
└── README.md
```

## Author

Rudrakshi Thakur  
GitHub: [@rudrakshiii8](https://github.com/rudrakshiii8)

## License

This project is for educational purposes only.
