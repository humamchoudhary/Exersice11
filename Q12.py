my_note = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

print('Cord types are : Minor, Augmented fifth, Minor fifth, Major sixth, Minor sixth\n \t\tDominant seventh, Minor seventh, Major seventh, Diminished seventh')
key = input('Enter Key: ')
cord_type = input('Enter Cord Type: ')

i = 0
while i < 12:
    if my_note[i] == key:
        break
    i = i+1

if cord_type == 'Minor':
    print(my_note[i], my_note[i+3], my_note[(i+7) % 11])
elif cord_type == 'Augmented fifth':
    print(my_note[i], my_note[i+4], my_note[(i+8) % 11])
elif cord_type == 'Minor fifth':
    print(my_note[i], my_note[i+4], my_note[(i+6) % 11])
elif cord_type == 'Major sixth':
    print(my_note[i], my_note[i+4], my_note[(i+7) % 11], my_note[(i+9) % 11])
elif cord_type == 'Dominant seventh':
    print(my_note[i], my_note[i+4], my_note[(i+7) % 11], my_note[(i+10) % 11])
elif cord_type == 'Minor seventh':
    print(my_note[i], my_note[i+3], my_note[(i+7) % 11], my_note[(i+10) % 11])
elif cord_type == 'Major seventh':
    print(my_note[i], my_note[i+4], my_note[(i+7) % 11], my_note[(i+11) % 11])
elif cord_type == 'Diminished seventh':
    print(my_note[i], my_note[i+3], my_note[(i+6) % 11], my_note[(i+10) % 11])
elif cord_type == 'Minor sixth':
    print(my_note[i], my_note[i+3], my_note[(i+7) % 11], my_note[(i+9) % 11])
