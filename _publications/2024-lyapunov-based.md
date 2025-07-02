---
type: "Journal Paper"
layout: publication
group: publications
title: "A Lyapunov-based approach to nonlinear programming and its application to nonlinear model predictive torque control"
authors: "<u>Kyunghwan Choi</u>, Christoph M Hackl&#42;"
domestic_or_international: "International" # or "Domestic"
preprint: 
  - name: Techrxiv
    doi: 10.36227/techrxiv.171085098.82768159/v1
    year: "2024"
    pdf: "/static/pub/2024-lyapunov-based.pdf"
    state: "published"
pub_date: "2024-03-14" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2024-lyapunov-based.png"
abstract: "
A tuning-parameter-free and matrix-inversionfree solution of nonlinear programming (NLP) problems is proposed. The key idea is to design an update law based on Lyapunov analysis to satisfy the first-order necessary conditions for optimality. To this aim, first, the Lyapunov function is defined as the summation of the norms of these conditions. Then, the desired optimization variables and Lagrange multipliers, which minimize the Lyapunov function the most, are found analytically, thereby rapidly approaching the necessary conditions. The proposed method neither requires tuning parameters nor matrix inversions; thus, it can be implemented easily with less iterations and computational load than conventional methods, such as sequential quadratic programming (SQP) and augmented Lagrangian method (ALM). The effectiveness of the proposed method is applied to and validated by using it to solve a nonlinear model predictive torque control (NMPTC) problem in electrical drives. The results are compared with those of SQP and ALM.
"
# links:
#   - name: 
#     url: 
---