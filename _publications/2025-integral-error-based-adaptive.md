---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Integral Error-Based Adaptive Neural Identifier for Nonlinear Lateral Tire Forces" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Donghwa Hong"
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
    pdf: "/static/pub/2025-integral-error-based-adaptive.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "accepted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-03-09" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-integral-error-based-adaptive.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
This paper presents an integral error-based adaptive neural identifier for online estimation of nonlinear lateral tire forces in vehicle dynamics. The adaptive law is derived from anexponentially weighted integral cost functional, which introduces a filtered error for weight updates and guarantees uniform ultimate boundedness of the estimation error, mitigating local overfitting inherent to instantaneous error-based schemes. To evaluate whether the network has learned a consistent, time invariant nonlinear mapping, a Frozen-Weight Reproducibility Test is introduced, in which past data are replayed using frozen neural network weights. Simulations under step-steer and slalom maneuvers show that the proposed identifier achieves real-time tire force estimation accuracy comparable to a conventional instantaneous error-based scheme, while significantly improving frozen-weight reproducibility and overall model consistency.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
comments: "

"
---