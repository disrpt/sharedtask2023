# ita.pdtb.luna

## Introduction

LUNA Corpus Discourse Data Set consists of 60 dialogs from Italian LUNA Human-Human Corpus in the hardware/software help desk domain annotated following Penn Discourse Treebank (PDTB) guideline. The data set contains a total of 1,606 discourse relations; Explicit, Implicit, AltLex and EntRel relations have been annotated. The discourse connectives are annotated, as well as possibly supplementary materials to the arguments.

### Relation set

As in PDTB, LUNA corpus is annotated with a 3-level hierarchy of senses, including some modifications compared to the PDTB label set:
- 3 more Level 1 classes which have only 1 level:
    - `Discourse Marker`
    - `Interrupted`
    - `Repetition`
- 3rd level further categorizes L2 relations into the following types:
    - Epistemic
    - Inferential
    - Pragmatic
    - Propositional
    - Semantic
    - Speech act
- Furthermore `Temporal` sense has no 3rd level, i.e. only
    - `Temporal.Asynchronous`
    - `Temporal.Synchrony`
- `Expansion.Restatement` on level 3 is further categorized into:
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



## DISRPT 2023 shared task information

The dialogs are split into training ( section 02) and development ( section 01).
A test set will be made available during the evaluation step of the shared task.

Tokenization, sentence segmentation, POS tagging and syntactic dependency parses are made available using Stanza.

## Note on discourse relation and segmentation for spoken dialogs  
Discourse relations may appear cross-speaker: different arguments of the same relation being in different speaker turns for elaboration relation, for instance.
Additionally, due to the phenomena such as one speaker completing the other's utterance, even arguments may appear cross-speaker.
Overall, in spoken dialogs the turn and speaker segmentation is not parallel to the discourse relation segmentation.

### Note on segmentation

As for other PDTB like corpora, with respect to LUNA, the DISRPT task only requires identifying segments corresponding to the explicit connectives in the text.

  * Labelling a token with "Seg=B-Conn" indicates that it is at the beginning of an explicit connective.
  * Labelling a token with "Seg=I-Conn" indicates that it is a continuation of the start of the connective
   to its left;
  * Labelling a token with "_" indicates that is is outside the segment to its left.

### Notes on relation classification

The predicted label (the last column) for each instance has been truncated at Level-2. For instance, the predicted label for the sense label “Expansion.Restatement.Equivalence” would be “Expansion.Restatement”. However, we keep the original label in the third-to-last column called “orig_label”, which matches the directionality information provided in the “dir” column.


## References

If you use this dataset for publication, please cite the following papers:

- Sara Tonelli, Giuseppe Riccardi, Rashmi Prasad, and Aravind K. Joshi,
  "Annotation of discourse relations for conversational spoken dialogs.",
  In Proceedings of the International Conference on Language Resources and Evaluation (LREC), 2010.

- Giuseppe Riccardi, Evgeny A. Stepanov, and Shammur Absar Chowdhury.
  "Discourse connective detection in spoken conversations.",
  IEEE International Conference on Acoustics Speech and Signal Processing (ICASSP), 2016.
