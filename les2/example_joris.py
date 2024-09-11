import tkinter as tk

class LEDBoard(tk.Tk):
    def __init__(self, num_leds):
        super().__init__()
        self.title("LED Board")
        self.leds = []
        self.current_led = 0
        self.num_leds = num_leds

        for i in range(num_leds):
            led = tk.Button(self, bg="green", width=4, height=2)
            led.grid(row=0, column=i, padx=2, pady=2)
            self.leds.append(led)

        self.flash_leds()

    def flash_leds(self):
        # Turn off all LEDs
        for led in self.leds:
            led.config(bg="green")

        # Turn on the current LED
        self.leds[self.current_led].config(bg="red")

        # Move to the next LED
        self.current_led = (self.current_led + 1) % self.num_leds

        # Schedule the next flash
        self.after(1000, self.flash_leds)  # Adjust the time (in milliseconds) as needed

if __name__ == "__main__":
    board = LEDBoard(8)  # Create a line of 8 
    board.mainloop()
