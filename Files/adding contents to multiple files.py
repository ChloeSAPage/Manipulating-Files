contents = ["All carrots are orange", "All Limes are green", "All lemons are yellow"]

filenames = ["carrots.txt", "limes.txt", "lemons.txt"]

for contents, filenames in zip(contents, filenames):
    file = open(filenames, "w")
    file.write(contents)