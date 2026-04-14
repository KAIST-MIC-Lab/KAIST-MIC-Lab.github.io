---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Online Constrained Reinforcement Learning for Optimal Tracking" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Hyochan Lee"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Federation of Automatic Control (IFAC)"
    pdf: "/static/pub/2026-online-constrained.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "1-6" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "accepted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-08-28" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2026-online-constrained.png" # Representative image of the paper
abstract: "
This paper presents a constrained online reinforcement learning framework for the optimal tracking control of constrained nonlinear systems. While reinforcement learning  provides powerful tools for optimal control, conventional implementations typically rely on unconstrained minimization strategies. Since this approach does not restrict the policy search space within the feasible region, it often drives the control policy toward unbounded actions, exacerbating the instability inherent in nonlinear function approximation. To address these issues, the proposed method reformulates the Bellman optimality equation as a constrained optimization problem where the control policy and value function are treated as joint decision variables. Crucially, this formulation allows for the explicit incorporation of system constraints directly into the learning process. A Lagrangian-based primal-dual scheme is then employed to find a Karush-Kuhn-Tucker solution, ensuring strict constraint satisfaction. Experimental validation on a differential-wheeled mobile robot demonstrates that the algorithm strictly enforces hard constraints during complex maneuvers while maintaining stable convergence of the value function."
---