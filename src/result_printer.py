class ResultPrinter:
    def print_results(self, result_dictionary):
        message = " ".join(str(v) for v in result_dictionary.values())
        print(message)

        max_result = max(result_dictionary.values())
        percentage_list = []
        for result in result_dictionary.values():
            percentage_of_max = (result / max_result) * 100
            percentage_list.append(round(percentage_of_max, 1))

        print(*percentage_list)

        for i in reversed(range(10)):
            draw_list = []
            for percentage in percentage_list:
                percentage_dec = percentage / 10
                if i <= percentage_dec:
                    draw_list.append("1")
                elif i == 0 and percentage_dec < 0:
                    draw_list.append("1")
                else:
                    draw_list.append("0")
            print(*draw_list)