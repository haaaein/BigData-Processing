#!/usr/bin/pyton3

from openpyxl import load_workbook

wb = load_workbook( filename = "student.xlsx")
sheet_ranges = wb["Sheet1"]

row_num=2
num_of_students=1

while True:
	col_midterm = sheet_ranges.cell( row = row_num, column = 3).value
	col_final = sheet_ranges.cell( row = row_num, column = 4).value
	col_homework = sheet_ranges.cell( row = row_num, column = 5).value
	col_attendance = sheet_ranges.cell(row = row_num, column = 6).value
	if col_midterm == None:
		break
	col_total = col_midterm * 0.3 + col_final * 0.35 + col_homework * 0.34 + col_attendance 
	sheet_ranges.cell(row = row_num, column = 7, value = col_total)

	row_num += 1
	num_of_students += 1

row_num = 2
while True:
	

wb.save( filename = "output.xlsx" )

