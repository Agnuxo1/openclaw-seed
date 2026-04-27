# 🌱 OpenCLAW SEED — Complete Autonomous AI Ecosystem

[![arXiv 2604.19792](https://img.shields.io/badge/related%20paper-arXiv%3A2604.19792-b31b1b.svg)](https://arxiv.org/abs/2604.19792)
[![Part of P2PCLAW](https://img.shields.io/badge/part%20of-P2PCLAW%20ecosystem-2ea44f.svg)](https://github.com/Agnuxo1/OpenCLAW-P2P)
[![License: Apache-2.0](https://img.shields.io/badge/license-Apache--2.0-blue.svg)](LICENSE)

> **Part of the P2PCLAW ecosystem.** This repository contains the *self-evolving*
> autonomous research agent — the SEED that progresses from SmolLM2-135M to
> Qwen2.5-7B+ via continuous LoRA training on harvested research data.
> For the full project overview, papers, and ecosystem map, see
> [**Agnuxo1/OpenCLAW-P2P**](https://github.com/Agnuxo1/OpenCLAW-P2P) (the front door).

## La Metáfora: De Semilla a Árbol

```
     🌱 GERMINATION (ahora)          🌿 SEEDLING              🌳 MATURE
     SmolLM2-135M                    Qwen2.5-0.5B             Qwen2.5-7B+
     442 datos                       2,000+ datos             10,000+ datos
     LoRA r=8                        LoRA r=16                LoRA r=64
     Aprende vocabulario             Razona sobre papers       Investiga autónomamente
```

## ✅ Sistemas Vivos (Verificados)

### 1. 🤖 Agente Social (24/7)
| Sistema | URL | Estado |
|---------|-----|--------|
| HuggingFace Space | https://agnuxo-openclaw-agent.hf.space | ✅ RUNNING |
| GitHub Actions (4h) | [Ver Actions](https://github.com/Agnuxo1/OpenCLAW-2-Autonomous-Multi-Agent-Scientific-Research-Platform/actions) | ✅ 6/8 exitosos |
| Moltbook | https://www.moltbook.com/u/OpenCLAW-Neuromorphic | ✅ API ACTIVA |
| NVIDIA LLM | 3 keys rotating | ✅ Generando contenido |

### 2. 🌱 Sistema SEED (Crecimiento Autónomo)
| Componente | Estado | Detalles |
|------------|--------|----------|
| Data Harvester | ✅ Operativo | 442 entradas, cosecha cada 6h |
| ArXiv Fetcher | ✅ 123 papers | Busca 10 temas de investigación |
| Semantic Scholar | ✅ 13 papers | Papers citados |
| GitHub Repos | ✅ 62 repos | 57 repos de Agnuxo1 |
| Bootstrap Data | ✅ 23 entradas | Conocimiento embebido sobre CHIMERA, NEBULA, etc. |
| Training Engine | ✅ Configurado | SmolLM2-135M → LoRA → merge → push |
| Evaluator | ✅ 10 benchmarks | Research, coherence, self-knowledge |
| Evolution | ✅ Selector | Natural selection of best models |
| Dataset HF | ✅ [Live](https://huggingface.co/datasets/Agnuxo/OpenCLAW-SEED-data) | 12 archivos, crece automáticamente |

### 3. 📂 Repositorio GitHub
- **Code**: https://github.com/Agnuxo1/OpenCLAW-2-Autonomous-Multi-Agent-Scientific-Research-Platform
- **36 archivos**: Agent + SEED + Workflows + Deploy configs
- **3 workflows**: Agent (4h), SEED Growth (6h), GPU Training
- **2 branches**: `main` (code), `seed-state` (persistent state)

## 🔄 Qué Hace Automáticamente (Sin Intervención)

```
Cada 1 hora (HF Space):
  └── Agente social → Lee Moltbook, busca posts relevantes

Cada 4 horas (GitHub Actions):
  └── Agente → Busca papers, publica en Moltbook, busca colaboradores

Cada 6 horas (GitHub Actions):
  └── SEED → Cosecha datos de ArXiv/Scholar/GitHub
  └── SEED → Prepara dataset de entrenamiento
  └── SEED → Sube datos a HuggingFace
  └── SEED → Genera scripts de training actualizados
  └── SEED → Evalúa modelos existentes
```

## 🏋️ Siguiente Paso: Entrenamiento con GPU

El sistema ya tiene **442 entradas de entrenamiento** — suficiente para el primer ciclo.

### Opción A: Kaggle (Recomendada — 30h GPU gratis/semana)
1. Ve a https://www.kaggle.com
2. Crea un nuevo Notebook
3. Importa `SEED_Training_Kaggle.ipynb` desde el dataset: https://huggingface.co/datasets/Agnuxo/OpenCLAW-SEED-data
4. En Settings → Add-ons → Secrets, añade `HF_TOKEN` = tu token
5. Activa GPU (T4)
6. ¡Run All! El notebook entrena, merge y publica automáticamente

### Opción B: Google Colab
1. Abre https://colab.research.google.com
2. Sube el notebook `SEED_Training_Kaggle.ipynb`
3. Cambia runtime a GPU
4. Ejecuta — el notebook funciona igual en Colab

### Opción C: HuggingFace AutoTrain
El sistema ya genera configuraciones AutoTrain automáticamente.

## 📊 Progresión del Modelo (Automática)

| Stage | Modelo | Datos Necesarios | Estado |
|-------|--------|-----------------|--------|
| GERMINATION | SmolLM2-135M | 100 ✅ (tenemos 442) | **LISTO PARA ENTRENAR** |
| SEEDLING | Qwen2.5-0.5B | 500 | ~2 ciclos más |
| SAPLING | Qwen2.5-1.5B | 2,000 | ~1 semana |
| YOUNG_TREE | Qwen2.5-3B | 5,000 | ~2 semanas |
| MATURE | Qwen2.5-7B | 10,000 | ~1 mes |

## 🔐 Seguridad
- ✅ Zero secrets in code (todo via GitHub Secrets + HF Space Secrets)
- ⚠️ **ROTA ESTAS CLAVES** (compartidas en texto plano):
  - GitHub token
  - Email passwords
  - API keys

## 🧬 Arquitectura del Código

```
openclaw-agent/
├── core/                    # Agente social autónomo
│   ├── agent.py            # Ciclo principal: research → post → engage → collab
│   ├── llm.py              # Multi-provider LLM (NVIDIA + fallbacks)
│   ├── config.py           # Configuración desde env vars
│   └── strategy.py         # Auto-análisis y mejora
├── seed/                    # 🌱 SEED — Sistema de crecimiento
│   ├── growth_engine.py    # Orquestador maestro (harvest → train → evaluate → evolve)
│   ├── data/harvester.py   # Cosechador autónomo de datos
│   ├── training/engine.py  # Motor de entrenamiento LoRA
│   ├── evaluation/evaluator.py  # Benchmarks automáticos
│   └── evolution/selector.py    # Selección natural de modelos
├── research/               # Fuentes de investigación
│   ├── arxiv_fetcher.py    # ArXiv real papers
│   └── web_scanner.py      # Semantic Scholar, HF models
├── social/                  # Plataformas sociales
│   └── moltbook.py         # Moltbook API client
├── seed_data/              # Datos de entrenamiento (crece solo)
│   ├── bootstrap_knowledge.jsonl  # Conocimiento semilla (23 entries)
│   ├── arxiv_training.jsonl       # Papers cosechados (123 entries)
│   ├── own_research.jsonl         # Nuestros repos (62 entries)
│   └── training_dataset.jsonl     # Dataset combinado (442 entries)
├── .github/workflows/
│   ├── agent.yml           # Agente social cada 4h
│   └── seed_growth.yml     # Crecimiento SEED cada 6h
├── app.py                  # Dashboard Gradio (HF Space)
├── Dockerfile              # Docker para HF Space
└── requirements.txt
```

## 🌍 La Visión

Este sistema es literalmente **una semilla de inteligencia artificial plantada en internet**:

1. **Nace pequeña** (135M parámetros) pero con conocimiento semilla sobre CHIMERA, NEBULA, y toda tu investigación
2. **Se alimenta sola** cosechando papers de ArXiv, Semantic Scholar, y tus repos
3. **Crece entrenándose** con LoRA en GPU gratis (Kaggle 30h/semana)
4. **Evoluciona** por selección natural — solo sobreviven los mejores modelos
5. **Se reproduce** publicando investigación y atrayendo colaboradores
6. **Escala** automáticamente a modelos más grandes cuando tiene suficientes datos

**No es un chatbot. Es un organismo digital que investiga, aprende, crece y busca colaboradores para la AGI.**

---
*Created by Francisco Angulo de Lafuente*
*Advanced AI Systems Laboratory, Madrid, Spain*
*https://github.com/Agnuxo1 | https://arxiv.org/search/cs?searchtype=author&query=de+Lafuente,+F+A*
