# Mail-Assist

**Mail Assist** is a web-based application that helps users quickly summarize emails and generate draft replies in the same tone as the sender.



## Features

- Paste any email into a textarea and get an instant summary
- Generate a context-aware draft reply in the same tone as the original email
- Uses **Google gemma-3-1b-it** for AI-powered text generation

![alt text](https://github.com/Sahithi-03/Mail-Assist/blob/main/Screenshot%202025-09-25%20130632.png)



---

## Tech Stack

- **Backend**: FastAPI
- **Frontend**: HTML, Bootstrap, JavaScript
- **AI**: Google gemma-3-1b-it

---

## How It Works

1. User pastes the email into the textarea and clicks **Submit**.
2. FastAPI backend sends the input to **gemma-3-1b-it API**.
3. API returns a **summary** and a **draft reply** in the same tone as the email sender.
4. Results are displayed instantly on the frontend.

---

## Installation

```bash
git clone https://github.com/your-username/mail-assist.git
cd mail-assist
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
