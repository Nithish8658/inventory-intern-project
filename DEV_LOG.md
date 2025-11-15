# 📙 Development Log (DEV_LOG.md)

This document records the day-by-day development progress of the **Inventory Management System** project.

---

## ** Project Setup**
- Installed Python and set up VS Code  
- Created project folders (`src`, `inventory`, `scripts`, `tests`)  
- Created virtual environment (`venv`)  
- Added placeholder Python files  
- Installed required packages  

---

## ** Models Development**
- Implemented `Item` class  
- Implemented `PerishableItem` class  
- Added validation for price, quantity, and expiry date  
- Added function to check if an item is expired  

---

## ** Inventory Manager**
- Implemented `InventoryManager` class  
- Added functions:  
  - add_item  
  - remove_item  
  - update_quantity  
  - search_by_name  
  - search_by_category  
  - low_stock  
  - total_value  
  - summary  
- Tested functions manually  

---

## **Persistence Layer**
- Created `persistence.py`  
- Implemented saving & loading to/from JSON  
- Implemented saving & loading to/from CSV  
- Verified JSON/CSV files are created successfully  

---

## **CLI (Command Line Interface)**
- Created `demo_cli.py`  
- Added argparse commands:  
  - list  
  - add  
  - update  
  - search  
  - save_json  
  - load_json  
  - summary  
- Tested CLI commands (add, list, save, load, etc.)  

---

## ** Testing with Pytest**
- Wrote test cases in `test_manager.py`  
- Test coverage includes:  
  - Adding items  
  - Low stock detection  
  - JSON save + load  
- All tests passed successfully (`3 passed`)  

---

## **Git & GitHub Workflow**
- Initialized Git inside project  
- Made commits  
- Pushed project to GitHub  
- Created a feature branch  
- Created a Pull Request  
- Merged Pull Request into main  
- Cleaned up repository  

---

## ** Documentation**
- Wrote complete `README.md`  
- Wrote `DEV_LOG.md`  
- Verified project structure  
- Final testing completed  

---

# ✔ Project is fully complete and ready for submission.
