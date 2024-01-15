# Explenation:
we First created 2 dictionaries `wins​` and `losses` to keep track of the wins and losses of each player where:
- `wins[i]` will contain 0 if the person `i` has won atleast one mach
- `losses[i]` will contain the number of games person `[i]` has lost ​
after that we iterate through `wins` if the person with a winning count does not have a `losses` count this person will have not lost a single game. and we search in losses for a person with a `loss` value of 1 and this perosn will be a person who has lost only once <br>
and at then end return `[wins,one_loss]`
