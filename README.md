# HNG 13 Stage 0 Task - Dynamic Profile Endpoint

This project is a simple RESTful API built with **Flask** for the **Backend Wizards Stage 0 Task**. It exposes a single endpoint `/me` that returns your profile information along with a dynamic cat fact fetched from the Cat Facts API.

---

## 🚀 Features

* Dynamic `/me` endpoint
* Fetches a random cat fact from [Cat Facts API](https://catfact.ninja/fact)
* Returns current UTC timestamp in ISO 8601 format
* Handles external API errors gracefully
* Configurable using environment variables

---

## 🛠️ Tech Stack

* **Language:** Python 3.x
* **Framework:** Flask
* **HTTP Client:** Requests

---

## 📂 Project Structure

```
backend-wizards-stage0/
│
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file in the project root and add your personal details:

```env
USER_EMAIL=your_email@example.com
USER_NAME=Olaiwon Ismail
USER_STACK=Python/Flask
```

These are used to populate the `user` field in your API response.

---

## 🧩 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Olaiwonismail/HNG-13-STAGE-0.git
cd backend-wizards-stage0
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the server

```bash
python app.py
```

The API will be available at:

```
http://127.0.0.1:5000/me
```

---

## 🧪 Example Response

```json
{
  "status": "success",
  "user": {
    "email": "email@example.com",
    "name": "Olaiwon Ismail",
    "stack": "Python/Flask"
  },
  "timestamp": "2025-10-15T23:45:21.123Z",
  "fact": "Cats sleep 70% of their lives."
}
```

---

## 📦 Dependencies

Listed in `requirements.txt`:

```
flask
requests
python-dotenv
```

Install all with:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Error Handling

* If the Cat Facts API is unreachable or times out, a fallback message is returned instead of a fact.
* Timeout for API requests is set to 5 seconds.

---


# HNG13-TASK-ZERO

