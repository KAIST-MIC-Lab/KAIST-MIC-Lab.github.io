---
type: "Conference Paper"
layout: publication
group: publications
title: "Performance Comparison of Long-Horizon FCS-MPC for IPMSM Considering THDi and Inverter Loss"
domestic_or_international: "International" # or "Domestic"
authors: # List of authors
  - name: "Jonghwan Kim"
  - name: "Youngseok Lee"
  - name: "Kyunghwan Choi"
  - name: "Jiho Song"
  - name: "Kinum Kim"
    corresponding: true # true if this author is the corresponding author
pub: 
  - name: International Conference on Power Electronics and ECCE Asia (ICPE - ECCE Asia)
    doi: 10.23919/ICPE2023-ECCEAsia54778.2023.10213826
    pp: 1680-1685
    state: "accepted" # published, accepted, submitted
    year: "2023"
pub_date: "2023-05-23" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2023-performance.png"
abstract: "
  In this paper, the feasibility of achieving performance benefits in two control objectives is analyzed using long-horizon finite control set-model predictive control for an interior permanent magnet synchronous motor. Current reference tracking and minimization of inverter loss are used as control objectives in a cost function. At the fixed sampling period, simulation results show the trend that the current total harmonic distortion and inverter efficiency improve as the length of the prediction horizon increases. To derive results of considering the sampling period and weighting factor effects, Monte Carlos simulations were carried out. Considering the real-time implementation and the system performance, length of horizon and sampling period should be decided depending on the motor speed and torque with an appropriate weighting factor.
  "
---