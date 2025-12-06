---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Vector-Space Optimization for Contraction Theory-Based Control Design: An Energy-Based Effective Space Approach" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Myeongseok Ryu"
  - name: "Kyunghwan Choi"
  - name: "Sesun You"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
# preprint: # Preprint information - REMOVE THIS FIELD IF NOT APPLICABLE!
#   - name: Techrxiv 
#     doi: "10.36227/techrxiv.173014412.26480551/v1"
#     year: 2024
    # pdf: "/static/pub/2025-all-wheel.pdf"
    # state: "published" # published, accepted, submitted
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Federation of Automatic Control (IFAC)"
    pdf: "/static/pub/2025-vector-space.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2025-12-06" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-vector-space.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  In this paper, we propose a novel vector-space optimization framework for contraction theory-based control design with input saturation.
   Conventional Linear Matrix Inequality (LMI) optimization frameworks suffer from computational complexity issues for high-dimensional systems and limited flexibility in handling various constraints, including input saturation.
   Moreover, there exists ill-posed problem in the objective function minimizing the condition number of the contraction metric.
   To address these issues, we project the contraction metrics onto the trajectory error vector space, leading to a simplified vector-space optimization framework within a lower-dimensional effective space.
   Furthermore, energy-based constraints are incorporated to obtain a finite number of locally optimal solutions and to maintain sufficient control effort.
   In addition, convex input saturation constraints are integrated to handle the practical limitations of actuators.
   The effectiveness and feasibility of the proposed method are validated through numerical simulations using the Lorenz system.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
comments: "
  **Prof. Sesun You** is Assistant Professor at Keimyung University, Daegu, South Korea.
  His biographical information can be found at [his Google Scholar profile](https://scholar.google.com/citations?user=QCJGLIwAAAAJ&hl=ko).
"
---