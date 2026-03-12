---
type: "Master's Thesis"
layout: publication
group: publications
title: "Robust Imitation Learning with Attention Constraints and Risk Awareness for Motion Planning in Autonomous Driving"
krtitle: "어텐션 제약과 위험 인지를 활용한 강건한 모방학습 기반 자율주행 모션 플래닝"
authors:
  - name: "Jiyun Kim"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
pub: # Publication information
  - name: Gwangju Institute of Science and Technology (GIST) Library
    doi: 
    pdf: "/static/pub/2026-jyKim-Master.pdf"
    year: "2026"
    state: "published"
pub_date: "2026-03-01" # abstract; emphasize the important part using **bold** or *italic* of markdown syntax
image: "/static/pub/2026-jyKim-Master.png"
abstract: "
Imitation learning (IL) has become a common approach for autonomous-driving motion planning, but achieving robust and safe behavior remains difficult under distribution shift and rare hazard scenarios. A key limitation is that IL objectives typically prioritize mean accuracy (e.g., Average Distance Error), which can high-consequence failures in the long tail. Moreover, planners that use attention mechanisms, including Transformer-based planners, can exhibit attention collapse such as shortcut learning by over-relying on a small subset of state channels. This dissertation proposes a robust IL framework for motion planning that combines attention constraints and risk awareness. Mean-Deviation Constrained Attention (MDCA) promotes balanced state usage, and a Conditional Value-at-Risk (CVaR)-based tail-risk objective down-weights rare but potentially dangerous modes. Experiments on the nuPlan benchmark show improved robustness and safety-related metrics over State-Of-The-Arts planners.
"
# links: # additional links;
#   - name: 
#     url: 
---