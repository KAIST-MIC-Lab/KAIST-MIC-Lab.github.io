---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "A Current Sensor Fault-detecting Method for Onboard Battery Management Systems of Electric Vehicles Based on Disturbance Observer and Normalized Residuals" # Title of the paper
krtitle: # only for domestic papers
authors: # List of authors
  - name: "Wooyong Kim"
  - name: "Kunwoo Na"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Journal of Control, Automation and Systems"
    doi: 10.1007/s12555-023-0377-8 # Leave it blank if not applicable
    vol:  "21"
    num:  "11"
    pp: "3563-3573" # Leave it blank if not applicable
    year: "2023" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2023-11-04" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2023-current-sensor.png" # Representative image of the paper
abstract: "
This study presents a current sensor fault-detecting method for an electric vehicle battery management system. The proposed current sensor fault detector comprises the nonlinear battery cell model, the Luenberger-type state estimator, and a disturbance observer-based current residual generator. The features of this study are summarized as follows: 1) A nonlinear state space representation of the battery cell model is derived so that the disturbance observer considering the engaged current as an external disturbance can be applied, 2) a nonlinear model-based state observer and disturbance observer are combined to deal with the state of charge estimation as well as the unknown current estimation and 3) the concept of the normalized residual is introduced for current sensor fault detection criteria. Because the proposed method can estimate the engaged current whether the current measurement is available or not, the residual between the estimated current and measured current can capture the current sensor fault. Additionally, the normalization process ensures the current sensor fault diagnosis can be realized regardless of the magnitude of the engaged current. The performance of the proposed current sensor fault algorithm was experimentally verified under several magnitudes of engaged current scenarios using a single battery cell.
"
# links: # additional links;
#   - name: 
#     url: 
---