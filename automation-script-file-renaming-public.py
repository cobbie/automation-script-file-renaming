import os
orig_dir = # input directory path here

# change directory to specified orig_dir
os.chdir(orig_dir)
print(os.getcwd())

# set counter for number of files
num_files = 0

# iterates through every directory in orig_dir
for dir_f in os.listdir():
    if os.path.isdir(dir_f) is True:
        # changes directory and iterates through each of their files, making the necessary changes
        os.chdir(orig_dir + '/' + dir_f)
        for f_in_dir in os.listdir():
            num_files += 1
            f_name, f_ext = os.path.splitext(f_in_dir)
            if f_ext == '.srt' and f_name[:4] != 'sub_':
                new_f_name = 'sub_' + f_in_dir
            else:
                new_f_name = f_in_dir
            os.rename(f_in_dir, new_f_name)

        # switches back to orig_dir to be able to go through the next directory
        os.chdir(orig_dir)
print(num_files)
