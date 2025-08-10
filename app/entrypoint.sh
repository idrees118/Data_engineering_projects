#!/bin/bash
set -e

echo "Waiting for PostgreSQL to start..."
sleep 5

echo "Running ETL script..."
python main.py
