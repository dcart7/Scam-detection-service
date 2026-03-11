# Scam-detection-service

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Export Postgres env vars in your shell:

```bash
export POSTGRES_DB=scam_detection
export POSTGRES_USER=scam_detection
export POSTGRES_PASSWORD=your_password
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the server:

```bash
python manage.py runserver
```
