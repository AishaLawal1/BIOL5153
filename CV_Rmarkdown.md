---
name: Aishat
surname: Lawal
position: "Graduate Research Assistant"
address: "University of Arkansas, Fayetteville"
phone: +1 4793329896
#www: mariecurie.com
email: "aolawal@uark.edu"
#twitter: mariecurie
#github: mariecurie
linkedin: "Aishat Lawal"
date: "`r format(Sys.time(), '%B %Y')`"
output: 
  vitae::awesomecv:
    page_total: true
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = FALSE, warning = FALSE, message = FALSE)
library(vitae)
#tinytex::install_tinytex(force = TRUE)
```

# Summary of research interest

I am a self-motivated scientist, passionate about research and driven by making meaningful interpretations from data. My current research focuses on using computational methods (or bioinformatics tools) to process and analyze genomic data from bacterial isolates responsible for different chicken diseases, with the overarching aim of developing effective prophylactic and/or control measures. I have had the opportunity to perform different molecular procedures (including DNA/RNA extraction, gel electrophoresis and qPCR) and analyze whole-genome sequence data for comparative and phylogenomic studies on the UNIX/Linux system and the High Performance Computing cloud system (HPC)
 

# Education

```{r}
library(tibble)
tribble(
  ~ Degree, ~ Year, ~ Institution, ~ Where,
  "Microbiology", "2011-2016", "Obafemi Awolowo University", "Nigeria",
  "Master of Cell and Molecular Biology", "2021-Till date", "University of Arkansas", "Fayetteville, Arkansas",
) %>% 
  detailed_entries(Degree, Year, Institution, Where)
```

# Work Experience

```{r}
tribble(
  ~outlook, ~Year, ~ Type, ~ Where,
  
  "conduct experiment using aseptic and molecular techniques, analyze and interpret genomic data", "2021-2023", "Research Assistant", "University of Arkansas, Fayetteville", 
  
"Managed the SMS Alert Business to ensure prompt delivery to all the Bank’s customers,	monitored the performance of the product and provided insights into how the products can be improved through data analysis", "2019-2021", "Product Manager, Card and Messaging Business", "First Bank of Nigeria Limited, Nigeria", 
  
) %>% 
  detailed_entries(outlook, Year, Type, Where)
    #glue::glue("{Type}"),
    #Year,
    #Desc
  
```

# Conference and Presentation
•	American Society for Microbiology South Central Branch (SCB-ASM) Meeting, Shreveport, Oct 28, 2022. Poster Presentation titled “Genomic characterization of Enterococcus species from infected Embryo”.

•	Bacterial and Viral Bioinformatics Resource Centre (BV-BRC) Bioinformatics Workshop, Argonne National Laboratory, Chicago, Illinois (Dec 14 -16, 2022)

•	University of Arkansas for Medical Sciences and University of Arkansas, Little Rock (UAMS-UALR) Genomics Workshop at Little Rock, Arkansas (March 21-23, 2021)

•	Droplet Digital PCR (ddPCR) training with BIORAD (Nov 30, 2022)


```{r}
#library(dplyr)
#knitr::write_bib(c("vitae", "tibble"), "packages.bib")

#bibliography_entries("packages.bib") %>%
  #arrange(desc(author$family), issued)
```

