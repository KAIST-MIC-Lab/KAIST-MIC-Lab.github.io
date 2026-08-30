---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Model-Adaptive Predictive Torque Control of IPMSMs for Online Optimal Operation: A Lookup-Table-Free Approach" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Jongseok Kim"
  - name: "Kyunghwan Choi"
  - name: "Youngseok Lee"
  - name: "Ki-Bum Park"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "IEEE Transactions on Transportation Electrification (Early Access)"
    pdf: # "/static/pub/2026-vector-space.pdf"
    doi: 10.1109/TTE.2026.3695345 # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
    pres: # "/static/pub/2026-vector-space-pres.pdf" # Leave it blank if not applicable
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-05-20" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2026-model-adaptive.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Interior permanent magnet synchronous machines (IPMSMs) are characterized by nonlinear torque-current relationships, voltage and current constraints, and parameter variations. However, most optimal torque control methods assume that machine parameters are accurately known. Conversely, existing robust control methods fail to seamlessly integrate all optimal strategies, such as maximum torque per ampere, flux weakening, maximum current, and maximum torque per voltage. This paper proposes an extended state observer-based predictive torque control (ESO-PTC) for IPMSMs that encompasses all optimal strategies while ensuring robustness to variations in inductance and flux-linkage. The conventional dynamic equations and flux-linkage lookup tables are replaced with the ultra-local model and flux-linkage estimator, respectively. The constrained optimal torque control problem is reformulated using the augmented Lagrangian method and solved online with a finite control set approach. The ESO-PTC is computationally efficient, allowing for real-time implementation on a general-purpose off-the-shelf processor. The effectiveness of the proposed method is validated through both experimental results and numerical simulations.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
# comments: "
#   **Prof. Sesun You** is Assistant Professor at Incheon National University, Incheon, South Korea.
#   His biographical information can be found at [his Google Scholar profile](https://scholar.google.com/citations?user=QCJGLIwAAAAJ&hl=ko).
# "
---