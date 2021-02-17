# A noob Journey from Python -> Pandas -> StreamLit -> Altair

- Journey is divided into two Areas 
  - Data sourced from gsheets and cleaning and tidying with Pandas
  - Visualisation of Data through StreamLit /Altair Chart 

- [Tidy Data Principles Used for Cleaning data](http://vita.had.co.nz/papers/tidy-data.pdf)
- StreamLit provides visualisation 
- Data is saved in python pickle for faster Loading

## To do list 

 - [ ] make pickle object with multiple variables 
  
 - [x] Airport List Sort
 - [ ] When dropping value based in the master dataset are there any edge cases 
 - [ ] "Text Comment"]=="A124" is a edge case  Vimp
 - [ ] 6E 497 STV HYD is not appearing T/s required
      - remove_duplicate_flights(dataframe)
      - dataframe = dataframe.drop_duplicates(subset=['Flt Desg'])
 - [ ] 