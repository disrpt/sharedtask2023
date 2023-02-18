# zho.rst.gcdt

GCDT: Georgetown Chinese Discourse Treebank 

More information at: https://github.com/logan-siyao-peng/GCDT

## Introduction

GCDT is the largest (as of October 2022) hierarchical discourse treebank for Mandarin Chinese in the framework of Rhetorical Structure Theory (RST). 

GCDT covers over 60K tokens across five genres of freely available text, using the same relation inventory as the contemporary RST treebank for English -- GUM (https://github.com/amir-zeldes/gum). 


### Corpus statistics 
The corpus contains 50 documents, 10 from each of the five genres below.

In total, there are 62,905 tokens and  9,717 EDUs. 

We provide an 8:1:1 train:dev:test split for each genre as shown in the table below.

The five test documents are double annotated and the second annotation version appears in the double/ partition.

| Genre   |  #docs |  Avg #tokens/doc | Avg #EDUs/doc | Source | Dev doc | Test doc |
|:----------:|:-------------:|------:|------:|:-------------:|:-------------:|:-------------:|
| academic | 10 | 1416.8 | 203.3 | https://www.hanspub.org/ | gcdt_academic_peoples | gcdt_academic_dingzhen |
| bio | 10 | 1348.5 | 202.1 | https://zh.wikipedia.org/ | gcdt_bio_byron | gcdt_bio_dvorak |
| interview | 10 | 1146.4 | 181.2 | https://zh.wikinews.org/ | gcdt_interview_ward | gcdt_interview_wimax |
| news | 10 | 1124.9 | 165.2 | https://zh.wikinews.org/ | gcdt_news_famine | gcdt_news_simplified |
| wikihow | 10 | 1253.9 | 219.9 | https://zh.wikihow.com/ | gcdt_whow_hiking | gcdt_whow_thanksgiving |


## DISRPT 2021 shared task information

Tokenization, sentence segmentation, POS tagging and syntactic dependency parses are made available using Stanza.

## Citing

Please cite the following for the source paper -- [GCDT: A Chinese RST Treebank for Multigenre and Multilingual Discourse Parsing](https://aclanthology.org/2022.aacl-short.47/):

```
@inproceedings{peng_gcdt_2022,
	address = {Online only},
	title = {{GCDT}: {A} {Chinese} {RST} {Treebank} for {Multigenre} and {Multilingual} {Discourse} {Parsing}},
	shorttitle = {{GCDT}},
	url = {https://aclanthology.org/2022.aacl-short.47},
	abstract = {A lack of large-scale human-annotated data has hampered the hierarchical discourse parsing of Chinese. In this paper, we present GCDT, the largest hierarchical discourse treebank for Mandarin Chinese in the framework of Rhetorical Structure Theory (RST). GCDT covers over 60K tokens across five genres of freely available text, using the same relation inventory as contemporary RST treebanks for English. We also report on this dataset's parsing experiments, including state-of-the-art (SOTA) scores for Chinese RST parsing and RST parsing on the English GUM dataset, using cross-lingual training in Chinese and English with multilingual embeddings.},
	urldate = {2022-11-22},
	booktitle = {Proceedings of the 2nd {Conference} of the {Asia}-{Pacific} {Chapter} of the {Association} for {Computational} {Linguistics} and the 12th {International} {Joint} {Conference} on {Natural} {Language} {Processing}},
	publisher = {Association for Computational Linguistics},
	author = {Peng, Siyao and Liu, Yang Janet and Zeldes, Amir},
	month = nov,
	year = {2022},
	pages = {382--391},
	file = {Full Text PDF:/Users/loganpeng/Zotero/storage/IEPKWVJH/Peng et al. - 2022 - GCDT A Chinese RST Treebank for Multigenre and Mu.pdf:application/pdf},
}
```

Please cite the following for the [Chinese Discourse Annotation Reference Manual](https://hal.archives-ouvertes.fr/hal-03821884):


```

@techreport{peng_chinese_2022,
	type = {Research {Report}},
	title = {Chinese {Discourse} {Annotation} {Reference} {Manual}},
	url = {https://hal.archives-ouvertes.fr/hal-03821884},
	abstract = {This document provides extensive guidelines and examples for Rhetorical Structure Theory (RST) annotation in Mandarin Chinese. The guideline is divided into three sections. We first introduce preprocessing steps to prepare data for RST annotation. Secondly, we discuss syntactic criteria to segment texts into Elementary Discourse Units (EDUs). Lastly, we provide examples to define and distinguish discourse relations in different genres. We hope that this reference manual can facilitate RST annotations in Chinese and accelerate the development of the RST framework across languages.},
	urldate = {2022-11-30},
	institution = {Georgetown University (Washington, D.C.)},
	author = {Peng, Siyao and Liu, Yang Janet and Zeldes, Amir},
	month = oct,
	year = {2022},
	keywords = {Chinese, Discourse Analysis Representation, Rhetorical Structure Theory RST},
	file = {HAL PDF Full Text:/Users/loganpeng/Zotero/storage/Q7ZFHQ3Q/Peng et al. - 2022 - Chinese Discourse Annotation Reference Manual.pdf:application/pdf},
}
```
