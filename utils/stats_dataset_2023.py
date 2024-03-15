# 0corpus_ 1lang_ 2framework_ 3rels_ 4rel_types_ 5discont_ 6train_toks_ 7train_sents_ 8train_docs_ 9dev_toks_ 10dev_sents_ 11dev_docs_ 12total_sents_ 13total_toks_ 14total_docs_ 15seg_style_ 16underscored_ 17syntax_ 18MWTs_ 19ellip_
#  18MWTs_ 19ellip_


import os
import re
import subprocess

class Dataset:
    def __init__(self, name, path) -> None:
        self.path = path
        self.name = name

        underscored = {'eng.pdtb.pdtb', 'eng.rst.gum', 'eng.rst.rstdt', 'tur.pdtb.tdb', 'zho.pdtb.cdtb'}
        self.underscored = "yes" if self.name in underscored else "no"

        syntax = {'eng.pdtb.pdtb': 'UD (gold)', 'eng.rst.gum': 'UD (gold)', 'eng.rst.rstdt': 'UD (gold)', 'zho.pdtb.cdtb': 'other (gold)'}
        self.syntax = syntax[name] if self.name in syntax.keys() else 'UD'


    def get_basics(self):
        if re.search('[a-z]+\.[a-z]+\.[a-z]+', self.name):
            p = re.match('([a-z]+)\.([a-z]+)\.[a-z]+', self.name)
            self.lang = p.group(1)
            self.frame = p.group(2)

        if self.frame == "rst" or self.frame == "sdrt" or self.frame == "dep":
            self.seg_style = "EDU"
        elif self.frame == "pdtb":
            self.seg_style = "Conn"


    def stats_rels(self):
        parts = ['dev', 'train']
        senses = set()
        count = 0
        for pa in parts:
            with open(f"{self.path}/{self.name}/{self.name}_{pa}.rels") as fr:
                self.discont = "no"
                for line in fr:
                    line = line.strip()
                    if line.startswith("doc	unit1_toks	unit2_toks	unit1_txt	uni"):
                        continue
                    elif re.search("<\*>", line):
                        self.discont = "yes"
                    sense = line.split("\t")[-1]
                    if sense != "_":
                        count += 1
                        senses.add(sense)
        self.rels = count
        self.rel_types = len(senses)


    def get_counts(self):
        self.mwts = "no"
        self.ellip = "no"
        parts = ['dev', 'train']
        for pa in parts:
            t = s = d = 0
            with open(f"{self.path}/{self.name}/{self.name}_{pa}.conllu") as fc:
                for line in fc:
                    line = line.strip()
                    if line.startswith("# newdoc"):
                        d += 1
                    elif line.startswith("# sent") or line.startswith("# newutterance"):
                        s += 1
                    elif line != "":
                        t += 1
                        if re.search('^\d+-\d+\t', line):
                            self.mwts = "yes"
                        if re.search('^\d+\.\d\t', line):
                            self.ellip = "yes"
                if pa == "dev":
                    self.dev_toks = t
                    self.dev_sents = s
                    self.dev_docs = d
                elif pa == "train":
                    self.train_toks = t
                    self.train_sents = s
                    self.train_docs = d


    def compute_total(self):
        self.total_sents = self.train_sents + self.dev_sents
        self.total_toks = self.train_toks + self.dev_toks
        self.total_docs = self.train_docs + self.dev_docs


    def print_stuff(self, fileo):
        with open(fileo, 'a', encoding='utf8') as fo:
            fo.write(f"{self.name}\t{self.lang}\t{self.frame.upper()}\t")
            fo.write(f"{self.rels}\t{self.rel_types}\t{self.discont}\t")
            fo.write(f"{self.train_toks}\t{self.train_sents}\t{self.train_docs}\t")
            fo.write(f"{self.dev_toks}\t{self.dev_sents}\t{self.dev_docs}\t")
            fo.write(f"{self.total_sents}\t{self.total_toks}\t{self.total_docs}\t")
            fo.write(f"{self.seg_style}\t{self.underscored}\t{self.syntax}\t")
            fo.write(f"{self.mwts}\t{self.ellip}")
            fo.write("\n")

if __name__ == "__main__":


    dirs = "../data"
    file_out = "stats_2023.txt"
    if os.path.isfile(file_out):
        subprocess.run(f"rm {file_out}", shell=True)

    for dir in os.listdir(dirs):

        dataset = Dataset(dir, dirs)
        dataset.get_basics()
        dataset.stats_rels()
        dataset.get_counts()
        dataset.compute_total()


        dataset.print_stuff(file_out)