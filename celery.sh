#!/bin/bash
python3 -m celery -A task worker -B --loglevel=info