from tkinter import *
from tkinter import ttk
import math


class NewJob:
    def __init__(self):

        # GUI for New Job page
        # set up GUI frames
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
        self.distance = DoubleVar()  # distance travelled to customer
        self.distance_label = Label(self.input_frame, text="Distance Travelled:", padx=5)
        self.distance_label.grid(row=5, column=0, sticky="e")
        self.distance_entry = Entry(self.input_frame, textvariable=self.distance, width=5)
        self.distance_entry.grid(row=5, column=1, sticky="w")
        self.distance_entry.delete(0, END)

        # set up virus time input
        self.virus_time = DoubleVar()  # time spent on virus protection
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

        # set up job charge variable
        self.job_charge = DoubleVar()

    def store_info(self):
        job_num = self.job_num.get()
        customer_name = self.customer_name.get()
        distance = self.distance.get()
        virus_time = self.virus_time.get()
        print(virus_time)
        wof_tune = self.wof_tune.get()

        # append info to all jobs list
        self.all_jobs_list.append([job_num, customer_name, distance, virus_time, wof_tune])

        # run calculate_charge()
        self.calculate_charge()

    def calculate_charge(self):
        # round distance to the nearest integer
        distance = self.distance.get()
        decimals = 0
        multiplier = 10 ** decimals
        distance = int(math.floor(distance*multiplier + 0.5) / multiplier)

        # round virus_time
        virus_time = self.virus_time.get()
        decimals = 0
        multiplier = 10 ** decimals
        virus_time = int(math.floor(virus_time*multiplier + 0.5) / multiplier)

        # calculate charge
        fixed_travel = 10
        additional_travel = 0.5
        virus_rate = 0.8

        if distance > 5:
            self.job_charge = fixed_travel + additional_travel*(distance - 5) + virus_rate*virus_time
        else:
            self.job_charge = fixed_travel + virus_rate*virus_time

        wof_tune = self.wof_tune.get()
        if wof_tune:
            self.job_charge += 100

        # append job charge to all jobs list
        job_num = self.job_num.get()
        job_num -= 1
        self.all_jobs_list[job_num].append(round(self.job_charge, 2))

        # clear user input and error msg
        self.customer_name.set("")
        self.distance_entry.delete(0, END)
        self.virus_time_entry.delete(0, END)
        self.wof_tune.set(False)

        # change job number
        job_num += 2
        self.job_num.set(job_num)

        print(self.all_jobs_list)

    def to_quit(self):
        new_job_box.destroy()


# main routine
if __name__ == '__main__':
    new_job_box = Tk()  # creates window
    new_job_box.title("Suzy's Professional Mobile Service")  # window heading
    main = NewJob()  # runs code
    new_job_box.mainloop()  # get the window to run
