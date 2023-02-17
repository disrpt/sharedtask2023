# eng.sdrt.stac

## Description

The STAC dataset is a corpus of strategic chat conversations manually annotated with negotiation-related information, dialogue acts and discourse structures in the framework of Segmented Discourse Representation Theory (SDRT).  This dataset was developed within the context of the STAC (Strategic Conversation) project supported by the European Research Council, Grant n. 269427.

This dataset consists of 45 games segmented into Elementary Discourse Units and then annotated using the Glozz tool.  The annotations were split into subdocuments to make them easier to work with.  

The annotations have benefitted from several passes---a first one done by annotators hired for the STAC project and subsequent revisions done by SDRT experts.  Thanks to Julie Hall, Helen Joseph and especially Lisa Grabow Peterson for the initial round of annotations.  

### Download

You may download the entire corpus from the STAC website:
https://www.irit.fr/STAC/


### License and attribution information

The STAC corpus is made available under the Creative Commons license Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
https://creativecommons.org/licenses/by-nc-sa/4.0/

If you use the STAC corpus in a scientific publication, we would appreciate citations to the following paper:
* Asher, N., Hunter, J., Morey, M., Benamara, F. & S. Afantenos (2016). Discourse structure and dialogue acts in multiparty dialogue: the STAC corpus. In The Tenth International Conference on Language Resources and Evaluation (LREC 2016). European Language Resources Association, pp. 2721-2727, Portorož.

### Contact information

Nicholas Asher
E-mail: nicholas.asher@irit.fr

## DISRPT 2021 shared task information

The STAC dataset treats individual chat turns as utterances for the purposes of syntactic sentence segmentation in the .conllu files. Parses were done automatically using Stanza's EWT model. Note that in .tok files, it is not always possible to recognize chat turn transitions, though in the .conllu files, they are guaranteed to be split into distinct sentences. Sentences may contain multiple discourse units. The .rels files contain no split EDUs, i.e. unit1 and unit2 are always uninterrupted sequences of tokens.