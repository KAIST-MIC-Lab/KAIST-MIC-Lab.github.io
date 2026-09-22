---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Online Learning of Control-Oriented Lateral Tire-Force Maps for Vehicle MPC" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Donghwa Hong"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Workshop on Intelligent Systems (IWIS)"
    pub_url: "https://islab.ulsan.ac.kr/iwis2026/" # conference or journal URL (not your paper URL)
    pdf: 
    doi: "10.1109/IWIS70716.2026.11667752"
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: "1-4"
    year: "2026"
    state: "published" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-08-09" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2026-online-learning.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Vehicle model predictive control (MPC) repeatedly evaluates a tire-force model at predicted slip angles over its prediction horizon. Hence, an instantaneous force correction is insufficient: the learned object should be a reusable slip-angle-indexed map. This paper presents an online method that updates front and rear lateral tire-force maps from lateral–yaw state errors without direct tire-force measurements. A **neural identifier** supplies the instantaneous adaptation signal, while a predefined **slip-angle table** retains the learned relation over the previously excited domain. CarMaker simulations with changing tire characteristics and steering transitions show that the proposed method reduces trajectory force errors and frozen-horizon prediction errors compared with instantaneous and recent-window updates. The resulting compact model can be directly evaluated inside a vehicle MPC prediction horizon.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
# comments: "
#   **Christoph M. Hackl** is Professor at Hochschule München (HM), Munich, Germany.
#   His biographical information can be found at [his Google Scholar profile](https://scholar.google.com/citations?user=LYhXm88AAAAJ&hl=ko).
# "
---
