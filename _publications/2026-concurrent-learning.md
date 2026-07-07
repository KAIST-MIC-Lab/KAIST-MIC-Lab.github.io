---
type: "Conference Paper"
layout: publication
group: publications
title: "Concurrent Learning-Based Adaptive Online Identification of Battery Thermal Dynamics"
krtitle: "동시학습 기반 배터리 열동역학 온라인 잔차 학습"
authors:
  - name: "Seunghun Jang"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "Domestic"
pub: 
  - name: 제어로봇시스템학회 (ICROS)
    doi: 
    year: "2026"
    pdf: "/static/pub/2026-concurrent-learning.pdf"
    state: "accepted"
pub_date: "2026-07-01"
image: "/static/pub/2026-concurrent-learning.png"
abstract: "
  This paper presents a data-driven online identification method for battery thermal dynamics in battery thermal management systems. An offline-identified lumped thermal model is used as a nominal battery thermal model, but its accuracy can deteriorate when operating conditions, ambient temperature, and load conditions vary. To improve model accuracy, a concurrent learning-based approach is introduced to learn the unmodeled thermal dynamics online while keeping the estimation errors bounded. The learning rules utilize the informative stored data together with current measurements, thereby improving parameter convergence without requiring continuous persistent excitation. Simulation studies in the MATLAB/Simulink 2025a EV environment show that the proposed method improves long-horizon temperature prediction and reduces rollout RMSE by up to 32.3% compared with the offline model.
"
---