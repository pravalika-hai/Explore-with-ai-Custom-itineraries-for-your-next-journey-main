# Explore with AI: Custom Itineraries for Your Next Journey

**Generative AI Project**

Explore with AI is an AI-powered travel planning web application that creates personalized, day-wise travel itineraries based on a selected destination and trip duration. It integrates Google’s Gemini AI model with a streamlined interface to automatically create structured travel plans, including recommended attractions and activities, making travel planning quick and easy.

## 🌟 The Problem
Travel planning can be overwhelming and time-consuming due to the extensive research and customization required to create detailed and personalized itineraries. Travelers often face challenges in finding reliable and tailored travel recommendations that suit their preferences, interests, and constraints. This problem is exacerbated for travel agencies and tour operators who need to generate high-quality itineraries efficiently to meet diverse client needs. 

A solution that automates and personalizes the creation of travel itineraries streamlines this process, providing valuable assistance to both individual travelers and industry professionals.

## ✨ Features
* **Personalized Itineraries:** Get day-by-day travel plans using state-of-the-art Generative AI (Google's Gemini Model).
* **Detailed Scheduling:** Includes morning, afternoon, and evening activities.
* **Local Dining & Tips:** Offers local dining suggestions and important travel tips (e.g., weather, transport, or etiquette).
* **Downloadable Itineraries:** Download the final plan directly as a `.txt` file.

## 🛠️ Tech Stack
* **Python**
* **Streamlit**: For the interactive web interface.
* **Google Generative AI (`google-generativeai`)**: Used for generating travel itineraries via the Gemini model.
* **python-dotenv**: For managing environment variables securely (API Key).

## 📁 Project Structure
* `Project Files/travel.py` – Main application file that runs the Streamlit app and connects to AI.
* `Project Files/requirements.txt` – Contains required Python libraries to install and run the project.
* `Document/` – Contains project documentation corresponding to various software development phases like Ideation, Requirement Analysis, Design, Planning, Development, and Demonstration.
* `Video Demo/` – Contains demonstration videos of the app.
* `README.md` – Project overview and instructions.

## 🚀 How to Run Locally

1. **Clone the repository or navigate to the project directory:**
   ```bash
   cd Explore-with-ai-Custom-itineraries-for-your-next-journey-main
   ```

2. **Install the required dependencies:**
   Navigate into the `Project Files` directory and install the libraries:
   ```bash
   pip install -r "Project Files/requirements.txt"
   ```

3. **Set up the Google Gemini API Key:**
   By default, the application has a placeholder or a development key in `travel.py`. For production use, or if you face quota limits, replace it with your own API Key directly in `Project Files/travel.py`:
   ```python
   API_KEY = "YOUR_API_KEY_HERE"
   ```
   *(Alternatively, you can configure it securely using `st.secrets` or `.env` using `python-dotenv`)*

4. **Launch the Streamlit Application:**
   Run the app from the root directory:
   ```bash
   streamlit run "Project Files/travel.py"
   ```

5. **Start Exploring!**
   Open your browser at the provided localhost URL (usually `http://localhost:8501`), enter your desired destination and duration, and instantly generate your travel itinerary!
