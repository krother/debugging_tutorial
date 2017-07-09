
import pandas as pd
import pylab as plt
from parse_uniprot import parse
import os


IN_PATH = '../data/'
OUT_PATH = '../output/'


def get_means(table):
    ss = table[table.columns[2:]].sum()
    return ss/ss.sum()

def prepare_df():
    homosap = pd.read_csv('../output/human_proteome.csv', index_col=0)
    chimp = pd.read_csv('../output/chimp_proteome.csv', index_col=0)
    banana = pd.read_csv('../output/banana_proteome.csv', index_col=0)

    means = pd.DataFrame(data = {
        'human': get_means(homosap),
        'chimp': get_means(chimp),
        'banana': get_means(banana),
        })
    return means


def calc_z(means):
    z = pd.DataFrame({
            'chimp': means['human'] / means['chimp'] - 1.0,
            'banana': means['human'] / means['banana'] - 1.0
            })
    z.plot.bar()
    plt.title('Proteome diversity')
    plt.ylabel('ratio of means human/x - 1.0')
    plt.xlabel('amino acid')
    plt.savefig('barplot.png')
    return z


    
if __name__ == '__main__':

    organisms = ['human', 'chimp', 'banana']

    for org in organisms:
        in_fn = "{}/{}.fasta".format(IN_PATH, org)
        out_fn = "{}/{}_proteome.csv".format(OUT_PATH, org)
        if not os.path.exists(out_fn):
            parse(in_fn, out_fn)

    means = prepare_df()
    print(means.sum())

    z = calc_z(means)
    print(z.abs().mean())
