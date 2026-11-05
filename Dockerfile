# Project: OpenCLAW SEED — Complete Autonomous AI Ecosystem
# Copyright (c) 2026 Francisco Angulo de Lafuente
# Author: Francisco Angulo de Lafuente
# ORCID: https://orcid.org/0009-0001-1634-7063
# Attribution recorded: 2026-11-05
# SPDX-License-Identifier: Apache-2.0

FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV STATE_DIR=/tmp/openclaw-state
ENV PORT=10000

EXPOSE 10000

CMD ["python", "server.py"]
