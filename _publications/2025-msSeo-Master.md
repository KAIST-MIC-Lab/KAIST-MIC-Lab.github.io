---
type: "Master's Thesis"
layout: publication
group: publications
title: "State-wise Safety in Autonomous Driving via Lagrangian-based Constrained Reinforcement Learning"
krtitle: "라그랑지안 기반 제약 강화학습을 이용한 자율주행에서의 상태별 안전성 고려"
authors:
# authors: # Authors of the paper
  - name: "Minseok Seo"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
pub: # Publication information
  - name: Gwangju Institute of Science and Technology (GIST) Library
    doi: 
    pdf: "/static/pub/2025-msSeo-Master.pdf"
    year: "2025"
    state: "published"
pub_date: "2025-09-01" # abstract; emphasize the important part using **bold** or *italic* of markdown syntax
image: "/static/pub/2025-msSeo-Master.png"
abstract: "
  For the practical deployment of autonomous driving systems, high levels of safety and adaptability are essential. Accordingly, Deep Reinforcement Learning (DRL), which learns and improves driving strategies through trial and error, has gained attention. However, the reward-driven nature of reinforcement learning may still lead to unsafe or abnormal behavior even after training. To address this limitation, Constrained Reinforcement Learning (CRL) has been proposed to balance safety and performance. While CRL typically defines constraints as expected cumulative costs, this formulation does not consider whether constraints are satisfied at each state, making it difficult to ensure state-wise safety. In this paper, we extend a Lagrangian-based CRL approach by estimating state-wise Lagrangian multipliers, allowing the policy to account for state-level safety. We evaluate the proposed method in OpenAI's Safety Gym environment and compare its performance with existing Lagrangian-based methods."
# links: # additional links;
#   - name: 
#     url: 
---
