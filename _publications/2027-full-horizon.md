---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Full-Horizon Predictive Battery Thermal Management via Low-Dimensional Link-Costate Optimization" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  # Seunghun Jang1, Geunyoung Park2 and Kyunghwan Choi1
  - name: "Seunghun Jang"
  - name: "Geunyoung Park"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "American Control Conference (ACC)"
    pub_url: "https://acc2027.a2c2.org"
    pdf: "/static/pub/2027-full-horizon.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2027" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    # pres: "/static/pub/2026-vector-space-pres.pdf" # Leave it blank if not applicable
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-12-31" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
# pub_date: "2027-07-09" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2027-full-horizon.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "

Battery thermal management (BTM) requires long-range anticipation of future cooling demands because slow battery thermal dynamics make effective precooling dependent on distant driving conditions. Conventional model predictive control (MPC), however, must limit its prediction horizon for real-time implementation, which can delay cooling and lead to temperature constraint violations. This paper proposes a full-horizon predictive BTM strategy that incorporates the entire remaining driving information while retaining a low-dimensional online optimization problem. The future driving trajectory is segmented into links and represented by lumped driving parameters, and the BTM optimal control problem is reformulated as a quadratic program over link-wise costates rather than a high-dimensional cooling trajectory. This formulation enables anticipation of distant high-load conditions and continuous updating of the cooling plan over the remaining trip. Simulations with a nonlinear battery model demonstrate effective precooling and reduced temperature constraint violations. Compared with nonlinear model predictive control (NMPC) using a 200-s prediction horizon, the proposed method reduces cooling energy consumption by approximately 3.5% and the maximum temperature constraint violation from 1.419 °C to 0.245 °C. The average and maximum computation times are 20.24 ms and 96.55 ms, respectively, with all optimizations completed within the 1-s control interval.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
# comments: "
#   This work was supported in part by **Hyundai Motor Company (HMC)**.
#   **Mr. Donghyun Hwang** and **Mr. Youngsik Yoon** are research engineers at HMC, South Korea.
# "
---