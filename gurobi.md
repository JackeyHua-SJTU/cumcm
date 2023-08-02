# Gurobi Quickview
- [startup quickly](https://zhuanlan.zhihu.com/p/52371462?from_voters_page=true)
- Solve _linear and quadratic_ problem.

# Structure
```python
import gurobipy
# coefficient of target expression
c = [8, 10, 7, 6, 11, 9]
# coefficient of constraint expression f(x) >= r
p = [[12, 9, 25, 20, 17, 13],
    [35, 42, 18, 31, 56, 49],
    [37, 53, 28, 24, 29, 20]]
# Value in the constraint
r = [60, 150, 125]
# Create a model 
# Usually Step 1 in solving
MODEL = gurobipy.Model("Example")

# Create variable
# lb = lower bound, default to be 0.0
# ub = upper bound, default to be gurobipy.GRB.INFINITY
# vtype = {GRB.CONTINUOUS, GRB.BINARY (0-1), GRB.INTEGER}
x = MODEL.addVars(6, lb=0, ub=1, name='x')

# update the model after initialization
MODEL.update()

# add objective function
# specify minimize or maximize
# IMPORTANT!
# prod = product, is very similar to vector dot product.
# It multiplies elements in the same place and adds them together.
# x.prod(c) = (x1,x2,x3).prod(c1,c2,c3) = x1c1 + x2c2 + x3c3
MODEL.setObjective(x.prod(c), gurobipy.GRB.MINIMIZE)

# add constraint
MODEL.addConstrs(x.prod(p[i]) >= r[i] for i in range(3))

# execute
MODEL.params.LogToConsole = True # print the whole process
MODEL.optimize()
# check the answer
print("Obj:", MODEL.objVal)
# check the value of each variable
for v in MODEL.getVars():
    print(f"{v.varName}：{round(v.x,3)}")
```

# Details
1. **Sum**. 
   $$\sum_{j\in J} x_{i,j} \le 5, \forall i \in I $$ 
   is equivalent to 
   ```python
    for i in I:
        Model.addConstr(quicksum(x[i, j] for j in J) <= 5)
   ```

   $$\sum_{i\in I}\sum_{j \in J} x_{i,j} \times c_{i,j}$$ 
   is equivalent to 
   ```python
    quicksum(x[i, j] * c[i, j] for i in I for j in J)
   ```

2. **Create multi variables.**
    
    `x = MODEL.addVars(3, 4, 5, lb=0, ub=1, name='x')` The first parameter is dimention. In this case, a $3 \times 4\times 5$ matrix of variables are created. Access the value by `x[i, j, k]` .

3. **Add multi objectives.**

    `setObjectiveN(expression, index, priority, weight)`
    - Index gives each expression an id.
    - Priority decides the order in optimization. The higher, the earlier.
    - Weight matters in same priority.

    Piecewise linear -> `setPWLObj(var, x, y)`. x refers to an array indicating the piecewise point.

4. **Add constraints.**
   - Range constraints. `addRange(expression, min_value, max_value, name)`
   - Indicator constraints.
     - Solve questions like $x_1,x_2,x_3 = 0$ or $\ge 80$
     - ```python
        for i in range(3):
            Model.addGenConstrIndicator(y[i + 1], 1, x[i + 1] >= 80)
            Model.addGenConstrIndicator(y[i + 1], 0, x[i + 1] == 0)
        ```

# Examples 
4.2 and 4.3 in [startup quickly](https://zhuanlan.zhihu.com/p/52371462?from_voters_page=true)