---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Computationally Efficient Model Predictive Torque Control of Permanent Magnet Synchronous Machines Using Numerical Techniques" # Title of the paper
krtitle: # only for domestic papers
authors: # List of authors
  - name: "Kyunghwan Choi"
  - name: "Yonghun Kim"
  - name: "Seok-Kyoon Kim"
    corresponding: true # true if this author is the corresponding author
  - name: "Kyung-Soo Kim"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "IEEE Transactions on Control Systems Technology"
    doi: "10.1109/TCST.2021.3113045" # Leave it blank if not applicable
    vol: "30" # Leave it blank if not applicable
    num:  "4" # Leave it blank if not applicable
    pp: "1774-1781"# Leave it blank if not applicable
    year: "2022"# Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2022-09-30" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2022-computationally-efficient.png" # Representative image of the paper
abstract: "
This study presents a computationally efficient model predictive torque control (MPTC) method for permanent magnet synchronous machines (PMSMs). The existing MPTC methods require solving complex optimization problems in iterations; this approach is computationally demanding. In contrast, the proposed MPTC transforms the optimization problem into two subproblems and derives the corresponding solutions explicitly using numerical techniques, which entail linearization of the torque function and current constraint; the proposed approach can significantly reduce the computational burden. Additionally, the proposed MPTC does not involve any control gains and weighting factors; hence, gain tuning is not required for the proposed MPTC. These features are advantageous when implementing torque control. Using a 4-kW PMSM drive, the effectiveness of the proposed MPTC is demonstrated both numerically and experimentally in terms of dynamic performance and computational efficiency. This is realized by comparing the proposed method with the existing methods.
"
# links: # additional links;
#   - name: 
#     url: 
---