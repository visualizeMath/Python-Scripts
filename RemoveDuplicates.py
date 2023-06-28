import os
import hashlib

def find_duplicates(path):
    # Create a dictionary to store the file hashes and paths
    hashes = {}
    total_size = 0
    count = 0

    # Loop over all the files in the directory and its subdirectories
    for root, dirs, files in os.walk(path):
        for filename in files:
            # Get the full path of the file
            filepath = os.path.join(root, filename)

            # Open the file and read its contents
            with open(filepath, 'rb') as f:
                contents = f.read()

            # Generate a hash of the file contents
            file_hash = hashlib.md5(contents).hexdigest()

            # If the hash is already in the dictionary, it's a duplicate
            if file_hash in hashes:
                duplicate_size = os.path.getsize(filepath)
                total_size += duplicate_size
                duplicate_sizeInKB=round(duplicate_size/1048576,2)
                print(f'Duplicate found: {filepath} (duplicate of {hashes[file_hash]}), size: {duplicate_sizeInKB} MB')
                os.remove(filepath)
                count += 1
            else:
                hashes[file_hash] = filepath
    totalSizeInKB=round(total_size/1048576,2)
    print('\n')
    print(f'\t\t {count} files removed..')
    print('\n')
    print(f'\t\tTotal size of all deleted duplicates: {totalSizeInKB} MB')
    

if __name__ == '__main__':
    # Ask the user for the path of the directory to search
    path = input('Enter the path of the directory to search: ')
    print('\n')

    # Call the function to find duplicates
    find_duplicates(path)
    a=input('\n\t\t ---- COMPLETED! ----- Press Enter to exit ...')
