#Sebastian SantaCruz
#CIS261
#MovieGuide2

with open("Movies.txt","w") as file:
  file.write("Cat on a Hot Tin Roof\nOn the Waterfront\nMonry Python and the Holy Grail\n")
def display_option():
   print("COMMAND MENU\n")
   print ("list - List all movies")
   print ("add - Add a movie")
   print ("del - Delete a movie")
   print ("exit - Exit program\n") 
def populate_list(file_name):
  movie_list = []
  with open(file_name,"r") as file:
    for line in file:
      movie_list.append(line.strip())
  return movie_list
def list_movies(movie_list):
    print("\nMovie Titles")
    print()
    for i, title in enumerate(movie_list, start=1):
        print(f"{i}. {title}")
        print ()
def add(movie_list, title, file_name):
    movie_list.append(title)  
    with open(file_name, "a") as file:
      file.write(title + "\n")
    print(title + " was added.") 
def delete(movie_list, index, file_name):
  if 1 <= index <= len(movie_list):
    deleted_title = movie_list.pop(index - 1)
    with open(file_name,"w") as file:
      file.write("\n".join(movie_list))
      print( deleted_title + " was deleted successfully!")
  else:
    print("Invalid index number. No movie was deleted") 
def main():
    movie_file = "Movies.txt"
    movie_list = populate_list(movie_file)
    while True:
        display_option()
        choice = input("Enter your choice: ").lower()
        if choice == "list":
            list_movies(movie_list)
        elif choice == "add":
            new_title = input("Enter the new movie title:")
            add(movie_list, new_title, movie_file)
            list_movies(movie_list)
        elif choice == "del":
            list_movies(movie_list)
            index =int(input("Enter the number of the movie title you would like to delete:"))
            delete(movie_list, index, movie_file)
            list_movies(movie_list)
        elif choice == "exit":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Not a valid command. Please try again")
if __name__ == "__main__":
 main()