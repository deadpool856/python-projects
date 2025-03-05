import time
import matplotlib.pyplot as plt

string = "The quick brown fox jumps over the lazy dog"
word_count = len(string.split())
border = '-+-'*10

def createbox():
    print(border)
    print()
    print('Enter the phrase as fast as possible and with accuracy')
    print()

# List to store the history of performances
history = []

while True:
    t0 = time.time()
    createbox()
    print(string, '\n')
    inputText = input()
    t1 = time.time()
    
    lengthOfInput = len(inputText.split())
    accuracy = len(set(inputText.split()) & set(string.split()))
    accuracy = (accuracy / word_count) * 100
    timeTaken = t1 - t0
    wordsperminute = (lengthOfInput / timeTaken) * 60

    # Store current performance in history
    performance = {
        'total_words': lengthOfInput,
        'time_used': round(timeTaken, 2),
        'wpm': round(wordsperminute, 2),
        'accuracy': round(accuracy, 2)
    }
    history.append(performance)

    # Showing results now
    print('Total words \t:', lengthOfInput)
    print('Time used \t:', round(timeTaken, 2), 'seconds')
    print('Your typing speed \t:', round(wordsperminute, 2), 'words per minute')
    print('Accuracy \t:', round(accuracy, 2), '%')
    print(border)

    # Display history
    print("Performance History:")
    for i, perf in enumerate(history, start=1):
        print(f"{i}. Total words: {perf['total_words']}, Time used: {perf['time_used']} seconds, WPM: {perf['wpm']}, Accuracy: {perf['accuracy']}%")
    print(border)

    # Option to try again or exit
    try_again = input("Do you want to try again? (yes/no): ").strip().lower()
    if try_again != 'yes':
        break

# Plotting the performance history
wpm_history = [perf['wpm'] for perf in history]
accuracy_history = [perf['accuracy'] for perf in history]
trials = list(range(1, len(history) + 1))

plt.figure(figsize=(10, 5))

# Plot WPM
plt.subplot(1, 2, 1)
plt.plot(trials, wpm_history, marker='o')
plt.title('Typing Speed Over Time')
plt.xlabel('Trial')
plt.ylabel('Words Per Minute (WPM)')
plt.grid(True)

# Plot Accuracy
plt.subplot(1, 2, 2)
plt.plot(trials, accuracy_history, marker='o', color='orange')
plt.title('Accuracy Over Time')
plt.xlabel('Trial')
plt.ylabel('Accuracy (%)')
plt.grid(True)

plt.tight_layout()
plt.show()
