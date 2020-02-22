import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)

        for filename in filenames:
            full_filename = os.path.join(dirname, filename)

            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                file_ext = os.path.splitext(full_filename)[-1]

                if file_ext == ".py":
                    print(full_filename)

    except PermissionError:
        print("Permission Error!!!")


search("/Users/tim/workspace/TUTORING/jihun/my-first-repository")
