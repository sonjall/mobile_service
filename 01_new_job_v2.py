from tkinter import *
from tkinter import ttk


class NewJob:
    def __init__(self):

        # GUI for New Job page
        # set up GUI frames
        self.top_frame = Frame(new_job_box, padx=10, pady=10)
        self.top_frame.grid(row=0)
        self.input_frame = Frame(new_job_box)
        self.input_frame.grid(row=1)
        self.bottom_frame = Frame(new_job_box)
        self.bottom_frame.grid(row=2)

        # company logo (row 0)
        logo_img = PhotoImage(file="mobile_service_images/business_logo.png")
        self.logo_label = Label(self.top_frame, image=logo_img)
        self.logo_label.image = logo_img
        self.logo_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # set up New Job heading
        self.new_job_heading = Label(self.top_frame, text="New Job Input",
                                     font="Arial 19 bold")
        self.new_job_heading.grid(row=1, columnspan=2)

        # user instructions
        self.instructions = StringVar()
        self.instructions.set("This program allows you to enter information for each job. \n"
                              "Press 'Enter Job' to submit the information entered. Press\n"
                              "'All Jobs' to view information for all entered jobs.")
        self.instructions_label = Label(self.top_frame, textvariable=self.instructions,
                                        justify=LEFT, font="Arial 14")
        self.instructions_label.grid(row=2, columnspan=2, padx=10, pady=5)

        # set up job number input
        self.job_num = IntVar()  # job number
        self.job_num.set("")
        self.job_num_label = Label(self.input_frame, text="Job Number:", padx=5)
        self.job_num_label.grid(row=3, column=0, sticky="e")
        self.job_num_entry = Entry(self.input_frame, textvariable=self.job_num, width=3)
        self.job_num_entry.grid(row=3, column=1, sticky="w")

        # set up customer name input
        self.customer_name = StringVar()  # customer name
        self.customer_name.set("")
        self.customer_name_label = Label(self.input_frame, text="Customer Name:", padx=5)
        self.customer_name_label.grid(row=4, column=0, sticky="e")
        self.customer_name_entry = Entry(self.input_frame, textvariable=self.customer_name, width=15)
        self.customer_name_entry.grid(row=4, column=1, sticky="w")

        # set up distance input
        self.distance = DoubleVar()  # distance travelled to customer
        self.distance.set("")
        self.distance_label = Label(self.input_frame, text="Distance Travelled:", padx=5)
        self.distance_label.grid(row=5, column=0, sticky="e")
        self.distance_entry = Entry(self.input_frame, textvariable=self.distance, width=5)
        self.distance_entry.grid(row=5, column=1, sticky="w")

        # set up virus time input
        self.virus_time = IntVar()  # time spent on virus protection
        self.virus_time.set("")
        self.virus_time_label = Label(self.input_frame, text="Time spend on virus protection:", padx=5)
        self.virus_time_label.grid(row=6, column=0, sticky="e")
        self.virus_time_entry = Entry(self.input_frame, textvariable=self.virus_time, width=3)
        self.virus_time_entry.grid(row=6, column=1, sticky="w")

        # set up wof and tune input
        self.wof_tune = IntVar()  # if a general wof and tune service was required
        self.wof_tune_label = Label(self.input_frame, text="General 'WOF and Tune':", padx=5)
        self.wof_tune_label.grid(row=7, column=0, sticky="e")
        self.wof_tune_checkbutton = ttk.Checkbutton(self.input_frame, text="Yes",
                                                    variable=self.wof_tune)
        self.wof_tune_checkbutton.grid(row=7, column=1, sticky="w")

        # set up enter job button
        self.enter_job_btn = Button(self.input_frame, text="Enter Job", font="Arial 14", pady=5)
        self.enter_job_btn.grid(row=8, columnspan=2, pady=5)

        # quit button
        self.quit_btn = Button(self.bottom_frame, text="Quit", font="Arial 14", pady=5,
                               command=self.to_quit)
        self.quit_btn.grid(row=9, column=0)

        # set up all jobs button
        self.all_jobs_btn = Button(self.bottom_frame, text="All Jobs", font="Arial 14", pady=5)
        self.all_jobs_btn.grid(row=9, column=1)

    def to_quit(self):
        new_job_box.destroy()


# main routine
if __name__ == '__main__':
    new_job_box = Tk()  # creates window
    new_job_box.title("Suzy's Professional Mobile Service")  # window heading
    main = NewJob()  # runs code
    new_job_box.mainloop()  # get the window to run
