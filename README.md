# 🚚 International Logistics & Delivery Fleet Audit Suite

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An automated financial ledger, fuel expense tracker, and interactive dashboard built specifically for dispatch companies, mini-logistics fleets, and delivery couriers.

This repository contains both the **Python-driven Streamlit web app** for live browser testing and the openpyxl source script for generating the offline **Microsoft Excel (`.xlsx`) and Google Sheets master templates**.

---

##  Key Features

- ** Daily Dispatch Ledger:** Tracks delivery fees, Cash-On-Delivery (COD) collections, and driver fuel allowances.
- ** Automatic Net Remittance Engine:** Computes exact cash expected from drivers after subtracting valid road expenses and tolls.
- ** Fleet Analytics:** Real-time visual breakdown of revenue vs. fuel burn per vehicle/courier.
- ** International Multi-Currency Ready:** Formatted for global SME operations (US, UK, EU, Africa).

---

##  Repository Layout

```text
logistics-fleet-log/
├── data/
│   └── Logistics_Fleet_Daily_Log_Master.xlsx
├── app.py              # Interactive Streamlit Web Engine
├── generator.ipynb     # Jupyter Notebook Excel Generation Script
├── requirements.txt    # Python dependencies
└── README.md           # Documentation & product overview

Master Template Access
For the offline Microsoft Excel master workbook or Google Sheets link:

👉 Buy Master Template on Gumroad

Built With
Python 3.10+

Streamlit

Pandas

OpenPyXL

Plotly

Author
Bamidele Adedeji

Founder & Principal Consultant, Dejifolakemi Enterprises

GitHub: @bamideleadedeji

Gumroad: Dejifolakemi Enterprises
