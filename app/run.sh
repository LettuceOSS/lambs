#!/bin/bash --login
conda activate lambs
uvicorn main:app --host 0.0.0.0 --port 80