# to get started read this https://realpython.com/python-gui-tkinter/
# watch this  https://www.youtube.com/watch?v=YXPyB4XeYLA
# done, you know tkinter now!
from tkinter import *
from tkinter import filedialog
from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
from ttkthemes import ThemedTk
from PIL import ImageTk, Image
from docx import *
from docx import Document

class App:
    def __init__(self):
        print('App created..')

    def gmtry(self, app_width, app_height):
        self.app_width = app_width
        self.app_height = app_height
        # Gets both half the screen width/height and window width/height
        positionRight = int(self.winfo_screenwidth()/2 - app_width/2)
        positionDown = int(self.winfo_screenheight()/2 - app_height/2)
        # Positions the window in the center of the page.
        self.geometry(f"{app_width}x{app_height}+{positionRight}+{positionDown}")

    def btn(self, frame, text, command ):
        return ttk.Button(frame, text = text,width=17, command=command)

    def img():
        pass


class Main_window(ThemedTk, App):
    def __init__(self):
        super().__init__()
        # global m_background
        # m_background = ImageTk.PhotoImage(Image.open('./assets/bk.jpg'))
        # ttk.Label(self, image =m_background).place(x = 0, y = 0)
        self.body = ttk.Frame(self)
        self.body.place(relx=0.5,rely=0.5,anchor=CENTER) # center all app content to the center of the body
        self.resizable(width = True, height = True) # Allow Window to be resizable
        self.title('Doctorizer')
        self.iconbitmap('./assets/logo.png')
        self.config(bg="#2d2d2d")
        #left and right frames
        self.left_frame = ttk.Frame(self.body)
        self.left_frame.grid(row=1, column=0, padx=50, pady=10)

        self.right_frame = ttk.LabelFrame(self.body, text='X-ray image', width=505,height=510)
        self.right_frame.grid(row=1, column=1, padx=50,pady=10)

        # main screen widgets
        # Label(self, text ="X-ray image analyzer", font=10).place(relx=0.5,rely=0.04, anchor=CENTER)

        self.btn(self.left_frame, text ="upload image", command=self.upload_image).grid(row=1, column=0,padx=50, pady=10)
        self.btn(self.left_frame, text ="clear workspace",command = lambda: self.clear_workspace(panel)).grid(row=2, column=0, pady=10)
        self.btn(self.left_frame, text ="classify", command=self.classify).grid(row=3, column=0, pady=10)
        self.btn(self.left_frame, text ="automated report", command=show_patient_dw).grid(row=4, column=0, pady=10)

    #functions
    def upload_image(self):
        # Select the Imagename  from a folder
        try:
            x = filedialog.askopenfilename(title ='"pen')
        except:
            return 'Failed To Open the File'
        if x:
            global img
            # opens the image
            img = Image.open(x)
            # resize the image and rootly a high-quality down sampling filter
            img = img.resize((500, 500), Image.ANTIALIAS)
            # PhotoImage class is used to add image to widgets, icons etc
            img = ImageTk.PhotoImage(img)
            # create a label
            global panel
            panel = ttk.Label(self.right_frame, image = img)
            # set the image as img
            self.clear_workspace(panel)
            panel.grid(row=0, column=0)

    def clear_workspace(self, panel):
        print('clear_workspace')
        panel.grid_forget()

    def classify(self):
        print('classify')


class Window(Toplevel, App):
    def __init__(self, parent):
        super().__init__(parent)
        # global wn_background
        # wn_background = ImageTk.PhotoImage(Image.open('./assets/bk.jpg'))
        # Label(self, image = wn_background).place(x = 0, y = 0)
        self.body = ttk.Frame(self)
        # center all app content to the center of the body
        self.body.place(relx=0.5,rely=0.5,anchor=CENTER)
        # Allow Window to be resizable
        self.resizable(width=False, height=False)
        self.title('Doctorizer')
        self.iconbitmap('./assets/logo.png')
        self.config(bg="#2d2d2d")

class Patient_data_window(Window):
    def __init__(self, parent):
        super().__init__(parent)
        #window settings
        self.title('patient data')
        ttk.Label(self.body, text='Patient Name').grid(row=0, column=0)
        entry0 = ttk.Entry(self.body)
        entry0.grid(row=0, column=1,padx=5, pady=10)
        name = entry0.get()

        ttk.Label(self.body, text='Patient Age').grid(row=1, column=0)
        entry1 = ttk.Entry(self.body)
        entry1.grid(row=1, column=1, padx=5,pady=10)
        Age = entry1.get()

        ttk.Label(self.body, text='Patient previous illness').grid(row=2, column=0)
        entry2 = ttk.Entry(self.body)
        entry2.grid(row=2, column=1, padx=5,pady=10)
        Age = entry2.get()

        self.btn(self.body, text='generate report', command = self.generate_report).grid(row=5,column=2, padx=10,pady=15)

    def generate_report(self):
        document = Document()
        document.add_heading('Doctorizer automated report', 0)
        p = document.add_paragraph('based on the analyzed chest x-ray image, the patient is infected with a strange and dangerous bacteria, ')
        p.add_run(' and he might die with a propabiliy of 98.2%. ').bold = True
        p.add_run('enjoy!').italic = True
        self.save_report(document)

    def save_report(self, document):
        filepath = filedialog.asksaveasfilename(initialfile = 'report.docx',defaultextension=".docx",filetypes=[("All Files","*.*"),("Word Documents","*.docx")])
        try:
            document.save(filepath)
        except:
            raise Exception('Error: File not saved')
        self.open_report(filepath)

    def open_report(self,filepath):
        import subprocess, os, platform
        if platform.system() == 'Darwin':       # macOS
            subprocess.call(('open', filepath))
        elif platform.system() == 'Windows':    # Windows
            os.startfile(filepath)
        else:                                   # linux variants
            subprocess.call(('xdg-open', filepath))


if __name__ == '__main__':
    def show_patient_dw():
        patient_dw = Patient_data_window(parent=root)
        patient_dw.gmtry(600,400)
    #create root instance
    root = Main_window()
    print(root.get_themes())
    root.set_theme('black') #xpnative
    root.gmtry(1100,600)
    root.mainloop()
