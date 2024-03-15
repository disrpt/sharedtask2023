# eng.rst.rstdt

### The RST Discourse Treebank

Carlson, Lynn, Daniel Marcu and Mary Ellen Okurowski (2001). RST Discourse Treebank LDC2002T07. Philadelphia: Linguistic Data Consortium.
```
@Misc{RSTDT-LDC,
author       = {Lynn Carlson, Daniel Marcu, Mary Ellen Okurowski},
year         = {2002},
title        = {{RST Discourse Treebank LDC2002T07}},
organization = {Linguistic Data Consortium},
address      = {Philadelphia}
}

@InCollection{CarlsonEtAl2003,
title                    = {Building a {D}iscourse-{T}agged {C}orpus in the {F}ramework of {R}hetorical {S}tructure {T}heory},
author                   = {Lynn Carlson and Daniel Marcu and Mary Ellen Okurowski},
booktitle                = {Current and New Directions in Discourse and Dialogue},
publisher                = {Kluwer},
year                     = {2003},
address                  = {Dordrecht},
pages                    = {85--112},
series                   = {Text, Speech and Language Technology 22}
}
```


## Introduction

Rhetorical Structure Theory (RST) Discourse Treebank was developed by researchers at the Information Sciences Institute (University of Southern California), the US Department of Defense and the Linguistic Data Consortium (LDC). It consists of 385 Wall Street Journal articles from the Penn Treebank annotated with discourse structure in the RST framework along with human-generated extracts and abstracts associated with the source documents.

In the RST framework (Mann and Thompson, 1988), a text's discourse structure can be represented as a tree in four aspects: (1) the leaves correspond to text fragments called elementary discourse units (the mininal discourse units); (2) the internal nodes of the tree correspond to contiguous text spans; (3) each node is characterized by its nuclearity, or essential unit of information; and (4) each node is also characterized by a rhetorical relation between two or more non-overlapping, adjacent text spans.

See: https://catalog.ldc.upenn.edu/LDC2002T07


## DISRPT 2023 Shared Task Information

For the DISRPT 2023 shared task the data was divided into train, test and dev partitions. The original test partition of 38 documents was retained, and 38 further documents from the remaining 347 documents were set aside for the dev partition.

Syntactic dependency parses are made available using the CoreNLP conversion to UD syntax from the gold Penn Treebank (PTB) constituent trees where possible; however for some sentences whose text varies slightly from the version found in the PTB, automatic parses using UDPipe were introduced, to match the automatic parser used for DISRPT 2019. This dataset contains discontinuous discourse units (split 'same-unit').

### Obtaining the Text

Since the underlying Wall Street Journal text cannot be placed openly online, the shared task data has replaced token information with underscores. To reconstruct the data, users must obtain a copy of the LDC release of the RST-DT and run the Python script `utils/process_underscores.py -m add rstdt`. You will be prompted to supply the locations of the RST-DT distribution's `data/` folder. For more details, run `python utils/process_underscores.py -h`.
