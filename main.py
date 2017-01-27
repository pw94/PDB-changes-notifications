from argparse import ArgumentParser
from laststructures import get_last_load_query, get_obsoletes
from structuresstatus import get_obsoletes_for, get_supersedings_for
from rna import contains_RNA_chains

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("-a", "--all", action="store_true", help="process entire list of obsolete structures")
    args = parser.parse_args()

    structures_pairs = []

    if not args.all:
        supersedings = get_last_load_query()
        structures_pairs = get_obsoletes_for(supersedings)
    else:
        obsoletes = get_obsoletes()
        structures_pairs = get_supersedings_for(obsoletes)
    
    structures_pairs = [(obsolete, superseding) for obsolete, superseding in structures_pairs if contains_RNA_chains(obsolete) and contains_RNA_chains(superseding)]
