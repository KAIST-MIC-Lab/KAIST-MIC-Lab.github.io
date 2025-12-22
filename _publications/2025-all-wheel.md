---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "All-Wheel Steering Vehicle Control Based on Contraction Theory with Neural Network" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Myeongseok Ryu"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
# preprint: # Preprint information - REMOVE THIS FIELD IF NOT APPLICABLE!
#   - name: Techrxiv 
#     doi: "10.36227/techrxiv.173014412.26480551/v1"
#     year: 2024
    # pdf: "/static/pub/2025-all-wheel.pdf"
    # state: "published" # published, accepted, submitted
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "IEEE International Conference on Advanced Motion Control (AMC)"
    pdf: "/static/pub/2025-all-wheel.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "accepted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-03-09" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-all-wheel.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  All-wheel steering (AWS) vehicles have been widely studied in the literature to enhance stability and maneuverability.
  In this study, we propose a contraction theory-based AWS vehicle control strategy integrated with neural networks (NNs).
  Contraction theory is a powerful tool for designing controllers for nonlinear systems, ensuring the incremental exponential convergence of all system trajectories to a unique trajectory, regardless of initial conditions.
  However, control performance may degrade due to system uncertainties.
  To address this issue, NNs are employed to approximate and compensate for these system uncertainties.
  The contraction property is guaranteed by formulating Linear Matrix Inequalities (LMIs) to obtain the contraction metric.
  Furthermore, the adaptation law for the NN weights is designed using Lyapunov theory to ensure the stability of the closed-loop system.
  Finally, numerical simulation results are provided to validate the proposed control strategy.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
---