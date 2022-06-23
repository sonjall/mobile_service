from tkinter import *
from tkinter import ttk


class NewJob:
    def __init__(self):

        # gui for New Job page
        # company logo (row 0)
        logo_img = PhotoImage(file="mobile_service_images/business_logo.png")
        self.logo_label = Label(new_job_box, image=logo_img)
        self.logo_label.image = logo_img
        self.logo_label.grid(row=0, column=0, columnspan=2)

        # set up New Job heading
        self.new_job_heading = Label(new_job_box, text="New Job",
                                     font="Arial 19 bold")
        self.new_job_heading.grid(row=1, columnspan=2)

        # user instructions
        self.instructions_label = Label(new_job_box,
                                        text="instructions text goes here.")
        self.instructions_label.grid(row=2, columnspan=2)

        # set up job number input
        self.job_num = IntVar()  # job number
        self.job_num.set("")
        self.job_num_label = Label(new_job_box, text="Job Number:", padx=5)
        self.job_num_label.grid(row=3, column=0)
        self.job_num_entry = Entry(new_job_box, textvariable=self.job_num, width=3)
        self.job_num_entry.grid(row=3, column=1)

        # set up customer name input
        self.customer_name = StringVar()  # customer name
        self.customer_name.set("")
        self.customer_name_label = Label(new_job_box, text="Customer Name:", padx=5)
        self.customer_name_label.grid(row=4, column=0)
        self.customer_name_entry = Entry(new_job_box, textvariable=self.customer_name, width=20)
        self.customer_name_entry.grid(row=4, column=1)

        # set up distance input
        self.distance = DoubleVar()  # distance travelled to customer
        self.distance.set("")
        self.distance_label = Label(new_job_box, text="Distance Travelled:", padx=5)
        self.distance_label.grid(row=5, column=0)
        self.distance_entry = Entry(new_job_box, textvariable=self.distance, width=5)
        self.distance_entry.grid(row=5, column=1)

        # set up virus time input
        self.virus_time = IntVar()  # time spent on virus protection
        self.virus_time.set("")
        self.virus_time_label = Label(new_job_box, text="Time spend on virus protection:", padx=5)
        self.virus_time_label.grid(row=6, column=0)
        self.virus_time_entry = Entry(new_job_box, textvariable=self.virus_time, width=3)
        self.virus_time_entry.grid(row=6, column=1)

        # set up wof and tune input
        self.wof_tune = IntVar()  # if a general wof and tune service was required
        self.wof_tune_label = Label(new_job_box, text="General 'WOF and Tune':", padx=5)
        self.wof_tune_label.grid(row=7, column=0)
        self.wof_tune_checkbutton = ttk.Checkbutton(new_job_box, text="Yes",
                                                    variable=self.wof_tune)
        self.wof_tune_checkbutton.grid(row=7, column=1)

        # set up enter job button
        self.enter_job_btn = Button(new_job_box, text="Enter Job")
        self.enter_job_btn.grid(row=8, columnspan=2)

        # quit button
        self.quit_btn = Button(new_job_box, text="Quit", command=self.to_quit)
        self.quit_btn.grid(row=9, column=0)

        # set up all jobs button
        self.all_jobs_btn = Button(new_job_box, text="All Jobs")
        self.all_jobs_btn.grid(row=9, column=1)

    def check_info(self):
        pass

    def store_info(self):
        pass

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
