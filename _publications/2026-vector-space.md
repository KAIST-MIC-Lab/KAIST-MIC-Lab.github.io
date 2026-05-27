---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Vector-Space Optimization Framework Based on Projected Contraction Condition for Control Design with Input Saturation" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Myeongseok Ryu"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
  - name: "Sesun You"
domestic_or_international: "International" # "International" or "Domestic"
# preprint: # Preprint information - REMOVE THIS FIELD IF NOT APPLICABLE!
#   - name: Techrxiv 
#     doi: "10.36227/techrxiv.173014412.26480551/v1"
#     year: 2024
    # pdf: "/static/pub/2025-all-wheel.pdf"
    # state: "published" # published, accepted, submitted
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Federation of Automatic Control (IFAC)"
    pdf: "/static/pub/2026-vector-space.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "accepted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-08-28" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2026-vector-space.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Conventional feedback control design based on contraction theory typically requires matrix-valued contraction metrics, which can limit real-time applicability as the system dimension increases and make direct handling of input saturation nontrivial.
  To address these issues, we project the contraction condition onto the instantaneous trajectory-error direction and introduce the metric-weighted error vector as the optimization variable.
  This yields a lower-dimensional formulation that avoids direct optimization over the full matrix-valued metric and enables input saturation constraints to be incorporated directly.
  Additionally, an energy-based constraint is introduced to resolve the scale ambiguity of condition-number minimization and maintain sufficient control effort.
  The effectiveness of the proposed method is validated through numerical simulations using the Lorenz system.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
comments: "
  **Prof. Sesun You** is Assistant Professor at Incheon National University, Incheon, South Korea.
  His biographical information can be found at [his Google Scholar profile](https://scholar.google.com/citations?user=QCJGLIwAAAAJ&hl=ko).
"
---