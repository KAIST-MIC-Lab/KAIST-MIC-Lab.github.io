---
type: "Journal Paper"
layout: publication
group: publications
title: "Model-Predictive-Control-Based Time-Optimal Trajectory Planning of the Distributed Actuation Mechanism Augmented by the Maximum Performance Evaluation"
authors: 
  - name: Jong Ho Kim
  - name: Kyunghwan Choi
  - name: In Gwun Jang
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # or "domestic"
pub:
  - name: "Applied Sciences"
    doi: 10.3390/app11167513
    year: "2021"
    vol: "11" # Leave it blank if not applicable
    num: "16" # Leave it blank if not applicable
    state: "published"
pub_date: "2021-08-16"
image: "/static/pub/2021-model-predictive.png"
abstract: "
Trajectory planning for a redundant manipulator is a classic problem. However, because it is difficult to precisely evaluate its maximum performance, an optimization method has been typically used. In this study, a novel time-optimal trajectory planning method for a redundant manipulator is proposed using the model predictive control (MPC) augmented by the maximum performance evaluation (MPE). First, the optimization formulation is expressed to evaluate the maximum performance of the distributed-actuation-mechanism-based three-revolute-joint manipulator (DAM-3R), which has a high level of redundancy, and the joint-actuation-mechanism-based three-revolute-joint manipulator (JAM-3R) for comparison. The optimization is conducted by linking the multibody dynamics analysis module and the optimization module. For time-optimal trajectory planning, the MPC problem is then formulated using mathematical performance models for the DAM-3R and JAM-3R based on the MPE results, which are considered as the upper bound of the manipulator performance at each end-effector position. To verify the proposed method, a point-to-point task with no predefined path is investigated. The simulation results show that the working time of the DAM-3R is 19.1% less than that of the JAM-3R. Moreover, the energy consumption for the DAM-3R is 45.0% lower than that for the JAM-3R by optimally utilizing the higher redundancy of the DAM-3R. Thus, it can be concluded that the proposed method is effective for time-optimal trajectory planning for redundant manipulators.
"
# links:
#   - name: 
#     url: 
---
