---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Chattering Reduction of Sliding Mode Control via Nonlinear Disturbance Observer for Anti-lock Braking System and Verification with Carsim Simulation" # Title of the paper
krtitle: # only for domestic papers
authors: # List of authors
  - name: "Minseong Choi"
  - name: "Kyunghwan Choi"
  - name: "Minsu Cho"
  - name: "Minyoung Lee"
  - name: "Kyung-Soo Kim"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Journal of Automotive Technology"
    doi: 10.1007/s12239-023-0093-7 # Leave it blank if not applicable
    vol:  "24"
    num:  "4"
    pp: "1141–1149" # Leave it blank if not applicable
    year: "2023" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2023-07-19" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2023-chattering-reduction.png" # Representative image of the paper
abstract: "
The anti-lock braking system (ABS) is a vehicle safety technology that prevents wheels from locking during braking by tracking the optimal reference slip. Due to the structural characteristics of hydraulic circuits, a brake system has a discontinuous pressure control input which is composed of apply and dump modes. Sliding mode control is a robust control technique that uses discontinuous control input and is being studied expensively. However, sliding mode control has a crucial chattering problem caused by high compensation gain, which leads to high wearing of the mechanical parts. This problem can be alleviated by compensating for unknown disturbances with estimated values. A nonlinear disturbance observer can estimate the system’s uncertainty without mathematical model information. Therefore, sliding mode control based on a nonlinear disturbance observer is proposed here, and the simulation results with ABS are compared with the original sliding mode control. Simulations are conducted with high- and low- μ road surface scenarios, and three key performance indicators for evaluations are compared. In conclusion, the brake performance was enhanced and the chattering issue of the sliding mode controller was reduced by proposed method.
"
# links: # additional links;
#   - name: 
#     url: 
---