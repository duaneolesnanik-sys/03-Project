movie = input("Enter a movie title: ").strip()
boring = input("Enter a boring word from the title: ").strip()
fun = input("Enter a funny replacement word: ").strip()

print("Your new movie title is:\n\n",movie.replace(boring, fun))