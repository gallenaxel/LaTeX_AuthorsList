import numpy as np
import pandas as pd

editors = pd.read_excel("Authors_16feb_DRAFT.xlsx",sheet_name = 0)
authors = pd.read_excel("Authors_16feb_DRAFT.xlsx",sheet_name = 1)

def generate_latex(editors, authors):
    editors, authors = editors.sort_values(by="Last name"), authors.sort_values(by="Last name") # Sort by last name

    ## SORT THEM SEPARATELY AND THEN APPEND TO EACH OTHER - WILL SOLVE EVERYTHIGN
    df_sorted = pd.concat([editors, authors], axis=0)

    affiliations = {}
    df_list = []
    affil_index = 1
    
    for i, row in df_sorted.iterrows(): # Loop through all authors
        author_name = f"{row['First name']} {row['Last name']}" # Format name
        author_affil_indices = []
        author_affil_indices_fixed = []
        for affil_col, city_col in [("Affiliation 1", "City, Country 1"), ("Affiliation 2", "City, Country 2")]:
            if pd.notna(row[affil_col]) and pd.notna(row[city_col]): # Deal with one or two affiliation cases
                affil_str = f"{row[affil_col]}, {row[city_col]}" 
                if affil_str not in affiliations:
                    affiliations[affil_str] = affil_index
                    affil_index += 1
                
                author_affil_indices.append(str(affiliations[affil_str]))
        for index in author_affil_indices:
            author_affil_indices_fixed.append(f"$^{{{index}}}$")
        df_list.append(f"{author_name}{author_affil_indices_fixed[0]}, ") # Append names to author part

    affil_lines = [fr"$^{{{idx}}}$ {affil} \\" for affil, idx in affiliations.items()] # Append names to affil part
    print(*df_list)
    return ''.join(df_list), '\n'.join(affil_lines)

authors, editors = generate_latex(editors, authors)
latex_file = "List.tex"
with open(latex_file, "w", encoding="utf-8") as f:
    f.write(authors)
    f.write(editors)


