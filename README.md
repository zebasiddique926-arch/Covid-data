# COVID-19 Data Viewer

A Python-based GUI application for viewing COVID-19 statistics across Indian states, including cases, deaths, discharges, and vaccination data.

## Team Members
- *Mubashira*
- *Vishal*
- *Sharad*

## Overview

This project provides an interactive graphical interface to explore COVID-19 data for different states in India. Users can search for any state and view key statistics including active cases, total deaths, total cases, and discharged patients.

## Features

- *User-Friendly GUI*: Built with Tkinter for easy interaction
- *State-wise Data*: Search and view COVID-19 statistics for any Indian state
- *Multiple Metrics*: Access data on:
  - Active cases
  - Total deaths
  - Total confirmed cases
  - Discharged/recovered patients
- *Data Cleaning*: Automated data preprocessing and standardization
- *Merged Datasets*: Combines COVID-19 case data with vaccination statistics

## Project Structure


â”œâ”€â”€ main.py          # Core data processing and cleaning functions
â”œâ”€â”€ data_load.py     # CSV data loading module
â”œâ”€â”€ gui.py           # Tkinter-based graphical user interface
â”œâ”€â”€ dataset_1.csv    # Vaccination data
â””â”€â”€ dataset_2.csv    # COVID-19 cases data


## Requirements

- Python 3.x
- pandas
- tkinter (usually comes with Python)

## Installation

1. Clone or download this repository
2. Install required dependencies:
   bash
   pip install pandas
   
3. Ensure dataset_1.csv and dataset_2.csv are in the project directory

## Usage

Run the application using:
bash
python gui.py


### How to Use:
1. Enter the name of an Indian state in the text field
2. Select one of the four options:
   - Active Cases
   - Deaths
   - Total Cases
   - Discharged
3. Click "Show Result" to view the data

## File Descriptions

### main.py
Contains the core data processing functions:
- clean_dataframe_cases(): Cleans and standardizes COVID case data
- clean_dataframe_vaccine(): Cleans and standardizes vaccination data
- get_clean_data(): Loads, cleans, and merges both datasets

### data_load.py
Handles CSV file loading with error handling. Loads two separate datasets for vaccination and case statistics.

### gui.py
Implements the graphical user interface using Tkinter. Features include input validation, state search functionality, and formatted result display.

## Data Sources

The project uses two CSV datasets:
- *dataset_1.csv*: State-wise vaccination data (total vaccinated, dose1, dose2, precaution doses, population)
- *dataset_2.csv*: State-wise COVID-19 case statistics (total cases, active, discharged, deaths)

## License

This project is created for educational purposes.

## Acknowledgments

Developed as part of a data science/programming coursework to demonstrate data processing, GUI development, and COVID-19 data visualization skills.
