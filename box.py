import tkinter as tk
import time

def to_string(data):
	data_str = ""
	for d in data:
		data_str = data_str + str(d) + " "
	return data_str

def mergeSort(data, label):
    print("Splitting ",data)
    if len(data)>1:
        mid = len(data)//2
        lefthalf = data[:mid]
        righthalf = data[mid:]

        mergeSort(lefthalf,label)
        mergeSort(righthalf,label)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                data[k]=lefthalf[i]
                i=i+1
            else:
                data[k]=righthalf[j]
                j=j+1
            k=k+1


        while i < len(lefthalf):
            data[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            data[k]=righthalf[j]
            j=j+1
            k=k+1

    print("Merging ",data)
    root.update()
    label.config(text=to_string(data))
    label.pack()
    time.sleep(1.2)


data = [23, 56, 78, 12, 14, 21, 57, 4, 18]
root = tk.Tk()
root.title("Sorting")
label = tk.Label(root, fg="dark green")
label.pack()
label.config(text=to_string(data))
sort_button = tk.Button(root, text='Sort', width=75,height=2,
	command=lambda:mergeSort(data,label))

exit_button = tk.Button(root, text='Exit', width=75,height=2, command=root.destroy)
sort_button.pack()
exit_button.pack()

root.mainloop()
