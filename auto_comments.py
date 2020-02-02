import sys
import os

def add_comments(dir, comment_file, is_head):
    comments = ""
    if os.path.isfile(comment_file):
        fcomment = open(comment_file)
        iter_f = iter(fcomment)
        for line in iter_f:
            comments = comments + line
        fcomment.close()
    comments += "\n"
    for path,subdirs,files in os.walk(dir):
        for file in files:
            file_path = os.path.join(path, file)
            if os.path.isfile(file_path):
                suffix = os.path.splitext(file_path)[-1]
                if suffix == ".h" or suffix == ".cpp" or suffix == ".hpp":
                    with open(file_path, "rb+") as f:
                        old_data = f.read()
                        f.seek(0, 0)
                        f.write(comments)
                        f.write(old_data)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("argv error.")
        os.abort()
    print(sys.argv[0])
    print(sys.argv[1])
    add_comments(sys.argv[1], sys.argv[2], True)