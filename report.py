from rnapdbeefetcher import get_RNA_secondary_structure_via_browser


def print_detailed_report(structures_pairs):
    print("*** REPORT ***")
    for obsolete, superseding in structures_pairs:
        obsolete_structure = get_RNA_secondary_structure_via_browser(obsolete)
        superseding_structure = get_RNA_secondary_structure_via_browser(superseding)
        if obsolete_structure == superseding_structure:
            print("# {} and {} have the same RNA secondary structure:".format(obsolete, superseding))
            print(obsolete_structure)
        else:
            print("# {} and {} have different RNA secondary structures:".format(obsolete, superseding))
            print("@ {}:".format(obsolete))
            print(obsolete_structure)
            print("@ {}:".format(superseding))
            print(superseding_structure)
