---
type: "Conference Paper"
layout: publication
group: publications
title: "CARE Planner : Constrained Attention and Risk-aware Planning for Imitation-based Autonomous Driving"
krtitle: "CARE Planner : 모방학습 기반 자율주행을 위한 제약 어텐션 및 위험 인지 플래닝"
authors:
  - name: "Jiyun Kim"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "Domestic"
pub: 
  - name: 제어로봇시스템학회 (ICROS)
    doi: 
    year: "2026"
    pdf: "/static/pub/2026-CARE-Planner-constrained.pdf"
    state: "accepted"
pub_date: "2026-6-25" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2026-CARE-Planner-constrained.png"
abstract: "
  Imitation-learning planners for autonomous driving commonly optimize displacement-based objectives, which improve average trajectory accuracy but may overlook rare unsafe modes. This paper presents CARE Planner, a risk-aware extension of CAR Planner that combines constrained ego-state attention with a Conditional Value at Risk (CVaR)-based tail-risk module. The proposed module estimates clearance-based risk along the prediction horizon, adjusts supervised mode selection toward safer candidates, and constructs risk-aware soft targets for multimodal trajectory learning. The attention constraint prevents excessive dependence on a small subset of ego-state channels, while the CVaR-based module reshapes the output distribution away from high-risk modes. Experiments on the nuPlan test14-random and test14-hard splits show improved open-loop and closedloop performance, and a pedestrian-waiting scenario analysis shows a reduced high-risk trajectory distribution.
"
additional: "📄 Awarded <span style=\"color: goldenrod;\"><strong>Best Paper Award</strong></span> at the _2026 Institute of Control, Robotics and Systems (ICROS) Conference_."
# links:
#   - name: 
#     url: 
---