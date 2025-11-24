"""
Cobb-Douglas Production Function — Analytical Block 1
-----------------------------------------------------
This script implements a standard Cobb-Douglas production function,
computes total output (Y), the marginal product of capital (MPK),
the marginal product of labor (MPL), and determines the returns to scale (RTS).

Author: Kevin A. Lorenzo C.
Training: Economics | Applied Analysis & Python
Repository: https://github.com/KLorenzoEconomics
"""

# ============================================================
# 1️⃣ Economic Inputs
# ============================================================

A = float(input("Enter A (TFP - Total Factor Productivity): "))
alpha = float(input("Enter α (capital elasticity): "))
beta = float(input("Enter β (labor elasticity): "))
K = float(input("Enter capital input (K): "))
L = float(input("Enter labor input (L): "))

# ============================================================
# 2️⃣ Cobb-Douglas Production Function
# ============================================================

def cobb_douglas(A: float, alpha: float, beta: float, K: float, L: float) -> float:
    """Returns total production Y under the Cobb-Douglas specification."""
    return A * (K ** alpha) * (L ** beta)

# ============================================================
# 3️⃣ Marginal Products (MPK & MPL)
# ============================================================

def mpk(A: float, alpha: float, beta: float, K: float, L: float) -> float:
    """Marginal product of capital (∂Y/∂K)."""
    return A * alpha * (K ** (alpha - 1)) * (L ** beta)

def mpl(A: float, alpha: float, beta: float, K: float, L: float) -> float:
    """Marginal product of labor (∂Y/∂L)."""
    return A * beta * (K ** alpha) * (L ** (beta - 1))

# ============================================================
# 4️⃣ Core Calculations
# ============================================================

Y = cobb_douglas(A, alpha, beta, K, L)
MPK = mpk(A, alpha, beta, K, L)
MPL = mpl(A, alpha, beta, K, L)

# ============================================================
# 5️⃣ Returns to Scale Classification
# ============================================================

exponent_sum = alpha + beta

if exponent_sum > 1:
    rts = "Increasing Returns to Scale"
elif exponent_sum == 1:
    rts = "Constant Returns to Scale"
else:
    rts = "Decreasing Returns to Scale"

# ============================================================
# 6️⃣ Final Economic Report
# ============================================================

print("\n------------------------------------------------------------")
print("              ECONOMIC REPORT — COBB-DOUGLAS MODEL")
print("------------------------------------------------------------")
print(f"Total Output (Y): {Y:.4f}")
print(f"MPK (∂Y/∂K): {MPK:.4f}")
print(f"MPL (∂Y/∂L): {MPL:.4f}")
print(f"Returns to Scale: {rts}")
print("------------------------------------------------------------\n")
