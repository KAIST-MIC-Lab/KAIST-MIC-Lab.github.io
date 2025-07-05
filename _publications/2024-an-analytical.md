---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "An Analytical Approach to the Predictive Energy Management of Connected HEVs: What Information Do We Need to Guarantee Global Optimality?" # Title of the paper
krtitle: # only for domestic papers
authors: # List of authors
  - name: "Kyunghwan Choi"
  - name: "Jongseok Kim"
  - name: "Ki-Bum Park"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "IEEE Transactions on Intelligent Transportation Systems"
    doi: "10.1109/TITS.2024.3384358" # Leave it blank if not applicable
    vol:  "25"
    num:  "9"
    pp: "12749-12761" # Leave it blank if not applicable
    year: "2024" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2024-04-24" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2024-an-analytical.png" # Representative image of the paper
abstract: "
The predictive energy management (PEM) of hybrid electric vehicles (HEVs) is a challenging problem of trajectory optimization involving future information. Most previous studies have presented intuitive methods for selecting parameters that represent future information. However, such intuitive methods lack theoretical analysis and do not guarantee global optimality. This study adopts the novel perspective that the PEM problem can be analytically solved so as to ensure near-optimal efficiency. The key idea is to reformulate the trajectory optimization problem as a quadratic programming (QP) problem based on optimal control principles. The equivalence between the original and QP problems is theoretically derived. The proposed PEM strategy is then implemented by solving the QP problem at every sampling time to obtain the optimal control input. Whereas the original problem requires information on the entire future trajectory, which is difficult to predict accurately, the QP problem requires only lumped parameters, specifically, the energy demands and time durations of each segment of the future path. These lumped future driving parameters can potentially be predicted using information obtained through vehicle connectivity. Simulation results obtained under a real-world driving scenario show that the proposed PEM strategy provides a control result in real time (within 2 ms) that is very close to the globally optimal solution both qualitatively and quantitatively, with a loss of optimality of only 0.14%.
"
# links: # additional links;
#   - name: 
#     url: 
---