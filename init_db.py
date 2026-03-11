"""
Run once to create all database tables and seed sample data.
Usage:
    python init_db.py
"""
from app import app, seed_data
from models import db

with app.app_context():
    db.create_all()
    seed_data()
    print("✓ Database initialized with all tables.")
    print("✓ Sample data seeded (projects, skills, experience, education, blog, achievements).")
    print()
    print("─── Tables created ──────────────────────")
    print("  project, skill, experience, education")
    print("  message, blog_post, achievement, site_settings")
    print()
    print("─── Admin access ────────────────────────")
    print("  URL:      http://localhost:5000/admin")
    print("  Username: admin")
    print("  Password: admin123")
    print()
    print("  ⚠  Change ADMIN_USERNAME and ADMIN_PASSWORD in your .env before deploying!")
