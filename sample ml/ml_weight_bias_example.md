
# Machine Learning Basics: Weights and Biases

## What are Weights and Biases?
- **Weights**: Coefficients that determine the importance of input features (e.g., how much "area" affects house price).
- **Bias**: A base value added to the prediction, independent of input features (e.g., minimum price even if area is zero).
---

## Example: Predicting House Price with `area`

### Problem Setup
**True Relationship**: `price = 2 * area` (weight=2, bias=0).  
**Goal**: Learn the weight and bias from data.

#### Data
| area | price |
|------|-------|
| 2    | 4     |
| 3    | 6     |

---

### Step-by-Step Training

#### Initial Values
- `weight = 0.5` (random guess)
- `bias = 0.0`
- `learning_rate = 0.1`

---

#### Epoch 1
1. **House 1** (area=2, price=4):
   - **Prediction**: `0.5 * 2 + 0.0 = 1.0`
   - **Error**: `4 - 1.0 = 3.0`
   - **Update Weight**: `0.5 + (0.1 * 3.0 * 2) = 1.1`
   - **Update Bias**: `0.0 + (0.1 * 3.0) = 0.3`

2. **House 2** (area=3, price=6):
   - **Prediction**: `1.1 * 3 + 0.3 = 3.6`
   - **Error**: `6 - 3.6 = 2.4`
   - **Update Weight**: `1.1 + (0.1 * 2.4 * 3) = 1.82`
   - **Update Bias**: `0.3 + (0.1 * 2.4) = 0.54`

**After Epoch 1**:  
`weight = 1.82`, `bias = 0.54`

---

#### Epoch 2
1. **House 1** (area=2, price=4):
   - **Prediction**: `1.82 * 2 + 0.54 = 4.18`
   - **Error**: `4 - 4.18 = -0.18`
   - **Update Weight**: `1.82 + (0.1 * -0.18 * 2) = 1.784`
   - **Update Bias**: `0.54 + (0.1 * -0.18) = 0.522`

2. **House 2** (area=3, price=6):
   - **Prediction**: `1.784 * 3 + 0.522 = 5.874`
   - **Error**: `6 - 5.874 = 0.126`
   - **Update Weight**: `1.784 + (0.1 * 0.126 * 3) = 1.8218`
   - **Update Bias**: `0.522 + (0.1 * 0.126) = 0.5346`

**After Epoch 2**:  
`weight = 1.8218`, `bias = 0.5346`

---

### Python Code
```python
# Training data: [area, price]
data = [[2, 4], [3, 6]]

# Initialize parameters
weight = 0.5
bias = 0.0
learning_rate = 0.1
epochs = 2

for epoch in range(epochs):
    print(f"\nEpoch {epoch + 1}:")
    for area, true_price in data:
        # Predict price
        predicted_price = (weight * area) + bias
        error = true_price - predicted_price

        # Update weight and bias
        weight += learning_rate * error * area
        bias += learning_rate * error

        # Print updates
        print(f"Area: {area}, Predicted: {predicted_price:.2f}, Error: {error:.2f}")
        print(f"Updated weight: {weight:.2f}, Updated bias: {bias:.2f}\n")
```

### Key Takeaways
#### Weights adjust based on:

- How much the feature (e.g., area) contributed to the error.

- Formula: weight += learning_rate * error * feature_value.

#### Bias adjusts based on the total error:

- Formula: bias += learning_rate * error.

Learning Rate controls the speed of adjustments.

Over epochs, weights and bias converge to the true values (weight=2, bias=0).

### Predicted Price=(weight×area)+bias
