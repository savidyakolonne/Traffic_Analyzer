#Author: Savidya Kolonne
#Date: 23/12/2024 (last update)
#Student ID: w2119725

from graphics import *

# Task A: Input Validation 
def validate_date_input():
    """
    Validates and formats the date input from the user in DD/MM/YYYY format.
    Returns the file name based on the entered date.
    """
    while True:
        try:
            day = int(input("Please enter the day of the survey in the format dd: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if 1 <= day <= 31:
                if day < 10:
                    day = '0' + str(day)
                break
            else:
                print("Out of range - values must be in the range 1 and 31.")

    while True:
        try:
            month = int(input("Please enter the month of the survey in the format MM: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if 1 <= month <= 12:
                if month < 10:
                    month = '0' + str(month)
                break
            else:
                print("Out of range - values must be in the range 1 to 12.")

    while True:
        try:
            year = int(input("Please enter the year of the survey in the format YYYY: "))
        except ValueError:
            print("Integer required")
            continue
        else:
            if 2000 <= year <= 2024:
                year = str(year)
                break
            else:
                print("Out of range - values must range from 2000 and 2024.")

    return f"traffic_data{day}{month}{year}.csv"

def process_hourly_data(datafile1):
    """
    Process traffic data from the specified file for hourly counts.
    Returns a dictionary with counts for Elm Avenue and Hanley Highway.
    """
    try:
        with open(datafile1, "r") as file:
            file.readline()  # Skip the header line

            elm_counts = [0] * 24
            hanley_counts = [0] * 24

            while True:
                line = file.readline().strip()
                if not line:
                    break

                data = line.split(",")

                if len(data) < 3:
                    continue

                # Extract time and location
                location = data[0]
                time = data[2]

                hour = int(time.split(":")[0])

                if location == "Elm Avenue/Rabbit Road":
                    elm_counts[hour] += 1
                elif location == "Hanley Highway/Westway":
                    hanley_counts[hour] += 1

        return {"green": elm_counts, "red": hanley_counts}

    except FileNotFoundError:
        print("Error: File not found. Please check the file name and try again.")
        return {"green": [], "red": []}
    
def validate_continue_input():
    """
    prompt the user to continue with a new data set or quit from the programme.
    returns True to continue or False to exit
    """
    while True :
        continue_input = input("Validate 'Y' to load new dataset or 'N' to quit: ").upper()
        if continue_input == "Y" :
            return True
        elif continue_input == "N" :
            return False
        else :
            print("Invalid input! Please enter 'Y' or 'N'.")


# Task B: Process CSV Data (Your existing code)
def process_csv_data(file_path):
    """
    Process traffic data from the specified CSV file.
    Returns a list of outcomes or an error message if the file is not found.
    """
    try:
        with open(file_path, "r") as file:
            file.readline()  # skip the header line
            outcomes = []
            total_vehicle = 0
            Truck = 0
            Electric_vehicles = 0
            two_wheeled = 0
            Buss_leave = 0
            no_turn_vehicles = 0
            Bikes = 0
            over_speed = 0
            elm_avenue_vehi = 0
            hanley_vehi = 0
            elm_Scooters = 0
            list1 = [0] * 24  # tracks vehicle per hour
            rain_hours = 0
            rain_times = []

            while True:
                data1 = file.readline().strip().split(",")
                if data1[0] != '': 
                    total_vehicle += 1 #increment total vehicle count

                    #count Trucks
                    if data1[8] == "Truck":
                        Truck += 1
                    
                    #count electric vehicles
                    if data1[9] == "True" :
                        Electric_vehicles += 1

                    #count two wheeled vehicles
                    if data1[8] == "Motorcycle" or data1[8] == "Scooter" or data1[8] == "Bicycle" :
                        two_wheeled += 1

                    #count busses leaving from Elm Avenue/Rabbit Road heading north
                    if data1[4] == "N" and data1[8] == "Buss" and data1[0] == "Elm Avenue/Rabbit Road" :
                        Buss_leave += 1

                    #count vehicles not turning left or right
                    if data1[3] == data1[4] :
                        no_turn_vehicles += 1

                    #calculate precentage of Trucks
                    truck_precentage = round((Truck / total_vehicle) * 100)
                    
                    #count bicycles and calculate their hourly average
                    if data1[8] == "Bicycle" :
                        Bikes += 1
                        bike_avg = Bikes / 24
                        bike_avg_round = round(bike_avg)
                    
                    #count vehicles over speeding
                    if int(data1[6]) < int(data1[7])  :
                        over_speed += 1
                    
                    #count vehicles at Elm Avenue/Rabbit Road
                    if data1[0] == "Elm Avenue/Rabbit Road" :
                        elm_avenue_vehi += 1
                    
                    #count vehicles at Hanley Highway/Westway
                    if data1[0] == "Hanley Highway/Westway" :
                        hanley_vehi += 1

                    #calculate precentage of sccoters at Elm Avenue/Rabbit Road
                    if data1[8] == "Scooter" and data1[0] == "Elm Avenue/Rabbit Road":
                        elm_Scooters += 1
                    precent_scooter_elm = int((elm_Scooters / elm_avenue_vehi ) * 100)
                        
                    #calculate highest number of vehicles in an hour at Hanley Highway/Westway 
                    if data1[0] == "Hanley Highway/Westway":
                        get_time = data1[2].split(':')                        
                        for i in range(24):
                            if int(get_time[0]) == i :
                                list1[i] += 1
                    hanley_highest_vehi_perhr = max(list1)
                    for i in range(len(list1)):
                        if list1[i] == hanley_highest_vehi_perhr :
                            outcomes01 = (i)
                            outcomes02 = (i+1)
                    
                    #calculate the rain time
                    if data1[5] == "Light Rain" or data1[5] == "Heavy Rain" :
                         get_time = data1[2].split(':')
                         timeInSeconds = (int(get_time[0])*3600)+(int(get_time[1])*60)+ (int(get_time[2]))
                         rain_times.append(timeInSeconds)
                    rain_times.sort()
                    for i in range(1,len(rain_times)):
                        difference = rain_times[i] - rain_times[i-1]
                        rain_hours += difference
                    rain_hours = int(rain_hours/3600)
                    outcomes03  = rain_hours

                else : 
                    break
  
            # Prepare outcomes
            outcomes = [
                f"The total number of vehicles recorded for this date is {total_vehicle}",
                f"The total number of trucks recorded for this date is {Truck}",
                f"The total number of electric vehicles for this date is {Electric_vehicles}",
                f"The total number of two-wheeled recorded for this date is {two_wheeled}",
                f"The total number of Busses leaving Elm Avenue/Rabbit Road heading North is {Buss_leave}",
                f"The total number of Vehicles through both junctions not turning left or right is {no_turn_vehicles}",
                f"The percentage of total vehicles recorded that are trucks for this date is {truck_precentage}%",
                f"The average number of Bikes per hour for this date is {bike_avg_round}",
                f"The total number of Vehicles recorded as over the speed limit for this date is {over_speed}",
                f"The total number of Vehicles recorded through Elm Avenue/Rabbit Road junction is {elm_avenue_vehi}",
                f"The total number of Vehicles recorded through Hanley Highway/Westway junction is {hanley_vehi}",
                f"{precent_scooter_elm}% of vehicles recorded through Elm Avenue/Rabbit Road are scooters.",
                f"The highest number of vehicles in an hour on Hanley Highway/Westway is {hanley_highest_vehi_perhr}",
                f"The most vehicles through Hanley Highway/Westway were recorded between {outcomes01}:00 and {outcomes02}:00",
                f"The number of hours of rain for this date is {rain_hours}\n"
                "\n*********************************************\n"
            ]

    except FileNotFoundError:
        return ["Error!!! Please enter the CORRECT file."]

    return outcomes

def display_outcomes(outcomes):
    """
    Display the list of outcomes
    """
    for outcome in outcomes:
        print(outcome)

# Task C: Save Results to Text File
def save_results_to_file(outcomes,datafile1, file_name="results.txt"):
    """
    Save the list of outcomes to a text file
    """
    with open(file_name, "a") as file:
        file.write(f"data file selected is {datafile1}\n")
        for outcome in outcomes:
            file.write(outcome + "\n")
    print(f"Results saved to {file_name}")

# Task D: Histogram Display
class HistogramApp:
    def __init__(self, traffic_data, date):
        """
        Initializes the histogram application with the traffic data and selected date.
        """
        self.traffic_data = traffic_data
        self.date = ("("+date[12:14]+'/'+date[14:16]+'/'+date[16:20]+")")
        self.canvas = None

    def setup_window(self):
        """
        Sets up the Tkinter window and canvas for the histogram.
        """
        self.canvas = GraphWin("Histogram", 1200, 600)
        self.canvas.setBackground("lightgray")


    def add_legend(self):
        """
        Adds a legend to the histogram.
        """
        legend1 = Rectangle(Point(85, 60), Point(105, 80))
        legend1.setFill("green")
        legend1.draw(self.canvas)
        legend1_label = Text(Point(205, 70), "Elm Avenue/Rabbit Road")
        legend1_label.setSize(12)
        legend1_label.setStyle("bold")
        legend1_label.draw(self.canvas)

        legend2 = Rectangle(Point(85, 90), Point(105, 110))
        legend2.setFill("red")
        legend2.draw(self.canvas)
        legend2_label = Text(Point(208, 100), "Hanley Highway/Westway")
        legend2_label.setSize(12)
        legend2_label.setStyle("bold")
        legend2_label.draw(self.canvas)

    def draw_histogram(self):
        """
        Draws the histogram bars based on the traffic data.
        """
        title = Text(Point(402, 40), f"Histogram of Vehicle Frequency per Hour {self.date}")
        title.setSize(19)
        title.setStyle("bold")
        title.draw(self.canvas)

        x_axis = Line(Point(110, 535), Point(1060, 535))
        x_axis.setWidth(2)
        x_axis.draw(self.canvas)

        # Draw x-axis labels (hours 00 to 24)
        x_labels = [
            ("00", 125), ("01", 165), ("02", 205), ("03", 245), ("04", 285),
            ("05", 325), ("06", 365), ("07", 405), ("08", 445), ("09", 485),
            ("10", 525), ("11", 565), ("12", 605), ("13", 645), ("14", 685),
            ("15", 725), ("16", 765), ("17", 805), ("18", 845), ("19", 885),
            ("20", 925), ("21", 965), ("22", 1005), ("23", 1045)]
        
        for label, position in x_labels:
            text = Text(Point(position, 545), label)
            text.setSize(10)
            text.draw(self.canvas)

        # Add a description below the x-axis
        x_label_text = Text(Point(600, 570), "Hours 00:00 to 24:00")
        x_label_text.setStyle("bold")
        x_label_text.setSize(12)
        x_label_text.draw(self.canvas)

        green_data = self.traffic_data.get("green", [])
        red_data = self.traffic_data.get("red", [])

        for i in range(24):
            # Green bars
            green_bar = Rectangle(
                Point(110 + i * 40, 535 - green_data[i] * 6),
                Point(125 + i * 40, 535)
            )
            green_bar.setFill("green")
            green_bar.draw(self.canvas)

            # Red bars
            red_bar = Rectangle(
                Point(125 + i * 40, 535 - red_data[i] * 6),
                Point(140 + i * 40, 535)
            )
            red_bar.setFill("red")
            red_bar.draw(self.canvas)

            # Add frequency labels
            green_label = Text(Point(117 + i * 40, 528 - green_data[i] * 6), str(green_data[i]))
            green_label.setSize(8)
            green_label.draw(self.canvas)

            red_label = Text(Point(132 + i * 40, 528 - red_data[i] * 6), str(red_data[i]))
            red_label.setSize(8)
            red_label.draw(self.canvas)

    def run(self):
        """
        Runs the application to display the histogram.
        """
        self.setup_window()
        self.add_legend()
        self.draw_histogram()

        self.canvas.getMouse()
        self.canvas.close()

# Task E: Validate Continue Input (Your existing code)
class MultiCSVProcessor:
    def __init__(self):
        """
        Initializes the application for processing multiple CSV files.
        """
        self.current_data = None

    def load_csv_file(self, datafile1):
        """
        Loads a CSV file and processes its data.
        """
        hourly_data = process_hourly_data(datafile1)
        if not hourly_data["green"] and not hourly_data["red"]:
            print("Processing failed. Please try again with a valid file.")
            return None
        return hourly_data
    
    def clear_previous_data(self):
        
        self.current_data = None

    def handle_user_interaction(self):
        """
        Handles user input for processing multiple files.
        """
        while True:
            
            datafile1 = validate_date_input()
            
            if not datafile1:
                print("Error: File name could not be generated. Please try again.")
                continue
        
            outcomes = process_csv_data(datafile1) #process data from the file

            if outcomes[0] == "Error!!! Please enter the CORRECT file.": #handle : display this when input a incorrect file
                print(outcomes[0])
                continue
            
            else:
                display_outcomes(outcomes)  #display processed results
                save_results_to_file(outcomes, datafile1) #save result to a txt file
 
            hourly_data = self.load_csv_file(datafile1)

            if hourly_data:
                app = HistogramApp(hourly_data, datafile1)
                app.run()

            if not validate_continue_input(): #ask user for continue or exit the programme
                break

if __name__ == "__main__":
    # Run the multi-CSV processor to handle multiple file processing
    processor = MultiCSVProcessor()
    processor.handle_user_interaction()