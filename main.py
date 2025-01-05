from ChainingHashTable import ChainingHashTable

movie_table = ChainingHashTable()

movie_table.insert(1, "Dune")
movie_table.insert(2, "Dune 2")
movie_table.insert(3, "Gladiator 2")

print(movie_table.table)
print("")

print(movie_table.search(2))

movie_table.remove('2')
print(movie_table.search(2))