---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "CAR Planner: Constrained-Attention-Based Robust Imitation Learning for Autonomous Driving" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Jiyun Kim"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
# preprint: # Preprint information - REMOVE THIS FIELD IF NOT APPLICABLE!
#   - name: Techrxiv 
#     doi: "10.36227/techrxiv.173014412.26480551/v1"
#     year: 2024
#     pdf: "/static/pub/2025-imposing-Techrxiv.pdf"
#     state: "published" # published, accepted, submitted
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  # - name: "IEEE Robotics and Automation Letters"
  - name: ______________________________
    pdf: "/static/pub/2026-CAR-Planner.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-04-26" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2026-CAR-Planner.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Imitation Learning (IL) for autonomous driving
  still suffers from shortcut learning, where policies rely on
  spurious correlations rather than causal driving behavior. In
  Transformer-based IL planners, such shortcut learning can
  appear as attention collapse, where attention weights become
  excessively concentrated on a small subset of input channels.
  This weakens robustness in challenging closed-loop scenarios.
  We propose CAR Planner, which mitigates shortcut learning by
  imposing a constrained optimization on ego-state cross-attention.
  The constraint penalizes only excessive concentration of attention
  weights, preserving task-driven channel-importance ordering
  while discouraging over-reliance on a few channels. On the
  nuPlan benchmark, CAR Planner shows substantially less degra-
  dation under ego-state channel reduction and achieves stronger
  closed-loop performance in challenging scenarios than strong
  baselines, with negligible training overhead and no inference-
  time cost. These results demonstrate that constrained attention
  is effective for robust imitation learning in autonomous driving.
"
# links: # additional links;
#   - name: 
#     url: 
# comments: 
#   **Christoph M. Hackl** is Professor at Hochschule München (HM), Munich, Germany.
#   His biographical information can be found at [his Google Scholar profile](https://scholar.google.com/citations?user=LYhXm88AAAAJ&hl=ko).
# 
---