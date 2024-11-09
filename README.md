# The Power of Cooperation


## Iterated Prisoner's Dilemma Simulator

This Python program explores the dynamics of cooperation in iterated prisoner's dilemma scenarios. Use it to simulate and analyze how different strategies fare against each other in repeated interactions.

## Key Features

Run Simulations: Execute main.py and follow the prompts to configure and run your simulations.
    
Customize Strategies: Craft your own strategies in functions.py. mine is the list of my moves so far, other is the list of my opponent's moves so far, and move is the current move number. Simply define a function for your strategy and add its name to the available_players set and the find_move function.
    
Testing: Use test.py to conduct tests, where the element of randomness is removed from the simulation.


Dive deeper into the complexities of game theory and the emergence of cooperation!

## New Strategies
Motivated by tit-for-tat's underwhelming performance in noisy environments, two new strategies "advanced-tit-for-tat" and "delayed-tit-for-two-tats." were designed.

"advanced-tit-for-tat": it plays like tit-for-tat except it will forgive retaliatory defections.
"delayed-tit-for-two-tats": it plays like tit-for-tat for the first n rounds, then it plays like tit-for-two-tats for the rest of rounds.

## License

This project is licensed under the Eclipse Public License 2.0 - see the [LICENSE](LICENSE) file for details.
