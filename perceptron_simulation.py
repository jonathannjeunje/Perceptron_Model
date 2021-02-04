# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'

# %% 
import pprint as pp
import json

# %%
def actual_output_fn(input, original_weight, threshold):
    weighted_sum = 0 
    for i in range(len(input)):
        weighted_sum += input[i] * original_weight[i]
    if weighted_sum < threshold: return 0
    else: return 1 

def new_weight_fn(current_weight, learning_coefficient, target_output, actual_output, input):
    size = len(original_weight)
    new_weight = [0]*size
    for i in range(size):
        new_weight[i] = current_weight[i] + learning_coefficient * (target_output - actual_output) * input[i]
    return new_weight

# %%
#Training data and Initial parameters
with open("data_or.json") as file: data = json.load(file)
# with open("data_and.json") as file: data = json.load(file)
# with open("data_1.json") as file: data = json.load(file)
pp.pprint(data)


# %%
current_weight = data["original_weight"]
size = len(data["input"])
actual_output = [0]*size
flag = 1
epoque = 0
while(flag == 1):
    epoque += 1
    print("\nEpoque", epoque,": ")
    for i in range(size):
        actual_output[i] = actual_output_fn(data["input"][i], current_weight, data["threshold"])
        updated_weight = new_weight_fn(current_weight, data["learning_coefficient"], data["target_output"][i], actual_output[i], data["input"][i])

        print("current_weight:", current_weight, "\nactual_output:", actual_output[i], "\nupdated_weight:", updated_weight, "\n")
        current_weight = updated_weight

    flag = 0
    for i in range(size):
        if target_output[i]^actual_output[i] == 1: 
            flag = 1
            break


# %%

# %%
