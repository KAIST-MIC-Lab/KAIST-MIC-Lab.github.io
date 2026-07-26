---
type: "Conference Paper"
layout: publication
group: publications
title: "Constrained Optimization Formulation of Bellman Optimality Equation for Online Reinforcement Learning"
krtitle: "온라인 강화학습을 위한 벨만 최적 방정식의 제약 최적화 문제"
authors:
  - name: "Hyochan Lee"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "Domestic"
pub:
  - name: 제어로봇시스템학회 (ICROS)
    doi:
    year: "2026"
    pdf: "/static/pub/2026-constrained-optimization-bellman.pdf"
    state: "accepted"
pub_date: "2026-07-01" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2026-constrained-optimization-bellman.png"
abstract: "
This paper proposes a constrained optimization-based reinforcement learning (RL) method to enhance learning stability for discrete-time nonlinear systems. To address the oscillatory convergence and hyperparameter sensitivity of conventional Adaptive Dynamic Programming (ADP), the Bellman Optimality Equation (BOE) is reformulated as a constrained optimization problem. By treating the control policy and critic weights as simultaneous decision variables and enforcing the BOE as an equality constraint, the framework ensures consistent optimality throughout the learning process. Online update laws are derived from the Karush-Kuhn-Tucker (KKT) conditions within a Lagrangian framework to seek the optimal solution in real time. The proposed approach demonstrates improved convergence and robustness over standard RL-based control methods.
"
---

