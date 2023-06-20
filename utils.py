import json


def get_data(filepath='operations.json'):

    """
    reading file operations.json using filepath
    :param filepath:
    :return:
    """

    with open(filepath, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_filtered_data(data):

    """
    using list comprehension if key of the dict -
    state and if value of the dict - EXECUTED
    :param data:
    :return:
    """

    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


def get_last_values(data, count_last_values):

    """
    sorted key of lambda function - date and reverse it
    then use the slice of count_last_values
    :param data:
    :param count_last_values:
    :return:
    """

    data = sorted(data, key=lambda x: x["date"], reverse=True)
    data = data[:count_last_values]
    return data


def encode_bill_info(bill_info):

    """
    split string by space and use
    two slices to make two variables
    then for one of the variables
    give a condition
    :param bill_info:
    :return:
    """

    bill_info = bill_info.split()
    bill, info = bill_info[-1], " ".join(bill_info[:-1])
    if len(bill) == 16:
        bill = f"{bill[:4]} {bill[4:6]}** **** {bill[-4:]}"
    else:
        bill = f"**{bill[-4:]}"

    to = f"{info} {bill}"
    return to


def get_formatted_data(data):

    """
    creating and using a formatted list
    :param data:
    :return:
    """

    formatted_data = []
    for row in data:
        print(f"Дата: {row['date']}")
        raw_date = row["date"][:10]
        # date = "2019-08-26"
        date_in_list = raw_date.split("-")
        # date_in_list = ['2019', '08', '26']
        date = f"{date_in_list[2]}.{date_in_list[1]}.{date_in_list[0]}"
        # date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strptime("%d.%m.%Y")
        print(f"Дата: {date}")

        description = row["description"]
        print(f"Описание: {description}")

        if "from" in row:
            sender = encode_bill_info(row["from"])
            sender = f"{sender} -> "
        else:
            sender = ""

        to = encode_bill_info(row['to'])
        operations_amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{sender}{to}
{operations_amount}""")
    return formatted_data
