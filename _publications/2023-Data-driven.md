---
type: "Conference Paper"
layout: publication
group: publications
title: "Data-driven Modeling of Model Residuals for Linear Model Predictive Control of Nonlinear Systems"
krtitle: "비선형 시스템의 선형모델예측제어를 위한 데이터 기반 시스템 잔차 모델링"
authors: 
  - name: "Myeongseok Ryu"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "Domestic"
pub: 
  - name: 제어로봇시스템학회 (ICROS)
    doi: 
    year: "2023"
    pdf: "/static/pub/2023-Data-driven.pdf"
    state: "published"
    url: "https://www.dbpia.co.kr/journal/articleDetail?nodeId=NODE11480596"
    pp: 837-838
pub_date: "2023-06-21" #Date of publication. Change from Biorxiv date to Journal date once accepted
image: "/static/pub/2023-Data-driven.png"
abstract: "
  An accurate system model is essential for predictive control schemes that use the system model to predict the future trajectory of states. To describe the system model precisely including residual terms, nonlinear approximators like the neural network can be used. However, training the whole system model needs big sample dataset which is hard to collect from the real environment. Thus, recent research focuses on high sample-efficient learning methods that utilize a pre-driven analytic model. In this paper, we propose to train only the residual terms in the system model from the dataset obtained by subtracting the analytic terms from the real data. A simulation study demonstrates modeling the residuals terms, the proposed method, ensures faster and more accurate learning than modeling the whole system model.
"
additional: "📄 Awarded <span style=\"color: goldenrod;\"><strong>Best Paper Award</strong></span> at the _2023 Institute of Control, Robotics and Systems (ICROS) Conference_."
# links:
#   - name: 
#     url: 
---