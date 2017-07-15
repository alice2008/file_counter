import unittest
import shutil
import tempfile
import os
from file_counter import FileCounter

class TestFileCounter(unittest.TestCase):
	"""
	Unit test class inherits from unittest.TestCase

	Attributes:
		file_count: An instance to the test class FileCounter.
		test_dir: An temporary test root directory with all test file structure built under.
	"""

	def setUp(self):
		"""
		Setup temporary directory to the unit test for FileCounter.

		The directory setup is shown below:
		root
		+---dir1
		|    +---subdir1
		|    |   +---subsubdir1
		|    |   |    +---test1.txt
		|    |   +---test2.txt
		|    |   +---test22.txt
		|    |   +---test222.txt
		|    +---test3.txt (x)
		+---dir2
		|    +---test4.txt
		|    +---test5.txt
		|    +---test6.txt
		|	 +---test7.txt
		|    +---test8.txt
		+---test9.txt (x)
		+---test10.txt
		"""

		print "Setting up"
		self.file_counter = FileCounter()
		self.test_dir = tempfile.mkdtemp()

		test9_path = os.path.join(self.test_dir, 'test9.txt')
		self.create_txt_file(test9_path, 'Hello World!\nThis is fun tonight!\n100_TESTResult2004')
		test10_path = os.path.join(self.test_dir, 'test10.txt')
		self.create_txt_file(test10_path, 'There is something I want to say: hello!\nhey_TESTResult')

		dir1_path = os.path.join(self.test_dir, 'dir1')
		dir1_subdir1_path = os.path.join(dir1_path, 'subdir1')
		dir1_subdir1_subsubdir1_path = os.path.join(dir1_subdir1_path, 'subsubdir1')
		os.makedirs(dir1_subdir1_subsubdir1_path)

		test1_path = os.path.join(dir1_subdir1_subsubdir1_path, 'test1.txt')
		self.create_txt_file(test1_path, 'a_TESTResult_05272017\n')

		test2_path = os.path.join(dir1_subdir1_path, 'test2.txt')
		self.create_txt_file(test2_path, 'b_TESTResult_0427\nHello\njibberish')

		test2_path = os.path.join(dir1_subdir1_path, 'test22.txt')
		self.create_txt_file(test2_path, 'cd_TESTResult_0427\nHello\njibberish')

		test2_path = os.path.join(dir1_subdir1_path, 'test222.txt')
		self.create_txt_file(test2_path, 'ee_TESTResult_0427\nHello\njibberish')

		test3_path = os.path.join(dir1_path, 'test3.txt')
		self.create_txt_file(test3_path, '22_TESTRESULT_0714')

		dir2_path = os.path.join(self.test_dir, 'dir2')
		os.mkdir(dir2_path)
		test_paths = []
		for i in range(4, 9):
			test_path = os.path.join(dir2_path, 'test'+str(i)+'.txt')
			self.create_txt_file(test_path, "tt"+'_TESTResult_dir2')


	def tearDown(self):
		"""
		Temporary directory tear down after test.
		"""
		shutil.rmtree(self.test_dir)

	def create_txt_file(self, path, string):
		"""
		Create txt file with path and content of string.

		Args:
			path: os abs file path to create file.
			string: file content.

		"""
		with open(path, 'w') as f:
			f.write(string)
		return

	def test_file_counter(self):
		"""
		Test method checking the equality between expected and actual return for class FileCounter.
		"""
		expected = {
					self.test_dir:1, 
					os.path.join(self.test_dir, 'dir1'): 0, 
					os.path.join(self.test_dir, 'dir2'): 5,
					os.path.join(self.test_dir, 'dir1', 'subdir1'): 3, 
					os.path.join(self.test_dir, 'dir1', 'subdir1', 'subsubdir1'): 1}
		actual = self.file_counter.count_files_with_keywords(self.test_dir, "^[a-zA-Z]+_TESTResult.*")
		self.assertEqual(expected, actual)

if __name__ == '__main__':
	unittest.main()
