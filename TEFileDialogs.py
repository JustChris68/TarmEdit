


class TOpenFile():
    def __init__(self, parent, *args, **kwargs):
        tkt.Frame.__init__(self, parent, *args, **kwargs)        
        style = ttk.Style(root)
        style.theme_use("clam")        
        testfile = askopenfilenames(parent=root,
                           initialdir='/',
                           initialfile='tmp',
                           filetypes=[("Pictures", "*.png|*.jpg|*.JPG"),
                                      ("All files", "*")])
        print(testfile)




























root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam")

        
def open_file():
    rep = askopenfilenames(parent=root,
                           initialdir='/',
                           initialfile='tmp',
                           filetypes=[("Pictures", "*.png|*.jpg|*.JPG"),
                                      ("All files", "*")])
#     print(rep)
#
#
# ttk.Button(root, text="Open files", command=open_file).grid(row=1, column=1,
#                                                               padx=4, pady=4,
#                                                               sticky='ew')
#
#
# root.mainloop()