# 1. Create README.md
echo "# Playwright End-to-End Testing Framework (Python)

## 📌 Overview
This is a **Hybrid Playwright Automation Framework** built using:
- **Python**
- **Pytest**
- **Playwright**
- **Allure Reporting**
- **Loguru Logging**

It supports:
- Cross-browser testing (Chromium, Firefox, WebKit)
- Page Object Model (POM)
- Utility functions for test reusability
- Screenshot & logging integration
- Allure report with browser & category grouping

---

## 🚀 Setup & Run Guide

### 1️⃣ Clone the repository
\`\`\`bash
git clone https://github.com/pankaj200298/hybrid_playwrught_work.git
cd hybrid_playwrught_work
\`\`\`

### 2️⃣ Create virtual environment
\`\`\`bash
python -m venv .venv
\`\`\`

#### Activate the environment
- **Windows**
\`\`\`bash
.venv\Scripts\activate
\`\`\`
- **Mac/Linux**
\`\`\`bash
source .venv/bin/activate
\`\`\`

### 3️⃣ Install dependencies
\`\`\`bash
pip install -r requirements.txt
playwright install --with-deps
\`\`\`

### 4️⃣ Run tests
#### Run all tests (default: Chromium)
\`\`\`bash
pytest --alluredir=reports/allure-results
\`\`\`

#### Run tests on specific browser
\`\`\`bash
pytest --browser=firefox --alluredir=reports/allure-results
\`\`\`

#### Run only smoke tests
\`\`\`bash
pytest -m smoke --alluredir=reports/allure-results
\`\`\`

### 5️⃣ Generate Allure Report
\`\`\`bash
allure serve reports/allure-results
\`\`\`

---

## 📂 Project Structure
\`\`\`
.
├── tests/                     # Test cases
├── pages/                     # Page Object Model classes
├── utils/                     # Utility functions
├── reports/                   # Allure results & screenshots
├── conftest.py                 # Pytest fixtures
├── pytest.ini                  # Pytest configuration
└── requirements.txt            # Python dependencies
\`\`\`

---

## ✅ Features Implemented
- [x] Day 1: Basic Playwright test
- [x] Day 2: Utility functions (\`string_utils\`, \`file_utils\`, \`error_handler\`)
- [x] Allure report integration
- [x] Screenshot attachment in reports
- [x] Browser & category grouping in Allure

---

## 📌 Upcoming Enhancements
- Parallel cross-browser execution in CI
- GitHub Actions + Allure report deployment
- Playwright trace video attachment to reports
" > README.md

# 2. Create .gitignore
echo "# Python cache files
__pycache__/
*.pyc
*.pyo
*.pyd

# Virtual environment
.venv/
env/
venv/

# IDE files
.idea/
.vscode/

# Allure reports & Playwright outputs
reports/allure-results/
reports/allure-report/
playwright-report/
trace.zip

# Logs
*.log

# OS generated files
.DS_Store
Thumbs.db
" > .gitignore

# 3. Stage all changes
git add .

# 4. Commit changes
git commit -m "Day 2: Added README.md, .gitignore, and utility function updates"

# 5. Push to GitHub
git push origin main
