from guizero import App
from guizero import Text
from guizero import TextBox
from guizero import PushButton

notes = [
    ["E|"],
    ["A|"],
    ["D|"],
    ["G|"],
]
print("initialised")
print("notes: ", notes)

def main():

    def e_string_proc():
        e_string_note = e_string_box.value
        notes[0][0] += e_string_note + "-"
        notes[1][0] += (len(e_string_note) * "-") + "-"
        notes[2][0] += (len(e_string_note) * "-") + "-"
        notes[3][0] += (len(e_string_note) * "-") + "-"
        print(notes[0])
        print(notes[1])
        print(notes[2])
        print(notes[3])
        print("\n")
    
    def a_string_proc():
        a_string_note = a_string_box.value
        notes[0][0] += (len(a_string_note) * "-") + "-"
        notes[1][0] += a_string_note + "-"
        notes[2][0] += (len(a_string_note) * "-") + "-"
        notes[3][0] += (len(a_string_note) * "-") + "-"
        print(notes[0])
        print(notes[1])
        print(notes[2])
        print(notes[3])
        print("\n")

    def d_string_proc():
        d_string_note = d_string_box.value
        notes[0][0] += (len(d_string_note) * "-") + "-"
        notes[1][0] += (len(d_string_note) * "-") + "-"
        notes[2][0] += d_string_note + "-"
        notes[3][0] += (len(d_string_note) * "-") + "-"
        print(notes[0])
        print(notes[1])
        print(notes[2])
        print(notes[3])
        print("\n")
    
    def g_string_proc():
        g_string_note = g_string_box.value
        notes[0][0] += (len(g_string_note) * "-") + "-"
        notes[1][0] += (len(g_string_note) * "-") + "-"
        notes[2][0] += (len(g_string_note) * "-") + "-"
        notes[3][0] += g_string_note + "-"
        print(notes[0])
        print(notes[1])
        print(notes[2])
        print(notes[3])
        print("\n")

    def rest_proc():
        for i in range(len(notes)):
            notes[i][0] += "--"
        for i in range(len(notes)):
            print(notes[i])
        print("\n")

    def break_proc():
        for i in range(len(notes)):
            notes[i][0] += "|"
        print(notes[0])
        print(notes[1])
        print(notes[2])
        print(notes[3])
        print("\n")

    def delete_proc():
        if notes[0][0] == "E|" or notes[1][0] == "A|" or notes[2][0] == "D|" or notes[3][0] == "G|":
            pass
        else:
            for i in range(len(notes)):
                notes[i][0] = notes[i][0][:-1]
            for i in range(len(notes)):
                print(notes[i])
            print("\n")

    def save_proc():
        if notes[0][0][-1] != "|":
            for i in range(len(notes)):
                notes[i][0] += "|"
        with open("tab.txt", "a") as f:
            for i in range(len(notes)):
                f.write(f"{str(* notes[i])}\n")
            f.write("\n")

    # App is a class, title is an attribute that gives a name to the window
    app = App(title="bass tabs", width=1280, height=720, layout="grid")

    # app.display() # display() is a method you can call on App objects

    app.bg = "#FFFFFF"

    # Text objects embed into app object of App class
    # the grid system places elements on coordinates, starting from 0, 0 at the top left
    title = Text(app, text="bass tab creator", color="#000000", grid=[0, 0])
    title.size = 30

    note_heading = Text(app, text="Note number", color="#000000", grid=[1, 2])
    note_heading.size = 20

    # instantiate a button object from PushButton class that binds to app
    # calls a proc when clicked
    # button = PushButton(app, command=on_click, text="click me", pady=10, padx=10)

    e_string_button = PushButton(app, command=e_string_proc, text="E string", grid=[0, 3], pady=10, padx=10)
    a_string_button = PushButton(app, command=a_string_proc, text="A string", grid=[0, 4], pady=10, padx=10)
    d_string_button = PushButton(app, command=d_string_proc, text="D string", grid=[0, 5], pady=10, padx=10)
    g_string_button = PushButton(app, command=g_string_proc, text="G string", grid=[0, 6], pady=10, padx=10)
    rest_button = PushButton(app, command=rest_proc, text="rest", grid=[0, 7], padx=10, pady=10)
    break_button = PushButton(app, command=break_proc, text="break", grid=[0, 8], padx=10, pady=10)
    delete_button = PushButton(app, command=delete_proc, text="delete last note", grid=[0, 9], padx=10, pady=10)
    save_button = PushButton(app, command=save_proc, text="save tab", grid=[0, 10], pady=10, padx=10)

    e_string_box = TextBox(app, text="0", grid=[1, 3]) # E
    e_string_box.text_color = "#000000"
    a_string_box = TextBox(app, text="0", grid=[1, 4]) # A
    a_string_box.text_color = "#000000"
    d_string_box = TextBox(app, text="0", grid=[1, 5]) # D
    d_string_box.text_color = "#000000"
    g_string_box = TextBox(app, text="0", grid=[1, 6]) # G
    g_string_box.text_color = "#000000"

    # the text needs to be black because otherwise it's white by default (and on a white bg)
    # cannot do something like:
    # `test_box = TextBox(app, text="hello", grid=[0, 0]).text_color="black`
    # calling .value on `test_box` like this will return an error
    # because python will think it has no attribute "value"
    # you have to change the text color after the fact to avoid calling a func call on a text box's val, instead of the val itself

    app.display()

if __name__ == '__main__':
    main()
