---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "CAR Planner: Constrained-Attention-Based Robust Imitation Learning for Autonomous Driving" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Jiyun Kim"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
preprint: # Preprint information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: Techrxiv 
    doi: "10.36227/techrxiv.175979328.80125117/v1"
    year: 2025
    pdf: "/static/pub/2025-car-planner.pdf"
    state: "published" # published, accepted, submitted
# pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
#   - name: IEEE International Conference on Robotics and Automation (ICRA)
#     doi: # Leave it blank if not applicable
#     vol: # Leave it blank if not applicable
#     num: # Leave it blank if not applicable
#     pp: # "380-385" # Leave it blank if not applicable
#     year: "2026" # Leave it blank if not applicable
#     state: "submitted" # published, accepted, submitted
pub_date: "2025-11-20" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-car-planner.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#   - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#     url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#     description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Imitation Learning (IL) has been widely applied to autonomous driving, but still suffers from shortcut learning, where policies rely on spurious correlations rather than causal driving behavior. This limits generalization and reduces robustness, defined here as the ability to sustain safe and reliable performance under distribution shifts and out-of-distribution (OOD) scenarios. We propose **CAR Planner**, which mitigates shortcut learning by enhancing the attention mechanism, widely adopted in recent planners, with a constrained optimization formulation. Specifically, we impose an **inequality constraint on the mean deviation of ego-state cross-attention weights** from a uniform distribution, and solve it using the Augmented Lagrangian Method (ALM). This regularizer discourages over-reliance on a few channels and promotes balanced state representations, with negligible training overhead and no inference-time cost. On the nuPlan benchmark, **CAR Planner** exhibits substantially less degradation when ego-state channels are reduced, providing strong evidence of robustness against shortcut reliance. Furthermore, it consistently outperforms both the baseline (without constraints) and state-of-the-art dropoutbased methods in challenging scenarios, while also producing smoother and more stable driving. These results highlight the effectiveness of CAR Planner in enabling **robust imitation learning** for autonomous driving.
"
Youtube:
  - name: Presentation Video
    representative: true
    url: 9s8VQOyphyA
---