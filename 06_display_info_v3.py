from tkinter import *
from functools import partial  # to prevent unwanted windows


class NewJob:
    def __init__(self):

        # GUI for New Job page
        # set up GUI frames
        self.bottom_frame = Frame(new_job_box)
        self.bottom_frame.grid(row=0)

        # quit button
        self.quit_btn = Button(self.bottom_frame, text="Quit", font="Arial 14", pady=5,
                               command=self.to_quit)
        self.quit_btn.grid(row=1)

        # set up all jobs button
        self.all_jobs_btn = Button(self.bottom_frame, text="All Jobs", font="Arial 14", pady=5,
                                   command=self.to_all_jobs)
        self.all_jobs_btn.grid(row=0)

    def to_all_jobs(self):
        AllJobs(self)

    def to_quit(self):
        new_job_box.destroy()


class AllJobs:
    def __init__(self, partner):

        # create All Jobs page
        self.all_jobs_box = Toplevel()

        # set up GUI frame
        self.display_frame = Frame(self.all_jobs_box, padx=10, pady=10)  # frame for job info
        self.display_frame.grid(row=0)
        self.buttons_frame = Frame(self.all_jobs_box, padx=10, pady=10)  # frame for buttons
        self.buttons_frame.grid(row=1)

        # disable All Jobs button on Menu page
        partner.all_jobs_btn.config(state=DISABLED)

        # if user presses cross at top, closes help and 'releases' All Jobs button on New Job page
        self.all_jobs_box.protocol('WM_DELETE_WINDOW', partial(self.close_all_jobs, partner))

        # set up All Jobs heading
        self.new_job_heading = Label(self.display_frame, text="All Jobs",
                                     font="Arial 19 bold")
        self.new_job_heading.grid(row=0, columnspan=2, pady=5)

        self.all_jobs_list = [[1, 'Sonja', 20.0, 30, True, 141.5],
                              [2, 'Bob', 15.0, 40, False, 47.0],
                              [3, 'Ariana Grande', 40.0, 30, True, 151.5],
                              [4, 'Lucy', 24.0, 20, True, 135.5]]

        self.job = 0

        # set up job number label
        self.job_num = IntVar()
        self.job_num.set(self.all_jobs_list[0][0])
        self.job_num_label = Label(self.display_frame, text="Job Number:")
        self.job_num_label.grid(row=1, column=0, sticky="e")
        self.show_job_num = Label(self.display_frame, textvariable=self.job_num)
        self.show_job_num.grid(row=1, column=1, sticky="w")

        # set up customer name label
        self.customer_name = StringVar()
        self.customer_name.set(self.all_jobs_list[0][1])
        self.customer_name_label = Label(self.display_frame, text="Customer Name:")
        self.customer_name_label.grid(row=2, column=0, sticky="e")
        self.show_customer_name = Label(self.display_frame, textvariable=self.customer_name)
        self.show_customer_name.grid(row=2, column=1, sticky="w")

        # set up job charge label
        self.job_charge = DoubleVar()
        self.job_charge.set(self.all_jobs_list[0][5])
        self.job_charge_label = Label(self.display_frame, text="Job Charge:")
        self.job_charge_label.grid(row=3, column=0, sticky="e")
        self.show_job_charge = Label(self.display_frame, textvariable=self.job_charge)
        self.show_job_charge.grid(row=3, column=1, sticky="w")

        # set up next button
        self.next_button = Button(self.buttons_frame, text="Next",
                                  command=lambda: self.display_info("next"))
        self.next_button.grid(row=0, column=1)

        # set up previous button
        self.previous_button = Button(self.buttons_frame, text="Previous",
                                      command=lambda: self.display_info("previous"))
        self.previous_button.grid(row=0, column=0)
        self.previous_button.config(state=DISABLED)

        # set up dismiss button
        self.dismiss_button = Button(self.buttons_frame, text="Dismiss",
                                     command=partial(self.close_all_jobs, partner))
        self.dismiss_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    def display_info(self, scroll):

        # change displayed job info
        if scroll == "next":
            self.job += 1
            self.job_num.set(self.all_jobs_list[self.job][0])
            self.customer_name.set(self.all_jobs_list[self.job][1])
            self.job_charge.set(self.all_jobs_list[self.job][5])
        elif scroll == "previous":
            self.job -= 1
            self.job_num.set(self.all_jobs_list[self.job][0])
            self.customer_name.set(self.all_jobs_list[self.job][1])
            self.job_charge.set(self.all_jobs_list[self.job][5])

        if self.job == 0:
            self.previous_button.config(state=DISABLED)
        else:
            self.previous_button.config(state=NORMAL)

        if self.job == len(self.all_jobs_list) - 1:
            self.next_button.config(state=DISABLED)
        else:
            self.next_button.config(state=NORMAL)

    def close_all_jobs(self, partner):

        # put All Jobs button back to normal
        partner.all_jobs_btn.config(state=NORMAL)

        # close All Jobs box
        self.all_jobs_box.destroy()


# main routine
if __name__ == '__main__':
    new_job_box = Tk()  # creates window
    new_job_box.title("Suzy's Professional Mobile Service")  # window heading
    main = NewJob()  # runs code
    new_job_box.mainloop()  # get the window to run
