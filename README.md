# Chatbot for FAQs

## Overview

This project is a versatile chatbot application designed to answer frequently asked questions (FAQs) using data sourced from an Excel file. The chatbot is implemented in both a desktop application using Tkinter and a web application using Flask, providing users with an interactive and user-friendly experience.

## Features

### 1. Data-Driven Responses
- The chatbot loads FAQ data from an Excel file, ensuring accurate and relevant answers.
- It checks for the presence of "Question" and "Answer" columns to maintain data integrity.

### 2. Flexible Search Functionality
- Users can input their questions, and the chatbot employs both exact and partial matching to find the best possible answer.
- If an exact match isn't found, it suggests related questions to guide users.

### 3. User-Friendly GUI
- The desktop application features an intuitive interface where users can easily enter their questions, view answers, and explore suggested questions.
- Built with Tkinter, the GUI is designed for simplicity and ease of use.

### 4. Web Application Integration
- The Flask-based web application offers a seamless chat experience.
- Users can enter their names to personalize the interaction, and the chatbot responds dynamically to their queries through AJAX requests.

### 5. Dynamic Suggestions
- The chatbot provides five random suggested questions, allowing users to explore common inquiries without needing to type them out.
- As users type their questions, the chatbot can filter and suggest relevant questions based on their input.

### 6. Session Management
- The web application includes session management, greeting users by name and maintaining a personalized chat experience throughout their interaction.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ammaremad/chatbot-for-faqs.git
   cd chatbot-for-faqs
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have an Excel file named `FAQ_data.xlsx` with "Question" and "Answer" columns in the specified path.

## Running the Application

### Desktop Application
- Run the Tkinter application:
  ```bash
  python chatbot_tkinter.py
  ```

### Web Application
- Run the Flask application:
  ```bash
  python chatbot_flask.py
  ```
- Open your web browser and navigate to `http://127.0.0.1:5000` to access the chatbot.

## Usage

- For the desktop application, enter your question in the input field and click the "Search" button to get an answer.
- For the web application, enter your name to start the chat, type your question, and click "Send" to receive an answer.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.


## Acknowledgments

- Special thanks to the libraries used in this project: Tkinter, Flask, and Pandas.
- Thanks to the community for their support and feedback.

---

Feel free to modify this README file as needed to better fit your project's specifics and your personal style!
