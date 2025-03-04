# CodeAlpha_secure-coding-review

This repository contains a Python web application built with Flask, created as part of a secure coding review assignment. The project demonstrates secure coding practices by identifying and analyzing common vulnerabilities using the Bandit static code analyzer.

## 📁 Files Included
- `app.py`: Main application code with intentional vulnerabilities.
- `requirements.txt`: Dependencies required to run the app.
- `bandit-report.html`: Detailed security analysis report generated by Bandit.
- `bandit-report.txt`: Summary of security vulnerabilities.
- `README.md`: Documentation for the project.

## 🔍 Security Analysis with Bandit
Bandit was used to identify the following vulnerabilities:
- **SQL Injection Risk:** Unparameterized SQL queries.
- **Hardcoded Secrets:** Sensitive information directly in code.
- **Insecure Input Handling:** Lack of validation.

## 🛠 How to Run the Application
1. **Clone the repository:**
   ```bash
   git clone https://github.com/YourGitHubUsername/secure-coding-assignment.git
   cd secure-coding-assignment
