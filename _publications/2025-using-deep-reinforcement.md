---
type: "Conference Paper"
layout: publication
group: publications
title: "Using Deep Reinforcement Learning for Dynamic Gain Adjustment of a Disturbance Observer"
authors:
  - name: "Hyochan Lee"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
  - name: "Wooyong Kim"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # or "domestic"
preprint: 
  - name: "TechRxiv"
    doi: "10.36227/techrxiv.171174527.70147690/v1"
    pdf: "/static/pub/2025-using-deep-reinforcement.pdf"
    year: "2024"
    state: "published"
pub:
  - name: "International Conference on Control, Automation and Systems (ICCAS)"
    doi: 
    year: "2025"
    state: "accepted"
pub_date: "2025-11-04"
image: "/static/pub/2025-using-deep-reinforcement.png"
abstract: "
 Increasing estimation accuracy and reducing noise sensitivity are challenging trade-offs in designing disturbance observers (DOBs). The DOB gain tuning process for overcoming this trade-off is not straightforward, nor does it guarantee optimal performance for the resulting DOBs. This paper presents a dynamic gain DOB that intelligently adjusts its gain based on deep reinforcement learning (DRL) to overcome this tradeoff. First, a variable gain DOB is designed by modifying the conventional DOB. The variable gain DOB can exponentially estimate a constant disturbance with a varying gain. Then, DRL is used to train a dynamic gain adjuster for the variable gain DOB. A case study demonstrated that the proposed dynamic gain DOB increases its gain only when needed (i.e., when the estimation error is significant) and otherwise decreases the gain to reduce noise. Comparison with the conventional DOB of various constant gains shows that the proposed DOB achieves superior performance.
"
# links:
#   - name: 
#     url: 
---
