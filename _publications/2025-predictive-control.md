---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Predictive Control of a Dog-Clutch Transmission via a Transformer-Based Velocity Prediction" # Title of the paper
krtitle: # only for domestic papers
authors:
  - name: "Geunyoung Park"
  - name: "Kyunghwan Choi"
  - name: "Dongsuk Kum"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "IEEE Transactions on Vehicular Technology"
    doi: "10.1109/TVT.2024.3468390" # Leave it blank if not applicable
    vol:  "74"
    num:  "5"
    pp: "7430-7443" # Leave it blank if not applicable
    year: "2025" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2025-05-01" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-predictive-control.png" # Representative image of the paper
abstract: "
Despite the advantages of better torque and greater speeds when using a transmission, electric vehicles (EVs) often forgo this component due to energy losses and the added cost and weight. A promising solution to these issues is to use a dog-clutch transmission. However, this introduces a new problem related to drivability, known as a torque hole, which hinders the implementation of dog-clutch transmissions in EVs. This paper proposes a novel preview gear-shifting strategy that adopts a two-motor architecture and utilizes predictive control to eliminate the torque hole problem. The optimal control problem is formulated to minimize torque holes while ensuring that drivability is not significantly compromised and system efficiency is maximized. The predictive control scheme leverages model predictive control (MPC) by incorporating forecasts of the vehicle's short-term velocity. In order to achieve accurate predictions, this paper utilizes a transformer network with headway distance and vehicle-to-infrastructure (V2I) information. The results demonstrate that the proposed prediction model can drastically enhance the performance of velocity predictions. Furthermore, the proposed gear-shifting strategy with high prediction accuracy can substantially mitigate torque holes compared to a non-predictive strategy, effectively addressing the challenges of a torque hole issue. Consequently, this approach offers new prospects for developing electric vehicle transmissions with dog clutches.
"
# links: # additional links;
#   - name: 
#     url: 
---