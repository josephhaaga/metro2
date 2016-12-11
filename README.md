#What path is fastest? #

Goal is to determine scenarioes where an indirect path would be faster

##Project##

Answer the question: "Should I wait for the next train to my destination? Or would it be faster to take an indirect train that transfers?"

##Inspiration##

I was sitting in the U St. metro station waiting for my Yellow line train to Braddock Road, when a girl next to me asked how long I had been waiting. I told her I had been there about 10 minutes, but didn't really mind because it gave me a chance to read. The inbound trains screen was only showing Green trains, and she recommended that we hop on a Green line train to L'Enfant Plaza, and from there hop on the Blue line towards Franconia-Springfield.


Paths between two stations:
https://developer.wmata.com/docs/services/5476364f031f590f38092507/operations/5476364f031f5909e4fe330e

	- The path between two stations API endpoint just returns the direct "straight" yellow-line path
	- Green -> Blue ended up being potentially faster, especially when the sign wasn't showing any inbound Yellow line trains from UStreet
 
Station list:
https://developer.wmata.com/docs/services/5476364f031f590f38092507/operations/5476364f031f5909e4fe3311


Try: 
- Farragut North to L'Enfant Plaza
- NoMa Gallaudet to Smithsonian
