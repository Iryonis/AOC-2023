# Question 1 :

# MAX_RED = 12
# MAX_GREEN = 13
# MAX_BLUE = 14


# def process_game_line(line):
#     game_id, game_data = line.split(":", 1)
#     game_data = [item.strip().split(",") for item in game_data.split(";")]

#     do_i_return = True
#     for list_item in game_data:
#         red, green, blue = 0, 0, 0
#         for item in list_item:
#             if "red" in item:
#                 red += int(item.replace("red", "").strip())
#             elif "green" in item:
#                 green += int(item.replace("green", "").strip())
#             else:
#                 blue += int(item.replace("blue", "").strip())
#         if red > MAX_RED or green > MAX_GREEN or blue > MAX_BLUE:
#             do_i_return = False

#     if do_i_return:
#         return int(game_id.strip("Game "))
#     else:
#         return 0


# def main():
#     total_sum = 0

#     with open("input2.txt", "r") as fichier:
#         lines = fichier.readlines()

#     for line in lines:
#         if line != "\n":
#             game_id = process_game_line(line)
#             if game_id != 0:
#                 total_sum += game_id

#     print(total_sum)


# if __name__ == "__main__":
#     main()

# Question 2 :


def process_game_line(line):
    _, game_data = line.split(":", 1)
    game_data = [item.strip().split(",") for item in game_data.split(";")]

    max_red, max_green, max_blue = 0, 0, 0
    for list_item in game_data:
        red, green, blue = 0, 0, 0
        for item in list_item:
            if "red" in item:
                red += int(item.replace("red", "").strip())
            elif "green" in item:
                green += int(item.replace("green", "").strip())
            else:
                blue += int(item.replace("blue", "").strip())
        if red > max_red:
            max_red = red
        if green > max_green:
            max_green = green
        if blue > max_blue:
            max_blue = blue

    return int(max_red) * int(max_green) * int(max_blue)


def main():
    total_sum = 0

    with open("input2.txt", "r") as fichier:
        lines = fichier.readlines()

    for line in lines:
        if line != "\n":
            total_sum += process_game_line(line)

    print(total_sum)


if __name__ == "__main__":
    main()
