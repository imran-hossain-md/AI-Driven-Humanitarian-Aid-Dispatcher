@echo off
mkdir app\api\endpoints app\core app\models app\services\ai_engine app\workers app\db\repositories app\utils logs tests\unit tests\integration tests\fixtures scripts

type nul > app\__init__.py
type nul > app\main.py
type nul > app\api\__init__.py
type nul > app\api\dependencies.py
type nul > app\api\endpoints\__init__.py
type nul > app\api\endpoints\logistics.py
type nul > app\api\endpoints\health.py
type nul > app\api\endpoints\audit.py
type nul > app\core\__init__.py
type nul > app\core\config.py
type nul > app\core\logging.py
type nul > app\core\exceptions.py
type nul > app\core\security.py
type nul > app\core\constants.py
type nul > app\models\__init__.py
type nul > app\models\schemas.py
type nul > app\models\domain.py
type nul > app\models\audit.py
type nul > app\services\__init__.py
type nul > app\services\logistics_service.py
type nul > app\services\audit_service.py
type nul > app\services\ai_engine\__init__.py
type nul > app\services\ai_engine\pathfinder.py
type nul > app\services\ai_engine\demand_forecast.py
type nul > app\services\ai_engine\terrain_analyzer.py
type nul > app\workers\__init__.py
type nul > app\workers\celery_app.py
type nul > app\workers\tasks.py
type nul > app\workers\worker_monitor.py
type nul > app\db\__init__.py
type nul > app\db\redis_client.py
type nul > app\db\postgres.py
type nul > app\utils\__init__.py
type nul > app\utils\validators.py
type nul > app\utils\helpers.py
type nul > logs\app.log
type nul > logs\audit_trail.log
type nul > logs\celery_worker.log
type nul > scripts\render-build.sh
type nul > scripts\entrypoint.sh
type nul > .env.example
type nul > .gitignore
type nul > docker-compose.yml
type nul > Dockerfile
type nul > Procfile
type nul > requirements.txt
type nul > README.md
type nul > render.yaml

echo Project structure created successfully!
pause