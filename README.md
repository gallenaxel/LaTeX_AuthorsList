# LaTeX_AuthorsList
Repo for development of excel to latex authors list.

Run the python file, using e.g.
```
python3 xlsx_to_tex.py
```

to convert the authors list in ```Test_names_authorlist.xlsx``` to an appropriate ```.tex``` format, which is ```authors_list.tex```. The output is the following:

```
\author[1]{Duck~Donald}
\author[2, 3]{Gianotti~Fabiola}
\author[4]{Johnson~Boris}
\author[5]{Name~Another}
\author[6]{Name~Again}
\author[7]{Rabbit~Peter}
\author[6]{Senna~Ayrton}
\author[8]{The Great~Alexander}
\affil[1]{Laboratoire de Physique de Clermont-Auvergne (LPCA), Clermont-Ferrand, France}
\affil[2]{University of Warsaw, Warsaw, Poland}
\affil[3]{Deutsches Elektronen-Synchrotron DESY, Hamburg, Germany}
\affil[4]{Uppsala University, Uppsala, Sweden}
\affil[5]{Instituto de Física Corpuscular (CSIC – Universitat de València), Paterna (València), Spain}
\affil[6]{CERN, Geneva, Switzerland}
\affil[7]{University of Zürich, Zürich, Switzerland}
\affil[8]{Stockholm University, Stockholm, Sweden}
```







