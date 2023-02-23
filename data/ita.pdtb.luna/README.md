# ita.pdtb.luna

## Introduction

The LUNA Corpus Discourse Data Set consists of 60 dialogs from Italian LUNA Human-Human Corpus in the hardware/software help desk domain annotated following the Penn Discourse Treebank (PDTB) guidelines. 

The data set contains a total of 1,606 discourse relation instances; Explicit, Implicit, AltLex and EntRel relations have been annotated. The discourse connectives are annotated, as well as possibly supplementary materials to the arguments.

### Relation Set

As in PDTB, the LUNA corpus is annotated with a 3-level hierarchy of senses, including some modifications compared to the PDTB label set:
- 3 more Level 1 classes which have only 1 level:
    - `Discourse Marker`
    - `Interrupted`
    - `Repetition`
- Level 3  further categorizes L2 relations into the following types:
    - Epistemic
    - Inferential
    - Pragmatic
    - Propositional
    - Semantic
    - Speech act
- Furthermore, the `Temporal` sense has no 3rd level, i.e. only
    - `Temporal.Asynchronous`
    - `Temporal.Synchrony`
- `Expansion.Restatement` on Level 3 is further categorized into:
    - `Expansion.Restatement.Equivalence`
    - `Expansion.Restatement.Specification`


### Anonymization

The data has been anonymized at token-level using the following conversions:

| Replacement   | Freq | Description                                     |
|:--------------|-----:|:------------------------------------------------|
| `<NUM>`       |  337 | number-words; e.g. `duomilasei`                 |
| `<ORD>`       |   29 | ordinals; e.g. `quarto`                         |
| `<DIGIT>`     |  740 | digit-words; e.g. `due`                         |
| `<CHAR>`      |   86 | letter; e.g. `C`                                |
| `<PUNC>`      |   18 | punctuation; e.g. `barra`                       |
| `<WORD>`      |   11 | a word to be masked; e.g. password, spelling    |
| `<CHARS>`     |    5 | a sequence of letters (abbreviation); e.g. `SG` |
| `<BRAND>`     |   36 | brands (hardware); e.g. `Fujitsu`               |
| `<SW>`        |  159 | software; e.g. `Windows`                        |
| `<PER>`       |  278 | person names; e.g. `Monica`                     |
| `<ORG>`       |   54 | named organizations; e.g. `CSI`                 |
| `<LOC>`       |  126 | locations; e.g. `Italia`                        |
| `<LOC.SPELL>` |   25 | locations for spelling; e.g. `Ancona`           |
| `<WD>`        |   13 | week days; e.g. `domenica`                      |
| `<MM>`        |   13 | month names; e.g. `gennaio`                     |
| `<MISC>`      |    2 | other; not covered above                        |


### Notes on Discourse Relation and Segmentation for Spoken Dialogs  

Discourse relations may appear cross-speaker: different arguments of the same relation are in different speaker turns for elaboration relation, for instance.

Additionally, due to the phenomena such as one speaker completing the other's utterance, even arguments may appear cross-speaker.
Overall, in spoken dialogs the turn and speaker segmentation is not parallel to the discourse relation segmentation.


### Notes on Segmentation

Like other PDTB-style corpora in DISRPT, with respect to LUNA, the DISRPT task only requires identifying segments corresponding to the explicit connectives in the text.

  * Labelling a token with "Seg=B-Conn" indicates that it is at the beginning of an explicit connective.
  * Labelling a token with "Seg=I-Conn" indicates that it is a continuation of the start of the connective
   to its left;
  * Labelling a token with "_" indicates that is is outside the segment to its left.


### Notes on Relation Classification

The predicted label (the last column) for each instance has been truncated at Level-2. 
For instance, the predicted label for the sense label “Expansion.Restatement.Equivalence” would be “Expansion.Restatement”. 
However, we keep the original label in the third-to-last column called “orig_label”, which matches the directionality information provided in the “dir” column.

Due to anonymity reasons, the original corpus has certain information masked by tags such as <PER> and <NUM>. 


## DISRPT 2023 Shared Task Information

For the 2023 shared task, the dialogs were split into training ( section 02) and development ( section 01).
A test set will be made available during the evaluation step of the shared task.

Tokenization, sentence segmentation, POS tagging and syntactic dependency parses are made available using Stanza.



## References

If you use this dataset for publication, please cite the following papers:

- Sara Tonelli, Giuseppe Riccardi, Rashmi Prasad, and Aravind K. Joshi,
  [Annotation of discourse relations for conversational spoken dialogs](http://www.lrec-conf.org/proceedings/lrec2010/pdf/184_Paper.pdf).
  In Proceedings of the International Conference on Language Resources and Evaluation (LREC), 2010.
  ```
  @inproceedings{tonelli-etal-2010-annotation,
    title = "Annotation of Discourse Relations for Conversational Spoken Dialogs",
    author = "Tonelli, Sara  and
      Riccardi, Giuseppe  and
      Prasad, Rashmi  and
      Joshi, Aravind",
    booktitle = "Proceedings of the Seventh International Conference on Language Resources and Evaluation ({LREC}'10)",
    month = may,
    year = "2010",
    address = "Valletta, Malta",
    publisher = "European Language Resources Association (ELRA)",
    url = "http://www.lrec-conf.org/proceedings/lrec2010/pdf/184_Paper.pdf",
    abstract = "In this paper, we make a qualitative and quantitative analysis of discourse relations within the LUNA conversational spoken dialog corpus. In particular, we first describe the Penn Discourse Treebank (PDTB) and then we detail the adaptation of its annotation scheme to the LUNA corpus of Italian task-oriented dialogs in the domain of software/hardware assistance. We discuss similarities and differences between our approach and the PDTB paradigm and point out the peculiarities of spontaneous dialogs w.r.t. written text, which motivated some changes in the annotation strategy. In particular, we introduced the annotation of relations between non-contiguous arguments and we modified the sense hierarchy in order to take into account the important role of pragmatics in dialogs. In the final part of the paper, we present a comparison between the sense and connective frequency in a representative subset of the LUNA corpus and in the PDTB. Such analysis confirmed the differences between the two corpora and corroborates our choice to introduce dialog-specific adaptations.",
  }
  ```
  

- Giuseppe Riccardi, Evgeny A. Stepanov, and Shammur Absar Chowdhury.
 [ Discourse connective detection in spoken conversations](https://ieeexplore.ieee.org/document/7472848).
  IEEE International Conference on Acoustics Speech and Signal Processing (ICASSP), 2016.
  ```
  @INPROCEEDINGS{RiccardiStepanovChowdhury2016,
  author={Riccardi, Giuseppe and Stepanov, Evgeny A. and Chowdhury, Shammur Absar},
  booktitle={2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  title={Discourse connective detection in spoken conversations},
  year={2016}, 
  pages={6095-6099},
  doi={10.1109/ICASSP.2016.7472848}}
  ```
