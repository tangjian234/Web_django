# ML_Name_Identification_Crawler.md
- [ML_Name_Identification_Crawler.md](file:///C:/Local/Work/ML_Name/Note/ML_Name_Identification/ML_Name_Identification_Crawler.md) 

[![GitHub Issues](https://img.shields.io/github/issues/zalandoresearch/flair.svg)](https://github.com/zalandoresearch/flair/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Travis](https://img.shields.io/travis/zalandoresearch/flair.svg)](https://travis-ci.org/zalandoresearch/flair)

## Todo

## Vision

- First good example of how to create raw data for training

## Objective

- Use faker to create names according to nationality

## Content

### What

1.  Use faker to create 10,000 Japense Convert Japanese name into romanji format
2.  Create Hindi name, converted to latin format .
3.  Created German, Italy and hindi names

- Crated new nationality names : German, Italy, hindi

### Output

C:\Local\Work\ML_Name\Code\Test\data
csv files :

### Learnt :

#### Normally training data format : CSV

##### csv format : easy to read and process.

- Format :
  - first line: column names :
  - e.g code,name
  - next lines: :

#### CSV file processing

1. Load csv into a panda data frame
   df = f_lib.load_csv_file(file_name)

2. Write file as csv format

   1. def generate_name_file(country, num=2, file_name=''):
   2. generate_name_file('de_DE',10000,'a1.csv')

#### Official Language ID

- Use LANGUAGE_BY_LOCALE as language ID

  LANGUAGE_BY_LOCALE = {
  'de_DE': "German (Germany)",
  'fr_FR': 'French (France)',
  'it_IT': 'Italian (Italy)',
  'hi_IN': 'Hindi (India)',
  'hi_IN': 'Hindi (India)',
  'ja_JP': "Japanese (Japan)",
  'ja': "Japanese",
  }

## Reference
