# Some key notes on Methods and data collection from the paper

### Methods: 

* probabilistic topic assignment vector was constructed using LDA 
* sentence embeddings were generated using BERT
*  the probabilstic topic assignment vector and the Bert embeddings of the sentences were combined togother in 
   order to balance the information contenct of each vector
*  lower-dimensional latent space representation of the combined vector was generated
*  The Silhouette Score was calculated in order to measure the clusters quality (the nearer the value to one,the
   better the quality)
   
   
   
### Data collection: 
*  Inside the corpus , the following keywords inside the title , keyword , and abstract were searched: like 
   "artifical intelligence" OR "AI" AND "sustainable" OR "Sustainability" And "energy"
*  This resulted in the retrievel of 981 documents

*  The document type was restricted to article and the langauge to "English" and this exclusion resulted in 296 
   articles. 

*  Following that , the titles and abstracts of the articles were manually evaluated to identify the most pertinent    ones that examined the role of artifical intelligence in ensuring the energy sector's sustainability and this  
   screnning yield 182 publications spanning the years 2004 and 2022. 

 

### Repository structure

``` plain
├── 📁 data                 <-- Package that contains different data sources (data preprocessed in the following order):
│   ├── 📁 data             <-- Raw data extracted for the three websites (without any preprocessing or filtering)
│   ├── 📁 processed_data   <-- The preprocessed data 
│   ├── 📁 filtered         <-- The filtered data, only abstracts that match the following query ==> ( [ai or artificial intelligence] and [sustainable or sustainability] and energy )
│   └── 📁 concatenated     <-- The filtered data from the three data sources are concatenated into one dataframe that should be used in topic modeling processeys
│
├── 📁 results              <-- visualizations about the results retrieved after conducting the topic modeling process
│   └── ...
│
├── 📁 notebooks            <-- Directory for Jupyter notebook files
│   └── ...
│
├── 📁 src                  <-- The code base of the project
│    ├── data_extraction     <-- web scraper python files to extract the abstracts of the papers
│    │    └── scrapers
│    │    │    └── acm_links_scraper.py       <--  links scraper for the website "acm"
│    │    │    └── acm_abstract_scraper.py    <--  abstract scraper for the website "acm" 
│    │    │    └── science_direct_data_scraper.py <-- scraper for the website "science direct" 
│    │    │    └── xplore.py  <-- scraper for the website "xplore" 
│    │    │    └── xplore_enrich.py <-- scraper for the website "xplore"
│    │    │
│    │    └── query_selection
│    │    │
│    │    └── deduplicating   <-- filter out duplicated papers after combining the data of the three resources
│    │        └── deduplicating.py <-- remove duplicated papers 
│    │        └── filter_out_html_tags.py <-- remove html tags from the data
│    │
│    ├── data_preprocessing  <-- preprocessing of the scrapped data
│    │   └── preprocessing.py 
│    │
│    ├── nlp_analytics       <-- Topic modeling implementation. 
│
├── 📃 .gitignore           <-- List of files and folders that should be ignored by git
│
├── 📃 environment.yml      <-- List of python dependencies for the conda environment
│
├── 📃 main.py              <-- Compare algorithms
│
├── 📃 pyproject.toml       <-- Configuration file
│
└── 📃 README.md            <-- Project documentation
```








































