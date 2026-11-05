---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Online Adaptive Differentiable Predictive Control With Application to IPMSM MTPA Control" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Changeun Park"
  - name: "Seunghun Jang"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "IEEE International Transportation Electrification Conference & Expo, Asia-Pacific (ITEC-AP)"
    pub_url: "https://itec-ap2026.com"
    pdf: "/static/pub/2026-online-adaptive.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    # pres: "/static/pub/2026-vector-space-pres.pdf" # Leave it blank if not applicable
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-12-04" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
# pub_date: "2027-07-09" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2026-online-adaptive.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Nonlinear model predictive control (NMPC) handles nonlinear dynamics and constraints through repeated optimization, but its computational burden can limit high-frequency implementation. To alleviate the computational burden of real-time control while retaining online adaptability, this paper proposes an online adaptive differentiable predictive control (DPC) framework that updates a residual neural policy without offline pretraining or NMPC-generated targets. A baseline feedforward controller provides nominal control actions, allowing the residual neural network to focus on corrective actions. The residual policy is optimized directly using predictive-cost gradients from short rollouts initialized by recent operating samples. A differentiable HardNet-Aff layer is incorporated to enforce affine control constraints without relying on soft constraint-violation penalties. Control execution and policy learning are performed in separate processes to exclude backpropagation from the time-critical control path. The proposed framework is evaluated through interior permanent magnet synchronous motor (IPMSM) current-control simulations under repeated maximum torque per ampere (MTPA) references. Online adaptation, current-tracking performance, and computational efficiency are compared with acados-based NMPC under varying reference and model conditions.
"
---