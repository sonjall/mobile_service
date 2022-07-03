from tkinter import *
from functools import partial  # to prevent unwanted windows
from tkinter import ttk
import math
import string


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
        self.instructions.set("This program allows you to enter information for jobs you \n"
                              "have completed. Press 'Enter Job' to submit the information \n"
                              "entered. Press 'All Jobs' to view information for all \n"
                              "entered jobs. You will not be able to view 'All Jobs' \n"
                              "until at least one job has been entered.")
        self.instructions_label = Label(self.top_frame, textvariable=self.instructions,
                                        justify=LEFT, font="Arial 14", bg="#3298FF",
                                        fg="white", padx=5, pady=5)
        self.instructions_label.grid(row=2, columnspan=2, padx=10, pady=5)

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
        self.distance_label = Label(self.input_frame, text="Distance Travelled to Customer (km):", padx=5)
        self.distance_label.grid(row=5, column=0, sticky="e")
        self.distance_entry = Entry(self.input_frame, textvariable=self.distance, width=5)
        self.distance_entry.grid(row=5, column=1, sticky="w")
        self.distance_entry.delete(0, END)

        # set up virus time input
        self.virus_time = StringVar()  # time spent on virus protection
        self.virus_time_label = Label(self.input_frame, text="Time spent on virus protection (min):", padx=5)
        self.virus_time_label.grid(row=6, column=0, sticky="e")
        self.virus_time_entry = Entry(self.input_frame, textvariable=self.virus_time, width=3)
        self.virus_time_entry.grid(row=6, column=1, sticky="w")
        self.virus_time_entry.delete(0, END)

        # set up wof and tune input
        self.wof_tune = BooleanVar()  # if a general wof and tune service was required
        self.wof_tune_label = Label(self.input_frame, text="Was a General 'WOF and Tune' \n"
                                                           "service required?:",
                                    padx=5, justify="right")
        self.wof_tune_label.grid(row=7, column=0, sticky="e")
        self.wof_tune_checkbutton = ttk.Checkbutton(self.input_frame, text="Yes",
                                                    variable=self.wof_tune)
        self.wof_tune_checkbutton.grid(row=7, column=1, sticky="w")

        # set up error/success label
        self.error_success_label = Label(self.input_frame, text="", font="Arial 14")
        self.error_success_label.grid(row=8, columnspan=2)

        # set up enter job button
        self.enter_job_btn = Button(self.input_frame, text="Enter Job", font="Arial 14", pady=5,
                                    command=self.store_info)
        self.enter_job_btn.grid(row=9, columnspan=2, pady=5)

        # set up all jobs list
        self.all_jobs_list = []

        # quit button
        self.quit_btn = Button(self.bottom_frame, text="Quit", font="Arial 14", pady=5,
                               command=self.to_quit)
        self.quit_btn.grid(row=9, column=0)

        # set up all jobs button
        self.all_jobs_btn = Button(self.bottom_frame, text="All Jobs", font="Arial 14", pady=5,
                                   command=lambda: self.to_all_jobs(self.all_jobs_list))
        self.all_jobs_btn.grid(row=9, column=1)
        self.all_jobs_btn.config(state=DISABLED)

    def store_info(self):
        # check customer name entry is not blank
        if self.customer_name.get() == "" or self.distance.get() == "" or self.virus_time.get() == "":
            self.error_success_label.configure(text="Please do not leave any of the entries blank.",
                                               bg="#FF4B38", fg="white")
        else:
            # check customer name is valid
            try:
                customer_name = self.customer_name.get()
                customer_name = ''.join([i for i in customer_name if not i.isdigit()])
                for char in string.punctuation:
                    customer_name = customer_name.replace(char, '')
                customer_name = customer_name.strip()
                if customer_name == "":
                    raise ValueError
            except ValueError:
                self.error_success_label.configure(text="Customer name should not include any numbers or symbols.",
                                                   bg="#FF4B38", fg="white")
            else:
                # check distance entry is a number
                try:
                    distance = float(self.distance.get())
                    if distance < 0 or distance > 2000:
                        raise ValueError
                except ValueError:
                    self.error_success_label.configure(text="Distance should be a number above or equal to 0, \n"
                                                            "and lower than or equal to 2000",
                                                       bg="#FF4B38", fg="white")
                else:
                    # check virus time entry is a number
                    try:
                        virus_time = float(self.virus_time.get())
                        if virus_time < 0:
                            raise ValueError
                    except ValueError:
                        self.error_success_label.configure(text="Virus Time should be a number above or equal to 0",
                                                           bg="#FF4B38", fg="white")
                    else:
                        job_num = self.job_num.get()
                        wof_tune = self.wof_tune.get()

                        # append info to all jobs list
                        self.all_jobs_list.append([job_num, customer_name, distance, virus_time, wof_tune])

                        # display success message
                        self.error_success_label.configure(text="Job was successfully saved!",
                                                           bg="#3298FF", fg="white", padx=5)

                        # enable All Jobs button
                        self.all_jobs_btn.config(state=NORMAL)

                        # run calculate_charge()
                        self.calculate_charge(job_num, distance, virus_time, wof_tune)

    def calculate_charge(self, job_num, distance, virus_time, wof_tune):
        # round distance to the nearest integer
        DECIMALS = 0
        MULTIPLIER = 10 ** DECIMALS
        distance = int(math.floor(distance*MULTIPLIER + 0.5) / MULTIPLIER)

        # round virus_time
        if virus_time > 10:
            virus_time = int(math.ceil(virus_time))

        # calculate charge
        FIXED_TRAVEL = 10
        ADDITIONAL_TRAVEL = 0.5
        VIRUS_RATE = 0.8

        if distance > 5:
            self.job_charge = FIXED_TRAVEL + ADDITIONAL_TRAVEL*(distance - 5) + VIRUS_RATE*virus_time
        else:
            self.job_charge = FIXED_TRAVEL + VIRUS_RATE*virus_time

        if wof_tune:
            self.job_charge += 100

        # append job charge to all jobs list
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

    def to_all_jobs(self, all_jobs_list):
        AllJobs(self, all_jobs_list)

    def to_quit(self):
        new_job_box.destroy()


