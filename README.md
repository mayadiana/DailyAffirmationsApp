# Daily Affirmations Web App

**A Flask-based web application designed to boost mental well-being by providing daily positive affirmations and an interactive chat interface.**

This project demonstrates the integration of a Python backend with a responsive web frontend, showcasing clean routing, file I/O operations, and asynchronous communication.

## 🌟 Key Features

* **Daily Affirmations:** Randomly serves empowering messages from a curated collection stored in a flat-file database (`affirmations.txt`).
* **Interactive Chat Interface:** A dedicated chat component designed to provide a conversational experience.
* **Responsive Design:** A clean and modern user interface built with HTML5 and CSS3, ensuring a seamless experience across devices.
* **Asynchronous Interaction:** Implements a chat loop that handles user input and placeholder responses, ready for further AI integration.

## 🏗️ Technical Architecture

The application is built using a lightweight and efficient stack:

1. **Backend (Python & Flask):** Manages server-side logic, handling routes for the home page and chat interactions.
2. **Data Management:** Implements simple yet effective file reading to manage the affirmation library without the overhead of a heavy database.
3. **Frontend:**
    * **HTML5:** Defines the structure of the affirmation display and chat window.
    * **CSS3:** Custom styling for a "zen" and modern aesthetic.

## 💻 Tech Stack

* **Language:** Python
* **Framework:** Flask (Web Server)
* **Frontend:** HTML, CSS
* **Environment:** Developed using Visual Studio / Python Tools

## 🚀 Future Roadmap: AI Integration

The current architecture includes a **Chat Console** and specific routes (`/chat`) that serve as a foundation for integrating local LLMs or AI APIs. The infrastructure is prepared to transition from placeholder logic to a fully functional AI-driven affirmations assistant.

---
*Developed as a project to explore Python web development and interactive user experiences.*
