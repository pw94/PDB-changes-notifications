from rnapdbeefetcher import get_RNA_secondary_structure_via_browser


def print_detailed_report(structures_pairs, print_only_differences=False):
    """
    Print report with information whether structures in pair have identical or different RNA secondary structure
    and print RNA secondary structures of structures
    :param structures_pairs: List of structure IDs pairs (obsolete and superseding structure) which contain RNA chains
    :param print_only_differences: If True, structures which contain identical RNA secondary structure are omitted in report
    """
    print("*** REPORT ***")
    for obsolete, superseding in structures_pairs:
        obsolete_structure = get_RNA_secondary_structure_via_browser(obsolete)
        superseding_structure = get_RNA_secondary_structure_via_browser(superseding)
        if obsolete_structure == superseding_structure and not print_only_differences:
            print("# {} and {} have the same RNA secondary structure:".format(obsolete, superseding))
            print(obsolete_structure)
        else:
            print("# {} and {} have different RNA secondary structures:".format(obsolete, superseding))
            print("@ {}:".format(obsolete))
            print(obsolete_structure)
            print("@ {}:".format(superseding))
            print(superseding_structure)


def print_list_report(structures_pairs):
    """
    Print report with number and list of structure pairs which have identical RNA secondary structure
    and number and list of structure pairs which have different RNA secondary structure
    :param structures_pairs: List of structure IDs pairs (obsolete and superseding structure) which contain RNA chains
    """
    print("*** REPORT ***")
    different_structures = []
    identical_structures = []
    for obsolete, superseding in structures_pairs:
        obsolete_structure = get_RNA_secondary_structure_via_browser(obsolete)
        superseding_structure = get_RNA_secondary_structure_via_browser(superseding)
        if obsolete_structure == superseding_structure:
            identical_structures.append((obsolete, superseding))
        else:
            different_structures.append((obsolete, superseding))

    print("Identical RNA secondary structure have {} structures".format(len(identical_structures)))
    for obsolete, superseding in identical_structures:
        print("{} {}".format(obsolete, superseding))
    print("Different RNA secondary structure have {} structures".format(len(different_structures)))
    for obsolete, superseding in different_structures:
        print("{} {}".format(obsolete, superseding))
