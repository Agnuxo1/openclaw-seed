# Project: OpenCLAW SEED — Complete Autonomous AI Ecosystem
# Copyright (c) 2026 Francisco Angulo de Lafuente
# Author: Francisco Angulo de Lafuente
# ORCID: https://orcid.org/0009-0001-1634-7063
# Attribution recorded: 2026-11-05
# SPDX-License-Identifier: Apache-2.0

"""
SEED — Self-Evolving Epistemic Dynamo
========================================
A self-growing AI system inspired by biological development.

Like an apple seed that becomes a tree, SEED starts as a tiny model
and autonomously grows through continuous learning, training, and evolution.

Growth Cycle (repeats forever):
    1. HARVEST: Collect knowledge from research, interactions, web
    2. CURATE:  Format into training datasets
    3. TRAIN:   Fine-tune with LoRA on free GPU (Kaggle/HF)
    4. MERGE:   Integrate adapter into base model
    5. EVALUATE: Test against benchmarks
    6. EVOLVE:  Keep best, mutate, repeat
    7. GROW:    Upgrade to larger base when ready

Author: Francisco Angulo de Lafuente
"""
__version__ = "1.0.0"
__codename__ = "Apple Seed"

STAGES = {
    "GERMINATION": "0.5B — Learning basic patterns",
    "SEEDLING":    "1B — Developing specializations",
    "SAPLING":     "3B — Growing knowledge branches",
    "YOUNG_TREE":  "7B — Producing useful outputs",
    "MATURE_TREE": "13B+ — Full autonomous research",
}
