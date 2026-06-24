# 🎬 Movie Recommendation System

## 📌 Project Overview

This project is a Content-Based Movie Recommendation System built using Python and Scikit-Learn.

The system recommends similar movies based on their genres. When a user enters a movie title, the system finds movies with similar genre patterns and displays the top recommendations.

---

## 🚀 Technologies Used

- Python
- Pandas
- Scikit-Learn
- CountVectorizer
- Cosine Similarity

---

## 📂 Dataset

Dataset contains:

- Movie ID
- Movie Title
- Genres

Total Movies: 10,329

---

## ⚙️ Project Workflow

### 1. Data Loading
Loaded the movie dataset using Pandas.

### 2. Data Exploration
Checked:
- Dataset shape
- Columns
- Missing values
- Data types

### 3. Feature Extraction
Converted movie genres into numerical vectors using CountVectorizer.

### 4. Similarity Calculation
Calculated similarity between movies using Cosine Similarity.

### 5. Recommendation System
Created a function that:
- Accepts a movie title
- Finds similar movies
- Displays the top 5 recommendations

---

## 💻 Sample Input

```python
recommend("Toy Story (1995)")
```

## 📊 Sample Output

```text
Recommended Movies:

Antz (1998)
Toy Story 2 (1999)
Adventures of Rocky and Bullwinkle, The (2000)
Emperor's New Groove, The (2000)
Monsters, Inc. (2001)
```

---

## 🎯 Skills Learned

- Data Preprocessing
- Feature Engineering
- CountVectorizer
- Recommendation Systems
- Cosine Similarity
- Python Programming

---

## 📈 Future Improvements

- Add movie posters
- Create a GUI using Streamlit
- Use movie ratings for better recommendations
- Deploy as a web application

---

## 👨‍💻 Author

**Shubham Arora**

BCA Student | AI & Machine Learning Learner

GitHub: Your GitHub Profile Link
LinkedIn: Your LinkedIn Profile Link
