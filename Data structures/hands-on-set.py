{'Ablum01', "Album02", "Album03"} #{} bracket with value is a SET, set doesn't allow duplicates and no ordering
playlist = {"Jonny B", "Mikey B", "Jon A"}
artists = {"James I", "Steve W", "Tyrese", "Mikey B"}

# print(dir(set()))
# print(playlist)
# playlist.add("Jonny C") 
# #playlist[1] = "Mikey C"
# print(playlist)
# print(playlist.pop())
# print(playlist)
# # print(type(playlist))
# # print(type(artists))
# # print(type({})) #Dictionary declaration

print(playlist.union(artists))
print(playlist.intersection(artists))

