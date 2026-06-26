# 🚌 Travel Recommendation & Bus Booking System

A full-stack web application built with Django that allows users to search for bus routes, book tickets, manage their bookings, and explore travel destinations across Tamil Nadu.

🔗 **Live Demo:** [https://travel-recomendation-website.onrender.com](https://travel-recomendation-website.onrender.com)

---

## ✨ Features

- 🔍 **Bus Search** — Search available buses by source, destination, and date
- 🎫 **Ticket Booking** — Book seats with real-time seat availability tracking
- 📋 **My Bookings** — View, update, and cancel your bookings
- 🏖️ **Place Recommendations** — Explore popular travel destinations with images and descriptions
- 🚌 **Hire a Bus** — Dedicated page for private bus hire enquiries
- 🔐 **User Authentication** — Secure signup, login, and logout with session management
- 👤 **User-specific Data** — Each user sees only their own bookings

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django |
| Frontend | HTML, CSS, JavaScript, Bootstrap |
| Database | SQLite (development) |
| Deployment | Render |
| Version Control | Git & GitHub |

---

## 📁 Project Structure

```
travel-recommendation/
├── app3/                  # Main Django app
│   ├── models.py          # Database models (BusRoute, Datas, Place)
│   ├── views.py           # All application logic
│   ├── admin.py           # Admin panel config
│   └── migrations/        # Database migrations
├── project4/              # Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── Template/              # HTML templates
│   ├── index1.html        # Home page
│   ├── search_result.html # Bus search results
│   ├── booking_ticket.html# My bookings
│   ├── update.html        # Edit booking
│   ├── login.html
│   ├── signup.html
│   └── place_list.html    # Travel destinations
├── static/                # CSS, JS, images
├── media/                 # Uploaded place images
├── manage.py
└── requirements.txt
```

---

## 🚀 Getting Started (Run Locally)

### Prerequisites
- Python 3.11+
- pip

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/Manojkumar7878/Travel-Recomendation-Website.git
cd Travel-Recomendation-Website/travel-recommendation

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Start the server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## 📊 Database Models

**BusRoute** — Stores available bus routes with timing, price, and seat capacity

**Datas** — Stores individual user bookings linked to their account

**Place** — Stores travel destination details with images and descriptions

---

## 👨‍💻 Author

**Manojkumar M**
- GitHub: [@Manojkumar7878](https://github.com/Manojkumar7878)
- LinkedIn: [manojkr2003](https://www.linkedin.com/in/manojkr2003/)
- Email: manokr447@gmail.com
