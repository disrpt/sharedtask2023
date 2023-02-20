# eus.rst.ert

### RST Basque TreeBank

### References: 

Iruskieta, M.; Aranzabe, M.J.; Diaz de Ilarraza, A.; Gonzalez, I.; Lersundi, M.; Lopez de la Calle, O. 2013. 
[The RST Basque TreeBank: An online search interface to check rhetorical relations](https://www.semanticscholar.org/paper/The-RST-Basque-TreeBank-%3A-an-online-search-to-check-Iruskieta-Aranzabe/e5dff6e196a6462906f00a6f264d6e4b5eb2c58e). 
Paper presented at the 4th Workshop ''RST and Discourse Studies'', Brasil, October 21-23.
```
 @InProceedings{IruskietaAranzabeIlarrazaEtAl2013,
  author    = {Mikel Iruskieta and Mar\'{i}a Jes\'{u}s Aranzabe and Arantza Diaz de Ilarraza and Itziar Gonzalez-Dios and Mikel Lersundi and Oier Lopez de Lacalle},
  title     = {The {RST} {B}asque {TreeBank}: An Online Search Interface to Check Rhetorical Relations},
  booktitle = {4th Workshop on RST and Discourse Studies},
  year      = {2013},
  pages     = {40-49},
  address   = {Fortaleza, Brasil},
  timestamp = {2019-03-14},
}
```

Aranzabe, M. J., Atutxa, A., Bengoetxea, K., de Ilarraza, A. D., Goenaga, I., Gojenola, K., & Uria, L. 2015. 
[Automatic conversion of the basque dependency treebank to universal dependencies](https://www.semanticscholar.org/paper/Automatic-Conversion-of-the-Basque-Dependency-to-Aranzabe-Atutxa/ffd4a990afcf6422ab5d56a46ac16c22d0e9737a). 
In Proceedings of the fourteenth international workshop on treebanks an linguistic theories (TLT14) (pp. 233-241).
```
@InProceedings{Aranzabe2015AutomaticCO,
  title={Automatic Conversion of the Basque Dependency Treebank to Universal Dependencies},
  author={Mar{\'i}a Jes{\'u}s Aranzabe and Aitziber Atutxa and Kepa Bengoetxea and Arantza D{\'i}az and Deliana Ilarraza and Iakes Goenaga and Koldo Gojenola},
  booktitle={the fourteenth international workshop on treebanks an linguistic theories (TLT14)},
  year={2015},
  pages={233-241},
  address={Warsaw, Poland},
}
```



## Introduction

The RST Basque Treebank was annotated at subsentential level following Tofilosky et al. (2009) and using the extended classification of discourse relations following the Rhetorical Structure Theory (RST) by Mann and Thompson (1988). The annotated corpus contains 164 texts from a variety of domains including medical, terminologycal and scientific. RSTTool (O'Donnel 2000), an annotation interface for RST was used to annotate this corpus and RhetDataBase was used to annotate the signals of the rhetorical relations.

Team-Group:

  * Oier Lopez de Lacalle
  * Esther Miranda
  * Kike Fernandez
  * Maxux Aranzabe
  * Itziar Gonzalez
  * Mikel Lersundi
  * Arantza Diaz de Ilarraza
  * Mikel Iruskieta

## DISRPT 2023 Shared Task Information

Sentence splits and parses balanced by genre. 
The `train`/`dev`/`test` partitions contain 116/24/24 documents respectively, parses were done automatically using Stanza. 
This dataset contains discontinuous discourse units (split 'same-unit'). 
