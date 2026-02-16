---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "LLM-PPO Driver: Improving Autonomous Driving via LLM-Guided Reward Shaping and Imitation Learning" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Ahmad Mouri Zadeh Khaki"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
# preprint: # Preprint information - REMOVE THIS FIELD IF NOT APPLICABLE!
#   - name: Techrxiv 
#     doi: "10.36227/techrxiv.173014412.26480551/v1"
#     year: 2024
    # pdf: "/static/pub/2025-all-wheel.pdf"
    # state: "published" # published, accepted, submitted
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "Asian Control Conference (ASCC)"
    pdf: "/static/pub/2026-LLM-PPO.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-02-16" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2026-LLM-PPO.png" # Representative image of the paper
abstract: "
 Proximal Policy Optimization (PPO) has shown promise for autonomous driving; however, it suffers from sparse rewards, slow convergence, and unsafe behaviors due to exploration without prior knowledge. These limitations are particularly critical in safety-sensitive driving scenarios, where failure events are rare but severe. To address this issue, we propose LLM-PPO Driver, a framework that enhances PPO-based motion planning by incorporating high-level semantic driving knowledge from a Large Language Model (LLM). The LLM does not participate in real-time decision-making; instead, it provides structured prior knowledge that is integrated through reward shaping and imitation learning. This lightweight and modular design eliminates deployment-time inference overhead while guiding policy learning toward safer and more efficient behaviors. Experiments in the Gym highway-v0 environment demonstrate consistent improvements in task success and safety over a baseline PPO agent, with imitation learning yielding the largest performance gain. These results highlight the effectiveness of leveraging LLM-based prior knowledge to mitigate unsafe exploration and improve learning efficiency in autonomous driving.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
---