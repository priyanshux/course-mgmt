import sqlite3 as lite


#functionality goes here

class DatabaseManage(object):

	def __init__(self):
		global con
		try:
			con = lite.connect('courses.db')
			with con:
				cur = con.cursor()
				cur.execute("CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
			except Exception(exc):
				print("Unable to create a DB!")

#TODO: create data
def insert_data(self, data):
	try:
		with con:
			cur = con.cursor()
			cur.execute(
				"INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)", data
				)
	except Exception:
		return False

#TODO: read data
def fetch_data(self):
	try:
		with con:
			cur = con.cursor()
			cur.execute("SELECT * FROM course")
			return cur.fetchall()
	except Exception:
		return False

#TODO: delete data
def delete_data(self, id):
	try:
		with con:
			cur = con.cursor()
			sql = "DELETE FROM course WHERE id = ?"
			cur.execute(sql, [id])

	except Exception:
		return False

#TODO: provide interface to user

def main():
	print("*"*40)
	print("\n:: COURSE MANAGEMENT :: \n")
	print("*"*40)
	print("\n")

	db = DatabaseManage()

	print("#"*40)
	print("\n :: User Manual :: \n")
	print("#"*40)

	print("\nPress 1. Insert a new course")
	print("\npress 2. Show all courses")
	print("\nPress 3. Delete a course (NEED ID)\n")
	print("#"*40)
	print("\n")

	choice = input("\nEnter a choice: ")

	if choice == "1":
		name = input("\nEnter course name: ")
		description = input("\nEnter course description: ")
		price = input("\nEnter course price: ")
		private = input("\nIs this course private (0/1): ")


		if db.insert_data([name, description, price, private]):
			print("Course was inserted successfully")
		else:
			print("Error!")

	elif choice == "2":
		print("\n:: Course List ::\n")

		
	
		


