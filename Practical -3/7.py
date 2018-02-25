# Q-7 : Write a Python program to convert list to list of dictionaries.
#		Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000",
#		"#800000", "#FFFF00"]
#		Expected Output:
# 		[{'color_name': 'Black', 'color_code': '#000000'},
#		 {'color_name':'Red', 'color_code': '#FF0000'},
#		 {'color_name': 'Maroon', 'color_code': '#800000'},
#		 {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

color_name = ["Black", "Red", "Maroon", "Yellow"]
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])
