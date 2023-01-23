# DISRPT/sharedtask2023

Repository for DISRPT2023 shared task Discourse Unit Segmentation, Connective Detection and Discourse Relation Classification.  

**Please check our [FAQ](https://sites.google.com/view/disrpt2023/home) page on our main [website](https://sites.google.com/view/disrpt2023/home) for more information about the Shared Task, Participation, and Evaluation etc.!**  


**Shared task participants are encouraged to follow this repository in case bugs are found and need to be fixed.** 


## Introduction

The [DISRPT 2023](https://sites.google.com/view/disrpt2023/home) shared task, held in conjonction with [CODI 2023](https://sites.google.com/view/codi-2023/) and [ACL 2023](https://2023.aclweb.org/), introduces the third iteration of a cross-formalism shared task on **discourse unit segmentation** and **connective detection**, as well as the second iteration of a cross-formalism **discourse relation classification** task.

We *will* provide training, development and test datasets from all available languages and treebanks in the **RST**, **SDRT**, **PDTB** and **dependency** formalisms, using a uniform format. Because different corpora, languages and frameworks use different guidelines, the shared task is meant to promote design of flexible methods for dealing with various guidelines, and help to push forward the discussion of standards for computational approaches to discourse relations. We include data for evaluation with and without gold syntax, or otherwise using provided automatic parses for comparison to gold syntax data.

## Types of Data
The tasks are oriented towards finding the locus and type of discourse relations in texts, rather than predicting complete trees or graphs. For frameworks that segment text into non-overlapping spans covering each entire documents (RST and SDRT), the segmentation task corresponds to finding the **starting point of each discourse unit**. For PDTB-style datasets, the unit-identification task is to identify the **spans of discourse connectives** that explicitly identify the existence of a discourse relation. These tasks use the files ending in `.tok` and `.conllu` for the **plain** text and **parsed** scenarios respectively.  

For relation classification, two discourse unit spans are given in text order together with the direction of the relation and context, using both plain text data and stand-off token index pointers to the treebanked files. Information is included for each corpus in the `.rels` file, with token indices pointing to the `.tok` file, though parse information may also be used for the task. The column to be predicted is the final label column; the penultimate `orig_label` column gives the original label from the source corpus, which may be different, for reference purposes only. This column may not be used. The relation direction column may be used for prediction and does not need to be predicted by systems (essentially, systems are labeling a kind of ready, unlabeled but directed dependency graph).  

External resources are allowed, including NLP tools, word embeddings/pre-trained language models, and **other** gold datasets for MTL etc. However, no further gold annotations of the datasets included in the task may be used (example: you may not use OntoNotes coref to pretrain a system that will be tested on WSJ data from RST-DT or PDTB, since this could contaminate the evaluation; exception: you may do this if you exclude WSJ data from OntoNotes during training).  

Note that some datasets contain **discontinuous** discourse units, which sometimes nest the second unit in a discourse relation. In such cases, the unit beginning first in the text is considered `unit1` and gaps in the discourse unit are given as `<*>` in the inline text representation. Token index spans point to the exact coverage of the unit either way, which in case of discontinuous units will contain multiple token spans.  

<!---
*Note about MWE*..............
--->


## Directories

The shared task repository currently comprises the following directories (to be extended as the task progresses):

  * data - individual corpora from various languages and frameworks (**for now, data samples**). 
    * Folders are given names in the scheme `LANG.FRAMEWORK.CORPUS`, e.g. `eng.rst.gum` is the directory for the GUM corpus, which is in English and annotated in the framework of Rhetorical Structure Theory (RST).
    * Note that some corpora (eng.rst.rstdt, eng.pdtb.pdtb, tur.pdtb.tdb, zho.pdtb.cdtb) **do not contain text** or have some documents without text (eng.rst.gum) and text therefore needs to be reconstructed using `utils/process_underscores.py`.
  * utils - **COMING SOON** scripts for validating, evaluating and generating data formats. The official scorer for segmentation and connective detection is `seg_eval.py`, and the official scorer for relation classification is `rel_eval.py`.

See the README files in individual data directories for more details on each dataset.

## Surprise language

At the release of the test data, a surprise language dataset will be added! We will disclose the language for this future corpus soon, to allow teams to be ready.


## Submitting a System

Systems should be accompanied by a regular workshop paper in the ACL format, as described on the CODI workshop website. During submission, you will be asked to supply a URL from which your system can be downloaded. If your system does not download necessary resources by itself (e.g. word embeddings), these resources should be included at the download URL. The system download should include a README file describing exactly how paper results can be reproduced. Please do not supply pre-trained models, but rather instructions on how to train the system using the downloaded resources and **make sure to seed your model** to rule out random variation in results. For any questions regarding system submissions, please contact the organizers.

## Important Dates
- January, 2023 &nbsp; &nbsp; &nbsp; &nbsp; Sample release  
- February, 15th, 2023 &nbsp; &nbsp; &nbsp; &nbsp; Train/dev dataset release  
- April, 15th, 2023 &nbsp; &nbsp; &nbsp; &nbsp; Test release  
- May, 8st, 2023 &nbsp; &nbsp; &nbsp; &nbsp; System release
- June, 5th, 2023 &nbsp; &nbsp; &nbsp; &nbsp; Camera ready
- July, 9-14th, 2023  &nbsp; &nbsp; &nbsp; &nbsp; Workshop/Conference, Toronto, Canada.

<!---
## Directories

## Surprise language

## Statistics
--->
