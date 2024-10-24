import json

# Create a list to hold dog and cat information
animals = []

# Dog information
dog = {
    "name": "Steve",
    "age": 15,
    "had_sex": True
}

# Append dog information to the list
animals.append(dog)

# Write the list to the JSON file
with open('dog_info.json', 'w') as f:
    json.dump(animals, f, indent=2)  # Store as a list

# Cat information
cats = {
    "name": "Alex",
    "age": 10,
    "living": None
}

# Open the same file in append mode and load existing data
with open('dog_info.json', 'r+') as file:
    # Load the existing data
    data = json.load(file)
    data.append(cats)
    file.seek(0)
    json.dump(data, file, indent=2)  # Write updated data back to the file
    file.truncate()  # Remove any leftover data after the new content

with open('dog_info.json') as read_file:
    data = json.load(read_file)  # Use read_file to load JSON
    print(data)  # Output the data
