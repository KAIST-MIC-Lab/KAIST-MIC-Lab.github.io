---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Model-Predictive-Control-Based Time-Optimal Trajectory Planning of the Distributed Actuation Mechanism Augmented by the Maximum Performance Evaluation" # Title of the paper
krtitle: # only for domestic papers
authors: "Jong Ho Kim, <u>Kyunghwan Choi</u>, Gwun Jang#42;"
domestic_or_international: "International" # "International" or "Domestic"
pubs: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "applied science"
    doi: "10.3390/app11167513" # Leave it blank if not applicable
    vol: "11" # Leave it blank if not applicable
    no: "16" # Leave it blank if not applicable
    pp: "#"# Leave it blank if not applicable
    year: "2022"# Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2022-08-16" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2021-trajectory.png" # Representative image of the paper
abstract: "
Trajectory planning for a redundant manipulator is a classic problem. However, because it is difficult to precisely evaluate its maximum performance, an optimization method has been typically used. In this study, a novel time-optimal trajectory planning method for a redundant manipulator is proposed using the model predictive control (MPC) augmented by the maximum performance evaluation (MPE). First, the optimization formulation is expressed to evaluate the maximum performance of the distributed-actuation-mechanism-based three-revolute-joint manipulator (DAM-3R), which has a high level of redundancy, and the joint-actuation-mechanism-based three-revolute-joint manipulator (JAM-3R) for comparison. The optimization is conducted by linking the multibody dynamics analysis module and the optimization module. For time-optimal trajectory planning, the MPC problem is then formulated using mathematical performance models for the DAM-3R and JAM-3R based on the MPE results, which are considered as the upper bound of the manipulator performance at each end-effector position. To verify the proposed method, a point-to-point task with no predefined path is investigated. The simulation results show that the working time of the DAM-3R is 19.1% less than that of the JAM-3R. Moreover, the energy consumption for the DAM-3R is 45.0% lower than that for the JAM-3R by optimally utilizing the higher redundancy of the DAM-3R. Thus, it can be concluded that the proposed method is effective for time-optimal trajectory planning for redundant manipulators.
"
# links: # additional links;
#   - name: 
#     url: 
---