---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "CARE Planner : Constrained Attention and Risk-aware Planning for Imitation based Autonomous Driving" # Title of the paper
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
    # pdf: "/static/pub/2025-all-wheel.pdf"
    # state: "published" # published, accepted, submitted
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Federation of Automatic Control (IFAC)"
    pdf: "/static/pub/2025-CARE-Planner.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2025-12-31" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-CARE-Planner.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Most imitation learning planners for autonomous driving are trained with
  displacement-based objectives such as average displacement error (ADE), which favor average
  accuracy but overlook how often predicted trajectories become unsafe. CARE Planner augments
  an attention-constrained Transformer with a Conditional Value at Risk (CVaR) based risk
  module that measures clearance-based tail risk along the prediction horizon. This risk is used
  both to select the supervised trajectory mode and to construct a tail-risk-aware soft target that
  downweights unsafe modes during multimodal learning. Compared to state-of-the-art planners
  such as PlanTF and our previous framework CAR Planner, CARE Planner outperforms overall
  performance and significant improvements in safety-related metrics on the nuPlan benchmark,
  highlighting the effectiveness of risk-aware training in enhancing the reliability of imitation
  learning planners.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
#comments: "
#  **Sesun You** is Assistant Professor at Keimyung University, Daegu, South Korea.
#  His biographical information can be found at [his Google Scholar profile](https://scholar.google.com/citations?#user=QCJGLIwAAAAJ&hl=ko).
#"
---