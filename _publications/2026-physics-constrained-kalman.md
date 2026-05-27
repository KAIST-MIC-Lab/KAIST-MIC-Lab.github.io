---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Physics-Constrained Kalman Filtering for Wheel Normal Load Estimation Using Suspension and IMU Measurements" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Angus Siegloff"
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
  - name: "IEEE Transactions on Vehicle Technology"
    pdf: "/static/pub/2026-physics-constrained-kalman.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-05-27" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2026-physics-constrained-kalman.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  This paper presents a physics-constrained Kalman filtering approach for estimating individual wheel normal loads using suspension and inertial measurement unit (IMU) measurements. The proposed method combines suspension-based wheel-load pseudo-measurements with IMU-based rigid-body equilibrium relations. These relations, including vertical-force, pitch-moment, and roll-moment equilibrium, are incorporated as probabilistic physical constraints, enabling the estimator to retain local sensitivity to suspension-induced load variations while enforcing global physical consistency in the wheel-load distribution. Spring, asymmetric damper, anti-roll-bar, and aerodynamic effects are included to improve the fidelity of the pseudo-measurements and constraints. The method is validated in IPG CarMaker under diverse driving scenarios, including the ISO double lane change, Nürburgring, and Hockenheim, and is compared with algebraic, quasi-static, suspension-only, and literature-based observer methods. The results demonstrate that the proposed method provides the most consistent overall performance across transient and full-lap conditions, while ablation studies confirm the dominant role of the physics-based constraint update in robust estimation.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
# comments: "
#   **Prof. Sesun You** is Assistant Professor at Keimyung University, Daegu, South Korea.
#   His biographical information can be found at [his Google Scholar profile](https://scholar.google.com/citations?user=QCJGLIwAAAAJ&hl=ko).
# "
---