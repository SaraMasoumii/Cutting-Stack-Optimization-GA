# Cutting Stock Problem Solver  
This project implements a **Genetic Algorithm (GA)** to solve the **Cutting Stock Problem**, an NP-hard optimization challenge. The goal is to minimize material wastage by efficiently cutting stock materials into requested sizes while fulfilling all requirements using the fewest rolls.  

## 📝 Table of Contents  
- [Features](#features)  
- [File Structure](#file-structure)  
- [Prerequisites](#prerequisites)  
- [Usage](#usage)  
- [Problem Overview](#problem-overview)  
- [Optimization Algorithms](#optimization-algorithms)  

## ✨ Features  
- **Efficient Roll Usage**: Uses a genetic algorithm to minimize the number of rolls needed to fulfill all requests.  
- **Customizable Inputs**: Supports dynamic stock lengths and request sets provided via input files.  
- **Optimized Performance**: Implements mutation, crossover, and fitness evaluation strategies for GA optimization.  
- **Flexible Output**: Provides detailed results of roll usage and material wastage for analysis.  

## 📁 File Structure  
Here is the file structure for the project:  

```plaintext  
Cutting-Stack-Optimization-GA/  
├── input1.txt             # Input file containing stock length and requests (example 1)  
├── input2.txt             # Input file containing stock length and requests (example 2)  
├── input3.txt             # Input file containing stock length and requests (example 3)  
├── input4.txt             # Input file containing stock length and requests (example 4)  
├── main.py                # Python script implementing the GA solution  
├── README.md              # Project documentation (this file)  
```  

## 📋 Prerequisites  
- **Python 3.7 or higher**: Required for running the solution.  
- Python Libraries: Install the required libraries using:  
  ```bash  
  pip install numpy  
  ```  
- Input Files: Provide input files with stock lengths and requests in the following format:  
  ```plaintext  
  Stock Length: 100  
  Requests: 22, 7, 5, 3, 28  
  ```  

## 💻 Usage  
1. **Setup**: Ensure all prerequisites are installed.  
2. **Prepare Inputs**: Place your input files in the same directory as the script.  
3. **Run the Script**: Execute the GA solution:  
   ```bash  
   python main.py input1.txt  
   ```  
4. **View Results**: The output displays the number of rolls used and a summary of the cutting plan.  

## 🔍 Problem Overview  
The **Cutting Stock Problem** involves cutting standard-sized rolls into pieces of requested sizes with minimal wastage. For example, given a 10-meter roll and requests for pieces of 3, 5, and 7 meters, the objective is to fulfill these requests with the fewest rolls.  

### Inputs:  
- **Stock Length**: Total length of the stock material.  
- **Requests**: List of required piece lengths.  

### Outputs:  
- **Roll Count**: Number of rolls used.  
- **Waste**: Total unused material after fulfilling all requests.  

## 🧠 Optimization Algorithms  
This project uses a **Genetic Algorithm** to solve the problem. Key features include:  

1. **Population Initialization**: Random generation of initial cutting plans.  
2. **Fitness Function**: Evaluates roll usage and material wastage for each solution.  
3. **Selection**: Chooses the best solutions for reproduction.  
4. **Crossover**: Combines solutions to create offspring.  
5. **Mutation**: Introduces randomness to avoid local optima.  

The algorithm iteratively refines solutions until a stopping criterion is met, such as a maximum number of generations or minimal wastage achieved.  
