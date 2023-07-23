

# BillBalancer

## Description

Welcome to Group Expense Tracker, a simple and intuitive Python program that takes the hassle out of managing expenses within a group of friends or colleagues. Say goodbye to messy calculations and disputes over who owes what. Let our tracker handle it all for you!

Group Expense Tracker utilizes graph algorithms and data structures to efficiently track expenses and calculate the amounts owed between group members. It ensures fairness in expense distribution and provides real-time updates as new expenses are added.

## Usage

1. Install Python on your computer.

2. Clone this repository to your local machine.

3. Run `main.py` using Python.

4. Follow the on-screen instructions to input the number of group members and their names.

5. Input expenses and who paid for them. The program will handle the rest!

6. View the calculated balances to see who owes or is owed what amount.

7. Continue adding expenses as needed, and the tracker will keep the accounts up to date.

## Data Structures Used

The Group Expense Tracker relies on the following data structures:

1. **Graph**: The program represents the group's financial relationships using an undirected graph. Each person in the group is a node in the graph, and edges between nodes indicate expenses paid.

2. **Hash Map (Dictionary)**: To efficiently manage names and their corresponding labels in the graph, the program uses a hash map (dictionary) to store the relationship between names and labels.

3. **2D Array (Matrix)**: The program utilizes a 2D array (matrix) to store the calculated expenses between group members. Each entry in the matrix represents the amount owed between two individuals.

## Example

Imagine three friends: Alice, Bob, and Carol. They went on a trip and incurred the following expenses:

- Alice paid $90 for groceries.
- Bob paid $50 for dinner.
- Carol paid $70 for movie tickets.

The Group Expense Tracker will display the following result:

