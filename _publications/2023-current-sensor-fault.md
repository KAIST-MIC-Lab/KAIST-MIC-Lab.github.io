---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "A Current Sensor Fault-detecting Method for Electric Vehicle Battery Systems Based on Disturbance Observer" # Title of the paper
krtitle: "외란 관측기를 사용한 전기차 배터리 시스템의 전류 센서 고장 감지 방법" # only for domestic papers
authors: 
  - name: "Kunwoo Na"
  - name: "Kyunghwan Choi"
  - name: "Wooyong Kim"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "Domestic" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "Journal of Institute of Control, Robotics and Systems"
    doi: "10.5302/J.ICROS.2023.23.0124" # Leave it blank if not applicable
    vol: "29" # Leave it blank if not applicable
    num: "12" # Leave it blank if not applicable
    pp: "1052-1059" # Leave it blank if not applicable
    year: "2023" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2023-06-01" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2023-current-sensor-fault.png" # Representative image of the paper
abstract: "
In the pursuit of developing a fault-tolerant architecture for battery management systems, rapid detection and isolation are pivotal functions. This study presents a method for detecting current sensor faults in an electric vehicle battery management system. Electric vehicle battery systems are exposed to harsh operating conditions, which increases the risk of failures in various onboard components. The proposed current sensor fault detection method incorporates a state estimator and a disturbance observer based on a nonlinear battery cell model for estimating unknown currents. The disturbance observer can estimate the engaged current even when the current measurement is unavailable, thereby allowing the detection of current sensor faults by analyzing the residual between the estimated and measured currents. Experimental results conducted on a single battery cell demonstrate the successful detection of current sensor faults using the proposed method. This sensor fault detection method plays a crucial role in determining the operation of the backup algorithm. 
"
# links: # additional links;
#   - name: 
#     url: 
---