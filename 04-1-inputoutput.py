# read and write text files

# write file

with open("notes.txt", "w") as file:
    file.write("Hello, world\n")
    file.write("This is live 2.\n")

# read file
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)


# "r"  → read   — baca file, error kalau file tidak ada
# "w"  → write  — tulis file, hapus isi lama kalau sudah ada
# "a"  → append — tambah di belakang, tidak hapus isi lama
# "x"  → create — buat file baru, error kalau sudah ada

