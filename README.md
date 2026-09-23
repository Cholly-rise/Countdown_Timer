# Countdown_Timer

START

Ask the user to enter a countdown duration

Validate the input:
    IF the input is empty, not a number, or negative:
        Display "Please enter a whole number."
    ELSE:
        Set the timer to the given duration
        Set the timer state to RUNNING

        WHILE the timer has not reached zero:

            IF the timer is RUNNING:
                Convert the time to minutes and seconds
                Display the remaining time as MM:SS
                Wait 1 second
                Subtract 1 second

            IF the user chooses PAUSE:
                Pause the timer

            IF the user chooses RESUME:
                Resume the timer

            IF the user chooses RESET:
                Restore the original duration
                Start the timer again

        Display "Time's up!"

        Allow the user to start another timer

END





IN SUMMARY

Our countdown timer can:

✅ Ask the user for the countdown time
✅ Reject empty input
✅ Reject letters
✅ Reject negative numbers
✅ Convert seconds into minutes:seconds
✅ Count down every second
✅ Stop at 00:00
✅ Display "Time's up!"
✅ Allow another timer after completion



# Countdown Timer

A beginner-friendly Python countdown timer that allows the user to enter **hours, minutes, and seconds** directly.

The timer supports:

* Hours, minutes, and seconds input
* Countdown in `HH:MM:SS` format
* Pause
* Resume
* Reset
* Stop
* Starting another timer after completion
* Terminal alarm when the countdown reaches zero
* Input validation

---



# How to Run

Open your terminal and go to your project folder:

```bash
cd ~/LEARNING_PYTHON
```

Then run the program:

```bash
python3 countdown_timer.py
```

---

# Setting the Timer

The program asks for the time separately:

```text
Enter hours:
Enter minutes:
Enter seconds:
```


# Timer Commands

While the timer is running, you can use these commands:

| Command | Action        |
| ------- | ------------- |
| `p`     | Pause         |
| `r`     | Resume        |
| `x`     | Reset         |
| `s`     | Stop          |
| `Enter` | Continue/wait |

---



# Main Parts of the Program

## 1. `fmt()`

Converts seconds into hours, minutes, and seconds.

```python
def fmt(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
```


## 2. `get_number()`

Gets input from the user and makes sure it is a whole number.

```python
def get_number(message):
```

This prevents invalid entries such as:

```text
abc
hello
2.5
```

---

## 3. `get_time()`

Collects:

```text
hours
minutes
seconds
```

and converts them into total seconds.

```python
total = (hours * 3600) + (minutes * 60) + seconds
```

---

# 4. `Timer` Class

The `Timer` class controls the countdown.

It contains methods for:

```python
start()
pause()
resume()
reset()
stop()
```

Using a class keeps all the timer-related functionality together.

---

# 5. Threading

The program uses:

```python
threading.Thread()
```

This allows the countdown to run in the background.

Without threading, the program would have difficulty listening for commands such as:

```text
p
r
x
s
```

while the timer is counting down.

---

# 6. `time.sleep()`

The program uses:

```python
time.sleep(0.1)
```

to make the program wait for a short period.

Ten waits of `0.1` seconds make approximately one second:

```text
0.1 × 10 = 1 second
```

Using smaller intervals allows the program to respond more quickly when the user pauses, resets, or stops the timer.

---

# Input Validation

The program checks that the user enters whole numbers.

For example:

```text
Enter hours: abc
```

produces:

```text
Please enter a whole number.
```

The program then asks again.

The timer also prevents a zero-duration timer:

```text
Enter hours: 0
Enter minutes: 0
Enter seconds: 0
```

The program responds:

```text
Please enter a time greater than 0.
```

---

# Alarm

When the countdown reaches:

```text
00:00:00
```

the program displays:

```text
Time's up!
```

It also uses:

```python
\a
```

which attempts to produce a terminal alert/beep.

Whether an audible beep is actually heard depends on the terminal and system settings.

---

# Learning Concepts

This project helps practice several Python concepts:

* Variables
* Functions
* Parameters
* Return values
* `input()`
* Type conversion
* `if / elif / else`
* `while` loops
* `for` loops
* Classes
* Objects
* Methods
* String formatting
* Arithmetic
* Input validation
* `threading`
* `threading.Event`
* `time.sleep()`
* Boolean conditions
* User interaction

---

# Possible Future Improvements

Some features that could be added later:

* Multiple timers
* A visual progress bar
* Custom alarm sounds
* Timer names
* Countdown percentage
* Graphical user interface (GUI)
* Saving timer settings
* Timer history
* More advanced input validation
* Separate hours/minutes/seconds display controls

---

# Author

Created as a Python learning project.
