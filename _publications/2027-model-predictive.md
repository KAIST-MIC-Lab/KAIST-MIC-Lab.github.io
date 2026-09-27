---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Model Predictive Control for Active Rear Steering Without Sideslip-Angle Feedback" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Myeongseok Ryu"
  - name: "Soobin Hwang"
  # - name: "Donghyun Hwang"
  # - name: "Youngsik Yoon"
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
  - name: "American Control Conference (ACC)"
    pub_url: "https://acc2027.a2c2.org"
    pdf: "/static/pub/2027-model-predictive.pdf"
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
image: "/static/pub/2027-model-predictive.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  This paper proposes a model predictive control (MPC) method for active rear steering (ARS) that does not require sideslip-angle feedback.
  ARS control can improve vehicle maneuverability and lateral stability while preserving the driver's steering intention through the front wheels. 
  However, conventional ARS controllers commonly rely on the vehicle sideslip angle, which must be obtained through direct sensing or online estimation and may therefore introduce sensing or estimation errors into the feedback loop. 
  To eliminate this dependence, the proposed MPC employs two complementary mechanisms. 
  First, the yaw rate is predicted without using the sideslip angle by exploiting its limited influence on finite-horizon yaw-rate prediction under the considered operating conditions. 
  Second, sideslip-angle attenuation is promoted by suppressing a residual term in the sideslip-angle dynamics that is independent of the sideslip angle itself. 
  These two mechanisms enable the MPC optimization to be formulated using yaw-rate and steering signals without requiring measured or estimated sideslip-angle feedback. 
  Numerical simulations demonstrate that the proposed controller maintains satisfactory yaw-rate tracking and sideslip suppression while remaining insensitive to sideslip-angle feedback errors.
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