import pandas as pd

# Creating a DataFrame
data = {
    "Name": ["Ali", "Sara", "Hassan"],
    "Age": [23, 21, 22],
    "City": ["Lahore", "Karachi", "Islamabad"]
}
df = pd.DataFrame(data)
print(df)
