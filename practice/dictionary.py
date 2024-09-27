# student information
student = {"name":"Alice", "age":18, "grade":"12th", "subjects":["Math", "English", "Science"]}
print(f"student name: {student["name"]}")
print(f'student age: {student["age"]}')
print(f"student grade: {student["grade"]}")
print(f"student subjects: {student["subjects"]}")

# tracking movie rating:

movies = {}

while True:
    movie_name = input("Enter movie name (or 'quit' to exit): ")
    if movie_name.lower() == 'quit':
        break

    rating = int(input("Enter rating (1-5): "))
    if movie_name in movies:
        movies[movie_name].append(rating)
    else:
        movies[movie_name] = [rating]

for movie, ratings in movies.items():
    average_rating = sum(ratings) / len(ratings)
    print(f"{movie}: Average Rating = {average_rating:.2f}")
