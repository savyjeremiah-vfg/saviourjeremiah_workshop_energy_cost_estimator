<<<<<<< HEAD
# CTE213 PROJECT: WORKSHOP ENERGY COST ESTIMATOR

**Student Name:** Saviour Jeremiah Etim  
**Department:** Mechatronics Engineering  
**Level:** ND2  
**Institution:** Yaba College of Technology (YABATECH)  
**Matric Number:** F/ND/24/3450003  
**Course Code:** CTE213  

## 1. Project Description

The Workshop Energy Cost Estimator is a Python program designed to calculate the electrical energy consumption and electricity cost of machines used in a workshop.

The program allows users to enter the names, power ratings, and daily working hours of different machines. It then calculates their daily energy consumption in kilowatt-hours (kWh), total electricity cost, and estimated monthly expenses.

It also provides energy-saving recommendations using PLC timers to help reduce unnecessary electricity consumption.

## 2. Objectives of the Project

The objectives of this project are to:

- Calculate the energy consumed by workshop machines.
- Estimate daily and monthly electricity costs.
- Identify machines with high power ratings.
- Classify the workshop based on its energy consumption.
- Provide basic energy-saving recommendations using PLC timers.

## 3. Programming Language and Tools Used

- **Programming Language:** Python
- **Code Editor:** Visual Studio Code (VS Code)
- **Version Control:** Git
- **Online Repository:** GitHub

## 4. How the Project Was Developed (Step by Step)

### Step 1: Importing the Required Knowledge

I started by identifying the problem I wanted to solve: estimating the energy consumption and electricity cost of machines used in a workshop.

I decided to use Python because it supports calculations, conditional statements, loops, lists, and functions.

### Step 2: Creating the Energy Calculation Function

I created a function called `calc_kwh()` to calculate the energy consumed by each machine.

The formula used is:

Energy (kWh) = (Power in Watts ÷ 1000) × Time in Hours

This converts the machine's power rating from watts to kilowatts before multiplying it by the number of working hours.

### Step 3: Creating the Cost Calculation Function

I created another function called `calc_cost()` to calculate the electricity cost.

The formula is:

Cost = Energy Consumption × Electricity Tariff

The user enters the electricity tariff per kWh in Naira.

### Step 4: Creating the PLC Energy-Saving Function

I developed a function called `energy_saving_status()`.

This function checks the power rating of each machine and provides recommendations:

- Above 1500W: High power – Use PLC timer.
- Above 800W: Medium power – Can use timer.
- 800W and below: Low power – OK.

This is the additional feature I introduced to make the project more useful in a mechatronics workshop.

### Step 5: Collecting User Information

I used the `input()` function to collect information from the user.

The program asks for:
- Number of machines in the workshop.
- Name of each machine.
- Power rating of each machine in watts.
- Daily working hours of each machine.
- Electricity tariff per kWh.

### Step 6: Storing the Information

I used Python lists to store the machine names, power ratings, working hours, and calculated energy consumption.

The lists used include:

- `machine_names`
- `machine_power`
- `machine_hours`
- `machine_kwh`

This makes it possible to access and process the information later.

### Step 7: Using Loops to Process the Machines

I used a `for` loop to collect information about each machine and calculate its energy consumption.

Another loop was used to calculate the total daily energy consumption of all the machines.

### Step 8: Calculating Daily and Monthly Costs

After collecting the machine information, the program calculates:

- Individual machine energy consumption.
- Total daily energy consumption.
- Total daily electricity cost.
- Monthly energy consumption based on 30 days.
- Estimated monthly electricity cost.

### Step 9: Analysing Workshop Energy Consumption

I added conditional statements (`if`, `elif`, and `else`) to classify the workshop according to its total daily energy consumption.

The program identifies the workshop as having low, medium, or high energy consumption.

It also counts the number of machines with power ratings above 1000W and identifies the machine with the largest daily energy consumption.

### Step 10: Adding My Own Twist

My additional feature is the PLC Energy-Saving Recommendation.

The program checks machines with high power ratings and recommends the use of PLC timers to help manage their operating periods.

It also suggests that high-power machines could save energy if unnecessary operating hours are reduced.

### Step 11: Testing the Program

After writing the code, I ran the program in Visual Studio Code.

I entered sample machine information, power ratings, working hours, and electricity tariffs to check whether the calculations and recommendations worked as expected.

### Step 12: Uploading the Project to GitHub

After completing the Python program, I saved the source code in my project folder.

I used Git to manage the project and GitHub to store and share the code online.

The commands used include:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/savyjeremiah-vfg/project-.git
git push -u origin main
```

For subsequent updates, I used:

```bash
git add .
git commit -m "Updated project"
git push
```

## 5. Python Concepts Used

The following Python concepts were applied in developing this project:

1. **Variables:** Used to store machine information and calculation results.
2. **Functions:** Used to organise energy calculations, cost calculations, and PLC recommendations.
3. **Lists:** Used to store machine names, power ratings, working hours, and energy consumption.
4. **For Loops:** Used to process multiple machines.
5. **Conditional Statements:** Used to classify energy consumption and provide recommendations.
6. **User Input:** Used to collect information from the user.
7. **Arithmetic Operations:** Used to perform energy and cost calculations.

## 6. Expected Output

When the program runs successfully, it displays:

- The energy consumption of each machine.
- Total daily energy consumption.
- Daily electricity cost in Naira.
- Monthly energy consumption.
- Monthly electricity cost.
- Largest daily energy consumption.
- Number of machines above 1000W.
- Workshop energy classification.
- PLC energy-saving recommendations.

## 7. Conclusion

The Workshop Energy Cost Estimator demonstrates how Python programming can be applied to solve practical problems in a mechatronics workshop.

Through this project, I gained practical experience in using Python functions, variables, lists, loops, conditional statements, and arithmetic operations.

The project also helped me understand the relationship between electrical power, energy consumption, electricity costs, and the use of PLC timers for energy management.

**Developed by: Saviour Jeremiah Etim**  
**ND2 Mechatronics Engineering, YABATECH**  
**Course: CTE213**
=======
# saviourjeremiah_workshop_energy_cost_estimator
>>>>>>> 8ce89ba18de99c62a332a62155eb4eaaaa17ac78
