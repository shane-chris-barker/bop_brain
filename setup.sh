#!/bin/bash

set -e
echo "🔧 Starting Bop Brain setup..."
echo "🔄 Updating package list..."
sudo apt update

echo "📦 Installing system packages..."
sudo apt install -y \
    python3-venv \
    python3-pip \
    mosquitto \
    mosquitto-clients

echo "🐍 Setting up Python venv (if not already present)..."
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi
echo "📡 Activating venv and installing Python packages..."

source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✅ Bop Brain environment is ready!"