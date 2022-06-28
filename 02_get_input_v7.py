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

        # set up job number input
        self.job_num = IntVar()  # job number
        self.job_num.set(1)
        self.job_num_label = Label(self.input_frame, text="Job Number:", padx=5)
        self.job_num_label.grid(row=3, column=0, sticky="e")
        self.show_job_num = Label(self.input_frame, textvariable=self.job_num, width=3)
        self.show_job_num.grid(row=3, column=1, sticky="w")

        # set up customer name input
        self.customer_name = StringVar()  # customer name
        self.customer_name.set("")
        self.customer_name_label = Label(self.input_frame, text="Customer Name:", padx=5)
        self.customer_name_label.grid(row=4, column=0, sticky="e")
        self.customer_name_entry = Entry(self.input_frame, textvariable=self.customer_name, width=15)
        self.customer_name_entry.grid(row=4, column=1, sticky="w")

        # set up distance input
        self.distance = StringVar()  # distance travelled to customer
        self.distance_label = Label(self.input_frame, text="Distance Travelled:", padx=5)
        self.distance_label.grid(row=5, column=0, sticky="e")
        self.distance_entry = Entry(self.input_frame, textvariable=self.distance, width=5)
        self.distance_entry.grid(row=5, column=1, sticky="w")
        self.distance_entry.delete(0, END)

        # set up virus time input
        self.virus_time = StringVar()  # time spent on virus protection
        self.virus_time_label = Label(self.input_frame, text="Time spend on virus protection:", padx=5)
        self.virus_time_label.grid(row=6, column=0, sticky="e")
        self.virus_time_entry = Entry(self.input_frame, textvariable=self.virus_time, width=3)
        self.virus_time_entry.grid(row=6, column=1, sticky="w")
        self.virus_time_entry.delete(0, END)

        # set up wof and tune input
        self.wof_tune = BooleanVar()  # if a general wof and tune service was required
        self.wof_tune_label = Label(self.input_frame, text="General 'WOF and Tune':", padx=5)
        self.wof_tune_label.grid(row=7, column=0, sticky="e")
        self.wof_tune_checkbutton = ttk.Checkbutton(self.input_frame, text="Yes",
                                                    variable=self.wof_tune)
        self.wof_tune_checkbutton.grid(row=7, column=1, sticky="w")

        # set up error/success label
        self.error_success_label = Label(self.input_frame, text="")
        self.error_success_label.grid(row=8, columnspan=2)

        # set up enter job button
        self.enter_job_btn = Button(self.input_frame, text="Enter Job", font="Arial 14", pady=5,
                                    command=self.store_info)
        self.enter_job_btn.grid(row=9, columnspan=2, pady=5)

        # quit button
        self.quit_btn = Button(self.bottom_frame, text="Quit", font="Arial 14", pady=5,
                               command=self.to_quit)
        self.quit_btn.grid(row=10, columnspan=2)

        # set up all jobs list
        self.all_jobs_list = []

    def store_info(self):
        # check customer name entry is not blank
        if self.customer_name.get() == "" or self.distance.get() == "" or self.virus_time.get() == "":
            self.error_success_label.configure(text="Please do not leave any of the entries blank.")
        else:
            customer_name = self.customer_name.get()
            try:
                distance = float(self.distance.get())
                if distance < 0:
                    raise ValueError
            except ValueError:
                self.error_success_label.configure(text="Distance should be a number above or equal to 0")
            else:
                # check virus time entry is a number
                try:
                    virus_time = float(self.virus_time.get())
                    if virus_time < 0:
                        raise ValueError
                except ValueError:
                    self.error_success_label.configure(text="Virus Time should be a number above or equal to 0")
                else:
                    job_num = self.job_num.get()
                    wof_tune = self.wof_tune.get()

                    # append info to all jobs list
                    self.all_jobs_list.append([job_num, customer_name, distance, virus_time, wof_tune])

                    # change job number
                    job_num += 1
                    self.job_num.set(job_num)
                    print(self.all_jobs_list)

                    # display success message
                    self.error_success_label.configure(text="Job was successfully saved!")

                    # clear user input
                    self.customer_name.set("")
                    self.distance_entry.delete(0, END)
                    self.virus_time_entry.delete(0, END)
                    self.wof_tune.set(False)

    def calculate_charge(self):
        pass

    def to_quit(self):
        new_job_box.destroy()


# main routine
if __name__ == '__main__':
    new_job_box = Tk()  # creates window
    new_job_box.title("Suzy's Professional Mobile Service")  # window heading
    main = NewJob()  # runs code
    new_job_box.mainloop()  # get the window to run
