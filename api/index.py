"""Vercel Python Function entrypoint for the Flask application."""

import os

# Vercel functions are short-lived. Keep background schedulers and startup
# warmups disabled; scheduled work should be moved to Vercel Cron separately.
os.environ.setdefault("ENABLE_SCHEDULER", "0")
os.environ.setdefault("ENABLE_STARTUP_BACKTEST_WARMUP", "0")
os.environ.setdefault("ENABLE_STARTUP_ML_WARMUP", "0")

from app import app  # noqa: E402,F401
