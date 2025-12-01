import datetime

print (" Welcome PLDT Workers & Staffs ")

record ={}

while True:
	print ()
	print ("Menu")
	print("1. Time-In")
	print("2. Time-Out")
	print("3. View Attendance Logs")
	print("4. Exit")
	
	choice = input("Enter your choice(1-4):")
	if choice == "1":
		ID = input("Enter your ID Number:")
		time_in = datetime.datetime.now().strftime("%I:%M %p")
		record[ID] = [time_in, "Not yet logged out"]
		print(f"Employee {ID} timed in at {time_in}.")
	elif choice == "2":
		ID = input("Enter your ID Number:")
		
		if ID in record:
			if record [ID] [1] != "Not yet logged out":
				print("You've already timed out")
			else:
				time_out = datetime.datetime.now().strftime("%I:%M %p")
				record [ID] [1] = time_out
				print(f"Employee {ID} timed out at {time_out}.")
		else:
				print("Employee ID not found. Please time-in first.")
	elif choice == "3":
		print("\n Attendance Logs")
		if not record:
			print("No attendance records yet")
		else:
		    for emp_id, times in record.items():
		    	print(f"ID: {emp_id} | Time-In: {times[0]} | Time-Out: {times[1]}")
	elif choice == "4":
		print("Thank you for using our system. Byeebyeee!")
		break
	else:
		print("Please select 1-4 only.")