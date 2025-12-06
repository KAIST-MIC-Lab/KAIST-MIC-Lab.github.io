---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Online Physics-Informed Learning-Based Identification: Application to Adaptive MTPA Control of Synchronous Machines" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Seunghun Jang"
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
    pdf: "/static/pub/2025-online-physics.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2025-12-06" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-online-physics.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Machine parameters such as flux linkages and inductances play a key role in achieving optimal torque control of synchronous machines (SMs).
  However, it is challenging to identify these parameters online based on the SM model, which has complex and nonlinear characteristics.
  A fully connected feedforward neural network (NN) is a promising candidate owing to its capability to approximate complex nonlinear functions.
  Therefore, this study proposes an online physics-informed learning framework for identifying the parameters of SMs using an NN.
  The proposed method enables the NN-modeled flux linkages and inductances to be learned online in compliance with the governing physical laws of SMs.
  Consequently, the NN can more effectively capture the nonlinear characteristics of SMs within the constraints imposed by these governing physical laws.
  The learned parameters can be employed as online estimators and applied to online MTPA control.
  As a result, the effectiveness of the proposed method is validated through simulations conducted on a 35-kW interior permanent magnet synchronous motor (IPMSM) drive.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
---