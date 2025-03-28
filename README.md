# TYPING SPEED TEST
#### Video Demo: <https://youtu.be/vh8M1nQqb-E>
#### Description:
This typing speed test project allows users to evaluate their typing speed and accuracy.The program prompts the user thier name and then to select a word count. The user then types the displayed text, and the program calculates:
- WPM (Words Per Minute): This measures the typing speed based on the no.of words and the time taken.
- Accuracy percentage: Compares the original text to the typed text and evaluates the accuracy of the typed text.

### Features:
WORD LENGTH - After entering your name, the user is asked to select one of the following options(A,B,C,D)[case-insensitive].

WORD GENERATION - A file called "words.txt" in this same folder contains 500 most common english words and from this file, based on the selected number of words at the beginning, the application generates that many number of words randomly.

EVALUATING TIME DIFFERENCE - As soon as the user types "yes"(case-insenstive) to start the test, the current time is tracked and as soon as the user presses enter after typing the text, the current time is tracked again and the time duration is calculated.

CALCULATING WPM - To calculate WPM total number of words is divided by time duration(in minutes).

ACCURACY - Typed text is compared to the original text and the percentage of the corrected letters in the whole text is calculated.

ERROR AND RESTART OPTIONS - If the user types invalid input anywhere, the input is prompted again. Also if accuracy falls below 50%, the user can choose to retake the test.

DATA HANDLING - The name, WPM and accuracy is stored in a csv file called "score.csv".

TESTING THE PROJECT - A file called "test_project.py" contains functions which tests the functions in the file "project.py".

### Modules Used:
- datetime: For tracking start and end time to calculate typing duration.
- csv: To store and manage user results.
- random: To select words randomly from a list.
- sys: To exit the code.

### Usage:
1. Run the program.
2. Enter your name.
3. Choose the number of words for the test.
4. Type yes(case-insensitive) to start the test.
5. Start typing the displayed text when prompted.
6. After typing the displayed text press enter.
7. View your WPM and accuracy results at the end.
8. Your name, WPM and Accuracy will also be displayed in the file called "score.csv".
