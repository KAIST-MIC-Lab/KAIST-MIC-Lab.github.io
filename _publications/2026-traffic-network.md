---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Traffic Network-Aware Energy Management for FCEVs: Integrating Trip-Specific Control and Long-Run Optimality" # Title of the paper
# krtitle: # only for domestic papers
authors: 
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
    pdf: "/static/pub/2026-traffic-network.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2026" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-02-16" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2026-traffic-network.png" # Representative image of the paper
abstract: "
  Energy management for fuel cell electric vehicles (FCEVs) is a challenging trajectory optimization problem. Conventional studies primarily focus on trip-specific optimal control, where the power distribution is optimized based on a predicted finite-horizon driving profile. However, these methods often suffer from a limited look-ahead horizon and fail to guarantee long-run optimality within the stochastic traffic network where the vehicle operates. This study proposes a novel framework that integrates finite-horizon optimal control with traffic network-aware long-run average costs. We formulate the problem by embedding the long-run optimality, derived from network-level transition probabilities, into the terminal cost of the trip-specific optimization. This approach enables an adaptive target State of Charge (SOC) that aligns with global network efficiency while satisfying immediate driving constraints. Simulation results in a virtual traffic network demonstrate that the proposed integrated strategy consistently outperforms traditional trip-specific methods, achieving a maximum performance improvement of 11%. These findings highlight the necessity of network-level statistical awareness for maximizing the long-term energy efficiency of electrified mobility.
"
# additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."
# links: # additional links;
#   - name: 
#     url: 
---