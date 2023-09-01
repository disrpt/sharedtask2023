""" Minors fixes for release 3  of DISRPT 2023 data.
"""

import glob, os, re


DATA_DIR = "../data"


def labels_to_lower_case():
    for corp in sorted(glob.iglob(os.path.join(DATA_DIR, "*", "*.rels"))):
        print(corp)

        with open(corp, 'r') as fi:
            data = fi.readlines()

        with open(corp, 'w', encoding='utf-8') as fo:
            for line in data:
                line = line.strip()
                fields = line.split("\t") #print(f"1-{fields[-1]}")
                fields[-1] = fields[-1].lower() #print(f"2-{fields[-1]}")
                fields[-2] = fields[-2].lower() #print(f"2-{fields[-1]}")
                new_line = "\t".join(fields)
                #print(new_line)
                fo.write(f"{new_line}\n")



if __name__ == "__main__":
    labels_to_lower_case()