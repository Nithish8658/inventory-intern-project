📘 Inventory Management System (Python)

A beginner-friendly Inventory Management System built using:

Python

Object-Oriented Programming (OOP)

JSON & CSV Persistence

Command-Line Interface (CLI)

pytest (Unit Testing)

Git & GitHub Workflow

This project was created as part of an internship assignment to demonstrate clean coding, project structuring, testing, and GitHub version control practices.

🚀 Features
🧩 Item Management

Add normal items

Add perishable items (with expiry date)

Validate price & quantity

Validate expiry date automatically

📦 Inventory Manager

Includes functions to:

Add items

Remove items

Update stock

Search by name

Search by category

Detect low-stock items

Calculate total inventory value

Get inventory summary

💾 Data Storage

Supports saving/loading inventory using:

JSON

CSV

🖥 Command-Line Interface (CLI)

Provides easy commands to:

List items

Add items

Update items

Save data

Load data

View summary

🧪 Automated Testing

Unit tests using pytest to ensure:

Items are added correctly

Low stock is detected

JSON save/load works properly

📁 Project Structure
Inventory_Project/
│
├── src/
│   └── inventory/
│        ├── __init__.py
│        ├── models.py
│        ├── manager.py
│        └── persistence.py
│
├── scripts/
│     └── demo_cli.py
│
├── tests/
│     └── test_manager.py
│
├── data/
│
├── README.md
├── DEV_LOG.md
├── requirements.txt
└── venv/

🛠 Installation
1️⃣ Clone the project
git clone https://github.com/Nithish8658/inventory-intern-project.git

2️⃣ Activate virtual environment

Windows:

venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

▶️ How to Run the CLI
List items
python scripts/demo_cli.py list

Add a new item
python scripts/demo_cli.py add

Search items
python scripts/demo_cli.py search --query Pen

Save to JSON
python scripts/demo_cli.py save_json --file data/inventory.json

Load from JSON
python scripts/demo_cli.py load_json --file data/inventory.json

🧪 Run Tests
pytest -q


Expected output:

3 passed

🔄 GitHub Workflow Summary

This project demonstrates:

Creating a repository

Using feature branches

Committing changes

Pushing to GitHub

Creating Pull Requests

Merging PRs into main

👤 Author

Nithish
Python & Data Science Learner
GitHub: https://github.com/Nithish8658