---
type: "Master's Thesis"
layout: publication
group: publications
title: "Online Stator Flux Linkage Estimation of Synchronous Machines"
krtitle: "동기전동기의 온라인 고정자 쇄교 자속 추정"
authors:
  - name: "Seunghun Jang"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
pub: # Publication information
  - name: Gwangju Institute of Science and Technology (GIST) Library
    doi: 
    pdf: "/static/pub/2024-shJang-Master.pdf"
    year: "2024"
    state: "published"
pub_date: "2024-09-01" # abstract; emphasize the important part using **bold** or *italic* of markdown syntax
image: "/static/pub/2024-shJang-Master.png"
abstract: "
  In this thesis, online flux linkage estimators for synchronous machines (SMs) are proposed.
  The proposed flux estimators are generally applicable to all types of synchronous
  machines and are designed to consider the nonlinearities caused by cross-coupling and
  magnetic saturation in the machines. Additionally, the estimators are designed without
  using filters designed in the frequency domain, thus avoiding phase and magnitude
  distortions in transient state. Existing estimators primarily determine their estimation
  performance in both transient and steady states based on the accuracy of the nominal
  parameters. However, the proposed estimators assume the nonlinear flux term as a
  ramp disturbance signal or estimate parameters online and update them to the actual
  values, thereby reducing the impact of parameter inaccuracies. This improves the flux
  estimation performance under various operating conditions. The validity of the proposed
  estimators is demonstrated through comparisons with existing estimators with
  finite element method (FEM)-based simulations of a 35 kW Interior Permanent Magnet
  Synchronous Motor (IPMSM) provided in MATLAB/Simulink.
"
# links: # additional links;
#   - name: 
#     url: 
---