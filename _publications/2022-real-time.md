---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Real-Time Predictive Energy Management Strategy for Fuel Cell-Powered Unmanned Aerial Vehicles Based on the Control-Oriented Battery Model" # Title of the paper
krtitle: # only for domestic papers
authors: # List of authors
  - name: "Kyunghwan Choi"
  - name: "Wooyong Kim"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "IEEE Control Systems Letters"
    doi: "10.1109/LCSYS.2022.3228946" # Leave it blank if not applicable
    vol: "7" # Leave it blank if not applicable
    no:  # Leave it blank if not applicable
    pp: "943-948"# Leave it blank if not applicable
    year: "2022"# Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2022-12-01" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2022-real-time.png" # Representative image of the paper
abstract: "
The predictive energy management (PEM) problem for hybrid electric powertrains is challenging to solve in real time, mainly due to the nonconvexity from the battery state of energy (SOE) model, which is nonlinear. This letter proposes a control-oriented battery model consisting of a stochastic linear SOE model and a quadratic power loss model to realize real-time PEM. The stochastic linear model describes the SOE trajectory from an average point of view. The quadratic power loss model describes the nonlinear power loss that the stochastic linear SOE model cannot consider. By replacing the nonlinear SOE model with the control-oriented model, the PEM problem is reformulated into quadratic programming (QP), which can be easily solved in real time by a QP solver. Simulation results obtained using a fuel cell-powered unmanned aerial vehicle (UAV) show that the proposed model predicts the trend of the SOE trajectory well, even for long prediction horizons (maximum of 750 s). In addition, PEM based on the proposed model results in near-optimal performance (0.36% difference from the global solution) with real-time capability (solved within 0.27 s).
"
# links: # additional links;
#   - name: 
#     url: 
---