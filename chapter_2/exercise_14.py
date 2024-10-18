#exercise 2.14 (Target Heart-Rate Calculate)
age = int(input("Enter your age: "))
max_heartrate = 220 - age #heartrate is measured in bpm (beats per minutes)
min_target_bpm = (50 / 100) * max_heartrate
max_target_bpm = (85 / 100) * max_heartrate

print("Your maximum heartrate is: ", max_heartrate,"bpm")
print("Recommended target is between: (", min_target_bpm, " to ", max_target_bpm,")bpm")
