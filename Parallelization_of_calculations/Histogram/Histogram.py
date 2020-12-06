import random
import threading
import matplotlib.pyplot as plt

res = []    # Output list of calculated histogram - count of classified values
x = list(range(1, 17))  # X-axe values

# thread_task() function - it is called from main by different threads
# ====================================================================
def thread_task(lock, data):

    # Use first method of lock instance -> LOCK -> Block thread
    # It causes that only one thread has access to shared variables at certain moment
    # ===============================================================================
    lock.acquire()

    # Values used to classify data to corresponding collumns on histogram
    # ===================================================================
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0

    # Classification
    # ==============
    for i in range(len(data)):
        if data[i] >= 0 and data[i] < 250:
            c1 += 1
        elif data[i] >= 250 and data[i] < 500:
            c2 += 1
        elif data[i] >= 500 and data[i] < 750:
            c3 += 1
        elif data[i] >= 750 and data[i] < 1000:
            c4 += 1

    # Add amount of classified numbers to res list
    # ============================================
    res.append(c1)
    res.append(c2)
    res.append(c3)
    res.append(c4)

    # Use second method of lock instance -> RELEASE -> Free thread
    # It allows other threads to get access to shared variables at next call
    # ======================================================================
    lock.release()


if __name__ == "__main__":

    # Declaration of data table - container of random values
    # ======================================================
    data = []

    # Fill data table with 1000 random values
    # ======================================
    for i in range(1000):
        data.append(random.random() * 1000)

    # Instance of Lock -> has 2 methods "acquire" and "release"
    # I will pass this value to Thread() function as an argument to synchronize threads
    # =================================================================================
    lock = threading.Lock()

    # Array of threads
    arrayOfThreads = []

    # Call thread_task() function with lock argument and get all threads to run
    # =========================================================================
    for i in range(4):
        t = threading.Thread(target=thread_task, args=(lock, data))
        arrayOfThreads.append(t)
        t.start()

    # Call join() method on every thread
    # ==================================
    for thread in arrayOfThreads:
        thread.join()

    # Plot histogram with random data values
    # ====================================
    plt.hist(data, 100, edgecolor = 'black')
    plt.show()

    # Plot histogram with classified to 16 intervals data and show it
    # ===============================================================
    barChart = plt.bar(x, res)
    plt.show()
