# 1.

[ML_data_prepare.md](file:///c:/Local/Work/ML_Name/Note/ML_data_prepare.md)

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## todo

- [ ] download [amazon database](#database)


https://htmledit.squarefree.com/

## database

[27-06]

- [The 25 Best Datasets for Natural Language Processing](https://lionbridge.ai/datasets/the-best-25-datasets-for-natural-language-processing/)

- **Amazon reviews data**

  - http://jmcauley.ucsd.edu/data/amazon/
  - http://deepyeti.ucsd.edu/jianmo/amazon/index.html
    https://snap.stanford.edu/data/web-Amazon.html
    // TODO : review and download

- [The Blog Authorship Corpus](http://u.cs.biu.ac.il/~koppel/BlogCorpus.htm)

- [20 Newsgroups](http://qwone.com/~jason/20Newsgroups/)

## Text vectorization

#### Bag of word

1.  -[Source](https://towardsdatascience.com/your-guide-to-natural-language-processing-nlp-48ea2511f6e1)

assume give each use the occurance as 1,0

for example :
vocabulary is jian tang li wang

jian tang 1 1 0 0
wang li 0 0 1 1
li jian 1 0 1 0

  <It make sure that every s is unique>
