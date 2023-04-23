import re
import matplotlib.pyplot as plt


def calculate_moving_average(array_list, window_size):
    moving_averages = []
    for i in range(len(array_list)):
        start_index = max(0, i - window_size + 1)
        end_index = i + 1
        window = array_list[start_index:end_index]
        average = sum(window) / len(window)
        moving_averages.append(average)
    return moving_averages


def main():
    file_name = "iSAID.out.rtf"
    file = open(file_name, "r")

    iterations = []
    total_loss = []

    for raw_data in file:
        data = re.split("[\:\s]\s+", raw_data)
        # print(data)

        iterations.append(int(data[4]))
        total_loss.append(float(data[6]))

    smoothed_losses = calculate_moving_average(total_loss, 10)

    plt.plot(iterations, smoothed_losses)
    plt.xlabel("Iterations")
    plt.ylabel("Total Losses")
    plt.show()


if __name__ == "__main__":
    main()
