# SauceDemo Test Suite

Playwright + pytest test suite for [saucedemo.com](https://www.saucedemo.com) covering unit, integration, and e2e tests.

## Project Structure

```
├── pages/                  # Page Object Models
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   ├── unit/               # Pure logic tests (no browser)
│   │   └── test_validators.py
│   ├── integration/        # Component interaction tests
│   │   └── test_login_inventory.py
│   └── e2e/                # Full user flow tests
│       └── test_flows.py
├── utils/
│   ├── config.py           # Centralized config via env vars
│   └── validators.py       # Reusable validation helpers
├── reports/                # Generated HTML reports
├── conftest.py             # Shared pytest fixtures
├── pytest.ini              # Pytest configuration
├── .env.example            # Environment variable template
├── .gitlab-ci.yml          # GitLab CI/CD pipeline
└── requirements.txt
```

## Setup

```bash
# 1. Create virtual environment
python -m venv .venv
source .venv/bin/activate        # Linux/macOS
.venv\Scripts\activate           # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Install Playwright browsers
playwright install chromium

# 4. Copy env file
cp .env.example .env
```

## Running Tests

```bash
# All tests
pytest

# By type
pytest tests/unit -m unit
pytest tests/integration -m integration
pytest tests/e2e -m e2e

# Run in parallel
pytest -n auto

# With visible browser (non-headless)
HEADLESS=false pytest tests/e2e
```

## CI/CD

The `.gitlab-ci.yml` defines 4 stages:
1. `install` — validates dependency installation
2. `unit` — runs unit tests
3. `integration` — runs integration tests
4. `e2e` — runs end-to-end tests
5. `report` — publishes HTML reports to GitLab Pages (on `main`/`develop`)

## Test Count Summary

| Layer       | File                          | Tests |
|-------------|-------------------------------|-------|
| Unit        | test_validators.py            | 13    |
| Integration | test_login_inventory.py       | 9     |
| E2E         | test_flows.py                 | 11    |
| **Total**   |                               | **33**|
