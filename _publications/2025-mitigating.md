---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Mitigating Attention Collapse via Mean-Deviation Constrained Optimization" # Title of the paper
domestic_or_international: "International" # "International" or "Domestic"
authors: 
  - name: "Jiyun Kim"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
preprint: # Preprint information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: Techrxiv 
    doi: "10.36227/techrxiv.175877819.93334616/v3"
    year: 2025
    pdf: "/static/pub/2025-mitigating.pdf"
    state: "published" # published, accepted, submitted
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Conference on Robot Intelligence Technology and Applications (RiTA)"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2025" # Leave it blank if not applicable
    state: "accepted" # published, accepted, submitted
pub_date: "2025-12-31" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-mitigating.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#   - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#     url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#     description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Attention mechanisms are widely used in deep learning to compute contextual representations, but they are prone to collapse when attention weights concentrate excessively on a few tokens, potentially degrading model performance. We propose an **Mean-Deviation Constrained Attention (MDCA)**, an optimization-based attention mechanism that constrains the mean-deviation of attention weights to **mitigate attention collapse**. The constraint is formulated as an inequality condition and is efficiently handled using the Augmented Lagrangian Method (ALM), enabling explicit control over attention concentration. Unlike heuristic approaches such as dropout or temperature scaling, our method introduces a principled regularization framework grounded in constrained optimization. We evaluate the proposed method on two tasks: (i) selective attention for **handwriting classification using the Badge-MNIST dataset**, in comparison with standard baselines including vanilla attention, entropy regularization, and temperature scaling; and (ii) **imitation learning on the nuPlan dataset**, compared with a representative state-of-the-art planner. On Badge-MNIST, our method improves attention selectivity and accuracy across seeds. On nuPlan, it yields safety driving in reactive closed loop and openloop evaluation while maintaining modest.
"
# links: # additional links;
#   - name: 
#     url: 
---
