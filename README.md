# AI---Constraint-satisfaction-problems
A program that solves a genetic mutaion which is an Np-complete problem. Solved using local search and optimized algorithms
AI Satisfaction Problem
This repository contains a solution to the AI satisfaction problem using the genetic algorithm. The problem statement is as follows:

Given a set of customer satisfaction ratings for a product, determine the optimal set of features that maximizes overall satisfaction.

Getting Started
Prerequisites
Python 3
NumPy
Matplotlib (for visualizing the results)
Installation
Clone the repository and navigate to the directory:

Copy code
git clone https://github.com/<username>/ai-satisfaction-problem.git
cd ai-satisfaction-problem
Usage
To run the genetic algorithm, use the following command:

Copy code
python main.py
The algorithm will run for a set number of generations and will output the optimal set of features that maximizes overall satisfaction, as well as a graph showing the progress of the population over time.

Algorithm
The genetic algorithm used in this solution is a standard implementation that follows the basic process of selection, crossover, and mutation.

Selection: The top performing individuals are selected to move on to the next generation.
Crossover: The selected individuals mate to create offspring.
Mutation: A small percentage of the offspring are randomly mutated.
These steps are repeated for a set number of generations.

Data
The satisfaction data used in this solution is a sample set and should be replaced with actual data for a more accurate solution.

Conclusion
This solution uses genetic algorithm to find the optimal set of features that maximizes overall customer satisfaction, however it's important to note that this is just one approach and other optimization techniques such as gradient descent could be used too. The sample dataset used here is for demonstration purposes and should be replaced with actual data for better results.
