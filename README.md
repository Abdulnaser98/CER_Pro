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
├── 📁 data                 <-- Data sources (stored in the following order):
│   ├── 📁 data             <-- Raw data extracted from websites
│   ├── 📁 processed_data   <-- Preprocessed data
│   ├── 📁 filtered         <-- Filtered data: abstracts matching query (AI/sustainable/energy)
│   └── 📁 concatenated     <-- Concatenated filtered data from three sources for topic modeling
│
├── 📁 results              <-- Visualizations of topic modeling results
│   └── ...
│
├── 📁 notebooks            <-- Jupyter notebook files
│   └── ...
│
├── 📁 src                  <-- Project code base (executed in the following order):
│    ├── data_extraction     <-- Data extraction, query selection, and deduplication
│    │    └── scrapers       <-- Web scrapers for abstract extraction
│    │    │    └── acm_links_scraper.py       <-- ACM website links scraper
│    │    │    └── acm_abstract_scraper.py    <-- ACM website abstract scraper
│    │    │    └── science_direct_data_scraper.py <-- Science Direct website scraper
│    │    │    └── xplore.py  <-- Xplore website scraper
│    │    │    └── xplore_enrich.py <-- Xplore website scraper (enriched)
│    │    │
│    │    └── query_selection <-- Query selection logic
│    │    │
│    │    └── deduplicating   <-- Deduplication of combined data
│    │        └── deduplicating.py <-- Duplicated papers removal
│    │        └── filter_out_html_tags.py <-- Removal of HTML tags
│    │
│    ├── data_preprocessing  <-- Preprocessing of scraped data
│    │   └── preprocessing.py 
│    │
│    ├── nlp_analytics       <-- Topic modeling implementation
│
├── 📃 .gitignore           <-- Git ignore list
│
├── 📃 environment.yml      <-- Conda environment dependencies
│
├── 📃 main.py              <-- Algorithm comparison
│
├── 📃 pyproject.toml       <-- Configuration file
│
└── 📃 README.md            <-- Project documentation

```








































