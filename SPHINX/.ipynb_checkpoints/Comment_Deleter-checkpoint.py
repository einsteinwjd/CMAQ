

import os
import glob

def comment_deleter(path):
    '''
    inputs
        path (string): A single path to a text file with a relative links section, to be deleted
    
    '''
    starts = []
    ends = []
    # open the file and read in the data line-by-line
    with open(path, 'r') as file:
        lines = file.readlines()
    # parse the lines to determine the section of lines
    # used for labeling relative links
    for i in range(len(lines)):
        if '<!--' in lines[i] and '-->' in lines[i]:
            pass
        elif '<!--' in lines[i] and '-->' not in lines[i]:
            starts.append(i)
        elif 'END_OF_COMMENT' in lines[i]:
            ends.append(i)
            
    if len(starts) >= 1:
        assert len(starts) == len(ends), "Comment Parsing error, unequal comment begins and endings in: " + path + str(len(starts)) + str(len(ends))
        
        try:
            for i in range(len(starts)):
            # edit the relative links section data in access memory
                lines[starts[i]:starts[i]+1] = ' '
                lines[ends[i]:ends[i]+2] = ' '
            with open(path, 'w') as file:
                file.writelines(lines)
            # close file
            file.close()
            # print file has been edited
            print(str(len(starts)) + ' comment(s) removed from: ', path)
        
        except:
            file.close()
        
        
## See FY23-26 Release OneNote for decision details, or contact Kristen/Fahim above.
## INPUT FOLDER PATHS HERE - all markdown that will have HTML built from it in source/
folder_list = ['./source/', './source/DOCS/',
               './source/DOCS/Users_Guide/', './source/DOCS/Release_FAQ/',
               './source/DOCS/Release_Notes/', './source/DOCS/Developers_Guide/',
               './source/DOCS/Users_Guide/Tutorials/',
               './source/DOCS/Users_Guide/Appendix'
              ]
file_list = []
## append all .md files in listed folders to list
for folder in folder_list:
    for file in glob.glob(os.path.join(folder, '*.md')):
        file_list.append(file)

## Iterate through list and make edits
for file in file_list:
    comment_deleter(file)

print('Comments Deleted -- Success')