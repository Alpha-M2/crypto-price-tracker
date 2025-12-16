# Crypto Price Tracker

A production-style cryptocurrency price tracking system built with Python.  
The application fetches real-time cryptocurrency prices, exposes them via multiple interfaces (CLI and web), and supports automated price alerts via email.

This project is intentionally designed to demonstrate **real-world backend engineering practices**, not just API consumption.

---

## Overview

The Crypto Price Tracker is a modular Python application that:

- Fetches live cryptocurrency prices from a public API
- Displays prices via a CLI and a Flask web interface
- Monitors prices continuously in the background
- Triggers email alerts based on configurable thresholds
- Uses clean architecture, centralized configuration, and structured logging

The system is built incrementally with production considerations in mind: separation of concerns, fault tolerance, and extensibility.

---

## Key Features

- **Real-time price fetching** using the CoinGecko API
- **CLI interface** for continuous terminal-based monitoring
- **Background alert engine** with idempotent email notifications
- **Flask web dashboard** for live price viewing
- **Centralized configuration management**
- **Structured logging** for observability
- **Single entry point** for all execution modes

---

### Design Principles

- **Separation of concerns**  
Business logic is isolated from presentation layers (CLI / Flask).

- **Single execution contract**  
All modes are started through `main.py`.

- **Config-driven behavior**  
No hardcoded credentials or environment-specific values.

- **Fault tolerance**  
External service failures (API, SMTP) do not crash the system.

- **Extensibility**  The system can be extended with persistence, async I/O, or ML-based forecasting.

---

## Execution Modes

The application supports three execution modes:

### 1. CLI Mode
Continuously prints live cryptocurrency prices to the terminal.

```bash
python app/main.py --mode cli
```

### 2. Alert Monitor Mode
Runs a background monitoring loop that evaluates alert rules and sends email notifications when thresholds are crossed.

```bash
python app/main.py --mode alerts
```

### 3. Web Interface Mode
Starts a Flask web server displaying live prices and a health endpoint.

```bash
python app/main.py --mode web
```

---

### Configuration & Environment Variables

Configuration is centralized in config.py and loaded from environment variables.
.env.example

```bash env

ENV=development
LOG_LEVEL=INFO

EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password
EMAIL_RECEIVER=receiver_email@gmail.com
```
Gmail requires an App Password (normal passwords will not work).

---

### Setup Instructions

1. Clone the Repository

```bash
git clone <https://github.com/Alpha-M2/crypto-price-tracker.git>
cd crypto-price-tracker
```

2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

3. Install Dependencies
```bash
pip install -r requirements.txt
```

4. Configure Environment

```bash
cp .env.example .env
```
Edit .env with your credentials.

---

###  Why This Project Exists

This project was built to demonstrate:

Backend system design

Clean Python architecture

Incremental development with stable milestones

Integration with third-party APIs

Stateful background processing

Real-world operational debugging (SMTP auth, API failures)