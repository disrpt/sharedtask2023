# fra.sdrt.annodis

## Description

The ANNODIS resource is a diversified corpus of written French texts enriched with a manual annotation of discourse structures. It was produced as part of the ANNODIS project (ANNOtation DIScursive), financed by the French National Research Agency (ANR). Its main features:

  * two mark-ups (corresponding to two distinct approaches to discourse organisation)
  * rhetorical relations annotation including 3188 Elementary Discourse Units (EDU) and 1395 Complex Discourse Units (CDU) linked by 3355 rhetorical relations (e.g. contrast, elaboration, result, attribution, etc.)
  * multi-level structures annotion including 991 Enumerative Structures (ES) and 588 Topical Chains (TC) with their clues (e.g. 2456 topical expressions)
  * texts (a total of 687,000 words) coming from four sources
    * the regional daily Est Républicain (39 articles - 10,000 words)
    * the French Wikipedia (30 articles + 30 extracts - 242,000 words)
    * the proceedings of the Congrès Mondial de Linguistique Française 2008 (25 articles - 169,000 words)
    * reports from the Institut Français de Relations Internationales (32 reports - 266,000 words)

The texts were annotated using the Glozz annotation tool created for the ANNODIS resource

Partners in the ANNODIS project (ANR corpus 2007)

  * CLLE (UMR 5263), Université de Toulouse UTM (Myriam Bras, Cécile Fabre, Lydia-Mai Ho-Dac, Anne Le Draoulec, Marie-Paule Péry-Woodley, Laurent Prévot, Josette Rebeyrolle, Franck Sajous, Ludovic Tanguy, Marianne Vergez-Couret)
  * IRIT (UMR 5505) Université de Toulouse UPS (Nicholas Asher, Farah Benamara, Philippe Muller, Laure Vieu, Stergos Afantenos)
  * GREYC (UMR 6072) Université de Caen (Thierry Charnois, Bruno Crémilleux, Patrice Enjalbert, Stéphane Ferrari , Alexandre Labadié, Julien Lebranchu, Dominique Legallois, Yann Mathet, Antoine Widlöcher)

Publications presenting the ANNODIS project/resource

  * Afantenos S. D., Asher N., Benamara F., Bras M., Fabre C., Ho-Dac L.-M., Le Draoulec A. Muller P., Péry-Woodley M.-P., Prévot L., Rebeyrolle J., Tanguy L., Vergez-Couret M., Vieu L. (2012). An empirical resource for discovering cognitive principles of discourse organization: the ANNODIS corpus. LREC 2012, Istanbul, Turkey, July 2012. 
  * Péry-Woodley M.-P., Afantenos S. D., Ho-Dac L.-M., Asher N. (2011). La ressource ANNODIS, un corpus enrichi d'annotations discursives. TAL 52(3), pp 71-101. 
  * Péry-Woodley M.-P., Asher N., Enjalbert P., Benamara F., Bras M., Fabre C., Ferrari S., Ho-Dac L.-M., Le Draoulec A. , Mathet Y., Muller P., Prévot L., Rebeyrolle J., Tanguy L., Vergez-Couret M., Vieu L., Wildöcher A. (2009). ANNODIS : une approche outillée de l'annotation de structures discursives, TALN 2009, Senlis, Juin, 2009. 

Annotation manuals (in French)

  * Muller P., Vergez-Couret M., Prévot L., Asher N., Benamara F., Bras M., Le Draoulec A., Vieu L. (2012). Manuel d'annotation en relations de discours du projet ANNODIS. Carnets de Grammaire 21, 34p. 
  * Colléter M., Fabre C., Ho-Dac L.-M., Péry-Woodley M.-P., Rebeyrolle J., Tanguy L. (2012). La ressource ANNODIS multi-échelle : guide d'annotation et "bonus" Carnets de Grammaire 20, 63p. 

### Licence

The ANNODIS resource is available under Creative Commons licence BY-NC-SA 3.0 (Attribution-NonCommercial-ShareAlike). Please read it carefully.

### Person in charge

Lydia-Mai Ho-Dac
Contact : hodac@univ-tlse2.fr

### Source

Yann MATHET & Antoine WIDLOCHER
ANR Project: ANNODIS

## DISRPT 2021 shared task information

For the DISRPT 2021 shared task on elementary discourse unit segmentation, only segmentations from the 'expert' annotation portion of the corpus were used, leaving outside the 'naive' annotation portions. Syntactic parses are automatic, generated using Spacy. For relation classification, note that this dataset contains discontinuous discourse units (analyzed as equivalent to split 'same-unit' in RST). 