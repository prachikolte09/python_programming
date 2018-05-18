'''
Name: Prachi Santosh kolte

File description: This file contains the graph plotter user need to provide a,b,c  cordinates of the equation which calculates values of
Y based on X range [-5,5] and plot the graph in the form of line and points
steps to run:
1. intially program starts with some basic values which respresents the simple equation
2.User need to click on new equation or select from menu to get graph of new equation
3. There are certain mathematical validations provided to input of the a,b,c values
4. After inputing the value and sucessful submission select the option from radio button the way you want to display the graph
5. Also can choose to clear the current graph or can change the graph from dotted to direct line also
6. you can also save your graph .ps in current directory


'''









from tkinter import *
import tkinter
import tkinter.messagebox
from tkinter import messagebox


class CoefficientsDialog:
    def __init__(self, master):
        self.parent = master
        self.coefficients = None  # Default value, to say its not been set yet

        self.master = Toplevel(self.parent)
        self.master.transient(self.parent)

        self.master.title("Coefficients ")
        self.lbl1 = Label(self.master, text="X^2  +").grid(row=0, column=1, sticky=E)
        self.lbl2 = Label(self.master, text="X    +").grid(row=1, column=1, sticky=E)
        self.lbl3 = Label(self.master, text="    +").grid(row=2, column=1, sticky=E)
        self.ent1 = Entry(self.master)
        self.ent1.grid(row=0, column=0)
        self.ent2 = Entry(self.master)
        self.ent2.grid(row=1, column=0)
        self.ent3 = Entry(self.master)
        self.ent3.grid(row=2, column=0)
        btn1 = tkinter.Button(self.master, text="Submit", command=self.submit, image=None)
        btn1.grid()

    def submit(self, event=None):
        '''
        Handle submit button action
        '''

        try:
            data = int(self.ent1.get())
            if data == 0:
                raise Exception
            data2 = int(self.ent2.get())
            data3 = int(self.ent3.get())
            print (data)
            print (data2)
            print (data3)
            self.coefficients={'a':data,'b':data2,'c':data3}
            self.master.destroy()

        except ValueError:

            error_window = tkinter.Tk()
            error_window.title("Error")
            error_window.geometry("200x200")
            label = Label(error_window, text="Please enter integer", height=0, width=100)
            b = Button(error_window, text="Ok", width=20, command=error_window.destroy)
            label.pack()
            b.pack(side='bottom', padx=0, pady=0)
        except Exception as e:
            error_window = tkinter.Tk()
            error_window.title("Error")
            error_window.geometry("100x100")
            label = Label(error_window, text="X^2 value can not be 0", height=0, width=100)
            b = Button(error_window, text="Ok", width=20, command=error_window.destroy)
            label.pack()
            b.pack(side='bottom', padx=0, pady=0)
    def show(self):
        self.toplevel.deiconify()
        self.toplevel.wait_window()
        value = self.var.get()
        return value


