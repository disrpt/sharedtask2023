import io
import os
import argparse
from sklearn.metrics import accuracy_score

"""
Script to evaluate relation classification accuracy score from the .rels file:

  * One relation classification instance per line, with 12 columns
  
The evaluation uses the simple accuracy score per corpus. 


Arguments:
 * goldfile: shared task gold test data in the .rels format 
 * predfile: same format, with predicted labels positions in column 12 (the last column) 
    - note **number of relation classification instances must match**  
 * string_input: if specified, files are replaced by strings with file contents instead of file names

"""


__author__ = "Janet Liu"
__license__ = "Apache 2.0"
__version__ = "1.0.0"


def parse_data(infile, string_input=False) -> list:
	"""
	This function is to read a gold or a pred file to obtain the label column for accuracy calculation.

	:param infile: shared task .rels file
	:param string_input: If True, files are replaced by strings with file contents (for import inside other scripts)
	:return: a list of labels
	"""

	if not string_input:
		data = io.open(infile, encoding="utf-8").read().strip().replace("\r", "")
	else:
		data = infile.strip()

	labels = [line.split("\t")[-1] for i, line in enumerate(data.split("\n")) if "\t" in line and i>0] # first line : metadata


	return labels


def get_accuracy_score(gold_file, pred_file, string_input=False) -> dict:
	"""
	This function is to obtain the gold and predicted labels from their respective .rels file
	and compute the accuracy score.

	:param gold_file: Gold shared task file
	:param pred_file: File with predictions
	:param string_input: If True, files are replaced by strings with file contents (for import inside other scripts)
	:return: dictionary of scores for printing
	"""

	gold_labels = parse_data(gold_file, string_input)
	pred_labels = parse_data(pred_file, string_input)

	filename = gold_file.split(os.sep)[-1]

	assert len(gold_labels) == len(pred_labels), "FATAL: different number of labels detected in gold and pred"

	acc = accuracy_score(gold_labels, pred_labels)

	score_dict = {"filename": filename,
	              "acc_score": acc,
	              "gold_rel_count": len(gold_labels),
	              "pred_rel_count": len(pred_labels)}

	return score_dict


if __name__ == "__main__":
	p = argparse.ArgumentParser(description="")
	p.add_argument("goldfile", help="Shared task gold file in .rels format")
	p.add_argument("predfile", help="Corresponding file with system predictions")
	p.add_argument("-s", "--string_input", action="store_true", help="Whether inputs are filenames or strings")

	opts = p.parse_args()

	report_dict = get_accuracy_score(opts.goldfile, opts.predfile, opts.string_input)
	print(f"o File: {report_dict['filename']}")
	print(f"o Number of Gold Relation Classification Instances: {report_dict['gold_rel_count']}")
	print(f"o Number of Predicted Relation Classification Instances: {report_dict['pred_rel_count']}")
	print(f"o Accuracy Score for Relation Classification: {report_dict['acc_score']}")
