---
type: "Conference Paper"
layout: publication
group: publications
title: "Constrained Optimization Formulation of Bellman Optimality Equation for Online Reinforcement Learning" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Hyochan Lee"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Conference on Robot Intelligence Technology and Applications (RiTA)"
    pdf: "/static/pub/2025-constrained-optimization.pdf"
    year: "2025" # Leave it blank if not applicable
    state: "accepted" # published, accepted, submitted
pub_date: "2025-12-16" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-constrained-optimization.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  This paper proposes an online reinforcement learning algorithm that directly solves the Bellman optimality equation by casting it as a constrained optimization problem. Unlike policy or value iteration, which incrementally approximate the Bellman (optimality) equation, the method treats the value function and control policy as joint decision variables and solves them simultaneously. The formulation also permits systematic incorporation of additional constraints, such as input or safety limits. Direct solution of the Bellman optimality equation enables coordinated value–policy updates that stabilize online adaptation. Explicit constraint handling ensures per-step feasibility in online settings. The problem is addressed using a Lagrangian-based primal–dual approach, resulting in online update laws that drive the Bellman error toward zero while satisfying all constraints. The effectiveness of the method is demonstrated on a constrained nonlinear optimal control task.
"
---