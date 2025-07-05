---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Neural Network-based Nonlinearity Estimation of Voltage Source Inverter for Synchronous Machine Drives" # Title of the paper
krtitle: "동기전동기 구동용 전압원 인버터의 인공 신경망 기반 비선형성 추정" # only for domestic papers
authors: # List of authors
  - name: "Yeongho Jeong"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "Domestic" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "제어로봇시스템학회 (ICROS)"
    doi: # Leave it blank if not applicable
    year: "2024" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
    pdf: "/static/pub/2024-neural-network-based-nonlinearity.pdf"
    pp: "312-313"
    url: "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11908882"
pub_date: "2024-7-2" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2024-neural-network-based-nonlinearity.png" # Representative image of the paper
abstract: "
  This  paper  investigates  the  concept  of  using  a  **neural  network  (NN)-based  approach**  for  the nonlinearity estimation of voltage source inverter (VSI) in synchronous machine (SM) drives. The proposed scheme utilizes an NN with one hidden layer to model the VSI nonlinearity, accompanied by an adaptive law that ensures stability and bounded weights during the NN's update process. Assuming known stator flux linkages, the study primarily evaluates the feasibility of applying NN for this estimation. Simulation results from a 35 kW SM drive indicate that the proposed estimator successfully tracks the actual value of the VSI nonlinearity, demonstrating its efficacy. 
"

additional: # additional information such as awards, etc.
#  - "📄 Awarded **Best Paper Award** at the _2025 European Control Conference (ECC)_."

# links: # additional links;
#   - name: DBpia Online
#     url: 
---