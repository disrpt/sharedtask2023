# eng.dep.covidtb

### COVID19-DTB: COVID-19 Discourse Dependency Treebank


## Introduction 

The following information about the dataset is extracted from the original paper and repository. 
Original data is available at https://github.com/norikinishida/biomedical-discourse-treebanks

COVID19-DTB is a collection of manually annotated discourse dependency structures for scholarly paper abstracts on COVID-19 and related coronaviruses like SARS and MERS.

The following figure shows an actual example of discourse dependency structure for an abstract ([Israeli et al., 2020](https://doi.org/10.1101/2020.06.10.144196)) in COVID19-DTB.

<p align="center">
<img src="https://norikinishida.github.io/tools/discdep/images/045_figure020.png" width="400">
</p>

### Description

The authors sampled 300 abstracts randomly from the 2020 September snapshot of [The COVID-19 Open Research Dataset (CORD-19)](https://allenai.org/data/cord-19).
Then, the 300 abstracts were segmented into Elementary Discourse Units (EDUs) manually by the authors.
Then two professional annotators annotated gold discourse dependency structures to the 300 abstracts independently.
The results were divided into development and test sets, each of which consists of 150 examples.

### Notes on Segmentation
In the paper, the authors indicate that their annotation scheme follows the RST-DT annotation guideline (Carlson and Marcu, 2001) for EDU segmentation. 
In particular, the authors used the relation 'Same-Unit'. 

### Notes on Discourse Relations
Based on SciDTB and Penn Discourse Treebank (PDTB) (Prasad et al., 2008), the authors defined 14 discourse relation classes.
They indicate that they merged some classes, such as Cause-Effect + Explain → Cause-Result. Some classes are also renamed from SciDTB to fit the biomedical domain, such as Evaluation → Findings.


## DISRPT 2023 Shared Task Information

The dataset only contains a `dev` and `test` partition, without a `train` partition. 
This dataset thus corresponds to an Out of Domain setting: 
participants have to produce a system based on other data.

Tokenization, sentence splits, POS tagging, and syntactic parsing were obtained with Stanza. 


## References

[Out-of-Domain Discourse Dependency Parsing via Bootstrapping: {A}n Empirical Analysis on its Effectiveness and Limitation](https://aclanthology.org/2022.tacl-1.8/)
(Nishida & Matsumoto, TACL 2022)

```
@article{nishida-matsumoto-2022-domain,
    title = "Out-of-Domain Discourse Dependency Parsing via Bootstrapping: An Empirical Analysis on Its Effectiveness and Limitation",
    author = "Nishida, Noriki  and
      Matsumoto, Yuji",
    journal = "Transactions of the Association for Computational Linguistics",
    volume = "10",
    year = "2022",
    address = "Cambridge, MA",
    publisher = "MIT Press",
    url = "https://aclanthology.org/2022.tacl-1.8",
    doi = "10.1162/tacl_a_00451",
    pages = "127--144",
    abstract = "Discourse parsing has been studied for decades. However, it still remains challenging to utilize discourse parsing for real-world applications because the parsing accuracy degrades significantly on out-of-domain text. In this paper, we report and discuss the effectiveness and limitations of bootstrapping methods for adapting modern BERT-based discourse dependency parsers to out-of-domain text without relying on additional human supervision. Specifically, we investigate self-training, co-training, tri-training, and asymmetric tri-training of graph-based and transition-based discourse dependency parsing models, as well as confidence measures and sample selection criteria in two adaptation scenarios: monologue adaptation between scientific disciplines and dialogue genre adaptation. We also release COVID-19 Discourse Dependency Treebank (COVID19-DTB), a new manually annotated resource for discourse dependency parsing of biomedical paper abstracts. The experimental results show that bootstrapping is significantly and consistently effective for unsupervised domain adaptation of discourse dependency parsing, but the low coverage of accurately predicted pseudo labels is a bottleneck for further improvement. We show that active learning can mitigate this limitation.",
}
```

