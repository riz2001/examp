#!/usr/bin/env bash
# Build React frontend
cd frontend
npm install
npm run build
cd ..

# Install Python dependencies
pip install -r requirements.txt
