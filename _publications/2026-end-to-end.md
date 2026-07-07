---
type: "Conference Paper"
layout: publication
group: publications
title: "End-to-End Online LSTM Control for Robust 4WS Path Tracking under Combined Disturbances"
krtitle: "복합 외란 하에서 강인한 4WS 경로 추종을 위한 엔드투엔드 온라인 LSTM 제어"
authors:
  - name: "Naol Samuel Erega"
  - name: "Kyunghwan Choi"
    corresponding: true
domestic_or_international: "Domestic"
pub:
  - name: 제어로봇시스템학회 (ICROS)
    doi:
    year: "2026"
    pdf: "/static/pub/2026-end-to-end.pdf"
    state: "accepted"
pub_date: "2026-07-01"
image: "/static/pub/2026-end-to-end.jpg"
abstract: "
  This paper proposes a continuous-time LSTM neural network as an end-to-end controller for four-wheel steering (4WS) path tracking. Without offline data, reference models, or expert demonstrations, the controller learns online from real-time tracking error and maps lateral and heading error directly to front and rear steering commands. The proposed method is evaluated on a slalom track under combined disturbances including actuator bias, Ornstein-Uhlenbeck colored noise, and a lateral wind gust. Simulation results show that the LSTM weights converge within a few episodes and maintain near-nominal tracking performance under disturbance, whereas a tuned PID baseline exhibits substantially larger RMSE increases. These results suggest that online LSTM adaptation improves robustness for 4WS path tracking under combined disturbances.
"
# links:
#   - name:
#     url:
---