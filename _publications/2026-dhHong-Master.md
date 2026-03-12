---
type: "Master's Thesis"
layout: publication
group: publications
title: "Integral Error-Based Adaptive Neural Identifier for a Class of Uncertain Nonlinear Systems"
krtitle: "불확실한 비선형시스템을위한 적분 오차 기반적응신경망 식별기"
authors:
  - name: "Donghwa Hong"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
pub: # Publication information
  - name: Gwangju Institute of Science and Technology (GIST) Library
    doi: 
    pdf: "/static/pub/2026-dhHong-Master.pdf"
    year: "2026"
    state: "published"
pub_date: "2026-03-01" # abstract; emphasize the important part using **bold** or *italic* of markdown syntax
image: "/static/pub/2026-dhHong-Master.png"
abstract: "
This thesis studies online identification of unknown nonlinear dynamics in estimation problems, focusing on how past information is reflected in parameter updates. Conventional adaptive neural identifiers rely on instantaneous estimation errors, which are effective for real-time compensation but often show limited consistency when the adapted parameters are reused. In contrast, buffer-based online learning approaches improve consistency by explicitly storing past data, at the cost of increased computational and memory complexity. Motivated by this trade-off, an integral error–based adaptive neural identifier is proposed, in which past estimation errors are incorporated through a dynamic integral state rather than an explicit buffer. The proposed method preserves the continuous-time adaptive structure of conventional identifiers while enabling accumulated error information to influence parameter updates in a structured manner. A Lyapunov-based analysis establishes uniform ultimate boundedness of the estimation error, and simulations on a robot manipulator with static friction and a vehicle lateral dynamics model demonstrate improved consistency with comparable instantaneous estimation accuracy.
"
# links: # additional links;
#   - name: 
#     url: 
---