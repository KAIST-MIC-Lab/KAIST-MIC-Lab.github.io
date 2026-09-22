---
type: "Journal Paper"
layout: publication
group: publications
title: "From Bellman Consistency toward Bellman Optimality: Constrained Online Critic Learning for Nonlinear Optimal Control"
domestic_or_international: "International" # or "Domestic"
authors: # List of authors
  - name: "Hyochan Lee"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
pub: 
  # - name: "IEEE Transactions on Systems, Man, and Cybernetics: Systems"
  - name: Withheld during double-blind review
    # pub_url: "https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=6221021"
    doi: 
    year: 
    pdf: "/static/pub/2026-from-bellman.pdf"
    state: "submitted"  
    year: "2026"
pub_date: "2026-12-31" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2026-from-bellman.png"
abstract: "
  This paper proposes a constrained online critic-learning method for discrete-time control-affine nonlinear systems that moves beyond policy-dependent Bellman residual reduction toward Bellman optimality. Because a small policy-dependent residual does not verify minimization over alternative controls, the method formulates online critic learning as a constrained optimization problem, with the one-step Bellman backup as the objective and Bellman consistency as an equality constraint. The resulting Lagrangian-based law updates the critic weights and Bellman multiplier from sampled transitions and uses the critic's state gradient for policy improvement. Lyapunov analysis establishes uniform ultimate boundedness of the learning errors. Real-world autonomous mobile robot experiments show that its trajectory root-mean-square error against an offline dynamic programming reference is 73.8% and 74.9% lower than those of one-step temporal-difference learning (TD(0)) and normalized adaptive dynamic programming, respectively. Complementary simulations show that its accumulated Bellman optimality residual over the evaluated state-error grid is 52.2% and 62.4% lower than those of the same methods, respectively. Additional learning reduces the residual along a newly encountered trajectory without substantially increasing it around the original trajectory.
  "
---