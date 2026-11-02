---
type: "Journal Paper" # Conference Paper, Journal Paper, Ph.D. Thesis, Master's Thesis
layout: publication # Do not change this
group: publications # Do not change this
title: "Reverse Path Tracking Control Methods for Tractor Trailers Using Trailer Steering System" # Title of the paper
# krtitle: # only for domestic papers
authors: 
# Kyumin Lee and Yonghwan Jeong
  - name: "Kyumin Lee"
  - name: "Yonghwan Jeong"
    corresponding: true # true if this author is the corresponding author
domestic_or_international: "International" # "International" or "Domestic"
pub: # Publication information - REMOVE THIS FIELD IF NOT APPLICABLE!
  - name: "Journal of Mechanical Science and Technology"
    pub_url: "https://link.springer.com/journal/12206" # conference or journal URL (not your paper URL)
    pdf: "/static/pub/2025-reverse-path.pdf"
    doi: "10.1007/s12206-025-1108-2" # Leave it blank if not applicable
    vol: 39 # Leave it blank if not applicable
    num: 12 # Leave it blank if not applicable
    pp: "7399-7407" # "380-385" # Leave it blank if not applicable
    year: 2025 # "2025" # Leave it blank if not applicable
    state: "published" # published, accepted, submitted
    bib: # "/static/pub/2025-imposing.bib" # Leave it blank if not applicable
pub_date: "2025-12-01" # Date of publication. Change Techrxiv (or other preprint) date to Journal date once published.
image: "/static/pub/2025-reverse-path.png" # Representative image of the paper
abstract: "
  This paper presents a control strategy to enhance **high-curvature trajectory tracking** in **tractor-trailer reverse maneuvers**. This study incorporates **rear-wheel steering control of the trailer**, enabling more flexible movement and improved trajectory tracking performance.


  The control system consists of two components: a **trailer rear-wheel steering controller**, which aligns the trailer's rear end with the target path, and a **tractor front-wheel steering controller**, which stabilizes the hitch angle. Geometric analysis is used to derive methods for calculating both the target curvature toward the desired point and the trailer's current curvature. Additionally, a novel approach for determining lateral error is proposed, utilizing a local coordinate system with the trailer's rear end as the origin.


  The control system is designed using Simulink and simulated through TruckSim. The results demonstrate improved reverse path tracking performance when following a high-curvature trajectory with discontinuous curvature changes.
"
---
