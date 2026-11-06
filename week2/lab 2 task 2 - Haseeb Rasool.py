def read_gmt_time():
	#get function to read and validate a time in 24-hour HH:MM format
	"""Read and validate a time in 24-hour HH:MM format."""
	while True:
		#while loop to keep prompting the user until a valid time is entered
		try:
			time_text = input("Enter GMT time (HH:MM): ")
			#split the input into hours and minutes
			hours_text, minutes_text = time_text.split(":")
			#convert the hours and minutes to integers
			hours, minutes = int(hours_text), int(minutes_text)
			#check if the hours and minutes are within valid ranges
			if 0 <= hours < 24 and 0 <= minutes < 60:
				#return the total minutes after midnight
				return hours * 60 + minutes
			#if the input is invalid, raise a ValueError
		except ValueError:
			#except block to catch the ValueError and print an error message
			pass
		#print an error message if the input is invalid
		print("Invalid time. Enter a valid time such as 14:30.")


def format_time(minutes_after_midnight):
	#get function to format a minute count as a wrapped 24-hour time string
	"""Return a minute count as a wrapped 24-hour time string."""
	#wrap the minutes around at midnight to ensure it stays within a 24-hour range
	minutes_after_midnight %= 24 * 60  
	#convert the total minutes back to hours and minutes
	hours, minutes = divmod(minutes_after_midnight, 60)
	#return the formatted time string in HH:MM format
	return f"{hours:02d}:{minutes:02d}"


def main():
	# Convert GMT minutes to each time zone using its GMT offset.
	gmt_minutes = read_gmt_time()
	pst_minutes = gmt_minutes - 8 * 60  # PST is GMT - 8 hours.
	cet_minutes = gmt_minutes + 60  # CET is GMT + 1 hour.

	# Print the converted times in 24-hour format.
	print(f"PST: {format_time(pst_minutes)}")
	print(f"CET: {format_time(cet_minutes)}")


if __name__ == "__main__":
	# Call the main function to execute the program
	main()
