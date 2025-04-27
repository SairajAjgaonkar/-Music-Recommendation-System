# 🎵 Music Recommendation System

---

## 🔍 Project Overview
This project is a **Music Recommendation System** that suggests songs to users based on their favorite singers and preferences. It uses **Collaborative Filtering** and **Content-Based Filtering** techniques, combined with a simple web app deployed using **Streamlit**.

---

## 📂 Dataset
- **File Used:** `gaanasongs.csv`
- **Columns:**
  - `name` (Song Name)
  - `singer` (Singer Name)
  - `singer_id` (Singer Unique ID)
  - `duration` (Duration of Song)
  - `link` (URL Link to Song)
  - `language` (Language of Song)

---

## 👥 Approach
1. **Data Cleaning & Preprocessing:**
   - Handle missing values.
   - Convert user interaction into numerical ratings if needed.

2. **Exploratory Data Analysis (EDA):**
   - Find top singers.
   - Explore language distribution.

3. **Model Building:**
   - Collaborative Filtering for recommending based on user preferences.
   - Content-Based Filtering for recommending songs with similar features.

4. **Deployment:**
   - Build a Streamlit app for interactive recommendations.

---

## 🚀 Technology Stack
- **Python**
- **Pandas**
- **Scikit-learn**
- **Streamlit**
- **Numpy**

---

## 👨‍💻 How to Run the Project

### ✅ Prerequisites
- Python installed (>=3.7)
- Install required libraries:
  ```bash
  pip install pandas numpy scikit-learn streamlit
  ```

### 🔄 Steps to Execute
1. Place `gaanasongs.csv`, `app.py`, and `utils.py` in the same folder.
2. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open the localhost link in your browser to view the app.

---

## 📊 Key Features
- Personalized music recommendations.
- Search songs by singer.
- Language insights of songs.
- Fast and lightweight web app.

---

## 🚫 Challenges Faced
- Dealing with incomplete/missing data.
- Building dynamic recommendation logic.
- Maintaining app responsiveness in Streamlit.

---

## 🚀 Future Enhancements
- Include audio features like tempo, rhythm.
- Add user feedback-based tuning.
- Expand dataset to international/global music.

---

## 🎉 Conclusion
This project demonstrates how **machine learning**, **data analysis**, and **web deployment** can come together to make a fun and useful **Music Recommendation System**! 📻🔗

---

> Developed with ❤️ by Sairaj Ajgaonkar

