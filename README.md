# DISRPT/sharedtask2023

**Update 04/05/23: datasets have been updated, don't forget to pull the new data files.**

**Update 19/04/23: datasets have been updated, don't forget to pull the new data files.**

**Update 17/04/23: test and surprise data has been released!**


~~**Update 17/03/23: data have been updated, don't forget to pull the new data files.**~~

Repository for DISRPT2023 Shared Task on Discourse Unit Segmentation, Connective Detection, and Discourse Relation Classification.  

**Please check our [FAQ](https://sites.google.com/view/disrpt2023/faq?authuser=0) page on our main [website](https://sites.google.com/view/disrpt2023/home) for more information about the Shared Task, Participation, and Evaluation etc.!**  

**Important Update (02/22/2023)**: Stable training and development data ~~will be~~ has been released! 
Test data as well as surprise datasets will be released in April 2023! 

**Shared task participants are encouraged to follow this repository in case bugs are found and need to be fixed.** 


## Introduction

The [DISRPT 2023](https://sites.google.com/view/disrpt2023/home) shared task, to be held in conjunction with [CODI 2023](https://sites.google.com/view/codi-2023/) and [ACL 2023](https://2023.aclweb.org/), introduces the third iteration of a cross-formalism shared task on **discourse unit segmentation** and **connective detection**, as well as the second iteration of a cross-formalism **discourse relation classification** task.

We *will* provide training, development, and test datasets from all available languages and treebanks in the **RST**, **SDRT**, **PDTB** and **dependency** formalisms, using a uniform format. 
Because different corpora, languages and frameworks use different guidelines, the shared task is meant to promote design of flexible methods for dealing with various guidelines, and help to push forward the discussion of standards for computational approaches to discourse relations. We include data for evaluation with and without gold syntax, or otherwise using provided automatic parses for comparison to gold syntax data.


## Types of Data
The tasks are oriented towards finding the locus and type of discourse relations in texts, rather than predicting complete trees or graphs. For frameworks that segment text into non-overlapping spans covering each entire documents (RST and SDRT), the segmentation task corresponds to finding the **starting point of each discourse unit**. For PDTB-style datasets, the unit-identification task is to identify the **spans of discourse connectives** that explicitly identify the existence of a discourse relation. These tasks use the files ending in `.tok` and `.conllu` for the **plain** text and **parsed** scenarios respectively.  

For relation classification, two discourse unit spans are given in text order together with the direction of the relation and context, using both plain text data and stand-off token index pointers to the treebanked files. Information is included for each corpus in the `.rels` file, with token indices pointing to the `.tok` file, though parse information may also be used for the task. The column to be predicted is the final label column; the penultimate `orig_label` column gives the original label from the source corpus, which may be different, for reference purposes only. This column may not be used. The relation direction column may be used for prediction and does not need to be predicted by systems (essentially, systems are labeling a kind of ready, unlabeled but directed dependency graph).  

Note that some datasets contain **discontinuous** discourse units, which sometimes nest the second unit in a discourse relation. In such cases, the unit beginning first in the text is considered `unit1` and gaps in the discourse unit are given as `<*>` in the inline text representation. Token index spans point to the exact coverage of the unit either way, which in case of discontinuous units will contain multiple token spans.  


### Notes on Discourse Relations

Compared to the data of the 2021 shared task, we made a few corrections as some instances' labels contained spelling errors: 'anthitesis', 'motibation' and 'backgroun'.

We also decided to make a few changes in the original labels provided in some corpora to harmonize the names of the relations. **But please note that this does not mean that relations with the same names in different corpora are defined in the exact same way, each relation definition is specific to an annotation project.**
We do the following modifications, while keeping the original label in the penultimate column:
* original `topicomment` mapped to `topic-comment`,
* original `topichange` mapped to `topic-change`,
* original `topidrift` mapped to `topic-drift`,
* original `solution-hood` mapped to `solutionhood`,
* original `non-volitional-cause` mapped to `nonvolitional-cause`,
* original `non-volitional-result` mapped to `nonvolitional-result`,
* original `e-elab`  mapped to `e-elaboration`


<!---
*Note about MWE*..............
--->


## Rules
External resources are allowed, including NLP tools, word embeddings/pre-trained language models, and **other** gold datasets for MTL etc. However, no further gold annotations of the datasets included in the task may be used (example: you may not use OntoNotes coref to pretrain a system that will be tested on WSJ data from RST-DT or PDTB, since this could contaminate the evaluation; exception: you may do this if you exclude WSJ data from OntoNotes during training).

**Training with dev is not allowed.** One could do so (e.g. as an experiment) and report the resulting scores in their paper, but such results will not be considered / reported as the official scores of the system in the overall ranking. 

Please also make sure to use seeds to keep performance as reproducible as possible!


## Evaluation

Evaluation scripts are provided for all tasks under [`utils`](https://github.com/disrpt/sharedtask2023/tree/main/utils).
In general, final results of each dataset will be reported on the corresponding`test` partition. 

**For datasets without a corresponding training set** (e.g. `eng.dep.covdtb`, `tur.pdtb.tedm`):  

- The scores will be reported as any other regular datasets on the `test` partition 
using the relation inventory of each respective dataset
  - one can collapse relations in any way one would like to during training, but the final results will be reported on each dataset's own relation labels, as indicated in the last column (i.e. `label`) in the corresponding test `.rels` file. 
- Systems can be trained on either a corpus with the same language or any other combination of the datasets available in DISRPT 2023. 
- For better interpretation of the results, we kindly ask you to 
  - document the composition of the training data in your README.md file as well as the paper describing the system. 
  - also report model performance on `dev` sets (wherever applicable) in the paper describing the system (this can go into the appendix of the paper)



## Directories

The shared task repository currently comprises the following directories:

  * `data` - individual corpora from various languages and frameworks. 
    * Folders are given names in the scheme `LANG.FRAMEWORK.CORPUS`, e.g. `eng.rst.gum` is the directory for the GUM corpus, which is in English and annotated in the framework of Rhetorical Structure Theory (RST).
    * Note that some corpora (eng.rst.rstdt, eng.pdtb.pdtb, tur.pdtb.tdb, zho.pdtb.cdtb) **do not contain text** or have some documents without text (eng.rst.gum) and text therefore needs to be reconstructed using `utils/process_underscores.py`.
  * `utils` - scripts for validating, evaluating and generating data formats. The official scorer for segmentation and connective detection is `seg_eval.py`, and the official scorer for relation classification is `rel_eval.py`.

See the README files in individual data directories for more details on each dataset.


## Surprise Language(s)
[17/04/2023] The Thai Discourse Treebank (TDTB) is our surprise language/dataset! 
We also include a few out-of-domain datasets to challenge the robustness and generalizability of your system! 

~~At the release of the test data, surprise language datasets will be added! We will disclose the languages for these corpora soon, to allow teams to be ready.~~ 


## Submitting a System

Systems should be accompanied by a regular workshop paper in the ACL format, as described on [the CODI workshop website](https://sites.google.com/view/codi-2023/call-for-papers?authuser=0). During submission, you will be asked to supply a URL from which your system can be downloaded. If your system does not download necessary resources by itself (e.g. word embeddings), these resources should be included at the download URL. The system download should include a README file describing exactly how paper results can be reproduced. Please do not supply pre-trained models, but rather instructions on how to train the system using the downloaded resources and **make sure to seed your model** to rule out random variation in results. For any questions regarding system submissions, please contact the organizers.

## Important Dates
- ~~January 2023&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sample release~~
- ~~February 22nd, 2023&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`train`/`dev` dataset release~~
- **April 17th, 2023&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`test` release**
- May 8th, 2023&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;System release
- June 1st, 2023&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Camera ready
- July 13-14th, 2023  &nbsp; &nbsp; &nbsp; &nbsp; CODI Workshop, ACL, Toronto, Canada.


## Statistics

**02/22/2023**: Please note that the following table currently only includes statistics corresponding to `train`+`dev`.
We will update the table to also include the `test` partition in each dataset upon the release of the test data in April.

[//]: # (**02/22/2023**: Please note that the following table currently only includes statistics corresponding to `train`+`dev`.)

[//]: # (We will update the table to also include the `test` partition in each dataset upon the release of the test data in April. )


| corpus | lang | framework | rels | discont | train_toks | train_sents | train_docs | train_segs | dev_toks | dev_sents | dev_docs | dev_segs | test_toks | test_sents | test_docs | test_segs | total_sents | total_toks | total_docs | total_segs | seg_style | underscored | syntax | MWTs | ellip |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| deu.rst.pcc | deu | rst | 2,665 | no | 26,831 | 1,773 | 142 | 2,471 | 3,152 | 207 | 17 | 275 | 3,239 | 213 | 17 | 294 | 2,193 | 33,222 | 176 | 3,040 | EDU | no | UD | no | no |
| eng.dep.covdtb | eng | dep | 4,985 | 29,405 | 1,162 | 150 | 2,754 | 31,502 | 1,181 | 150 | 2,951 | 0 | 0 | 0 | 0 | 2,343 | 60,907 | 300 | 5,705 | EDU | no | UD | yes | no |
| eng.dep.scidtb | eng | dep | 9,904 | yes | 62,488 | 2,570 | 492 | 6,740 | 20,299 | 815 | 154 | 2,130 | 19,747 | 817 | 152 | 2,116 | 4,202 | 102,534 | 798 | 10,986 | EDU | no | UD | yes | no |
| eng.pdtb.pdtb | eng | pdtb | 47,851 | yes | 1,076,448 | 44,563 | 1,992 | 23,850 | 40,384 | 1,703 | 79 | 953 | 56,547 | 2,364 | 91 | 1,245 | 48,630 | 1,173,379 | 2,162 | 26,048 | Conn | yes | UD (gold) | yes | no |
| eng.pdtb.tedm | eng | pdtb | 529 | 2,616 | 143 | 2 | 110 | 5,569 | 238 | 4 | 231 | 0 | 0 | 0 | 0 | 381 | 8,185 | 6 | 341 | Conn | yes | UD | yes | no |
| eng.rst.gum | eng | rst | 24,688 | yes | 163,210 | 9,234 | 165 | 20,722 | 21,743 | 1,221 | 24 | 2,790 | 22,061 | 1,201 | 24 | 2,740 | 11,656 | 207,014 | 213 | 26,252 | EDU | no | UD (gold) | yes | yes |
| eng.rst.rstdt | eng | rst | 19,778 | yes | 169,321 | 6,672 | 309 | 17,646 | 17,574 | 717 | 38 | 1,797 | 22,017 | 929 | 38 | 2,346 | 8,318 | 208,912 | 385 | 21,789 | EDU | yes | UD (gold) | yes | no |
| eng.sdrt.stac | eng | sdrt | 12,235 | no | 41,930 | 8,754 | 33 | 9,887 | 4,864 | 991 | 6 | 1,154 | 6,732 | 1,342 | 6 | 1,547 | 11,087 | 53,526 | 45 | 12,588 | EDU | no | UD | yes | no |
| eus.rst.ert | eus | rst | 3,825 | yes | 30,690 | 1,599 | 116 | 2,785 | 7,219 | 366 | 24 | 677 | 7,871 | 415 | 24 | 740 | 2,380 | 45,780 | 164 | 4,202 | EDU | no | UD | no | no |
| fas.rst.prstc | fas | rst | 5,191 | yes | 52,497 | 1,713 | 120 | 4,609 | 7,033 | 202 | 15 | 576 | 7,396 | 264 | 15 | 670 | 2,179 | 66,926 | 150 | 5,855 | EDU | no | UD | yes | no |
| fra.sdrt.annodis | fra | sdrt | 3,338 | yes | 22,515 | 1,020 | 64 | 2,255 | 5,013 | 245 | 11 | 556 | 5,171 | 242 | 11 | 618 | 1,507 | 32,699 | 86 | 3,429 | EDU | no | UD | no | no |
| ita.pdtb.luna | ita | pdtb | 1,544 | yes | 17,344 | 3,721 | 42 | 671 | 3,180 | 775 | 6 | 139 | 6,465 | 1,315 | 12 | 261 | 5,811 | 26,989 | 60 | 1,071 | Conn | yes | UD | yes | no |
| nld.rst.nldt | nld | rst | 2,264 | no | 17,562 | 1,156 | 56 | 1,662 | 3,783 | 255 | 12 | 343 | 3,553 | 240 | 12 | 338 | 1,651 | 24,898 | 80 | 2,343 | EDU | no | UD | no | no |
| por.pdtb.crpc | por | pdtb | 11,330 | yes | 147,594 | 4,078 | 243 | 3,994 | 20,102 | 581 | 28 | 621 | 19,153 | 535 | 31 | 544 | 5,194 | 186,849 | 302 | 5,159 | Conn | yes | UD | no | no |
| por.pdtb.tedm | por | pdtb | 554 | 2,785 | 148 | 2 | 102 | 5,405 | 246 | 4 | 203 | 0 | 0 | 0 | 0 | 394 | 8,190 | 6 | 305 | Conn | yes | UD | no | no |
| por.rst.cstn | por | rst | 4,993 | yes | 52,177 | 1,825 | 114 | 4,601 | 7,023 | 257 | 14 | 630 | 4,132 | 139 | 12 | 306 | 2,221 | 63,332 | 140 | 5,537 | EDU | no | UD | yes | no |
| rus.rst.rrt | rus | rst | 34,566 | yes | 390,375 | 18,932 | 272 | 34,682 | 40,779 | 2,025 | 30 | 3,352 | 41,851 | 2,087 | 30 | 3,508 | 23,044 | 473,005 | 332 | 41,542 | EDU | no | UD | no | no |
| spa.rst.rststb | spa | rst | 3,049 | yes | 43,055 | 1,548 | 203 | 2,472 | 7,551 | 254 | 32 | 419 | 8,111 | 287 | 32 | 460 | 2,089 | 58,717 | 267 | 3,351 | EDU | no | UD | no | no |
| spa.rst.sctb | spa | rst | 692 | yes | 10,253 | 326 | 32 | 473 | 2,448 | 76 | 9 | 103 | 3,814 | 114 | 9 | 168 | 516 | 16,515 | 50 | 744 | EDU | no | UD | no | no |
| tha.pdtb.tdtb | tha | pdtb | 10,865 | yes | 199,135 | 5,076 | 139 | 8,277 | 27,326 | 633 | 19 | 1,243 | 30,062 | 825 | 22 | 1,344 | 6,534 | 256,523 | 180 | 10,864 | Conn | yes | UD | no | no |
| tur.pdtb.tdb | tur | pdtb | 3,185 | yes | 398,515 | 24,960 | 159 | 7,063 | 49,952 | 2,948 | 19 | 831 | 47,891 | 3,289 | 19 | 854 | 31,197 | 496,358 | 197 | 8,748 | Conn | yes | UD | yes | no |
| tur.pdtb.tedm | tur | pdtb | 577 | 2,159 | 141 | 2 | 135 | 4,127 | 269 | 4 | 247 | 0 | 0 | 0 | 0 | 410 | 6,286 | 6 | 382 | Conn | yes | UD | yes | no |
| zho.dep.scidtb | zho | dep | 1,298 | no | 11,289 | 308 | 69 | 898 | 3,853 | 103 | 20 | 309 | 3,622 | 89 | 20 | 235 | 500 | 18,764 | 109 | 1,442 | EDU | no | UD | no | no |
| zho.pdtb.cdtb | zho | pdtb | 5,270 | yes | 52,061 | 2,049 | 125 | 1,034 | 11,178 | 438 | 21 | 314 | 10,075 | 404 | 18 | 312 | 2,891 | 73,314 | 164 | 1,660 | Conn | yes | other (gold) | no | no |
| zho.rst.gcdt | zho | rst | 8,413 | yes | 47,639 | 2,026 | 40 | 7,470 | 7,619 | 331 | 5 | 1,144 | 7,647 | 335 | 5 | 1,092 | 2,692 | 62,905 | 50 | 9,706 | EDU | no | UD (V1) | no | no |
| zho.rst.sctb | zho | rst | 692 | yes | 9,655 | 361 | 32 | 473 | 2,264 | 86 | 9 | 103 | 3,577 | 133 | 9 | 168 | 580 | 15,496 | 50 | 744 | EDU | no | UD | no | no |
$*Legend*

  * `corpus` - unique corpus identifier, consisting of the language code, framework acronym and an abbreviation for the corpus name
  * `lang` - ISO 639-3, 3 letter language code
  * `framework` - one of pdtb (Penn Discourse Treebank framework), rst (Rhetorical Structure Theory) or sdrt (Segmented Discourse Representation Theory)
  * `rels` - number of discourse relation instances (note that for tur.pdtb.tdb, only a subset of the data annotated for connectives also has discourse relation types, so there are much fewer relation instances and documents than connectives)
  * `rel_types` - number of distinct relation types targeted in the shared task 'label' column. Note that for some corpora, these were collapsed from a larger inventory, but the original uncollapsed relation labels are retained in the column orig_label
  * `discont` - whether the relation classification dataset contains discontinuous discourse units. Note that for segmentation, each part of a discontinous unit constitutes its own segment, so these datasets only differ overtly in the .rels file, where gaps are indicated by `<*>`.
  * `underscored` - whether all text is contained in the data (`no`), all text needs to be retrieved using the `process_underscores.py` script (`yes`), or part of the text needs to be retrieved by the same script (`part`)
  * `syntax` - type of syntax trees: automatic Universal Dependencies (UD) or other, and gold standard (manual or converted from manual annotation) or not (automatic). See individual corpus README files for more details.
  * `MWTs` - whether the corpus uses CoNLL-U Multiword Tokens with hyphens in IDs for complex word forms (e.g. `1-2 don't ... 1 do ... 2 n't`)
  * `ellip` - whether the corpus uses CoNLL-U ellipsis tokens (a.k.a. null or empty tokens) with decimal IDs (e.g. `8.1`) to reconstruct ellipsis phenomena. Note that such tokens only appear in `.conllu` files, since they are not actually part of the text; they are never the location of a discourse unit segmentation point and are omitted in .tok and .rels files, and they are not counted in the token offsets in .rels files.






<!---
## Old statistics

| corpus | lang | framework | rels | rel_types | discont | train_toks | train_sents | train_docs | train_segs | dev_toks | dev_sents | dev_docs | dev_segs | total_sents | total_toks | total_docs | total_segs | seg_style | underscored | syntax | MWTs | ellip |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| deu.rst.pcc | deu | rst | 2,164 | 26 | no | 26,831 | 1,773 | 142 | 2,471 | 3,152 | 207 | 17 | 275 | 1,980 | 29,983 | 159 | 2,746 | EDU | no | UD | no | no |
| eng.dep.scidtb | eng | dep | 6,060 | 24 | yes | 62,488 | 2,570 | 492 | 6,740 | 20,299 | 815 | 154 | 2,130 | 3,385 | 82,787 | 646 | 8,870 | EDU | no | UD | yes | no |
| eng.pdtb.pdtb | eng | pdtb | 43,920 | 23 | yes | 1,076,448 | 44,563 | 1,992 | 23,850 | 40,384 | 1,703 | 79 | 953 | 46,266 | 1,116,832 | 2,071 | 24,803 | Conn | yes | UD (gold) | yes | no |
| eng.rst.gum | eng | rst | 19,496 | 14 | yes | 163,210 | 9,234 | 165 | 20,722 | 21,743 | 1,221 | 24 | 2,790 | 10,455 | 184,953 | 189 | 23,512 | EDU | no | UD (gold) | yes | yes |
| eng.rst.rstdt | eng | rst | 16,002 | 17 | yes | 169,321 | 6,672 | 309 | 17,646 | 17,574 | 717 | 38 | 1,797 | 7,389 | 186,895 | 347 | 19,443 | EDU | yes | UD (gold) | yes | no |
| eng.sdrt.stac | eng | sdrt | 9,580 | 16 | no | 41,930 | 8,754 | 33 | 9,887 | 4,864 | 991 | 6 | 1,154 | 9,745 | 46,794 | 39 | 11,041 | EDU | no | UD | yes | no |
| eus.rst.ert | eus | rst | 2,533 | 29 | yes | 30,690 | 1,599 | 116 | 2,785 | 7,219 | 366 | 24 | 677 | 1,965 | 37,909 | 140 | 3,462 | EDU | no | UD | no | no |
| fas.rst.prstc | fas | rst | 4,100 | 17 | yes | 52,497 | 1,713 | 120 | 4,609 | 7,033 | 202 | 15 | 576 | 1,915 | 59,530 | 135 | 5,185 | EDU | no | UD | yes | no |
| fra.sdrt.annodis | fra | sdrt | 2,185 | 18 | yes | 22,515 | 1,020 | 64 | 2,255 | 5,013 | 245 | 11 | 556 | 1,265 | 27,528 | 75 | 2,811 | EDU | no | UD | no | no |
| ita.pdtb.luna | ita | pdtb | 961 | 15 | yes | 17,343 | 3,724 | 42 | 668 | 3,179 | 776 | 6 | 134 | 4,500 | 20,522 | 48 | 802 | Conn | yes | UD | yes | no |
| nld.rst.nldt | nld | rst | 1,608 | 32 | no | 17,562 | 1,156 | 56 | 1,662 | 3,783 | 255 | 12 | 343 | 1,411 | 21,345 | 68 | 2,005 | EDU | no | UD | no | no |
| por.rst.cstn | por | rst | 4,148 | 32 | yes | 52,177 | 1,825 | 114 | 4,601 | 7,023 | 257 | 14 | 630 | 2,082 | 59,200 | 128 | 5,231 | EDU | no | UD | yes | no |
| rus.rst.rrt | rus | rst | 28,868 | 22 | yes | 390,375 | 18,932 | 272 | 34,682 | 40,779 | 2,025 | 30 | 3,352 | 20,957 | 431,154 | 302 | 38,034 | EDU | no | UD | no | no |
| spa.rst.rststb | spa | rst | 2,240 | 28 | yes | 43,055 | 1,548 | 203 | 2,472 | 7,551 | 254 | 32 | 419 | 1,802 | 50,606 | 235 | 2,891 | EDU | no | UD | no | no |
| spa.rst.sctb | spa | rst | 439 | 24 | yes | 10,253 | 326 | 32 | 473 | 2,448 | 76 | 9 | 103 | 402 | 12,701 | 41 | 576 | EDU | no | UD | no | no |
| tur.pdtb.tdb | tur | pdtb | 2,451 | 23 | yes | 398,515 | 24,960 | 159 | 7,063 | 49,952 | 2,948 | 19 | 831 | 27,908 | 448,467 | 178 | 7,894 | Conn | yes | UD | yes | no |
| zho.dep.scidtb | zho | dep | 802 | 23 | no | 11,289 | 308 | 69 | 898 | 3,853 | 103 | 20 | 309 | 411 | 15,142 | 89 | 1,207 | EDU | no | UD | no | no |
| zho.pdtb.cdtb | zho | pdtb | 3,657 | 9 | yes | 52,061 | 2,049 | 125 | 1,034 | 11,178 | 438 | 21 | 314 | 2,487 | 63,239 | 146 | 1,348 | Conn | yes | other (gold) | no | no |
| zho.rst.gcdt | zho | rst | 6,454 | 31 | yes | 47,639 | 2,026 | 40 | 7,470 | 7,619 | 331 | 5 | 1,144 | 2,357 | 55,258 | 45 | 8,614 | EDU | no | UD (V1) | no | no |
| zho.rst.sctb | zho | rst | 439 | 26 | yes | 9,655 | 361 | 32 | 473 | 2,264 | 86 | 9 | 103 | 447 | 11,919 | 41 | 576 | EDU | no | UD | no | no |




| corpus | lang | framework | rels | rel_types | discont | train_toks | train_sents | train_docs | dev_toks | dev_sents | dev_docs | test_toks | test_sents | test_docs | total_sents | total_toks | total_docs | seg_style | underscored | syntax | MWTs | ellip |
| --- | --- | --- | --- |-----------| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| deu.rst.pcc | deu | rst | 2,164 | 26        | no | 26,831 | 1,773 | 142 | 3,152 | 207 | 17 | 3,239 | 213 | 17 | 2,193 | 33,222 | 176 | EDU | no | UD | no | no |
| eng.pdtb.pdtb | eng | pdtb | 43,920 | 23        | yes | 1,061,229 | 44,563 | 1,992 | 39,768 | 1,703 | 79 | 55,660 | 2,364 | 91 | 48,630 | 1,156,657 | 2,162 | Conn | yes | UD (gold) | no | no |
| eng.rst.gum | eng | rst | 13,897 | 15        | yes | 116,557 | 6,346 | 128 | 18,172 | 947 | 20 | 18,127 | 999 | 20 | 8,292 | 152,856 | 168 | EDU | no | UD (gold) | yes | yes |
| eng.rst.rstdt | eng | rst | 16,002 | 17        | yes | 166,854 | 6,672 | 309 | 17,309 | 717 | 38 | 21,666 | 929 | 38 | 8,318 | 205,829 | 385 | EDU | yes | UD (gold) | no | no |
| eng.sdrt.stac | eng | sdrt | 9,580 | 16        | no | 41,060 | 8,754 | 33 | 4,747 | 991 | 6 | 6,547 | 1,342 | 6 | 11,087 | 52,354 | 45 | EDU | no | UD | no | no |
| eus.rst.ert | eus | rst | 2,533 | 29        | yes | 30,690 | 1,599 | 116 | 7,219 | 366 | 24 | 7,871 | 415 | 24 | 2,380 | 45,780 | 164 | EDU | no | UD | no | no |
| fas.rst.prstc | fas | rst | 4,100 | 17        | yes | 52,497 | 1,713 | 120 | 7,033 | 202 | 15 | 7,396 | 264 | 15 | 2,179 | 66,926 | 150 | EDU | no | UD | yes | no |
| fra.sdrt.annodis | fra | sdrt | 2,185 | 18        | yes | 22,515 | 1,020 | 64 | 5,013 | 245 | 11 | 5,171 | 242 | 11 | 1,507 | 32,699 | 86 | EDU | no | UD | no | no |
| nld.rst.nldt | nld | rst | 1,608 | 32        | no | 17,562 | 1,156 | 56 | 3,783 | 255 | 12 | 3,553 | 240 | 12 | 1,651 | 24,898 | 80 | EDU | no | UD | no | no |
| por.rst.cstn | por | rst | 4,148 | 32        | yes | 52,177 | 1,825 | 114 | 7,023 | 257 | 14 | 4,132 | 139 | 12 | 2,221 | 63,332 | 140 | EDU | no | UD | yes | no |
| rus.rst.rrt | rus | rst | 28,868 | 22        | yes | 390,375 | 18,932 | 272 | 40,779 | 2,025 | 30 | 41,851 | 2,087 | 30 | 23,044 | 473,005 | 332 | EDU | no | UD | no | no |
| spa.rst.rststb | spa | rst | 2,240 | 28        | yes | 43,055 | 1,548 | 203 | 7,551 | 254 | 32 | 8,111 | 287 | 32 | 2,089 | 58,717 | 267 | EDU | no | UD | no | no |
| spa.rst.sctb | spa | rst | 439 | 24        | yes | 10,253 | 326 | 32 | 2,448 | 76 | 9 | 3,814 | 114 | 9 | 516 | 16,515 | 50 | EDU | no | UD | no | no |
| tur.pdtb.tdb | tur | pdtb | 2,451 | 23        | yes | 398,515 | 24,960 | 159 | 49,952 | 2,948 | 19 | 47,891 | 3,289 | 19 | 31,197 | 496,358 | 197 | Conn | yes | UD | yes | no |
| zho.pdtb.cdtb | zho | pdtb | 3,657 | 9         | yes | 52,061 | 2,049 | 125 | 11,178 | 438 | 21 | 10,075 | 404 | 18 | 2,891 | 73,314 | 164 | Conn | yes | other (gold) | no | no |
| zho.rst.sctb | zho | rst | 439 | 26        | yes | 9,655 | 361 | 32 | 2,264 | 86 | 9 | 3,577 | 133 | 9 | 580 | 15,496 | 50 | EDU | no | UD | no | no |

*Legend*

  * `corpus` - unique corpus identifier, consisting of the language code, framework acronym and an abbreviation for the corpus name
  * `lang` - ISO 639-3, 3 letter language code
  * `framework` - one of pdtb (Penn Discourse Treebank framework), rst (Rhetorical Structure Theory) or sdrt (Segmented Discourse Representation Theory)
  * `rels` - number of discourse relation instances (note that for tur.pdtb.tdb, only a subset of the data annotated for connectives also has discourse relation types, so there are much fewer relation instances and documents than connectives)
  * `rel_types` - number of distinct relation types targeted in the shared task 'label' column. Note that for some corpora, these were collapsed from a larger inventory, but the original uncollapsed relation labels are retained in the column orig_label
  * `discont` - whether the relation classification dataset contains discontinuous discourse units. Note that for segmentation, each part of a discontinous unit constitutes its own segment, so these datasets only differ overtly in the .rels file, where gaps are indicated by `<*>`.
  * `underscored` - whether all text is contained in the data (`no`), all text needs to be retrieved using the `process_underscores.py` script (`yes`), or part of the text needs to be retrieved by the same script (`part`)
  * `syntax` - type of syntax trees: automatic Universal Dependencies (UD) or other, and gold standard (manual or converted from manual annotation) or not (automatic). See individual corpus README files for more details.
  * `MWTs` - whether the corpus uses CoNLL-U Multiword Tokens with hyphens in IDs for complex word forms (e.g. `1-2 don't ... 1 do ... 2 n't`)
  * `ellip` - whether the corpus uses CoNLL-U ellipsis tokens (a.k.a. null or empty tokens) with decimal IDs (e.g. `8.1`) to reconstruct ellipsis phenomena. Note that such tokens only appear in `.conllu` files, since they are not actually part of the text; they are never the location of a discourse unit segmentation point and are omitted in .tok and .rels files, and they are not counted in the token offsets in .rels files.
--->

<!---
## Directories

## Surprise language

## Statistics
--->
