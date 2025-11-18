# Piyu's Kitchen - Authentic Indian Cuisine Startup Script
# This script activates the virtual environment and starts the Flask server

Write-Host "Starting Piyu's Kitchen..." -ForegroundColor Green
Write-Host "Authentic Indian Cuisine 🍛" -ForegroundColor Yellow

# Activate virtual environment
& .\venv\Scripts\Activate.ps1

# Set absolute database path
$env:DATABASE_URL = "sqlite:///C:/Users/Piyu/Downloads/Expirement/database.db"

# Start Flask application
Write-Host "`nFlask server starting at http://127.0.0.1:5000" -ForegroundColor Cyan
Write-Host "Press CTRL+C to stop the server`n" -ForegroundColor Yellow

python run.py
