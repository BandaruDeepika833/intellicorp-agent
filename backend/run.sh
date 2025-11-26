#!/bin/bash
source /home/ar-in-u-078/intellicorp-agent/backend/venv/bin/activate
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
