import pandas as pd
import csv


def create_item():
    name = input('name of the art: ')
    year = input('the year of the art: ')
    value = input('the price of the art: ')
    item_info = [name, year, value]
    for compared_item in museum_items:
        if item_info[0] == compared_item[0]:
            return None
    return item_info


def show_item():
    data = pd.read_csv("museum.csv")
    print(data)


def delete_item():
    delete_stuff = input("What do you want to delete? ")
    index = 0
    for items in museum_items:
        if items[0] == delete_stuff:
            museum_items.pop(index)
            break
        index += 1
        data = pd.read_csv("museum.csv")
        data = data.iloc[index]
        print(data)


def update_item():
    update_stuff = input("What do you want to modify? ")
    for items in museum_items:
        if items[0] == update_stuff:
            items[0] = input(f'{items[0]} : ')
            items[1] = input(f'{items[1]} : ')
            items[2] = input(f'{items[2]} : ')
            print(f'{items[0]}' + f'{items[1]}' + f'{items[2]} ' 'update!')
            break


if __name__ == "__main__":
    museum_items = []
    item_title = ['name', 'year', 'value']
    is_alive = True
    print("Hi, how are you? what can I do for you today? :) ")
    while is_alive:
        print("press 1 to add item")
        print("press 2 to show items")
        print("press 3 to delete item")
        print("press 4 to update item")
        print("press q to exit")
        x = input()
        if x == '1':
            new_item = create_item()
            if new_item is not None:
                museum_items.append(new_item)
                print(new_item)
                with open('museum.csv', 'a') as f:
                    write = csv.writer(f)
                    write.writerow(item_title)
                    write.writerows(museum_items)
                    f.close()
            else:
                print('we already have the same item :) ')
        elif x == '2':
            show_item()
        elif x == '3':
            delete_item()
        elif x == '4':
            update_item()
            with open('museum.csv', 'w') as f:
                write = csv.writer(f)
                write.writerow(museum_items)
                f.close()
        elif x == 'q':
            print('see you next time!')
            is_alive = False
