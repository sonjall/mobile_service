from tkinter import *


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

        # set up All Jobs heading
        self.new_job_heading = Label(self.all_jobs_box, text="All Jobs")
        self.new_job_heading.grid(row=0, columnspan=2, pady=5)


# main routine
if __name__ == '__main__':
    new_job_box = Tk()  # creates window
    new_job_box.title("Suzy's Professional Mobile Service")  # window heading
    main = NewJob()  # runs code
    new_job_box.mainloop()  # get the window to run
