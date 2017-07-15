# file_counter
Return and plot all the file count with keyword under certain directory.
## Files 
* file_counter.py: FileCounter class to implement the file count function.
* file_counter_test.py: unitest to test the file count function.
## How to run
```
python file_counter_test.py
```
## Example result
![My image](https://github.com/alice2008/images/blob/master/file_counter_example.png)
## Potential Issues
* Directories has symbolic links will create loop: solved by using os.walk function.
* Duplicate files might exist due to other program reading: need to have a central hash to detect the same file
* File too big to read through line by line: might need to breakdown the file to small chunks.