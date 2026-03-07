import sys
import os

# Add the 'app' directory to sys.path so its internal modules can be imported
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app"))
)

# Import the Flask application instance
from interfaces.web import app

# Vercel requires an 'app' instance exported in the entrypoint file
