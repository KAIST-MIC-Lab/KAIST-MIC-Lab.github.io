---
type: "Conference Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Water–Thermal Management of FCEVs Based on Adaptive Equivalent Consumption Minimization Strategy" # Title of the paper
# krtitle: # only for domestic papers
authors: 
  - name: "Geunyoung Park"
  - name: "Kyunghwan Choi"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "American Control Conference (ACC)"
    pub_url: "https://acc2027.a2c2.org"
    pdf: "/static/pub/2027-water-thermal.pdf"
    doi: # Leave it blank if not applicable
    vol: # Leave it blank if not applicable
    num: # Leave it blank if not applicable
    pp: # "380-385" # Leave it blank if not applicable
    year: "2027" # Leave it blank if not applicable
    state: "submitted" # published, accepted, submitted
    # pres: "/static/pub/2026-vector-space-pres.pdf" # Leave it blank if not applicable
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2026-12-31" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
# pub_date: "2027-07-09" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2027-water-thermal.png" # Representative image of the paper
# github: # Leave this blank if not applicable
#  - name: # "CONAC/ECC25-weight-constraint" # GitHub repository name
#    url: # "KAIST-MIC-Lab/CoNAC/tree/ECC25-weight-constraint" # GitHub repository URL
#    description: # "Code for the paper" # Description of the repository
# abstract; emphasize the important part using **bold** or *italic* of markdown syntax
abstract: "
  Thermal management of fuel cell electric vehicles must minimize auxiliary energy consumption while keeping component temperatures within allowable ranges, yet the temperature flexibility of the stack is limited by membrane hydration. This study proposes a water–thermal adaptive equivalent consumption minimization strategy (WT-AECMS) that coordinates system-level heat allocation using requested heat-transfer rates as control inputs. Stack water dynamics determine hydration-dependent temperature bounds, and adaptive costates account for the component temperatures relative to their admissible ranges. The strategy is evaluated through high-fidelity GT-SUITE/Python co-simulation over the WLTC at an ambient temperature of−10 ◦C. WT-AECMS reduces the energy consumption of the vehicle thermal management system by approximately 61% relative to the baseline controller while improving thermal and hydration constraint satisfaction. Compared with thermal-only AECMS, it increases the allowable hydration time ratio from 0.70 to 1.00 with approximately 2% additional energy consumption, indicating that membrane hydration can be maintained while preserving most of the energy savings of thermal optimization.
"
---