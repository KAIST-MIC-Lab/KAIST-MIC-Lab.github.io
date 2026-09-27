---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Constraint-Aware Speed Planning under Curved Road Conditions for Smart Regenerative Braking using an Analytical Minimum-Jerk Approach" # Title of the paper
# krtitle: # only for domestic papers
authors: 
# Soobin Hwang, Yewon Kang, Sungeun Park, Gyubin Sim, and Sooyoung Kim
  - name: "Soobin Hwang"
  - name: "Yewon Kang"
  - name: "Sungeun Park"
  - name: "Gyubin Sim"
  - name: "Sooyoung Kim"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "IEEE Transactions on Vehicular Technology"
    pub_url: "https://ieeexplore.ieee.org/xpl/RecentIssue.jsp?punumber=25" # conference or journal URL (not your paper URL)
    pdf: "/static/pub/2026-constraint-aware.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: 2026 # "2025" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-12-31" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2026-constraint-aware.png" # Representative image of the paper
abstract: "
  Achieving smooth and predictable deceleration during cornering remains a critical challenge for smart regenerative braking systems (SRS) in electric vehicles (EVs), particularly when fixed deceleration strategies fail to reflect driver preferences and varying road geometries.


  This paper presents a constraint-aware speed planning framework for curvature-induced deceleration in EVs equipped with SRS. A minimum-jerk-based analytical formulation is employed to generate continuous and human-centered deceleration profiles, while an efficient time-adjustment mechanism ensures compliance with longitudinal acceleration constraints without iterative numerical optimization, enabling real-time implementation. In addition, a driver-adaptive target speed update strategy is introduced, which adjusts curvature-based target speeds based on driver pedal interventions to reflect individual driving tendencies during SRS operation.


  The proposed framework is implemented in a vehicle control unit and validated through simulation and real-vehicle experiments. The results demonstrate that the proposed method provides feasible and smooth deceleration under varying curvature conditions, reduces driver pedal interventions, and improves deceleration comfort during cornering. These improvements contribute to enhanced drivability and increased utilization of regenerative braking in EVs.
"
---