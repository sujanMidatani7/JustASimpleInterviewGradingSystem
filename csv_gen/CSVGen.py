import csv
import random
import string

def create_csv_file(question, answer, rubrics_list, plagiarism_score):
    # Define the field names for the CSV file
    fields = ['question', 'answer', 'rubrics_list', 'plagiarism_score']
    
    # Create a list of rows containing the provided data
    rows = [(question, answer, rubrics_list, plagiarism_score)]
    
    # Generate a random filename based on the question
    filename = ''.join(question) + ".csv"
    
    # Open the CSV file in write mode and write the data
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
       
        csvwriter.writerow(fields)
        csvwriter.writerows(rows)
    
    return filename
