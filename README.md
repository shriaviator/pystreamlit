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
 - [ ] "Text Comment"]=="A107" is a edge case  Vimp
 - [x] 6E 497 STV HYD is not appearing T/s required
      - remove_duplicate_flights(dataframe)
      - dataframe = dataframe.drop_duplicates(subset=['Flt Desg'])

## The Zen of Python, will be adhered !!

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- Special cases aren't special enough to break the rules.
- Although practicality beats purity.
- Errors should never pass silently.
- Unless explicitly silenced.
- In the face of ambiguity, refuse the temptation to guess.
- There should be one-- and preferably only one --obvious way to do it.
- Although that way may not be obvious at first unless you're Dutch.
- Now is better than never.
- Although never is often better than *right* now.
- If the implementation is hard to explain, it's a bad idea.
- If the implementation is easy to explain, it may be a good idea.
- Namespaces are one honking great idea -- let's do more of those!
