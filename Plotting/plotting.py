import pandas as pd
import matplotlib.pyplot as plt

# Load the parsed data
file_path = "./parsed_final_data.csv"
data = pd.read_csv(file_path)

# Ensure the data types are correct
data['Trial'] = data['Trial'].astype(int)
data['State'] = data['State'].astype(int)
data['Q(left)'] = data['Q(left)'].astype(float)
data['Q(right)'] = data['Q(right)'].astype(float)
data['Q(forward)'] = data['Q(forward)'].astype(float)

# Create a list of Q-value columns for plotting
q_columns = ['Q(left)', 'Q(right)', 'Q(forward)']

# Iterate over Q-value columns to create individual plots
for q in q_columns:
    plt.figure(figsize=(10, 6))
    for state in data['State'].unique():
        state_data = data[data['State'] == state]
        plt.plot(state_data['Trial'], state_data[q], label=f'State {state}')
    
    plt.title(f"{q} Over Trials by State")
    plt.xlabel("Trial")
    plt.ylabel(q)
    plt.legend(title="State")
    plt.grid()
    plt.show()
