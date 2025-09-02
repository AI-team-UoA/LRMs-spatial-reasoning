from src_automation_app.update_accuracies import update_accuracies_Interface
from src_automation_app.heatmap_create import create_heatmap_Interface

class UserInputError(Exception):
    pass

if __name__ == '__main__':

	print("Welcome to the Automation App")

	exit = False
	while exit == False:
		print("There are many options to choose from. Below there is a list with options")
		print("1-Calculate Jaccard Index")
		print("2-Heatmap")
		print("3-Exit ")
	
		try:
			decide = int(input("Please choose one of the options above by pressing the corresponding number\n"))
			if decide < 0:
				raise UserInputError("Invalid input")
		except ValueError:
			raise UserInputError("Invalid input")
		
		if decide == 1:
			update_accuracies_Interface()
		elif decide == 2:
			create_heatmap_Interface()
		else:
			print("Exiting the program. Goodbye!")
			exit = True