class AllJobs:
    def __init__(self, partner, all_jobs_list):

        # create All Jobs page
        self.all_jobs_box = Toplevel()

        # set up GUI frame
        self.display_frame = Frame(self.all_jobs_box, padx=10, pady=10)  # frame for job info
        self.display_frame.grid(row=0)
        self.buttons_frame = Frame(self.all_jobs_box, padx=10, pady=10)  # frame for buttons
        self.buttons_frame.grid(row=1)

        # disable All Jobs button on New Job page
        partner.all_jobs_btn.config(state=DISABLED)

        # disable Enter Job button on New Job page
        partner.enter_job_btn.config(state=DISABLED)

        # if user presses cross at top, closes help and 'releases' All Jobs button on New Job page
        self.all_jobs_box.protocol('WM_DELETE_WINDOW', partial(self.close_all_jobs, partner))

        # set up All Jobs heading
        self.new_job_heading = Label(self.display_frame, text="All Jobs",
                                     font="Arial 19 bold")
        self.new_job_heading.grid(row=0, columnspan=2, pady=5)

        # set up all jobs list
        self.all_jobs_list = all_jobs_list

        # set up displayed job
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
        if len(self.all_jobs_list) == 1:
            self.next_button.config(state=DISABLED)

        # set up previous button
        self.previous_button = Button(self.buttons_frame, text="Previous",
                                      command=lambda: self.display_info("previous"))
        self.previous_button.grid(row=0, column=0)
        self.previous_button.config(state=DISABLED)

        # set up dismiss button
        self.dismiss_button = Button(self.buttons_frame, text="Dismiss",
                                     command=partial(self.close_all_jobs, partner))
        self.dismiss_button.grid(row=1, columnspan=2, padx=10, pady=5)

        # set up message informing user that no new jobs can be entered
        self.no_job_msg = Label(self.buttons_frame, text="No new jobs can be entered \n"
                                                         "while this page is open.",
                                bg="#FF4B38", fg="white", padx=5, pady=5)
        self.no_job_msg.grid(row=2, columnspan=2)

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

        # put Enter Job button back to normal
        partner.enter_job_btn.config(state=NORMAL)

        # close All Jobs box
        self.all_jobs_box.destroy()


# main routine
if __name__ == '__main__':
    new_job_box = Tk()  # creates window
    new_job_box.title("Suzy's Professional Mobile Service")  # window heading
    main = NewJob()  # runs code
    new_job_box.mainloop()  # get the window to run
