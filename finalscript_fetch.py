import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='/home/yami/rsids.txt')
parser.add_argument('gvf_file', help='/home/yami/bos_taurus.gvf')
args = parser.parse_args()

rsids = []

with open(args.input_file, 'r') as f:
    for line in f:
        rsids.append(line.strip())

with open(args.gvf_file, 'r') as f, open('output.txt', 'w') as out:
    for line in f:
        if not line.startswith('#'):
            fields = line.strip().split('\t')
            attributes = dict(item.split('=') for item in fields[8].split(';'))
            if 'Dbxref' in attributes and attributes['Dbxref'].split(':')[1] in rsids:
                rsid = attributes['Dbxref'].split(':')[1]
                chrom = fields[0]
                pos = fields[3]
                ref = attributes['Reference_seq']
                alt = attributes['Variant_seq']
                out.write(f'{rsid}\t{chrom}\t{pos}\t{ref}\t{alt}\n')

