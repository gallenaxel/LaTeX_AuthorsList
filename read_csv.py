import numpy as np
import pandas as pd

authors = pd.read_excel("authors.xlsx").iloc[3:11] # doing testing on the first 8 authors in the sheet

authors_input = authors.sort_values(by="Last name") # Sorting by last name

def generate_latex(df):
    affiliations = {}
    authors = []
    affil_index = 1
    
    for i, row in df.iterrows():
        author_name = f"{row['Last name']}~{row['First name']}"
        author_affil_indices = []
        
        for affil_col, city_col in [("Affiliation 1", "City, Country 1"), ("Affiliation 2", "City, Country 2")]:
            if pd.notna(row[affil_col]) and pd.notna(row[city_col]):
                affil_str = f"{row[affil_col]}, {row[city_col]}"
                
                if affil_str not in affiliations:
                    affiliations[affil_str] = affil_index
                    affil_index += 1
                
                author_affil_indices.append(str(affiliations[affil_str]))
        
        authors.append(f"\\author[{', '.join(author_affil_indices)}]{{{author_name}}}")
    
    affil_lines = [f"\\affil[{idx}]{{{affil}}}" for affil, idx in affiliations.items()]
    
    return '\n'.join(authors + affil_lines)

latex_output = generate_latex(authors_input)
print(latex_output)

