---
type: "Conference Paper"
layout: publication
group: publications
title: "LMI-based Neural Network Observer for State and Nonlinearity Estimation"
authors:
  - name: "Yeongho Jeong"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # or "domestic"
pub:
  - name: Annual Conference of the IEEE Industrial Electronics Society (IECON)
    doi: "10.1109/IECON58223.2025.11221827"
    year: "2025"
    pdf: "/static/pub/2025-LMI-based-neural.pdf"
    pp: "1-7"
    state: "published"
pub_date: "2025-10-14" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2025-LMI-based-neural.png"
abstract: "
  This paper proposes a design method for linear matrix inequality (LMI)-based neural network (NN) observer gain in discrete-time domain. The proposed scheme employs an NN with a single hidden layer to approximate the lumped nonlinear term which includes uncertainties. A Lyapunov function is constructed to guarantee the stability of both the linear observer and the NN updates. The observer gain is determined by solving the LMI conditions, and the design is simplified by minimizing the number of tuning parameters, using a common gain structure for all vertices. Furthermore, designing an H∞ observer can reduce the effect of NN approximation error and the measurement noise. The key advantages of the proposed method lie in its optimal LMI-based observer gain design, minimal tuning parameter requirement, and the capability to estimate both the system states and the lumped nonlinear term simultaneously. Simulation results indicate that the proposed method successfully tracks the actual states and the lumped nonlinear term and reduce the effects of NN approximation error and the measurement noise with comparison of the root mean square error (RMSE) values.
"
# links:
#   - name: 
#     url: 
---

