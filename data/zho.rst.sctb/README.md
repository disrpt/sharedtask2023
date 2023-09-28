# zho.rst.sctb

### The RST Spanish-Chinese Treebank - Chinese section

### References

Cao Shuyuan, da Cunha Iria, and Iruskieta Mikel. 2018. [The RST Spanish-Chinese Treebank](https://aclanthology.org/W18-4917/). In Proceedings of the Joint Workshop of Linguistic Annotation, Multiword Expression and Constructions (LAW-MWE-CxG-2018), 156-166.
```
@inproceedings{cao-etal-2018-rst,
title = "The {RST} {S}panish-{C}hinese Treebank",
author = "Cao, Shuyuan  and
da Cunha, Iria  and
Iruskieta, Mikel",
booktitle = "Proceedings of the Joint Workshop on Linguistic Annotation, Multiword Expressions and Constructions ({LAW}-{MWE}-{C}x{G}-2018)",
month = aug,
year = "2018",
address = "Santa Fe, New Mexico, USA",
publisher = "Association for Computational Linguistics",
url = "https://aclanthology.org/W18-4917",
pages = "156--166",
abstract = "Discourse analysis is necessary for different tasks of Natural Language Processing (NLP). As two of the most spoken languages in the world, discourse analysis between Spanish and Chinese is important for NLP research. This paper aims to present the first open Spanish-Chinese parallel corpus annotated with discourse information, whose theoretical framework is based on the Rhetorical Structure Theory (RST). We have evaluated and harmonized each annotation part to obtain a high annotated-quality corpus. The corpus is already available to the public.",
}
```


Cao Shuyuan, Xue Nianwen, da Cunha Iria, Iruskieta Mikel, and Wang Chuan. 2017. [Discourse Segmentation for Building a RST Chinese Treebank](https://aclanthology.org/W17-3610/). In Proceedings of 6th Workshop “Recent Advances in RST and Related Formalisms”, 73-81.
```
@inproceedings{cao-etal-2017-discourse,
title = "Discourse Segmentation for Building a {RST} {C}hinese Treebank",
author = "Cao, Shuyuan  and
Xue, Nianwen  and
da Cunha, Iria  and
Iruskieta, Mikel  and
Wang, Chuan",
booktitle = "Proceedings of the 6th Workshop on Recent Advances in {RST} and Related Formalisms",
month = sep,
year = "2017",
address = "Santiago de Compostela, Spain",
publisher = "Association for Computational Linguistics",
url = "https://aclanthology.org/W17-3610",
doi = "10.18653/v1/W17-3610",
pages = "73--81",
ISBN = "978-1-945626-78-4",
}
```


Cao Shuyuan, da Cunha Iria, Iruskieta Mikel. 2017. [Toward the Elaboration of a Spanish-Chinese Parallel Annotated Corpus](https://easychair.org/publications/paper/l). EPiC Series of Language and Linguistics, 2: 315-324.
```
@inproceedings{AESLA2016:Toward_Elaboration_of_Spanish_Chinese,
author    = {Shuyuan Cao and Iria Da-Cunha and Mikel Iruskieta},
title     = {Toward the Elaboration of a Spanish-Chinese Parallel Annotated Corpus},
booktitle = {Professional and Academic Discourse: an Interdisciplinary Perspective},
editor    = {Chelo Vargas-Sierra},
series    = {EPiC Series in Language and Linguistics},
volume    = {2},
pages     = {315--324},
year      = {2017},
publisher = {EasyChair},
bibsource = {EasyChair, https://easychair.org},
issn      = {2398-5283},
url       = {https://easychair.org/publications/paper/l},
doi       = {10.29007/gxv3}}
```


Cao Shuyuan, da Cunha Iria, and Iruskieta Mikel. 2016. [A Corpus-based Approach for Spanish-Chinese Language Learning](https://aclanthology.org/W16-4913/). In Proceedings of the 3rd Workshop on Natural Language Processing Techniques for Educational Applications (NLP-TEA3), 97-106.
```
@inproceedings{cao-etal-2016-corpus,
title = "A Corpus-based Approach for {S}panish-{C}hinese Language Learning",
author = "Cao, Shuyuan  and
da Cunha, Iria  and
Iruskieta, Mikel",
booktitle = "Proceedings of the 3rd Workshop on Natural Language Processing Techniques for Educational Applications ({NLPTEA}2016)",
month = dec,
year = "2016",
address = "Osaka, Japan",
publisher = "The COLING 2016 Organizing Committee",
url = "https://aclanthology.org/W16-4913",
pages = "97--106",
abstract = "Due to the huge population that speaks Spanish and Chinese, these languages occupy an important position in the language learning studies. Although there are some automatic translation systems that benefit the learning of both languages, there is enough space to create resources in order to help language learners. As a quick and effective resource that can give large amount language information, corpus-based learning is becoming more and more popular. In this paper we enrich a Spanish-Chinese parallel corpus automatically with part of-speech (POS) information and manually with discourse segmentation (following the Rhetorical Structure Theory (RST) (Mann and Thompson, 1988)). Two search tools allow the Spanish-Chinese language learners to carry out different queries based on tokens and lemmas. The parallel corpus and the research tools are available to the academic community. We propose some examples to illustrate how learners can use the corpus to learn Spanish and Chinese.",
}
```



## Introduction

The RST Spanish-Chinese Treebank is a corpus of specialized texts in Spanish and their parallel texts in Chinese. All the texts are annotated manually with discourse relations under the theoretical framework Rhetorical Structure Theory (RST) (Mann and Thompson, 1988). RSTTool (O’Donnell, 2000) is used to annotate this corpus. The annotation results are saved by rstWeb (Zeldes, 2016).

In total, 100 texts are included in this corpus. The genres of these texts are: (a) scientific abstract; (b) advertisement; (c) news and (d) announcement. The topics of the corpus are: (a) terminology; (b) culture; (c) language; (d) economy; (e) education; (f) art and (g) international affairs.

## DISRPT 2023 Shared Task Information

Automatic parses were added using Stanza's Simplified Chinese model trained on UD_Chinese-GSD (`gsdsimp`). Some tokenization and parsing errors are expected. This dataset contains discontinuous discourse units (split 'same-unit').
