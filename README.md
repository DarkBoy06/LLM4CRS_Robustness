# LLM4CRS Robustness

Robustness Analysis of LLM-Based Conversational 
Recommender Systems using RobustExplain Metrics.

## Overview
This repository contains the experimental code for 
evaluating the robustness of ChatCRS (Li et al., 2025) 
under realistic user behavior perturbations, adapted 
from the RobustExplain framework (Zhang et al., 2026).

## Perturbations Evaluated
- Noise Injection
- Temporal Shuffle  
- Entity Corruption
- Missing Values

## Key Results
| Perturbation | Overall Score |
|---|---|
| Noise Injection | 0.420 |
| Temporal Shuffle | 0.432 |
| Entity Corruption | 0.430 |
| Missing Values | 0.399 |
| **Average** | **0.420** |
| RobustExplain Baseline | 0.500 |

## Requirements
- Python 3.10+
- Groq API key (free at console.groq.com)
- Google Colab recommended

## Dataset
DuRecDial 2.0 (English subset) — 50 dialogues

## References
- Li et al. (2025) ChatCRS — NAACL 2025
- Zhang et al. (2026) RobustExplain — WWW 2026
