---
type: "Journal Paper"
layout: publication
group: publications
title: "Constrained Optimization-Based Neuro-Adaptive Control (CONAC) for Unknown Systems Under Multiple Convex Input Constraints"
domestic_or_international: "International" # or "Domestic"
authors: # List of authors
  - name: "Myeongseok Ryu"
  - name: "Donghwa Hong"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
# preprint: 
  # - name: Techrxiv
  #   doi: "10.36227/techrxiv.172954216.68720680/v1"
  #   pdf: "/static/pub/2026-CONAC-Robot-Techrxiv.pdf"
  #   state: "published"
  #   year: "2026"
pub: 
  # - name: "IEEE Transactions on Systems, Man, and Cybernetics: Systems"
  - name: ____________________________
    # pub_url: "https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6221021"
    doi: 
    year: 
    pdf: "/static/pub/2026-CONAC.pdf"
    state: "submitted"  
    year: "2026"
pub_date: "2026-12-31" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2026-CONAC.png"
github: 
  - name: "CONAC"
    url: "KAIST-MIC-Lab/CONAC"
    description: "Code for the paper"
abstract: "
This study presents a constrained optimization-based neuro-adaptive control (CONAC) for a class of unknown multi-input-multi-output (MIMO) systems subject to multiple convex input constraints. 
A deep neural network (DNN) is employed to approximate the ideal control law while handling multiple convex input constraints within a unified constrained optimization framework.
The adaptive variables, including the DNN weights and Lagrange multipliers, are updated through adaptation law derived from the formulated constrained optimization problem, yielding Karush-Kuhn-Tucker (KKT) optimality conditions at equilibrium.
The controller's stability is rigorously analyzed using Lyapunov theory, establishing the uniform ultimate boundedness (UUB) of the tracking errors and adaptive variables.
The proposed controller is compared with existing methods through real-time experiments on a 2-degree-of-freedom (DOF) robotic manipulator, highlighting its superior capability to handle input constraints and its feasibility in real-time implementation.
  "
Youtube:
  - name: Demonstration Video
    url: kOMk1zkHoT4
# links:
#   - name: 
#     url: 
comments: "
  This work has been submitted to the IEEE for possible publication. Copyright may be transferred without notice, after which this version may no longer be accessible.
"
---