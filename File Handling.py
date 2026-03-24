# FILE HANDLING MEANS CRUD OPERATIONS ON FILES
# CREATING, READING, UPDATING, DELETING

r = open("Superman.txt", "w")       # w means write mode, it will create a new file if it doesn't exist
r.write("Superman is the best superhero in the world.")
r.close()       # closing the file after writing

r = open("Superman.txt", "a")       # a means append mode, it will add new content to the existing file without overwriting it
r.write("adding new content with a = append")
r.close()       
