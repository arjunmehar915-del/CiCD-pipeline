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
├── .github/
│   └── workflows/
│       └── tests.yml       # GitHub Actions CI/CD pipeline
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

The `.github/workflows/tests.yml` defines 4 jobs:
1. `unit_tests` — runs unit tests
2. `integration_tests` — runs integration tests (needs unit to pass)
3. `e2e_tests` — runs e2e tests (needs integration to pass)
4. `publish_report` — deploys HTML reports to GitHub Pages (on `main`/`develop`)

## Test Count Summary

| Layer       | File                          | Tests |
|-------------|-------------------------------|-------|
| Unit        | test_validators.py            | 13    |
| Integration | test_login_inventory.py       | 9     |
| E2E         | test_flows.py                 | 11    |
| **Total**   |                               | **33**|
