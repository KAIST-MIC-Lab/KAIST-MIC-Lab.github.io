---
type: "Conference Paper"
layout: publication
group: publications
title: "Imposing a Weight Norm Constraint for Neuro-Adaptive Control"
authors:
  - name: "Myeongseok Ryu"
  - name: "Jiyun Kim"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # or "domestic"
preprint: 
  - name: Techrxiv
    doi: "10.36227/techrxiv.173014412.26480551/v1"
    pdf: "/static/pub/2025-imposing-Techrxiv.pdf"
    year: "2024"
    state: "published"
pub:
  - name: "European Control Conference (ECC)"
    doi: 10.23919/ECC65951.2025.11186942
    year: "2025"
    pp: "380-385"
    pdf: "/static/pub/2025-imposing-ECC.pdf"
    state: "published"
    pres: "/static/pub/2025-imposing-pres.pdf"
    bib: "/static/pub/2025-imposing.bib"
pub_date: "2025-06-30" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2025-imposing.png"
github: 
  - name: "CONAC/ECC25-weight-constraint"
    url: "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint"
    description: "Code for the paper"
abstract: "
  In this paper, a **neuro–adaptive controller** with weight norm constraints is proposed for uncertain Euler‒Lagrange systems. 
  The boundedness of the weights in the neuro–adaptive controller design is important to prevent excessively large control inputs and system instability. 
  To ensure the boundedness of the weights, the weight norm constraints are imposed as inequality constraints in the weight adaptation. 
  The adaptation law is derived based on the **constrained optimization method**. 
  The stability of the proposed controller is analyzed in the sense of **Lyapunov**, ensuring the **boundedness** of the tracking error and weight estimation. 
  For the comparative study, two benchmark controllers and the proposed controller were evaluated through a numerical simulation of a two-link manipulator system and compared in terms of tracking performance and parameter dependency. 
  The comparative study verified that the proposed controller has better tracking performance and lower parameter dependency.
"
# links:
#   - name: 
#     url: 
---