---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "A Current-sensor Error Compensation Algorithm for Battery Management Systems Based on Sigma-point Kalman Filter" # Title of the paper
krtitle: "시그마–포인트 칼만 필터를 사용한 배터리 관리 시스템의 전류 센서 오차 보상 알고리즘" # only for domestic papers
authors: 
  - name: "Kunwoo Na"
  - name: "Youngkook Kim"
  - name: "Kyunghwan Choi"
  - name: "Wooyong Kim"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "Domestic" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "Journal of Institute of Control, Robotics and Systems"
    doi: "10.5302/J.ICROS.2024.24.0095" # Leave it blank if not applicable
    vol: "30" # Leave it blank if not applicable
    num: "10" # Leave it blank if not applicable
    pp: "1131-1138" # Leave it blank if not applicable
    year: "2024" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2024-04-01" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2024-current-sensor.png" # Representative image of the paper
abstract: "
Because current information is the most crucial factor for the state estimation of battery management systems, it is essential to ensure the accuracy of the current-sensor built into battery systems. However, non-contact current-sensors, which are widely used in battery systems, are sensitive to operational conditions and the environment. The accuracy of the sensor is easily affected by various factors, such as temperature changes or unstable supply voltages. This study proposes a current-sensor error compensation algorithm to overcome the potential inaccuracies caused by various current-sensor faults. This method is based on the dual sigma-point Kalman filter, which enables simultaneous estimation of the internal states of the battery cell and the bias of the current measurement. To verify the effectiveness of the proposed method, three types of possible current-sensor errors step, ramp, and sinusoidal errors were subjected to current measurement. The effectiveness of the proposed algorithm was verified using a cylindrical battery cell, and the experimental results showed that the proposed method could estimate and compensate for all current measurement errors.
"
# links: # additional links;
#   - name: 
#     url: 
---