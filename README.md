# The S2 subunit of spike encodes diverse targets for functional antibody responses to SARS-CoV-2
Jamie Guenthoer<sup>1</sup>, Meghan E. Garrett<sup>1</sup>, Michelle Lilly<sup>1</sup>, Delphine M. Depierreux<sup>1</sup>, Felicitas Ruiz<sup>1</sup>, Margaret Chi<sup>1</sup>, Caitlin I. Stoddard<sup>1</sup>, Vrasha Chohan<sup>1</sup>, Kevin Sung<sup>2</sup>, Duncan Ralph<sup>2</sup>, Helen Y. Chu<sup>3</sup>, Frederick A. Matsen IV<sup>2,4</sup>, Julie Overbaugh<sup>1,2*<sup>

<sup>1</sup>Human Biology Division, Fred Hutchinson Cancer Center, Seattle, WA 98109, USA</br>
<sup>2</sup>Public Health Sciences Division, Fred Hutchinson Cancer Center, Seattle, WA 98109, USA</br>
<sup>3</sup>Division of Allergy and Infectious Diseases, University of Washington, Seattle, WA 98195, USA</br>
<sup>4</sup>Howard Hughes Medical Institute, Seattle, WA 98195, USA</br>

<sup>*</sup>Corresponding Author</br>

## Abstract

The SARS-CoV-2 virus responsible for the COVID-19 global pandemic has exhibited a striking capacity for viral evolution that drives continued evasion from vaccine and infection-induced immune responses. Mutations in the receptor binding domain of the S1 subunit of the spike glycoprotein have led to considerable escape from antibody responses, reducing the efficacy of vaccines and monoclonal antibody (mAb) therapies. Therefore, there is a need to interrogate more constrained regions of Spike, such as the S2 subdomain. Here, we describe a collection of S2 mAbs from two SARS-CoV-2 convalescent individuals that target multiple regions in the S2 subdomain and can be grouped into at least five epitope classes. Most did not neutralize SARS-CoV-2 with the exception of C20.119, which bound to a highly conserved epitope in the fusion peptide and showed broad binding and neutralization activity across SARS-CoV-2, SARS-CoV-1, and closely related zoonotic sarbecoviruses. Several of the S2 mAbs tested mediated antibody-dependent cellular cytotoxicity (ADCC) at levels similar to the S1 mAb S309 that was previously authorized for treatment of SARS-CoV-2 infections. Three of the mAbs with ADCC function also bound to spike trimers from HCoVs, such as MERS-CoV and HCoV-HKU1. Our findings suggest there are diverse epitopes in S2, including functional S2 mAbs with HCoV and sarbecovirus breadth that likely target functionally constrained regions of spike. These mAbs could be developed for potential future pandemics, while also providing insight into ideal epitopes for eliciting a broad HCoV response.

## Overview
The code for downstream analyses and generation of plots for some figures in the manuscript is provided here.

## Environment Setup
Currently, the environment is set up with [Conda](https://docs.conda.io/en/latest/) and `pip`. Clone this repository and create the `sars2-s2-env` environment as follows:
```sh
git clone https://github.com/matsengrp/SARS-CoV-2-S2-Abs
cd SARS-CoV-2-S2-Abs
conda create -n sars2-s2-env python=3.8.10
conda activate sars2-s2-env
python -m pip install -r requirements.txt
```
Once the environment has been created, only the `conda activate sars2-s2-env` command call is needed next time before running the code.

## Figure 6A,B
The plots for Figure 6A and 6B are generated with `plot_20C_mAbs_phage-dms_preFP-FP.ipynb`.

## Figure S9
Figure S9 is generated with `plot_plasma_enrichment.ipynb`.

## Figure S10
Figure S10A is generated with `heatmap-S2-mAbs-PhageDMS.ipynb`, and Figure S10B is generated with `heatmap-S2-mAbs-PanCoV.ipynb`.

## Figure S11
The plots in Figure S11 are generated with `plot_mAbs_enrichment.ipynb`.