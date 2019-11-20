# mantis-ml 

- [Introduction](#introduction) 
- [Installation](#installation) 
- [Run](#run) 



Introduction
============
`mantis-ml` is a disease-agnostic gene prioritisation framework, implementing stochastic semi-supervised learning on top of `scikit-learn` and `keras`/`tensorflow`.  
`mantis-ml` takes its name from the Greek word 'μάντης' which means 'fortune teller', 'predicter'.

<br>

|Citation: |
| :---- |
|Vitsios Dimitrios, Petrovski Slavé. **Stochastic semi-supervised learning to prioritise genes from high-throughput genomic screens**. <br/>
https://www.biorxiv.org/content/10.1101/655449v1 bioRxiv, May 30, 2019, [doi:10.1101/655449](https://doi.org/10.1101/655449) |

<br>

| Gene prioritisation Atlas: |
| :---- |
| [https://dvitsios.github.io/mantis-ml-predictions](https://dvitsios.github.io/mantis-ml-predictions) |
| This resource contains gene prediction results extracted by **mantis-ml** across **10 disease areas** in **6 specialties**: _Cardiology_, _Immunology_, _Nephrology_, _Neurology_, _Psychiatry_ and _Pulmonology_. |


<br>

Installation
============
**Requirements:** `Python3` (tested with v3.6.7)

<br>

`mantis-ml` can be installed through `pip`:
```
pip install mantis-ml
```

<br>

Alternatively, it can be installed from the github repository:

```
git clone https://github.com/astrazeneca-cgr-publications/mantis-ml-release.git
python setup.py install
```

<br>

---

In either case, it is highly recommended to **create a new virtual environment** (e.g. with `conda`) before installing `mantis-ml`:
```
conda create -n mantis_ml python=3.6
conda config --append channels conda-forge   	# add conda-forge in the channels list
conda activate mantis_ml			# activate the newly created conda environment
```

---

<br>


You may now call the following scripts from the command line:
- **`mantisml`**: run mantis-ml gene prioritisation based on a provided config file (`.yaml`)
- **`mantisml-preview`**: preview selected phenotypes and features based on a provided config file
- **`mantisml-overlap`**: run enrichment test between mantis-ml predictions and an external ranked gene list to get refined gene predictions

Run each command with `-h` to see all available options.


<br><br>



Run
===

You need to provide a config file (`.yaml`) containing information about the diseases/phenotypes of interest.
<br>


#### Required field:
- `Disease/Phenotype terms`: **terms that characterise a phenotype or disease of interest**


#### Optional fields:
- `Additional associated terms`: terms used along with `Disease/Phenotype terms` to extract additional disease/phenotype-associated features
- `Diseases/Phenotypes to exclude`: terms to exclude from disease/phenotype characterisation and feature selection


<br>


**Config examples**:
```
# Epilepsy_config.yaml
Disease/Phenotype terms: epileptic, epilepsy, seizure
Additional associated terms: brain, nerve, nervous, neuronal, cerebellum, cerebral, hippocampus, hypothalamus
Diseases/Phenotypes to exclude: 
```
```
# CKD_config.yaml
Disease/Phenotype terms: renal, kidney, nephro, glomerul, distal tubule 
Additional associated terms: 
Diseases/Phenotypes to exclude: adrenal
```

Other example config files can be found under `mantis-ml/conf`. 

<br>




## `mantisml`
You need to provide a config file (`.yaml`) and an output directory. 
<br>
You may also define the number of threads to use (`-n` option; default value: 4).
```
mantisml -c [config_file] -o [output_dir] [-n nthreads]
```

#### Example
```
mantisml -c CKD_config.yaml -o ./CKD-run
mantisml -c Epilepsy_config.yaml -o /tmp/Epilepsy-testing -n 20
```


#### `mantisml` Output
`mantisml` predictions for all genes and across all classifiers can be found at **`[output_dir]/Gene-Predictions`**. 
<br>
The `AUC_performance_by_Classifier.pdf` file under the same dir contains information about the AUC performance per classifier and thus informs about the best performing classifier.

Output figures from all steps during the `mantis-ml` run (e.g. *Exploratory Data Analysis/EDA, supervised-learning, unsupervised-learning*) can be found under **`[output_dir]/Output-Figures`**.

<br>

## `mantisml-profiler`

#### Preview selected phenotypes and features (optional)
You may preview all selected phenotypes and relevant features based on your input config file parameters by running the `mantisml-profiler` command.
<br>

To run `mantisml-profiler`, you need to provide a config file (`.yaml`) and an output directory.
```
mantisml-profiler [-v] -c [config_file] -o [output_dir]
```

<br><br>

## `mantisml-overlap`
#### Run enrichment test between mantis-ml predictions and an external ranked gene list to get refined gene predictions

To run `mantisml-overlap`, you need to provide a config file (`.yaml`), an output directory with `mantisml` results and an external ranked gene list file (`mantisml` has to be run already given the same ouput directory).
```
mantisml-overlap -c [config_file] -o [output_dir] -e [external_ranked_file]
```


#### `mantisml-overlap` Output
Results are available under **`[output_dir]/Overlap-Enrichment-Results`**.

- `mantisml-overlap` generates figures with the enrichment signal between mantis-ml predictions and the external ranked file, based on a hypergeometric test. 
These can be found under: **`Overlap-Enrichment-Results/hypergeom-enrichment-figures`**.

- `mantisml-overlap` also extracts consensus gene predictions with support by multiple classifiers. 
Results can be found at **`Overlap-Enrichment-Results/Gene-Predictions-After-Overlap`**.