class QuadEQPlot:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        self.x_values = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
        self.y_values = []
        # print(self.x_values)
        self.init_widget()

        self.window.mainloop()

    def hello(self):
        print("hello!")

    def init_widget(self):
        self.coefficientsDialog = None
        self.window = tkinter.Tk()
        # self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.title("Function Plot")
        self.eqation = "No Equation"
        self.height = 700
        self.width = 700
        self.window.geometry("{}x{}".format(self.width, self.height))

        self.root = tkinter.Frame(self.window)
        self.root.pack(expand=True, fill="both")

        self.new_equation = Button(self.root, text="New Equation", width=20, command=self.get_new_coefficient)
        self.new_equation.pack()

        self.labelframe = LabelFrame(self.root)
        self.labelframe.pack(expand=True, fill="both")

        self.eqationLabel = Label(self.labelframe, text=self.eqation)
        self.eqationLabel.pack(side='left')

        self.canvas = tkinter.Canvas(self.root, width=500, height=500, bg="white")
        self.canvas.pack()

        self.plot_axis()
        self.plot_equation()

        #################radiobutton###################
        R1 = Radiobutton(self.window, text="Points", command=self.plot_points)
        R1.pack(side='right')

        R2 = Radiobutton(self.window, text="Lines", command=self.plot_line)
        R2.pack(side='right')
        ################## Menu##################
        menubar = Menu(self.window)

        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="New Equation", command=self.get_new_coefficient)
        filemenu.add_command(label="Save plot .ps", command=self.save_canvas)
        filemenu.add_separator()
        filemenu.add_command(label="Clear", command=self.clear_canvas)
        filemenu.add_command(label="Exit", command=self.exit_window)

        menubar.add_cascade(label="File", menu=filemenu)

        helpmenu = Menu(menubar, tearoff=0)
        helpmenu.add_command(label="About", command=self.show_help_about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        # display the menu
        self.window.config(menu=menubar)
        ##########################



    def plot_axis(self):
        self.canvas.create_line(250, 50, 250, 450, width=2, fill="blue")
        self.canvas.create_line(50, 250, 450, 250, width=2, fill="blue")

    def plot_equation(self):
        self.clear_canvas()

        self.plot_axis()
        for i in self.x_values:
            self.y_values.append(self.a * i * i + self.b * i + self.c)


        print("########################################")
        print (self.y_values)
        print("########################################")
        ################################
        x_x0 = 50  # x axis
        y_x0 = 250  # for x axis

        x_y0 = 250  # for y axis
        y_y0 = 50  # for y axis
        d = 40

        for i in range(-5, 6):
            self.canvas.create_line(x_x0, y_x0, x_x0 + 1, y_x0 + 1, fill='darkblue')  ## for x axis
            self.canvas.create_line(x_y0, y_y0, x_y0 + 1, y_y0 + 1, fill='darkblue')  ## for y axis

            x_x0 = x_x0 + d
            y_y0 = y_y0 + d
        x_x0 = 50  # x axis
        y_x0 = 250  # x axis
        for value in self.x_values:
            self.canvas.create_text(x_x0, y_x0 + 5, fill="Black", font="Times 10 italic bold", text=value)
            print("x_x0:", x_x0, value)
            x_x0 = x_x0 + d

        x_y0 = 250  # for y axis
        y_y0 = 50  # for y axis
        d = 40

        for value in self.y_values[:5]:
            print("*****")
            print(value)
            self.canvas.create_text(x_y0 + 10, y_y0, fill="darkblue", font="Times 10 italic bold", text=value)

            y_y0 = y_y0 + d

        x_y0 = 250  # for y axis
        y_y0 = 450  # for y axis
        d = 40
        for value in self.y_values[:5]:
            print(value * (-1))
            self.canvas.create_text(x_y0 + 10, y_y0, fill="darkblue", font="Times 10 italic bold",
                                    text=value * (-1))


            y_y0 = y_y0 - d
         ##########   #################################

        self.y_values = []
        for i in self.x_values:
            self.y_values.append(self.a * i * i + self.b * i + self.c)

        self.eqationLabel[
            "text"] = self.get_a_coeff_expression() + self.get_b_coeff_expression() + self.get_c_coeff_expression()

    def get_new_coefficient(self):
        if self.coefficientsDialog == None:
            self.coefficientsDialog = CoefficientsDialog(self.root)
            self.coefficientsDialog.parent.wait_window(self.coefficientsDialog.master)
            self.a = self.coefficientsDialog.coefficients['a']
            self.b = self.coefficientsDialog.coefficients['b']
            self.c = self.coefficientsDialog.coefficients['c']
            # print (self.a)
            # print (self.b)
            # print (self.c)
            self.plot_axis()
            self.plot_equation()
            self.coefficientsDialog = None


    def plot_points(self):
        self.clear_canvas()
        self.plot_axis()
        self.plot_equation()
        try:
            y_min = abs(min(self.y_values))
            y_max = abs(max(self.y_values))

            y_final = y_min if y_min > y_max else y_max
            y_ratio = y_final / 5
            print(y_final)

            for i in range(len(self.x_values)):
                    x_ax = (self.x_values[i] + 5) * 40 + 50
                    y_ax = (-1 * self.y_values[i] / y_ratio * 40) + 250
                    #print(x_ax, y_ax)
                    self.canvas.create_oval(x_ax - 2, y_ax - 2, x_ax + 2, y_ax + 2, outline="red", fill="yellow")
        except:
                pass



    def plot_line(self):
        self.clear_canvas()
        self.plot_axis()
        self.plot_equation()
        y_min = abs(min(self.y_values))
        y_max = abs(max(self.y_values))

        y_final = y_min if y_min > y_max else y_max
        y_ratio = y_final / 5
        print(y_final)
        lines_cordionates={}

        for i in range(len(self.x_values)):
            x_ax = (self.x_values[i] + 5) * 40 + 50
            y_ax = (-1 * self.y_values[i] / y_ratio * 40) + 250
            lines_cordionates[i]=x_ax,y_ax
        try:

            for i in range(len(self.x_values)):
                self.canvas.create_line(lines_cordionates[i][0], lines_cordionates[i][1], lines_cordionates[i+1][0], lines_cordionates[i+1][1], fill='darkblue')
        except:
            pass
    def exit_window(self):
        if messagebox.askyesno("Exit", "Do you want to quit the application?"):
            self.window.destroy()

    def clear_canvas(self):

        self.canvas.delete("all")

    def new_equation(self):
        self.plot_axis()
        self.y_values = []
        for i in self.x_values:
            self.y_values.append(self.a * i * i + self.b * i + self.c)
        self.plot_points()
        self.eqationLabel[
            "text"] = self.get_a_coeff_expression() + self.get_b_coeff_expression() + self.get_c_coeff_expression()

    def get_new_coefficient(self):
        if self.coefficientsDialog == None:
            self.coefficientsDialog = CoefficientsDialog(self.root)
            self.coefficientsDialog.parent.wait_window(self.coefficientsDialog.master)
            self.a = self.coefficientsDialog.coefficients['a']
            self.b = self.coefficientsDialog.coefficients['b']
            self.c = self.coefficientsDialog.coefficients['c']

            self.plot_axis()
            self.plot_equation()
            self.coefficientsDialog = None

    def get_a_coeff_expression(self):
        if self.a > 1 or self.a < -1:
            return str(self.a) + "X" + u"\u00B2"
        elif self.a == -1:
            return "-X" + u"\u00B2"
        else:
            return "X" + u"\u00B2"

    def get_b_coeff_expression(self):
        coeef = self.b
        if coeef > 1:
            return "+" + str(coeef) + "X"
        elif coeef < -1:
            return str(coeef) + "X"
        elif coeef == 1:
            return "+" + "X"
        elif coeef == -1:
            return "-" + "X"
        else:
            return ""

    def get_c_coeff_expression(self):
        coeef = self.c
        if coeef > 0:
            return "+" + str(coeef)
        elif coeef < 0:
            return str(coeef)
        else:
            return ""

    def save_canvas(self):
        self.canvas.postscript(file="1017665.ps", colormode='color')

    def show_help_about(self):
        top = Toplevel()
        top.title("About this application...")

        msg = Message(top, text="Created by Prachi Kolte \n UB ID: 1017665")
        msg.pack()

        button = Button(top, text="Dismiss", command=top.destroy)
        button.pack()


obj = QuadEQPlot(1, 0, 0)

