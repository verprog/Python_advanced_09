class ContextManagerFile(object):
    def __init__(self, file_name, method):
        self.open_file = open(file_name, method)

    def __enter__(self):
        return self.open_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f'Error File closed - {exc_val}')
        self.open_file.close()
        return True


with ContextManagerFile('test.txt', 'w') as file:
    file.write('ContextManagerFile test with - done!')