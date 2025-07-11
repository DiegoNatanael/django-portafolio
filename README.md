# 💻 Full-Stack Developer Portfolio

*A dynamic, full-stack portfolio and blog built from the ground up with Django and Python, designed to showcase a range of software development projects.*

<br>

<!-- Add your technology badges here. shields.io is a great resource. -->
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)

<br>

<!--
IMPORTANT: Create a high-quality GIF of you interacting with the live portfolio.
Show scrolling, the animations, and clicking to open the live demo modal.
Name it 'portfolio-demo.gif' and place it in a folder like 'assets/'.

<p align="center">
  <img src="[LINK_TO_YOUR_DEMO_GIF]" alt="Portfolio Demo GIF" width="90%">
</p>
-->

## 📖 About The Project

This repository contains the source code for my personal portfolio website, live at **[your-username].pythonanywhere.com**.

Unlike a simple static site, this project is a complete full-stack web application. It uses a Django backend to manage project data via a PostgreSQL database and a dynamic templating system to render the content. The frontend is built with vanilla HTML, CSS, and JavaScript, featuring modern, interactive animations to create an engaging user experience.

The primary goal was to build a robust and scalable platform for me to showcase my work, while also demonstrating my skills in backend architecture and full-stack development.

---

## ✨ Key Features

*   **Dynamic Project Management:** All project data (titles, descriptions, images, links) is stored in a database and managed through the built-in Django Admin panel. This allows me to add, update, or remove projects without touching the source code.
*   **Interactive UI:** The frontend is packed with animations and interactive elements, including:
    *   A live `particles.js` background on the hero section.
    *   A "typing" effect for the main headline using `Typed.js`.
    *   Graceful "fade-up" animations on all elements using `AOS.js`.
*   **Live Previews:** Features an embedded `<iframe>` to showcase a live, interactive version of my "Chaotic Password Generator" directly on the homepage. Other projects can be previewed in a pop-up modal window.
*   **Markdown Case Studies:** In-depth project detail pages are rendered from Markdown, allowing for rich formatting and easy content creation.
*   **Responsive Design:** The entire site is fully responsive and designed to work beautifully on devices of all sizes, from mobile phones to desktop monitors.

---

## 🛠️ Built With

This project integrates a robust backend with a carefully crafted frontend.

**Backend:**
*   **Python**
*   **Django** (for the core web framework and ORM)
*   **PostgreSQL** (for the production database)
*   **Markdown2** (for rendering case studies)

**Frontend:**
*   **HTML5**
*   **CSS3** (with Flexbox and Grid for layout)
*   **Vanilla JavaScript (ES6+)**
*   **Third-Party Libraries:** `particles.js`, `Typed.js`, `AOS.js`

**Deployment:**
*   Hosted on **PythonAnywhere**
*   Source code managed with **Git & GitHub**

---

## 🏁 Getting Started

To get a local copy up and running, follow these steps.

### Prerequisites

You will need Python 3.x and Pip installed on your machine.

### Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/DiegoNatanael/django-portafolio
    ```
2.  Navigate into the project directory:
    ```sh
    cd django-portafolio
    ```
3.  (Recommended) Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
4.  Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```
5.  Run the database migrations:
    ```sh
    python manage.py migrate
    ```
6.  Start the local development server:
    ```sh
    python manage.py runserver
    ```
7.  Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

*(Or choose the GPL license if you prefer)*

---

## 📬 Contact

Diego Natanael - Natanael1221.pythonanywhere.com

Project Link: https://github.com/DiegoNatanael/django-portafolio
