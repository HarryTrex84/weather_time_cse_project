
# 🌤️ Simple Python Weather Checker

A brief description of what this project does and who it's for


## 📜 Overview of the Project

This project is a simple Command-Line Interface (CLI) weather application written in Python. It allows users to quickly retrieve the current weather report for any specified city, displaying the temperature, condition, and local time.

The application uses an external weather service (via an API) to fetch real-time data and includes error handling for common issues like network errors or invalid city names.

## ✨ Features
Real-time Weather Data: Fetches up-to-date weather information (temperature, condition).

Local Time Display: Shows the local date and time for the queried city.

Simple CLI Interface: Easy-to-use command-line input for city names.

Robust Error Handling: Catches and manages exceptions for:

Network connection issues.

Invalid city names/data not found.

Missing required libraries (requests).
## 🛠️ Technologies/Tools Used
Language: Python 3.x

Core Library: requests (for making HTTP requests to the weather API)

Development Environment: Visual Studio Code

Weather Data Source: An external API (implied by the URL structure: http://wtr.in/io/?city={city_name}).
## ⚙️ Steps to Install & Run the Project
1. Prerequisites
Ensure you have Python 3.x installed on your system.

2. Install Dependencies
This project relies on the requests library. Open your terminal or command prompt and run the following command to install it:

 ->Bash

 ->pip install requests

3. Save the Code
Save the provided code into a single file named weather_time_project.py.

4. Run the Application
Execute the Python script from your terminal:

 ->Bash

 ->python weather_time_project.py
## ☀️ Friendly Weather App Design
1. The Weather Checker Function: get_weather(city_name)
Think of this as the smart robot that goes out to get the information.

It Asks: The robot first figures out the exact web address it needs, using the city name you gave it.

It Fetches: It quickly zaps a message to the weather website (wttr.in) to grab the data.

It Reads: The robot takes the messy data it gets back and sorts it out. It pulls out just the things we care about: the temperature, what the weather looks like (sunny, cloudy), the city/country, and the local time.

It Tells You: It prints all those clear details right on your screen.

It Doesn't Panic: If the web is down, or you typed a city name that doesn't exist (like "Unicornville"), the robot won't break. It just prints a nice, clear error message instead.

2. The Main Program (The "Chat")
This is the part that talks to you and keeps things running.

Greeting: When you start the app, it says "Hello!"

Asking: It keeps asking you, "What city should I check?"

Stopping: If you type "quit", the app stops immediately.

Checking: If you type a city name, it hands that name off to the Weather Checker Function (above) to get the details.

Oops! If you just hit Enter without typing anything, it reminds you to actually type a city name and asks again.

3. What You See (Inputs & Outputs)
Your Job (Input): You type a city name (e.g., "Tokyo").

App's Job (Output): It shows you a neat, easy-to-read list of the weather details (temp, condition, place, time) OR it shows you a simple error message if something went wrong.
## 🧪 Instructions for Testing
Start the application as described above. You will see the prompt: Enter the city name (or 'quit' to exit):

1) Test successful lookup:

Enter a valid city name, like BHOPAL or MUMBAI.

The application should display the weather report, including Local Time, Temperature, and Condition.

2) Test city not found (Error Handling):

Enter a non-existent or misspelled city name (e.g., Zzzzzz).

The application should output the error: Error: weather data not found for 'Zzzzzz'. Check the spelling.

3) Test exit functionality:

Type quit and press Enter.

The application should print: Exiting weather checker. Goodbye! and close.

4) Test exit functionality:

Type quit and press Enter.

The application should print: Exiting weather checker. Goodbye! and close.