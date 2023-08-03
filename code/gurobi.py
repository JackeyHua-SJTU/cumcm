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