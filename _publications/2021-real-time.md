---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Real-Time Optimal Torque Control of Interior Permanent Magnet Synchronous Motors Based on a Numerical Optimization Technique" # Title of the paper
krtitle: # only for domestic papers
authors: 
  - name: "Kyunghwan Choi"
  - name: "Yonghun Kim"
  - name: "Seok-Kyoon Kim"
    corresponding: true # true if this author is the corresponding author
  - name: "Kyung-Soo Kim"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "IEEE Transactions on Control Systems Technology"
    doi: "10.1109/TCST.2020.3006900" # Leave it blank if not applicable
    vol: "29" # Leave it blank if not applicable
    num:  "4" # Leave it blank if not applicable
    pp: "1815-1822"# Leave it blank if not applicable
    year: "2021"# Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2021-07-15" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2021-real-time.png" # Representative image of the paper
abstract: "
This study presents a real-time optimal torque control scheme for interior permanent magnet synchronous motors (IPMSMs). The proposed scheme enables computation of optimal current reference for a torque reference under all operating regions, including the maximum torque per ampere (MTPA), flux weakening (FW), maximum current (MC), and maximum torque per voltage (MTPV), using numerical optimization techniques to simplify the problems and obtain the corresponding solutions with reduced computation burden. Linearizing the torque equation of IPMSM is utilized to derive solutions for the MTPA and FW. These solutions are proved to converge to their optimum with the aid of the reference smoother. Numerical solutions for the MC and MTPV are derived based on the assumption that the resistive voltage drop is small enough but not zero. These solutions differ from the existing solutions that ignore the resistive voltage drop. The effectiveness of the proposed method is numerically and experimentally verified using a 7.5-kW IPMSM with a considerable reduction in computational time of approximately 90% in the simulation compared with the analytic solution.
"
# links: # additional links;
#   - name: 
#     url: 
---