---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "CAR Planner: Constrained-Attention-Based Robust Imitation Learning for Autonomous Driving" # Title of the paper
krtitle: "CAR Planner: 제약 어텐션 기반 강건 모방학습 플래너" # only for domestic papers
authors: 
  - name: "Jiyun Kim"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "Domestic" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "한국자동차공학회 추계학술대회 (KSAE)"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2025" # Leave it blank if not applicable
    state: "accepted" # published, accepted, submitted
    pdf: "/static/pub/2025-car-planner-constrained.pdf" # Leave it blank if not applicable
pub_date: "2025-11-14" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-car-planner-constrained.png" # Representative image of the paper
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Imitation Learning (IL) is widely used for autonomous driving but remains vulnerable to shortcut learning, where
  policies exploit spurious correlations rather than causal driving cues, undermining generalization and robustness under distribution
  shift and OOD conditions. We present CAR Planner, which augments the attention mechanism with a constrained formulation: an
  inequality constraint limits the mean deviation of ego-state cross-attention weights from uniform, enforced via the Augmented
  Lagrangian Method (ALM). This regularizer curbs over-reliance on a few channels and encourages balanced state representations,
  adding negligible training overhead and no inference cost. On nuPlan, CAR Planner shows markedly smaller performance drops
  when ego-state channels are reduced, providing strong evidence of robustness against shortcut reliance. Furthermore, it
  consistently outperforms both an unconstrained baseline(without constraint) and state-of-the-art dropout-based methods in
  challenging scenarios, while also producing smoother and more stable driving. These results indicate that CAR Planner enables
  more robust IL for autonomous driving.
"
---