#boarProject v2.0
#------Standard Chance is Calculated as Such:-----
	#(skillName)*(skillLevel)*(totalLevel)
	#To change the dificulty we just tru to get anything that is greater than that number out of 'x' arbitrary number

#-----Imports:----
import random
import time

#-----Itmes:-----
items={
	"2) Rawhide Armor": "Rough form of protection, stitched together.(+5 protection)",
	"1) Leather Satchel": "An old, raggedy sack that carries the few things you have.",
	"3) Quiver": "An old quiver you father used, there is a family seal on it's front."
}

#-----Random Temporary Variables:-----

#-----Mob Info:-----
boar1Dead=False

#-----Character Info:-----
name=""
alive=True
inventory={""}

for key, value in sorted(items.items()):
		print(key," = ", value)
