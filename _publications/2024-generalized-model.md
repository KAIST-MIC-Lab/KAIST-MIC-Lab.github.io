---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Generalized Model Predictive Torque Control of Synchronous Machine" # Title of the paper
krtitle: # only for domestic papers
authors: # List of authors
  - name: "Kyunghwan Choi"
  - name: "Jongseok Kim"
  - name: "Ki-Bum Park"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "IEEE/ASME Transactions on Mechatronics"
    doi: "10.1109/TMECH.2024.3461209" # Leave it blank if not applicable
    vol:  # Leave it blank if not applicable
    num:  # Leave it blank if not applicable
    pp: "1-11" # Leave it blank if not applicable
    year: "2024" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
pub_date: "2024-11-04" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2024-generalized-model.png" # Representative image of the paper
abstract: "
This study presents a generalized model predictive torque control (GMPTC) method that applies to all types of synchronous machines (SMs). The GMPTC method aims to minimize both torque error and performance index (PI) while adhering to voltage and current constraints. The PI can be defined by any function to be minimized to enhance the SM drive's performance, such as copper loss and inverter loss. The GMPTC problem, a nonlinear optimization problem, is solved based on either a continuous control set or a finite control set using the augmented Lagrangian method. The GMPTC method guarantees optimal operation across all regions, including maximum torque per ampere, flux weakening, maximum current, and maximum torque per voltage, without needing additional controllers. The GMPTC method is practical, requiring only a few tuning parameters (four to five), making it easy to implement. The method's effectiveness is demonstrated by numerical control of a 385-W synchronous reluctance machine and experimental control of a 1-kW interior permanent magnet SM.
"
# links: # additional links;
#   - name: 
#     url: 
---