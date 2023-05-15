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
   screnning yield 182 publicationsspanning the years 2004 and 2022. 

 
       








































