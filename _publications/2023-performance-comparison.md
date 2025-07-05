---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Performance Comparison of Long-Horizon FCS-MPC for IPMSM Considering THDi and Inverter Loss" # Title of the paper
krtitle: # only for domestic papers
authos: 
  - name: "Jongseok Kim"
  - name: "Youngseok Lee"
  - name: "Kyunghwan Choi"
  - name: "Jiho Song"
  - name: "Ki-Bum Park"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Conference on Power Electronics and ECCE Asia (ICPE 2023 - ECCE Asia)"
    doi: "10.23919/ICPE2023-ECCEAsia54778.2023.10213826" # Leave it blank if not applicable
    vol:  # Leave it blank if not applicable
    num:  # Leave it blank if not applicable
    pp: "1680-1685" # Leave it blank if not applicable
    year: "2023" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2023-08-31" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2023-performance-comparison.png" # Representative image of the paper
abstract: "
In this paper, the feasibility of achieving performance benefits in two control objectives is analyzed using long-horizon finite control set-model predictive control for an interior permanent magnet synchronous motor. Current reference tracking and minimization of inverter loss are used as control objectives in a cost function. At the fixed sampling period, simulation results show the trend that the current total harmonic distortion and inverter efficiency improve as the length of the prediction horizon increases. To derive results of considering the sampling period and weighting factor effects, Monte Carlos simulations were carried out. Considering the real-time implementation and the system performance, length of horizon and sampling period should be decided depending on the motor speed and torque with an appropriate weighting factor.
"
# links: # additional links;
#   - name: 
#     url: 
---