import numpy as np
import pandas as pd

authors = pd.read_excel("Test_names_authorlist.xlsx").iloc[3:11] # doing testing on the first 8 authors in the sheet

def generate_latex(df):
    df = df.sort_values(by="Last name") # Sort by last name
    affiliations = {}
    authors = []
    affil_index = 1
    
    for i, row in df.iterrows(): # Loop through all authors
        author_name = f"{row['Last name']}~{row['First name']}" # Format name
        author_affil_indices = []
        
        for affil_col, city_col in [("Affiliation 1", "City, Country 1"), ("Affiliation 2", "City, Country 2")]:
            if pd.notna(row[affil_col]) and pd.notna(row[city_col]): # Deal with one or two affiliation cases
                affil_str = f"{row[affil_col]}, {row[city_col]}" 
                if affil_str not in affiliations:
                    affiliations[affil_str] = affil_index
                    affil_index += 1
                
                author_affil_indices.append(str(affiliations[affil_str]))
        
        authors.append(f"\\author[{', '.join(author_affil_indices)}]{{{author_name}}}") # Append names to author part
    
    affil_lines = [f"\\affil[{idx}]{{{affil}}}" for affil, idx in affiliations.items()] # Append names to affil part
    
    return '\n'.join(authors + affil_lines)

latex_output = generate_latex(authors)
latex_file = "authors_list.tex"
with open(latex_file, "w", encoding="utf-8") as f:
    f.write(latex_output)


