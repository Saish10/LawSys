from __future__ import absolute_import, unicode_literals

import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "law_sys.configurations.settings"
)

# Initialize Celery app
app = Celery("law_sys")

# Celery configuration
app.conf.update(
    broker_url=os.environ.get("CELERY_BROKER_URL"),
    accept_content=["json"],
    task_serializer="json",
    result_serializer="json",
    timezone="UTC",
    broker_connection_retry_on_startup=True,
)

app.conf.task_default_queue = "default"
app.conf.task_queues = {
    "default": {
        "exchange": "default",
        "exchange_type": "direct",
        "binding_key": "default",
    },
    "small": {
        "exchange": "small",
        "exchange_type": "direct",
        "binding_key": "small",
    },
    "medium": {
        "exchange": "medium",
        "exchange_type": "direct",
        "binding_key": "medium",
    },
    "large": {
        "exchange": "large",
        "exchange_type": "direct",
        "binding_key": "large",
    },
}

# Load tasks from all registered Django app configs.
app.autodiscover_tasks()
