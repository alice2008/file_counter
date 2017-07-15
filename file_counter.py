import re
import os
from textwrap import wrap
import matplotlib.pyplot as plt


class FileCounter(object):
    def __init__(self):
        pass

    def count_files_with_keywords(self, root_dir, keyword):
        """ Return all the file counts has keyword.

        Recursively walk through the directories under root_dir
        to find the all the files contains 'keyword'.

        Args:
            root_dir: Root directory to start search all files have keyword.
            keyword: A String in regular expression form.

        Returns:
            A dict mapping keys to the directory abs path under root_dir. Each
            value is the number of files in such directory contain keyword pattern.
            Example:

            {'/a': 1, '/a/b': 2, '/a/b/c': 3}
        """
        res = {}
        if not os.path.isdir(root_dir):
            print "ERROR: %s is not a valid directory!".format(root_dir)
            return res
        pattern = re.compile(keyword)
        for root, dirs, files in os.walk(root_dir):
            count = 0
            for f in files:
                if self.check_keyword(os.path.join(root, f), pattern):
                    count += 1
            res[root] = count
        self.plot_graph(res, keyword)
        return res

    def check_keyword(self, path, pattern):
        """
        Check file contains pattern in regular expression.

        Args:
            path: os abs file path to retrieve the file.
            pattern: an re compile pattern to do the match.

        Return:
            Boolean value based on whether match found or not in the file.
        """
        with open(path, 'r') as f:
            for line in f:
                if pattern.search(line):
                    return True
        return False

    def plot_graph(self, file_count, keyword):
        """
        Plot graph from dictionary file_count with title using keyword.

        Args:
            file_count: A dict with keys of directory abs path, values of file count with keyword.
            keyword: A string in regular expression form.

        Return:
            Nothing. An bar chart popped up with X-axis is the list of directories, Y-axis is the
            count of files with keyword.S

        """
        if not file_count:
            print "Did not find any match. Exiting..."
            return
        plt.bar(range(len(file_count)), file_count.values(), 0.4, align='center', alpha=0.5)
        plt.xlabel('Directory Names')
        plt.ylabel('Keyword Count')
        plt.title('Count of pattern: %s' % keyword)
        max_count = max(file_count.values())+1
        x_labels = ['\n'.join(wrap(line, 15)) for line in file_count.keys()]
        plt.xticks(range(len(file_count)), x_labels, size=10)
        plt.yticks(range(0, max_count))
        plt.tight_layout()
        plt.show()
        return
