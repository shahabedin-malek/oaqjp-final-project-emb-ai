# oaqjp-final-project-emb-ai

## Final Project - Emotion Detector

An AI-based web application that detects emotions in text using the **Watson NLP Embed library**.

---

## Project Structure

```
oaqjp-final-project-emb-ai/
│
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
│
├── templates/
│   └── index.html
│
├── server.py
├── test_emotion_detection.py
└── README.md
```

---

## Tasks Completed

| Task | Description |
|------|-------------|
| Task 1 | Cloned the project repository |
| Task 2 | Created emotion detection application using Watson NLP library |
| Task 3 | Formatted the output of the application |
| Task 4 | Packaged the application as `EmotionDetection` |
| Task 5 | Ran unit tests on the application |
| Task 6 | Web deployment using Flask |
| Task 7 | Incorporated error handling (status 400 & blank input) |
| Task 8 | Ran static code analysis with pylint (10.00/10) |

---

## How to Run

### 1. Install dependencies
```bash
pip install flask requests
```

### 2. Start the Flask server
```bash
python3 server.py
```

### 3. Open in browser
```
http://localhost:5000
```

---

## API Endpoint

```
GET /emotionDetector?textToAnalyze=<your text here>
```

### Sample Response
```
For the given statement, the system response is 'anger': 0.006274985,
'disgust': 0.0025689833, 'fear': 0.009251649, 'joy': 0.9680386 and
'sadness': 0.049744144. The dominant emotion is joy.
```

---

## Technologies Used

- Python 3.x
- Flask
- Watson NLP Embed Library
- Pylint
- Unittest / Pytest

---

## Author

**Joel Jolly**  
GitHub: [withinjoel](https://github.com/withinjoel)
