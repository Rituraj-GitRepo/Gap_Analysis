# JSW Motors — Competency & TNA Survey Portal

Django MVP for Competency Mapping and TNA surveys across 9 functions at JSW Motors.

## Features
- Welcome portal with role-based routing (GET/MT → Self-Assessment, FH → Prioritisation)
- 9 functions · 118 KPI-aligned competencies from the Functional Scorecard
- Functional Head Survey: rate importance, select Top 10, set Day-1 level
- Employee Self-Assessment: rate current proficiency (GET/MT)
- Admin Dashboard: view all responses, delete individual records, export Excel
- Gap Analysis: interactive charts (importance, Top 10, gap, severity, radar)

## Deploy to Railway

```bash
# 1. Push to GitHub
git init && git add . && git commit -m "init"
git remote add origin https://github.com/YOUR_USERNAME/jsw-tna-portal.git
git push -u origin main

# 2. railway.app → New Project → Deploy from GitHub
#    Add a PostgreSQL database service

# 3. Set environment variables in Railway dashboard:
SECRET_KEY=<generate a long random string>
DATABASE_URL=<auto-filled by Railway PostgreSQL plugin>
ADMIN_USERNAME=admin
ADMIN_PASSWORD=JSW@Admin2026
DEBUG=False
```

`railway.toml` auto-runs `pip install`, `collectstatic`, and `migrate` on every deploy.

## Run Locally

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # edit SECRET_KEY
python manage.py migrate
python manage.py runserver
```

Admin login: `/admin-login/` · default: `admin` / `JSW@Admin2026`
