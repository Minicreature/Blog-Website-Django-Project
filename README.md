# Blog Website — Demo Project

**Author:** Aditya Khadkikar (Minicreature)
**Built / Iterated:** 2025-11-16

## Short summary
A simple Django blog built iteratively to demonstrate a clean development & release workflow.

## Project timeline (how this was built)
- **v1.0.0 — 2025-11-18** — Project scaffold: Django project + `blog` app, `Post` model, initial migration.
- **v2.0.0 — 2025-11-18** — Views & templates: post listing (home) & post detail.
- **v3.0.0 — 2025-11-18** — CRUD: create/update/delete posts, admin, auth.
- **v4.0.0 — 2025-11-18** — Styling (static CSS) and user-specific post listing.
- **v5.0.0 — 2025-12-04** — Social features (Like/Comment/Share), Inline editing, Public access.

## Quick run (local)
1. **Clone:**
   bash
   git clone git@github.com:Minicreature/Blog-Website-Djnango-Project.git
   cd Blog-Website-Djnango-Project

2. **Create & activate venv (Git Bash):**
   python -m venv venv
   source venv/Scripts/activate

3. **Install:**
   pip install -r requirements.txt

4. **Migrate & superuser:**
   python manage.py migrate
   python manage.py createsuperuser

5. **Run:**
   python manage.py runserver

6. **Visit:**
   Home- http://127.0.0.1:000/
   Admin- http://127.0.0.1:000/admin/
   Login- http://127.0.0.1:000/accounts/login/

## What's inside:
- blog/model.py - Post model (title, content, author, date_posted)
- blog/views.py - list/details and CRUD vievs
- blog/templates/blog/ - templates for pages
- blog/static/blog/main.css - project CSS

## Notes:
- Do not commit venv/ or db.sqlite3 — they are in .gitignore.
- Tags: v1.0.0, v2.0.0, v3.0.0, v4.0.0, v5.0.0.
