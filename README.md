# Story_into_animation
This project allows users to enter a short story in English and automatically detects characters (like "boy", "girl") and their actions (like "walking", "running", "dancing") using basic Natural Language Processing (NLP) with the nltk library.

---

## ✨ Features

- Takes a user-written story as input
- Tokenizes the text into sentences and words
- Removes stopwords and punctuation
- Matches words with predefined character-action pairs
- Displays detected actions for each character

---

## 📷 Example

**Input:**
A boy is walking and a girl is dancing.

**Output:**
Sentence: A boy is walking.
Actions found: ['boy -> walk']
Sentence: A girl was dancing.
Actions found: ['girl -> dance']


https://github.com/user-attachments/assets/b95e663e-2236-451b-bb16-88835f5a5a85




---

## 🛠 Technologies Used

- Python 3
- NLTK (Natural Language Toolkit)

---

## 📥 Installation

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2.**Install dependencies:**

```
pip install nltk
```
3.**Run the script:**

```
python app.py
```

Enter your story and see the output!

**🧾 Requirements**
Python 3.x

Internet connection (to download nltk data)

**🚀 Future Scope**
Add more character types and action words

Create animations using MoviePy

Add speech using text-to-speech

Make a web interface using Flask or Streamlit


**🤝 Contributing**
Feel free to open issues or submit pull requests to improve the project!
