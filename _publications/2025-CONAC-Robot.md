---
type: "Journal Paper"
layout: publication
group: publications
title: "Constrained Optimization-Based Neuro-Adaptive Control (CONAC) for Euler-Lagrange Systems Under Weight and Input Constraints"
domestic_or_international: "International" # or "Domestic"
authors: # List of authors
  - name: "Myeongseok Ryu"
  - name: "Donghwa Hong"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
preprint: 
  - name: Techrxiv
    doi: "10.36227/techrxiv.172954216.68720680/v1"
    pdf: "/static/pub/2025-CONAC-Robot-Techrxiv.pdf"
    state: "published"
    year: "2024"
# pub: 
#   - name: IEEE Transactions on Systems, Man, and Cybernetics
#     doi: 
#     year: 
#     pdf: "/static/pub/2025-CONAC-Robot.pdf"
#     state: "submitted"  
pub_date: "2025-08-31" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2025-CONAC-Robot.png"
github: 
  - name: "CONAC"
    url: "KAIST-MIC-Lab/CONAC"
    description: "Code for the paper"
abstract: "
  This study presents a **constrained optimization-based neuro-adaptive control (CONAC)** for **unknown** Euler-Lagrange systems subject to **weight and convex input constraints**. A **deep neural network (DNN)** is employed to approximate the ideal stabilizing control law while simultaneously learning the unknown system dynamics and addressing both types of constraints within a **unified constrained optimization framework**. The adaptation law of DNN weights is formulated to solve the defined constrained optimization problem, ensuring satisfaction of **first-order optimality conditions** at steady state. The controller’s stability is rigorously analyzed using **Lyapunov theory**, guaranteeing bounded tracking errors and bounded DNN weights. The proposed controller is validated through a **real-time implementation** on a 2-DOF robotic manipulator, demonstrating its effectiveness in achieving accurate trajectory tracking while satisfying all imposed constraints.
"
Youtube:
  - name: Demonstration Video
    representative: true
    url: rplQZs3YBc8
# links:
#   - name: 
#     url: 
---