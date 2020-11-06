# This is a sample Python script.
import generateRandomNumber
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    start = input();
    end = input();
    flag = input('Shall I rotate a dice? (Y/N)')

    while(flag == 'Y'):
        print(generateRandomNumber.generateRandom(start, end))
        flag = input('Shall I rotate a dice? (Y/N)')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
