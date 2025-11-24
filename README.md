📈 Cobb–Douglas Production Analysis

A clean and extensible Python implementation of the Cobb–Douglas production function, including:

Total output Y

Marginal Product of Capital (MPK)

Marginal Product of Labor (MPL)

Returns to Scale (increasing, constant, decreasing)

This repository is part of a broader project on computational economics, numerical modeling, and applied microeconomic analysis.

🔢 1. Mathematical Model

The standard Cobb–Douglas production function is defined as:

Y = A * K^α * L^β


Where:

Symbol	Meaning
A	Total Factor Productivity (TFP)
K	Capital input
L	Labor input
α	Output elasticity of capital
β	Output elasticity of labor

Marginal Products
MPK = ∂Y/∂K = A * α * K^(α - 1) * L^β
MPL = ∂Y/∂L = A * β * K^α * L^(β - 1)

Returns to Scale
If α + β > 1 → Increasing Returns  
If α + β = 1 → Constant Returns  
If α + β < 1 → Decreasing Returns  

🧪 2. Running the Script

Execute the model with:

python cobb_douglas_analysis.py


You will be prompted to enter values for:

A (TFP)

α (capital elasticity)

β (labor elasticity)

K (capital input)

L (labor input)

📂 3. File Structure
cobb-douglas-production-analysis/
│── cobb_douglas_analysis.py
└── README.md

📘 4. Sample Output
----------------------------------------------
      ECONOMIC REPORT — COBB–DOUGLAS MODEL
----------------------------------------------
Total Output (Y): 156.9168
MPK (∂Y/∂K): 0.5492
MPL (∂Y/∂L): 0.5100
Returns to Scale: Constant
----------------------------------------------

👨‍💻 Author

Kevin A. Lorenzo C.
Computational Economics • Applied Microeconomics • Python Modeling
GitHub: https://github.com/KLorenzoEconomics
