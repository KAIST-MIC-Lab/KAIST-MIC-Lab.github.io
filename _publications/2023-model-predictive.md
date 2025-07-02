---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Model Predictive Torque Control of Synchronous Machines Without a Current or Stator Flux Reference Generator" # Title of the paper
krtitle: # only for domestic papers
authors: "<u>Kyunghwan Choi</u>, Ki-Bum Park&#42;"
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "International Symposium on Industrial Electronics (ISIE)"
    doi: "10.1109/ISIE51358.2023.10228177" # Leave it blank if not applicable
    vol:  # Leave it blank if not applicable
    num:  # Leave it blank if not applicable
    pp: "1-6" # Leave it blank if not applicable
    year: "2023" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2023-08-31" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2023-model-predictive.png" # Representative image of the paper
abstract: "
Conventional model predictive torque control (MPTC) of synchronous machines (SMs) relies on a current or stator flux reference generator to attract the d-axis current or stator flux to desired operating points while minimizing the torque error. However, using a reference generator has two issues: 1) an additional demanding optimization is required to obtain the reference generator, and 2) the additional optimization restricts the degrees of freedom (DOF) for MPTC to determine the operating points of SMs. Therefore, this study presents an MPTC scheme that does not rely on a current or stator flux reference generator. To this end, first, a novel MPTC problem is formulated to minimize a performance index while satisfying the torque, voltage, and current constraints. The performance index, e.g., copper loss or inverter loss, determines how the MPTC utilizes the DOF in the torque control. Then, the proposed MPTC problem, a nonlinear optimization, is solved based on the finite control set (FCS) using the Augmented Lagrangian method. Simulation results obtained using a 50-kW SM show that 1) the proposed MPTC guarantees optimal operation under all operating regions without a reference generator, and 2) it can significantly enhance efficiency by utilizing its DOF in determining the operating point.
"
# links: # additional links;
#   - name: 
#     url: 
---