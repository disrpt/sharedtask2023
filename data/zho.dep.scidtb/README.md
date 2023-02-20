# zho.dep.scidtb

### SciDTB: Discourse Dependency TreeBank for Scientific Abstracts

[//]: # (or UnifiedDep: Unified Chinese Dependency Discourse Datasets )

[//]: # ()
[//]: # (The unified Chinese discourse dependency dataset is now composed of **SciCDTB** developed by Peking University and **SU-CDTB_{dep}** converted from CDTB developed by Soochow University.)


The underlying data is available at https://github.com/PKU-TANGENT/UnifiedDep but only corresponds to the SciDTB/ directory in the available data.


## DISRPT 2023 Shared Task Information
### Notes on Relation Classification 
The underlying data used in the DISRPT 2023 Shared Task comes from the GitHub repository of the
paper titled [Unifying Discourse Resources with Dependency Framework](https://aclanthology.org/2021.ccl-1.94/). 
Therefore, the data is in the unified format proposed in this paper. 

Since there is no publicly available information on the data partitions, we've made our own splits
based on the number of files in each partition as shown in Table 3 of the paper:
- `train`: 69 files
- `dev`: 20 files
- `test`: 20 files



## References

Please cite the following source papers: 
- [Zero-shot Chinese Discourse Dependency Parsing via Cross-lingual Mapping](https://aclanthology.org/W19-8104/)
    ```
    @inproceedings{cheng-li-2019-zero,
        title = "Zero-shot {C}hinese Discourse Dependency Parsing via Cross-lingual Mapping",
        author = "Cheng, Yi  and
          Li, Sujian",
        booktitle = "Proceedings of the 1st Workshop on Discourse Structure in Neural NLG",
        month = nov,
        year = "2019",
        address = "Tokyo, Japan",
        publisher = "Association for Computational Linguistics",
        url = "https://aclanthology.org/W19-8104",
        doi = "10.18653/v1/W19-8104",
        pages = "24--29",
        abstract = "Due to the absence of labeled data, discourse parsing still remains challenging in some languages. In this paper, we present a simple and efficient method to conduct zero-shot Chinese text-level dependency parsing by leveraging English discourse labeled data and parsing techniques. We first construct the Chinese-English mapping from the level of sentence and elementary discourse unit (EDU), and then exploit the parsing results of the corresponding English translations to obtain the discourse trees for the Chinese text. This method can automatically conduct Chinese discourse parsing, with no need of a large scale of Chinese labeled data.",
    }
    ```
- [Unifying Discourse Resources with Dependency Framework](https://aclanthology.org/2021.ccl-1.94/)

    ```
    @inproceedings{yi-etal-2021-unifying,
        title = "Unifying Discourse Resources with Dependency Framework",
        author = "Yi, Cheng  and
          Sujian, Li  and
          Yueyuan, Li",
        booktitle = "Proceedings of the 20th Chinese National Conference on Computational Linguistics",
        month = aug,
        year = "2021",
        address = "Huhhot, China",
        publisher = "Chinese Information Processing Society of China",
        url = "https://aclanthology.org/2021.ccl-1.94",
        pages = "1058--1065",
        abstract = "For text-level discourse analysis there are various discourse schemes but relatively few labeleddata because discourse research is still immature and it is labor-intensive to annotate the innerlogic of a text. In this paper we attempt to unify multiple Chinese discourse corpora under different annotation schemes with discourse dependency framework by designing semi-automatic methods to convert them into dependency structures. We also implement several benchmark dependency parsers and research on how they can leverage the unified data to improve performance.1",
        language = "English",
    }
    ```
