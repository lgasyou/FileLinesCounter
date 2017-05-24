import os


class FileLinesCounter:
    def __init__(self):
        self.selected_file_extensions = \
            input("Please input file name extension. Leave empty will be [.cpp, .c, .h, .hpp, .py, .java]").split() or \
            [".cpp", ".c", ".h", ".hpp", ".py", ".java"]
        self.filters = \
            input("Please input strings which will not be included. Leave empty will be [moc_, ui_]").split() or \
            ["moc_", "ui_"]

    def count_single_file_lines(self, absolute_path):
        # this program only cares about '\n', so it's no need to consider errors of converting.
        with open(absolute_path, 'r', encoding="utf-8", errors="ignore") as file:
            lines_count = 0
            while file.readline():
                lines_count += 1
            return lines_count

    def process_each_file(self, root, file_name):
        lines_count = 0
        absolute_path = os.path.join(root, file_name)
        file_extension = os.path.splitext(absolute_path)
        if file_extension[1] in self.selected_file_extensions:
            for selector in self.filters:
                if selector in file_name:
                    break
            else:
                lines_count = self.count_single_file_lines(absolute_path)
                print("{:<80} {}".format(absolute_path, lines_count), sep='\t')
        return lines_count

    def run(self):
        total_lines_count = 0
        for root, dirs, files in os.walk("."):
            for file_name in files:
                total_lines_count += self.process_each_file(root, file_name)

        print("total lines:", total_lines_count)


if __name__ == '__main__':
    FileLinesCounter().run()
