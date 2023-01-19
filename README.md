# Map Coloring Problem
![image](https://user-images.githubusercontent.com/84153519/213347217-5a3c0356-5b07-4b49-bc2c-7306f6390e04.png)


This repository contains a solution to the map coloring problem using the genetic algorithm. The problem statement is as follows:

Given a map of territories, color the territories such that no two adjacent territories have the same color.

## Getting Started

### Prerequisites

- Python 3
- NumPy
- Matplotlib (for visualizing the results)

### Installation

Clone the repository and navigate to the directory:


### Usage

To run the genetic algorithm, use the following command:

python main.py


The algorithm will run for a set number of generations and will output the optimal coloring of the map that satisfies the constraints, as well as a graph showing the progress of the population over time.

## Algorithm

The genetic algorithm used in this solution is a standard implementation that follows the basic process of selection, crossover, and mutation.

1. Selection: The top performing individuals (colorings) are selected to move on to the next generation.
2. Crossover: The selected individuals (colorings) mate to create offspring.
3. Mutation: A small percentage of the offspring are randomly mutated.

These steps are repeated for a set number of generations. The fitness function used to evaluate the performance of each individual takes into account the number of constraints satisfied by the coloring.

## Data

The map data used in this solution is a sample set and should be replaced with actual data for a more accurate solution.

## Conclusion

This solution uses genetic algorithm to find the optimal coloring of the map that satisfies the constraints of no two adjacent territories having the same color. However, it's important to note that this is just one approach and other optimization techniques such as simulated annealing or constraint programming could also be used. The sample map dataset used here is for demonstration purposes and should be replaced with actual map data for better results.
