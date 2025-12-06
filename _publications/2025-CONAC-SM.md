---
type: "Conference Paper"
layout: publication
group: publications
title: "Constrained Optimization-Based Neuro-Adaptive Control (CONAC) for Synchronous Machine Drives Under Voltage Constraints"
domestic_or_international: "International" # or "Domestic"
authors:
  - name: "Myeongseok Ryu"
  - name: "Niklas Monzen"
  - name: "Pascal Seitter"
  - name: "Kyunghwan Choi"
  - name: "Christoph M. Hackl"
    corresponding: true # true if this author is the corresponding author
preprint: 
  - name: Techrxiv
    doi: "10.36227/techrxiv.174585949.94234666/v1"
    pdf: "/static/pub/2025-CONAC-SM-Techrxiv.pdf"
    state: "published"
    year: "2025"
pub: 
  - name: Annual Conference of the IEEE Industrial Electronics Society (IECON)
    doi: "10.1109/IECON58223.2025.11221692"
    year: "2025"
    pp: "1-7"
    pdf: "/static/pub/2025-CONAC-SM-IECON.pdf"
    bib: "/static/pub/2025-CONAC-SM.bib"
    state: "published"
pub_date: "2025-10-14" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2025-CONAC-SM.png"
github: 
  - name: "CoNAC on SM"
    url: "KAIST-MIC-Lab/CONAC-on-SM"
    description: "Code for the paper (not public yet)"
abstract: "
  This paper presents a **constrained optimization-based neuro-adaptive control (CONAC)** for **nonlinear synchronous machines (SMs)** under **voltage constraints**, which allows to control the completely **unknown** electrical drive system, after a brief learning phase with very satisfactory control performance. 
  The artificial neural network (ANN) in the proposed neuro-adaptive controller (NAC) learns online and empowers the controller to handle parameter uncertainties. 
  Moreover, it solves a **constrained optimization problem** which allows to consider the nonlinear voltage constraints as well, by deriving the adaptation laws of the ANN's weights from the Lagrangian function.
  Boundedness of tracking error, convergence of the ANN weights, and satisfaction of the constraints are guaranteed by **Lyapunov theory**.  
  Numerical simulations in combination with a realistic (nonlinear) synchronous machine drive demonstrate the effectiveness and robustness against parameter and modeling uncertainties of the proposed NAC and its very acceptable constraints handling.
"
# links:
#   - name: 
#     url: 
comments: "
  **Prof. Christoph M. Hackl** is Professor at Hochschule München (HM), München, Germany.
  His biographical information can be found at [his Google Scholar profile](https://scholar.google.com/citations?user=LYhXm88AAAAJ&hl=ko).
"
---