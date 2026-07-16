---
type: "Conference Paper"
layout: publication
group: publications
title: "TRIAD Planner: Three-Level Robust Imitation Learning for Autonomous Driving"
#krtitle: "CARE Planner : 모방학습 기반 자율주행을 위한 제약 어텐션 및 위험 인지 플래닝"
authors:
  - name: "Jiyun Kim"
  - name: "Ahmad Mouri Zadeh Khaki"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International"
pub: 
  - name: Conference on Robot Learning (CoRL)
    doi: 
    year: "2026"
    pdf: "/static/pub/2026-TRIAD.pdf"
    state: "submitted"
pub_date: "2026-12-31" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2026-TRIAD.png"
abstract: "
  Imitation learning for autonomous driving suffers from distribution shift between logged expert trajectories and self-induced deployment states. In Transformer-based planners, this shift can appear as ego-state shortcut learning, incomplete scene understanding, and unsafe mode selection under interaction un certainty. This paper presents a robust imitation-learning planner based on a three level robustness formulation. 1) Channel-level robustness: constrained ego-state attention to reduce shortcut dependence on a small subset of state channels. 2) Scene-level robustness: offline vision-language model (VLM) guidance to encour age the ego query to retain interaction-critical agent evidence and route-relevant map evidence. 3) Decision-level robustness: training-time multimodal supervi sion reshaped with a tail-risk score based on mean excess above Value at Risk. The scene-level VLM guidance and decision-level tail-risk supervision are used only during training, and the deployed planner incurs no additional inference-time over head. On nuPlan test14, the proposed planner achieves the strongest performance among the evaluated learning-based methods and improves over CAR Planner, a strong constrained-attention imitation-learning baseline. The gains are especially pronounced on test14-hard, which contains more challenging scenarios, where NR-CLS and R-CLS change from 70.81 and 66.12 to 73.39 and 67.12, respec tively. Ablation results show that combining all three-level components yields consistent performance across diverse scenarios, supporting the effectiveness of robust imitation learning for autonomous driving.
"
# links:
#   - name: 
#     url: 
---