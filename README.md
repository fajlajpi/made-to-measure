# made-to-measure
Walking Tour: Made to Measure - customisable walking tour built out of pre-made chunks

## Idea
### One line pitch
Walking Tours meet made-to-measure tailoring.

### Elevator pitch
Buying a suit? Get one off the rack for a basic, "fits all but no-one perfectly" solution. 
Opposite end? Bespoke tailoring, as expensive as it gets.
Middle option? Made-to-measure. Start with a template and modify it in key places to achieve a great fit at a reasonable price.

Now apply the same to walking tours.
Off the rack? Join a tour, buy a book.
Bespoke? Hire a guide individually.
Made-to-measure? Get a basic tour that can be modified based on your interests.

## Current status
### V1: Original idea (completed in prototype)
Original idea of "made-to-measure" was technically "done", I created the tour generation script that would choose blocks in stops, always adding the mandatory ones, and optionally adding more.

However, after consulting with a more experienced developer, I realised I wasn't going to learn much more, I would instead have to create better data (which has nothing to do with programming) or improve the front-end experience (which I'm not currently interested in learning).

Therefore, V2!

### V2: New direction (in progress)
To focus more on learning, I want to take this in a new direction.

Instead of pre-made tours with slight modification, I will generate a tour based on a starting point and chosen parameters - end point, length, etc.

The code would look at all our available Stops and generate a list of them for the user to follow.

That means working with:
* GPS coordinate data 'Either using GeoDjango, or more simply with Pythagorean geometry)
* Generating a "walk" - possibly a tree structure
* Pathfinding - if we allow the user to pick an end-point, we need to reach it

All of these present interesting challenges with problems to solve and more to learn, so that's the way to go next.
