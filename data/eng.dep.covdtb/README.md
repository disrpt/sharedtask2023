# eng.dep.covdtb

COVID19-DTB: COVID-19 Discourse Dependency Treebank

Data are available at: https://github.com/norikinishida/biomedical-discourse-treebanks

## Introduction 

COVID19-DTB is a collection of manually annotated discourse dependency structures for scholarly paper abstracts on COVID-19 and related coronaviruses like SARS and MERS.

The following figure shows an actual example of discourse dependency structure for an abstract ([Israeli et al., 2020](https://doi.org/10.1101/2020.06.10.144196)) in COVID19-DTB.

<p align="center">
<img src="https://norikinishida.github.io/tools/discdep/images/045_figure020.png" width="400">
</p>

### Description

First, we sampled 300 abstracts randomly from the 2020 September snapshot of [The COVID-19 Open Research Dataset (CORD-19)](https://allenai.org/data/cord-19).
Then, the 300 abstracts were segmented into Elementary Discourse Units (EDUs) manually by the authors.
Then, we employed two professional annotators to give gold discourse dependency structures to the 300 abstracts independently.
We divided the results into development and test sets, each of which consists of 150 examples.

The further details on the annotation scheme, annotation procedure, and corpus statistics can be found in our paper.


## DISRPT 2023 shared task information

The dataset only contains a dev and test split, without train section. This dataset thus corresponds to an Out of Domain setting: participants have to produce a system based on other data.

Tokenization, setence split, POS tagging and syntactic parsing were obtained with Stanza. 

## References

The blank entries (i.e., volume, pages, doi) in the bibtex item below will be filled in after publication in TACL.

```
@article{nishida2021outofdomain,
    title={Out-of-Domain Discourse Dependency Parsing via Bootstrapping: {A}n Empirical Analysis on its Effectiveness and Limitation},
    author={Nishida, Noriki and Matsumoto, Yuji},
    journal={Transactions of the Association for Computational Linguistics},
    volume={},
    pages={},
    year={2021},
    doi={},
}
```

