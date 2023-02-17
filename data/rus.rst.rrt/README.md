# rus.rst.rrt

Russian RST Treebank

## Introduction

Russian RST Treebank is a Russian corpus with annotations for Discourse Structure, annotated manually with discourse relations. This treebank was annotated manually with discourse structure in the Rhetorical Structure Theory  framework (RST, Mann & Thompson 1988) using rstWeb [https://corpling.uis.georgetown.edu/rstweb/info/]. 

Russian RST Treebank 1.0 consisted of 79 news articles and 99 research articles (in the fields of computer science and on linguistics). The latest data includes an additional 104 blog documents, and 50 more news documents for a total of 332 documents.

This study was funded by RFBR according to the research project ¹ 17-29-07033.

## Feedback

For further questions or inquiries about this dataset, you can contact:

Dina Pisarevskaya dinabpr@gmail.com
Maria Kobozeva marya.kobozeva@gmail.com
Svetlana Toldova toldova@yandex.ru

## Citation Info

If you use this dataset, please cite the publication of the data:

Pisarevskaya D. et al. (2017), Towards building a discourse-annotated corpus of Russian. In Computational Linguistics and Intellectual Technologies: Proc. of the Int. Conf." Dialogue, Vol. 1, pp. 194-204.

Toldova, S., Pisarevskaya, D., Ananyeva, M., Kobozeva, M., Nasedkin, A., Nikiforova, S., ... & Shelepov, A. (2017). Rhetorical relations markers in Russian RST Treebank. In Proceedings of the 6th Workshop on Recent Advances in RST and Related Formalisms, pp. 29-33.

## License

Russian RST Treebank 1.0 is publicly available under the Creative Commons - Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license.

References:
[Mann & Thompson 1988] Mann, William C. and Sandra A. Thompson (1988). "Rhetorical Structure Theory: Toward a functional theory of text organization". In: Text 8 (3), pp.243-281.

## DISRPT 2021 shared task information

This dataset has been expanded with the latest files bringing the total up from 178 documents in DISRPT 2019 to 322 in DISRPT 2021. Since the Russian RST Treebank does not contain gold tokenization and sentence splitting, data was automatically tokenized and parsed using Stanza's Syntagrus model. As a result sentence splits in conll files are not always correct. Additionally, some of the scientific texts contain portions in other languages, such as bibliographical references in English, brief summaries or keywords not in Russian.

Note also that some regions of text in the Russian RST Treebank are not internally segmented despite containing multiple sentences, such as bibliographies. This dataset contains discontinuous discourse units (split 'same-unit').
